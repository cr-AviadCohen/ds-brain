---
tags: [virustotalclassifier, pipeline-flow, meta]
type: reference
project: virustotalclassifier-meta
---

# Meta Pipeline Flow

The end-to-end data flow inside `virustotalclassifier/meta/`. This is the recipe; per-file detail lives in [[06 - Feature Engineering]], [[07 - Binary Estimator]], [[08 - Multiclass Estimator]].

## High-level

```
   build_dataset.py ─► vtreferees.py ─► train.py ─► estimator.py ─► classify.py / eval.py
        │                  │              │              │
        │                  │              │              └── persisted as dill pipeline
        │                  │              │
        │                  │              └── builds sklearn pipeline (Phase 1 + optional Phase 2)
        │                  │
        │                  └── selects top AV engines as referees (F-β, β=0.5)
        │
        └── pulls samples from BigQuery (vt_file_report_feed_1)
```

## Stages in detail

### 1. `build_dataset.py` — sample selection
Three `DatasetBuilder` subclasses, each producing a DataFrame indexed by `sha1` with columns: `scans` (list of dicts), `tags`, `positives`, `scan_date`, `type`, `vhash`.

| Builder | Strategy | Used for |
|---|---|---|
| `RefereesDatasetBuilder` | "back to the future" — samples where `min_positives ≤ 2` at first scan and `max_positives ≥ 8` at last scan, with a `detections_increased` flag indicating real detection growth | training the referee selector |
| `TrainingDatasetBuilder` | random samples with `positives > 1`, stratified by file type | training the classifier itself |
| `EvaluationDatasetBuilder` | latest scans of specific SHAs or in a date range | evaluation |

Why "back to the future"? Real malware is typically **first undetected** (zero-day-ish) and **later detected by many engines**. Training the referee selector on these samples teaches "which engines are best at *eventually* catching real malware" — i.e. the engines whose detections track real maliciousness, not random noise.

The `detections_increased` boolean flag distinguishes "engines genuinely learned to detect this" from "engines noisily flipped".

All builders share a SQL backbone targeting `vt-feed-pipeline-acfe9f.vt_file_report_feed.vt_file_report_feed_1`. Queries are decorated with `@mark_as_query` and registered via `@query_registrar_class` (see `meta/utils.py`) so they can be looked up by name from the configuration JSON.

### 2. `vtreferees.py` — pick the level-0 engines
Class: `VirusTotalReferees`. Given the back-to-future dataset, computes per-engine TP/FP/precision/recall and selects engines in the **top 10% by F_β=0.5 score** (minimum 10 engines). Bias toward precision: F_0.5 weights precision 2× recall.

Engine grouping (`group_names_mapper`) merges echoes (e.g. `"K7_GW_Security"` and similar) so duplicates don't get separate votes.

Output: a list of referee engine names, persisted (cached) to avoid recomputation.

Detail in [[05 - Referee Selection]].

### 3. `train.py` — fit the pipeline
Class: `MetaTrainer`. Builds an sklearn `Pipeline` based on `task` from the configuration:

#### Binary task
```python
Pipeline([
    ('verdict_transformer', VerdictTransformer(extracted_value='detected', fillna=False)),
    ('estimator', MetaBinaryEstimator(configuration=config)),
])
```
- `VerdictTransformer` → binary matrix `samples × engines` (True = detected).
- `MetaBinaryEstimator` → wraps `VirusTotalAnalyzer`, learns threshold, applies 3-zone rule. See [[07 - Binary Estimator]].

#### Multiclass task
```python
SampleSplitter([
    ("tags_tokens_pipeline",
       Pipeline([
           DataFrameMapper([
               (['tags'],  TagsTransformer()),
               (['scans'], VerdictTransformer(...) + EnginesTokensTransformer(...)),
           ]),
           MetaMultiEstimator(configuration=config)
       ])),
    ("dummy_estimator", ConstantEstimator(constant="benign")),
])
```
The `SampleSplitter` routes:
- samples the binary phase already labelled `benign` → `ConstantEstimator("benign")`.
- samples labelled `malicious` → the rule-based multiclass.

Whole thing serialised with `dill` (handles closures and lambdas that `pickle` can't).

### 4. `estimator.py` — the actual decision-making
Two estimator classes:
- `MetaBinaryEstimator` — see [[07 - Binary Estimator]].
- `MetaMultiEstimator` — see [[08 - Multiclass Estimator]].

### 5. `classify.py` — runtime entry
`VirusTotalSnitchDocumentsClassifier` (despite the name, used beyond snitch) loads the dill pipeline, deduplicates samples by index (sha1), and calls `predict()`.

Optional: `predict_proba()` exists for binary; **NotImplementedError** for multiclass (since the multi phase is rule-based).

### 6. `eval.py` — measure performance
`MetaMSEvaluation` pulls a test dataset (via `EvaluationDatasetBuilder`), runs `predict`, computes precision / recall / F1 (per class for multiclass). Supports multi-threshold evaluation.

### 7. `run.py` — top-level orchestrator
The `run(configuration)` function:
1. `validate_configuration(configuration)` — ensures required keys.
2. Loads referees from cache OR computes them (calls `vtreferees`).
3. Loads training dataset from cache OR queries BigQuery (calls `build_dataset`).
4. Calls `MetaTrainer.fit()`.
5. Logs metadata to MLflow (optional, controlled by `configuration['mlflow']`).
6. Optionally runs `MetaMSEvaluation` on a test set.
7. Calls `build_prod_config()` to serialise model metadata for production consumption.

This is the function each wrapper (`ginger`, `olive/*`, `snitch`) ultimately calls.

## Caching
Both referees and the training dataset are cached on disk between runs. This matters because:
- The "back to the future" referee query is heavy (multi-CTE BigQuery scan).
- The training-dataset query can pull millions of rows.

Cache invalidation is by parameters in the JSON config (date ranges, file type filters, minimum positives).

## Configuration shape (what `run.py` expects)
```json
{
  "task": "binary" | "multiclass",
  "version": "...",
  "model_name": "...",
  "output_path": "...",
  "mlflow": {...},
  "referees_configuration": {
     "build_dataset_query": "...",
     "min_positives": 2,
     "max_positives": 8,
     ...
  },
  "train_dataset_builder_configuration": {
     "build_dataset_query": "...",
     "training_dates_range": [...],
     "file_types": [...]
  },
  "estimator_configuration": {
     "min_positives_detection": 3,
     "max_positives_detection": 8,
     ...
  },
  // multiclass only:
  "classes": ["downloader", "dropper", "exploit"],
  "classes_tags": {...},
  "conditions": [...],
  "test_settings": {...}
}
```

## Related
- [[03 - Meta Model Concept]] — the central idea
- [[05 - Referee Selection]] — the referee picker
- [[06 - Feature Engineering]] — the transformers
- [[07 - Binary Estimator]] / [[08 - Multiclass Estimator]] — the two phases
- [[11 - Data Sources]]
