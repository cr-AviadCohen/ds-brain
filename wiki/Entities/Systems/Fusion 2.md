---
title: Fusion 2
type: system
tags: [system, wiki]
owner: Level Blue
vendor: Level Blue
related_projects: ["[[Incident Investigation (for Fusion 2)]]"]
seeds:
  - raw/data_science_drive/data-science-projects.md
last_updated: 2026-05-11
---

# Fusion 2

> Level Blue's central analyst platform — destination for cross-vendor incidents (Defender, Cortex, Sentinel, Phoenix, …) and the integration target for the Incident Investigation project.

## Owner / vendor

Level Blue.

## Integration surface

(stub — populate from Incident Investigation design docs)

## Data flow

External EDR/SIEM (Defender, Cortex, Sentinel, …) → Fusion 2 → AI-assisted pre-analysis ([[IRCA]], [[AIDRA]], [[AI Assistant]], [[RCE-NG]]) → analyst review.

## Current usage

Integration target for [[Incident Investigation (for Fusion 2)]] — the Q2 High/Medium-priority DS workstream that wires Cybereason/LevelBlue AI components into the Fusion 2 analyst flow.

## Known issues

- Missing entities / IOCs in upstream vendor alerts (Sentinel, Defender, Cortex) limit AI verdict accuracy.

## Related entities

[[Incident Investigation (for Fusion 2)]], [[Phoenix]]

## Open questions

- Final Incident / Alert / Evidence schemas.
- Feedback API design between Fusion 2 and Cybereason AI components.
