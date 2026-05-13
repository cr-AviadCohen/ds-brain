---
title: Incident Investigation (for Fusion 2)
type: project
tags: [project, wiki]
status: active
started: 2026-05-11
systems: []
related_decisions: []
related_teams: ["[[Fusion 2 Team]]"]
raw_path: raw/projects/Project - Incident Investigation (for Fusion 2)/
last_updated: 2026-05-13
---

# Incident Investigation (for Fusion 2)

> Integration between Fusion 2 (central analyst platform) and Cybereason/LevelBlue AI-driven security analysis components (IRCA, AIDRA, AI Assistant, RCE-NG) to deliver automated enrichment, correlation, and reasoning before analyst review.

## Goal

Position Fusion 2 as the central analyst platform where alerts originate in external EDR/SIEM systems (Defender, Cortex), incidents are ingested as high-fidelity alerts, and an AI pre-analysis phase suggests false-positive resolutions, recommends next response actions, and supplies supporting evidence — so analysts focus on validation rather than navigation.

## Approach

Six-step workflow: alert ingestion into Fusion 2 → fetch incident details via vendor APIs → enrichment (IOCs, threat intel, historical data) → automated AI analysis → AI-generated initial verdict → analyst review and final decision. AI capabilities integrated as platform-agnostic components: IRCA (incident analysis), AI-DRA (script/PE analysis), AI Assistant (multi-agent investigation), RCE-NG (multi-vendor correlation). AI output structured as confidence score + verdict (TP/FP/benign/unknown/needs-review) + reasoning. Analyst feedback returned via API with at least one human validation step before feedback is applied. Open issues: missing entities/IOCs in vendor alerts (Sentinel, Defender, Cortex) significantly limit AI verdict accuracy; need structured schemas (Incident, Alert, Evidence) and additional enrichment APIs.

## Status

active — seeded from raw 2026-05-11.

## Decisions

(populated by /ingest as decisions are taken)

## Risks

- Missing entities/IOCs in upstream vendor alerts limit AI analysis quality.

## Mentions

- 2026-05-11 — [[data-science-team-knowledge]] — Q2 High/Medium priority; Fusion 2 + Phoenix platforms; status TBD; engineering contacts [[Ortal Keizman]], [[Hila Karmi]], [[Atchuta Meka]] (`atchuta.meka@levelblue.com`); owner [[Guy Kassorla]]. HLA: `drive.google.com/file/d/1uvy1MlMDsXYF-4zuWSvYqmxHCJ36VaCS`; design doc: `docs.google.com/document/d/1Wcr1O0dyph_6jOBnNU0o4q845vDKdGuBrnZ7HZBUaHE`.

## Open questions

- Feedback API design.
- Sunrise DB data schemas.
- AI Notes structure detail.
- Data availability and enrichment completeness from vendors.
