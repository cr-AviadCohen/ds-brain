---
title: XDR Correlation for Phoenix
type: project
tags: [project, wiki]
status: proposed
lead: [[Guy Kassorla]]
team: []
started: 2026-05-11
systems: ["[[Phoenix]]"]
related_decisions: []
raw_path: raw/data_science_drive/data-science-projects.md
last_updated: 2026-05-11
---

# XDR Correlation for Phoenix

> Bring [[RCE-NG]]-style XDR correlation onto the [[Phoenix]] platform — correlate detection events into attack stories on the new schema. Q2 High priority. Engineering contacts: [[Ortal Keizman]], [[Tonny Pham]].

## Goal

Port the XDR correlation pipeline (today running over [[Observe]] / [[Chronicle]]) onto Phoenix — correlating detection events into attack stories on Phoenix's new schema, leveraging Phoenix's Postgres-backed correlation services instead of Core's graph DB.

## Approach

To be defined. Reference material captured from the DS Team project tracker:

- Slack channel: `cybereason.slack.com/archives/C0A00FYDL7N/p1777282345907659`
- Phoenix Confluence page: `cybereason.atlassian.net/wiki/spaces/CE/pages/31790891225/Phoenix+Project`
- Asset Correlation architecture: `cybereason.atlassian.net/wiki/spaces/CE/pages/32547962882/Asset+Correlation+Architecture+Service+Tasks+and+Data+Management+Overview`
- Grafana data-from-Postgres example: `grafana-dev-us-ashburn-1.cybereason.net/explore?…`

## Status

Proposed (Q2 priority: High per DS Team project tracker — "To Be Defined"). Lead: [[Guy Kassorla]]; Engineering contacts [[Ortal Keizman]], [[Tonny Pham]].

## Decisions

(populated by /ingest as decisions are taken)

## Risks

- Phoenix schema differs from legacy XDR — pipeline must remap inputs (same risk class as [[Phoenix]]'s own Known Issues entry).
- Benign-vs-detection separation at correlation input still open (cost + accuracy implications) — flagged on the [[Phoenix]] page.

## Mentions

- 2026-05-11 — [[data-science-team-knowledge]] — Q2 High-priority project; lead [[Guy Kassorla]]; Phoenix platform; contacts [[Ortal Keizman]], [[Tonny Pham]].

## Open questions

- Final detection-stage scheme into and out of the correlation engine.
- Cost / latency budget on Phoenix.
- Relationship to [[RCE-NG]] (port vs successor).
