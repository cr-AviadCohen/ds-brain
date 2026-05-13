---
title: BigQuery
type: system
tags: [system, wiki]
owner: Google (vendor)
vendor: Google
related_projects: ["[[CMD Classification]]", "[[Malop-Worthy]]", "[[NGAV]]", "[[META]]"]
seeds:
  - raw/projects/Project - CMD Classification/Project CMD Classification.docx.md
  - raw/projects/Project - Malop-Worthy/Project Malop-Worthy.docx.md
  - raw/projects/Project - NGAV/01 - Project Overview.md
last_updated: 2026-05-11
---

# BigQuery

> Google Cloud's serverless analytics warehouse — the team's primary store for historical event data, triage labels, correlation outputs, and the VirusTotal sample feed.

## Owner / vendor

Google Cloud (GCP).

## Integration surface

- Datasets in project `global-soc-14311f` (e.g., `hunting_amer.triage_result`, `hunting_apac.triage_result`, `hunting_emea.triage_result`, `xdr_malop_*.rce_triage_result`).
- Datasets in regional projects (`dc-as-ne1-1-stack-prod-2d`, `dc-us-e1-1-stack-prod-e3`, `dc-eu-w1-1-stack-prod-70`, `dc-eu-w3-1-stack-prod-be`) with `dc_rce_dataset.correlation_output` (partitioned daily, 365-day retention).
- VirusTotal BigQuery feed for NGAV/META training samples.

## Data flow

Elastic / Cybereason data extracted into BigQuery (via Raz Isaac for CMD Classification). Triage tables hold human-labelled Malops by region. Correlation outputs hold XDR detection events partitioned by day. Apac tables are co-located in `asia-northeast1`; US and EU tables are split across `us-east1`, `europe-west1`, and `europe-west3`.

## Current usage

- [[CMD Classification]]: customer command-line samples (~95K records / day sample).
- [[Malop-Worthy]]: `rce_triage_result` (labels) + `correlation_output` (events).
- [[NGAV]]: VirusTotal BigQuery feed (labelled PE samples).
- [[META]]: VirusTotal feed rows feeding the meta classifier.

## Known issues

- Cross-region data — apac is co-located, US and EU are split (multi-region queries may require care).
- `correlation_output` has 365-day retention.

## Related entities

[[VirusTotal]], [[CMD Classification]], [[Malop-Worthy]], [[NGAV]], [[META]]

## Open questions
