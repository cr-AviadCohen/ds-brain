---
title: UEBA
type: concept
tags: [concept, wiki]
domain: ml
related_projects: ["[[UEBA]]", "[[UEBA (USMA)]]"]
related_systems: ["[[USMA]]", "[[Phoenix]]"]
last_updated: 2026-05-12
---

# UEBA

> User & Entity Behavior Analytics — detect anomalies in user/entity activity (logins, exfiltration, lateral movement) using unsupervised ML over time-series telemetry.

## What it is

A class of detection technique that profiles per-user / per-entity behaviour over time, learns a baseline of "normal" via unsupervised ML over event-stream telemetry, then flags time-windows where the entity deviates from its own (and its peers') baseline. Canonical scenarios: anomalous logins, data exfiltration, lateral movement.

## Why we care

The DS team has built UEBA twice across sibling orgs — once at Level Blue / USMA (Jose's work) and once at Cybereason (Guy Kapach's POC). Both attempts are currently stalled due to organisational turnover. The pattern recurs, the underlying problem is unsolved in either codebase, and any future XDR detection roadmap repeatedly converges on "we need UEBA".

## Manifestations

- ~2022 — [[UEBA (USMA)]] — [[Jose Manuel Martin Rodriguez]] built unsupervised UBA at Level Blue / USMA; abandoned ~2 yrs ago due to AT&T DS team turnover.
- 2026-05-11 — [[UEBA]] — Cybereason project, lead [[Guy Kapach]], POC not completed, owner lost in layoffs.
- 2026-05-12 — [[Rebuild UEBA in Phoenix XDR]] — Aviad-proposed hypothesis to consolidate both into [[Phoenix]] XDR.

## Tensions

- **Build vs. buy.** Jose floated SentinelOne / IBM UEBA as viable buys; two abandoned in-house attempts at sister orgs suggest UEBA may be a poor in-house bet — or, equivalently, a recurring DS bottleneck worth solving deliberately once with platform-grade investment.
- **Same problem, two codebases.** Cybereason's `ueba_python` (Guy's notebooks) and USMA's abandoned UBA component are independent rebuilds of the same capability — neither survives reorg events; the [[Rebuild UEBA in Phoenix XDR]] hypothesis tries to break the cycle.

## Open questions

- Is in-house UEBA structurally fragile (kills itself on every reorg), or have the two failures been incidental (specific layoffs)?
- Does Phoenix XDR's centralised event surface meaningfully reduce per-tenant UEBA complexity vs. the USMA / Cybereason-Core split that the prior attempts faced?
- What is the minimum entity-resolution quality ([[Identity Correlation]]) needed before per-user baselines become statistically meaningful?
