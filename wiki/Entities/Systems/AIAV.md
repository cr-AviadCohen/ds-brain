---
title: AIAV
type: system
tags: [system, wiki]
owner: Cybereason
related_projects: []
seeds:
  - raw/data_science_drive/data-science-main.md
last_updated: 2026-05-11
---

# AIAV

> Cybereason's new event-based sensor — successor to the legacy graph-based [[Core]] sensor. Cheaper than Core's RAM-resident Transparency, but not yet deployed because it doesn't support migration.

## Owner / vendor

Cybereason.

## Integration surface

(stub — populate from raw as more design context lands)

## Data flow

Endpoint event stream (rather than [[Core]]'s graph events) → backend. Target backend post-migration is expected to be [[Phoenix]].

## Current usage

Not deployed. Per the DS team's general-knowledge doc, migration onto AIAV is gated on full [[Phoenix]] rollout — at which point AIAV becomes the path forward.

## Known issues

- Does not support migration from Core — hard blocker on rollout today.

## Related entities

[[Core]], [[Phoenix]]

## Open questions

- Migration path design (Core → AIAV).
- Detection-engine parity with the Core sensor (VFP, VPP, BEP, PRP, NGAV, BDP, BDP-AI, Fileless, BitDefender, Anti-Ransomware).
- Timeline.
