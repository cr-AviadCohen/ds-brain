---
title: Pixel Agents
type: project
tags: [project, wiki]
status: active
lead: [[Itamar Hershko]]
team: []
started: 2026-05-11
systems: []
related_decisions: []
raw_path: raw/projects/Itamar Project - Pixel Agents/
last_updated: 2026-05-11
---

# Pixel Agents

> Autonomous multi-agent framework that replaces single-agent Claude Code with a council of six specialized AI agents that deliberate, challenge each other, and reach consensus before executing.

## Goal

Provide a richer collaborative coding agent experience where each of six agents (Scout, Architect, Critic, Implementer, Tester, Debugger) has distinct expertise and tools. Includes a real-time pixel-art office visualization showing agents working and communicating.

## Approach

Node.js Express server on port 3333 (proxied via nginx at `/_proxy/3333/`). Each agent has scoped tools (Scout: Read/Glob/Grep search-only; Implementer: also Write/Edit; etc.). The full council pipeline runs Scout-first exploration, parallel Architect/Critic deliberation, then Implementer execution with optional `SPLIT_TASKS` worker clones. Execution modes auto-route based on NL analysis (Solo, Direct, Team, Debug, Full Council).

## Status

active — seeded from raw 2026-05-11.

## Decisions

(populated by /ingest as decisions are taken)

## Risks

(populated as identified)

## Mentions

(populated by /ingest)

## Open questions
