---
title: UEBA (USMA)
type: project
tags: [project, wiki]
status: archived
lead: ["[[Jose Manuel Martin Rodriguez]]"]
team: []
started: ~2022
target_ship: n/a
systems: ["[[USMA]]"]
related_decisions: []
related_concepts: ["[[UEBA (concept)]]"]
raw_path: raw/meetings/meeting_2026.05.12_aviad_jose.txt
last_updated: 2026-05-12
---

# UEBA (USMA)

> Historical Level Blue / USMA Unsupervised UBA — anomalous-login + exfiltration + lateral-movement detection — abandoned ~2 yrs ago due to staff turnover. Level Blue's prior implementation of [[UEBA (concept)]], sibling to Cybereason's stalled [[UEBA]] POC.

## Goal

Detect anomalous user behaviour in [[USMA]] telemetry: anomalous logins, exfiltration patterns, lateral movement. Unsupervised ML approach, deployed inside USMA's correlation/detection stack alongside hand-authored correlation rules and [[Suricata Signatures]].

## Approach

Per [[Jose Manuel Martin Rodriguez]]: unsupervised ML over the USMA event stream to model per-user behavioural baselines. Built directly into USMA so detections surfaced through the existing Level Blue SOC analyst workflow.

## Status

archived (~2024). Project was completely abandoned roughly two years ago after severe DS-team turnover — first the AT&T data-science team was lost, then subsequently-hired DS staff left. The abandoned system still emits noisy alarms in production today and generates customer complaints. Active rebuild interest captured in [[Rebuild UEBA in Phoenix XDR]].

## Decisions

(none documented in transcript)

## Risks

- **Same turnover risk that killed v1.** Any relaunch faces the same staff-stability problem that ended the original — Level Blue engineering bandwidth is currently strictly focused on maintaining USMA until the [[Phoenix]] migration completes.
- **Platform sunset.** USMA itself is on a migration path to [[Phoenix]]; rebuilding inside USMA repeats the abandonment risk on a deprecating platform.

## Mentions

- 2026-05-12 — [[2026-05-12 — Aviad and Jose intro]] — Jose described the history of the abandoned USMA UBA; Aviad proposed a unified Phoenix XDR rebuild path covering both this project and Cybereason's stalled [[UEBA]] POC.

## Open questions

- Is the abandoned codebase still in source control? Where?
- Can the original training data be recovered as input to a rebuild?
- Who owns customer complaints today regarding the noisy abandoned alarms still in production?
