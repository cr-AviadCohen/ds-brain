---
title: Over-merge Preferred over Under-merge
type: decision
tags: [decision, wiki]
date: 2026-05-18
deciders: ["[[Xin Tang]]"]
status: accepted
related_projects: ["[[Smart Asset Correlation]]"]
last_updated: 2026-05-18
---

# Over-merge Preferred over Under-merge — 2026-05-18

## Context

[[Smart Asset Correlation]] merges vendor-specific asset / identity instances into canonical real-world entities so that [[Phoenix]] automated response (isolate machine, disable account) operates on the complete view of a compromised actor. Confidence is never 100% — both directions of error are possible.

## Decision

When the system must choose, over-merge: prefer false-positive correlations (merging two instances that may be different real-world entities) over false-negative correlations (failing to merge two instances that are actually the same entity).

## Why

If the correlation engine under-merges, automated response is incomplete — when an analyst isolates a compromised machine or disables a compromised user, the un-merged sibling instance is not contained and the threat continues. The product's MDR value proposition depends on full containment.

Over-merging is recoverable: at worst, response actions scope in a few extra benign assets, which is operationally annoying but reversible. Under-merging silently fails to contain a live threat, which is not recoverable.

[[Xin Tang]] framed this as the team's working priority — false positives in correlation are the lesser evil because they protect the response surface.

## Alternatives considered

- **Symmetric thresholds.** Treats both errors equally. Rejected — the costs are asymmetric.
- **Conservative (under-merge bias).** Cleaner UX (no spurious links) at the cost of broken response. Rejected — defeats the MDR product story.

## Consequences

- Confidence-score thresholds in the DS Phase 2 service should err on the inclusive side.
- Analyst UX must surface "this merge is low-confidence" and allow override / split — over-merge is recoverable only if analysts can see it and unwind it.
- Evaluation harness must measure both directions of error, but optimisation targets recall (catching all true merges) over precision.

## Open questions

- Specific confidence threshold + calibration plan.
- Override UX — how does an analyst split a wrongly-merged canonical entity, and does the system learn from it?
- Are there asset classes (e.g. service accounts vs human users) where the asymmetry inverts?
