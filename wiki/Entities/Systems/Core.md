---
title: Core
type: system
tags: [system, wiki]
owner: Cybereason
related_projects: []
seeds:
  - raw/data_science_drive/data-science-main.md
  - raw/cybereason/core/
last_updated: 2026-05-11
---

# Core

> Cybereason's legacy EDR backend (the platform that predates Phoenix), built around an in-memory graph database (Transparency) and an orchestration/UI layer (Perspective).

## Owner / vendor

Cybereason — legacy platform, currently in production while Phoenix is rolled out.

## Integration surface

- Sensor on endpoint sends events.
- Detection engines run on incoming data: VFP (Variant File Protection), VPP (Variant Payload Prevention), BEP (Behavioral Execution Prevention), PRP (Predictive Ransomware Protection), NGAV, BDP (Behavioral Document Protection), BDP-AI, Fileless (PowerShell, .NET, VBScript, JavaScript), Anti-Ransomware canaries (legacy), BitDefender AV engine.
- Backend exposes UI and API via Perspective.

## Data flow

Sensor → graph events in Transparency (held in RAM, expensive) → Perspective manages all Transparency instances and serves UI/API.

## Current usage

Production EDR backend. Will be superseded by [[Phoenix]] once migration is complete. Note: AIAV (new sensor, event-based instead of graph-based) was not deployed because it doesn't support migration — migration to AIAV may become possible after Phoenix is deployed.

## Known issues

- Transparency holds the entire data set in RAM — high cost.
- Graph-based design limits scaling vs Phoenix's event-based, multi-tenant model.

## Related entities

[[Phoenix]] (successor), [[MLAV]], [[NGAV]] (detection engines that ship with the sensor).

## Open questions

- Timeline for full retirement.
