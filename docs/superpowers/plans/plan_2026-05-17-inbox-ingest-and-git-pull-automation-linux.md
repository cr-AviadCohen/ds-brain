# INBOX Ingest + Git-Pull Automation (Linux/systemd) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Continuously keep the `ds-brain` working tree on a long-running Ubuntu VM in sync with `origin/unified` and auto-process every new INBOX file (except `README.md`) through `/ingest` without prompting — committing and pushing on completion.

**Architecture:** Two **systemd user units** drive the automation under a dedicated unprivileged Linux user (e.g. `dsbrain`):

1. `dsbrain-git-pull.timer` → `dsbrain-git-pull.service` — `OnUnitActiveSec=5min`, runs `scripts/systemd/git-pull.sh` (fast-forward only).
2. `dsbrain-inbox-ingest.path` → `dsbrain-inbox-ingest.service` — systemd `PathModified=` on `INBOX/` triggers `scripts/systemd/inbox-ingest.sh` whenever directory contents change.

Both scripts share an atomic `mkdir`-based mutex so they cannot collide with each other (or a manual `/ingest` if someone shells in). The ingest script invokes `claude -p "/ingest <path>"` non-interactively for each non-README file, relies on `/ingest`'s built-in commit + push, and has a backstop `git add -A && git commit && git push` after each run in case anything was left uncommitted. `loginctl enable-linger <user>` ensures the user manager runs without an active login session.

**Why systemd user units (not cron + inotifywait):**
- **Timer** survives reboots, missed runs are recoverable via `Persistent=true`, status visible via `systemctl --user status`.
- **Path units** are native to systemd; no need to install `inotify-tools` or babysit a long-lived `inotifywait` loop.
- **Journal logging** — every script line lands in `journalctl --user -u dsbrain-*` automatically; we still keep per-script log files for grep-friendly tailing.
- **Single uniform interface** for install/uninstall/inspect via `systemctl --user`.

**Why not Claude Code's `CronCreate`:** `CronCreate` only fires while a Claude session is active. The VM must drive automation 24×7 without a session attached, so a host-level scheduler is required.

**Tech Stack:** Ubuntu 22.04+ / systemd ≥ 245 (path units, user lingering), `bash`, `git`, `claude` CLI in headless `-p` mode, `mkdir` atomic mutex, `journalctl`.

---

## File Structure

**Create:**
- `scripts/systemd/git-pull.sh` — fast-forward pull of `origin/unified`, under mutex. Linux-flavoured `stat` syntax (`stat -c %Y`).
- `scripts/systemd/inbox-ingest.sh` — iterate `INBOX/`, invoke `claude -p "/ingest …"` per file, backstop commit + push, under mutex.
- `scripts/systemd/_lib.sh` — shared helpers (mutex acquire/release, log trim, repo path resolution). Same logic as the macOS variant but using Linux `stat -c %Y`.
- `scripts/systemd/units/dsbrain-git-pull.service.template` — oneshot service running `git-pull.sh`.
- `scripts/systemd/units/dsbrain-git-pull.timer.template` — `OnUnitActiveSec=5min` + `OnBootSec=30s` + `Persistent=true`.
- `scripts/systemd/units/dsbrain-inbox-ingest.service.template` — oneshot service running `inbox-ingest.sh`.
- `scripts/systemd/units/dsbrain-inbox-ingest.path.template` — `PathModified=__REPO_PATH__/INBOX`.
- `scripts/systemd/install.sh` — render templates with absolute repo path, copy to `~/.config/systemd/user/`, enable + start both units, run `loginctl enable-linger` if needed.
- `scripts/systemd/uninstall.sh` — stop, disable, and remove both unit groups.
- `scripts/systemd/log/.gitkeep` — keep log dir tracked, contents gitignored.
- `docs/automation-linux.md` — user-facing doc: install/uninstall/inspect/troubleshoot on Ubuntu VM.

**Modify:**
- `.gitignore` — ignore `scripts/systemd/log/*` except `.gitkeep`, ignore `scripts/systemd/.lock/`.
- `.claude/commands/ingest.md` — append a "Headless mode" note saying that when invoked via `claude -p`, Step 2's "wait for go-ahead" gate is skipped and the workflow proceeds straight through Phases A→D. (Idempotent — if already added by the macOS plan, skip.)

**Test:**
- Manual end-to-end test described in Task 9. No automated test harness — these are system-integration scripts; correctness is verified by exercising them against the real repo on the actual VM and inspecting `journalctl` + the log files.

---

## Design decisions locked in here

