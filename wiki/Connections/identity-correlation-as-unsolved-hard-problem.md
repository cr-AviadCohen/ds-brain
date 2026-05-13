---
title: Identity correlation as the unsolved hard problem in cross-vendor security
type: connection
tags: [connection, wiki]
instances: ["[[RCE-NG]]", "[[Incident Investigation (for Fusion 2)]]", "[[2026-04-30 — Aviad and Pawel intro]]"]
last_updated: 2026-05-11
---

# Identity correlation as the unsolved hard problem in cross-vendor security

> Every cross-vendor correlation / attack-story effort eventually breaks on the same wall: there is no unified identity model across SIEMs, vendors, and customer fleets, so the same "user" or "asset" cannot be reliably joined across data sources.

## Instances

- [[2026-04-30 — Aviad and Pawel intro]] — Pawel's "Correlate ML" effort stalled on missing unified identity management across ~4,000 clients; Aviad confirmed the same identity-resolution gap is blocking attack-story correlation on the Phoenix XDR project.
- [[RCE-NG]] — Risk Chain Engine correlates detection events from multiple vendors (XDR) into a single attack story; its pivot to Phoenix as input source explicitly depends on Phoenix's detection schema and on bringing entities/IOCs into alignment.
- [[Incident Investigation (for Fusion 2)]] — open issue called out directly: "missing entities/IOCs in vendor alerts (Sentinel, Defender, Cortex) significantly limit AI verdict accuracy"; the project needs structured Incident/Alert/Evidence schemas and additional enrichment APIs.

## What we infer

Any project that depends on joining the same entity across multiple vendors must explicitly own — or pick — an identity-resolution layer; it cannot assume one exists. New AI-for-correlation projects should be designed to fail loudly when identity coverage is sparse rather than silently degrading verdict quality. This is also a strategic investment area: a unified identity model would unblock multiple in-flight projects simultaneously.

## Open questions

- Is there a single owner (Phoenix? RCE-NG?) who should drive a unified identity model rather than each project rolling its own?
- Can OTX / VirusTotal / Sage enrichment APIs be combined to bootstrap a "good enough" identity resolution layer for the next ~12 months while a deeper solution is designed?
