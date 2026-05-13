---
title: Risk Assessment
type: project
tags: [project, wiki]
status: active
started: 2026-05-11
systems: []
related_decisions: []
raw_path: raw/projects/Project - Risk Assessment/
last_updated: 2026-05-11
---

# Risk Assessment

> Defines required schema fields and rule logic for computing event risk scores and downstream incident correlation in the new platform.

## Goal

Specify the fields the new schema must surface so risk scoring (Day 1: per-event score driven by metadata, asset/file/process reputations, integrity, NAT/URL reputations, permissions checks for admin/system via regex) and correlation (Day 2: incident-level grouping by metadata IDs, asset, file, network interface, process identity) can be implemented consistently.

## Approach

Day 1 — list of required fields for event-level scoring (metadata.action/engine/severity, principal/target asset reputations, file/IP/URL/DNS/email reputations, process/parent integrity and reputation, registry/user permission names checked via regex for "admin"/"system"). Day 2 — extended schema requirements for incident correlation (event_id, subtype, type, severity, severity_details, timestamp, type, uuid, principal and target asset fields, file SHA256/TLSH/UUID/internal_name, group name, NAT IP, network interface details, process creation_time, etc.). Open ask to engineering: is there a field indicating whether the process is still running?

## Status

active — seeded from raw 2026-05-11.

## Decisions

(populated by /ingest as decisions are taken)

## Risks

(populated as identified)

## Mentions

(populated by /ingest)

## Open questions

- Is there a schema field indicating whether the process is still running?
