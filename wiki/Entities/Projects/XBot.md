---
title: XBot
type: project
tags: [project, wiki]
status: paused
started: 2026-05-11
systems: []
related_decisions: []
raw_path: raw/projects/Project - XBot/
last_updated: 2026-05-11
---

# XBot

> Cybereason internal AI chatbot ("Ask Seinfeld" / "Ask Seifeld" — older naming) with a Slack integration, originally backed by scraping NEST documentation and other Cybereason resources.

## Goal

Provide a question-answering chatbot over Cybereason's internal documentation (NEST, Confluence resources, XBot Resources GenAI Wiki).

## Approach

Web frontend at `cybereasonai.eng.cybereason.net` plus a Slack integration. Scrapes NEST and related Cybereason documentation. Codebase under `cybereason-labs/CybereasonAI` (`v1.1.0-beta`). Currently the server is down, so both the web UI and the Slack integration are non-functional. NEST itself is going through structural changes, so any reactivation would require updating the scraping code to match the new NEST layout.

## Status

paused — server is currently down; seeded from raw 2026-05-11.

## Decisions

(populated by /ingest as decisions are taken)

## Risks

- NEST documentation structure is changing; scraping code will need updates before reactivation.

## Mentions

(populated by /ingest)

## Open questions

- Should the project be reactivated or fully retired?
- Whether to retain the dual name (XBot vs Ask Seinfeld).
