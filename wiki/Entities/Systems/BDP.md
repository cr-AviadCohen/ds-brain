---
title: BDP
type: system
tags: [system, wiki]
owner: Cybereason
vendor: Cybereason
integration_surface: [endpoint-sensor, ngav-module]
related_projects: ["[[MLAV]]"]
last_updated: 2026-05-12
---

# BDP

> Behavioral Document Protection — Cybereason's YARA-signature-based detection engine for malicious Office documents (Word / Excel / PowerPoint). Now mostly superseded by BDP-AI under [[NGAV]].

## Owner / vendor

Cybereason Core team. Embedded inside the Cybereason platform; ships via the endpoint sensor as part of [[NGAV]].

## Integration surface

- Endpoint sensor — rule-based detection layer that inspects Office documents.
- Embedded NGAV module — BDP rules are consumed by the broader NGAV decision stack; BDP-AI ML model augments the legacy rules.

## Data flow

Office document on endpoint → BDP rule engine (YARA signatures) → verdict → NGAV decision → block / allow / report. BDP-AI extends this path by using the legacy BDP rule-based logic as feature input to an ML classifier.

## Current usage

- Production component of Cybereason platform (per `raw/data_science_drive/data-science-projects.md` — "BDP — In Production — CR Core").
- BDP-AI: POC completed, agnostic (CR Core) — per same source.
- Referenced from [[MLAV]] project documentation and [[AI Assistant]] RAG benchmark fixtures.

## Known issues

- Legacy BDP relied on a single strict signature; any document change altered the signature, making it hard to capture behavioural intent. This drove the move to BDP-AI.
- BDP itself is "mostly obsolete" per the DS team's main internal doc — surviving primarily as a feature input to BDP-AI.

## Related entities

- Systems: [[NGAV]] is mis-tagged as a Project today — BDP lives under NGAV's umbrella; [[Core]] is the platform host.
- Projects: [[MLAV]] (referenced alongside in DS Drive docs).

## Open questions

- From which sensor version is BDP-AI shipped to customers?
- Concrete advantage of BDP-AI vs. BDP (lift in detection rate, FPR delta)?
- How is the BDP-AI model trained and refreshed in production?
- Should BDP and BDP-AI be split into two System pages once BDP-AI has more documented surface?
