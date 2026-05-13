---
tags: [virustotalclassifier, architecture]
type: reference
project: virustotalclassifier-meta
---

# Architecture — Five Subsystems

The repo has one umbrella project, five subsystems, and **two architectural lineages**:

```
                  virustotalclassifier/
                   │
                   ├── meta/          ← lineage A: meta-classifier (stacking over AV engines)
                   │     ▲
                   │     │ (calls meta.run())
                   ├── ginger/main.py        ← Linux ELF, binary
                   ├── olive/black_olive/    ← scripts, binary (malicious)
                   ├── olive/green_olive/    ← scripts, binary (benign)
                   ├── snitch/main.py        ← MS Office, multiclass
                   │
                   ├── broccoli/       ← lineage B: KNN over hand-crafted features
                   │     - cluster.py / build_dataset.py / train.py / classify.py
                   │
                   ├── classify.py / collect_engine_data.py / cruvit.py  ← top-level utilities
                   ├── version.py
                   └── quicklib_setup.yml
```

## Lineage A — Meta classifier (`meta/` and its wrappers)
The headline system. Architectural pattern: **two-phase sklearn pipeline**, where Phase 1 is always a learned binary, and Phase 2 (only for multiclass tasks) is a rule-based fine-grained classifier.

Domain-specific wrappers (`ginger/`, `olive/*`, `snitch/`) **don't extend the model** — they just load a JSON config and call `meta.run(config)`. The whole flexibility lives in the configuration file (referees query, dataset filters, classes, conditions, …).

Mental model: meta = framework, wrappers = configurations.

Detailed in:
- [[03 - Meta Model Concept]] — the central idea.
- [[04 - Meta Pipeline Flow]] — the data flow.
- [[09 - Sister Projects (olive, ginger, snitch)]] — what each wrapper does.

## Lineage B — Broccoli (`broccoli/`)
A separate, older approach: instead of meta-learning over AV engines, build **hand-crafted features** from VT reports (counts, tags, certs, malware-name TFIDF, …), reduce dimensionality, and classify with **KNN over an Annoy index**.

Mental model: broccoli = "look up the nearest-neighbour samples in feature space and return their majority label". A purely instance-based, similarity-search approach.

Detailed in [[10 - Broccoli Subsystem]].

## Why both lineages coexist
- Broccoli came first (older code, references InnoDB/MySQL via `innovationdb`).
- Meta came later, leveraging sklearn 0.20+, with a cleaner pipeline + estimator architecture.
- They're complementary tools: broccoli for fast nearest-neighbour lookup; meta for principled thresholded decisions.
- Some glue exists (e.g. `meta/samples.py` selects samples where snitch ≠ broccoli for analyst review — using the *disagreement* as a query strategy).

## Top-level files
- **`classify.py` (top-level)** — convenience CLI that classifies a list of SHAs.
- **`collect_engine_data.py`** — pulls engine statistics from BigQuery for offline analysis.
- **`cruvit.py`** — auxiliary tool (likely a small script — minor).
- **`version.py`** — package version.
- **`quicklib_setup.yml`** — internal Cybereason package metadata; declares dependencies (sklearn, annoy, dill, …) and entry points.

## Mapping to "meta models" terminology
When the user / your team says "the meta models", they almost always mean:
- the **`meta/`** framework, AND
- the four wrappers that consume it (**ginger / black_olive / green_olive / snitch**).

Broccoli is normally referred to by its own name. Top-level utilities are pre-pipeline tooling, not "the model".

## Data flow at the top level

```
                      VirusTotal feed (BigQuery)
                              │
                              ▼
                       meta/build_dataset.py
                              │
                              ▼
                       meta/vtreferees.py  ←── selects top AV engines
                              │
                              ▼
                       meta/train.py  →  meta/estimator.py (binary + multi)
                              │
                              ▼                   ┌── ginger (ELF, binary)
                       trained pipeline (.dill)  ─┼── olive black/green (scripts, binary)
                              │                   └── snitch (Office, multiclass)
                              ▼
                       meta/classify.py / meta/eval.py
                              │
                              ▼
                       label per sha1
```

## Related
- [[01 - Project Overview]]
- [[03 - Meta Model Concept]]
- [[10 - Broccoli Subsystem]]
