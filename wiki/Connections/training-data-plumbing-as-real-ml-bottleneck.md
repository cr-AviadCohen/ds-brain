---
title: Training data plumbing as the real ML bottleneck
type: connection
tags: [connection, wiki]
instances: ["[[CMD Classification]]", "[[Malop-Worthy]]", "[[2026-04-27 — Aviad and Phil intro]]", "[[2026-05-06 — DS team and Santi handover]]", "[[2026-05-12 — Aviad and Jose intro]]"]
last_updated: 2026-05-12
---

# Training data plumbing as the real ML bottleneck

> Across our ML projects the modelling step is rarely where work stalls — what consistently blocks progress is the upstream plumbing: labelling, ground truth, dataset refresh, and "is this candidate model actually better than the live one?" evaluation.

## Instances

- [[CMD Classification]] — initial VT + BigQuery experiment produced poor results; the explicit conclusion is that "future work emphasises a curated validated dataset", not a model change.
- [[Malop-Worthy]] — known label-coverage gap: "current labels for Malop-Worthy come only from correlations that already passed the existing rules — large untagged regions in the data".
- [[2026-04-27 — Aviad and Phil intro]] — Phil stated outright: "the hardest part is not modelling but training-data plumbing: labelling, refreshing, evaluating good vs bad data, and proving a candidate model is better than the live one".
- [[2026-05-06 — DS team and Santi handover]] — IOI weighting model owns an open ground-truth question ("what labelled benign/malicious dataset will train the IOI weighting model"); Themis automation is explicitly gated on building an OTX-derived ground-truth pipeline.
- [[2026-05-12 — Aviad and Jose intro]] — [[Jose Manuel Martin Rodriguez]] spent the recent phase of his 10-yr Level Blue tenure not writing models but acting as a domain expert who builds datasets and translates cybersecurity concepts for pure data scientists who lacked security background — same pattern from the other side: the highest-leverage ML work was the upstream dataset + label-quality plumbing, done by the person with deep security context.

## What we infer

Any new ML project should budget more time for the labelled-data pipeline than for the modelling step, and define its label source and "is the new model better?" evaluation harness before training begins. A reusable labelling + ground-truth-evaluation layer (OTX pulse joins, analyst-tagging UI, LLM-assisted pre-labelling) is probably more leveraged than a shared modelling library. When prioritising between candidate projects, prefer the one with the cleanest label source.

## Open questions

- Could a single labelling/ground-truth service be shared across CMD Classification, Malop-Worthy, IOI weighting, and Themis retraining instead of each project rolling its own?
- What is the right pattern for proving "new model > live model" — A/B in production, holdout-on-recent-traffic, or analyst-graded sample evaluation?
