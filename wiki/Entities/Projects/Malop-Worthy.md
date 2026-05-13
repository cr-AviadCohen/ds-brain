---
title: Malop-Worthy
type: project
tags: [project, wiki]
status: active
started: 2026-05-11
systems: []
related_decisions: []
raw_path: raw/projects/Project - Malop-Worthy/
last_updated: 2026-05-11
---

# Malop-Worthy

> Module in the RCE-NG pipeline that classifies a given correlation (group of correlated events) as "interesting and malicious enough to become a Malop" — or not.

## Goal

Reduce false positives at the Malop-decision gate without missing real malicious correlations. Initial target: FPR ≤ 15% with the highest possible TPR×TNR, evaluated via 10-fold cross-validation. Operate at the Malop level (groups of correlated events), not individual events.

## Approach

Pipeline: feature extraction → classification → results. Features bootstrapped from the 11 existing Malop-Ready rules whose fields persist into Phoenix's new detection schema, augmented with simulated data and additional fields identified with security researchers. Source data lives in BigQuery: `rce_triage_result` (Malops with detection events and human-analyst classification, by region: apac/amer/emea) and `correlation_output` (XDR events, partitioned daily, 365-day retention, multiple regions). LLM (OpenAI gpt-o4) used for both classification baseline and feature suggestion; future work includes LSTM for sequential treatment. Codebase under `cybereason-labs/research_notebooks` (`malop_decision_guy_3_9_25/malop_worthy`).

## Status

active — seeded from raw 2026-05-11.

## Decisions

(populated by /ingest as decisions are taken)

## Risks

- Current labels for "Malop Worthy" come only from correlations that already passed the existing rules — large untagged regions in the data.
- Phoenix schema differences require remapping.

## Mentions

(populated by /ingest)

## Open questions

- How to label correlations that did not pass current Malop-Worthy (manual analyst tagging? LLM-assisted?).
- Adapt the solution to Phoenix's new schema.
