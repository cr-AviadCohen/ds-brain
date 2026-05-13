---
title: OWLINT
type: project
tags: [project, wiki]
status: active
lead: [[Itamar Hershko]]
team: []
started: 2026-05-11
systems: ["[[Langfuse]]"]
related_decisions: []
raw_path: raw/projects/Itamar Project - OWLINT/
last_updated: 2026-05-12
---

# OWLINT

> Automated CTI pipeline that ingests threat articles and feeds, filters noise using AI, and generates production-quality YARA detection rules.

## Goal

Transform raw threat articles and IOC feeds into actionable YARA rules end-to-end: AI-powered triage to classify actionable vs noise, automated rule generation with Red Team validation, syntax verification and false-positive checking, and structured output with full metadata and source tracking.

## Approach

Five-stage pipeline (INGEST → TRIAGE → FORGE → QA → DELIVER) built on a dual-agent system (Triage Agent classifies, Forge Agent generates with red-team validation). Streamlit UI; ingests from abuse.ch feeds (MalwareBazaar, ThreatFox, URLhaus, Feodo Tracker). Python 3.9+, optional Redis (dedup) and PostgreSQL (persistence), Azure OpenAI / OpenAI LLM provider with optional Langfuse observability.

## Status

active — seeded from raw 2026-05-11.

## Decisions

(populated by /ingest as decisions are taken)

## Risks

(populated as identified)

## Mentions

(populated by /ingest)

## Open questions
