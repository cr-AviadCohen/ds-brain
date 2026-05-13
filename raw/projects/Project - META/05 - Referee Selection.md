---
tags: [virustotalclassifier, referees, av-engines]
type: note
project: virustotalclassifier-meta
---

# Referee Selection

> Picking which AV engines get to vote — the most influential design choice in the whole system.

## Module
`virustotalclassifier/meta/vtreferees.py`. Class: `VirusTotalReferees`.

## What it does
Given the **"back to the future" dataset** (samples that started undetected and later became widely detected), compute per-engine performance and select the top engines as **referees**. Those referees are passed to `VirusTotalAnalyzer` later to weigh more heavily.

## The "back to the future" labelling
For each sample in the dataset:
- **Positive label** (`detections_increased = True`): `min_positives ≤ 2` at first scan AND `max_positives ≥ 8` at last scan AND `last_scan_date > first_scan_date`. These are samples where the engine community **eventually agreed** something was malicious — strong proxy for "actually malicious".
- **Negative label** (`detections_increased = False`): the sample's positive count was stable / didn't genuinely grow.

This is a *temporal* proxy: instead of using a curated ground truth, the system uses **future consensus** as the label.

Why it works: if 8+ engines eventually flag something that started undetected, that's strong evidence of real maliciousness. The few engines that **caught it early** (or at all) are the ones we should trust.

## The metric: F_β with β = 0.5
For each AV engine independently:

```
precision = TP / (TP + FP)
recall    = TP / total_increased

F_β = (1 + β²) · precision · recall / (β² · precision + recall)
F_0.5 = 1.33 · precision · recall / (0.25 · precision + recall)
```

Where:
- TP = the engine flagged a `detections_increased=True` sample as malicious.
- FP = the engine flagged a `detections_increased=False` sample as malicious.
- "total_increased" = total samples where consensus actually grew.

`β=0.5` weights **precision twice as much as recall**. This is intentional: an engine that is reliably right when it says "malicious" is more useful as a referee than one that catches everything but with lots of FPs.

## Selection rule
- Compute F_0.5 for every engine.
- Take the **top 10%**, with a floor of 10 engines (so even if all engines tie, you get at least 10).
- Output: `referees` list of engine names + per-engine TP / FP / precision / recall as a DataFrame for inspection.

## Engine grouping (echo handling)
`group_names_mapper` is a dict that merges engines whose verdicts are near-identical (e.g. K7 variants, multiple Bitdefender-engine wrappers). Within a group, the system treats agreeing votes as **one vote**, not many. This avoids double-counting echoes.

The grouping is **explicit and curated** in this file — not learned. If a new vendor licenses another vendor's engine, this dict needs updating.

## How referees flow downstream

```
   referees = ['Avast', 'Kaspersky', 'ESET', ...]
                  │
                  ▼
   MetaBinaryEstimator(referees=referees)
                  │
                  ▼
   VirusTotalAnalyzer(referees=referees, min_engine_distance=0.05)
                  │  (internal vtutils black box)
                  ▼
   per-sample maliciousness score
```

`VirusTotalAnalyzer` (from internal `vtutils`) presumably weights referee votes higher than non-referee votes, and possibly excludes non-referees entirely. Its source isn't in this repo — treat it as a black box.

`min_engine_distance = 0.05` means engines whose verdicts are < 5% Hamming-distance apart are treated as the same vote (more echo handling, this time done online).

## Caching
Referee computation is **expensive** — a multi-CTE BigQuery scan over many months of feed data — so it's cached. `meta/run.py` checks for a cached referees file before recomputing.

## What can go wrong here
- **Stale `group_names_mapper`**: if a new echo group is missed, those engines effectively vote multiple times.
- **Bias by file type**: referees selected on one file-type distribution may not be optimal for another. Each wrapper (`ginger`, `olive`, `snitch`) re-runs referee selection per file type — this is correct.
- **"Back to the future" labelling assumes consensus = truth**: a coordinated FP cascade across engines (rare but possible) would poison the labels.
- **Top-10% threshold is arbitrary**: not learned, just a heuristic.

## Why this matters conceptually
The whole meta-classifier rests on: **"some engines are systematically more reliable than others, and we can statistically pick those engines using past consensus as a label."** If that premise breaks, the cascade collapses.

The premise is reasonable but worth periodic re-validation — re-running `VirusTotalReferees` quarterly and comparing the chosen referee list over time is a sensible health check.

## Related
- [[03 - Meta Model Concept]] — why we even bother
- [[04 - Meta Pipeline Flow]] — where this stage sits
- [[07 - Binary Estimator]] — what consumes referees
- [[14 - Glossary]] — F_β definition