- **Target user.** Runs as a dedicated unprivileged service account (`dsbrain` recommended) under that user's systemd user manager. The repo is checked out at `~/ds-brain` (or wherever — `install.sh` discovers the absolute path from its own location).
- **Lingering required.** `loginctl enable-linger dsbrain` (run once as root) so the user manager starts at boot and survives logout. `install.sh` checks for this and prints the exact `sudo` command if missing.
- **Branch.** `unified` (per `CLAUDE.md`). Pull strategy: `git pull --ff-only origin unified`. Fast-forward only — never auto-merge/rebase from a background agent.
- **Mutex.** Atomic `mkdir scripts/systemd/.lock` (POSIX atomic; `flock` could be used but `mkdir` keeps cross-platform parity with the macOS plan). Stale-lock guard: if the lock dir is older than 30 minutes, steal it (a hung ingest is dead).
- **Skip-if-empty.** `inbox-ingest.sh` exits 0 silently when only `README.md` (or only dotfiles) remain. Matches `.claude/hooks/inbox-check.sh`.
- **Path unit refire behaviour.** `PathModified=` fires every time `INBOX/` changes — including when `/ingest` runs `git mv` to drain a file. The script re-checks "is there still a pending file?" each iteration; once drained, exits 0; the next refire short-circuits. With the mutex, this is harmless.
- **Rate limit.** Service files set `StartLimitIntervalSec=60s`, `StartLimitBurst=10` so a runaway path-trigger cycle backs off instead of crashing systemd.
- **Headless ingest invocation:** `claude -p "/ingest INBOX/<file>" --permission-mode bypassPermissions --dangerously-skip-permissions`. Prompt also says "This is an automated headless ingest; proceed without waiting for confirmation."
- **Backstop commit + push:** after each `claude -p` returns, if `git status --porcelain` is non-empty the wrapper does `git add -A && git commit -m "ingest | auto-backstop <file>" && git push origin unified`. `/ingest` is expected to handle this itself; the backstop is defense-in-depth.
- **Log files.** `scripts/systemd/log/git-pull.log` and `scripts/systemd/log/inbox-ingest.log`, trimmed to last 2000 lines after each run. systemd journal additionally captures stdout/stderr via `StandardOutput=append:…` and `StandardError=append:…`.
- **Logrotate** is out of scope — the in-script trim is sufficient for the expected volume.

---

### Task 1: Bootstrap log dir, gitignore, lib helpers

**Files:**
- Create: `scripts/systemd/log/.gitkeep`
- Create: `scripts/systemd/_lib.sh`
- Modify: `.gitignore`

- [ ] **Step 1: Create the log directory placeholder**

```bash
mkdir -p scripts/systemd/log
touch scripts/systemd/log/.gitkeep
```

- [ ] **Step 2: Add ignore rules so logs and lockfile aren't tracked**

Append to `.gitignore`:

```gitignore

# systemd user units — runtime state
scripts/systemd/log/*
!scripts/systemd/log/.gitkeep
scripts/systemd/.lock/
```

- [ ] **Step 3: Create the shared helper library**

Write `scripts/systemd/_lib.sh`:

```bash
#!/bin/bash
# Shared helpers for ds-brain systemd unit scripts. Source, don't execute.
#
# Provides:
#   REPO_DIR             — absolute path to repo root
#   LOG_DIR              — scripts/systemd/log
#   LOCK_DIR             — scripts/systemd/.lock
#   STALE_LOCK_SECONDS   — 1800 (30 min)
#   acquire_lock <name>  — mkdir-based atomic mutex; returns 0 if held, 1 if busy
#   release_lock         — rmdir the lock
#   log_to <file> <msg>  — timestamped append, then trim to 2000 lines
#   trim_log <file>      — keep only the last 2000 lines

set -euo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
LOG_DIR="${REPO_DIR}/scripts/systemd/log"
LOCK_DIR="${REPO_DIR}/scripts/systemd/.lock"
STALE_LOCK_SECONDS=1800

mkdir -p "$LOG_DIR"

# Cross-platform mtime in seconds-since-epoch. Linux: `stat -c %Y`.
# macOS:  `stat -f %m`. We prefer Linux; fallback for macOS dev runs.
_mtime() {
  if stat -c %Y "$1" >/dev/null 2>&1; then
    stat -c %Y "$1"
  else
    stat -f %m "$1"
  fi
}

acquire_lock() {
  local owner="${1:-unknown}"
  if mkdir "$LOCK_DIR" 2>/dev/null; then
    echo "$owner $$ $(date -u +%FT%TZ)" > "$LOCK_DIR/owner"
    return 0
  fi
  if [ -d "$LOCK_DIR" ]; then
    local age
    age=$(( $(date +%s) - $(_mtime "$LOCK_DIR") ))
    if [ "$age" -gt "$STALE_LOCK_SECONDS" ]; then
      rm -rf "$LOCK_DIR"
      if mkdir "$LOCK_DIR" 2>/dev/null; then
        echo "$owner $$ $(date -u +%FT%TZ) (stole stale lock age=${age}s)" > "$LOCK_DIR/owner"
        return 0
      fi
    fi
  fi
  return 1
}

release_lock() {
  rm -rf "$LOCK_DIR" 2>/dev/null || true
}

trim_log() {
  local file="$1"
  [ -f "$file" ] || return 0
  local tmp
  tmp="$(mktemp)"
  tail -n 2000 "$file" > "$tmp" && mv "$tmp" "$file"
}

log_to() {
  local file="$1"; shift
  printf '[%s] %s\n' "$(date -u +%FT%TZ)" "$*" >> "$file"
  trim_log "$file"
}
```

