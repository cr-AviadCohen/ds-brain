"""Append-only timestamped log writer with trim."""

from __future__ import annotations

import datetime as dt
from pathlib import Path


def now_iso() -> str:
    return dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


class Logger:
    def __init__(self, log_file: Path, trim_lines: int = 2000) -> None:
        self.log_file = log_file
        self.trim_lines = trim_lines
        self.log_file.parent.mkdir(parents=True, exist_ok=True)

    def log(self, msg: str) -> None:
        line = f"[{now_iso()}] {msg}\n"
        with self.log_file.open("a", encoding="utf-8") as fh:
            fh.write(line)
        # Cheap append; trim lazily.
        self._trim()

    def _trim(self) -> None:
        try:
            with self.log_file.open("r", encoding="utf-8") as fh:
                lines = fh.readlines()
        except FileNotFoundError:
            return
        if len(lines) <= self.trim_lines:
            return
        tail = lines[-self.trim_lines:]
        with self.log_file.open("w", encoding="utf-8") as fh:
            fh.writelines(tail)
