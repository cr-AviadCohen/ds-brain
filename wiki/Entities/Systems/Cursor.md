---
title: Cursor
type: system
tags: [system, wiki]
owner: Anysphere (Cursor team)
vendor: Anysphere
integration_surface: [ide, mcp]
related_projects: ["[[Malop-Worthy]]", "[[OwlBot]]", "[[AI Assistant]]", "[[Assembly LLM]]", "[[MCP]]", "[[UEBA]]", "[[RCE-NG]]"]
last_updated: 2026-05-12
---

# Cursor

> Anysphere's AI-augmented IDE (VS Code fork) — the DS team's default development environment for agent / ML work and the primary MCP client for in-house tooling.

## Owner / vendor

Anysphere. Commercial SaaS (paid pro tier used by team members) with VS Code-compatible extension surface.

## Integration surface

- IDE (VS Code fork) — chat, inline edit, agent mode.
- MCP client — registers MCP servers via `.cursor/mcp.json`; auto-activation rules under `.cursor/rules/*.mdc`.
- Standard VS Code extensions and language servers.

## Data flow

Source code in / refactor + chat / agent edits out. With MCP servers attached, Cursor can call internal tools (Notion search, JIRA, internal RAG) from the editor agent loop.

## Current usage

- [[Malop-Worthy]] — explicitly adopted "Start working with Cursor for faster implementation."
- [[OwlBot]] — Cursor is a first-class client of the OwlBot MCP server (`.cursor/rules/owl-bot.mdc` triggers auto-activation).
- [[MCP]] — DS team's MCP exploration project; Cursor is the reference client.
- [[AI Assistant]], [[Assembly LLM]], [[UEBA]], [[RCE-NG]] — referenced in source-code repos / cursor-summarised artefacts as the development tool of record.

## Known issues

(none documented yet — vendor-lock and prompt-leakage concerns mentioned informally in meetings but not in raw docs)

## Related entities

- Systems: [[MCP]] (Cursor consumes MCP servers as tools).
- People: [[Aviad Cohen]], [[Itamar Hershko]] — primary advocates per Malop-Worthy and OwlBot docs.
- Projects: see Current usage.

## Open questions

- Enterprise vs individual licensing — what is the procurement story under Level Blue?
- Code / prompt egress policy — are there guardrails for sensitive Cybereason source?
- Should the team standardise on a shared `.cursor/rules` baseline across projects?
