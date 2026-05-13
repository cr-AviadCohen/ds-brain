---
title: RCE-NG
type: project
tags: [project, wiki]
status: active
lead: [[Guy Kassorla]]
team: [[Aviad Cohen]]
started: 2026-05-11
systems: []
related_decisions: []
raw_path: raw/projects/Project - RCE-NG/
last_updated: 2026-05-11
---

# RCE-NG

> Risk Chain Engine — Next Generation. Engine that correlates detection events on XDR into an attack narrative with detailed LLM-generated explanation (currently GPT-4o), replacing the problematic existing RCE.

## Goal

Connect security alerts from multiple vendors (XDR) and correlate them into a single comprehensive attack story ("Malop") with explanations. Pivot the architecture to Phoenix as the input source (instead of the existing XDR EDR), align with Phoenix's detection scheme, and produce a complete cost model for production deployment.

## Approach

Multi-stage pipeline. Stage 3 (correlation) consumes Phoenix detections (Phoenix scheme) and outputs Phoenix-detection-shaped objects; benign data is filtered out before reaching RCE for cost and accuracy reasons. Convert prompts to COSTAR style. Cost evaluation includes: total events/detections per month, integrations (vendors) per customer, LLM query volume in Phase #3, average correlation-group size, and maximum input-token limits. Adjacent module: Malop-Worthy (separate project) provides the ML classifier that decides whether a correlation graduates to a Malop. Codebase under `cybereason-labs/data-science` (`rce-ng` branch).

## Status

active — seeded from raw 2026-05-11.

## Decisions

(populated by /ingest as decisions are taken)

## Risks

- Existing labels for Malop-Worthy training are partial and use the old schema; depends on real Phoenix data flow to bootstrap.
- Architecture pivot from old XDR to Phoenix requires alignment with Phoenix engineering (Ortal Keizman, Tonny Pham, Tal Stavi).

## Mentions

(populated by /ingest)

## Open questions

- Final Phoenix scheme for Stage 3 input/output (detection vs benign separation).
- Comprehensive cost model for the proposed solution.
