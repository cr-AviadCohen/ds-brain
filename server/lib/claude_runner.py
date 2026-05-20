"""Wrapper for `claude -p` headless invocation."""

from __future__ import annotations

import subprocess
from pathlib import Path


class ClaudeError(Exception):
    pass


def run_slash(
    claude_bin: str,
    command: str,
    arg: str,
    cwd: Path,
    permission_mode: str = "bypassPermissions",
    timeout_seconds: int = 1800,
    model: str | None = None,
) -> tuple[int, str, str]:
    """Invoke `claude -p "/<command> <arg>"`. Returns (rc, stdout, stderr).

    If `model` is non-empty, passes `--model <model>` so the per-job model
    config in server/config.yaml is honoured.
    """
    prompt = f"/{command} {arg}".rstrip()
    args = [
        claude_bin,
        "-p", prompt,
        "--permission-mode", permission_mode,
    ]
    if model:
        args += ["--model", model]
    try:
        r = subprocess.run(
            args,
            cwd=str(cwd),
            text=True,
            capture_output=True,
            timeout=timeout_seconds,
        )
        return r.returncode, r.stdout, r.stderr
    except subprocess.TimeoutExpired as e:
        raise ClaudeError(f"claude -p timed out after {timeout_seconds}s") from e