- [ ] **Step 4: Mark executable (not strictly required for sourcing but harmless)**

```bash
chmod +x scripts/systemd/_lib.sh
```

- [ ] **Step 5: Smoke-test the helper**

```bash
bash -c 'source scripts/systemd/_lib.sh && acquire_lock test && echo "acquired"; release_lock && echo "released"'
```

Expected output:
```
acquired
released
```

- [ ] **Step 6: Commit**

```bash
git add scripts/systemd/_lib.sh scripts/systemd/log/.gitkeep .gitignore
git commit -m "schema | scaffold systemd unit lib + log dir for ds-brain automation"
```

---

### Task 2: Write the git-pull script

**Files:**
- Create: `scripts/systemd/git-pull.sh`

- [ ] **Step 1: Create the script**

Write `scripts/systemd/git-pull.sh`:

```bash
#!/bin/bash
# Fast-forward pull of origin/unified. Safe under concurrent manual git
# work because it (a) takes the shared mutex and (b) refuses anything
# beyond a fast-forward.
#
# Run by systemd user unit dsbrain-git-pull.service via dsbrain-git-pull.timer.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=./_lib.sh
source "$SCRIPT_DIR/_lib.sh"

LOG="${LOG_DIR}/git-pull.log"

cd "$REPO_DIR"

if ! acquire_lock "git-pull"; then
  log_to "$LOG" "skip: lock busy"
  exit 0
fi
trap 'release_lock' EXIT

current_branch=$(git rev-parse --abbrev-ref HEAD)
if [ "$current_branch" != "unified" ]; then
  log_to "$LOG" "skip: branch is '$current_branch', not 'unified'"
  exit 0
fi

if ! git diff --quiet || ! git diff --cached --quiet; then
  log_to "$LOG" "skip: working tree dirty"
  exit 0
fi

if ! git fetch --quiet origin unified; then
  log_to "$LOG" "fetch failed"
  exit 1
fi

local_sha=$(git rev-parse HEAD)
remote_sha=$(git rev-parse origin/unified)
if [ "$local_sha" = "$remote_sha" ]; then
  # Quiet: only note no-op once per hour.
  if [ "$(date +%M)" = "00" ]; then
    log_to "$LOG" "up-to-date at $local_sha"
  fi
  exit 0
fi

if git merge-base --is-ancestor "$local_sha" "$remote_sha"; then
  if git merge --ff-only --quiet origin/unified; then
    log_to "$LOG" "fast-forwarded $local_sha → $remote_sha"
    exit 0
  fi
  log_to "$LOG" "fast-forward failed unexpectedly"
  exit 1
fi

log_to "$LOG" "diverged: local=$local_sha remote=$remote_sha — manual resolution required"
exit 1
```

- [ ] **Step 2: Mark executable**

```bash
chmod +x scripts/systemd/git-pull.sh
```

- [ ] **Step 3: Run it manually and inspect the log**

```bash
./scripts/systemd/git-pull.sh && tail -n 5 scripts/systemd/log/git-pull.log
```

Expected: exit 0, log shows either nothing new (silent) or `up-to-date` / `fast-forwarded`.

- [ ] **Step 4: Exercise the mutex with overlapping runs**

```bash
./scripts/systemd/git-pull.sh &
./scripts/systemd/git-pull.sh
wait
tail -n 5 scripts/systemd/log/git-pull.log
```

Expected: one logs success, the other logs `skip: lock busy` (or both succeed if the first finished in microseconds — either is fine; the mutex did not crash).

- [ ] **Step 5: Commit**

```bash
git add scripts/systemd/git-pull.sh
git commit -m "schema | add git-pull script for ds-brain Linux systemd automation"
```

---

### Task 3: Write the inbox-ingest script

**Files:**
- Create: `scripts/systemd/inbox-ingest.sh`

- [ ] **Step 1: Create the script**

Write `scripts/systemd/inbox-ingest.sh`:

