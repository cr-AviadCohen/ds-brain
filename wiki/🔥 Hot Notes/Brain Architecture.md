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
| --- | --- | --- | --- |
| Raw | `raw/`, `INBOX/` | Humans | Append-only (guarded by PreToolUse hook) |
| Wiki | `wiki/` | Claude | Free |
| Schema | `CLAUDE.md`, `.claude/`, `tools/`, `scripts/` | DS leadership + Claude | Co-evolves |

## Topology (team-wide rollout — 2026-05-12)

Local vs. server roles when the brain is shared across the four-person DS
team ([[Aviad Cohen]], [[Guy Kassorla]], [[Itamar Hershko]],
[[Inbar Dekel]]):

- **Local Claude** (in [[Cursor]] / Obsidian via MCP) — **reads** `wiki/`
  for queries, **writes only** into `INBOX/`. Never mutates `raw/` or
  `wiki/`. Boundary enforced by a Skill / system prompt — see
  [[2026-05-12 — Local Claude Write-Only to INBOX]].
- **Server Claude** (shared Ubuntu VM) — sole authority for
  `INBOX/ → raw/ + wiki/` ingest and for daily `/lint` — see
  [[2026-05-12 — Server VM as Sole Ingest Authority]].
- **Branch model** — single `unified` branch for all users; no split or
  sparse checkout — see
  [[2026-05-12 — Unified Branch over Split for DS Brain]].

Full project view: [[DS Brain]].

## Folder map

- `Entities/People/` — 50 seed pages from `raw/people/`
- `Entities/Projects/` — 28 active projects from `raw/projects/`
- `Entities/Systems/` — third-party + platform components
- `Meetings/` — distilled outcomes
- `Decisions/` — DS-leadership ADRs
- `Ideas/` — hypotheses (empty at bootstrap)
- `Research/` — ML/AI/security concepts (empty at bootstrap)
- `Sources/` — external-source one-pagers
- `Syntheses/` — filed `/query` answers (empty at bootstrap)
- `Connections/` — ≥2-instance patterns
- `🔥 Hot Notes/` — active working memory (≤7)
- `🗺️ Maps/` — Obsidian canvases (placeholder)
- `📦 Archive/` — soft-deleted notes
- `Memories/` — durable team know-how (empty at bootstrap)
- `INDEX.md` (vault root) — structural navigation across the whole wiki
- `Log/` — `wiki-ops.md` (audit trail) + `pulse.md` (daily ops)

## Operations

`/ingest`, `/query`, `/lint`, `/remove`, `/braindump` — see
`.claude/commands/`.

## Drift / intended next changes

(empty — populate as the team learns)

## Open questions
