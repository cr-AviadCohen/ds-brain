---
title: Campaign Assembler
type: system
tags: [system, wiki, clustering, threat-intel]
owner: "[[Labs]]"
vendor: internal (Level Blue / SLR)
integration_surface: [ioi-pipeline, analyst-workflow]
related_projects: ["[[Infrastructure of Interest]]", "[[Tipper]]"]
related_systems: ["[[Themis]]", "[[Behavior Clustering]]"]
source: raw/meetings/meeting_2026-05-14_infrastructure_of_interest.md
last_updated: 2026-05-19
---

# Campaign Assembler

> Final stage of [[Infrastructure of Interest]]. Groups disparate domain observations into cohesive, investigation-ready **campaign objects** so analysts can pivot from a single IOC to a full attack narrative in ~2 hours. Five clustering methodologies × 16 views; consensus ≥4 views → solid cluster.

## Owner / vendor

Internal SLR Labs system under [[Jose Manuel Martin Rodriguez]]. Direct collaboration request to DS team ([[Aviad Cohen]]) on clustering improvements.

## Integration surface

- Input: enriched + scored observations from [[Infrastructure of Interest]].
- Output: campaign objects (5 evidence dimensions + text templates + suggested investigation steps + 11-type cluster taxonomy) surfaced to analysts via [[Tipper]].
- Deliberately no LLM on the per-observation hot path (cost). Templates are text-based. LLM scoring of "which campaigns to investigate first" planned as an off-hot-path layer.

## Clustering methodologies (5)

- **Hash bucketing** — same payload / same MD5 of sorted ports / same cert.
- **Weighted Jaccard** — weighted vector overlap on shared attributes.
- **Time-window bursts** — 48h coordination signal.
- **Latent community detection** — graph-based clustering that fills gaps where pairwise signals are sparse.
- (+ one more, unnamed in source).

## Consensus rule

Run all 5 methodologies across 16 analytical views in parallel. **≥4 of 16 views must agree** → solid cluster. Below threshold → discard or defer.

## Output: 5 evidence dimensions

Each cluster ships with:
- Forensic payload evidence.
- External attribution signals.
- Content morphology.
- Shared infrastructure.
- Behavioral signals.

Plus text-template explanations + suggested investigation steps. No LLM at this stage (cost-prohibitive at scale).

## Cluster taxonomy (11 types)

- **Analyst-ready**: direct attribution, strong 48h coordination, forensic 3rd-party report (Country / Mute / phishing-feed match).
- **Emerging legitimate**: monitor, defer.
- **Noise**: discard.

45-day bootstrap stats: 774 consensus clusters → 234 analyst-ready campaigns. ~0.6 of observations actually funnel into a cluster.

## Current usage

- Production stage of [[Infrastructure of Interest]] dissemination.
- Surfaces via [[Tipper]] UI alongside the Sigma interop tool.

## Known issues

- LLM cost ceiling: cannot afford LLM-per-observation, so explanations are templated.
- 16-view breakdown not fully enumerated in current docs (only 5 methodologies named).

## Related entities

- Projects: [[Infrastructure of Interest]] (parent), [[Tipper]] (analyst surface).
- People: [[Jose Manuel Martin Rodriguez]] (owner), [[Aviad Cohen]] (DS collaboration offered).
- Meetings: [[2026-05-14 — Infrastructure of Interest (SLR Brownbag)]].

## Open questions

- Fifth clustering methodology — name + role.
- 16-view enumeration — which methodology contributes how many views?
- LLM ranking layer scope (off-hot-path) — DS team or SLR own?
- Can the 5 evidence dimensions feed [[Owlint-Sigma]] as net-new Sigma-rule seeds?