```bash
#!/bin/bash
# Auto-ingest every non-README file in INBOX/ via `claude -p "/ingest …"`.
# Triggered by systemd user unit dsbrain-inbox-ingest.service via
# dsbrain-inbox-ingest.path (PathModified on INBOX/). Can also be run
# manually.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=./_lib.sh
source "$SCRIPT_DIR/_lib.sh"

LOG="${LOG_DIR}/inbox-ingest.log"
# Allow env override; default to where `claude` is installed for service user.
CLAUDE_BIN="${CLAUDE_BIN:-$(command -v claude || echo "$HOME/.local/bin/claude")}"

cd "$REPO_DIR"

list_pending() {
  # One non-README, non-dotfile entry per line; nothing if INBOX is empty.
  ls -1 "$REPO_DIR/INBOX" 2>/dev/null \
    | grep -v '^README\.md$' \
    | grep -v '^\.' \
    || true
}

# Early no-op (cheap, before lock contention).
if [ -z "$(list_pending)" ]; then
  exit 0
fi

if ! acquire_lock "inbox-ingest"; then
  log_to "$LOG" "skip: lock busy"
  exit 0
fi
trap 'release_lock' EXIT

current_branch=$(git rev-parse --abbrev-ref HEAD)
if [ "$current_branch" != "unified" ]; then
  log_to "$LOG" "skip: branch is '$current_branch', not 'unified'"
  exit 0
fi
if ! git diff --quiet || ! git diff --cached --quiet; then
  log_to "$LOG" "skip: working tree dirty"
  exit 0
fi

if [ ! -x "$CLAUDE_BIN" ]; then
  log_to "$LOG" "fatal: claude CLI not found at $CLAUDE_BIN"
  exit 1
fi

processed=0
while true; do
  pending="$(list_pending)"
  [ -z "$pending" ] && break

  file="$(printf '%s\n' "$pending" | sort | head -n 1)"
  path="INBOX/$file"

  log_to "$LOG" "begin: $path"

  prompt="/ingest $path

This is an automated headless ingest run from scripts/systemd/inbox-ingest.sh
on the Ubuntu VM. Proceed through all phases without waiting for
confirmation. Auto-commit and push on completion per the ingest spec."

  if "$CLAUDE_BIN" -p "$prompt" \
        --permission-mode bypassPermissions \
        --dangerously-skip-permissions \
        >> "$LOG" 2>&1; then
    log_to "$LOG" "ok: $path (claude -p exit 0)"
  else
    rc=$?
    log_to "$LOG" "fail: $path (claude -p exit $rc) — leaving file in place"
    # Don't loop forever on a poison-pill. Bail; next path event retries.
    exit "$rc"
  fi

  # Backstop: if /ingest didn't commit, do it now.
  if [ -n "$(git status --porcelain)" ]; then
    log_to "$LOG" "backstop: committing residual changes"
    git add -A
    git commit -m "ingest | auto-backstop after $file" >> "$LOG" 2>&1 || true
    git push origin unified >> "$LOG" 2>&1 || \
      log_to "$LOG" "backstop: push failed"
  fi

  processed=$((processed + 1))
  # Safety cap: do not process more than 10 files in one trigger fire.
  if [ "$processed" -ge 10 ]; then
    log_to "$LOG" "cap: processed 10 files, deferring rest to next fire"
    break
  fi
done

if [ "$processed" -gt 0 ]; then
  log_to "$LOG" "done: processed $processed file(s)"
fi
```

- [ ] **Step 2: Mark executable**

```bash
chmod +x scripts/systemd/inbox-ingest.sh
```

- [ ] **Step 3: Dry-run when INBOX has only README**

```bash
# Temporarily relocate the pending Strotz file (if present) to exercise the
# empty-INBOX no-op path:
[ -e "INBOX/Strotz Friedberg" ] && mv "INBOX/Strotz Friedberg" /tmp/strotz.bak
./scripts/systemd/inbox-ingest.sh
echo "exit=$?"
[ -e /tmp/strotz.bak ] && mv /tmp/strotz.bak "INBOX/Strotz Friedberg"
```

Expected: exit 0, nothing appended to the log (early no-op short-circuits before any logging).

- [ ] **Step 4: Verify lock contention path**

```bash
mkdir -p scripts/systemd/.lock && echo "test $$ $(date -u +%FT%TZ)" > scripts/systemd/.lock/owner
./scripts/systemd/inbox-ingest.sh
tail -n 3 scripts/systemd/log/inbox-ingest.log
rm -rf scripts/systemd/.lock
```

Expected: log shows `skip: lock busy` (only fires if INBOX actually has a pending file).

- [ ] **Step 5: Commit (defer live ingest test to Task 9)**

```bash
git add scripts/systemd/inbox-ingest.sh
git commit -m "schema | add inbox-ingest script for ds-brain Linux systemd automation"
```

---

### Task 4: Add headless-mode note to /ingest command (idempotent)

**Files:**
- Modify: `.claude/commands/ingest.md`

- [ ] **Step 1: Check whether the note already exists**

```bash
grep -q '## Headless / automated mode' .claude/commands/ingest.md && echo "already present" || echo "needs append"
```

If the macOS plan already added this section, the rest of this task is a no-op. Otherwise continue.

- [ ] **Step 2: Append the headless-mode note**

If the previous step said `needs append`, append at the end of `.claude/commands/ingest.md`:

```markdown

## Headless / automated mode

If this command is invoked through `claude -p` (e.g. by
`scripts/systemd/inbox-ingest.sh` on the Ubuntu VM, or by
`scripts/cron/inbox-ingest.sh` on macOS), Step 2's "wait for go-ahead
before continuing" gate is **skipped**. Proceed straight through Phase
A → B → C → D using your best judgement on the destination tab. The
automated run expects auto-commit + push to complete; do not stop and
ask questions.

Signals you are in headless mode:
- The invoking prompt explicitly says "headless" / "automated" / "Proceed
  without waiting for confirmation".
- There is no human in the loop to answer.
```

