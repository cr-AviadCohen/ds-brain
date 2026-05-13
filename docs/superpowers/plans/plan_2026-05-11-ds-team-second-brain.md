# DS-Team Second Brain Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use `superpowers:subagent-driven-development` (recommended) or `superpowers:executing-plans` to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Stand up a Karpathy-style "Wiki LLM" second brain for the Data Science team — a three-layer Obsidian-compatible repo where humans write raw inputs (`raw/`, `INBOX/`), Claude synthesises a navigable wiki (`wiki/`), and operations are encoded as slash-commands and hooks (`.claude/`).

**Architecture.** Three layers per Karpathy's gist (https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f):

| Layer | Path | Owner | Mutability |
|---|---|---|---|
| Raw | `raw/`, `INBOX/` | Humans + upstream systems | Append-only; Claude reads, never edits body |
| Wiki | `wiki/` | Claude | Full read/write under conventions |
| Schema | `CLAUDE.md`, `.claude/`, `tools/`, `scripts/` | DS leadership + Claude | Co-evolves |

Wiki is organised by DS-domain folders already laid out in this repo: `Entities/{People,Projects,Systems}`, `Meetings`, `Decisions`, `Ideas`, `Research`, `Syntheses`, `Sources`, `Connections`, `🔥 Hot Notes`, `🗺️ Maps`, `📦 Archive`, plus a new `Log/` and `Memories/`. Five slash commands (`/ingest`, `/query`, `/lint`, `/remove`, `/braindump`) drive day-to-day workflow. Deterministic lint at `tools/lint/run_all.py` checks frontmatter, orphans, stale links.

**Tech stack.** Markdown + YAML frontmatter; Obsidian Desktop client (Smart Connections plugin); Python ≥3.11 with `uv` virtualenv for lint/converters; Bash + `jq` for hooks; Git on `unified` branch with auto-push to `origin/unified`; Claude Code as the agentic runtime.

**Current state (2026-05-11).** Already in repo: 12 folder READMEs, two seed Source notes (`Karpathy — LLM Wiki Gist`, `LevelBlue — Acquisition of Cybereason`), one Hot Note (`Active Focus`), `.claude/settings.json` (permissions + SessionStart inbox hook). Missing: `CLAUDE.md`, `INDEX.md`, `Log/`, `Memories/README.md`, `Sources/README.md`, `Entities/README.md`, `🔥 Hot Notes/README.md`, all wiki content notes, `tools/`, `scripts/`, `INBOX/`. Raw layer is full: 50 people, 27 project folders, 6 meeting transcripts, 295 Cybereason KB files, plus Level Blue + DS Drive.

**Existing-convention drift to fix in Phase 2.** Existing Source and Hot Note files use tags like `[karpathy, llm-wiki, second-brain, schema]` or `[active, focus, hot]` — none of them carry the mandatory `wiki` layer tag the new schema requires. Phase 2 retags them.

**Parallelisation note.** Phase headers flag PARALLELISM where lanes are file-disjoint. Use `superpowers:dispatching-parallel-agents` — batch all independent reads in one message, all independent writes in one message. Lanes touching shared files (`INDEX.md`, `wiki-ops.md`, `CLAUDE.md`) merge sequentially.

---

## Phase 0 — Bootstrap missing scaffolding (sequential)

### Task 0.1: Land the `raw/INBOX` immutability guard script

**Files:**
- Create: `scripts/hooks/guard_immutable.py`
- Create: `scripts/__init__.py` (empty)
- Create: `scripts/hooks/__init__.py` (empty)

**Why.** The current `.claude/settings.json` has no PreToolUse guard. The Karpathy pattern hinges on raw-layer immutability; without a programmatic guard, an LLM agent will eventually edit a raw note. Add the guard and wire it in Task 0.3.

- [ ] **Step 1: Create directories**

```bash
mkdir -p scripts/hooks scripts/cron
```

- [ ] **Step 2: Write `scripts/hooks/guard_immutable.py`**

```python
#!/usr/bin/env python3
"""PreToolUse:Bash + PreToolUse:Write guard.

Blocks shell commands and file writes that mutate raw/ or INBOX/. The raw
layer is human-authored and immutable to Claude. Allows reads, allows
`git mv INBOX/... raw/...` (the ingest move), allows everything outside
the immutable trees.

Hook contract: read JSON payload from stdin, exit 0 to allow, exit 2 to
block. stderr is shown to the agent.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

IMMUTABLE_PREFIXES = ("raw/", "INBOX/")

ALLOW_BASH = [
    re.compile(r"^\s*git\s+(status|log|diff|show|blame|branch|fetch|pull|remote)\b"),
    re.compile(r"^\s*git\s+mv\s+INBOX/"),  # ingest move from INBOX to raw/
    re.compile(r"^\s*(ls|find|grep|rg|cat|less|head|tail|wc|stat|file|du)\b"),
    re.compile(r"^\s*cd\s+tools\s+&&"),  # lint runner
    re.compile(r"^\s*mkdir\s+-p\s+(wiki|tools|scripts|docs|INBOX|\.claude)"),
    re.compile(r"^\s*echo\b"),
    re.compile(r"^\s*python3?\s+-c\b"),
    re.compile(r"^\s*uv\s+(venv|pip|run|sync)\b"),
    re.compile(r"^\s*chmod\s+\+x\s+(scripts|\.claude)/"),
]

DENY_BASH = [
    re.compile(r"\b(rm|mv|cp|sed|awk|tee|truncate)\b[^|]*\b(raw|INBOX)/"),
    re.compile(r">\s*(raw|INBOX)/"),  # redirect into raw/
    re.compile(r"^\s*git\s+(reset\s+--hard|clean\s+-fd|push\s+--force)\b"),
]


def _check_bash(payload: dict) -> int:
    cmd: str = payload.get("toolInput", {}).get("command", "")
    for allow in ALLOW_BASH:
        if allow.search(cmd):
            return 0
    for deny in DENY_BASH:
        if deny.search(cmd):
            print(
                f"guard_immutable: blocked '{cmd}' — raw/ and INBOX/ are immutable.",
                file=sys.stderr,
            )
            return 2
    return 0


def _check_write(payload: dict) -> int:
    file_path = payload.get("toolInput", {}).get("file_path", "")
    if not file_path:
        return 0
    repo = Path.cwd()
    try:
        rel = Path(file_path).resolve().relative_to(repo)
    except ValueError:
        return 0  # outside the repo, not our concern
    rel_str = str(rel)
    for prefix in IMMUTABLE_PREFIXES:
        if rel_str.startswith(prefix):
            print(
                f"guard_immutable: blocked Write to '{rel_str}' — immutable tree.",
                file=sys.stderr,
            )
            return 2
    return 0


def main() -> int:
    payload = json.load(sys.stdin)
    tool = payload.get("toolName", "")
    if tool == "Bash":
        return _check_bash(payload)
    if tool in ("Write", "Edit", "NotebookEdit"):
        return _check_write(payload)
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 3: Make executable**

```bash
chmod +x scripts/hooks/guard_immutable.py
```

- [ ] **Step 4: Smoke-test the guard with two synthetic payloads**

```bash
echo '{"toolName":"Bash","toolInput":{"command":"ls wiki/"}}' | python3 scripts/hooks/guard_immutable.py ; echo "allow=$?"
echo '{"toolName":"Bash","toolInput":{"command":"rm raw/people/Alice.md"}}' | python3 scripts/hooks/guard_immutable.py ; echo "deny=$?"
```
Expected:
```
allow=0
guard_immutable: blocked 'rm raw/people/Alice.md' — raw/ and INBOX/ are immutable.
deny=2
```

- [ ] **Step 5: Commit**

```bash
git add scripts/
git commit -m "infra: add raw/INBOX immutability guard hook (PreToolUse)"
```

### Task 0.2: Author `.claude/hooks/inbox-check.sh` (SessionStart reminder)

**Files:**
- Create: `.claude/hooks/inbox-check.sh`

The current `.claude/settings.json` already references this script — it must exist or the SessionStart hook will error.

- [ ] **Step 1: Write the hook script**

```bash
#!/bin/bash
# SessionStart hook: if INBOX/ has files (other than README.md), inject a
# system reminder telling Claude to run /ingest.
set -e

INBOX_DIR="${CLAUDE_PROJECT_DIR:-.}/INBOX"
files=$(ls -1 "$INBOX_DIR" 2>/dev/null | grep -v '^README\.md$' || true)

if [ -z "$files" ]; then
  exit 0
fi

count=$(printf '%s\n' "$files" | wc -l | tr -d ' ')

jq -n --arg files "$files" --arg count "$count" '{
  hookSpecificOutput: {
    hookEventName: "SessionStart",
    additionalContext: ("INBOX has \($count) unprocessed file(s) waiting for ingest:\n\($files)\n\nRun /ingest to process them into the wiki layer per CLAUDE.md.")
  }
}'
```

- [ ] **Step 2: Make executable + verify**

```bash
mkdir -p .claude/hooks
chmod +x .claude/hooks/inbox-check.sh
test -x .claude/hooks/inbox-check.sh && echo OK
```

- [ ] **Step 3: Commit**

```bash
git add .claude/hooks/
git commit -m "schema: add SessionStart inbox-check hook"
```

### Task 0.3: Wire the immutability guard into `.claude/settings.json`

**Files:**
- Modify: `.claude/settings.json`

- [ ] **Step 1: Read current settings**

Expected current shape: `env`, `permissions` (allow + deny), `hooks.SessionStart`. Need to add `hooks.PreToolUse` block and broaden `permissions.allow` for the new commands the plan needs.

- [ ] **Step 2: Edit settings**

Add to `permissions.allow` (append, don't replace):
```json
"Bash(git commit:*)",
"Bash(git push origin unified:*)",
"Bash(chmod +x scripts/*:*)",
"Bash(chmod +x .claude/hooks/*:*)",
"Bash(mkdir -p INBOX)",
"Bash(mkdir -p scripts/*)",
"Bash(mkdir -p tools/*)",
"Bash(mkdir -p docs/*)",
"Bash(echo:*)",
"Bash(uv venv:*)",
"Bash(uv pip:*)",
"Bash(uv run:*)",
"Bash(cd tools && uv run:*)",
"Bash(claude -p:*)",
"Bash(find:*)",
"Bash(wc:*)",
"Bash(python3 scripts/hooks/guard_immutable.py)",
"Bash(.claude/hooks/inbox-check.sh)"
```

Add to `permissions.deny` (append):
```json
"Bash(git push --force:*)",
"Bash(rm raw/*)",
"Bash(rm INBOX/*)"
```

Add a new `PreToolUse` block under `hooks`:
```json
"PreToolUse": [
  {
    "matcher": "Bash",
    "hooks": [
      { "type": "command", "command": "python3 ${CLAUDE_PROJECT_DIR}/scripts/hooks/guard_immutable.py" }
    ]
  },
  {
    "matcher": "Write|Edit|NotebookEdit",
    "hooks": [
      { "type": "command", "command": "python3 ${CLAUDE_PROJECT_DIR}/scripts/hooks/guard_immutable.py" }
    ]
  }
]
```

- [ ] **Step 3: Validate JSON parses**

```bash
python3 -c "import json; json.load(open('.claude/settings.json')); print('ok')"
```

- [ ] **Step 4: Commit (do NOT `/clear` yet — verify in next phase first)**

```bash
git add .claude/settings.json
git commit -m "schema: wire raw/INBOX guard into PreToolUse + broaden allowlist"
```

### Task 0.4: Carve out `INBOX/`, `tools/`, `docs/`

**Files:**
- Create: `INBOX/README.md`
- Create: `tools/.gitkeep`
- Create: `docs/.gitkeep`

- [ ] **Step 1: Make directories**

```bash
mkdir -p INBOX tools docs/superpowers/plans
touch tools/.gitkeep docs/.gitkeep
```

- [ ] **Step 2: Write `INBOX/README.md`**

```markdown
---
title: INBOX — Folder Guide
type: schema
created: 2026-05-11
updated: 2026-05-11
tags: [schema, folder-guide]
---

