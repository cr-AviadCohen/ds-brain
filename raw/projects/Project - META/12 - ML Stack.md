---
tags: [virustotalclassifier, dependencies, ml-stack]
type: reference
project: virustotalclassifier-meta
---

# ML Stack

Dependencies and architectural choices behind them. Source of truth: `virustotalclassifier/quicklib_setup.yml`.

## Core (always installed)

| Package | Version | Used for |
|---|---|---|
| `pandas` | ≥ 0.25 | DataFrame manipulation everywhere |
| `numpy` | (any) | numerical |
| `scikit-learn` | ≥ 0.20.2 | `Pipeline`, estimators, transformers |
| `scipy` | ≥ 0.19.0 | sparse matrices for TF-IDF, etc. |
| `decorator` | ~= 4.0 | for the `@mark_as_query` registry |
| `dill` | == 0.2.6 | serialise pipelines (handles closures `pickle` can't) |
| `attrs` | == 18.2.0 | typed attribute classes |
| `cytoolz` | (any) | functional utilities |
| `joblib` | (any) | parallelisation |

## "Full" extras (broccoli + Annoy KNN)

| Package | Version | Used for |
|---|---|---|
| `annoy` | == 1.9.1 | Approximate Nearest Neighbour index in broccoli |
| (newer sklearn / scipy versions, sometimes pinned) | | |

## Internal Cybereason packages

These come from JFrog Artifactory's PyPI. They carry significant logic:

| Package | What it provides |
|---|---|
| `cyberlib` | general utilities, logging, config loaders |
| `sklearn_extras` | `DataFrameMapper`, `SampleSplitter`, `NearestNeighborsAnnoy`, `YeoJohnsonTransformer`, `ConstantEstimator` |
| `pandas_extras` | `pdload` / `pddump` (typed pickle), `drop_duplicates_by_index` |
| `featuresinfra` | `FeatureMaker`, `FeatureType` (broccoli's feature schema) |
| `vtutils` | **`VirusTotalAnalyzer`**, `AVWeights` — the engine-clustering and weighting logic the binary estimator wraps |
| `hanabase` | BigQuery client |
| `innovationdb` | InnoDB / MySQL ORM (broccoli only) |

**`vtutils` is the most load-bearing** — `VirusTotalAnalyzer` is the secret sauce that makes the binary estimator work. It's not in this repo; it's a black box from a meta-system perspective.

## Optional: MLflow
`mlflow_extras` for experiment tracking. Controlled by `configuration['mlflow']` — when on, `meta/run.py` logs hyperparameters, metrics, and artefacts to an MLflow server.

## What's notably absent

- **No TensorFlow / PyTorch / DL libraries.** This is a classical ML codebase, by design.
- **No XGBoost / LightGBM** in `meta/` (compare to [[../ngav-pipeline/04 - ML Model & Hyperparameters|ngav-pipeline]] which is LightGBM-centric).
- **No deep feature embeddings.** All features are hand-crafted or simple statistical (TF-IDF, softmax over counts).

## Why this stack
- **sklearn pipelines** make the architecture introspectable and serialisable.
- **`dill` over `pickle`** because the pipeline includes closures (e.g. lambda comparators in `SampleSplitter`).
- **Annoy** because for KNN at scale, exact KNN is too slow.
- **Heavy reliance on internal libs** because Cybereason has its own opinionated tooling (`hanabase` for BigQuery, `featuresinfra` for feature schemas, `sklearn_extras` for shared transformers).

## Reproducibility footguns
- `dill==0.2.6` is **very old** — modern Python may have compatibility issues. Pickled pipelines from this era may not load in newer envs without a compatible `dill`.
- Internal packages are pinned by JFrog version; their internal API can shift. A working pipeline locked to specific internal versions is a "fossil" — try to resurrect carefully.
- sklearn 0.20+ is fine but the API has evolved; some classes (`DataFrameMapper`) come from sklearn-pandas-style packages, not core sklearn.

## Mental model
> "Classical sklearn project, with most of the serious logic delegated to internal Cybereason libraries. The repo is the orchestration layer, not the algorithmic layer."

## Related
- [[02 - Architecture - Five Subsystems]]
- [[07 - Binary Estimator]] — wraps `VirusTotalAnalyzer` from `vtutils`
- [[14 - Glossary]] — quick definitions
