---
title: UEBA
type: project
tags: [project, wiki]
status: active
lead: [[Guy Kapach]]
team: []
started: 2026-05-11
systems: []
related_decisions: []
related_concepts: ["[[UEBA (concept)]]"]
related_ideas: ["[[Rebuild UEBA in Phoenix XDR]]"]
raw_path: raw/projects/Project - UEBA/
last_updated: 2026-05-12
---

# UEBA

> Cybereason UEBA — User & Entity Behavioral Analytics — detect anomalies in user/entity activity over XDR/[[Observe]] data using behavioural-baseline models. POC not completed under owner [[Guy Kapach]], who was lost in layoffs.

> See also: [[UEBA (USMA)]] — Level Blue / USMA sibling project (abandoned ~2024). [[UEBA (concept)]] — the abstract concept both projects implement.

Cybereason implementation of [[UEBA (concept)]].

## Goal

Train per-user baseline models on multi-vendor XDR telemetry (initially Fortinet FortiGate Firewall data via Observe), then detect anomalies in future time-windows. Sanity checks: features should distinguish between users, cluster similar users together, and surface within-user anomalies over time. Target architecture supports event-wise anomaly scoring plus time-range-wise anomaly detection (HBOS over per-feature histograms, with fit-on-week / predict-on-hour cadence).

## Approach

Pipeline implemented as classes: Feature Extraction → Dataset Creation → Anomaly Detection → Visualisation & Comparison (heatmaps, histograms). Data sources: Observe (APAC/EU/US). Features include distributions of feature values over time-ranges; explored event-rate metrics per user, internal-vs-external events, and Windows-events frequency per user. Code translated from legacy Empow UEBA codebase (`Cybereason-Empow/main/sst/empow/ueba`) into Python under `cybereason-labs/data-science` (`ueba/ueba_python`). Tracked under Jira ENG-3925.

## Status

active — seeded from raw 2026-05-11.

## Decisions

(populated by /ingest as decisions are taken)

## Risks

- Lots of users and high event rate per minute — AD model must be fast.
- Feasibility-in-Observe cost question for some feature extractions.

## Mentions

- 2026-05-11 — [[data-science-team-knowledge]] — POC not completed under owner [[Guy Kapach]]; Q2 Low priority; Phoenix platform target; Jira ENG-9972. Guy's notebooks + code remain as the research artefact.
- 2026-05-12 — [[2026-05-12 — Aviad and Jose intro]] — Cybereason UEBA POC has no active owner after [[Guy Kapach]] was lost in layoffs; Level Blue's parallel UBA component on [[USMA]] was abandoned ~2 yrs ago; rebuild-in-Phoenix vs. buy-from-SentinelOne/IBM trade-off captured in [[Rebuild UEBA in Phoenix XDR]].

## Tensions

- **Ownership crisis.** Listed `lead: [[Guy Kapach]]` but Guy was lost in recent layoffs — no active owner today. Any rebuild depends on either reassigning the POC to another DS engineer or co-leading with [[Jose Manuel Martin Rodriguez]] (who has the parallel USMA UBA history).
- **Phoenix-platform dependency.** Aviad's proposed rebuild path runs inside [[Phoenix]] XDR, but Phoenix itself is "still a long way from being fully functional" per [[2026-05-12 — Aviad and Jose intro]] — UEBA is gated on XDR maturity it cannot influence.
- **Build vs. buy.** Jose floated SentinelOne / IBM UEBA as a viable buy alternative; rebuild must beat them on both cost and detection quality — see [[Rebuild UEBA in Phoenix XDR]].

## Open questions

- What is UEBA vs general Anomaly Detection in our context?
- Vendor events in Observe — regular behavioural events or trigger/anomaly events?
- Are the rate-metric / sismograph-style approaches cost-feasible in Observe?
