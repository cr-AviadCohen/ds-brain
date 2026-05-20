#!/usr/bin/env python3
"""SessionStart hook.

If INBOX/ contains any pending file (anything that is not README.md and not
a dotfile), emit a `SessionStart` hook payload telling Claude to run
`/ingest`. Otherwise exit silently.

No external deps (stdlib only — replaces previous bash + jq version).
"""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path


IGNORE_EXACT = {"README.md"}


def list_pending(inbox_dir: Path) -> list[str]:
    if not inbox_dir.is_dir():
        return []
    out: list[str] = []
    for entry in sorted(inbox_dir.iterdir()):
        name = entry.name
        if name.startswith("."):
            continue
        if name in IGNORE_EXACT:
            continue
        out.append(name)
    return out


def main() -> int:
    project_dir = os.environ.get("CLAUDE_PROJECT_DIR", ".")
    inbox_dir = Path(project_dir) / "INBOX"

    pending = list_pending(inbox_dir)
    if not pending:
        return 0

    files_block = "\n".join(pending)
    message = (
        f"INBOX has {len(pending)} unprocessed file(s) waiting for ingest:\n"
        f"{files_block}\n\n"
        "Run /ingest to process them into the wiki layer per CLAUDE.md."
    )

    payload = {
        "hookSpecificOutput": {
            "hookEventName": "SessionStart",
            "additionalContext": message,
        }
    }
    json.dump(payload, sys.stdout)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
