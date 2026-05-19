---
title: DGA Detection
type: concept
tags: [concept, wiki]
domain: security
related_projects: ["[[Infrastructure of Interest]]"]
related_systems: ["[[BestWhois Collector]]"]
last_updated: 2026-05-19
source: raw/meetings/meeting_2026-05-14_infrastructure_of_interest.md
---

# DGA Detection

> Detection of **Domain Generation Algorithm** output — pseudo-random domains an attacker pre-computes (often thousands per day) so C2 endpoints can rotate faster than defender takedowns.

## What it is

DGA signatures used in [[Infrastructure of Interest]] / [[BestWhois Collector]]:

- **High Shannon entropy** on the second-level label (random-looking text).
- **Suspicious TLDs** (cheap, lenient registrars).
- **Burst registration** — many domains of similar length / pattern registered within minutes-to-hours of each other.

Each signal alone is noisy; the combination at registration time is a strong DGA indicator.

## Why we care

- Direct flag in the IOI ~45-flag scoring layer.
- Detected early via [[BestWhois Collector]] entropy + TLD filter — pre-resolution.
- DGAs feed [[Command and Control]] beacons; catching them at registration starves C2 channels before deployment.
- Adjacent to [[Behavior Clustering]] *exponential* cluster signal (DGA registration vs. DGA usage observed in fleet).

## Manifestations

- 2026-05-14 — [[2026-05-14 — Infrastructure of Interest (SLR Brownbag)]] — Jose Manuel called out entropy + TLD + burst-registration combo.

## Open questions

- Entropy threshold tuning — fixed cutoff or adaptive per TLD?
- TLD blocklist source + refresh.
- Could DGA cluster output feed [[Owlint-Sigma]] as auto-generated network-detection rules?
