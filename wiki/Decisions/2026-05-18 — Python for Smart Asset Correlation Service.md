---
title: Python for Smart Asset Correlation Service
type: decision
tags: [decision, wiki]
date: 2026-05-18
deciders: ["[[Aviad Cohen]]", "[[Xin Tang]]"]
status: accepted
related_projects: ["[[Smart Asset Correlation]]"]
last_updated: 2026-05-18
---

# Python for Smart Asset Correlation Service — 2026-05-18

## Context

DS team owns Phase 2 / Mode 3 of [[Smart Asset Correlation]] — a scheduled async service that queries [[ClickHouse]] for raw events, applies behavioral rules + ML, and writes confidence-scored relations to PostgreSQL/TB. Language choice was open at the start of the 2026-05-18 knowledge-transfer.

## Decision

Build the service in Python.

## Why

Service profile is async + DB-bound: most wall-clock time is spent waiting on ClickHouse query responses, not on CPU-bound logic. There is no latency floor that would justify a faster compiled language. DS team is already proficient in Python and Python's ML / SQL client ecosystem is mature.

[[Xin Tang]]: *"Most of the time you is waiting to waiting the response of a database. So it's not a very high transparent or very low latency required from your language… it's fine if you are more familiar with Python."*

## Alternatives considered

- **Rust** — rejected. No latency requirement that benefits from native compilation; would slow DS-team iteration.
- **Java/Kotlin** — not seriously considered; misaligned with DS-team stack.

## Consequences

- Existing DS-team Python stack (LangGraph, async I/O, SQL clients) carries over directly.
- ML model invocation lives inside the same process — no cross-language IPC.
- If future profiling shows CPU-bound hotspots inside the rule engine, isolate via Rust extension rather than rewriting the whole service.

## Open questions

- Concurrency model — asyncio vs threadpool — to be settled once query patterns are profiled.
