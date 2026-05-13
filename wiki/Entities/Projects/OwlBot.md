---
title: OwlBot
type: project
tags: [project, wiki]
status: active
lead: [[Itamar Hershko]]
team: []
started: 2026-05-11
systems: []
related_decisions: []
raw_path: raw/projects/Itamar Project - OwlBot/
last_updated: 2026-05-11
---

# OwlBot

> MCP server that transforms Notion into an AI-friendly knowledge base for LevelBlue, bridging IDE environments (Cursor, Claude Code) with the Notion workspace.

## Goal

Enable AI agents and developers to seamlessly search, query, synthesize, and manage knowledge across the LevelBlue Notion workspace — search & discover, fetch & read, synthesize & answer with citations, query databases in natural language, manage tasks, and create/document via slash commands.

## Approach

Node.js 18+ / TypeScript 6.0.2 stdio-transport MCP server (~1,900 lines) exposing 6 MCP tools, 2 dynamic resources, 3 system prompts, and 10 slash commands. Integrates Cursor IDE and Claude Code via MCP and the Notion API (@modelcontextprotocol/sdk v1.29.0, @notionhq/client v5.16.0). Supports 25+ Notion block types.

## Status

active — seeded from raw 2026-05-11.

## Decisions

(populated by /ingest as decisions are taken)

## Risks

(populated as identified)

## Mentions

(populated by /ingest)

## Open questions
