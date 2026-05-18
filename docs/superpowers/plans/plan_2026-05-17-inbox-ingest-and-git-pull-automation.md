# INBOX Ingest + Git-Pull Automation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Continuously keep the `ds-brain` working tree in sync with `origin/unified` and auto-process new INBOX files through `/ingest` without manual prompting.

**Architecture:** Two macOS `launchd` LaunchAgents drive the automation. A timer agent (`com.cybereason.ds-brain.git-pull`) runs `scripts/cron/git-pull.sh` every 5 minutes (`StartInterval: 300`). A file-watch agent (`com.cybereason.ds-brain.inbox-ingest`) uses launchd's native `WatchPaths` on `INBOX/` and runs `scripts/cron/inbox-ingest.sh` whenever a file appears. Both scripts share an `mkdir`-based mutex so they cannot stomp each other (or a manual `/ingest` session). The ingest script invokes `claude -p "/ingest <path>"` in non-interactive mode for each non-README file, relying on `/ingest`'s built-in commit + push (with a backstop commit-if-dirty step after each invocation).

**Why launchd over cron:** native macOS, survives sleep/wake (cron silently misses ticks during sleep), built-in `WatchPaths` removes the need for an `fswatch` dependency, and logs route through `StandardOutPath`/`StandardErrorPath`.

**Why not Claude Code's `CronCreate`:** `CronCreate` only fires while a Claude session is active. The requirement is "every 5 minutes" regardless of whether anyone is at the keyboard, so a host-level scheduler is required.

**Tech Stack:** macOS `launchd` (plist-driven LaunchAgents), `bash`, `git`, `claude -p` headless invocation, `mkdir` atomic mutex.

---

## File Structure

**Create:**
- `scripts/cron/git-pull.sh` — fast-forward pull of `origin/unified`, under mutex.
- `scripts/cron/inbox-ingest.sh` — iterate INBOX/, invoke `claude -p "/ingest …"` per file, backstop commit + push, under mutex.
- `scripts/cron/_lib.sh` — shared helpers (mutex acquire/release, log rotation, repo path resolution).
- `scripts/cron/install.sh` — render plists with absolute repo path, copy to `~/Library/LaunchAgents/`, `launchctl bootstrap` both agents.
- `scripts/cron/uninstall.sh` — `launchctl bootout` both agents and remove plists.
- `scripts/cron/launchagents/com.cybereason.ds-brain.git-pull.plist.template` — plist template with `__REPO_PATH__` placeholder.
- `scripts/cron/launchagents/com.cybereason.ds-brain.inbox-ingest.plist.template` — same.
- `scripts/cron/log/.gitkeep` — keep log dir tracked, contents gitignored.
- `docs/automation.md` — user-facing doc: what's running, how to install/uninstall/inspect.

**Modify:**
- `.gitignore` — ignore `scripts/cron/log/*` except `.gitkeep`, ignore `scripts/cron/.lock/`.
- `.claude/commands/ingest.md` — append a "Headless mode" note saying that when invoked via `claude -p`, Step 2's "wait for go-ahead" gate is skipped and the workflow proceeds straight through Phases A→D.

**Test:**
- Manual end-to-end test described in Task 9. No automated test harness — these are system-integration scripts; correctness is verified by exercising them against the real repo and inspecting log output.

---

## Design notes locked in here

