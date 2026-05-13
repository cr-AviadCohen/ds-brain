---
title: Aviad and Guy DS Brain architecture meeting summary
type: source
tags: [source, wiki, source_type/meeting-summary]
authors: ["[[Aviad Cohen]]", "[[Guy Kassorla]]"]
year: 2026
raw_path: raw/meetings/meeting_summary_2026.05.12_aviad_guy_ds_brain.md
last_updated: 2026-05-12
---

# Aviad and Guy DS Brain architecture meeting summary

> LLM-generated meeting summary (not raw transcript) covering [[Aviad Cohen]] ↔ [[Guy Kassorla]] design session on transitioning the [[DS Brain]] from Aviad's local laptop instance to a shared team-wide system.

## Summary

- **Current state.** [[DS Brain]] runs locally on Aviad's box. Single git repo, three layers: raw + wiki (Obsidian markdown w/ YAML frontmatter + wikilinks) + schema (`.claude/`, `CLAUDE.md`). INBOX/ holds incoming material. Claude `/ingest`, `/query`, `/lint` commands automate processing.
- **Goal.** Make the brain global so [[Inbar Dekel]], [[Itamar Hershko]], [[Guy Kassorla]], and Aviad can all query it — e.g. someone working on [[Martin News Chatbot]] auto-gets full company + Jose context without prompting.
- **Server VM.** Shared Ubuntu VM hosts the ingest Claude instance. Pulls git every few minutes, processes INBOX/, runs daily `/lint`. Sole authority for moving material from INBOX/ → raw/ → wiki/.
- **Local clients.** Each team member runs Obsidian + MCP + local Claude. Read-only on wiki/; write-only on INBOX/. Cannot push processed wiki content directly (would cause sync conflicts).
- **Unified branch (Aviad conceded).** Aviad initially proposed split branches (server holds full repo; clients clone restricted branch hiding `.claude/` and schema). Guy argued unified is simpler. Live test: Aviad queried Claude on git's native folder-subset sync support — Claude confirmed not supported without `git subtree` scripts. Aviad agreed. Safety now enforced via a robust local Claude Skill (system prompt) defining boundaries, not via repo structure.
- **Aside: Martin News collaborators.** [[Jose Manuel Martin Rodriguez]]'s team works in AWS workspaces with **no git** — ships code via ZIP downloads. Flagged as version-control / collaboration risk for the [[Martin News Chatbot]] productionisation.
- **Next.** Pair in office to build out, gated on Aviad's upcoming presentation + meeting with [[Inbar Dekel]]. Aviad explicitly thanked Guy for the pushback ("constructive pushback is the best way to refine complex architectural designs").

## Why we care

First documented architectural design for the [[DS Brain]] as a team-wide system. Defines the security boundary (local = read wiki / write INBOX; server VM = sole ingest authority) that subsequent client-Claude Skill design must enforce. Confirms the existing `unified` git branch is the canonical strategy.

## Cited from

(Append-only. Wikilink per citing page.)

- [[DS Brain]]
- [[2026-05-12 — Aviad and Guy DS Brain architecture]]
- [[2026-05-12 — Unified Branch over Split for DS Brain]]
- [[2026-05-12 — Local Claude Write-Only to INBOX]]
- [[2026-05-12 — Server VM as Sole Ingest Authority]]
- [[Martin News Chatbot]]

## Open questions

- Concrete Skill / system-prompt that enforces local Claude's read-wiki / write-INBOX boundary — design TBD.
- Server VM provisioning (host, ownership, secrets management, git credentials) — not yet scoped.
- Conflict-resolution policy when two team members enqueue overlapping material into INBOX/ before server processes it.
- Disaster recovery if VM-side Claude pushes a corrupt commit to `unified` — rollback procedure TBD.

#source #ds-brain #infrastructure