- [ ] **Step 3: Commit (skip if no changes)**

```bash
if git diff --quiet .claude/commands/ingest.md; then
  echo "no changes — skipping commit"
else
  git add .claude/commands/ingest.md
  git commit -m "schema | document /ingest headless mode for systemd automation"
fi
```

---

### Task 5: Write the systemd unit templates

**Files:**
- Create: `scripts/systemd/units/dsbrain-git-pull.service.template`
- Create: `scripts/systemd/units/dsbrain-git-pull.timer.template`
- Create: `scripts/systemd/units/dsbrain-inbox-ingest.service.template`
- Create: `scripts/systemd/units/dsbrain-inbox-ingest.path.template`

- [ ] **Step 1: Create the templates directory**

```bash
mkdir -p scripts/systemd/units
```

- [ ] **Step 2: Write the git-pull service template**

Write `scripts/systemd/units/dsbrain-git-pull.service.template`:

```ini
[Unit]
Description=ds-brain: fast-forward pull of origin/unified
Documentation=https://github.com/cybereason-labs/ds-brain
ConditionPathIsDirectory=__REPO_PATH__/.git

[Service]
Type=oneshot
WorkingDirectory=__REPO_PATH__
Environment=PATH=__HOME_PATH__/.local/bin:/usr/local/bin:/usr/bin:/bin
Environment=HOME=__HOME_PATH__
ExecStart=/bin/bash __REPO_PATH__/scripts/systemd/git-pull.sh
StandardOutput=append:__REPO_PATH__/scripts/systemd/log/git-pull.systemd.log
StandardError=append:__REPO_PATH__/scripts/systemd/log/git-pull.systemd.log

# Don't tank the whole unit on transient git/network blips.
StartLimitIntervalSec=60
StartLimitBurst=10
```

- [ ] **Step 3: Write the git-pull timer template**

Write `scripts/systemd/units/dsbrain-git-pull.timer.template`:

```ini
[Unit]
Description=ds-brain: every 5min, fast-forward unified

[Timer]
Unit=dsbrain-git-pull.service
OnBootSec=30s
OnUnitActiveSec=5min
AccuracySec=15s
Persistent=true

[Install]
WantedBy=timers.target
```

`Persistent=true` means if the VM was off when a fire would have happened, systemd runs it once on boot to catch up.

- [ ] **Step 4: Write the inbox-ingest service template**

Write `scripts/systemd/units/dsbrain-inbox-ingest.service.template`:

```ini
[Unit]
Description=ds-brain: headless /ingest for files in INBOX/
Documentation=https://github.com/cybereason-labs/ds-brain
ConditionPathIsDirectory=__REPO_PATH__/INBOX

[Service]
Type=oneshot
WorkingDirectory=__REPO_PATH__
Environment=PATH=__HOME_PATH__/.local/bin:/usr/local/bin:/usr/bin:/bin
Environment=HOME=__HOME_PATH__
# CLAUDE_BIN may be overridden via a drop-in if installed elsewhere.
ExecStart=/bin/bash __REPO_PATH__/scripts/systemd/inbox-ingest.sh
StandardOutput=append:__REPO_PATH__/scripts/systemd/log/inbox-ingest.systemd.log
StandardError=append:__REPO_PATH__/scripts/systemd/log/inbox-ingest.systemd.log

# Ingest can run for minutes; don't reap it.
TimeoutStartSec=30min

# Rate limit refire churn.
StartLimitIntervalSec=60
StartLimitBurst=10
```

- [ ] **Step 5: Write the inbox-ingest path template**

Write `scripts/systemd/units/dsbrain-inbox-ingest.path.template`:

```ini
[Unit]
Description=ds-brain: watch INBOX/ for new files

[Path]
PathModified=__REPO_PATH__/INBOX
Unit=dsbrain-inbox-ingest.service

[Install]
WantedBy=paths.target
```

`PathModified=` triggers whenever the directory's contents change (file added, removed, renamed). The script's internal `list_pending` + mutex absorbs any refire storm during a `/ingest`'s own `git mv`.

- [ ] **Step 6: Commit**

```bash
git add scripts/systemd/units/
git commit -m "schema | add systemd user unit templates for ds-brain automation"
```

---

### Task 6: Write the install / uninstall scripts

**Files:**
- Create: `scripts/systemd/install.sh`
- Create: `scripts/systemd/uninstall.sh`

- [ ] **Step 1: Write `install.sh`**

Write `scripts/systemd/install.sh`:

