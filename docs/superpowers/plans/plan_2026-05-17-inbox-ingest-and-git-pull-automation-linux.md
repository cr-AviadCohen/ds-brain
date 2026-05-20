# INBOX Auto-Ingest Automation (Ubuntu VM / systemd / `server/`) Implementation Plan

> **Status — 2026-05-20:** First version of this plan was reviewed by an LLM council and rejected as written (PathModified+pull race, prompt-injection-to-RCE via `--dangerously-skip-permissions`, distributed-write conflict on hot files, no idempotency, no audit trail). The current version below incorporates every council fix and matches the code actually scaffolded under `server/` on 2026-05-20.

**Goal:** On a long-running Ubuntu VM, every 5 minutes pull `origin/unified` and process every new file in `INBOX/` (except `README.md` and dotfiles) through a fresh headless `claude -p "/auto-ingest <path>"` session, opening a PR titled `PR Auto-Inject - <description>` and auto-merging it via `gh pr merge --auto --squash` when blast-radius caps pass.

**Architecture (final shape):** One `systemd --user` timer fires `jobs/auto_ingest.py` every `auto_ingest_interval_minutes`. The Python entry-point owns the full lifecycle: mutex → branch+clean check → `git pull --ff-only` → INBOX scan → per-file (ledger check → bot branch → `claude -p` → diff inspect → push → PR → auto-merge or `needs-review` label → ledger record → cleanup). All knobs live in `server/config.yaml`.

---

## Why this shape (council findings → mitigations)

| Council finding (original plan) | Mitigation in the final design |
|---|---|
| `PathModified=INBOX/` + 5-min `git pull` is a self-firing loop (Contrarian) | No inotify/path-watcher. Single timer. `git pull` happens **inside** the timer fire, under mutex. |
| Distributed-write conflict on `wiki/INDEX.md`, `wiki/Log/wiki-ops.md` (Reviewer 3) | PR + `gh pr merge --auto --squash` — GitHub serializes the merge, not the VM. Per-VM mutex is no longer load-bearing for correctness. |
| `--dangerously-skip-permissions` headless = prompt-injection-to-RCE (Outsider, Reviewer 2) | Use `--permission-mode bypassPermissions` only. `scripts/hooks/guard_immutable.py` PreToolUse hook stays active. |
| `git add -A` commits stray files / leaked secrets (Outsider) | Wrapper owns branching. Only the bot-branch diff lands in the PR. Path allowlist (`wiki/**`, `raw/**`, `INBOX/**`) enforced as a cap. |
| Multiple commits per ingest = hard revert | Squash-merge → one revertable commit per ingest. |
| No idempotency, replays after pull rewrites INBOX (Contrarian) | Content-hash ledger keyed by SHA-256 of file content, survives renames + pulls. |
| No audit trail, garbage compounds (Outsider) | Every ingest is one PR titled `PR Auto-Inject - …`. Owner skims PR list weekly. |
| `claude -p` headless behavior unverified (Executor) | Manual smoke-test is the **first** step before any systemd glue. |
| Expansion premature (all 3 reviewers on Expansionist) | `server/jobs/sources/` exists as an empty hook point but is deliberately not built until the INBOX path is proven stable. |

Open items not in scope of this plan (tracked in `server/README.md`):
- Per-path caps inside `wiki/` (e.g. extra guard around `wiki/Decisions/`).
- `provenance: auto-ingest` frontmatter stamping (owned by `.claude/commands/auto-ingest.md`).

---

## Locked decisions (recap from review thread)

- **Single timer**, fires every 5 minutes. No separate git-pull timer.
- **PR + `gh pr merge --auto --squash`** — never direct push to `unified` from the bot. Caps-exceeded PRs labelled `needs-review`.
- **PR title prefix:** `PR Auto-Inject - `.
- **Caps:** `max_files_changed=20`, `max_lines_changed=2000`, path allowlist `wiki/** raw/** INBOX/**`. Single source of truth: `server/config.yaml`.
- **Identity:** owner's GitHub PAT (Aviad) via `gh auth login`. Claude bills against the owner's Claude Code subscription.
- **Python `setup.py`** (uv-managed env), under `server/` (matches `tools/` precedent of per-dir venv).
- **`/auto-ingest` slash command** (`.claude/commands/auto-ingest.md`) stays the contract — autonomous, no clarifying questions. The Python wrapper does **not** modify the command at runtime.