- **Branch:** `unified` (per `CLAUDE.md`). Pull strategy: `git pull --ff-only origin unified`. If the fast-forward fails, log and exit non-zero — never auto-merge or auto-rebase from a background agent.
- **Mutex:** atomic `mkdir scripts/cron/.lock` (POSIX atomic; `flock` isn't reliably present on macOS). Stale-lock guard: if the lock dir is older than 30 minutes, remove and re-acquire (an ingest run that hangs that long is dead).
- **Skip condition for ingest:** if `INBOX/` contains only `README.md`, exit 0 silently. Same logic as `.claude/hooks/inbox-check.sh:6-7`.
- **`WatchPaths` fires on every change inside `INBOX/`** — including when `/ingest` moves a file *out* via `git mv`. The script re-checks "is there still a non-README file?" before each iteration; once the queue drains, it exits cleanly. The next move-out fires the agent again but the re-check short-circuits.
- **Headless ingest invocation:** `claude -p "/ingest INBOX/<file>" --permission-mode bypassPermissions --dangerously-skip-permissions`. The trailing prompt also includes "This is an automated headless ingest; proceed without waiting for confirmation."
- **Backstop commit:** after each `claude -p` returns, if `git status --porcelain` is non-empty the wrapper does `git add -A && git commit -m "ingest | auto-backstop <file>" && git push origin unified`. `/ingest` is expected to handle this itself; the backstop is defense-in-depth.
- **Log rotation:** each script trims its log to the last 2000 lines after each run.

---

### Task 1: Bootstrap log dir, gitignore, lib helpers

**Files:**
- Create: `scripts/cron/log/.gitkeep`
- Create: `scripts/cron/_lib.sh`
- Modify: `.gitignore`

- [ ] **Step 1: Create the log directory placeholder**

```bash
mkdir -p scripts/cron/log
touch scripts/cron/log/.gitkeep
```

- [ ] **Step 2: Add ignore rules so logs and lockfile aren't tracked**

Append to `.gitignore`:

```gitignore

# Cron / LaunchAgent runtime state
scripts/cron/log/*
!scripts/cron/log/.gitkeep
scripts/cron/.lock/
```

- [ ] **Step 3: Create the shared helper library**

Write `scripts/cron/_lib.sh`:

```bash
#!/bin/bash
# Shared helpers for ds-brain cron scripts. Source, don't execute.
#
# Provides:
#   REPO_DIR             — absolute path to repo root
#   LOG_DIR              — scripts/cron/log
#   LOCK_DIR             — scripts/cron/.lock
#   STALE_LOCK_SECONDS   — 1800 (30 min)
#   acquire_lock <name>  — mkdir-based atomic mutex; returns 0 if held, 1 if busy
#   release_lock         — rmdir the lock
#   log_to <file> <msg>  — timestamped append, then trim to 2000 lines
#   trim_log <file>      — keep only the last 2000 lines

set -euo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
LOG_DIR="${REPO_DIR}/scripts/cron/log"
LOCK_DIR="${REPO_DIR}/scripts/cron/.lock"
STALE_LOCK_SECONDS=1800

mkdir -p "$LOG_DIR"

acquire_lock() {
  local owner="${1:-unknown}"
  if mkdir "$LOCK_DIR" 2>/dev/null; then
    echo "$owner $$ $(date -u +%FT%TZ)" > "$LOCK_DIR/owner"
    return 0
  fi
  # Stale check
  if [ -d "$LOCK_DIR" ]; then
    local age
    age=$(($(date +%s) - $(stat -f %m "$LOCK_DIR")))
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

- [ ] **Step 4: Make it executable (not strictly needed for source but harmless)**

```bash
chmod +x scripts/cron/_lib.sh
```

- [ ] **Step 5: Smoke-test the helper**

```bash
bash -c 'source scripts/cron/_lib.sh && acquire_lock test && echo "acquired"; release_lock && echo "released"'
```

Expected output:
```
acquired
released
```

- [ ] **Step 6: Commit**

```bash
git add scripts/cron/_lib.sh scripts/cron/log/.gitkeep .gitignore
git commit -m "schema | scaffold cron lib + log dir for ds-brain automation"
```

---

### Task 2: Write the git-pull script

**Files:**
- Create: `scripts/cron/git-pull.sh`

- [ ] **Step 1: Create the script**

Write `scripts/cron/git-pull.sh`:

```bash
#!/bin/bash
# Fast-forward pull of origin/unified. Designed to be safe under concurrent
# manual git work because it (a) takes the shared cron mutex and (b) refuses
# anything beyond a fast-forward.
#
# Run by LaunchAgent com.cybereason.ds-brain.git-pull every 300s.

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

# Only touch unified. If someone has checked out another branch, skip.
current_branch=$(git rev-parse --abbrev-ref HEAD)
if [ "$current_branch" != "unified" ]; then
  log_to "$LOG" "skip: branch is '$current_branch', not 'unified'"
  exit 0
fi

# Bail if working tree dirty — never pull over uncommitted work.
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
  # Quiet: keep log clean. Only note the no-op every ~hour by checking minute.
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

- [ ] **Step 2: Make it executable**

```bash
chmod +x scripts/cron/git-pull.sh
```

- [ ] **Step 3: Run it manually and inspect the log**

```bash
./scripts/cron/git-pull.sh && tail -n 5 scripts/cron/log/git-pull.log
```

Expected: exit 0, log shows either nothing new (silent) or an `up-to-date` / `fast-forwarded` line.

- [ ] **Step 4: Run it twice rapidly to exercise the mutex**

```bash
./scripts/cron/git-pull.sh &
./scripts/cron/git-pull.sh
wait
tail -n 5 scripts/cron/log/git-pull.log
```

Expected: one run logs success, the other logs `skip: lock busy` (or both succeed if the first finished too fast — either is fine; the mutex is not crashing).

- [ ] **Step 5: Commit**

```bash
git add scripts/cron/git-pull.sh
git commit -m "schema | add git-pull cron script for ds-brain automation"
```

---

### Task 3: Write the inbox-ingest script

**Files:**
- Create: `scripts/cron/inbox-ingest.sh`

- [ ] **Step 1: Create the script**

Write `scripts/cron/inbox-ingest.sh`:

```bash
#!/bin/bash
# Auto-ingest every non-README file in INBOX/ via `claude -p "/ingest …"`.
# Triggered by LaunchAgent com.cybereason.ds-brain.inbox-ingest on WatchPaths
# changes to INBOX/. Can also be run manually.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=./_lib.sh
source "$SCRIPT_DIR/_lib.sh"

LOG="${LOG_DIR}/inbox-ingest.log"
CLAUDE_BIN="${CLAUDE_BIN:-$HOME/.local/bin/claude}"

cd "$REPO_DIR"

list_pending() {
  # Print one non-README file name per line; nothing if INBOX is empty.
  ls -1 "$REPO_DIR/INBOX" 2>/dev/null \
    | grep -v '^README\.md$' \
    | grep -v '^\.' \
    || true
}

# Early no-op (cheap, runs before lock contention).
if [ -z "$(list_pending)" ]; then
  exit 0
fi

if ! acquire_lock "inbox-ingest"; then
  log_to "$LOG" "skip: lock busy"
  exit 0
fi
trap 'release_lock' EXIT

# Refuse to run if branch isn't unified or tree is dirty — keep the
# automation conservative.
current_branch=$(git rev-parse --abbrev-ref HEAD)
if [ "$current_branch" != "unified" ]; then
  log_to "$LOG" "skip: branch is '$current_branch', not 'unified'"
  exit 0
fi
if ! git diff --quiet || ! git diff --cached --quiet; then
  log_to "$LOG" "skip: working tree dirty"
  exit 0
fi

processed=0
while true; do
  pending="$(list_pending)"
  [ -z "$pending" ] && break

  # Pick first file deterministically (sorted).
  file="$(printf '%s\n' "$pending" | sort | head -n 1)"
  path="INBOX/$file"

  log_to "$LOG" "begin: $path"

  prompt="/ingest $path

This is an automated headless ingest run from scripts/cron/inbox-ingest.sh.
Proceed through all phases without waiting for confirmation. Auto-commit and
push on completion per the ingest spec."

  if "$CLAUDE_BIN" -p "$prompt" \
        --permission-mode bypassPermissions \
        --dangerously-skip-permissions \
        >> "$LOG" 2>&1; then
    log_to "$LOG" "ok: $path (claude -p exit 0)"
  else
    rc=$?
    log_to "$LOG" "fail: $path (claude -p exit $rc) — leaving file in place"
    # Don't loop forever on a poison-pill file. Bail.
    exit "$rc"
  fi

  # Backstop: if /ingest didn't commit cleanly, do it now.
  if [ -n "$(git status --porcelain)" ]; then
    log_to "$LOG" "backstop: committing residual changes"
    git add -A
    git commit -m "ingest | auto-backstop after $file" >> "$LOG" 2>&1 || true
    git push origin unified >> "$LOG" 2>&1 || \
      log_to "$LOG" "backstop: push failed"
  fi

  processed=$((processed + 1))
  # Safety cap — don't process more than 10 files in one launchd fire.
  if [ "$processed" -ge 10 ]; then
    log_to "$LOG" "cap: processed 10 files, deferring rest to next fire"
    break
  fi
done

if [ "$processed" -gt 0 ]; then
  log_to "$LOG" "done: processed $processed file(s)"
fi
```

- [ ] **Step 2: Make it executable**

```bash
chmod +x scripts/cron/inbox-ingest.sh
```

- [ ] **Step 3: Dry-run when INBOX is empty (except README)**

For now, temporarily move `INBOX/Strotz` out of the way so the empty path runs:

```bash
mv INBOX/Strotz Friedberg /tmp/Strotz Friedberg.bak
./scripts/cron/inbox-ingest.sh
echo "exit=$?"
mv /tmp/Strotz Friedberg.bak INBOX/Strotz Friedberg
```

Expected: exit 0, nothing appended to log (early no-op fires before any log line).

- [ ] **Step 4: Verify lock contention path**

```bash
mkdir -p scripts/cron/.lock && echo "test $$ $(date -u +%FT%TZ)" > scripts/cron/.lock/owner
./scripts/cron/inbox-ingest.sh
tail -n 3 scripts/cron/log/inbox-ingest.log
rm -rf scripts/cron/.lock
```

Expected: log shows `skip: lock busy` (only fires if INBOX has a pending file, which it does — `Strotz`).

- [ ] **Step 5: Commit (defer the live ingest test until Task 9)**

```bash
git add scripts/cron/inbox-ingest.sh
git commit -m "schema | add inbox-ingest cron script for ds-brain automation"
```

---

### Task 4: Add headless-mode note to /ingest command

**Files:**
- Modify: `.claude/commands/ingest.md`

- [ ] **Step 1: Append the headless-mode note**

Append at the end of `.claude/commands/ingest.md`, after the existing "Hard rules" section:

```markdown

## Headless / automated mode

If this command is invoked through `claude -p` (e.g. by
`scripts/cron/inbox-ingest.sh`), Step 2's "wait for go-ahead before
continuing" gate is **skipped**. Proceed straight through Phase A → B → C
→ D using your best judgement on the destination tab. The automated run
expects auto-commit + push to complete; do not stop and ask questions.

Signals you are in headless mode:
- The invoking prompt explicitly says "headless" / "automated" / "Proceed
  without waiting for confirmation".
- There is no human in the loop to answer.
```

- [ ] **Step 2: Commit**

```bash
git add .claude/commands/ingest.md
git commit -m "schema | document /ingest headless mode for cron automation"
```

---

### Task 5: Write the LaunchAgent plist templates

**Files:**
- Create: `scripts/cron/launchagents/com.cybereason.ds-brain.git-pull.plist.template`
- Create: `scripts/cron/launchagents/com.cybereason.ds-brain.inbox-ingest.plist.template`

- [ ] **Step 1: Create the templates directory**

```bash
mkdir -p scripts/cron/launchagents
```

- [ ] **Step 2: Write the git-pull plist template**

Write `scripts/cron/launchagents/com.cybereason.ds-brain.git-pull.plist.template`:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN"
  "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key>
  <string>com.cybereason.ds-brain.git-pull</string>

  <key>ProgramArguments</key>
  <array>
    <string>/bin/bash</string>
    <string>__REPO_PATH__/scripts/cron/git-pull.sh</string>
  </array>

  <key>StartInterval</key>
  <integer>300</integer>

  <key>RunAtLoad</key>
  <true/>

  <key>WorkingDirectory</key>
  <string>__REPO_PATH__</string>

  <key>EnvironmentVariables</key>
  <dict>
    <key>PATH</key>
    <string>/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin</string>
    <key>HOME</key>
    <string>__HOME_PATH__</string>
  </dict>

  <key>StandardOutPath</key>
  <string>__REPO_PATH__/scripts/cron/log/git-pull.launchd.out</string>
  <key>StandardErrorPath</key>
  <string>__REPO_PATH__/scripts/cron/log/git-pull.launchd.err</string>
</dict>
</plist>
```

- [ ] **Step 3: Write the inbox-ingest plist template**

Write `scripts/cron/launchagents/com.cybereason.ds-brain.inbox-ingest.plist.template`:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN"
  "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key>
  <string>com.cybereason.ds-brain.inbox-ingest</string>

  <key>ProgramArguments</key>
  <array>
    <string>/bin/bash</string>
    <string>__REPO_PATH__/scripts/cron/inbox-ingest.sh</string>
  </array>

  <key>WatchPaths</key>
  <array>
    <string>__REPO_PATH__/INBOX</string>
  </array>

  <key>ThrottleInterval</key>
  <integer>30</integer>

  <key>RunAtLoad</key>
  <false/>

  <key>WorkingDirectory</key>
  <string>__REPO_PATH__</string>

  <key>EnvironmentVariables</key>
  <dict>
    <key>PATH</key>
    <string>/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin</string>
    <key>HOME</key>
    <string>__HOME_PATH__</string>
  </dict>

  <key>StandardOutPath</key>
  <string>__REPO_PATH__/scripts/cron/log/inbox-ingest.launchd.out</string>
  <key>StandardErrorPath</key>
  <string>__REPO_PATH__/scripts/cron/log/inbox-ingest.launchd.err</string>
</dict>
</plist>
```

`ThrottleInterval: 30` means even if `WatchPaths` fires repeatedly (e.g. while `/ingest` is moving files), launchd waits at least 30s between starts — combined with the mutex this prevents thrash.

- [ ] **Step 4: Commit**

```bash
git add scripts/cron/launchagents/
git commit -m "schema | add LaunchAgent plist templates for ds-brain automation"
```

---

### Task 6: Write the install script

**Files:**
- Create: `scripts/cron/install.sh`

- [ ] **Step 1: Write `install.sh`**

Write `scripts/cron/install.sh`:

```bash
#!/bin/bash
# Render LaunchAgent plists from templates (substituting absolute paths),
# copy to ~/Library/LaunchAgents/, and bootstrap them via launchctl.
#
# Idempotent: re-running replaces the installed plists and reloads the
# agents.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_DIR="$(cd "$SCRIPT_DIR/../.." && pwd)"
TEMPLATE_DIR="$SCRIPT_DIR/launchagents"
TARGET_DIR="$HOME/Library/LaunchAgents"
UID_VAL=$(id -u)

mkdir -p "$TARGET_DIR"

agents=(
  "com.cybereason.ds-brain.git-pull"
  "com.cybereason.ds-brain.inbox-ingest"
)

for label in "${agents[@]}"; do
  src="$TEMPLATE_DIR/${label}.plist.template"
  dst="$TARGET_DIR/${label}.plist"

  if [ ! -f "$src" ]; then
    echo "error: missing template $src" >&2
    exit 1
  fi

  # Bootout if already loaded; ignore failure (might not be loaded yet).
  launchctl bootout "gui/$UID_VAL/$label" 2>/dev/null || true

  # Substitute placeholders.
  sed \
    -e "s|__REPO_PATH__|${REPO_DIR}|g" \
    -e "s|__HOME_PATH__|${HOME}|g" \
    "$src" > "$dst"

  launchctl bootstrap "gui/$UID_VAL" "$dst"
  echo "installed: $label"
done

echo
echo "Verify:"
echo "  launchctl print gui/$UID_VAL/com.cybereason.ds-brain.git-pull"
echo "  launchctl print gui/$UID_VAL/com.cybereason.ds-brain.inbox-ingest"
echo "  tail -f $REPO_DIR/scripts/cron/log/*.log"
```

- [ ] **Step 2: Write `uninstall.sh`**

Write `scripts/cron/uninstall.sh`:

```bash
#!/bin/bash
# Stop and remove the ds-brain LaunchAgents.
set -euo pipefail

UID_VAL=$(id -u)
TARGET_DIR="$HOME/Library/LaunchAgents"

for label in \
  "com.cybereason.ds-brain.git-pull" \
  "com.cybereason.ds-brain.inbox-ingest"
do
  launchctl bootout "gui/$UID_VAL/$label" 2>/dev/null || true
  rm -f "$TARGET_DIR/${label}.plist"
  echo "removed: $label"
done
```

- [ ] **Step 3: Make both executable**

```bash
chmod +x scripts/cron/install.sh scripts/cron/uninstall.sh
```

- [ ] **Step 4: Commit**

```bash
git add scripts/cron/install.sh scripts/cron/uninstall.sh
git commit -m "schema | add install/uninstall scripts for ds-brain LaunchAgents"
```

---

### Task 7: Install the LaunchAgents and verify boot

**Files:** none modified — runtime action only.

- [ ] **Step 1: Install**

```bash
./scripts/cron/install.sh
```

Expected output ends with two `installed:` lines plus the `Verify:` block.

- [ ] **Step 2: Confirm both agents are loaded**

```bash
launchctl list | grep ds-brain
```

Expected: two lines, one per label. The PID column may be `-` (idle) — that's normal for an interval-triggered job between fires.

- [ ] **Step 3: Confirm the git-pull agent fired on load**

```bash
sleep 5 && tail -n 5 scripts/cron/log/git-pull.log
```

Expected: either a log line (recent UTC timestamp) or — if the log is still empty because the repo is already up-to-date and the minute isn't `:00` — nothing. Re-check `scripts/cron/log/git-pull.launchd.err` for any plist-parse errors; should be empty.

- [ ] **Step 4: Confirm the inbox-ingest agent is registered with WatchPaths**

```bash
launchctl print gui/$(id -u)/com.cybereason.ds-brain.inbox-ingest | grep -A2 'paths ='
```

Expected: the printout shows `INBOX` under the watched paths.

---

### Task 8: Verify the git-pull cycle end-to-end

**Files:** none — runtime verification.

- [ ] **Step 1: Make a no-op remote change to trigger a fast-forward**

From a different working copy (or via web UI on `cr-AviadCohen/ds-brain`), push a trivial commit to `origin/unified` — e.g. add a blank line to a scratch file in `wiki/Log/pulse.md`. If a separate working copy is inconvenient, skip this step; the agent will simply continue to log `up-to-date` until something else lands.

- [ ] **Step 2: Wait up to 5 minutes, then inspect the log**

```bash
sleep 310 && tail -n 5 scripts/cron/log/git-pull.log
```

Expected (if a new remote commit existed): a line `fast-forwarded <old> → <new>`. Otherwise: silent (the quiet up-to-date path).

- [ ] **Step 3: Confirm the local branch advanced**

```bash
git log --oneline -3
```

Expected: HEAD matches what's on `origin/unified`.

---

### Task 9: Verify the inbox-ingest cycle end-to-end

**Files:** none — runtime verification using a real test file.

- [ ] **Step 1: Drop a small test note into INBOX/**

```bash
cat > INBOX/test-automation-2026-05-17.md <<'EOF'
---
title: Cron automation smoke-test note
created: 2026-05-17
---

# Cron automation smoke-test

This file exists to verify that scripts/cron/inbox-ingest.sh picks up new
INBOX/ files and runs /ingest headlessly. Treat as a one-line synthesis;
file under wiki/Sources/ or delete after verification.
EOF
```

The plain `cp`/redirect should trigger a `WatchPaths` event within seconds.

- [ ] **Step 2: Watch the log live**

```bash
tail -f scripts/cron/log/inbox-ingest.log
```

Expected within ~30s (ThrottleInterval): lines `begin: INBOX/test-automation-2026-05-17.md`, then `claude -p` output streamed in, then `ok: …` or backstop/commit lines. Stop the tail with Ctrl-C once you see `done:` or `fail:`.

- [ ] **Step 3: Confirm the file moved out of INBOX/**

```bash
ls INBOX/
```

Expected: only `README.md` (and possibly the pre-existing `Strotz` file if that's still pending — note that one will *also* have been processed by the same agent fire; verify it was either ingested or is still present with a `fail:` log line explaining why).

- [ ] **Step 4: Confirm the commit + push landed**

```bash
git log --oneline -5
```

Expected: a recent `ingest | …` commit. Verify it's also on the remote:

```bash
git fetch origin unified && git log --oneline origin/unified -3
```

- [ ] **Step 5: If the run failed, inspect and fix**

If the log shows `fail: …`, read `scripts/cron/log/inbox-ingest.launchd.err` for plist-level errors, and the inline `claude -p` output earlier in `inbox-ingest.log` for ingest-level errors. Most likely fixes:
- `CLAUDE_BIN` path wrong → edit `scripts/cron/inbox-ingest.sh` and re-run manually.
- Permissions prompt blocked headless → confirm `--dangerously-skip-permissions` is in the args.
- `/ingest` failed mid-flight and left the file in place → manually `claude` interactive `/ingest` to recover, then revisit the script.

---

### Task 10: Document the automation

**Files:**
- Create: `docs/automation.md`

- [ ] **Step 1: Write the doc**

Write `docs/automation.md`:

```markdown
---
title: ds-brain Background Automation
type: doc
created: 2026-05-17
tags: [doc, automation, ops]
---

# Background automation

Two macOS LaunchAgents keep the vault in sync and process INBOX/ without
manual prodding.

| Agent label | Trigger | Script |
|---|---|---|
| `com.cybereason.ds-brain.git-pull` | every 300 s | `scripts/cron/git-pull.sh` |
| `com.cybereason.ds-brain.inbox-ingest` | file change in `INBOX/` (throttled to 30 s) | `scripts/cron/inbox-ingest.sh` |

Both scripts share a mutex (`scripts/cron/.lock/`) so they can't collide
with each other or with a manual `/ingest` session.

## Install / uninstall

```bash
./scripts/cron/install.sh    # one-time setup; idempotent
./scripts/cron/uninstall.sh  # remove
```

`install.sh` renders the plist templates in `scripts/cron/launchagents/`
with absolute paths and bootstraps them under `gui/$(id -u)`.

## Inspect

```bash
launchctl list | grep ds-brain
launchctl print gui/$(id -u)/com.cybereason.ds-brain.git-pull
launchctl print gui/$(id -u)/com.cybereason.ds-brain.inbox-ingest
tail -f scripts/cron/log/git-pull.log scripts/cron/log/inbox-ingest.log
```

## Conservative behaviour

Both scripts **skip** (no error) when:
- Current branch is not `unified`.
- Working tree is dirty.
- The shared mutex is held.

`git-pull.sh` refuses anything beyond a fast-forward. If
`origin/unified` has diverged from local, it logs and exits non-zero;
resolution is manual.

`inbox-ingest.sh` calls `claude -p "/ingest <path>" --dangerously-skip-permissions`
and trusts `/ingest`'s commit + push. A backstop `git add -A && git commit
&& git push` runs after each invocation in case anything was left
uncommitted.

## Failure modes worth knowing

- **Headless `/ingest` hangs**: the mutex has a 30-minute stale-lock
  guard. After that, the next fire will steal the lock and proceed.
- **Push rejected** (e.g. someone else also pushed): `git pull --ff-only`
  on the next 5-min tick reconciles, and the next INBOX event ingests
  fresh.
- **Plist parse error**: check `scripts/cron/log/*.launchd.err` for the
  exact line launchd choked on; re-run `install.sh` after fixing the
  template.
```

- [ ] **Step 2: Commit**

```bash
git add docs/automation.md
git commit -m "schema | document ds-brain background automation"
```

- [ ] **Step 3: Push everything**

```bash
git push origin unified
```

Expected: clean push, all 10 commits from this plan land on `origin/unified`.

---

## Rollback

If anything goes wrong:

```bash
./scripts/cron/uninstall.sh
```

This stops both agents and removes the plists from `~/Library/LaunchAgents/`.
The scripts and templates in the repo remain (committed) — re-install when
ready.

---

## Self-review notes

- **Spec coverage:** (1) every-5-min git pull → Task 2 + plist in Task 5 with `StartInterval: 300`. (2) auto-ingest on new INBOX file (except README) → Task 3's `list_pending` excludes README + `WatchPaths` in Task 5's plist + non-interactive `claude -p` invocation + post-ingest backstop commit/push. (3) "ingestion without questions to the user" → Task 4 documents headless mode in `/ingest`, Task 3 passes `--dangerously-skip-permissions` and an explicit "proceed without waiting" prompt addendum.
- **Cron vs launchd justification** is captured in the Architecture block at the top.
- **Conservative defaults** (skip on dirty tree / wrong branch, fast-forward only, mutex with stale-guard, throttle 30 s, 10-file cap per fire) are all locked into the code in Tasks 2 and 3.
