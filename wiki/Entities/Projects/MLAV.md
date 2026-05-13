---
title: MLAV
type: project
tags: [project, wiki]
status: active
started: 2026-05-11
systems: []
related_decisions: []
raw_path: raw/projects/Project - MLAV/
last_updated: 2026-05-11
---

# MLAV

> Malware classifier (LightGBM) for PE & DLL files (managed & unmanaged) used by the Cybereason sensor anti-virus on client endpoints. Unlike NGAV, MLAV does not depend on BitDefender — it is designed to detect known hacking tools and is trained on them directly.

## Goal

Provide an on-endpoint ML detector that classifies PE & DLL files (managed and unmanaged .NET) as benign/malicious based on STool-extracted metadata plus feature engineering (one-hot encoding, etc.). When the classifier doesn't catch known hacking tools well, add them to a blocklist.

## Approach

Static-analysis features extracted via STool metadata extractor; full training pipeline orchestrated by a Jenkins job (`mlav-model-generator`, ~20-hour run). Codebase under `cybereason-labs/data-science` (`mlav_14_5_25` branch). Adjacent / complementary engines covered in the same write-up: NGAV (second layer after BitDefender, ~125–311 features per file type, trained on BitDefender-benign labelled via Broccoli), and BDP-AI (Behavioral Document Protection — ML detector with feature-based UID for allowlisting, caching, and dedup; combines legacy YARA-style BDP rules with an ML classifier).

## Status

active — seeded from raw 2026-05-11.

## Decisions

(populated by /ingest as decisions are taken)

## Risks

- Concept drift — model performance degrades over time without retraining.
- False positives require careful threshold calibration.

## Mentions

(populated by /ingest)

## Open questions

- From which sensor version is BDP-AI available?
- Advantages of BDP-AI over legacy BDP.
- Training/update cadence for BDP-AI.