---

## File layout (matches `server/` as scaffolded)

```
server/
  config.yaml                 # single source of truth — caps, paths, schedule
  setup.py                    # idempotent installer
  pyproject.toml + uv.lock    # uv-managed env (pyyaml only)
  README.md                   # full setup walkthrough + troubleshooting
  jobs/
    auto_ingest.py            # entry — timer invokes this
    sources/                  # future Slack/Gmail/RSS pullers (empty hook)
  lib/
    config.py                 # yaml loader
    mutex.py                  # mkdir atomic lock + 30-min stale-steal
    ledger.py                 # SHA-256 content-hash store
    git_safe.py               # ff-only pull, branch ops, diff inspect, allowlist
    pr.py                     # gh CLI wrapper — create + label + --auto --squash
    claude_runner.py          # subprocess wrapper for claude -p (timeout, rc)
    logging.py                # timestamped append-only logger + trim
  units/
    dsbrain-auto-ingest.service.template
    dsbrain-auto-ingest.timer.template
  state/                      # gitignored runtime
    logs/                     # auto_ingest.log + auto_ingest.systemd.log
    .lock/                    # mutex
    processed.json            # content-hash ledger
```

`.gitignore` updated to ignore `server/.venv/`, `server/state/.lock/`, `server/state/logs/*` (except `.gitkeep`), `server/state/processed.json{,.tmp,.corrupt}`, and `__pycache__` under `server/**`.

Relationship to other dirs:
- **`scripts/hooks/guard_immutable.py`** — kept. Active PreToolUse hook wired in `.claude/settings.json`. Runs inside every Claude session including the headless `claude -p` invoked by the daemon. Sole filesystem-level rail against prompt-injected writes to `raw/`.
- **`scripts/cron/weekly-lint.sh`** — kept. Separate weekly lint automation, unrelated to auto-ingest.
- **`tools/`** — kept. Local lint + convert utilities, separate uv env, unrelated to the VM daemon.

---

## One fire — what the daemon does

`jobs/auto_ingest.py` per tick:

1. Load `config.yaml`.
2. Acquire `server/state/.lock/` (`mkdir`-atomic). If lock is busy and not stale (>30 min), log `skip: lock busy` and exit 0.
3. Verify `git rev-parse --abbrev-ref HEAD == unified` and `git status --porcelain` is empty. Skip otherwise.
4. `git fetch origin unified` → check ancestry → `git merge --ff-only origin/unified`. Diverged → log + exit 1 (timer retries next fire; manual recovery needed for divergence).
5. Scan `INBOX/`, drop `README.md` and dotfiles.
6. For each pending file (alphabetical order):
   1. Compute SHA-256. If ledger has the hash → log `skip (ledger hit)`, continue.
   2. Record current `git rev-parse --short HEAD` as `base_sha`.
   3. `git checkout -b auto-ingest/<UTC-YYYYMMDD-HHMMSS>-<base_sha>`.
   4. `claude -p "/auto-ingest <relative-path>" --permission-mode bypassPermissions` with `timeout_minutes=20`.
   5. If `rc != 0` → log, abandon the bot branch (`checkout unified`, `branch -D bot-branch`), continue (no ledger record → retried next fire).
   6. `git diff --numstat unified...HEAD` → count files, lines, gather paths.
   7. If no diff → record ledger hit anyway (file was processed but produced no change), cleanup, continue.
   8. Compute `cap_exceeded = files > 20 or lines > 2000 or any(path ∉ allowlist)`.
   9. `git push -u origin <bot-branch>`.
   10. `gh pr create --base unified --head <bot-branch> --title "PR Auto-Inject - <description>" --body <…>`.
   11. If `cap_exceeded`: `gh pr edit <PR> --add-label needs-review`. **Do not auto-merge.**
   12. Else: `gh pr merge <PR> --auto --squash`.
   13. Record `{content_hash: {source: <path>, pr: <pr_url>}}` in `server/state/processed.json`.
   14. `git checkout unified && git branch -D <bot-branch>` (best-effort).
