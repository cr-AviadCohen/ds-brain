"""Load and resolve server/config.yaml."""

from __future__ import annotations

import os
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml


REPO_ROOT = Path(__file__).resolve().parents[2]
CONFIG_PATH = REPO_ROOT / "server" / "config.yaml"


@dataclass
class Config:
    raw: dict[str, Any]

    @property
    def branch(self) -> str:
        return self.raw["repo"]["branch"]

    @property
    def remote(self) -> str:
        return self.raw["repo"]["remote"]

    @property
    def path_allowlist(self) -> list[str]:
        return list(self.raw["repo"]["path_allowlist"])

    @property
    def interval_minutes(self) -> int:
        return int(self.raw["schedule"]["auto_ingest_interval_minutes"])

    @property
    def claude_command(self) -> str:
        return self.raw["claude"]["command"]

    @property
    def claude_permission_mode(self) -> str:
        return self.raw["claude"]["permission_mode"]

    @property
    def claude_timeout_seconds(self) -> int:
        return int(self.raw["claude"]["timeout_minutes"]) * 60

    @property
    def claude_bin(self) -> str:
        return self.raw["claude"].get("claude_bin", "claude")

    @property
    def pull_strategy(self) -> str:
        return self.raw["git"]["pull_strategy"]

    @property
    def bot_branch_prefix(self) -> str:
        return self.raw["git"]["bot_branch_prefix"]

    @property
    def commit_op_token(self) -> str:
        return self.raw["git"]["commit_op_token"]

    @property
    def pr_title_prefix(self) -> str:
        return self.raw["pr"]["title_prefix"]

    @property
    def pr_auto_merge(self) -> bool:
        return bool(self.raw["pr"]["auto_merge"])

    @property
    def pr_merge_strategy(self) -> str:
        return self.raw["pr"]["merge_strategy"]

    @property
    def pr_needs_review_label(self) -> str:
        return self.raw["pr"]["needs_review_label"]

    @property
    def gh_bin(self) -> str:
        return self.raw["pr"].get("gh_bin", "gh")

    @property
    def max_files_changed(self) -> int:
        return int(self.raw["caps"]["max_files_changed"])

    @property
    def max_lines_changed(self) -> int:
        return int(self.raw["caps"]["max_lines_changed"])

    @property
    def inbox_dir(self) -> Path:
        return REPO_ROOT / self.raw["inbox"]["dir"]

    @property
    def inbox_ignore(self) -> list[str]:
        return list(self.raw["inbox"]["ignore"])

    @property
    def log_dir(self) -> Path:
        return REPO_ROOT / self.raw["logging"]["log_dir"]

    @property
    def log_trim_lines(self) -> int:
        return int(self.raw["logging"]["trim_lines"])

    @property
    def lock_dir(self) -> Path:
        return REPO_ROOT / self.raw["mutex"]["lock_dir"]

    @property
    def mutex_stale_seconds(self) -> int:
        return int(self.raw["mutex"]["stale_seconds"])

    @property
    def ledger_path(self) -> Path:
        return REPO_ROOT / self.raw["ledger"]["path"]


def load(path: Path = CONFIG_PATH) -> Config:
    with path.open("r", encoding="utf-8") as fh:
        raw = yaml.safe_load(fh)
    return Config(raw=raw)
