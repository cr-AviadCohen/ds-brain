---
tags: [virustotalclassifier, tech-debt, observations]
type: note
project: virustotalclassifier-meta
---

# Technical Debt & Observations

Honest read of the codebase. Roughly ordered by impact.

## High impact

### 1. `VirusTotalAnalyzer` is a black box 🔴
The binary estimator's actual model — engine clustering, referee weighting, score computation — lives in internal `vtutils`. None of it is in this repo. Consequences:
- Can't reason about its calibration without access to that source.
- Bugs there are inherited silently.
- Replacing or A/B-testing the analyser requires rebuilding the dependency.

This is by far the most consequential piece of "hidden" logic in the system.

### 2. Multiclass has no `predict_proba` 🟠
`MetaMultiEstimator.predict_proba` raises `NotImplementedError`. Many downstream consumers expect probabilities (calibration, ROC-curve evaluation, ensembling). Forcing a hard label limits how multiclass results can be used.

### 3. Threshold learning is unsupervised and brittle 🟠
`MetaBinaryEstimator._find_malicious_score_threshold` uses 3-sigma outlier filtering on the score distribution rather than optimising against a holdout. If the score distribution is unimodal (no clear bimodal split), the learned threshold becomes arbitrary.

A small labelled holdout would let it use precision/recall targets and be much more robust.

### 4. Hardcoded zone boundaries (3 / 8) 🟠
`min_positives_detection=3` and `max_positives_detection=8` are configurable but not learned. They were presumably picked once. If VT's engine pool grows or the average engine quality shifts, these would need re-tuning, but there's no automated mechanism.

## Medium impact

### 5. Two systems doing similar work without explicit integration 🟡
Meta and broccoli both classify VT samples but live in parallel. The only documented intersection is `meta/samples.py:rand_samples()` which selects samples where they disagree — but no formal ensembling, no policy for which to trust when. Either:
- Designate one as primary and document the other's role explicitly, or
- Combine them via a meta-meta layer (probably overkill).

### 6. `global_vars.py` is a mutable module-level dict 🟡
`run.py` populates it at runtime. Any code can mutate it. Hard to test in isolation; hard to reason about state. Replace with a config object passed explicitly.

### 7. Rule-based multiclass is brittle to drift 🟡
`MetaMultiEstimator`'s rules reference specific tag names (`download`, `cve`, `macros`, `powershell`). If VT renames or removes one, the rules silently degrade. No drift detection, no validation.

### 8. Inline / hand-written BigQuery (large multi-CTE) 🟡
Like the [[../ngav-pipeline/10 - Technical Debt & Open Issues|ngav pipeline]], queries are constructed in Python with large embedded SQL fragments. Hard to test, version, or migrate.

### 9. Caching invalidation is implicit 🟡
Cached referees / training datasets are keyed by JSON-config parameters but the keying is not robust to whitespace / ordering changes in the config. Easy to silently use a stale cache when you intended a fresh run.

### 10. `dill==0.2.6` is ancient 🟡
Loading old pickled models in modern Python may fail. Bumping it requires re-pickling, which requires retraining. Lock-in risk.

## Low impact

### 11. Typo in feature name (`marcos_plus_powershell`) 🟢
Should be `macros`. Not breaking — but propagates through downstream consumers.

### 12. Top-10% referee selection is a hardcoded magic constant 🟢
Configurable but not documented. Other projects might want a different cutoff.

### 13. `EnginesTokensTransformer` cutoff (0.7 in `difflib`) 🟢
Permissive. Can pull in noisy tokens. Worth audit if a class has weak performance.

### 14. No drift / health-check tooling 🟢
Engines come and go on VT; their reliability shifts. There's no automated alert for "your top referee Engine X dropped to 50% F-β last month."

### 15. The four wrappers duplicate boilerplate 🟢
`ginger/main.py`, `olive/black_olive/main.py`, `olive/green_olive/main.py`, `snitch/main.py` are nearly identical. Could be one CLI taking a config path.

## Categorical observations

### Strengths
- **Cleanly layered**: meta/ is a framework, wrappers are configurations. Genuinely good separation.
- **Decorator-based query registry** (`@mark_as_query`) is elegant — queries can be referenced by name from JSON.
- **Two-phase architecture** (binary gate then multiclass rules) is a thoughtful design that handles asymmetric error costs.
- **"Back to the future" labelling** is a creative use of temporal consensus to bootstrap labels without a human-curated ground truth.
- **Echo grouping** for engine deduplication is a real insight — naïve majority votes get this wrong.

### Patterns of debt
- A lot of magic numbers (top-10%, cutoff 0.7, zones 3/8, 95% null filter, etc.) without documented rationale.
- Heavy reliance on internal black-box libraries.
- Two parallel systems (meta + broccoli) with no explicit policy for combining them.

## Suggested refactor batches
1. **Replace unsupervised threshold learning with a small labelled holdout** — biggest quality win.
2. **Unify the four wrappers into one `meta-cli <config_path>` entry point** — boilerplate cleanup.
3. **Document `VirusTotalAnalyzer`'s contract** — even just the input/output schema and key parameters. Reduces black-box risk.
4. **Add drift monitoring on the referees list** — quarterly sanity check.
5. **Either learn the multiclass model or document why the rules are deliberately rule-based** (cf. [[08 - Multiclass Estimator]]).

## Related
- [[03 - Meta Model Concept]]
- [[07 - Binary Estimator]]
- [[10 - Broccoli Subsystem]]
