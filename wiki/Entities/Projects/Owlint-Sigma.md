---
title: Owlint-Sigma
type: project
tags: [project, wiki]
status: active
lead: [[Itamar Hershko]]
team: []
started: 2026-05-11
systems: ["[[Langfuse]]", "[[LangGraph]]", "[[Tipper]]"]
related_decisions: ["[[2026-05-07 — Sigma as Common Detection Language]]", "[[2026-05-07 — Deterministic Sigma HQ Translation with LLM Fallback]]"]
related_projects: ["[[Detection Engineering Hub]]"]
raw_path: raw/projects/Itamar Project - Owlint-Sigma/
last_updated: 2026-05-13
---

# Owlint-Sigma

> AI-powered Sigma detection rule generation and bidirectional SIEM translation platform that transforms DFIR reports, threat intel, and SIEM queries into production-ready Sigma rules across six SIEM platforms.

## Goal

Solve three detection engineering challenges: (1) convert DFIR reports and IOC lists into validated multi-logsource Sigma rules using tiered LLM generation with self-healing validation; (2) bidirectional Sigma ↔ SIEM translation across Splunk, Microsoft Sentinel, Elastic, CrowdStrike Falcon, Google Chronicle, IBM QRadar; (3) semantic deduplication and persistent rule storage to avoid duplicate rules.

## Approach

Owlint-Sigma v5.0 (Python 3.10+) with three processing tracks (Threat Intel → Sigma → SIEM, Sigma → SIEM, SIEM → Sigma), per-platform translation modules inheriting from BasePlatform (syntax patterns, field mapping, validation, repair loops), red-team review, and ChromaDB vector embeddings for the detection library.

## Status

active — seeded from raw 2026-05-11.

## Decisions

- [[2026-05-07 — Sigma as Common Detection Language]] — Sigma is the common detection language across Level Blue SIEMs (Fusion, USM Anywhere, Phoenix, Core, Alert Logic).
- [[2026-05-07 — Deterministic Sigma HQ Translation with LLM Fallback]] — primary translation via Sigma HQ; LLM with RAG only fills gaps and validates.

## Risks

(populated as identified)

## Tipper collaboration

Per the DS Team project tracker, an "Owlint (Tipper Collaboration)" track is Q2 High priority — owned by [[Itamar Hershko]], status "to be deployed for Tipper" — folded into this broader Owlint-Sigma project.

## Mentions

- 2026-05-11 — [[data-science-team-knowledge]] — Tipper Collaboration track: Q2 High priority; owner [[Itamar Hershko]]; status "to be deployed for Tipper".

## Open questions
