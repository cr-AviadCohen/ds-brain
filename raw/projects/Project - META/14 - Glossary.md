---
tags: [virustotalclassifier, glossary]
type: glossary
project: virustotalclassifier-meta
---

# Glossary

## Project-specific

- **meta model** — a classifier whose features are other classifiers' outputs. In this codebase: a model over AV-engine verdicts. See [[03 - Meta Model Concept]].
- **referee** — an AV engine selected (by F_β=0.5) as a trusted voter. See [[05 - Referee Selection]].
- **echo / echo grouping** — when multiple AV engines emit identical verdicts because they license each other's signatures. The system clusters them and counts as one vote.
- **back to the future** — a sample-selection strategy: pick samples that started undetected and later became widely detected, to capture real-malware-emergence signal. Used to label data for referee selection.
- **3-zone rule** — the binary estimator's decision: low-detection → benign, high-detection → malicious, mid → use the model. Boundaries default to `≤ 3` and `≥ 8`.
- **broccoli** — the older subsystem in this repo. KNN over Annoy index. (Different "broccoli" than the labeller mentioned in [[../ngav-pipeline/11 - Glossary|ngav-pipeline/11 - Glossary]].)
- **olive (black/green)** — the meta wrappers for scripts. Black = malicious-recall. Green = benign-precision.
- **ginger** — the meta wrapper for Linux ELF binaries.
- **snitch** — the meta wrapper for MS Office documents (multiclass).

## VirusTotal terms

- **VT** — VirusTotal.
- **scans** — the per-engine verdict list inside a VT report. List of dicts: `{name, detected, result}`.
- **positives** — number of engines reporting detection on a given scan.
- **`vhash`** — VT's structural / variant hash. Files with the same `vhash` are likely from the same packer/family.
- **tags** — VT-curated labels on a sample (`cve-2022-12345`, `macros`, `powershell`, …).
- **`vt_file_report_feed_1`** — the BigQuery table the meta system reads from.
- **`vt_files_scans`** — the legacy MySQL table broccoli reads from.
- **VT v2** — the older VT API; raw responses cached as MsgPack files.

## ML terms

- **stacking** — using the outputs of base classifiers as inputs to a higher-level classifier. The pattern this whole project uses.
- **F_β** — `F = (1+β²) · prec · rec / (β² · prec + rec)`. β > 1 emphasises recall, β < 1 emphasises precision. The system uses β = 0.5.
- **softmax** — exponential normalisation across classes; sum to 1.
- **TF-IDF** — Term Frequency × Inverse Document Frequency, classic text feature.
- **ManyHotEncoder** — multi-label one-hot for tag sets.
- **Annoy** — Spotify's Approximate Nearest Neighbour library. Trades exactness for speed.
- **KNN** — K-Nearest Neighbours classifier.
- **TruncatedSVD** — sparse-friendly SVD for dimensionality reduction.

## Internal Cybereason packages

- **`vtutils`** — provides `VirusTotalAnalyzer`, the load-bearing engine-clustering / referee-weighting logic.
- **`hanabase`** — internal BigQuery client.
- **`innovationdb`** — internal MySQL ORM.
- **`sklearn_extras`** — internal sklearn add-ons: `DataFrameMapper`, `SampleSplitter`, `NearestNeighborsAnnoy`, etc.
- **`pandas_extras`** — `pdload` / `pddump` (typed pickle), `drop_duplicates_by_index`.
- **`featuresinfra`** — feature schema layer used by broccoli.
- **`cyberlib`** — generic Cybereason utilities.
- **`quicklib`** — internal Python packaging convention. `quicklib_setup.yml` declares the package.

## File / module names you'll see often

- **`run.py`** — `meta/run.py`, the top-level orchestrator each wrapper calls.
- **`build_dataset.py`** — `meta/build_dataset.py`, the BigQuery sample picker (3 builder classes).
- **`vtreferees.py`** — referee selection.
- **`features_transformers.py`** — `VerdictTransformer`, `EnginesTokensTransformer`, `TagsTransformer`.
- **`estimator.py`** — `MetaBinaryEstimator`, `MetaMultiEstimator`.
- **`rules.py`** — multiclass rule primitives.
- **`global_vars.py`** — runtime config bag (mutable; see [[13 - Technical Debt & Observations]]).

## Cross-project link
- [[../ngav-pipeline/00 - Index|NGAV pipeline]] — sister project. PE static features, LightGBM, production scanner. Uses different signal entirely.