7. Release mutex.

Per-file errors are caught and logged; the loop continues to the next file. Per-fire errors (mutex, branch check, pull failure) abort the fire cleanly. No partial state leaks because the ledger is the only durable side-effect besides the PR.

---

## Tasks

These tasks reflect what was already implemented on 2026-05-20 (under `server/`). They are listed here so the plan and the code agree. Re-execute them only on a fresh VM.

### Task 1: Pre-flight checks on the VM

- [x] Ubuntu 22.04+ with systemd ≥ 245.
- [ ] Service user (recommended `dsbrain`) created. Lingering enabled.
- [ ] `git`, `python3 (>=3.10)`, `curl` installed.
- [ ] `uv`, `gh`, `claude` installed for the service user.
- [ ] `gh auth login` completed with owner PAT (scopes: `repo`, `workflow`). Verified via `gh auth status`.
- [ ] `claude` logged in once interactively. `~/.claude/` populated.
- [ ] Repo cloned to `~/ds-brain` on branch `unified`.

Detailed commands in `server/README.md` under **VM provisioning** and **Service-user setup**.

### Task 2: Manual smoke-test `claude -p "/auto-ingest"` (council Executor's #1 risk)

Before installing systemd units, validate the end-to-end Claude path:

- [ ] Drop a tiny test note into `INBOX/`.
- [ ] As the service user, run:
  ```bash
  cd ~/ds-brain
  claude -p "/auto-ingest INBOX/<test-file>.md" --permission-mode bypassPermissions
  ```
- [ ] Confirm: exits 0, produces a diff that respects `path_allowlist`, commits or leaves the diff cleanly stageable. Inspect `git status`.

If this step fails (auth, hang, MCP-in-no-TTY, slash command malformed), **stop and fix `/auto-ingest`** before continuing — every later task assumes a working `claude -p`.

### Task 3: Scaffold (DONE 2026-05-20)

- [x] `server/pyproject.toml` + `server/uv.lock` (pyyaml dep only).
- [x] `server/config.yaml` with all knobs.
- [x] `server/lib/{config,mutex,ledger,git_safe,pr,claude_runner,logging}.py`.
- [x] `server/jobs/auto_ingest.py`.
- [x] `server/units/dsbrain-auto-ingest.{service,timer}.template`.
- [x] `server/setup.py`.
- [x] `server/state/{,logs/}.gitkeep`.
- [x] `server/README.md` (full setup walkthrough).
- [x] `.gitignore` entries for `server/` runtime state.

### Task 4: Install on the VM

As the service user, from inside the cloned repo:

- [ ] `cd ~/ds-brain/server`
- [ ] `uv sync`  (bootstraps `.venv` from `uv.lock`)
- [ ] `uv run python setup.py`

`setup.py`:
1. Refuses to run as root.
2. Verifies `git`, `uv` on PATH.
3. Verifies `systemctl --user status` succeeds (linger or active session required).
4. Loads `config.yaml`.
5. Verifies `claude_bin` resolves; if missing, fails with hint to authenticate.
6. Verifies `gh_bin` resolves and `gh auth status` is OK.
7. Renders unit templates by substituting `__REPO_PATH__`, `__HOME_PATH__`, `__UV_BIN__`, `__INTERVAL_MINUTES__`.
8. Writes units under `~/.config/systemd/user/`.
9. `systemctl --user daemon-reload && systemctl --user enable --now dsbrain-auto-ingest.timer`.
10. Reports linger status; prints verification commands.

Idempotent — re-running after a `config.yaml` edit re-renders the templates.

### Task 5: Verify on the VM