```bash
#!/bin/bash
# Render systemd user unit files from templates (substituting absolute
# paths), install them under ~/.config/systemd/user/, enable, and start.
#
# Idempotent: re-running replaces unit files and reloads. Must be run as
# the service user (not root). Run-once-as-root setup is printed below
# if lingering isn't enabled.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_DIR="$(cd "$SCRIPT_DIR/../.." && pwd)"
TEMPLATE_DIR="$SCRIPT_DIR/units"
UNIT_DIR="$HOME/.config/systemd/user"

if [ "$(id -u)" = "0" ]; then
  echo "error: do not run install.sh as root. Run as the service user." >&2
  exit 1
fi

# Verify systemd user manager is available.
if ! command -v systemctl >/dev/null; then
  echo "error: systemctl not found — this script requires systemd." >&2
  exit 1
fi
if ! systemctl --user status >/dev/null 2>&1; then
  echo "error: systemd --user is not running for this session." >&2
  echo "If this is a headless VM you must enable lingering as root:" >&2
  echo "  sudo loginctl enable-linger $(id -un)" >&2
  exit 1
fi

mkdir -p "$UNIT_DIR"

units=(
  "dsbrain-git-pull.service"
  "dsbrain-git-pull.timer"
  "dsbrain-inbox-ingest.service"
  "dsbrain-inbox-ingest.path"
)

for unit in "${units[@]}"; do
  src="$TEMPLATE_DIR/${unit}.template"
  dst="$UNIT_DIR/${unit}"
  if [ ! -f "$src" ]; then
    echo "error: missing template $src" >&2
    exit 1
  fi
  sed \
    -e "s|__REPO_PATH__|${REPO_DIR}|g" \
    -e "s|__HOME_PATH__|${HOME}|g" \
    "$src" > "$dst"
  echo "rendered: $dst"
done

systemctl --user daemon-reload

# Enable + start the trigger units (timer + path). Their .service units
# don't need enabling — they're activated by the triggers.
systemctl --user enable --now dsbrain-git-pull.timer
systemctl --user enable --now dsbrain-inbox-ingest.path

echo
echo "Lingering check:"
if loginctl show-user "$(id -un)" 2>/dev/null | grep -q '^Linger=yes'; then
  echo "  linger: enabled ✓"
else
  echo "  linger: NOT enabled. Run once as root:"
  echo "    sudo loginctl enable-linger $(id -un)"
fi

echo
echo "Verify:"
echo "  systemctl --user list-timers | grep dsbrain"
echo "  systemctl --user status dsbrain-inbox-ingest.path"
echo "  journalctl --user -u dsbrain-git-pull.service -n 20"
echo "  journalctl --user -u dsbrain-inbox-ingest.service -n 20"
echo "  tail -f $REPO_DIR/scripts/systemd/log/*.log"
```

- [ ] **Step 2: Write `uninstall.sh`**

Write `scripts/systemd/uninstall.sh`:

```bash
#!/bin/bash
# Stop, disable, and remove the ds-brain systemd user units.
set -euo pipefail

UNIT_DIR="$HOME/.config/systemd/user"

units=(
  "dsbrain-git-pull.timer"
  "dsbrain-inbox-ingest.path"
  "dsbrain-git-pull.service"
  "dsbrain-inbox-ingest.service"
)

for unit in "${units[@]}"; do
  systemctl --user disable --now "$unit" 2>/dev/null || true
  rm -f "$UNIT_DIR/$unit"
  echo "removed: $unit"
done

systemctl --user daemon-reload
echo "done. Lingering left intact — disable manually if no longer needed:"
echo "  sudo loginctl disable-linger $(id -un)"
```

- [ ] **Step 3: Mark both executable**

```bash
chmod +x scripts/systemd/install.sh scripts/systemd/uninstall.sh
```

- [ ] **Step 4: Commit**

```bash
git add scripts/systemd/install.sh scripts/systemd/uninstall.sh
git commit -m "schema | add systemd install/uninstall scripts for ds-brain"
```

---

### Task 7: Install on the Ubuntu VM and verify boot

> **Run these steps ON the Ubuntu VM**, not on a dev macOS box.

**Files:** none modified — runtime action only.

- [ ] **Step 1: One-time pre-reqs (skip if already done)**

As **root** (or with `sudo`):

```bash
# Enable user lingering so the service-user's systemd runs without login.
sudo loginctl enable-linger "$(id -un dsbrain 2>/dev/null || echo dsbrain)"
```

Verify `claude` CLI is installed under the service user (e.g. `/home/dsbrain/.local/bin/claude`) and that user has logged into Claude Code at least once interactively (so the auth token + Claude config exist in `~/.config/`).

- [ ] **Step 2: Install the units**

As the service user:

```bash
cd ~/ds-brain    # or wherever the repo lives
./scripts/systemd/install.sh
```

Expected: four `rendered:` lines, two `Created symlink` confirmations from `systemctl enable`, and the `Lingering check: ✓` line (or the sudo prompt if not yet set).

- [ ] **Step 3: Confirm timer is scheduled**

```bash
systemctl --user list-timers | grep dsbrain
```

Expected: one line for `dsbrain-git-pull.timer` showing a `NEXT` time within the next 5 min.

- [ ] **Step 4: Confirm path watcher is active**

