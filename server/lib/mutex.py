"""mkdir-based atomic mutex with stale-lock steal."""

from __future__ import annotations

import os
import shutil
import time
from pathlib import Path


class LockBusy(Exception):
    pass


class Mutex:
    def __init__(self, lock_dir: Path, stale_seconds: int = 1800) -> None:
        self.lock_dir = lock_dir
        self.stale_seconds = stale_seconds
        self._held = False

    def acquire(self, owner: str) -> None:
        try:
            os.mkdir(self.lock_dir)
        except FileExistsError:
            if not self._try_steal_stale():
                raise LockBusy(f"lock held at {self.lock_dir}")
            os.mkdir(self.lock_dir)
        (self.lock_dir / "owner").write_text(
            f"{owner} pid={os.getpid()} ts={int(time.time())}\n",
            encoding="utf-8",
        )
        self._held = True

    def _try_steal_stale(self) -> bool:
        try:
            age = time.time() - self.lock_dir.stat().st_mtime
        except FileNotFoundError:
            return True
        if age > self.stale_seconds:
            shutil.rmtree(self.lock_dir, ignore_errors=True)
            return True
        return False

    def release(self) -> None:
        if not self._held:
            return
        shutil.rmtree(self.lock_dir, ignore_errors=True)
        self._held = False

    def __enter__(self) -> "Mutex":
        return self

    def __exit__(self, exc_type, exc, tb) -> None:
        self.release()