# INBOX/

Queue for newly-added external sources (clipped articles, transcripts dropped
by hand, PDFs, slack exports) awaiting ingest.

- INBOX/ sits **outside** `raw/`. Claude reads files here, may add summary
  frontmatter, but never edits body content. The PreToolUse guard
  (`scripts/hooks/guard_immutable.py`) enforces this.
- `/ingest` moves the source out of INBOX/ into the agreed `raw/<tab>/`
  destination using `git mv` so history is preserved.
- The SessionStart hook (`.claude/hooks/inbox-check.sh`) auto-injects a
  reminder when this folder has unprocessed files.
```

- [ ] **Step 3: Commit**

```bash
git add INBOX/README.md tools/.gitkeep docs/.gitkeep
git commit -m "infra: scaffold INBOX/ tools/ docs/"
```

---

## Phase 1 — Schema layer (sequential)

Everything downstream depends on the conventions set here.

### Task 1.1: Author root `CLAUDE.md`

**Files:**
- Create: `CLAUDE.md`

- [ ] **Step 1: Write**

```markdown
# CLAUDE.md

Guidance for Claude Code when working in this repository.

## What this repo is

This repo is the Data Science team's **second brain** — an Obsidian-compatible
Markdown vault implementing Andrej Karpathy's "wiki LLM" pattern
(https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

There is no build, lint, or test pipeline beyond the wiki lint at
`tools/lint/run_all.py`. The only artifacts are Markdown notes, YAML
frontmatter, Obsidian config (`.obsidian/`), and `.claude/` hooks +
commands.

The vault is multi-author. **Raw layer is immutable to Claude.** The
`scripts/hooks/guard_immutable.py` PreToolUse hook enforces this.

## Three-layer architecture (Karpathy)

1. **Raw** — `raw/`. Source-of-truth artifacts already populated:
   - `raw/people/<First Last>.md` — 50 seed notes for team / stakeholders / vendors
   - `raw/projects/{Project,Itamar Project} - <name>/` — 27 project folders
     with decks, drawio, design docs
   - `raw/meetings/meeting_*.txt` — meeting transcripts
   - `raw/cybereason/{core,phoenix}/` — 295 internal KB exports
   - `raw/level_blue/{company,products,org_tree_slr}` — org context
   - `raw/data_science_drive/` — exported Drive files (`.docx`, `.xlsx`, json)

   Claude reads, never edits. Companion folder `INBOX/` (sibling, not inside
   `raw/`) queues new material; `/ingest` moves files from `INBOX/` into the
   agreed `raw/<tab>/` destination.

2. **Wiki** — `wiki/`. Claude-owned synthesis layer:
   - `Entities/People/` — synthesised people notes
   - `Entities/Projects/` — one canonical note per active DS project
   - `Entities/Systems/` — products/components the team integrates with
   - `Meetings/` — distilled outcomes per meeting
   - `Decisions/` — DS-leadership ADRs
   - `Ideas/` — hypotheses + evidence
   - `Research/` — ML/AI/security concept notes
   - `Sources/` — one-pagers for external sources
   - `Syntheses/` — LLM-generated answers worth keeping
   - `Connections/` — cross-domain patterns spotted ≥2 times
   - `🔥 Hot Notes/` — active focus + brain architecture (≤7 entries)
   - `🗺️ Maps/` — `.canvas` and Obsidian-base visual maps
   - `📦 Archive/` — soft-deleted notes
   - `Memories/` — durable team know-how
   - `Log/` — `INDEX.md` (structural navigation), `wiki-ops.md` (audit
     trail), `pulse.md` (daily ops notes)

3. **Schema** — `CLAUDE.md`, `.claude/`, `tools/`, `scripts/`. Defines
   conventions, commands, hooks, lint. Co-evolves between DS leadership and
   Claude.

## Key rules for Claude

- **Never edit a `raw/` note's body.** Frontmatter touch-ups okay only on
  explicit user request. The PreToolUse guard will block accidental writes.
- **Always update `wiki/Log/INDEX.md`** and prepend to `wiki/Log/wiki-ops.md`
  (newest on top, below the `---` preamble separator) when ingest / lint /
  remove / braindump / synthesis touches the wiki.
- **Wikilinks only.** `[[Entity Name]]`, never markdown links.
- **Frontmatter is required** on every `wiki/` page. Every wiki page must
  carry `wiki` in its `tags` array (typically the second tag, after the
  domain tag). This is the layer marker — mirrors the `raw` tag concept on
  raw notes.
- **Filename conventions** vary per folder; see the folder's `README.md`.
- **Smart Connections** (community Obsidian plugin) provides semantic
  search. Use it for "similar to X" questions; use `Log/INDEX.md` for
  structural navigation.
- **Session start.** Every session, after this `CLAUDE.md`, also read
  `wiki/Log/INDEX.md`, `wiki/🔥 Hot Notes/Active Focus.md`, and
  `wiki/🔥 Hot Notes/Brain Architecture.md` before answering.

## Operations

Five slash-commands under `.claude/commands/`:

- `/ingest <path>` — process a source from `INBOX/` (or any `raw/` note)
  into the wiki layer
- `/query <question>` — synthesise a cited answer against the wiki
- `/lint` — deterministic + LLM health checks
- `/remove <topic>` — two-pass removal with reference cleanup; soft-deletes
  into `📦 Archive/` by default
- `/braindump <thoughts>` — append a free-form thought stream that Claude
  then files into appropriate `wiki/` pages

Each command's prompt and parallelisation strategy is documented in
`.claude/commands/<name>.md`. See `superpowers:dispatching-parallel-agents`
for the batching pattern.

## Wiki page conventions

- **Frontmatter required.** Every wiki page has `title`, `type`, `tags`,
  `last_updated` minimum. Type-specific extras per the folder's README.
- **`wiki` tag mandatory.** Layer marker.
- **Wikilinks only.** `[[Name]]`.
- **Cite raw and wiki together.** A synthesis claim should link both to the
  `raw/` source AND to the entity/concept page that catalogs it.
- **Dates.** Always `YYYY-MM-DD` in frontmatter and log entries.
- **Open-questions section.** Every Entity, Decision, Idea, Research, and
  Synthesis page ends with `## Open questions`. This feeds future ingest
  cycles.

## Git workflow

- Active branch: `unified`. All commits push to `origin/unified`.
- Auto-commit + push is part of every `/ingest`, `/query` (when filing),
  `/lint` (when fixes applied), `/remove`, `/braindump`.
- Commit message format: `<op> | <subject>` (e.g. `ingest | Tipper rollout
  retro 2026-05-08`).
- Never `git push --force` on `unified`. Never bypass hooks with
  `--no-verify`.

## Rhythm

- **Per session.** When a raw note lands or a source drops into INBOX/,
  run `/ingest`. The SessionStart hook auto-flags an unprocessed inbox.
- **Weekly (Sunday).** Run `/lint`. Skim `wiki/Log/wiki-ops.md` for the
  past week.
- **Monthly.** Generate a synthesis page; promote recurring synthesis
  themes to dedicated entity or research pages.
- **Ad hoc.** `/query` whenever a question arises.
```

- [ ] **Step 2: Commit**

```bash
git add CLAUDE.md
git commit -m "schema: author root CLAUDE.md (3-layer Karpathy pattern)"
```

### Task 1.2: Replace `TO_COMPLETE` stubs in root `README.md`

**Files:**
- Modify: `README.md`

- [ ] **Step 1: Rewrite**

```markdown
# ds-brain (branch: unified)

Data Science team second brain based on Karpathy-style LLM Wiki
(https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f). The brain
runs continuously on a team Ubuntu VM; Obsidian Desktop and Claude Code both
read/write the same repo.

## Quick start (DS member, laptop)

1. Clone: `git clone git@github.com:<org>/ds-brain.git && cd ds-brain`
2. `git checkout unified`
3. Open `ds-brain/` as an Obsidian vault. Enable Smart Connections (already
   in `.obsidian/community-plugins.json`).
4. Drop a new source into `INBOX/` and run `/ingest` in Claude Code. The
   SessionStart hook will remind you if INBOX/ has unprocessed files.
5. Read `CLAUDE.md` for the layer model and `wiki/<folder>/README.md` for
   the conventions of each folder.

## Slash commands (in `.claude/commands/`)

| Command | Purpose |
|---|---|
| `/ingest <path>` | Process a source from INBOX/ (or any raw/ note) into wiki/ |
| `/query <question>` | Synthesise a cited answer against the wiki |
| `/lint` | Deterministic + LLM health checks |
| `/remove <topic>` | Two-pass removal with reference cleanup |
| `/braindump <thoughts>` | Append free-form thought stream; Claude files it |

## Layers (Karpathy)

| Layer | Where | Who writes |
|---|---|---|
| Raw | `raw/`, `INBOX/` | Humans (immutable to Claude — guarded by PreToolUse hook) |
| Wiki | `wiki/{Entities,Meetings,Decisions,Ideas,Research,Syntheses,Sources,Connections,🔥 Hot Notes,🗺️ Maps,📦 Archive,Memories,Log}/` | Claude |
| Schema | `CLAUDE.md`, `.claude/`, `tools/`, `scripts/` | DS leadership + Claude |

## Tooling (`scripts/` and `tools/`)

- `scripts/hooks/guard_immutable.py` — PreToolUse guard blocking writes to
  `raw/` and `INBOX/`
- `tools/lint/run_all.py` — deterministic lint (frontmatter / orphans /
  stale links) with thread-pooled fan-out
- `tools/convert/` — `.docx` and `.xlsx` → Markdown converters for ingest

## Triggers

- **SessionStart** — `.claude/hooks/inbox-check.sh` flags unprocessed INBOX/
  files
- **PreToolUse (Bash, Write, Edit)** — `scripts/hooks/guard_immutable.py`
  enforces raw/ immutability
- **Weekly cron (Ubuntu VM)** — `scripts/cron/weekly-lint.sh` runs
  `claude -p "/lint"` every Sunday 03:00 UTC

## License

Internal — Cybereason / Level Blue Data Science.
```

- [ ] **Step 2: Commit**

```bash
git add README.md
git commit -m "docs: flesh out root README (replace TO_COMPLETE stubs)"
```

### Task 1.3: Author the five slash commands (PARALLEL, single batched message)

**Files:**
- Create: `.claude/commands/ingest.md`
- Create: `.claude/commands/query.md`
- Create: `.claude/commands/lint.md`
- Create: `.claude/commands/remove.md`
- Create: `.claude/commands/braindump.md`

All five are file-disjoint. Dispatch a subagent per command in a SINGLE message OR write all five via batched `Write` calls in one message.

- [ ] **Step 1: Write `.claude/commands/ingest.md`**

````markdown
---
description: Ingest a source from INBOX/ (or any raw/ note) into the wiki layer
argument-hint: <path-to-source-or-empty-to-pick-from-INBOX>
---

Ingest `$ARGUMENTS` into the wiki per `CLAUDE.md` § Operations.

If `$ARGUMENTS` is empty, list what's currently in `INBOX/` and ask which file(s)
to ingest.

## Workflow

1. **Read the source fully.** No skimming. For `.docx` / `.xlsx`, first run
   `python3 tools/convert/docx_to_md.py <path>` (or `xlsx_to_md.py`) to
   produce a Markdown sidecar in the same directory; ingest both.

2. **Stop and report key takeaways.** Before writing or moving anything:
   - Summarise what the source actually says.
   - Propose a destination tab under `raw/<tab>/` for the file(s) (e.g.
     transcript → `raw/meetings/`, project deck → `raw/projects/Project -
     <name>/`).
   - List the People / Projects / Systems / Decisions / Ideas / Research
     pages you plan to touch.
   - Flag any contradictions you spotted with existing wiki pages.
   - Ask clarifying questions if intent is ambiguous.

   **Wait for go-ahead before continuing.**

3. **After approval, execute — parallelise independent work.**

   **Phase A — discovery (parallel reads).** In a SINGLE message, batch
   `Read` calls for every existing target page. Files are independent.

   **Phase B — page work (parallel writes).** Each Entity / Decision / Idea
   / Research / Source page is an independent file. In a SINGLE message,
   batch the `Edit` / `Write` calls:
   - For each Person/Project/System: append to `## Mentions` if the page
     exists, else create per the folder's README template.
   - For each Decision impacted: add to `## Decisions` on the related
     Project page.
   - For external sources: write `wiki/Sources/<slug>.md`.
   - For meetings: create `wiki/Meetings/YYYY-MM-DD — <topic>.md`.

   Use `superpowers:dispatching-parallel-agents` when a single page needs
   heavy net-new prose.

   **Phase C — shared-file updates (sequential):**
   - Update `wiki/Log/INDEX.md` (new pages + revised one-line summaries).
   - **Move source file(s) out of `INBOX/` into the agreed `raw/<tab>/`
     destination using `git mv`.** Update `sources:` frontmatter on every
     wiki page just written to reference the new path.
   - Prepend to `wiki/Log/wiki-ops.md` (newest on top, below the `---`
     preamble separator):
     ```
     ## [YYYY-MM-DD] ingest | <source title>
     - wiki/Sources/<slug>.md (new)
     - wiki/Entities/People/<name>.md (updated)
     - wiki/Entities/Projects/<name>.md (updated)
     Files moved:
     - INBOX/<old> → raw/<tab>/<new>
     ```

   **Phase D — commit + push:** Stage all touched files (including
   `wiki/Log/wiki-ops.md` and the moved source), commit
   `ingest | <source title>`, `git push` to `origin/unified`.

4. **Final report:** pages created / modified, files moved, commit SHA +
   push result, anything flagged for human review.

## Hard rules

- Never edit a user-authored `raw/` note's body.
- Wikilinks only (`[[Name]]`).
- Every wiki page must include `wiki` in its `tags` array.
- Phase A and Phase B must batch tool calls in a single message.
- Auto-commit + push is mandatory. `wiki/Log/wiki-ops.md` must always be in
  the commit.
````

- [ ] **Step 2: Write `.claude/commands/query.md`**

````markdown
---
description: Ask a question of the wiki and synthesise a cited answer
argument-hint: <question>
---

Answer this question against the wiki: **$ARGUMENTS**

Workflow:

1. **Read `wiki/Log/INDEX.md` first** to find candidate pages.
2. **Drill into the 2–5 most-relevant wiki pages — read them all in a
   SINGLE message (parallel `Read` calls).** Optionally consult Smart
   Connections in the same batch for semantically nearest `raw/` notes.
3. **Synthesise an answer** — every claim cited with `[[wikilinks]]`. No
   uncited claims. If something can't be cited, say so explicitly.
4. **End by asking whether to file** this as
   `wiki/Syntheses/<YYYY-MM-DD> — <question>.md`.

Don't write any files until the user says yes to filing.

## When filing (after approval)

- Create the page using the template in `wiki/Syntheses/README.md` (include
  `derived_from: [<page A>, <page B>, ...]` frontmatter).
- Update `wiki/Log/INDEX.md`.
- Prepend `## [YYYY-MM-DD] query | <question>` to `wiki/Log/wiki-ops.md`
  (newest on top, below the `---` preamble separator).
- Stage, commit `query | <question>`, push to `origin/unified`.

## Heuristics for whether filing is worth it

- Did the answer surface a connection not previously known?
- Would the team want to find this answer again in 6 months?
- Did it prompt new follow-up questions worth tracking?

If none, suggest skipping the file step.
````

- [ ] **Step 3: Write `.claude/commands/lint.md`**

````markdown
---
description: Run a wiki health check — deterministic checks then LLM checks
argument-hint: (no args)
---

Lint the wiki per `CLAUDE.md` § Operations.

## Step 1 — deterministic checks

From the vault root:

```bash
cd tools && uv run python -m lint.run_all
```

The Python script fans frontmatter / orphans / stale-links across a thread
pool internally. Report what it found. Fix every issue (or flag what can't
be auto-fixed) before Step 2.

## Step 2 — LLM checks (parallel subagents)

Dispatch the five checks below as **separate subagents in a SINGLE
message** so they run concurrently (`superpowers:dispatching-parallel-agents`).
Each subagent reads `wiki/Log/INDEX.md` plus the relevant subset of pages,
returns a numbered findings list with file paths and exact quotes, and does
**not** write.

1. **Contradictions** — claim X on page A, claim ¬X on page B, no
   `## Tensions` block.
2. **Stale claims** — page `last_updated` is old AND newer `raw/` notes
   supersede info.
3. **Orphaned concepts** — recurring in `raw/` but no `wiki/Research/` or
   `wiki/Entities/*` page exists.
4. **Missing cross-references** — entities that should link to each other
   but don't.
5. **Data gaps** — areas where an external source would clarify (suggest
   the search; don't run it).

Pick `subagent_type: Explore` for each — read-only audits. Brief each one
with: which check it owns, the wiki layout it should scan, the exact
report format. Collate the five reports into one numbered list. **Do NOT
make edits yet.**

## Step 3 — apply approved fixes

After review:
- Apply only the fixes approved. Independent file edits batch in a SINGLE
  message (parallel `Edit` calls).
- For >5 changes, batch into commits per category.
- Prepend `## [YYYY-MM-DD] lint | <summary>` to `wiki/Log/wiki-ops.md` with
  counts of issues found and fixed.
- Stage all touched files (including `wiki/Log/wiki-ops.md`), commit
  `lint | <summary>`, push to `origin/unified`.

If no fixes were applied (clean run), do not write to `wiki/Log/wiki-ops.md`
and do not commit. Just report the clean status.
````

- [ ] **Step 4: Write `.claude/commands/remove.md`**

````markdown
---
description: Two-pass removal of a topic (raw note, wiki page, or both) with reference cleanup; soft-deletes into 📦 Archive/ by default
argument-hint: <topic — file path, entity/concept name, or theme>
---

Remove **$ARGUMENTS** from the wiki per `CLAUDE.md` § Operations.

The topic could be a single `raw/` note, a single wiki page, or a
multi-page topic spanning both layers.

If editing a single page would suffice, **say so and stop** — removal is
the heavier hammer.

## PASS 1 — list, don't write

**Run discovery in parallel.** In a SINGLE message, batch the searches —
each is independent:
- `grep -rn "[[<topic>]]"` across `raw/` and `wiki/` for direct wikilinks.
- `grep -rn` for alias forms (`[[<topic>|...]]`, `[[<topic>#...]]`).
- `grep -rn` for `sources:` / `derived_from:` frontmatter pointers.
- `grep -n` against `wiki/Log/INDEX.md` and `wiki/Log/wiki-ops.md` for
  mentions.
- `find` for sibling files that share the topic name.

Produce a single markdown report with these sections (totals at the top):

1. **Files to soft-delete (move to 📦 Archive/)** — exact paths.
2. **Files with stale wikilinks to fix.**
3. **`wiki/Log/INDEX.md` entries** that reference the topic.
4. **`sources:` / `derived_from:` frontmatter entries** to clean.
5. **`wiki/Log/wiki-ops.md` mentions** (NOT edited — log is prepend-only).

**Do not write or move anything. Wait for approval before PASS 2.**

## PASS 2 — execute (only after approval)

1. For each file in PASS 1 step 1, soft-delete by `git mv` into the
   matching `📦 Archive/` sub-path (e.g.
   `wiki/Entities/Projects/Tipper.md` →
   `wiki/📦 Archive/Entities/Projects/Tipper.md`). Stamp three frontmatter
   fields on the archived note: `deleted: YYYY-MM-DD`,
   `deleted_reason: "..."`, `deleted_from: <original-relative-path>`.
2. **For each file with a stale wikilink, edit in parallel — batch every
   `Edit` call into a SINGLE message.** Independent files have no ordering
   dependency.
   - In a list → remove the bullet entirely.
   - In body prose → replace with link's display text in plain (no
     brackets); rewrite the sentence cleanly. Surface ambiguous cases.
3. Update `wiki/Log/INDEX.md` to remove the archived entries.
4. Update `sources:` / `derived_from:` frontmatter — drop the entry; flag
   pages that now have zero sources.
5. Prepend to `wiki/Log/wiki-ops.md`:
   ```
   ## [YYYY-MM-DD] removal | <topic>
   - files archived: ...
   - files modified: ...
   - reason: <one paragraph in the user's words>
   ```
6. Run `cd tools && uv run python -m lint.run_all` and report. Fix
   anything dangling.
7. Stage all touched files, commit `removal | <topic>`, push to
   `origin/unified`.
8. Final report: total archived, total modified, lint status, commit SHA +
   push result.

## Hard rules

- `wiki/Log/wiki-ops.md` is prepend-only (newest on top). Past entries
  mentioning the removed topic stay — that's the historical record.
- Removals touching >5 files always go through PASS 1 review.
- PASS 1 discovery and PASS 2 reference-fixing must batch tool calls in a
  single message.
- Auto-commit + push is mandatory after PASS 2 lint passes.
````

- [ ] **Step 5: Write `.claude/commands/braindump.md`**

````markdown
---
description: Append a free-form thought stream; Claude files it into appropriate wiki/ pages
argument-hint: <free-form thoughts, any length>
---

Take this braindump and file it into the wiki: **$ARGUMENTS**

## Workflow

1. **Acknowledge what was said.** Restate in 2–3 bullets to confirm
   understanding. Ask one clarifying question only if intent is ambiguous.

2. **Classify the content** into one or more buckets:
   - new fact about a Person / Project / System
   - new Idea / hypothesis
   - new Decision
   - new Connection (cross-domain pattern)
   - new Hot Note (active focus)
   - new entry on an existing page
   - candidate Source pointer

3. **Plan the writes.** List the wiki pages you'll create or modify, one
   line each. Wait for go-ahead.

4. **After approval, execute — parallelise independent writes.** Same
   Phase A / B / C / D structure as `/ingest`. Skip the raw/ move (no
   INBOX/ file involved unless the braindump references an attached file).

5. Append `## [YYYY-MM-DD] braindump | <one-line subject>` to
   `wiki/Log/wiki-ops.md`. Commit `braindump | <subject>`, push.

## Hard rules

- Wikilinks only. Frontmatter required. `wiki` tag mandatory.
- A braindump may seed a new Idea or Connection, but never a new Decision
  unless the user explicitly says "we decided X".
````

- [ ] **Step 6: Verify**

```bash
ls .claude/commands/
```
Expected: `braindump.md  ingest.md  lint.md  query.md  remove.md`

- [ ] **Step 7: Commit**

```bash
git add .claude/commands/
git commit -m "schema: add 5 slash commands (ingest, query, lint, remove, braindump)"
```

### Task 1.4: Author `tools/lint/` (TDD)

**Files:**
- Create: `tools/pyproject.toml`
- Create: `tools/uv.lock` (generated)
- Create: `tools/lint/__init__.py` (empty)
- Create: `tools/lint/check_frontmatter.py`
- Create: `tools/lint/check_orphans.py`
- Create: `tools/lint/check_stale_links.py`
- Create: `tools/lint/run_all.py`
- Create: `tools/lint/tests/__init__.py` (empty)
- Create: `tools/lint/tests/test_frontmatter.py`
- Create: `tools/lint/tests/test_orphans.py`
- Create: `tools/lint/tests/test_stale_links.py`

TDD: test first, watch fail, implement, watch pass, commit.

- [ ] **Step 1: `tools/pyproject.toml`**

```toml
[project]
name = "ds-brain-tools"
version = "0.1.0"
description = "Lint and ingest helpers for ds-brain"
requires-python = ">=3.11"
dependencies = [
    "pyyaml>=6.0",
    "rich>=13.0",
]

[tool.uv]
dev-dependencies = ["pytest>=8.0"]
```

- [ ] **Step 2: Bootstrap venv**

```bash
cd tools && uv venv && uv sync
```

- [ ] **Step 3: Write failing test `tools/lint/tests/test_frontmatter.py`**

```python
from pathlib import Path

from lint.check_frontmatter import find_violations


def test_missing_wiki_tag_is_violation(tmp_path: Path) -> None:
    p = tmp_path / "Entities" / "People" / "Alice.md"
    p.parent.mkdir(parents=True)
    p.write_text(
        "---\ntitle: Alice\ntype: person\ntags: [person]\nlast_updated: 2026-05-11\n---\nBody.\n",
        encoding="utf-8",
    )
    violations = find_violations(tmp_path)
    assert any("wiki tag" in v.message for v in violations)


def test_proper_frontmatter_passes(tmp_path: Path) -> None:
    p = tmp_path / "Entities" / "People" / "Bob.md"
    p.parent.mkdir(parents=True)
    p.write_text(
        "---\ntitle: Bob\ntype: person\ntags: [person, wiki]\nlast_updated: 2026-05-11\n---\nBody.\n",
        encoding="utf-8",
    )
    violations = find_violations(tmp_path)
    assert not violations


def test_archive_files_excluded(tmp_path: Path) -> None:
    p = tmp_path / "📦 Archive" / "x.md"
    p.parent.mkdir(parents=True)
    p.write_text("no frontmatter\n", encoding="utf-8")
    violations = find_violations(tmp_path)
    assert not violations


def test_readme_files_excluded(tmp_path: Path) -> None:
    p = tmp_path / "Entities" / "People" / "README.md"
    p.parent.mkdir(parents=True)
    p.write_text("no frontmatter\n", encoding="utf-8")
    violations = find_violations(tmp_path)
    assert not violations
```

- [ ] **Step 4: Run — expect FAIL**

```bash
cd tools && uv run pytest lint/tests/test_frontmatter.py -v
```
Expected: ModuleNotFoundError or AttributeError on `lint.check_frontmatter`.

- [ ] **Step 5: Implement `tools/lint/check_frontmatter.py`**

```python
"""Frontmatter check: every wiki/ page must have title, type, tags incl. 'wiki', last_updated."""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import yaml

REQUIRED_KEYS = ("title", "type", "tags", "last_updated")


@dataclass(frozen=True)
class Violation:
    path: Path
    message: str


def _parse_frontmatter(text: str) -> dict | None:
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end == -1:
        return None
    block = text[3:end]
    try:
        data = yaml.safe_load(block)
    except yaml.YAMLError:
        return None
    return data if isinstance(data, dict) else None


def _is_archived(path: Path, root: Path) -> bool:
    rel = path.relative_to(root)
    return "📦 Archive" in rel.parts


def find_violations(root: Path) -> list[Violation]:
    violations: list[Violation] = []
    for md in root.rglob("*.md"):
        if _is_archived(md, root):
            continue
        if md.name == "README.md":
            continue  # folder guides have their own schema
        text = md.read_text(encoding="utf-8")
        fm = _parse_frontmatter(text)
        if fm is None:
            violations.append(Violation(md, "missing frontmatter"))
            continue
        for key in REQUIRED_KEYS:
            if key not in fm:
                violations.append(Violation(md, f"missing key: {key}"))
        tags = fm.get("tags", [])
        if not isinstance(tags, list) or "wiki" not in tags:
            violations.append(Violation(md, "missing wiki tag"))
    return violations
```

- [ ] **Step 6: Run — expect PASS**

```bash
cd tools && uv run pytest lint/tests/test_frontmatter.py -v
```
Expected: 4 passed.

- [ ] **Step 7: Write failing test `tools/lint/tests/test_orphans.py`**

```python
from pathlib import Path

from lint.check_orphans import find_orphans


def test_page_with_no_inbound_links_is_orphan(tmp_path: Path) -> None:
    a = tmp_path / "Entities" / "People" / "Alice.md"
    a.parent.mkdir(parents=True)
    a.write_text("---\ntags: [wiki]\n---\nbody\n", encoding="utf-8")
    idx = tmp_path / "Log" / "INDEX.md"
    idx.parent.mkdir()
    idx.write_text("# Index\n\n(no links)\n", encoding="utf-8")
    orphans = find_orphans(tmp_path)
    assert any(o.name == "Alice.md" for o in orphans)


def test_linked_page_not_orphan(tmp_path: Path) -> None:
    a = tmp_path / "Entities" / "People" / "Alice.md"
    a.parent.mkdir(parents=True)
    a.write_text("---\ntags: [wiki]\n---\nbody\n", encoding="utf-8")
    idx = tmp_path / "Log" / "INDEX.md"
    idx.parent.mkdir()
    idx.write_text("# Index\n\n[[Alice]]\n", encoding="utf-8")
    orphans = find_orphans(tmp_path)
    assert all(o.name != "Alice.md" for o in orphans)
```

- [ ] **Step 8: Run — expect FAIL**

```bash
cd tools && uv run pytest lint/tests/test_orphans.py -v
```

- [ ] **Step 9: Implement `tools/lint/check_orphans.py`**

```python
"""Orphan check: any wiki page with zero inbound wikilinks from another wiki page."""
from __future__ import annotations

import re
from pathlib import Path

LINK_RE = re.compile(r"\[\[([^\]|#]+)(?:[|#][^\]]*)?\]\]")


def _wiki_md_files(root: Path) -> list[Path]:
    return [
        p
        for p in root.rglob("*.md")
        if "📦 Archive" not in p.relative_to(root).parts
        and p.name != "README.md"
    ]


def find_orphans(root: Path) -> list[Path]:
    files = _wiki_md_files(root)
    by_stem = {p.stem: p for p in files}
    referenced: set[str] = set()
    for p in files:
        for m in LINK_RE.finditer(p.read_text(encoding="utf-8")):
            referenced.add(m.group(1).strip())
    return sorted(p for stem, p in by_stem.items() if stem not in referenced)
```

- [ ] **Step 10: Run — expect PASS**

```bash
cd tools && uv run pytest lint/tests/test_orphans.py -v
```

- [ ] **Step 11: Write failing test `tools/lint/tests/test_stale_links.py`**

```python
from pathlib import Path

from lint.check_stale_links import find_stale_links


def test_link_to_missing_page_flagged(tmp_path: Path) -> None:
    p = tmp_path / "Entities" / "People" / "Alice.md"
    p.parent.mkdir(parents=True)
    p.write_text("Worked with [[Ghost]].\n", encoding="utf-8")
    stale = find_stale_links(tmp_path)
    assert any(s.target == "Ghost" for s in stale)


def test_link_to_existing_page_ok(tmp_path: Path) -> None:
    (tmp_path / "Entities" / "People").mkdir(parents=True)
    (tmp_path / "Entities" / "People" / "Alice.md").write_text(
        "Worked with [[Bob]].\n", encoding="utf-8"
    )
    (tmp_path / "Entities" / "People" / "Bob.md").write_text("hi", encoding="utf-8")
    stale = find_stale_links(tmp_path)
    assert not stale
```

- [ ] **Step 12: Run — expect FAIL**

```bash
cd tools && uv run pytest lint/tests/test_stale_links.py -v
```

- [ ] **Step 13: Implement `tools/lint/check_stale_links.py`**

```python
"""Stale-link check: wikilinks pointing to a target that doesn't exist as a .md stem."""
from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

LINK_RE = re.compile(r"\[\[([^\]|#]+)(?:[|#][^\]]*)?\]\]")


@dataclass(frozen=True)
class StaleLink:
    source: Path
    target: str


def find_stale_links(root: Path) -> list[StaleLink]:
    stems = {p.stem for p in root.rglob("*.md")}
    stale: list[StaleLink] = []
    for p in root.rglob("*.md"):
        if "📦 Archive" in p.relative_to(root).parts:
            continue
        for m in LINK_RE.finditer(p.read_text(encoding="utf-8")):
            target = m.group(1).strip()
            if target not in stems:
                stale.append(StaleLink(p, target))
    return stale
```

- [ ] **Step 14: Run — expect PASS**

```bash
cd tools && uv run pytest lint/tests/test_stale_links.py -v
```

- [ ] **Step 15: Write `tools/lint/run_all.py` — thread-pool runner**

```python
"""Run all wiki lint checks with thread-pool fan-out."""
from __future__ import annotations

import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from rich.console import Console

from lint.check_frontmatter import find_violations
from lint.check_orphans import find_orphans
from lint.check_stale_links import find_stale_links


def main() -> int:
    repo_root = Path(__file__).resolve().parents[2]
    wiki = repo_root / "wiki"
    console = Console()

    with ThreadPoolExecutor(max_workers=3) as pool:
        f_fronts = pool.submit(find_violations, wiki)
        f_orphs = pool.submit(find_orphans, wiki)
        f_stale = pool.submit(find_stale_links, wiki)

    fronts = f_fronts.result()
    orphs = f_orphs.result()
    stale = f_stale.result()

    console.rule("frontmatter")
    for v in fronts:
        console.print(f"  {v.path.relative_to(repo_root)} — {v.message}")
    console.rule("orphans")
    for p in orphs:
        console.print(f"  {p.relative_to(repo_root)}")
    console.rule("stale links")
    for s in stale:
        console.print(f"  {s.source.relative_to(repo_root)} → [[{s.target}]]")

    total = len(fronts) + len(orphs) + len(stale)
    console.rule()
    console.print(
        f"frontmatter: {len(fronts)}  orphans: {len(orphs)}  stale: {len(stale)}  total: {total}"
    )
    return 0 if total == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 16: Run full suite + e2e**

```bash
cd tools && uv run pytest lint/tests -v
cd tools && uv run python -m lint.run_all || true
```
Expected pytest: 8 passed. e2e: prints violations (current Sources/Hot Notes lack `wiki` tag and `last_updated` — expected; Phase 2 fixes).

- [ ] **Step 17: Commit**

```bash
git add tools/
git commit -m "tooling: deterministic wiki lint (frontmatter, orphans, stale-links) via TDD"
```

### Task 1.5: Author `tools/convert/` — `.docx` and `.xlsx` → markdown

**Files:**
- Create: `tools/convert/__init__.py`
- Create: `tools/convert/docx_to_md.py`
- Create: `tools/convert/xlsx_to_md.py`
- Create: `tools/convert/tests/test_docx_to_md.py`
- Create: `tools/convert/tests/test_xlsx_to_md.py`
- Modify: `tools/pyproject.toml` (add `python-docx`, `openpyxl`)

`raw/data_science_drive/` has `.docx` and `.xlsx` files. Without a converter, `/ingest` can't read them. Out-of-scope to render PowerPoint or drawio; punt those.

- [ ] **Step 1: Add deps**

Add to `[project.dependencies]` in `tools/pyproject.toml`:
```toml
"python-docx>=1.1",
"openpyxl>=3.1",
```
Then `cd tools && uv sync`.

- [ ] **Step 2: Write failing test `tools/convert/tests/test_docx_to_md.py`**

```python
from pathlib import Path

from docx import Document

from convert.docx_to_md import docx_to_markdown


def test_paragraphs_become_markdown_paragraphs(tmp_path: Path) -> None:
    doc = Document()
    doc.add_heading("Title", level=1)
    doc.add_paragraph("First paragraph.")
    doc.add_paragraph("Second paragraph.")
    src = tmp_path / "x.docx"
    doc.save(src)

    md = docx_to_markdown(src)
    assert "# Title" in md
    assert "First paragraph." in md
    assert "Second paragraph." in md
```

- [ ] **Step 3: Implement `tools/convert/docx_to_md.py`**

```python
"""Minimal .docx → Markdown. Headings, paragraphs, lists, tables."""
from __future__ import annotations

import sys
from pathlib import Path

from docx import Document
from docx.document import Document as _Doc


def docx_to_markdown(path: Path) -> str:
    doc: _Doc = Document(str(path))
    out: list[str] = []
    for p in doc.paragraphs:
        style = p.style.name if p.style else ""
        text = p.text.rstrip()
        if not text:
            out.append("")
            continue
        if style.startswith("Heading"):
            try:
                level = int(style.split()[-1])
            except ValueError:
                level = 1
            out.append("#" * level + " " + text)
        elif style in ("List Bullet", "List Paragraph"):
            out.append(f"- {text}")
        else:
            out.append(text)
    for t in doc.tables:
        out.append("")
        rows = [[c.text.strip() for c in r.cells] for r in t.rows]
        if rows:
            out.append("| " + " | ".join(rows[0]) + " |")
            out.append("| " + " | ".join("---" for _ in rows[0]) + " |")
            for r in rows[1:]:
                out.append("| " + " | ".join(r) + " |")
    return "\n".join(out).rstrip() + "\n"


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: docx_to_md.py <path.docx>", file=sys.stderr)
        return 2
    src = Path(sys.argv[1])
    dst = src.with_suffix(".md")
    dst.write_text(docx_to_markdown(src), encoding="utf-8")
    print(dst)
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 4: Verify**

```bash
cd tools && uv run pytest convert/tests/test_docx_to_md.py -v
```

- [ ] **Step 5: Write failing test `tools/convert/tests/test_xlsx_to_md.py`**

```python
from pathlib import Path

from openpyxl import Workbook

from convert.xlsx_to_md import xlsx_to_markdown


def test_sheet_becomes_table(tmp_path: Path) -> None:
    wb = Workbook()
    ws = wb.active
    ws.title = "people"
    ws.append(["Name", "Role"])
    ws.append(["Alice", "PM"])
    ws.append(["Bob", "Eng"])
    src = tmp_path / "x.xlsx"
    wb.save(src)

    md = xlsx_to_markdown(src)
    assert "## people" in md
    assert "| Name | Role |" in md
    assert "| Alice | PM |" in md
```

- [ ] **Step 6: Implement `tools/convert/xlsx_to_md.py`**

```python
"""Minimal .xlsx → Markdown. One H2 per sheet, one table per sheet."""
from __future__ import annotations

import sys
from pathlib import Path

from openpyxl import load_workbook


def xlsx_to_markdown(path: Path) -> str:
    wb = load_workbook(str(path), data_only=True, read_only=True)
    out: list[str] = []
    for sheet in wb.worksheets:
        out.append(f"## {sheet.title}")
        out.append("")
        rows = list(sheet.iter_rows(values_only=True))
        rows = [r for r in rows if any(c is not None and str(c).strip() for c in r)]
        if not rows:
            out.append("(empty)")
            out.append("")
            continue
        header = ["" if c is None else str(c).strip() for c in rows[0]]
        out.append("| " + " | ".join(header) + " |")
        out.append("| " + " | ".join("---" for _ in header) + " |")
        for r in rows[1:]:
            cells = ["" if c is None else str(c).strip().replace("|", "\\|") for c in r]
            cells += [""] * (len(header) - len(cells))
            out.append("| " + " | ".join(cells[: len(header)]) + " |")
        out.append("")
    return "\n".join(out).rstrip() + "\n"


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: xlsx_to_md.py <path.xlsx>", file=sys.stderr)
        return 2
    src = Path(sys.argv[1])
    dst = src.with_suffix(".md")
    dst.write_text(xlsx_to_markdown(src), encoding="utf-8")
    print(dst)
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 7: Run full convert suite**

```bash
cd tools && uv run pytest convert/tests -v
```
Expected: 2 passed.

- [ ] **Step 8: Commit**

```bash
git add tools/convert/ tools/pyproject.toml
git commit -m "tooling: docx + xlsx → markdown converters (TDD)"
```

---

## Phase 2 — Folder schemas (HIGH PARALLELISM)

Every `wiki/<folder>/README.md` is independent. **Dispatch one subagent (or
one batched Write call) per folder.** All 13 lanes below can run
concurrently in a single message.

| Lane | Action | File |
|---|---|---|
| 2.1 | Create | `wiki/Entities/README.md` |
| 2.2 | Rewrite | `wiki/Entities/People/README.md` |
| 2.3 | Rewrite | `wiki/Entities/Projects/README.md` |
| 2.4 | Rewrite | `wiki/Entities/Systems/README.md` |
| 2.5 | Rewrite | `wiki/Meetings/README.md` |
| 2.6 | Rewrite | `wiki/Decisions/README.md` |
| 2.7 | Rewrite | `wiki/Ideas/README.md` |
| 2.8 | Rewrite | `wiki/Research/README.md` |
| 2.9 | Create | `wiki/Sources/README.md` |
| 2.10 | Rewrite | `wiki/Syntheses/README.md` |
| 2.11 | Rewrite | `wiki/Connections/README.md` |
| 2.12 | Create | `wiki/🔥 Hot Notes/README.md`, `wiki/Memories/README.md`, `wiki/Log/README.md` (sub-batch) |
| 2.13 | Refresh `updated:` date | `wiki/🗺️ Maps/README.md`, `wiki/📦 Archive/README.md` (sub-batch) |

All READMEs share the shape: frontmatter (`title`, `type: schema`,
`created`, `updated`, `tags: [schema, folder-guide]`), one-line purpose,
filename convention, frontmatter schema, body schema with section template.

### Task 2.1: `wiki/Entities/README.md` (parent overview)

```markdown
---
title: Entities — Folder Guide
type: schema
created: 2026-05-11
updated: 2026-05-11
tags: [schema, folder-guide]
---

# Entities/

Every nameable thing the DS team cares about. Split by type:

- `Entities/People/` — humans (team members, stakeholders, vendors, candidates)
- `Entities/Projects/` — DS-owned R&D efforts
- `Entities/Systems/` — third-party / platform components the team
  integrates with (Tipper, MailMarshal, URLDeep, …)

Each sub-folder has its own README defining its page template.

### Cross-cutting rules

- Filename = canonical English display name (Projects: drop the
  `Project - ` / `Itamar Project - ` prefix).
- `wiki` tag mandatory; second tag is the entity type (`person`,
  `project`, `system`).
- Every entity page ends with `## Open questions`.
- Entities reference each other freely via `[[wikilinks]]`.
```

### Task 2.2: `wiki/Entities/People/README.md`

````markdown
---
title: People — Folder Guide
type: schema
created: 2026-05-05
updated: 2026-05-11
tags: [schema, folder-guide]
---

# Entities/People/

One canonical synthesised note per person the team interacts with. Source
seeds live in `raw/people/<First Last>.md`; this folder holds the richer
evolving note.

### Filename

`<First Last>.md` — exact display name, English. No emoji, no
parenthetical role.

### Frontmatter

```yaml
---
title: <First Last>
type: person
tags: [person, wiki]
role: <current role>
org: <Cybereason | Level Blue | vendor | external>
team: <team name>             # optional
seeds: [raw/people/<First Last>.md]
related_projects: [[Project A]], [[Project B]]
first_seen: YYYY-MM-DD
last_updated: YYYY-MM-DD
---
```

### Body shape

```markdown
# <First Last>

> One-sentence orientation in DS context.

## Background

## Mentions

Append-only timeline.
- 2026-05-08 — [[2026-05-08 — Tipper rollout retro]] — proposed fallback
  classifier path

## Related entities

## Open questions
```

### Update workflow

Appended to by `/ingest` (Phase B) when an external source mentions them.
Never rewrite the whole page — append `## Mentions` rows and bump
`last_updated`.
````

### Task 2.3: `wiki/Entities/Projects/README.md`

````markdown
---
title: Projects — Folder Guide
type: schema
created: 2026-05-05
updated: 2026-05-11
tags: [schema, folder-guide]
---

# Entities/Projects/

One synthesised canonical note per active DS project. Source artifacts
(decks, drawio, design docs) stay under
`raw/projects/{Project,Itamar Project} - <name>/`.

### Filename

`<Project name>.md` — drop the `Project - ` or `Itamar Project - ` prefix
from the raw folder. Use the team's canonical short name.

### Frontmatter

```yaml
---
title: <Project name>
type: project
tags: [project, wiki]
status: <proposed | active | paused | completed | archived>
lead: [[<First Last>]]
team: [[<First>]], [[<Last>]]
started: YYYY-MM-DD
target_ship: YYYY-MM-DD
systems: [[Tipper]], [[URLDeep]]
related_decisions: [[2026-04-15 — go on AIDRA]]
raw_path: raw/projects/Project - <name>/
last_updated: YYYY-MM-DD
---
```

### Body shape

```markdown
# <Project name>

> One-sentence problem statement.

## Goal

## Approach

## Status

## Decisions

## Risks

## Mentions

## Open questions
```
````

### Task 2.4: `wiki/Entities/Systems/README.md`

````markdown
---
title: Systems — Folder Guide
type: schema
created: 2026-05-07
updated: 2026-05-11
tags: [schema, folder-guide]
---

# Entities/Systems/

One synthesised note per product / component / external system the team
integrates with. Distinct from `Projects/` — Systems covers stable product
surfaces, third-party tools, and platform components consumed or extended
by the team.

### Filename

`<System name>.md` (no prefix).

### Frontmatter

```yaml
---
title: <System name>
type: system
tags: [system, wiki]
owner: <Cybereason team | vendor | open-source>
vendor: <if external>
integration_surface: [API, file-drop, message-bus]
related_projects: [[Project A]]
last_updated: YYYY-MM-DD
---
```

### Body shape

```markdown
# <System name>

> One-sentence: what this system does.

## Owner / vendor

## Integration surface

## Data flow

## Current usage

## Known issues

## Related entities

## Open questions
```
````

### Task 2.5: `wiki/Meetings/README.md`

````markdown
---
title: Meetings — Folder Guide
type: schema
created: 2026-05-05
updated: 2026-05-11
tags: [schema, folder-guide]
---

# Meetings/

Distilled outcomes from `raw/meetings/meeting_*` transcripts. One note per
meeting. Source filenames are inconsistent (`meeting_2026-01-29_X`,
`meeting_2026.04.27_x_y.txt`) — normalise the wiki filename.

### Filename

`YYYY-MM-DD — <topic>.md`.

### Frontmatter

```yaml
---
title: <topic>
type: meeting
tags: [meeting, wiki]
date: YYYY-MM-DD
participants: [[<First Last>]], [[<First Last>]]
related_projects: [[Project A]]
related_decisions: []
source: raw/meetings/meeting_<original>.txt
last_updated: YYYY-MM-DD
---
```

### Body shape

```markdown
# <topic> — YYYY-MM-DD

> One-sentence outcome.

## Decisions

## Action items

- [ ] <task> — [[<owner>]] — due YYYY-MM-DD

## Discussion notes

(Distil, never transcribe.)

## Open questions
```
````

### Task 2.6: `wiki/Decisions/README.md`

````markdown
---
title: Decisions — Folder Guide
type: schema
created: 2026-05-05
updated: 2026-05-11
tags: [schema, folder-guide]
---

# Decisions/

DS-leadership decisions / ADRs (org design, hiring, budget, project
go/no-go, scoping). Always include WHY + tradeoff.

### Filename

`YYYY-MM-DD — <decision title>.md`.

### Frontmatter

```yaml
---
title: <decision title>
type: decision
tags: [decision, wiki]
date: YYYY-MM-DD
deciders: [[<First Last>]]
status: <proposed | accepted | superseded | reversed>
supersedes: [[YYYY-MM-DD — <old decision>]]
related_projects: [[Project A]]
last_updated: YYYY-MM-DD
---
```

### Body shape

```markdown
# <decision title> — YYYY-MM-DD

## Context

## Decision

## Why

## Alternatives considered

## Consequences

## Open questions
```
````

### Task 2.7: `wiki/Ideas/README.md`

````markdown
---
title: Ideas — Folder Guide
type: schema
created: 2026-05-05
updated: 2026-05-11
tags: [schema, folder-guide]
---

# Ideas/

Product or research ideas with rationale. Filename: `<title>.md`.

### Frontmatter

```yaml
---
title: <idea title>
type: idea
tags: [idea, wiki]
proposer: [[<First Last>]]
status: <draft | investigating | adopted-as-project | shelved>
hypothesis: <one sentence>
related_projects: [[Project A]]
last_updated: YYYY-MM-DD
---
```

### Body shape

```markdown
# <idea title>

## Hypothesis

## Evidence

## Evaluation criteria

## Risks

## Next step

## Open questions
```
````

### Task 2.8: `wiki/Research/README.md`

````markdown
---
title: Research — Folder Guide
type: schema
created: 2026-05-05
updated: 2026-05-11
tags: [schema, folder-guide]
---

# Research/

ML / AI / security concept notes (papers, frameworks, theories, evaluation
methodologies). Equivalent to `wiki/concepts/` in the reference vault,
scoped to DS subject matter.

### Filename

`<concept>.md`.

### Frontmatter

```yaml
---
title: <concept>
type: research
tags: [research, wiki]
domain: <ml | nlp | security | ops | eval>
derived_from: [[Source A]], [[Source B]]
related_projects: [[Project A]]
last_updated: YYYY-MM-DD
---
```

### Body shape

```markdown
# <concept>

> One-paragraph orientation.

## What it is

## Why we care

## Manifestations

(Append-only. Each entry: date, wikilink, one-line context.)

## Tensions

(If sources disagree, list both with wikilinks.)

## Open questions
```
````

### Task 2.9: `wiki/Sources/README.md`

````markdown
---
title: Sources — Folder Guide
type: schema
created: 2026-05-11
updated: 2026-05-11
tags: [schema, folder-guide]
---

# Sources/

One-page summary per external source the wiki cites (paper, blog post,
talk, slack export, customer interview). Created at `/ingest` time when
the source is external.

### Existing seeds

Two already in place:
- `Karpathy — LLM Wiki Gist.md` — canonical spec for this vault
- `LevelBlue — Acquisition of Cybereason.md` — active org context

Both need a Phase 2.14 retag pass to add the mandatory `wiki` tag.

### Filename

`<slug>.md` — title-case OK; year suffix optional. No path slashes.

### Frontmatter

```yaml
---
title: <full title>
type: source
tags: [source, wiki, source_type/<paper|talk|blog|slack|interview|deck>]
authors: [<name>, <name>]
year: YYYY
url: https://...
raw_path: raw/<tab>/<file>     # post-ingest location
last_updated: YYYY-MM-DD
---
```

### Body shape

```markdown
# <full title>

> One-sentence headline finding.

## Summary

3–8 bullet points — synthesised takeaways, not a verbatim abstract.

## Why we care

## Cited from

(Append-only. Wikilink per citing page.)

## Open questions
```
````

### Task 2.10: `wiki/Syntheses/README.md`

````markdown
---
title: Syntheses — Folder Guide
type: schema
created: 2026-05-05
updated: 2026-05-11
tags: [schema, folder-guide]
---

# Syntheses/

LLM-generated answers worth keeping (file-back-queries pattern from
Karpathy). Created from `/query` when filing is approved, or at monthly
cadence to capture "what's shifted" overviews.

### Filename

`YYYY-MM-DD — <question or theme>.md`.

### Frontmatter

```yaml
---
title: <question or theme>
type: synthesis
tags: [synthesis, wiki]
derived_from: [[Page A]], [[Page B]], [[Page C]]
asker: [[<First Last>]]
last_updated: YYYY-MM-DD
---
```

### Body shape

```markdown
# <question or theme>

> One-sentence headline answer.

## Answer

(Every claim cited inline via [[wikilink]]. No uncited claims.)

## Follow-up questions
```
````

### Task 2.11: `wiki/Connections/README.md`

````markdown
---
title: Connections — Folder Guide
type: schema
created: 2026-05-05
updated: 2026-05-11
tags: [schema, folder-guide]
---

# Connections/

Cross-domain patterns spotted **≥2 times**. Where Research/ holds atomic
concepts and Syntheses/ holds answers, Connections captures recurring
shapes spanning multiple Projects / People / Systems.

### Filename

`<pattern>.md`.

### Frontmatter

```yaml
---
title: <pattern>
type: connection
tags: [connection, wiki]
instances: [[<Project A>]], [[<Project B>]], [[<Meeting>]]
last_updated: YYYY-MM-DD
---
```

### Body shape

```markdown
# <pattern>

> One-sentence pattern statement (abstracted).

## Instances

(≥2 required; wikilink + one-line evidence each.)

## What we infer

## Open questions
```
````

### Task 2.12: `wiki/🔥 Hot Notes/README.md`, `wiki/Memories/README.md`, `wiki/Log/README.md` (sub-batch)

**Sub-batch — write all three in one message.**

- [ ] **`wiki/🔥 Hot Notes/README.md`**

```markdown
---
title: 🔥 Hot Notes — Folder Guide
type: schema
created: 2026-05-11
updated: 2026-05-11
tags: [schema, folder-guide]
---

# 🔥 Hot Notes/

Live working memory. **Cap: 7 notes.** Anything older than two weeks that
isn't being actively edited graduates to a permanent folder or gets
archived.

Two anchor notes always live here:

- `Active Focus.md` — what the team is heads-down on this week.
- `Brain Architecture.md` — the current shape of the wiki itself.

`/lint` flags Hot Notes older than 14 days that haven't been edited.

## Note shape

Standard wiki frontmatter (`title`, `type: hot`, `tags: [hot, wiki]`,
`last_updated`). No fixed body schema.
```

- [ ] **`wiki/Memories/README.md`**

````markdown
---
title: Memories — Folder Guide
type: schema
created: 2026-05-11
updated: 2026-05-11
tags: [schema, folder-guide]
---

# Memories/

Durable team-level know-how that doesn't fit a single Entity / Project /
Decision: failure patterns, conventions, the "we tried that in 2024"
stories.

### Filename

Free-form English, Title Case.

### Frontmatter

```yaml
---
title: <memory>
type: memory
tags: [memory, wiki]
related_projects: [[Project A]]
last_updated: YYYY-MM-DD
---
```

### Body shape

```markdown
# <memory>

## What happened

## Why it matters now

## Related
```
````

- [ ] **`wiki/Log/README.md`**

````markdown
---
title: Log — Folder Guide
type: schema
created: 2026-05-11
updated: 2026-05-11
tags: [schema, folder-guide]
---

# Log/

Three files, never split into per-day pages.

| File | Purpose | Update cadence | Append direction |
|---|---|---|---|
| `INDEX.md` | Structural navigation (every page, grouped by folder, with one-line summary) | Touched on every ingest / synthesis / removal | Replaces sections |
| `wiki-ops.md` | Audit trail of operations | Every `/ingest`, `/query` (filed), `/lint` (fixed), `/remove`, `/braindump` | Prepend below the `---` preamble separator |
| `pulse.md` | One-line-per-day operational notes (VM health, cron status, anomalies) | Daily cron tick | Append at bottom |

### `wiki-ops.md` entry shape

```
## [YYYY-MM-DD] <op> | <subject>
- wiki/<path>.md (new|updated|archived)
Files moved:
- INBOX/<old> → raw/<tab>/<new>
```

### `INDEX.md` shape

One H2 per top-level wiki folder, bulleted wikilinks with one-line
summaries. Regenerated by `/lint` or hand-edited during ingest.
````

### Task 2.13: Refresh `wiki/🗺️ Maps/README.md` and `wiki/📦 Archive/README.md`

Both already exist with good content. Just bump the `updated:` field to `2026-05-11`. Single batched Edit message.

### Task 2.14: Retag existing notes — add `wiki` tag (PARALLEL)

**Files (read all in one message; Edit all in one message):**
- `wiki/Sources/Karpathy — LLM Wiki Gist.md`
- `wiki/Sources/LevelBlue — Acquisition of Cybereason.md`
- `wiki/🔥 Hot Notes/Active Focus.md`

For each, edit the frontmatter `tags:` line to include `wiki`:

- Karpathy gist: `tags: [karpathy, llm-wiki, second-brain, schema]` → `tags: [source, wiki, karpathy, llm-wiki, second-brain]`
- LevelBlue: `tags: [levelblue, cybereason, acquisition, org-context]` → `tags: [source, wiki, levelblue, cybereason, acquisition, org-context]`
- Active Focus: `tags: [active, focus, hot]` → `tags: [hot, wiki, active, focus]`

Also add `last_updated: 2026-05-11` to each if missing.

### Task 2.15: Phase 2 verification + commit

- [ ] **Step 1: Lint**

```bash
cd tools && uv run python -m lint.run_all
```
Expected: 0 frontmatter violations on existing notes (Phase 2.14 fixed them).
Orphans expected on every README.md — filtered out. Stale links possible on
Karpathy gist (`folder_tree.md` reference) — surface, fix in Step 2.

- [ ] **Step 2: Fix surfaced stale links**

`wiki/Sources/Karpathy — LLM Wiki Gist.md` references `folder_tree.md`,
`Brain Architecture.md`, `CLAUDE.md` which don't exist yet. Either:
- replace with a deferred note: "See [[Brain Architecture]] once Phase 4
  lands"
- or leave; Phase 4 + Phase 5 create the targets and stale-link clears.

Prefer leaving and committing — stale at this snapshot, fixed by
end-of-plan.

- [ ] **Step 3: Commit Phase 2**

```bash
git add wiki/ CLAUDE.md
git commit -m "schema: author all folder READMEs + retag existing notes (Phase 2)"
```

---

## Phase 3 — Bootstrap wiki content from `raw/` (HEAVY PARALLELISM)

Phase 2 produced the schema. Phase 3 fills the wiki from raw inputs. Three
top-level lanes, each runs as a fan-out of subagents.

### Task 3.0: Pre-flight raw inventory

- [ ] **Step 1: Confirm counts**

```bash
echo "people:    $(find raw/people -type f -name '*.md' | wc -l)"
echo "projects:  $(find raw/projects -maxdepth 1 -type d | tail -n +2 | wc -l) folders"
echo "meetings:  $(ls raw/meetings | wc -l)"
echo "level_blue:$(ls raw/level_blue | wc -l)"
```
Reference baseline (2026-05-11): people=50, projects=27 folders, meetings=6,
level_blue=3.

- [ ] **Step 2: Convert binary DS Drive files**

```bash
cd tools && uv run python -m convert.docx_to_md ../raw/data_science_drive/Data\ Science\ -\ Main.docx
cd tools && uv run python -m convert.docx_to_md ../raw/data_science_drive/_Ideas/Deep\ Research\ -\ Data\ Science\ Projects\ Portfolio\ for\ Cybereason\ and\ LevelBlue.docx
cd tools && uv run python -m convert.xlsx_to_md ../raw/data_science_drive/Data\ Science\ Projects.xlsx
cd tools && uv run python -m convert.xlsx_to_md ../raw/data_science_drive/VMs.xlsx
```

The PreToolUse guard blocks Write into `raw/`. **Workaround for converter
output:** write to `INBOX/converted/` instead and ingest from there.
Re-run with `--out INBOX/converted/`:

Pass `OUT_DIR` env or sentinel:

```bash
mkdir -p INBOX/converted
cd tools && OUT_DIR=../INBOX/converted uv run python -c "
from pathlib import Path; from convert.docx_to_md import docx_to_markdown
src = Path('../raw/data_science_drive/Data Science - Main.docx')
out = Path('../INBOX/converted/data-science-main.md')
out.write_text(docx_to_markdown(src), encoding='utf-8')
print(out)
"
```
(Pattern repeats for each file. Optional: add `--out` flag to converters in
a follow-up commit.)

- [ ] **Step 3: Commit converted markdown to INBOX**

```bash
git add INBOX/converted/
git commit -m "raw: convert DS Drive .docx/.xlsx → markdown into INBOX/converted/"
```

### Task 3.A: Build People pages (50 parallel subagents in 5 batches of 10)

**Files:**
- Read per subagent: `raw/people/<First Last>.md`, plus grep results from
  `raw/meetings/` and `raw/projects/`
- Create per subagent: `wiki/Entities/People/<First Last>.md`

**Strategy.** Dispatch in 5 batches of 10 subagents each (≤10 keeps the
single-message size manageable). Each subagent gets the same brief:

```
You are filling wiki/Entities/People/<First Last>.md from raw seeds.

INPUTS (batch reads in ONE message):
- raw/people/<First Last>.md
- any file under raw/meetings/ whose body contains "<First Last>"
- any file under raw/projects/ whose body contains "<First Last>"

OUTPUT (single Write):
- wiki/Entities/People/<First Last>.md per the wiki/Entities/People/README.md
  template.

Constraints:
- Wikilinks only; tags must include `person, wiki`.
- ## Mentions ordered oldest → newest.
- Do NOT invent facts. Omit unknown fields.
- Cite raw/ paths in `seeds:` frontmatter.
- Return: file path + 3-line summary.
```

- [ ] **Step 1: Get the people list**

```bash
ls raw/people/ | sed 's/\.md$//' > /tmp/people.txt
wc -l /tmp/people.txt
```

- [ ] **Step 2: Dispatch batch 1 of 5 (people 1–10) — single message, 10 subagents**

(Repeat for batches 2–5.)

- [ ] **Step 3: Verify**

```bash
ls wiki/Entities/People/ | wc -l
```
Expected: 50 (+ README.md = 51 entries).

- [ ] **Step 4: Lint snapshot**

```bash
cd tools && uv run python -m lint.run_all || true
```
Stale-link warnings expected (people reference Projects not yet built).
Move on.

- [ ] **Step 5: Commit lane 3.A**

```bash
git add wiki/Entities/People/
git commit -m "wiki: seed 50 People pages from raw/people/ (Phase 3.A)"
```

### Task 3.B: Build Projects (27 subagents) + Systems pages

**Files:**
- Read per subagent: `raw/projects/{Project,Itamar Project} - <name>/*`
- Create per subagent: `wiki/Entities/Projects/<name>.md`
- Plus one Systems-discovery subagent

**Strategy.** 27 parallel subagents in 3 batches of 9. Each gets:

```
You are filling wiki/Entities/Projects/<name>.md from one raw project folder.

INPUTS (batch reads):
- every file under raw/projects/<original folder name>/
- any meeting in raw/meetings/ whose body mentions the project

OUTPUT (one Write):
- wiki/Entities/Projects/<name>.md per wiki/Entities/Projects/README.md.

Constraints:
- Strip `Project - ` / `Itamar Project - ` prefix on the wiki filename.
- Wikilinks only. Tag must include `project, wiki`.
- People refs go via [[<First Last>]] — pages exist from Phase 3.A.
- Decisions section: leave empty if no decision yet; do not invent.
- Set `raw_path:` frontmatter to the original folder path.
```

Plus one **Systems discovery** subagent:

```
Discover wiki/Entities/Systems/ pages from raw/cybereason/ and
raw/data_science_drive/.

Heuristic: capitalised proper noun recurring ≥2× across files. Conservative
— prefer missing a system over inventing.

OUTPUT (batched Writes):
- wiki/Entities/Systems/<System>.md per the README template, one per
  distinct system, citing the raw paths.

Likely targets: Tipper, MailMarshal, URLDeep, Snowflake, BigQuery, Airflow.
Confirm each via grep before writing.
```

- [ ] **Step 1: Build prefix-strip map**

```bash
ls raw/projects/ | sed -E 's/^(Itamar Project - |Project - )//' | sort | uniq
```
Surface duplicates (same name post-strip): write Project name plus
`(prefix: Itamar)` suffix to disambiguate. Currently none expected.

- [ ] **Step 2: Dispatch project batches in 3 messages of 9 subagents**

- [ ] **Step 3: Dispatch the single Systems discovery subagent** (can run in
  parallel to Step 2's batches if file-disjoint — and it is, since Systems
  reads raw/cybereason/, Projects reads raw/projects/).

- [ ] **Step 4: Verify**

```bash
ls wiki/Entities/Projects/
ls wiki/Entities/Systems/
```

- [ ] **Step 5: Commit lane 3.B**

```bash
git add wiki/Entities/Projects/ wiki/Entities/Systems/
git commit -m "wiki: seed Projects (27) + Systems pages from raw/ (Phase 3.B)"
```

### Task 3.C: Build Meetings (6 parallel subagents)

**Files:**
- Read: `raw/meetings/<file>`
- Create: `wiki/Meetings/YYYY-MM-DD — <topic>.md`

Per-meeting subagent brief:

```
Fill wiki/Meetings/YYYY-MM-DD — <topic>.md from one transcript.

INPUT: raw/meetings/<original file>

OUTPUT: wiki/Meetings/YYYY-MM-DD — <topic>.md per the README template.

Constraints:
- Parse the date from filename (handles both `meeting_2026-01-29_X` and
  `meeting_2026.04.27_x_y.txt` formats).
- Participants resolve to [[<First Last>]] wikilinks; if a name doesn't
  match an existing wiki/Entities/People/ page, flag it (don't invent).
- Distil. Do NOT transcribe.
- Decisions: bullet form, each with wikilink to a candidate
  wiki/Decisions/ page (don't write the Decisions page here — Phase 3.D
  extracts).
- Action items: `- [ ] <task> — [[<owner>]] — due YYYY-MM-DD`.
```

- [ ] **Step 1: Dispatch all 6 in a single message**

- [ ] **Step 2: Collate unresolved-name flags**

If any subagent reported "name X not in Entities/People/", surface as a
follow-up list. Do not auto-create.

- [ ] **Step 3: Commit lane 3.C**

```bash
git add wiki/Meetings/
git commit -m "wiki: seed Meetings pages from raw/meetings/ (Phase 3.C)"
```

### Task 3.D: Extract Decisions + Connections (sequential, AFTER 3.A+B+C)

Depends on outputs of A/B/C.

- [ ] **Step 1: Decision-extraction subagent**

```
Extract Decisions from the wiki/Meetings/ pages just written.

INPUT: every file under wiki/Meetings/

OUTPUT (batched Writes):
- wiki/Decisions/YYYY-MM-DD — <title>.md per the template, one per concrete
  decision identified.

A "concrete decision" has named decider(s), a date, and a yes/no outcome
(or "X over Y" tradeoff). Vague aspirations are Ideas, not Decisions.

Back-link from the source Meeting page (`related_decisions:` frontmatter).
Update the affected Project page's `## Decisions` section.
```

- [ ] **Step 2: Connections-extraction subagent**

```
Extract Connections (cross-domain ≥2-instance patterns) from the seeded
wiki.

INPUT: wiki/Entities/Projects/, wiki/Entities/Systems/, wiki/Meetings/,
wiki/Decisions/

OUTPUT: wiki/Connections/<pattern>.md per template. ≥2 instances required;
cite each.

Conservative — fewer high-quality Connections beats many speculative ones.
```

- [ ] **Step 3: Dispatch both in one message**

- [ ] **Step 4: Commit**

```bash
git add wiki/Decisions/ wiki/Connections/ wiki/Meetings/ wiki/Entities/Projects/
git commit -m "wiki: extract Decisions + Connections (Phase 3.D)"
```

### Task 3.E: Ingest DS Drive converted files + Level Blue

- [ ] **Step 1: Run `/ingest INBOX/converted/data-science-main.md`** — likely
  feeds Memories/ and Active Focus updates.

- [ ] **Step 2: Run `/ingest INBOX/converted/data-science-projects.md`** —
  cross-references with Phase 3.B Projects.

- [ ] **Step 3: Run `/ingest INBOX/converted/vms.md`** — likely seeds
  Memories/ ("which VM runs what") or a `Systems/Team VM.md` page.

- [ ] **Step 4: Run `/ingest raw/level_blue/products.md`** — feeds existing
  `wiki/Sources/LevelBlue — Acquisition of Cybereason.md` plus a new
  `Systems/LevelBlue Platform.md` or similar.

Each `/ingest` follows its command spec — pause for approval, parallel
phase B writes, then commit + push.

---

## Phase 4 — Index, Hot Notes, Log (sequential, after Phase 3)

### Task 4.1: Generate `wiki/Log/INDEX.md`

Single subagent walks `wiki/` (excluding `📦 Archive/`), groups by
top-level folder, one bullet per `.md` file with a one-line summary drawn
from the file's first non-frontmatter paragraph.

Folder order: Entities/People, Entities/Projects, Entities/Systems,
Meetings, Decisions, Ideas, Research, Sources, Syntheses, Connections,
🔥 Hot Notes, Memories.

Frontmatter:
```yaml
---
title: Wiki INDEX
type: index
tags: [index, wiki]
generated: 2026-05-11
last_updated: 2026-05-11
---
```

- [ ] **Verify lint**

```bash
cd tools && uv run python -m lint.run_all
```
Expected: orphan count drops to near zero; remaining orphans are intentional
(e.g. Log/ files, README.md).

### Task 4.2: Seed `wiki/🔥 Hot Notes/Brain Architecture.md`

`Active Focus.md` already exists; keep it. Create `Brain Architecture.md`:

```markdown
---
title: Brain Architecture
type: hot
tags: [hot, wiki]
last_updated: 2026-05-11
---

# Brain Architecture

> Current shape of the wiki itself. Read this when starting a Claude Code
> session.

## Layers (Karpathy)

| Layer | Where | Owner | Mutability |
|---|---|---|---|
| Raw | `raw/`, `INBOX/` | Humans | Append-only (guarded by PreToolUse hook) |
| Wiki | `wiki/` | Claude | Free |
| Schema | `CLAUDE.md`, `.claude/`, `tools/`, `scripts/` | DS leadership + Claude | Co-evolves |

## Folder map

- `Entities/People/` — 50 seed pages from `raw/people/`
- `Entities/Projects/` — 27 active projects from `raw/projects/`
- `Entities/Systems/` — third-party + platform components
- `Meetings/` — distilled outcomes
- `Decisions/` — DS-leadership ADRs
- `Ideas/` — hypotheses
- `Research/` — ML/AI/security concepts
- `Sources/` — external-source one-pagers
- `Syntheses/` — filed `/query` answers
- `Connections/` — ≥2-instance patterns
- `🔥 Hot Notes/` — active working memory (≤7)
- `🗺️ Maps/` — Obsidian canvases (placeholder)
- `📦 Archive/` — soft-deleted notes
- `Memories/` — durable team know-how
- `Log/` — `INDEX.md` + `wiki-ops.md` + `pulse.md`

## Operations

`/ingest`, `/query`, `/lint`, `/remove`, `/braindump` — see
`.claude/commands/`.

## Drift / intended next changes

(empty — populate as the team learns)

## Open questions
```

### Task 4.3: Seed `wiki/Log/wiki-ops.md` and `wiki/Log/pulse.md`

`wiki-ops.md`:

```markdown
---
title: Wiki Ops Log
type: log
tags: [log, wiki]
direction: prepend (newest on top)
last_updated: 2026-05-11
---

## [2026-05-11] bootstrap | initial wiki content
- wiki/Entities/People/* (50 new)
- wiki/Entities/Projects/* (27 new)
- wiki/Entities/Systems/* (new)
- wiki/Meetings/* (6 new)
- wiki/Decisions/* (extracted)
- wiki/Connections/* (extracted)
- wiki/Log/INDEX.md (new)
- wiki/🔥 Hot Notes/Brain Architecture.md (new)
```

`pulse.md`:

```markdown
---
title: Daily Pulse
type: log
tags: [log, wiki]
direction: append (newest at bottom)
last_updated: 2026-05-11
---

# Daily Pulse

| Date | VM | Cron | Notes |
|---|---|---|---|
| 2026-05-11 | bootstrap | n/a | repo initialised, second-brain bootstrap |
```

- [ ] **Commit Phase 4**

```bash
git add wiki/Log/ wiki/🔥\ Hot\ Notes/Brain\ Architecture.md
git commit -m "wiki: generate INDEX.md + seed Brain Architecture + Log/ files (Phase 4)"
```

---

## Phase 5 — Cron + Obsidian (parallel where possible)

### Task 5.A: Weekly `/lint` cron on the Ubuntu VM

**Files:**
- Create: `scripts/cron/weekly-lint.sh`

```bash
#!/bin/bash
# Weekly LLM lint via Claude Code in non-interactive mode.
set -euo pipefail

cd /home/dsbrain/ds-brain
git fetch --quiet origin unified
git reset --hard origin/unified

mkdir -p logs
claude -p "/lint" --output-format=json 2>&1 | tee -a "logs/lint-$(date +%F).log"
```

```bash
chmod +x scripts/cron/weekly-lint.sh
```

Print to user:
```
Add to dsbrain crontab:
  0 3 * * 0 /home/dsbrain/ds-brain/scripts/cron/weekly-lint.sh
```

- [ ] **Commit**

```bash
git add scripts/cron/
git commit -m "infra: weekly /lint cron script"
```

### Task 5.B: Obsidian setup doc

**Files:**
- Create: `docs/obsidian-setup.md`

```markdown
# Obsidian setup

1. Open `ds-brain/` as an Obsidian vault.
2. Settings → Community plugins → Turn on community plugins.
3. Install: **Smart Connections** (search the directory).
4. Settings → Smart Connections → choose embedding model (default
   MiniLM). Re-index on first open.
5. Commit `.obsidian/community-plugins.json` and
   `.obsidian/plugins/smart-connections/data.json` for team consistency.
   Exclude the `.smart-env/` cache via `.gitignore`.
```

- [ ] **Add to `.gitignore`**

```
.smart-env/
.obsidian/workspace.json
.obsidian/workspace-mobile.json
```

- [ ] **Commit**

```bash
git add docs/obsidian-setup.md .gitignore
git commit -m "docs: Obsidian + Smart Connections setup"
```

---

## Phase 6 — Final lint + smoke test + push

### Task 6.1: Full deterministic + LLM lint pass

- [ ] **Deterministic**

```bash
cd tools && uv run python -m lint.run_all
```
Fix anything that surfaces. Repeat until clean (or all remaining issues are
intentional and noted in `wiki/Log/wiki-ops.md`).

- [ ] **LLM lint**

Run `/lint` per the command file. Apply approved fixes; commit per command
protocol.

- [ ] **Final push**

```bash
git push origin unified
```

### Task 6.2: Smoke-test each slash command (manual)

- [ ] `/ingest` — drop a dummy file into `INBOX/`, run `/ingest`, verify
  wiki update + `git mv` to `raw/`.
- [ ] `/query` — ask a question the wiki should answer; verify cited
  answer.
- [ ] `/lint` — verify deterministic + LLM phases both run.
- [ ] `/remove` — soft-delete a placeholder page; verify Archive move +
  lint still passes.
- [ ] `/braindump` — drop a multi-paragraph thought; verify it lands in
  the right folders.

- [ ] **Capture results**

Write `docs/superpowers/plans/2026-05-11-ds-team-second-brain.smoke-test.md`
with: command, duration, files touched, pass/fail.

```bash
git add docs/superpowers/plans/2026-05-11-ds-team-second-brain.smoke-test.md
git commit -m "docs: smoke-test report for second-brain bootstrap"
git push origin unified
```

---

## Self-review

**Spec coverage.** Karpathy three-layer pattern: Phase 1 schema (`CLAUDE.md`,
`.claude/`), Phase 2 conventions (folder READMEs), Phase 3 raw→wiki bootstrap.
Five operations: `/ingest`, `/query`, `/lint`, `/remove`, `/braindump`
(Task 1.3). Deterministic lint with TDD (Task 1.4). Binary-source converters
(Task 1.5). Existing seed Sources + Hot Note retagged (Task 2.14).
Parallelisation: 12 folder READMEs (Phase 2), 50+27+6 content lanes
(Phase 3), 5 LLM lint subagents (Phase 6).

**Placeholder scan.** No `TBD` / `TODO` left. All step content is concrete:
code blocks where code is needed, exact commands where commands are needed,
exact frontmatter templates in every README task.

**Type consistency.** `last_updated` is the date field everywhere.
`wiki` tag enforced in `CLAUDE.md`, READMEs, and lint code
(`check_frontmatter.py`). `Log/INDEX.md`, `Log/wiki-ops.md`, `Log/pulse.md`
filenames used consistently. Project filename strips both
`Project - ` and `Itamar Project - ` prefixes consistently.

**Known follow-ups (intentionally deferred, out of scope for "bootstrap"):**

- `raw/cybereason/` 295-file KB — bulk ingest will overwhelm wiki noise;
  ingest on-demand per query/topic instead.
- `raw/data_science_drive/_General/azure_config.json` — not human-readable
  prose, skip.
- `.pptx` / `.drawio` converters — punt; `/ingest` describes "read the
  source", a human can summarise these manually until needed.
- A monthly `/synthesise` cadence command (sibling of `/query` for trend-
  spotting). Punt until 3+ months of operations log.
- Web-search-augmented Research notes.
- Obsidian Smart Connections re-index automation.
