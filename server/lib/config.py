"""Load and resolve server/config.yaml."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml


REPO_ROOT = Path(__file__).resolve().parents[2]
CONFIG_PATH = REPO_ROOT / "server" / "config.yaml"


@dataclass
class JobConfig:
    name: str
    enabled: bool
    claude_command: str
    model: str | None
    bot_branch_prefix: str
    commit_op_token: str
    pr_title_prefix: str
    max_files_changed: int
    max_lines_changed: int
    path_allowlist: list[str]
    # Exactly one of these is set:
    interval_minutes: int | None = None   # repeating timer (OnUnitActiveSec)
    calendar: str | None = None           # calendar timer (OnCalendar)

    def trigger_kind(self) -> str:
        if self.interval_minutes is not None:
            return "interval"
        if self.calendar is not None:
            return "calendar"
        raise ValueError(f"job {self.name}: must set interval_minutes or calendar")


@dataclass
class Config:
    raw: dict[str, Any]

    # ---- shared ----
    @property
    def branch(self) -> str:
        return self.raw["repo"]["branch"]

    @property
    def remote(self) -> str:
        return self.raw["repo"]["remote"]

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
    def claude_default_model(self) -> str | None:
        return self.raw["claude"].get("model")

    @property
    def pull_strategy(self) -> str:
        return self.raw["git"]["pull_strategy"]

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

    # ---- per-job ----
    def _job(self, name: str) -> JobConfig:
        j = self.raw["jobs"][name]
        return JobConfig(
            name=name,
            enabled=bool(j["enabled"]),
            claude_command=j["claude_command"],
            model=j.get("model") or self.claude_default_model,
            bot_branch_prefix=j["bot_branch_prefix"],
            commit_op_token=j["commit_op_token"],
            pr_title_prefix=j["pr_title_prefix"],
            max_files_changed=int(j["caps"]["max_files_changed"]),
            max_lines_changed=int(j["caps"]["max_lines_changed"]),
            path_allowlist=list(j["path_allowlist"]),
            interval_minutes=j.get("interval_minutes"),
            calendar=j.get("calendar"),
        )

    @property
    def auto_ingest(self) -> JobConfig:
        return self._job("auto_ingest")

    @property
    def auto_lint(self) -> JobConfig:
        return self._job("auto_lint")


def load(path: Path = CONFIG_PATH) -> Config:
    with path.open("r", encoding="utf-8") as fh:
        raw = yaml.safe_load(fh)
    return Config(raw=raw)
