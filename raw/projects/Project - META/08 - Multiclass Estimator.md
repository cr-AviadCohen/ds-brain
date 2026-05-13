---
tags: [virustotalclassifier, estimator, multiclass, rules]
type: reference
project: virustotalclassifier-meta
---

# Multiclass Estimator (`MetaMultiEstimator`)

The fine-grained classifier. **Not** a learned model — a configurable rule engine.

Source: `virustotalclassifier/meta/estimator.py` (lower half) + `meta/rules.py` for rule primitives.

## When does this even run?
Only when:
1. `configuration['task'] == 'multiclass'`, AND
2. The Phase 1 binary estimator already labelled the sample as `malicious`.

The `SampleSplitter` in `meta/train.py` routes Phase-1-`benign` samples to a `ConstantEstimator("benign")`, bypassing this estimator entirely.

So: **multiclass labels are only produced for samples already confidently flagged as malicious.**

## Class shape
```python
class MetaMultiEstimator(BaseEstimator):
    def __init__(self, configuration):
        self.classes = configuration['classes']               # ['downloader', 'dropper', 'exploit', ...]
        self.classes_tags = configuration['classes_tags']     # {'downloader': ['download', 'cve'], ...}
        self.conditions_list = configuration['conditions']    # ordered list of rule dicts
        self.default_label = configuration['default_label']   # fallback class

    def fit(self, X, y=None):
        return self          # nothing to learn

    def predict(self, X):
        return X.apply(self.decide, axis=1)

    def predict_proba(self, X):
        raise NotImplementedError
```

## The decision (`decide` per row)
Each row has columns from [[06 - Feature Engineering]]: `tag_*` indicators and `token_*` softmax scores.

```python
def decide(self, report):
    for condition_dict in self.conditions_list:
        classes_scores = {
            c: report.get(f'tag_{tag}', 0) + report.get(f'token_{c}', 0)
            for c in self.classes
            for tag in self.classes_tags[c]
        }
        if check_condition(classes_scores, condition_dict):
            return condition_dict['label']
    return self.default_label
```

Rules are **evaluated in order**. First matching rule wins. The default label catches anything that didn't match.

## Rule grammar (`rules.py`)
Conditions are dicts with this shape:
```python
{
    'condition': {
        'class_name': 'rule_function_name',
        ...
    },
    'operator': 'all' | 'any',
    'label': 'downloader' | 'dropper' | ...
}
```

`rule_function_name` is one of (from `rules.py`):
- `bigger_than_one(score)` → True if score > 1.0
- `bigger_than_threshold_and_smaller_or_equal_to_one(score, threshold)` → True if `threshold < score ≤ 1.0`
- (a small registry of similar primitives)

Combined with the operator:
- `all` → every class score must satisfy its condition.
- `any` → at least one class score must satisfy its condition.

Why `> 1.0`? Because `EnginesTokensTransformer` produces softmax-normalised scores, plus tag indicator bits — so a class score above 1.0 means "tag fired AND tokens favoured this class strongly". A natural confidence boundary.

## Concrete example (Snitch — Office docs)
For the `snitch` wrapper (`virustotalclassifier/snitch/`), the configuration might say:

```json
{
  "classes": ["downloader", "dropper", "exploit", "benign"],
  "classes_tags": {
     "downloader": ["download"],
     "dropper":    ["macros", "powershell"],
     "exploit":    ["cve"],
     "benign":     []
  },
  "conditions": [
     {
       "condition": {"exploit": "bigger_than_one"},
       "operator": "all",
       "label": "exploit"
     },
     {
       "condition": {"downloader": "bigger_than_one"},
       "operator": "all",
       "label": "downloader"
     },
     {
       "condition": {"dropper": "bigger_than_one"},
       "operator": "all",
       "label": "dropper"
     }
  ],
  "default_label": "benign"
}
```

Mental model: "Try each class in priority order; the first one whose evidence threshold is met wins; else fall back to benign."

The priority order matters — exploit is checked first because misclassifying an exploit as a downloader is worse than the reverse.

## Why rule-based instead of learned?
Three reasons (cf. [[03 - Meta Model Concept]]):
1. **Class imbalance** — multiclass labels are scarce.
2. **Interpretability** — analysts need to read and override rules.
3. **The features are already very class-aligned** — class names appear literally in malware-name tokens (`Trojan-Downloader`, `Exploit.CVE-...`) and VT tags. The mapping is not subtle.

## What this estimator gives up
- No probabilities (`predict_proba` raises).
- No automatic tuning of thresholds.
- Brittle to feature drift: if VT changes a tag name or stops emitting a category, rules silently degrade.

## What you'd change to make it learned
- Replace `MetaMultiEstimator` with a `LogisticRegression` / `LightGBM` over the same input features (tags + tokens).
- Enable `predict_proba`.
- Train on labelled multiclass samples (likely needs weak supervision — e.g. tag-derived labels — to bootstrap).
- Keep a **rule fallback** for known-rare classes that the learned model would underfit.

## Mental model
> "Phase 2 is a configurable lookup table over class-aligned features. It's not learned because it doesn't need to be — the features carry the class label nearly directly."

## Related
- [[03 - Meta Model Concept]] — why this is rule-based
- [[06 - Feature Engineering]] — the inputs
- [[07 - Binary Estimator]] — the gate
- [[09 - Sister Projects (olive, ginger, snitch)]] — where this is used (mostly snitch)
