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
`.claude/hooks/guard_immutable.py` PreToolUse hook enforces this.

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
   - `Entities/Teams/` — sub-units within an Organization (DS Team, SLR, Engineering, Spider Labs, …)
   - `Entities/Organizations/` — companies/vendors/customers/standards bodies (Cybereason, LevelBlue, Trustwave, Anthropic, MITRE, …)
   - `Entities/Projects/` — one canonical note per active DS project
   - `Entities/Systems/` — products/components the team integrates with
   - `Entities/Concepts/` — atomic named ideas / techniques / frameworks (LoRA, Prompt Injection, Sigma) — lighter-weight than `Research/`
   - `Entities/Locations/` — geographic / office locations the team operates from
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
   - `INDEX.md` (vault root) — structural navigation: one section per
     top-level folder, every page bulleted with a one-line summary
   - `Log/` — `wiki-ops.md` (audit trail), `pulse.md` (daily ops notes)

3. **Schema** — `CLAUDE.md`, `.claude/`, `tools/`, `server/`. Defines
   conventions, commands, hooks, lint. Co-evolves between DS leadership and
   Claude.

## Key rules for Claude

- **Never edit a `raw/` note's body.** Frontmatter touch-ups okay only on
  explicit user request. The PreToolUse guard will block accidental writes.
- **Always update `wiki/INDEX.md`** and prepend to `wiki/Log/wiki-ops.md`
  (newest on top, below the `---` preamble separator) when ingest / lint /
  remove / braindump / synthesis touches the wiki.
- **Log files in `wiki/Log/` are append-only, prepend-order**
  (`wiki-ops.md`, `pulse.md`). New entries go directly under the
  preamble — never edit or delete past entries; they are the historical
  record. The `direction: prepend (newest on top)` and `append_only: true`
  frontmatter fields are the enforced signal.
- **Wikilinks only.** `[[Entity Name]]`, never markdown links.
- **Frontmatter is required** on every `wiki/` page. Every wiki page must
  carry `wiki` in its `tags` array (typically the second tag, after the
  domain tag). This is the layer marker — mirrors the `raw` tag concept on
  raw notes.
- **Filename conventions** vary per folder; see the folder's `README.md`.
- **Smart Connections** (community Obsidian plugin) provides semantic
  search. Use it for "similar to X" questions; use `wiki/INDEX.md` for
  structural navigation.
- **Session start.** Every session, after this `CLAUDE.md`, also read
  `wiki/INDEX.md`, `wiki/🔥 Hot Notes/Active Focus.md`, and
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
