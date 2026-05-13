---
title: Identity Correlation
type: concept
tags: [concept, wiki]
domain: ops
related_projects: ["[[Phoenix Review]]", "[[RCE-NG]]", "[[Incident Investigation (for Fusion 2)]]", "[[Smart Asset Correlation]]", "[[UEBA]]"]
related_systems: ["[[Phoenix]]", "[[Fusion 2]]"]
last_updated: 2026-05-12
---

# Identity Correlation

> The cross-tenant, cross-vendor entity-resolution problem: deciding
> when two observed identifiers (user, host, session, asset) refer to
> the same real-world entity.

## What it is

Across heterogeneous data sources — endpoint sensor telemetry, cloud
IAM logs, identity providers, third-party SIEM feeds — the "same"
entity surfaces under multiple identifiers (hostname vs. asset-id vs.
MAC; email vs. SAM-account-name vs. UPN). Correlation = the mapping
function that resolves these to a single canonical entity.

Recurring bottleneck across DS-team projects; recognized as a hard
unsolved problem per [[identity-correlation-as-unsolved-hard-problem]].

## Why we care

- [[Phoenix Review]] flagged identity correlation as core unfinished platform work.
- [[RCE-NG]] correlation quality is gated on entity resolution upstream.
- [[Incident Investigation (for Fusion 2)]] cross-platform correlation needs identity bridging between Cybereason and Level Blue.
- [[Smart Asset Correlation]] is directly framed as an identity / asset correlation project.
- [[UEBA]] depends on stable per-user / per-entity baselines.

## Tensions

Deterministic rule-based mapping is brittle but auditable; ML-based
similarity matching is more robust but harder to debug + risks
silently merging distinct entities.

## Manifestations

- 2026-05-12 — Catalogued during Concepts seed.
- See [[identity-correlation-as-unsolved-hard-problem]] for cross-project pattern.
- 2026-05-12 — [[UEBA]] lateral-movement detection is a direct manifestation: per-user baseline modelling requires stable cross-source entity resolution ([[UEBA (USMA)]] had this exact challenge — surfaced in [[2026-05-12 — Aviad and Jose intro]]).

## Open questions

- Is there a single canonical identity-correlation service that all DS-team projects should depend on, or per-project resolution?
- ML vs. deterministic — what's the team's preferred posture for production correlation?
