---
tags: [virustotalclassifier, estimator, binary]
type: reference
project: virustotalclassifier-meta
---

# Binary Estimator (`MetaBinaryEstimator`)

The workhorse of the meta system. Source: `virustotalclassifier/meta/estimator.py`.

## Class shape
```python
class MetaBinaryEstimator(BaseEstimator, TransformerMixin):
    def __init__(self, configuration):
        self.configuration = configuration   # incl. referees, thresholds, hyperparams
        ...

    def fit(self, X, y=None): ...
    def predict(self, X) -> Series['benign'|'malicious']: ...
    def predict_proba(self, X) -> array of (P_benign, P_malicious): ...
```

It is a sklearn-compatible estimator; it can sit at the end of a `Pipeline`.

## What it actually does (`fit`)

```python
def fit(self, X, y=None):
    # X is the binary verdict matrix from VerdictTransformer (samples × engines).
    self.vta_ = VirusTotalAnalyzer(
        min_engine_distance=0.05,
        referees=self.configuration['referees']
    )
    X_vta_scores = self.vta_.fit_predict(X)   # per-sample maliciousness score in [0,1]

    # Normalise positives count by unique engine groups (echo handling)
    normalised_positives = self._normalize_positives_detections(X)

    # Fit MinMax scaler over (positives ≤ 30)
    self._vta_min_max_transformer.fit_transform(X_vta_scores)

    # Learn threshold separating low-detection vs high-detection samples
    self._find_malicious_score_threshold(X, X_vta_scores, normalised_positives)
```

The threshold-learning step uses **3-sigma outlier filtering**: instead of optimising a recall/FPR target on a holdout (we don't have a curated ground truth), it picks the score value that best separates the bulk of the score distributions of "few-detection" vs "many-detection" samples.

## What it does (`predict`)

```python
def predict(self, X):
    score = self.vta_.predict(X)
    pos   = self._normalize_positives_detections(X)
    return self._make_decision(score, pos)
```

### The 3-zone rule (`_make_decision`)
```python
if normalised_positives <= self.min_positives_detection:    # default 3
    return 'benign'
elif normalised_positives >= self.max_positives_detection:  # default 8
    return 'malicious'
else:
    return 'benign' if score < self.malicious_score_threshold_ else 'malicious'
```

| Zone | Rule | Why |
|---|---|---|
| **Low** (`pos ≤ 3`) | always `benign` | Even our top referees rarely all-miss real malware. ≤ 3 detections in real-world traffic is usually noise. |
| **High** (`pos ≥ 8`) | always `malicious` | If 8+ engines (post echo-grouping) flag it, the case is closed. The model can't add information here. |
| **Mid** (`3 < pos < 8`) | use the learned score threshold | The interesting zone. Engines disagree. The learned model uses *which* engines agree, not just *how many*. |

**Critical insight**: the model only really matters in the middle zone. Outside it, the rule alone decides. This is by design — the model is calibrated against "easy" cases and adds value to ambiguous ones.

## What's normalised in `_normalize_positives_detections`?
Raw `positives` from VT counts every flag as one. But after echo-grouping (engines that always agree are one vote), the "effective" count is lower. `_normalize_positives_detections` returns the count of *unique engine groups* that flagged the sample — a less-noisy detection count.

## How `predict_proba` works
Available for binary. Returns `(P_benign, P_malicious)` based on `vta` score (with calibration via the MinMax scaler). Useful for downstream consumers that want a continuous score.

> Note: `MetaMultiEstimator` (Phase 2) explicitly **does not** implement `predict_proba` — it raises `NotImplementedError`. So if you need probabilities for a multi-class run, you only have them for the binary phase.

## Hyperparameters (from `configuration['estimator_configuration']`)
- `min_positives_detection` — default `3` — boundary of the low zone.
- `max_positives_detection` — default `8` — boundary of the high zone.
- `min_engine_distance` — default `0.05` — passed to `VirusTotalAnalyzer` for echo grouping.
- `referees` — list — comes from the referee selection stage ([[05 - Referee Selection]]).

These are **not learned** — they're configuration. Re-tuning them requires manual experiments.

## The dependency on `VirusTotalAnalyzer`
The estimator is essentially a **calibrated wrapper around `VirusTotalAnalyzer`** (from internal `vtutils`). The analyser does the actual heavy lifting:
- engine clustering for echo handling,
- referee weighting,
- score computation per sample.

`MetaBinaryEstimator` adds:
- learned threshold (from the score distribution),
- the 3-zone decision rule,
- a sklearn-compatible interface.

If `VirusTotalAnalyzer` is buggy or stale, the estimator inherits the bug.

## Mental model
> "The estimator is a calibration layer on top of VirusTotalAnalyzer. It says: trust the analyser's score in the middle zone, but override with hard rules at the extremes — most of the noise is at the extremes anyway."

## Failure modes worth knowing
- **Score-distribution bimodality assumption**: if the score distribution is unimodal (every sample looks similar), the learned threshold becomes meaningless. Re-fitting on a more diverse dataset is the answer.
- **3-zone hardcoding**: the boundaries `3` and `8` are independent of the analyser's calibration. If the analyser changes its scoring scale, these need re-tuning.
- **Cold start**: with no referees yet (first run), `VirusTotalAnalyzer` falls back to default weighting — quality degrades.

## Related
- [[03 - Meta Model Concept]] — the 3-zone idea
- [[06 - Feature Engineering]] — the input matrix
- [[08 - Multiclass Estimator]] — the next phase
- [[14 - Glossary]] — `vtutils`, `VirusTotalAnalyzer`, echo grouping
