"""Idempotent installer for the ds-brain auto-ingest daemon.

Run as the service user (NOT root) from inside the repo:

    cd server
    uv sync                        # bootstrap .venv from uv.lock
    uv run python setup.py         # render + install systemd units

Re-run after editing config.yaml to re-render unit files.
"""

from __future__ import annotations

import os
import shutil
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from lib import config as cfg_mod


REPO_ROOT = Path(__file__).resolve().parents[1]
SERVER_DIR = REPO_ROOT / "server"
UNIT_TEMPLATE_DIR = SERVER_DIR / "units"
USER_UNIT_DIR = Path.home() / ".config" / "systemd" / "user"

REQUIRED_BINS = ["git", "uv"]


def die(msg: str, hint: str | None = None) -> None:
    print(f"error: {msg}", file=sys.stderr)
    if hint:
        print(f"  hint: {hint}", file=sys.stderr)
    sys.exit(1)


def check_not_root() -> None:
    if os.geteuid() == 0:
        die("do not run as root", "run as the service user (e.g. `dsbrain`)")


def check_bin(name: str) -> str:
    path = shutil.which(name)
    if not path:
        die(f"`{name}` not on PATH")
    return path


def check_systemd_user() -> None:
    r = subprocess.run(
        ["systemctl", "--user", "status"],
        capture_output=True,
        text=True,
    )
    if r.returncode != 0:
        die(
            "systemd --user is not running for this session",
            f"on headless VM run as root: sudo loginctl enable-linger {os.getlogin()}",
        )


def check_claude(cfg: cfg_mod.Config) -> str:
    path = shutil.which(cfg.claude_bin)
    if not path:
        die(
            f"claude CLI `{cfg.claude_bin}` not found",
            "install Claude Code CLI and run `claude` once interactively to authenticate",
        )
    return path


def check_gh(cfg: cfg_mod.Config) -> str:
    path = shutil.which(cfg.gh_bin)
    if not path:
        die(f"`{cfg.gh_bin}` not found", "install GitHub CLI: https://cli.github.com/")
    r = subprocess.run([cfg.gh_bin, "auth", "status"], capture_output=True, text=True)
    if r.returncode != 0:
        die(
            "gh CLI is not authenticated",
            "run: gh auth login  (use owner PAT with repo + workflow scopes)",
        )
    return path


def check_linger() -> None:
    user = os.getlogin()
    r = subprocess.run(
        ["loginctl", "show-user", user],
        capture_output=True,
        text=True,
    )
    if "Linger=yes" in r.stdout:
        print(f"  linger: enabled ✓")
    else:
        print(f"  linger: NOT enabled — run once as root:")
        print(f"    sudo loginctl enable-linger {user}")


def render_unit(template: Path, dest: Path, subs: dict[str, str]) -> None:
    text = template.read_text(encoding="utf-8")
    for k, v in subs.items():
        text = text.replace(k, v)
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(text, encoding="utf-8")
    print(f"rendered: {dest}")


def main() -> int:
    check_not_root()
    for b in REQUIRED_BINS:
        check_bin(b)
    check_systemd_user()

    cfg = cfg_mod.load()
    claude_path = check_claude(cfg)
    gh_path = check_gh(cfg)
    uv_path = shutil.which("uv") or "/usr/local/bin/uv"

    print(f"  claude: {claude_path}")
    print(f"  gh:     {gh_path}")
    print(f"  uv:     {uv_path}")

    # Ensure state dirs exist.
    (SERVER_DIR / "state" / "logs").mkdir(parents=True, exist_ok=True)

    subs = {
        "__REPO_PATH__": str(REPO_ROOT),
        "__HOME_PATH__": str(Path.home()),
        "__UV_BIN__": uv_path,
        "__INTERVAL_MINUTES__": str(cfg.interval_minutes),
    }

    USER_UNIT_DIR.mkdir(parents=True, exist_ok=True)
    units = ["dsbrain-auto-ingest.service", "dsbrain-auto-ingest.timer"]
    for unit in units:
        src = UNIT_TEMPLATE_DIR / f"{unit}.template"
        dst = USER_UNIT_DIR / unit
        if not src.exists():
            die(f"missing template {src}")
        render_unit(src, dst, subs)

    subprocess.run(["systemctl", "--user", "daemon-reload"], check=True)
    subprocess.run(
        ["systemctl", "--user", "enable", "--now", "dsbrain-auto-ingest.timer"],
        check=True,
    )

    print()
    print("Lingering check:")
    check_linger()

    print()
    print("Verify:")
    print("  systemctl --user list-timers | grep dsbrain")
    print("  systemctl --user status dsbrain-auto-ingest.timer")
    print("  journalctl --user -u dsbrain-auto-ingest.service -n 20")
    print(f"  tail -f {SERVER_DIR}/state/logs/auto_ingest.log")
    return 0


if __name__ == "__main__":
    sys.exit(main())
