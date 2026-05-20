"""GitHub PR helpers via the `gh` CLI."""

from __future__ import annotations

import subprocess
from pathlib import Path


class GhError(Exception):
    pass


def _run(args: list[str], cwd: Path, check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(args, cwd=str(cwd), check=check, text=True, capture_output=True)


def gh_authed(repo: Path, gh_bin: str = "gh") -> bool:
    r = _run([gh_bin, "auth", "status"], cwd=repo, check=False)
    return r.returncode == 0


def create_pr(
    repo: Path,
    base: str,
    head: str,
    title: str,
    body: str,
    gh_bin: str = "gh",
) -> str:
    """Open PR. Returns PR URL."""
    r = _run(
        [
            gh_bin, "pr", "create",
            "--base", base,
            "--head", head,
            "--title", title,
            "--body", body,
        ],
        cwd=repo,
    )
    return r.stdout.strip().splitlines()[-1]


def add_label(repo: Path, pr_url: str, label: str, gh_bin: str = "gh") -> None:
    _run([gh_bin, "pr", "edit", pr_url, "--add-label", label], cwd=repo, check=False)


def enable_auto_merge(
    repo: Path,
    pr_url: str,
    strategy: str = "squash",
    gh_bin: str = "gh",
) -> None:
    """`gh pr merge --auto --<strategy>` — waits for required checks."""
    flag = {"squash": "--squash", "merge": "--merge", "rebase": "--rebase"}[strategy]
    _run([gh_bin, "pr", "merge", pr_url, "--auto", flag], cwd=repo)