```bash
systemctl --user status dsbrain-inbox-ingest.path
```

Expected: `Active: active (waiting)` and `PathModified: <repo>/INBOX`.

- [ ] **Step 5: Trigger an immediate test fire and inspect**

```bash
systemctl --user start dsbrain-git-pull.service
journalctl --user -u dsbrain-git-pull.service -n 20 --no-pager
tail -n 10 scripts/systemd/log/git-pull.log
```

Expected: a fast-forward / up-to-date line, no errors in the journal.

---

### Task 8: Verify the git-pull cycle end-to-end on the VM

**Files:** none — runtime verification.

- [ ] **Step 1: Push a no-op change to `origin/unified` from a different machine**

Make a trivial commit (e.g. a blank line at the end of `wiki/Log/pulse.md`) and push to `origin/unified`. If inconvenient, skip — the timer will simply continue logging quiet `up-to-date` ticks.

- [ ] **Step 2: Wait up to 5 min and inspect**

```bash
sleep 310 && tail -n 5 scripts/systemd/log/git-pull.log
```

Expected (when something landed): `fast-forwarded <old> → <new>`. Otherwise silent.

- [ ] **Step 3: Confirm the local branch advanced**

```bash
git log --oneline -3
git fetch origin unified --quiet && git log --oneline origin/unified -3
```

Expected: local HEAD matches `origin/unified`.

---

### Task 9: Verify the inbox-ingest cycle end-to-end on the VM

**Files:** none — runtime verification using a real test file.

