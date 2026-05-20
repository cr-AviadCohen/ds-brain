"""Auto-lint entry point.

Flow per fire (weekly systemd calendar timer, default Sun 03:00):
  1. Acquire shared mutex (same lock_dir as auto_ingest — never run concurrently).
  2. Verify on branch `unified`, tree clean.
  3. `git pull --ff-only origin unified`.
  4. Create bot branch `auto-lint/<ts>-<short-sha>` from unified.
  5. Invoke `claude -p "/auto-lint"` (model per config — defaults to Sonnet).
  6. Inspect resulting diff vs unified:
       - file count cap
       - line count cap
       - path allowlist (default: wiki/** only)
     Exceed any → push + open PR with `needs-review` label.
     Else → push + open PR + `--auto --squash`.
  7. No-diff (lint had nothing to do) → cleanup, exit 0.
  8. Checkout unified, delete local bot branch.
  9. Release mutex.

No ledger — lint is idempotent on its own; an extra fire that finds the
same issues already fixed by the previous run produces a no-diff and
skips PR creation.
"""

from __future__ import annotations

import datetime as dt
import sys
import traceback
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from lib import config as cfg_mod
from lib import git_safe, pr as pr_mod
from lib.claude_runner import run_slash
from lib.logging import Logger
from lib.mutex import LockBusy, Mutex


REPO_ROOT = Path(__file__).resolve().parents[2]


def bot_branch_name(prefix: str, short_sha: str) -> str:
    ts = dt.datetime.now(dt.timezone.utc).strftime("%Y%m%d-%H%M%S")
    return f"{prefix}/{ts}-{short_sha}"


def run_lint(
    cfg: cfg_mod.Config,
    job: cfg_mod.JobConfig,
    logger: Logger,
) -> None:
    base_sha = git_safe.short_sha(REPO_ROOT)
    branch = bot_branch_name(job.bot_branch_prefix, base_sha)
    logger.log(f"begin: lint → branch {branch} (model={job.model or 'default'})")

    git_safe.checkout_new_branch(REPO_ROOT, branch)
    try:
        rc, out, err = run_slash(
            claude_bin=cfg.claude_bin,
            command=job.claude_command,
            arg="",  # /auto-lint takes no args
            cwd=REPO_ROOT,
            permission_mode=cfg.claude_permission_mode,
            timeout_seconds=cfg.claude_timeout_seconds,
            model=job.model,
        )
        if rc != 0:
            logger.log(f"claude rc={rc}: lint — stderr tail: {err[-500:]}")
            return

        n_files, n_lines, paths = git_safe.diff_against(REPO_ROOT, cfg.branch)
        if n_files == 0:
            logger.log("clean: lint produced no changes")
            return

        in_allow, offenders = git_safe.paths_within_allowlist(paths, job.path_allowlist)
        cap_exceeded = (
            n_files > job.max_files_changed
            or n_lines > job.max_lines_changed
            or not in_allow
        )

        git_safe.push_branch(REPO_ROOT, cfg.remote, branch)

        ts = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d")
        title = f"{job.pr_title_prefix}{ts}"
        body_lines = [
            f"Weekly auto-lint run.",
            "",
            f"- files changed: {n_files}",
            f"- lines changed: {n_lines}",
            f"- model: `{job.model or 'default'}`",
        ]
        if cap_exceeded:
            body_lines += [
                "",
                "**Caps exceeded — auto-merge disabled.**",
                f"- max_files: {job.max_files_changed} (got {n_files})",
                f"- max_lines: {job.max_lines_changed} (got {n_lines})",
            ]
            if offenders:
                body_lines.append(f"- path allowlist violations: {offenders[:20]}")

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
            logger.log(f"needs-review: lint → {pr_url}")
        else:
            if cfg.pr_auto_merge:
                pr_mod.enable_auto_merge(
                    REPO_ROOT, pr_url, strategy=cfg.pr_merge_strategy, gh_bin=cfg.gh_bin
                )
                logger.log(f"auto-merge enabled: lint → {pr_url}")
            else:
                logger.log(f"PR opened (manual merge): lint → {pr_url}")
    finally:
        try:
            git_safe.checkout(REPO_ROOT, cfg.branch)
        except Exception:
            pass
        git_safe.delete_local_branch(REPO_ROOT, branch)


def main() -> int:
    cfg = cfg_mod.load()
    job = cfg.auto_lint
    if not job.enabled:
        return 0

    logger = Logger(cfg.log_dir / "auto_lint.log", trim_lines=cfg.log_trim_lines)
    mutex = Mutex(cfg.lock_dir, stale_seconds=cfg.mutex_stale_seconds)

    try:
        mutex.acquire("auto_lint")
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

        try:
            run_lint(cfg, job, logger)
        except Exception as e:
            logger.log(f"error during lint: {e}\n{traceback.format_exc()}")
            return 1
        return 0
    finally:
        mutex.release()


if __name__ == "__main__":
    sys.exit(main())
