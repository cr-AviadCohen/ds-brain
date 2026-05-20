"""Auto-ingest entry point.

Flow per fire (5-min systemd timer):
  1. Acquire mutex.
  2. Verify on branch `unified`, tree clean.
  3. `git pull --ff-only origin unified`.
  4. List INBOX/ pending files (filter ignore patterns).
  5. For each pending file:
       a. Content-hash → ledger lookup; skip if already processed.
       b. `git checkout -b auto-ingest/<ts>-<short-sha>` from unified.
       c. Invoke `claude -p "/auto-ingest <path>"`.
       d. Inspect resulting diff vs base unified:
            - file count cap
            - line count cap
            - path allowlist
          Exceed any → push branch + open PR with `needs-review` label,
          skip auto-merge.
          Else → push branch + open PR + `--auto --squash`.
       e. Record hash in ledger.
       f. Checkout unified, delete local bot branch.
  6. Release mutex.

Idempotent. Crash-safe: ledger updates after PR open, so a crash mid-
ingest just retries the file next fire (Claude session was wasted but
no double-commit).
"""

from __future__ import annotations

import datetime as dt
import fnmatch
import sys
import traceback
from pathlib import Path

# Make `server/` importable when invoked via `uv run python jobs/auto_ingest.py`.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from lib import config as cfg_mod
from lib import git_safe, pr as pr_mod
from lib.claude_runner import run_slash, ClaudeError
from lib.ledger import Ledger, sha256_of
from lib.logging import Logger
from lib.mutex import LockBusy, Mutex


REPO_ROOT = Path(__file__).resolve().parents[2]


def list_pending(inbox_dir: Path, ignore: list[str]) -> list[Path]:
    if not inbox_dir.exists():
        return []
    out: list[Path] = []
    for entry in sorted(inbox_dir.iterdir()):
        name = entry.name
        if any(fnmatch.fnmatch(name, pat) for pat in ignore):
            continue
        if not entry.is_file():
            # Future: support dirs (e.g. raw/projects/foo bundles)
            continue
        out.append(entry)
    return out


def bot_branch_name(prefix: str, short_sha: str) -> str:
    ts = dt.datetime.now(dt.timezone.utc).strftime("%Y%m%d-%H%M%S")
    return f"{prefix}/{ts}-{short_sha}"


def short_description(file_path: Path) -> str:
    return file_path.stem.replace("_", " ").replace("-", " ")[:80]


def process_one(
    file: Path,
    cfg: cfg_mod.Config,
    logger: Logger,
    ledger: Ledger,
) -> None:
    rel = file.relative_to(REPO_ROOT)
    content_hash = sha256_of(file)

    if ledger.has(content_hash):
        logger.log(f"skip (ledger hit): {rel}")
        return

    base_sha = git_safe.short_sha(REPO_ROOT)
    branch = bot_branch_name(cfg.bot_branch_prefix, base_sha)
    logger.log(f"begin: {rel} → branch {branch}")

    git_safe.checkout_new_branch(REPO_ROOT, branch)
    try:
        rc, out, err = run_slash(
            claude_bin=cfg.claude_bin,
            command=cfg.claude_command,
            arg=str(rel),
            cwd=REPO_ROOT,
            permission_mode=cfg.claude_permission_mode,
            timeout_seconds=cfg.claude_timeout_seconds,
        )
        if rc != 0:
            logger.log(f"claude rc={rc}: {rel} — stderr tail: {err[-500:]}")
            git_safe.checkout(REPO_ROOT, cfg.branch)
            git_safe.delete_local_branch(REPO_ROOT, branch)
            return

        n_files, n_lines, paths = git_safe.diff_against(REPO_ROOT, cfg.branch)
        if n_files == 0:
            logger.log(f"noop (no diff): {rel} — recording ledger hit anyway")
            ledger.record(content_hash, str(rel), pr_url=None)
            git_safe.checkout(REPO_ROOT, cfg.branch)
            git_safe.delete_local_branch(REPO_ROOT, branch)
            return

        in_allow, offenders = git_safe.paths_within_allowlist(paths, cfg.path_allowlist)
        cap_exceeded = (
            n_files > cfg.max_files_changed
            or n_lines > cfg.max_lines_changed
            or not in_allow
        )

        git_safe.push_branch(REPO_ROOT, cfg.remote, branch)

        desc = short_description(file)
        title = f"{cfg.pr_title_prefix}{desc}"
        body_lines = [
            f"Auto-ingest of `{rel}`.",
            "",
            f"- files changed: {n_files}",
            f"- lines changed: {n_lines}",
            f"- content sha256: `{content_hash}`",
        ]
        if cap_exceeded:
            body_lines += [
                "",
                "**Caps exceeded — auto-merge disabled.**",
                f"- max_files: {cfg.max_files_changed} (got {n_files})",
                f"- max_lines: {cfg.max_lines_changed} (got {n_lines})",
            ]
            if offenders:
                body_lines.append(
                    f"- path allowlist violations: {offenders[:20]}"
                )

        pr_url = pr_mod.create_pr(
            repo=REPO_ROOT,
            base=cfg.branch,
            head=branch,
            title=title,
            body="\n".join(body_lines),
            gh_bin=cfg.gh_bin,
        )

        if cap_exceeded:
            pr_mod.add_label(REPO_ROOT, pr_url, cfg.pr_needs_review_label, gh_bin=cfg.gh_bin)
            logger.log(f"needs-review: {rel} → {pr_url}")
        else:
            if cfg.pr_auto_merge:
                pr_mod.enable_auto_merge(
                    REPO_ROOT, pr_url, strategy=cfg.pr_merge_strategy, gh_bin=cfg.gh_bin
                )
                logger.log(f"auto-merge enabled: {rel} → {pr_url}")
            else:
                logger.log(f"PR opened (manual merge): {rel} → {pr_url}")

        ledger.record(content_hash, str(rel), pr_url=pr_url)
    finally:
        # Always end on unified, regardless of branch state. Best-effort.
        try:
            git_safe.checkout(REPO_ROOT, cfg.branch)
        except Exception:
            pass
        git_safe.delete_local_branch(REPO_ROOT, branch)


def main() -> int:
    cfg = cfg_mod.load()
    logger = Logger(cfg.log_dir / "auto_ingest.log", trim_lines=cfg.log_trim_lines)
    mutex = Mutex(cfg.lock_dir, stale_seconds=cfg.mutex_stale_seconds)
    ledger = Ledger(cfg.ledger_path)

    try:
        mutex.acquire("auto_ingest")
    except LockBusy:
        logger.log("skip: lock busy")
        return 0

    try:
        branch = git_safe.current_branch(REPO_ROOT)
        if branch != cfg.branch:
            logger.log(f"skip: branch is '{branch}', not '{cfg.branch}'")
            return 0
        if not git_safe.is_clean(REPO_ROOT):
            logger.log("skip: working tree dirty")
            return 0

        try:
            result = git_safe.ff_pull(REPO_ROOT, cfg.remote, cfg.branch)
            if result == "fast-forwarded":
                logger.log("git: fast-forwarded")
        except git_safe.GitError as e:
            logger.log(f"git pull failed: {e}")
            return 1

        pending = list_pending(cfg.inbox_dir, cfg.inbox_ignore)
        if not pending:
            return 0

        for file in pending:
            try:
                process_one(file, cfg, logger, ledger)
            except Exception as e:
                logger.log(f"error processing {file.name}: {e}\n{traceback.format_exc()}")
                # Continue to next file. Ledger NOT updated → retry next fire.
                continue
        return 0
    finally:
        mutex.release()


if __name__ == "__main__":
    sys.exit(main())
