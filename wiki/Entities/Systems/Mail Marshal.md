---
title: Mail Marshal
type: system
tags: [system, wiki]
owner: Trustwave (acquired by Level Blue)
vendor: Trustwave / Level Blue
integration_surface: [email-gateway]
related_projects: []
last_updated: 2026-05-12
---

# Mail Marshal

> Trustwave's email-security gateway product (anti-spam, anti-phishing, attachment analysis). Acquired by Level Blue as part of the Trustwave acquisition; candidate for DS-team email-attachment ML collaboration.

## Owner / vendor

Trustwave (now Level Blue). Product line inherited via the 2025 Trustwave acquisition.

## Integration surface

Email gateway — inbound mail funnel. Attachments / URLs / sender metadata exposed.

## Data flow

Inbound email → Mail Marshal scoring → quarantine / pass / flag. Candidate flow: enrich Mail Marshal verdict with DS ML scores (attachment classification, URL reputation).

## Current usage

External — Trustwave customer base. No current DS integration as of 2026-05-12.

## Known issues

(unknown — populate as engagement deepens)

## Related entities

- [[Phil Hay]] — Trustwave contact, raised collaboration intent in [[2026-04-27 — Aviad and Phil intro]]
- Decisions: [[2026-04-27 — Email Attachments as First ML Collaboration Target]], [[2026-04-27 — ML Outputs as Mail Marshal Scoring Inputs]]

## Open questions

- Which scoring fields can Mail Marshal accept as inputs (rate-limit, schema)?
- Volume of email flow eligible for ML enrichment (per day, per customer tier)?
