---
title: IRCA Cloud
type: project
tags: [project, wiki]
status: active
lead: [[Guy Kassorla]]
team: [[Aviad Cohen]]
started: 2026-05-11
systems: []
related_decisions: []
raw_path: raw/projects/Project - IRCA Cloud/
last_updated: 2026-05-11
---

# IRCA Cloud

> Cloud-detections counterpart to IRCA — generates IRCA-style reports for cloud events sourced from Observe / XDR (AWS CloudTrail, Cisco Firewall, Microsoft Office 365, Microsoft Azure Identity).

## Goal

Produce a cloud-equivalent IR report on top of cloud telemetry. Address the unscalable raw-data volume (hundreds of thousands to millions of CloudTrail records daily) by filtering down to a small set of high-value event names (a Pareto-style 80–90%) before LLM summarisation, and produce IRCA-style reports tailored to cloud incidents.

## Approach

Security team filters raw cloud logs and creates detections for a focused vendor set (AWS CloudTrail, Cisco Firewall, MS Office 365, MS Azure Identity), truncating logs to relevant fields. Data Science consumes events in Unified Data Model (UDM) format from filtered Opal datasets, optionally adds a scoring/anomaly mechanism (timestamp-aware, sequence-based via BERT on event names; distribution / internal-vs-external features), then runs an IRCA-style report-generation pipeline (preprocess UDM events → prompt build → LLM). Initial PoC focuses on a specific scenario. Codebase under `cybereason-labs/research_notebooks` (`irca_cloud` branch).

## Status

active — seeded from raw 2026-05-11.

## Decisions

(populated by /ingest as decisions are taken)

## Risks

- No dirty cloud environment available for malicious-activity injection (unlike EDR-IRCA's MITRE dry-runs).
- Summarising summaries of CloudTrail logs is unscalable; aggressive filtering required.

## Mentions

(populated by /ingest)

## Open questions

- Best IR report format for cloud incidents.
- Final scoring/anomaly mechanism and threshold.
