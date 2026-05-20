# ds-brain server

Scheduled automation for the ds-brain vault on a long-running Ubuntu VM.

A single `systemd --user` timer fires every N minutes, pulls the latest
`origin/unified`, scans `INBOX/` for new files, and for each file runs
`/auto-ingest` in a fresh `claude -p` session, opens a PR titled
`PR Auto-Inject - <description>`, and enables `--auto --squash` if the
diff stays inside configured blast-radius caps.

---

## Table of contents

1. [How it works (one fire)](#how-it-works-one-fire)
2. [Why this shape (council guardrails)](#why-this-shape-council-guardrails)
3. [Prerequisites](#prerequisites)
4. [VM provisioning (one-time, as root)](#vm-provisioning-one-time-as-root)
5. [Service-user setup (one-time, as the service user)](#service-user-setup-one-time-as-the-service-user)
6. [Install the daemon](#install-the-daemon)
7. [Verify and inspect](#verify-and-inspect)
8. [Configuration](#configuration)
9. [Troubleshooting](#troubleshooting)
10. [Uninstall](#uninstall)
11. [File layout](#file-layout)
12. [Future: source pullers](#future-source-pullers)
13. [Identity and accountability](#identity-and-accountability)

---

## How it works (one fire)

Each tick of the systemd timer runs `jobs/auto_ingest.py`. Per fire:

1. **Acquire mutex** at `server/state/.lock/`. Stale lock (>30 min) is stolen.
2. **Sanity-check repo state.** Branch must be `unified`, working tree clean. Skip otherwise.
3. **`git pull --ff-only origin unified`.** Plain git, no LLM. Diverged → abort with error.
4. **List pending INBOX files** (ignore `README.md`, dotfiles).
5. **Per pending file:**
   1. Hash content (SHA-256). Skip if ledger already has hash (idempotency — survives pull-rewrites of `INBOX/`).
   2. `git checkout -b auto-ingest/<UTC-timestamp>-<short-sha>` from `unified`.
   3. `claude -p "/auto-ingest <relative-path>" --permission-mode bypassPermissions`.
   4. Inspect resulting diff vs `unified`:
      - Cap: `caps.max_files_changed`
      - Cap: `caps.max_lines_changed`
      - Cap: every changed path matches `repo.path_allowlist` (default `wiki/**`, `raw/**`, `INBOX/**`)
   5. Push bot branch to origin.
   6. `gh pr create --base unified --head <bot-branch> --title "PR Auto-Inject - <description>"`.
   7. Caps passed → `gh pr merge <PR> --auto --squash` (waits for required checks if any).
   8. Caps exceeded → label PR `needs-review`, leave open.
   9. Record content hash in ledger.
   10. Checkout `unified`, delete local bot branch.
6. **Release mutex.**

Idempotent. Crash-safe: ledger updated only after PR open, so a crash mid-ingest retries the file next fire (one Claude session wasted, no double-commit).

---

## Why this shape (council guardrails)

The original plan was reviewed by an LLM council. Findings and how this server addresses them:

| Council finding | Mitigation |
|---|---|
| `PathModified=INBOX/` + 5-min `git pull` is a self-firing loop | Single timer; no inotify; pull happens inside the timer fire under mutex |
| Distributed-write conflict on hot files (`wiki/INDEX.md`, `wiki/Log/wiki-ops.md`) | PR + `gh pr merge --auto --squash` — GitHub serializes the merge, not the VM |
| `--dangerously-skip-permissions` headless = prompt-injection-to-RCE | Uses `--permission-mode bypassPermissions` only; `guard_immutable.py` PreToolUse hook stays active |
| `git add -A` backstop commits stray files / secrets | Wrapper owns branching; only the bot-branch diff lands in the PR; path allowlist enforces what's allowed |
| Multiple commits per ingest = hard revert | Squash-merge → one revertable commit per ingest |
| No idempotency, re-ingest after pull rewrites INBOX | Content-hash ledger keyed by SHA-256 of file content |
| No audit trail | Every ingest = one PR titled `PR Auto-Inject - …`; auditor scans PR list weekly |
| No human-noticeable failure mode | Caps exceeded → PR stays open + labeled `needs-review` (auto-merge disabled) |

Open work not yet mitigated:

- **Wiki-layer integrity.** `/auto-ingest` can rewrite `wiki/Decisions/`, `wiki/🔥 Hot Notes/Active Focus.md`, etc. Future: per-path caps in `config.yaml`.
- **Content-trust compounding.** Auto-ingested syntheses must carry `provenance: auto-ingest` frontmatter so `/query` and future `/ingest` runs can treat them as lower-trust on retrieval. Owned by the `/auto-ingest` command spec.

---

## Prerequisites

VM: Ubuntu 22.04+ with systemd ≥ 245 (path units, user lingering).

Binaries (installed below):
- `git`
- `python` ≥ 3.10
- `uv` (Python env manager) — https://docs.astral.sh/uv/
- `gh` (GitHub CLI) — https://cli.github.com/
- `claude` (Claude Code CLI) — must be logged in once interactively so `~/.claude/` carries the auth token

Identity:
- Owner's GitHub PAT (Aviad's — `repo` + `workflow` scopes).
- Owner's Anthropic / Claude Code subscription (the headless `claude -p` session bills against this account).

---

## VM provisioning (one-time, as root)

```bash
# Base packages.
sudo apt update
sudo apt install -y git python3 python3-venv curl

# Dedicated service user (recommended).
sudo useradd --create-home --shell /bin/bash dsbrain

# Lingering — so systemd --user runs without an active login.
sudo loginctl enable-linger dsbrain
```

---

## Service-user setup (one-time, as the service user)

Switch to the service user:

```bash
sudo -iu dsbrain
```

Install `uv`:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
exec $SHELL   # reload PATH so ~/.local/bin/uv is found
uv --version
```

Install `gh` and authenticate with the **owner's PAT** (scopes: `repo`, `workflow`):

```bash
# Install gh — see https://cli.github.com/ for current instructions.
type -p curl >/dev/null || sudo apt install curl -y
curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg
sudo chmod go+r /usr/share/keyrings/githubcli-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null
sudo apt update && sudo apt install gh -y

gh auth login   # follow prompts, paste the PAT
gh auth status  # verify
```

Install the Claude Code CLI and log in once interactively:

```bash
# Follow Anthropic's install instructions for the Linux Claude Code CLI.
claude --version
claude          # launches TUI; complete login flow, then exit with /quit
ls ~/.claude/   # confirm auth token file exists
```

Clone the repo into the service user's home (path is configurable — `setup.py` discovers it from its own location):

```bash
cd ~
git clone https://github.com/cybereason-labs/ds-brain.git
cd ds-brain
git checkout unified
```

---

## Install the daemon

From inside the repo:

```bash
cd ~/ds-brain/server
uv sync                       # bootstrap .venv from uv.lock (pyyaml only)
uv run python setup.py        # render + install systemd units, enable timer
```

`setup.py` is idempotent. Re-run after any edit to `config.yaml` (so changes to `schedule.auto_ingest_interval_minutes` re-render the timer unit).

Expected output ends with a verification block:

```
rendered: ~/.config/systemd/user/dsbrain-auto-ingest.service
rendered: ~/.config/systemd/user/dsbrain-auto-ingest.timer

Lingering check:
  linger: enabled ✓

Verify:
  systemctl --user list-timers | grep dsbrain
  ...
```

---

## Verify and inspect

```bash
# Timer scheduled?
systemctl --user list-timers | grep dsbrain

# Timer + service status.
systemctl --user status dsbrain-auto-ingest.timer
systemctl --user status dsbrain-auto-ingest.service

# Journal logs (systemd-captured stdout/stderr).
journalctl --user -u dsbrain-auto-ingest.service -n 50
journalctl --user -u dsbrain-auto-ingest.service -f

# Application logs (timestamped append-only).
tail -f server/state/logs/auto_ingest.log
tail -f server/state/logs/auto_ingest.systemd.log

# Trigger an immediate fire (for manual testing).
systemctl --user start dsbrain-auto-ingest.service
```

**Before trusting the timer**, manually validate the end-to-end Claude path:

```bash
cd ~/ds-brain
# Drop a small test note into INBOX/ for the smoke test.
cat > INBOX/test-automation-$(date -u +%Y-%m-%d).md <<'EOF'
---
title: Automation smoke-test
created: 2026-05-20
---

# Smoke test

This file verifies that the auto-ingest daemon picks up a new INBOX file,
runs /auto-ingest, opens a PR, and (caps permitting) merges automatically.
EOF

# Manually fire the job once (don't wait for the timer).
systemctl --user start dsbrain-auto-ingest.service
journalctl --user -u dsbrain-auto-ingest.service -f
```

Expected within a few minutes: `begin: …`, `claude rc=0`, `auto-merge enabled: … → https://github.com/.../pull/<N>`, the PR appears in GitHub, gets squash-merged.

---

## Configuration

Everything lives in `server/config.yaml`. See the inline comments there for full schema. Key knobs:

| Key | Default | Meaning |
|---|---|---|
| `schedule.auto_ingest_interval_minutes` | `5` | Timer cadence |
| `caps.max_files_changed` | `20` | Auto-merge blocked if diff touches more files |
| `caps.max_lines_changed` | `2000` | Auto-merge blocked if diff exceeds this |
| `repo.path_allowlist` | `wiki/** raw/** INBOX/**` | Auto-merge blocked if any changed path doesn't match |
| `pr.title_prefix` | `PR Auto-Inject - ` | Prefix for every auto-generated PR title |
| `pr.merge_strategy` | `squash` | `squash` / `merge` / `rebase` |
| `pr.needs_review_label` | `needs-review` | Label applied when caps exceeded |
| `claude.permission_mode` | `bypassPermissions` | Keeps PreToolUse hooks active |
| `claude.timeout_minutes` | `20` | Hard timeout per `claude -p` call |
| `mutex.stale_seconds` | `1800` | Stolen if held longer (30 min) |

After editing, re-run `uv run python setup.py` to re-render unit files if you changed the schedule.

---

## Troubleshooting

**Timer doesn't fire.**
- `loginctl show-user dsbrain | grep Linger` — must be `Linger=yes`.
- `systemctl --user list-timers` — does the timer show with a `NEXT` time?
- `journalctl --user -u dsbrain-auto-ingest.service -n 100`.

**`claude` CLI not found by systemd.**
- Service template hardcodes `PATH=__HOME_PATH__/.local/bin:/usr/local/bin:/usr/bin:/bin`. If `claude` lives elsewhere, create a drop-in:
  ```bash
  mkdir -p ~/.config/systemd/user/dsbrain-auto-ingest.service.d
  cat > ~/.config/systemd/user/dsbrain-auto-ingest.service.d/path.conf <<'EOF'
  [Service]
  Environment=PATH=/path/to/claude/dir:/usr/local/bin:/usr/bin:/bin
  EOF
  systemctl --user daemon-reload
  ```

**`claude -p` hangs on first run.**
- It expects auth; log in once interactively as the service user: `claude` → complete flow → exit.

**`gh pr create` fails with auth error.**
- `gh auth status` must show authenticated. Re-run `gh auth login` as the service user.

**Push rejected (`! [rejected] unified -> unified (non-fast-forward)`).**
- Someone pushed to `unified` between the bot's pull and its push. The next timer fire will pull and retry. Persistent failure → check for divergence: `git fetch origin unified && git log HEAD..origin/unified --oneline`.

**Caps exceeded on every fire.**
- A single INBOX file is producing a huge synthesis. Either the `/auto-ingest` command is misbehaving, or the file legitimately needs a big change. Inspect the PR labeled `needs-review`; merge by hand if OK, then either raise caps in `config.yaml` or tighten `/auto-ingest`.

**Ledger says "already processed" but PR isn't visible.**
- `server/state/processed.json` records the hash → PR URL map. `cat server/state/processed.json | jq '. | to_entries | map(.value.pr)'`. If the PR was closed without merging and the file is still in INBOX, manually delete that hash from the ledger to allow retry.

**Stale lock.**
- Auto-stolen after 30 min. To force-clear: `rm -rf server/state/.lock/`.

---

## Uninstall

```bash
systemctl --user disable --now dsbrain-auto-ingest.timer
rm ~/.config/systemd/user/dsbrain-auto-ingest.{timer,service}
systemctl --user daemon-reload
```

Repo files (templates, scripts, config) remain — re-install by re-running `setup.py`.

Linger is intentionally left intact. Disable manually if no longer needed:

```bash
sudo loginctl disable-linger dsbrain
```

---

## File layout

```
server/
  config.yaml           # single source of truth — caps, paths, schedule
  setup.py              # idempotent installer
  pyproject.toml        # uv-managed env (pyyaml only)
  uv.lock
  README.md             # this file
  jobs/
    auto_ingest.py      # entry point — invoked by the timer
    sources/            # future: Slack/Gmail/RSS pullers (one module each)
  lib/
    config.py           # config loader
    mutex.py            # mkdir-based atomic lock
    ledger.py           # content-hash processed-files store
    git_safe.py         # ff-only pull, branch ops, diff inspection, allowlist
    pr.py               # gh CLI wrapper — create + label + --auto --squash
    claude_runner.py    # subprocess wrapper for `claude -p`
    logging.py          # timestamped append-only logger
  units/
    dsbrain-auto-ingest.service.template
    dsbrain-auto-ingest.timer.template
  state/                # runtime — gitignored
    logs/
      auto_ingest.log         # app log
      auto_ingest.systemd.log # captured stdout/stderr
    .lock/                    # mutex
    processed.json            # content-hash ledger
```

---

## Future: source pullers

`server/jobs/sources/` is the home for scheduled pullers that deposit files into `INBOX/`. Each puller is a Python module with its own systemd timer. Enable by adding to `config.yaml`:

```yaml
sources:
  enabled:
    - slack_digest
    - gmail_calendar
    - granola_recordings
```

Each source-puller fires on its own cadence → drops into `INBOX/` → next `auto_ingest` fire picks it up. Same ledger, same caps, same PR flow.

Candidates (council Expansionist suggestions):

- Slack channel digest → daily summary into `INBOX/`
- Gmail/Calendar webhook → meeting invites + decks pre-ingested
- Granola/Otter/Fathom recordings → auto-routed
- GitHub PR descriptions from `cybereason-labs/*` DS repos → engineering decisions captured
- Arxiv/HN/vendor RSS pre-filtered by wiki concept tags

---

## Identity and accountability

All commits and PRs are made under the GitHub identity of the PAT configured via `gh auth`. Currently the **owner's (Aviad's) PAT**. The Claude session also bills against the owner's Claude Code subscription.

Consequence: every `PR Auto-Inject - …` PR is attributable to the owner. The owner is on the hook for hallucinations, misattributions, and content errors. The caps gate + `needs-review` label exist precisely so the owner doesn't have to read every PR before merge.

If the bot ever pushes something embarrassing or wrong:

1. `gh pr list --search "PR Auto-Inject"` to locate.
2. `gh pr view <N>` to inspect the diff.
3. If already merged: `git revert <squash-merge-sha>` on `unified`, push.
4. Delete the offending content's hash from `server/state/processed.json` so the source file (if still in `INBOX/`) can be re-ingested cleanly.
