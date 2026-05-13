---
title: Local Claude Write-Only to INBOX
type: decision
tags: [decision, wiki]
date: 2026-05-12
deciders: ["[[Aviad Cohen]]", "[[Guy Kassorla]]"]
status: accepted
related_projects: ["[[DS Brain]]"]
last_updated: 2026-05-12
---

# Local Claude Write-Only to INBOX — 2026-05-12

## Context

Once the [[DS Brain]] goes team-wide on a unified branch ([[2026-05-12 — Unified Branch over Split for DS Brain]]), every team member's local Claude (running inside [[Cursor]] / Obsidian via MCP) has, by default, full read/write access to the whole repo. Without an explicit boundary, a local Claude could write directly into `wiki/` or `raw/`, bypassing the ingest pipeline and producing sync conflicts and unlinted / unsynthesised entries.

## Decision

Local Claude instances are constrained to **read `wiki/` for queries and write only into `INBOX/`**. Writes to `raw/` and `wiki/` from any local Claude are forbidden. The constraint is enforced primarily through a robust Skill / system-prompt boundary distributed with the brain, and is intended to be backed by a filesystem-level guard analogous to the existing `scripts/hooks/guard_immutable.py` rule for `raw/`.

## Why

The ingest pipeline (`/ingest`, `/lint`) is the only path that keeps wikilinks, frontmatter, and the synthesis layer coherent. Allowing direct writes to `wiki/` would silently break the wiki-LLM invariants the [[DS Brain]] depends on. Channeling all human contributions through `INBOX/` keeps the server-side ingest Claude (see [[2026-05-12 — Server VM as Sole Ingest Authority]]) as the single authority for shape and convention. Mirrors the existing protection model already applied to the `raw/` layer.

## Alternatives considered

- **No boundary, trust humans to invoke `/ingest`** — rejected: predictable failure mode where any local Claude opportunistically edits `wiki/` to "be helpful" or to answer a query in-place.
- **Branch-level isolation** (split repo) — rejected separately, see [[2026-05-12 — Unified Branch over Split for DS Brain]].
- **Read-only-everywhere local Claude** — rejected: would prevent the most important local use case (dropping new material into `INBOX/` for later ingest).

## Consequences

- All new material lands in `INBOX/` first, regardless of source (human drop, Claude-generated note, exported source).
- The local Claude Skill must explicitly describe the read/write surface and refuse `wiki/` / `raw/` writes.
- The `scripts/hooks/guard_immutable.py` filesystem guard should be extended to block `wiki/` writes from non-server agents, providing defence in depth beneath the prompt boundary.
- `/query` remains read-only by construction; `/ingest`, `/lint`, `/remove`, `/braindump` execute on the server only.
- Editor UX trade-off: a user who wants a quick wiki correction must drop a note into `INBOX/` rather than fixing in place.

## Open questions

- How is "the server" identified at the hook layer (env var, hostname, signed marker file)?
- Should the boundary degrade gracefully (read-only fallback) when the local Skill is missing or out of date?
- What is the audit trail for `INBOX/` writes — distinguishing Claude-emitted notes from human drops?
- Does this rule apply transitively to subagents spawned by a local Claude?
