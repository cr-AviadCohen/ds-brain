---
title: META
type: project
tags: [project, wiki]
status: active
started: 2026-05-11
systems: []
related_decisions: []
raw_path: raw/projects/Project - META/
last_updated: 2026-05-11
---

# META

> `virustotalclassifier` — research codebase that uses the consensus of ~70 AV engines from VirusTotal as its input feature space, learning higher-order classifiers ("meta models") that decide malicious / benign with calibrated confidence.

## Goal

Learn to read the panel of ~70 AV engine verdicts (stacking pattern: level-0 = AV engines, level-1 = the meta classifier) — accounting for engine bias, expertise, echoes (engines that license each other's signatures), and detection delays. Serve as a labelling and consensus tool that feeds high-quality labels into downstream pipelines (including, indirectly, NGAV's training set) and provides domain-specific wrappers for scripts, Linux ELF, and Office documents.

## Approach

Given a VirusTotal report: (1) extract per-engine verdicts (~70 binary detections plus engine-specific malware names); (2) statistically pick trusted engines as referees; (3) compute a maliciousness score via `VirusTotalAnalyzer` (clusters engines by similarity to detect echoing); (4) learn a threshold separating benign from malicious using outlier-robust statistics; (5) decide via a 3-zone rule (few detections → benign, many → malicious, middle → learned threshold on model score); (6) optional rule-based multiclass classifier over malware-name tokens and VT tags. Five subsystems: `meta/` (core), `broccoli/` (KNN over hand-crafted features via Annoy index), `olive/{black,green}` (script wrappers, binary), `ginger/` (Linux ELF binary), `snitch/` (MS Office multiclass).

## Status

active — seeded from raw 2026-05-11.

**Phoenix variant** (a.k.a. "META Phoenix") — Q2 High-priority team-effort port to [[Phoenix]]; status "waiting for engineering to start moving those" per the DS Team project tracker. Engineering contact: [[Ortal Keizman]]. Jira ENG-9969. Slack data-transfer channel: `cybereason.enterprise.slack.com/archives/C089AGMU8RW`.

## Decisions

(populated by /ingest as decisions are taken)

## Risks

(populated as identified)

## Mentions

- 2026-05-11 — [[data-science-team-knowledge]] — Phoenix variant tracked as Q2 High-priority team-effort project; engineering contact [[Ortal Keizman]]; Jira ENG-9969; waiting for engineering to start moving.

## Open questions
