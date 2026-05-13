---
title: XIS
type: system
tags: [system, wiki]
owner: Cybereason
related_projects: []
seeds:
  - raw/data_science_drive/data-science-main.md
last_updated: 2026-05-11
---

# XIS

> Phoenix-side third-party log ingestion layer — adapts external SIEM / cloud telemetry into the [[Phoenix]] schema so XDR runs over Phoenix instead of [[Chronicle]] or [[Observe]].

## Owner / vendor

Cybereason.

## Integration surface

(stub — populate from raw)

## Data flow

External SIEM / 3rd-party telemetry → XIS (or equivalent connector) → Phoenix schema → downstream Phoenix XDR processing.

## Current usage

Per the DS team's general-knowledge doc, XIS is the connector technology powering the new XDR-over-Phoenix direction.

## Known issues

(stub — design context not yet captured)

## Related entities

[[Phoenix]], [[Chronicle]], [[Observe]]

## Open questions

- Exact technology stack and protocols supported.
- Coverage matrix (which 3rd-party sources are in scope).
