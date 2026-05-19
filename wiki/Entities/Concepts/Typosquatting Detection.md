---
title: Typosquatting Detection
type: concept
tags: [concept, wiki]
domain: security
related_projects: ["[[Infrastructure of Interest]]"]
related_systems: ["[[BestWhois Collector]]"]
last_updated: 2026-05-19
source: raw/meetings/meeting_2026-05-14_infrastructure_of_interest.md
---

# Typosquatting Detection

> Detection of domain names visually or phonetically close to a target brand (`gmial.com`, `paypa1.com`, `blackhorizon.online`) intended to deceive users into trusting attacker-controlled infrastructure.

## What it is

Two complementary techniques used in [[Infrastructure of Interest]]:

- **Fuzzy string matching** — Jaro-Winkler edit-distance against a known-brand list (catches typos of any length).
- **Semantic similarity** — embedding-model nearest-neighbor against the same brand list (catches lookalikes that fuzzy misses: visually similar but edit-distance far — e.g., `outlook-365-login.online` for "Outlook").

Both run inside [[BestWhois Collector]] on the WHOIS new-registration feed so candidates are caught at registration time, often before any victim resolves the domain.

## Why we care

- Foundational filter for IOI's earliest-signal collector.
- Pattern transfers cleanly to phishing detection in [[Mail Marshal]] / customer email gateways.
- Embedding-similarity layer is a DS-leverageable surface — improving the embedding choice / brand list maintenance is a candidate DS contribution.

## Manifestations

- 2026-05-14 — [[2026-05-14 — Infrastructure of Interest (SLR Brownbag)]] — Jose Manuel walked through fuzzy + semantic submodules + entropy/TLD filter.

## Open questions

- Brand-list curation: who owns the canonical "known brands" set and how is it updated?
- Embedding model identity + drift handling.
- Does the same detector serve any other DS-team workflows ([[Owlint-Sigma]], [[Mail Marshal]] ML)?
