---
tags: [virustotalclassifier, concept, meta-learning, stacking]
type: note
project: virustotalclassifier-meta
---

# Meta Model Concept

> The single most important concept in this project. Read this once and the rest of the code makes sense.

## What is a "meta model" here?
A **classifier whose features are other classifiers' outputs**. In ML terminology this is **stacking**:

```
   Level-0 (the engines):
     [Avast]   [Kaspersky]  [ESET]  [TrendMicro]  …  ~70 of them
       │            │          │            │
       │            │          │            │
       └────────────┴──────────┴────────────┘
                          │
                          ▼
                Level-1 (our meta classifier)
                          │
                          ▼
                   {malicious, benign}
```

In this project, **level-0 = AV engines on VirusTotal**. We don't train them — VT already runs them and gives us their verdicts in the `scans` field of each report.

Level-1 is what `meta/` learns.

## Why this is interesting (vs naive majority vote)

A naive baseline is: "if ≥N of 70 engines say malicious, it's malicious." That's already pretty good. But it has flaws:

1. **Engines are not independent.** Many license each other's signatures and "echo" each other. Counting echoes as separate votes overweights certain detections.
2. **Engines have different biases.** Some chase recall (over-detect), some chase precision (under-detect). A flat count loses this information.
3. **The temporal dimension matters.** A sample undetected today and detected next week is different from a sample detected by the same engines repeatedly.
4. **Some engines are good at certain file types.** Kaspersky might be great at PDFs, ESET at scripts, Avast at PE, etc.

The meta system addresses all four:
1. **Echo grouping** — `VirusTotalAnalyzer` (from internal `vtutils`) clusters engines whose verdicts always agree (Hamming distance < 5%) and merges them into a single weighted vote.
2. **Referee selection** — `vtreferees.py` picks top engines by F-β (β=0.5, weighted toward precision) — see [[05 - Referee Selection]].
3. **"Back to the future" sampling** — training data is constructed from samples that started undetected but later got many detections — capturing the harder cases (see [[04 - Meta Pipeline Flow]]).
4. **File-type wrappers** — per-domain configs (`ginger`, `olive`, `snitch`) re-run referee selection per file type, so the right engines get picked for each domain.

## The two-phase architecture

### Phase 1: Learned binary classifier (always)
`MetaBinaryEstimator` — a sklearn estimator that wraps `VirusTotalAnalyzer` and adds a learned threshold + a 3-zone decision rule. See [[07 - Binary Estimator]].

### Phase 2: Rule-based multiclass (optional, only for multiclass tasks)
`MetaMultiEstimator` — *not* a learned model. A configurable rule engine over malware-name tokens and VT tags. If the binary phase says `benign`, this phase doesn't run (the `SampleSplitter` routes to a `ConstantEstimator("benign")`). See [[08 - Multiclass Estimator]].

```
                  X (VT report)
                        │
                        ▼
              ┌─────────────────────┐
              │  Phase 1: binary    │   learned classifier
              │  MetaBinary         │
              └────────┬────────────┘
                       │
              ┌────────┴────────┐
              │                 │
              ▼ benign          ▼ malicious
        ┌─────────┐    ┌────────────────────────┐
        │ return  │    │ Phase 2 (multi-only):  │
        │ benign  │    │ rule-based             │
        └─────────┘    │ MetaMulti              │
                       │ classes_tags + tokens  │
                       └────────┬───────────────┘
                                ▼
                          {downloader,
                           dropper, exploit,
                           ...}
```

Why two phases? **Asymmetric error costs.** A wrong "benign" call is acceptable; a wrong "exploit" call is not. The binary stage acts as a confident gate. The multiclass stage runs only on what the binary stage already confidently flagged as malicious — and uses **rules**, not a classifier, because the failure mode of "made-up rare class" is worse than the failure mode of "didn't get the rare class but said malicious".

## Why is Phase 2 rule-based, not learned?

Three reasons (interpreting the design):
1. **Class imbalance.** Multiclass labels (downloader, dropper, exploit, …) are scarce. Training a learned multiclass would require either label-noisy weak supervision or many-fold over-sampling.
2. **Interpretability.** Rules ("any tag matches CVE → label exploit") are inspectable, auditable, and debuggable. Analysts can read them.
3. **Tag and token signals are surface-level.** They're enough to write good rules over (see [[06 - Feature Engineering]]) and don't benefit much from a learned model.

It's also a pragmatic choice: the project's best-known multiclass deployment is `snitch` (Office docs), where the class taxonomy is well-defined and AV detection-name tokens are very predictive (e.g. `"Trojan-Downloader"` → `downloader`).

## Connection to the broader ML literature
- This is **stacking** in the standard sense (Wolpert 1992).
- The "echo grouping" via Hamming-distance clustering is conceptually close to **ensemble pruning** / **diversity-aware ensembling**.
- The 3-zone decision rule is a form of **abstention / cascade** classifier — confident extremes go straight, uncertain middle defers to a more expressive model.

## Related
- [[04 - Meta Pipeline Flow]] — concretely how it's trained and run.
- [[05 - Referee Selection]] — how level-0 engines are picked.
- [[07 - Binary Estimator]] — the workhorse.
- [[08 - Multiclass Estimator]] — the rule-based stage.