- [ ] **Step 1: Drop a small test note into INBOX/**

```bash
cat > INBOX/test-automation-2026-05-17.md <<'EOF'
---
title: Cron automation smoke-test note (Linux)
created: 2026-05-17
---

# Cron automation smoke-test (Linux/systemd)

This file exists to verify that scripts/systemd/inbox-ingest.sh picks up
new INBOX/ files and runs /ingest headlessly. Treat as a one-line
synthesis; file under wiki/Sources/ or delete after verification.
EOF
```

The `PathModified=` watcher fires within seconds; the service starts.

- [ ] **Step 2: Watch the journal and the log file live**

In one shell:

```bash
journalctl --user -u dsbrain-inbox-ingest.service -f
```

In another:

```bash
tail -f scripts/systemd/log/inbox-ingest.log
```

Expected within ~5 s: `begin: INBOX/test-automation-2026-05-17.md`, then `claude -p` output streamed in, then `ok: …` (or backstop commit lines). Stop the tails with Ctrl-C once `done:` or `fail:` is logged.

- [ ] **Step 3: Confirm the file moved out of INBOX/**

```bash
ls INBOX/
```

Expected: only `README.md` (and any *other* pre-existing pending file that has also now been processed by the same run).

- [ ] **Step 4: Confirm commit + push landed**

```bash
git log --oneline -5
git fetch origin unified --quiet && git log --oneline origin/unified -3
```

Expected: a recent `ingest | …` commit on both local and remote.

- [ ] **Step 5: If the run failed, diagnose**

If the log shows `fail: …`, check (in order):

1. `journalctl --user -u dsbrain-inbox-ingest.service -n 100 --no-pager` for systemd-level errors.
2. `scripts/systemd/log/inbox-ingest.log` for the inline `claude -p` output that preceded the failure.
3. `scripts/systemd/log/inbox-ingest.systemd.log` for stdout/stderr captured by `StandardError=`.

Common fixes:
- `CLAUDE_BIN` path wrong → either `chmod +x` it, or create a drop-in:

  ```bash
  mkdir -p ~/.config/systemd/user/dsbrain-inbox-ingest.service.d
  cat > ~/.config/systemd/user/dsbrain-inbox-ingest.service.d/claude-bin.conf <<'EOF'
  [Service]
  Environment=CLAUDE_BIN=/usr/local/bin/claude
  EOF
  systemctl --user daemon-reload
  ```

- Claude CLI not authenticated for the service user → run `claude` interactively once as that user to complete auth.
- `--dangerously-skip-permissions` rejected → confirm the installed `claude` CLI version supports it; otherwise drop to `--permission-mode bypassPermissions` only.
- `/ingest` failed mid-flight and left the file in place → run an interactive `claude` `/ingest` session manually to recover, then re-check the script.

---

### Task 10: Document the automation

**Files:**
- Create: `docs/automation-linux.md`

- [ ] **Step 1: Write the doc**

Write `docs/automation-linux.md`:

```markdown
---
title: ds-brain Background Automation (Linux/systemd)
type: doc
created: 2026-05-17
tags: [doc, automation, ops, linux]
---

# Background automation (Linux Ubuntu VM)

Two systemd user units keep the vault in sync and process INBOX/
without manual prodding on a long-running Ubuntu VM.

| Unit | Trigger | Script |
|---|---|---|
| `dsbrain-git-pull.timer` → `.service` | every 5 min (`OnUnitActiveSec=5min`, `Persistent=true`) | `scripts/systemd/git-pull.sh` |
| `dsbrain-inbox-ingest.path` → `.service` | `PathModified=` on `INBOX/` | `scripts/systemd/inbox-ingest.sh` |

Both scripts share a mutex (`scripts/systemd/.lock/`) so they can't
collide with each other or with a manual `/ingest` session.

## One-time host setup

```bash
# As root: allow the service user's systemd to run without an active login.
sudo loginctl enable-linger dsbrain

# As the service user: make sure `claude` is on PATH and authenticated.
which claude
claude --version
```

## Install / uninstall

Run as the **service user** (not root) from inside the repo:

```bash
./scripts/systemd/install.sh    # idempotent
./scripts/systemd/uninstall.sh  # remove
```

`install.sh` renders the unit templates in `scripts/systemd/units/`
with absolute paths, installs them under `~/.config/systemd/user/`,
and enables both triggers.

## Inspect

```bash
systemctl --user list-timers | grep dsbrain
systemctl --user status dsbrain-inbox-ingest.path
systemctl --user status dsbrain-git-pull.timer
journalctl --user -u dsbrain-git-pull.service -n 50
journalctl --user -u dsbrain-inbox-ingest.service -f
tail -f scripts/systemd/log/git-pull.log scripts/systemd/log/inbox-ingest.log
```

## Conservative behaviour

Both scripts **skip** (exit 0, no error) when:
- Current branch is not `unified`.
- Working tree is dirty.
- The shared mutex is held by another run.

`git-pull.sh` refuses anything beyond a fast-forward. If
`origin/unified` has diverged from local, it logs and exits non-zero
— resolution is manual.

`inbox-ingest.sh` calls `claude -p "/ingest <path>"
--dangerously-skip-permissions` and trusts `/ingest`'s commit + push. A
backstop `git add -A && git commit && git push` runs after each
invocation in case anything was left uncommitted. A 10-file cap per
fire prevents one trigger from running for hours.

## Failure modes worth knowing

- **Headless `/ingest` hangs**: the mutex has a 30-minute stale-lock
  guard. After that, the next fire steals the lock and proceeds.
- **Push rejected** (someone else pushed concurrently): the 5-min
  `git pull --ff-only` reconciles, and the next INBOX event ingests
  fresh.
- **Unit fails to start**: `journalctl --user -u dsbrain-* -n 50` and
  `scripts/systemd/log/*.systemd.log` show the reason. Common: missing
  `claude` CLI or stale unit file after a template edit (re-run
  `install.sh`).
- **`claude` CLI requires interactive auth**: log in once as the service
  user with `claude` interactively; the saved auth token is then reused
  by `claude -p` in headless mode.

## Relationship to the macOS plan

This is the Linux counterpart of
`docs/superpowers/plans/plan_2026-05-17-inbox-ingest-and-git-pull-automation.md`,
which targets macOS via launchd. The two coexist: pick the one matching
the host. They share the same script logic and headless-mode contract
on `/ingest`.
```

- [ ] **Step 2: Commit**

```bash
git add docs/automation-linux.md
git commit -m "schema | document ds-brain Linux systemd automation"
```

- [ ] **Step 3: Push everything**

```bash
git push origin unified
```

Expected: clean push; all commits from this plan land on `origin/unified`.

---

## Rollback

If anything goes wrong on the VM:

```bash
./scripts/systemd/uninstall.sh
```

This stops both triggers and removes the unit files from
`~/.config/systemd/user/`. Scripts and templates in the repo remain
(committed) — re-install when ready. Lingering is intentionally left
intact; disable manually with `sudo loginctl disable-linger <user>` if
no longer needed.

---

## Self-review notes

- **Spec coverage:**
  - "do git pull every 5 minutes" → Task 2 script + Task 5 `OnUnitActiveSec=5min` + `Persistent=true`.
  - "run /ingest if a new file added to INBOX (except README.md)" → Task 3 `list_pending` excludes `README.md` and dotfiles + Task 5 `PathModified=` on `INBOX/`.
  - "ingestion without questions to the user" → Task 4 documents headless mode in `/ingest`; Task 3 passes `--dangerously-skip-permissions` and an explicit "proceed without waiting for confirmation" prompt.
  - "after ingestion, commit and push" → Task 3 trusts `/ingest`'s own auto-commit + push, with a backstop `git add -A && git commit && git push origin unified` if anything residual is left.
- **Conservative defaults** (skip on dirty tree / wrong branch, fast-forward only, mutex with stale-guard, rate-limit `StartLimitBurst=10`, 10-file cap per fire) locked into the code in Tasks 2 and 3.
- **Choice of systemd over alternatives** (cron + inotifywait, `claude` MCP CronCreate) justified in the Architecture block.
- **Cross-platform `stat`** in `_lib.sh` so the scripts also run on a macOS dev box for one-off debugging.
- **Idempotent install** so re-running `install.sh` after a template edit just replaces files and reloads.
- **`Task 4` is idempotent** — won't double-append the headless-mode section if the macOS plan already added it.
