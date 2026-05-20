"""Content-hash ledger of processed INBOX files.

Survives `git pull` rewrites of INBOX/ from other authors because keys
are SHA-256 of file content, not paths. If a file with identical content
re-appears under a different name (because another author ingested it
elsewhere and the pull replayed the INBOX state), the ledger lookup hits
and the file is skipped.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


def sha256_of(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


class Ledger:
    def __init__(self, path: Path) -> None:
        self.path = path
        self._data: dict[str, dict[str, Any]] = {}
        self._load()

    def _load(self) -> None:
        if not self.path.exists():
            self._data = {}
            return
        try:
            self._data = json.loads(self.path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            # Corrupt ledger — preserve old file, start fresh.
            backup = self.path.with_suffix(self.path.suffix + ".corrupt")
            self.path.rename(backup)
            self._data = {}

    def has(self, content_hash: str) -> bool:
        return content_hash in self._data

    def record(self, content_hash: str, source_path: str, pr_url: str | None = None) -> None:
        self._data[content_hash] = {
            "source": source_path,
            "pr": pr_url,
        }
        self._save()

    def _save(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        tmp = self.path.with_suffix(self.path.suffix + ".tmp")
        tmp.write_text(json.dumps(self._data, indent=2), encoding="utf-8")
        tmp.replace(self.path)
