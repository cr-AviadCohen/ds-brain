"""Safe git operations: ff-only pull, branch ops, diff inspection."""

from __future__ import annotations

import fnmatch
import subprocess
from pathlib import Path


class GitError(Exception):
    pass


def _run(args: list[str], cwd: Path, check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        args,
        cwd=str(cwd),
        check=check,
        text=True,
        capture_output=True,
    )


def current_branch(repo: Path) -> str:
    r = _run(["git", "rev-parse", "--abbrev-ref", "HEAD"], cwd=repo)
    return r.stdout.strip()


def is_clean(repo: Path) -> bool:
    r = _run(["git", "status", "--porcelain"], cwd=repo)
    return r.stdout.strip() == ""


def fetch(repo: Path, remote: str, branch: str) -> None:
    _run(["git", "fetch", "--quiet", remote, branch], cwd=repo)


def ff_pull(repo: Path, remote: str, branch: str) -> str:
    """Fast-forward only. Returns 'up-to-date' | 'fast-forwarded' | raises."""
    fetch(repo, remote, branch)
    local = _run(["git", "rev-parse", "HEAD"], cwd=repo).stdout.strip()
    upstream = _run(["git", "rev-parse", f"{remote}/{branch}"], cwd=repo).stdout.strip()
    if local == upstream:
        return "up-to-date"
    anc = _run(
        ["git", "merge-base", "--is-ancestor", local, upstream],
        cwd=repo,
        check=False,
    )
    if anc.returncode != 0:
        raise GitError(
            f"diverged: local={local} remote={upstream} — manual resolution required"
        )
    _run(["git", "merge", "--ff-only", "--quiet", f"{remote}/{branch}"], cwd=repo)
    return "fast-forwarded"


def checkout_new_branch(repo: Path, name: str) -> None:
    _run(["git", "checkout", "-b", name], cwd=repo)


def checkout(repo: Path, name: str) -> None:
    _run(["git", "checkout", name], cwd=repo)


def push_branch(repo: Path, remote: str, branch: str, set_upstream: bool = True) -> None:
    args = ["git", "push"]
    if set_upstream:
        args += ["-u"]
    args += [remote, branch]
    _run(args, cwd=repo)


def diff_against(repo: Path, base_ref: str) -> tuple[int, int, list[str]]:
    """Return (files_changed, lines_changed, file_paths) vs base_ref."""
    r = _run(["git", "diff", "--numstat", f"{base_ref}...HEAD"], cwd=repo)
    files: list[str] = []
    total_lines = 0
    for line in r.stdout.strip().splitlines():
        parts = line.split("\t")
        if len(parts) != 3:
            continue
        added, removed, path = parts
        # Binary files report "-".
        if added != "-":
            total_lines += int(added)
        if removed != "-":
            total_lines += int(removed)
        files.append(path)
    return len(files), total_lines, files


def paths_within_allowlist(paths: list[str], allowlist: list[str]) -> tuple[bool, list[str]]:
    """Return (all_match, offenders)."""
    offenders: list[str] = []
    for p in paths:
        if not any(fnmatch.fnmatch(p, pat) for pat in allowlist):
            offenders.append(p)
    return len(offenders) == 0, offenders


def short_sha(repo: Path) -> str:
    return _run(["git", "rev-parse", "--short", "HEAD"], cwd=repo).stdout.strip()


def delete_local_branch(repo: Path, name: str) -> None:
    _run(["git", "branch", "-D", name], cwd=repo, check=False)
