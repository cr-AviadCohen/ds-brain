"""Idempotent installer for the ds-brain auto-* daemons.

Run as the service user (NOT root) from inside the repo:

    cd server
    uv sync                        # bootstrap .venv from uv.lock
    uv run python setup.py         # render + install systemd units

Re-run after editing config.yaml to re-render unit files (changes to
interval_minutes / calendar / enabled flags require re-render).
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
        print("  linger: enabled ✓")
    else:
        print("  linger: NOT enabled — run once as root:")
        print(f"    sudo loginctl enable-linger {user}")


def render_unit(template: Path, dest: Path, subs: dict[str, str]) -> None:
    text = template.read_text(encoding="utf-8")
    for k, v in subs.items():
        text = text.replace(k, v)
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(text, encoding="utf-8")
    print(f"rendered: {dest}")


def install_job(
    job: cfg_mod.JobConfig,
    shared_subs: dict[str, str],
) -> None:
    """Render + install one job's service + timer unit pair."""
    short = job.name.replace("_", "-")  # auto_ingest → auto-ingest
    base = f"dsbrain-{short}"
    service_tpl = UNIT_TEMPLATE_DIR / f"{base}.service.template"
    timer_tpl = UNIT_TEMPLATE_DIR / f"{base}.timer.template"
    if not service_tpl.exists() or not timer_tpl.exists():
        die(f"missing template(s) for {job.name}: {service_tpl} / {timer_tpl}")

    subs = dict(shared_subs)
    kind = job.trigger_kind()
    if kind == "interval":
        subs["__INTERVAL_MINUTES__"] = str(job.interval_minutes)
    elif kind == "calendar":
        subs["__CALENDAR__"] = str(job.calendar)

    render_unit(service_tpl, USER_UNIT_DIR / f"{base}.service", subs)
    render_unit(timer_tpl, USER_UNIT_DIR / f"{base}.timer", subs)

    if job.enabled:
        subprocess.run(
            ["systemctl", "--user", "enable", "--now", f"{base}.timer"],
            check=True,
        )
        print(f"  enabled+started: {base}.timer")
    else:
        subprocess.run(
            ["systemctl", "--user", "disable", "--now", f"{base}.timer"],
            check=False,
        )
        print(f"  disabled: {base}.timer (config says enabled=false)")


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

    (SERVER_DIR / "state" / "logs").mkdir(parents=True, exist_ok=True)
    USER_UNIT_DIR.mkdir(parents=True, exist_ok=True)

    shared_subs = {
        "__REPO_PATH__": str(REPO_ROOT),
        "__HOME_PATH__": str(Path.home()),
        "__UV_BIN__": uv_path,
    }

    for job in (cfg.auto_ingest, cfg.auto_lint):
        print(f"\n[{job.name}] model={job.model or 'default'} enabled={job.enabled}")
        install_job(job, shared_subs)

    subprocess.run(["systemctl", "--user", "daemon-reload"], check=True)

    print()
    print("Lingering check:")
    check_linger()

    print()
    print("Verify:")
    print("  systemctl --user list-timers | grep dsbrain")
    print("  systemctl --user status dsbrain-auto-ingest.timer")
    print("  systemctl --user status dsbrain-auto-lint.timer")
    print("  journalctl --user -u dsbrain-auto-ingest.service -n 20")
    print("  journalctl --user -u dsbrain-auto-lint.service -n 20")
    print(f"  tail -f {SERVER_DIR}/state/logs/auto_ingest.log")
    print(f"  tail -f {SERVER_DIR}/state/logs/auto_lint.log")
    return 0


if __name__ == "__main__":
    sys.exit(main())
