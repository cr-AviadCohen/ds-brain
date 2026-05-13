---
title: OwlHub
type: project
tags: [project, wiki]
status: active
lead: [[Itamar Hershko]]
team: []
started: 2026-05-11
systems: []
related_decisions: []
raw_path: raw/projects/Itamar Project - OwlHub/
last_updated: 2026-05-11
---

# OwlHub

> Centralized orchestration platform for autonomous AI agents — management, monitoring, safety guardrails, and collaboration infrastructure for AI agent projects like VOWL, AIDRA, and OWLINT.

## Goal

Provide a unified hub where AI agents live, collaborate, and stay safe — agent management with real-time heartbeat and kill switches, LLM proxy with secret scrubbing and prompt-injection detection, response scanning (PII, exfiltration, prompt leaks), YAML-based policy engine with human-in-the-loop approval, cross-project event bus and workflow engine, and full observability (token/cost tracking, real-time WebSocket streams, dashboard).

## Approach

Four-component platform (v0.1.0): `owlhub-core` (FastAPI + SQLAlchemy + Redis backend with 70+ endpoints), `owlhub-cli` (Typer + Rich terminal interface), `owlhub-dashboard` (Streamlit + Plotly), and `owlhub-sdk` (Python + httpx, OpenAI drop-in). Redis Streams for cross-project events, multi-step workflow engine.

## Status

active — seeded from raw 2026-05-11.

## Decisions

(populated by /ingest as decisions are taken)

## Risks

(populated as identified)

## Mentions

(populated by /ingest)

## Open questions
