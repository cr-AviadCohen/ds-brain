---
tags: [virustotalclassifier, overview]
type: note
project: virustotalclassifier-meta
---

# Project Overview

## One-sentence summary
`virustotalclassifier` is a research codebase that uses **the consensus of ~70 AV engines from VirusTotal** as its input feature space, learning higher-order classifiers ("meta models") that decide malicious / benign with calibrated confidence.

## What it actually does
Given a VirusTotal report for a sample (a row from the VT BigQuery feed), the system:
1. Extracts the **per-engine verdicts** (~70 binary detections, plus engine-specific malware names).
2. Picks a subset of trusted engines as **referees** (statistical selection — see [[05 - Referee Selection]]).
3. Computes a maliciousness score using `VirusTotalAnalyzer` (from internal `vtutils` — clusters engines by similarity to detect echoing).
4. Learns a **threshold** that separates benign from malicious using outlier-robust statistics.
5. Decides via a 3-zone rule:
   - Few detections → `benign`.
   - Many detections → `malicious`.
   - Middle → use the learned threshold on the model score.
6. (Optional) For multi-class tasks, applies a **rule-based** secondary classifier over malware-name tokens and VT tags.

## Why "meta"?
Because the model's inputs are **other models' outputs**.

The VT feed gives you ~70 votes per file from independent commercial AV engines. Each engine has its own:
- **biases** (some over-detect, some under-detect),
- **expertise** (engine X is great at PDFs, engine Y is great at Office docs),
- **echoes** (some engines license each other's signatures and effectively vote twice),
- **delays** (a sample undetected on first scan may show up later).

Meta-modelling is the act of **learning to read the panel of votes** rather than re-detecting from raw bytes. This is exactly the **stacking** pattern in classical ML (level-0 = AV engines, level-1 = our meta classifier).

## Why it exists (vs the [[../ngav-pipeline/00 - Index|ngav-pipeline]])
Different problems, different signals:

| | NGAV pipeline | virustotalclassifier (meta) |
|---|---|---|
| Input signal | PE binary static features | VT engine verdicts + tags |
| Use case | endpoint scanner | label generator / referee / research |
| Online or offline | online | offline (typically labels) |
| Scope | Win32 PE only | any VT-covered file (PE, scripts, Office, ELF, …) |
| Classifier | LightGBM | sklearn pipelines + custom estimators |
| Decision style | learned threshold + AV combine | learned threshold + 3-zone rule + (optional) rule-based multiclass |

In practice the meta system serves as a **labelling and consensus tool**: it produces high-quality labels that other pipelines (including, indirectly, NGAV's training set) consume. It also has **domain-specific wrappers** (olive, ginger, snitch) for scripts, Linux ELF, and Office docs — file types where PE-based classifiers don't apply.

## Five subsystems at a glance
The repo is one project but contains five subsystems with different goals and maturity. Detailed in [[02 - Architecture - Five Subsystems]].

| Subsystem | Role | Status |
|---|---|---|
| `meta/` | core meta-classifier framework | active, well-structured |
| `broccoli/` | KNN-based file classifier (Annoy index over hand-crafted features) | older, complementary |
| `olive/black_olive`, `olive/green_olive` | meta wrappers for scripts (binary) | active |
| `ginger/` | meta wrapper for Linux ELF (binary) | active |
| `snitch/` | meta wrapper for MS Office docs (multiclass) | active |

## What it is *not*
- Not a real-time scanner — purely offline.
- Not a single end-to-end model — the multiclass case is a learned binary stage followed by a rule-based stage.
- Not the production scanner — that's [[../ngav-pipeline/00 - Index|NGAV]].
