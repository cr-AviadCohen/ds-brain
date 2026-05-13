---
title: Chronicle
type: system
tags: [system, wiki]
owner: Google (vendor)
vendor: Google
related_projects: []
seeds:
  - raw/data_science_drive/data-science-main.md
last_updated: 2026-05-11
---

# Chronicle

> Google Chronicle on GCP — one of Cybereason's two current XDR data-lake backends. Full feature suite (including IDM — Identity Management), expensive.

## Owner / vendor

Google Cloud.

## Integration surface

(stub — populate from raw)

## Data flow

External telemetry → Chronicle on GCP → analyst tooling.

## Current usage

Current XDR backend. Per the DS team's general-knowledge doc, the strategic direction is XDR over [[Phoenix]] via [[XIS]] — Chronicle expected to be deprioritised over time.

## Known issues

- Cost (full feature suite including IDM).

## Related entities

[[Observe]], [[Phoenix]], [[XIS]]

## Open questions

- Sunset timeline once Phoenix-native XDR is generally available.
