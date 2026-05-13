#!/usr/bin/env python3
"""PreToolUse:Bash + PreToolUse:Write guard.

Blocks shell commands and file writes that mutate raw/ or INBOX/. The raw
layer is human-authored and immutable to Claude. Allows reads, allows
`git mv INBOX/... raw/...` (the ingest move), allows everything outside
the immutable trees.

Hook contract: read JSON payload from stdin, exit 0 to allow, exit 2 to
block. stderr is shown to the agent.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

IMMUTABLE_PREFIXES = ("raw/", "INBOX/")

# Wiki-layer tooling needs to write specific paths inside INBOX/. Everything
# else under INBOX/ stays immutable to Claude.
ALLOWED_WRITES_UNDER_INBOX = (
    "INBOX/README.md",
    "INBOX/converted/",
)

ALLOW_BASH = [
    re.compile(r"^\s*git\s+(status|log|diff|show|blame|branch|fetch|pull|remote)\b"),
    re.compile(r"^\s*git\s+mv\s+INBOX/"),  # ingest move from INBOX to raw/
    re.compile(r"^\s*(ls|find|grep|rg|cat|less|head|tail|wc|stat|file|du)\b"),
    re.compile(r"^\s*cd\s+tools\s+&&"),  # lint runner
    re.compile(r"^\s*mkdir\s+-p\s+(wiki|tools|scripts|docs|INBOX|\.claude)"),
    re.compile(r"^\s*echo\b"),
    re.compile(r"^\s*python3?\s+-c\b"),
    re.compile(r"^\s*uv\s+(venv|pip|run|sync)\b"),
    re.compile(r"^\s*chmod\s+\+x\s+(scripts|\.claude)/"),
]

DENY_BASH = [
    re.compile(r"\b(rm|mv|cp|sed|awk|tee|truncate)\b[^|]*\b(raw|INBOX)/"),
    re.compile(r">\s*(raw|INBOX)/"),  # redirect into raw/
    re.compile(r"^\s*git\s+(reset\s+--hard|clean\s+-fd|push\s+--force)\b"),
]


def _check_bash(payload: dict) -> int:
    cmd: str = payload.get("toolInput", {}).get("command", "")
    for allow in ALLOW_BASH:
        if allow.search(cmd):
            return 0
    for deny in DENY_BASH:
        if deny.search(cmd):
            print(
                f"guard_immutable: blocked '{cmd}' — raw/ and INBOX/ are immutable.",
                file=sys.stderr,
            )
            return 2
    return 0


def _check_write(payload: dict) -> int:
    file_path = payload.get("toolInput", {}).get("file_path", "")
    if not file_path:
        return 0
    repo = Path.cwd()
    try:
        rel = Path(file_path).resolve().relative_to(repo)
    except ValueError:
        return 0  # outside the repo, not our concern
    rel_str = str(rel)
    for allowed in ALLOWED_WRITES_UNDER_INBOX:
        if rel_str == allowed or rel_str.startswith(allowed):
            return 0
    for prefix in IMMUTABLE_PREFIXES:
        if rel_str.startswith(prefix):
            print(
                f"guard_immutable: blocked Write to '{rel_str}' — immutable tree.",
                file=sys.stderr,
            )
            return 2
    return 0


def main() -> int:
    payload = json.load(sys.stdin)
    tool = payload.get("toolName", "")
    if tool == "Bash":
        return _check_bash(payload)
    if tool in ("Write", "Edit", "NotebookEdit"):
        return _check_write(payload)
    return 0


if __name__ == "__main__":
    sys.exit(main())