- [ ] `systemctl --user list-timers | grep dsbrain` — `NEXT` time within `auto_ingest_interval_minutes`.
- [ ] `systemctl --user status dsbrain-auto-ingest.timer` — `Active: active (waiting)`.
- [ ] `systemctl --user start dsbrain-auto-ingest.service` — fires the job immediately.
- [ ] `journalctl --user -u dsbrain-auto-ingest.service -n 50 --no-pager` — clean exit.
- [ ] `tail -n 50 server/state/logs/auto_ingest.log` — expected `git: up-to-date` or `git: fast-forwarded`, plus any per-file ingest lines.

### Task 6: End-to-end ingest verification

- [ ] Drop a small test note into `INBOX/`:
  ```bash
  cat > INBOX/test-auto-ingest-$(date -u +%Y-%m-%d).md <<'EOF'
  ---
  title: Auto-ingest smoke-test
  created: 2026-05-20
  ---
  # Smoke test
  Single paragraph note to exercise the auto-ingest daemon end to end.
  EOF
  ```
- [ ] Either wait for the next timer fire, or `systemctl --user start dsbrain-auto-ingest.service`.
- [ ] Watch logs:
  ```bash
  journalctl --user -u dsbrain-auto-ingest.service -f
  tail -f server/state/logs/auto_ingest.log
  ```
- [ ] Confirm a `PR Auto-Inject - test auto-ingest …` PR appears at the repo. Confirm `--auto --squash` enabled. Wait for merge.
- [ ] Confirm `unified` advanced with a `auto-ingest |` (or squash-merge) commit.
- [ ] Confirm `INBOX/test-auto-ingest-…` is gone (moved by `/auto-ingest`, merged via PR).
- [ ] Confirm `server/state/processed.json` contains the hash + PR URL.

### Task 7: Failure-mode drills

Exercise each rail at least once:

- [ ] **Caps exceeded:** drop a deliberately huge file into INBOX; confirm PR is opened but **not** auto-merged, labelled `needs-review`.
- [ ] **Mutex contention:** start the service twice in quick succession; confirm one logs `skip: lock busy`.
- [ ] **Branch divergence:** push a conflicting commit to `unified` from another machine; confirm next fire logs `git pull failed: diverged …` and exits non-zero.
- [ ] **Stale lock:** `mkdir server/state/.lock && touch -d '1 hour ago' server/state/.lock`; confirm next fire steals it.
- [ ] **Ledger replay:** drop the same file content twice (different filename); confirm second fire logs `skip (ledger hit)`.

### Task 8: Document + commit

- [x] `server/README.md` (full walkthrough — done).
- [ ] Commit the `server/` tree + `.gitignore` updates: `git commit -m "schema | server/ auto-ingest daemon scaffold (council-revised)"`.
- [ ] Push: `git push origin unified`.
- [ ] Optionally archive the previous plan revision (`docs/superpowers/plans/plan_2026-05-17-inbox-ingest-and-git-pull-automation.md`, the macOS launchd variant) — the Linux/server design supersedes it for the VM use case.

---

## Rollback

```bash
systemctl --user disable --now dsbrain-auto-ingest.timer
rm ~/.config/systemd/user/dsbrain-auto-ingest.{timer,service}
systemctl --user daemon-reload
```

Repo files (`server/`) remain. Linger is intentionally left intact.

---

## Open questions / future work

- **Per-path caps** inside `wiki/` (`wiki/Decisions/` should require human review even within `path_allowlist`).
- **`provenance: auto-ingest` frontmatter** — `.claude/commands/auto-ingest.md` should stamp this on every page so `/query` retrieval can weight machine-ingested syntheses lower.
- **Source pullers** (`server/jobs/sources/`) — Slack digest, Gmail/Calendar, Granola recordings, GitHub PR descriptions, RSS feeds. Each as its own timer + module. Deliberately deferred until the INBOX path proves stable in production.
- **Alerting on cap-exceeded PRs.** Currently labelled and left open; consider a Slack webhook so the owner is notified rather than relying on periodic PR-list scans.
- **Secondary VM / failover.** Single VM is a single point of failure. If two VMs ever run the daemon concurrently against the same repo, the GitHub-side PR merge queue serializes correctly, but the content-hash ledger does not deduplicate across machines — same file on two VMs would produce two PRs (both content-identical, one will fail to merge as a duplicate diff). Not a correctness bug, just noise.
