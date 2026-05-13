---
title: Karpathy — LLM Wiki Gist
type: source
created: 2026-05-05
updated: 2026-05-05
tags: [source, wiki, karpathy, llm-wiki, second-brain]
last_updated: 2026-05-11
salience: 5
source: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
---

# Karpathy — LLM Wiki Gist

## Summary

The canonical specification for this vault. Andrej Karpathy proposes a three-layer system in which an LLM agent maintains a persistent, compounding markdown wiki on top of immutable raw inputs, governed by a human-owned schema document.

## Three layers

1. **Raw sources** — immutable documents (articles, papers, images). Never rewritten.
2. **The wiki** — LLM-generated markdown files that the AI maintains and rewrites as understanding evolves.
3. **The schema** — configuration document(s) (e.g. `CLAUDE.md`) defining wiki structure, conventions, and workflows.

## Central insight

> "The wiki is a persistent, compounding artefact" — rather than re-deriving context from raw sources on each query, the LLM builds and maintains a structured knowledge base that grows richer over time.

## Three operations

- **Ingest** — drop a source → LLM reads → writes summary pages, updates entity / concept pages, maintains cross-references.
- **Query** — ask questions against wiki pages (not raw documents). LLM synthesises answers with citations. Good answers become new wiki pages.
- **Lint** — periodic health checks for contradictions, stale claims, orphaned pages, broken links.

## Special coordination files

- `INDEX.md` — content catalogue with links, summaries, metadata. Updated on every ingest.
- `Log/` log file — append-only chronological record of ingests, queries, lint passes with consistent prefixes for parseability. (In this vault: `Log/wiki-ops.md` for ops, `Log/pulse.md` for sessions.)

## Workflow

> "I have the LLM agent open on one side and Obsidian open on the other. The LLM makes edits based on our conversation."

The agent writes markdown files; the user browses in real-time.

## No prescriptive constraints

Karpathy explicitly notes the pattern is "intentionally abstract." Directory structure, naming conventions, page formats, and tooling depend on domain and preferences. The pattern is modular and composable.

## How this vault implements it

- Raw layer: `raw/` (Cybereason KB, projects, people, meetings, LevelBlue, DS Drive) + `INBOX/`.
- Wiki layer: `Projects/`, `People/`, `Meetings/`, `Decisions/`, `Roadmaps/`, `Research/`, `Ideas/`, `Connections/`, `Memories/`, `Syntheses/`, `Sources/`, `🔥 Hot Notes/`, `🗺️ Maps/`, `📦 Archive/`, `Log/`.
- Schema layer: `CLAUDE.md`, `INDEX.md`, `folder_tree.md`, `.claude/commands/`.
- Operations: `/wiki-ingest`, `/braindump`, `/url-dump`, `/process-inbox`, `/compile`, `/pulse`, `/lint-wiki`, `/brain-delete`, dispatcher `/brain`.

## Related notes

- `🔥 Hot Notes/Brain Architecture.md`
- `folder_tree.md`
- `CLAUDE.md`

#source #karpathy #schema
