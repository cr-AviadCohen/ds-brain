---
tags: [ngav, glossary, reference]
type: glossary
project: ngav-pipeline
---

# Glossary

Domain terms and acronyms used throughout the project. Aim is to flatten them so the rest of the notes can use them freely.

## NGAV-specific

- **NGAV** — Next-Generation Antivirus. Cybereason's static-analysis malware classifier component.
- **stool** — internal Cybereason PE-feature-extraction tool. CLI: `ngav-stool-featuregen`. Outputs `*.index.pkl.pklbz2`.
- **`featuresinfra`** — internal package that defines the actual PE feature schema.
- **`crossguard`** — internal training-core package. `crossguard.train.train` is the actual model-training callable.
- **`protect`** — model export library. `protect.exportmodel` writes `.features.conf` and `.model.conf` for the production scanner.
- **broccoli** — Cybereason's automated VT-based labeller. Has known accuracy issues (see `broccoli_compensator` in `build_dataset.py`). Note: there is also a *separate* "broccoli" subsystem in the [[../virustotalclassifier-meta/00 - Index|virustotalclassifier]] project — same name, different artefact.
- **allowlist** — a curated list of high-confidence-benign SHAs. Used in production to skip scanning known-good files.
- **managed / unmanaged** — managed = .NET PE files (single import: `mscoree.dll`). Unmanaged = native Win32. They get separate models because their feature distributions are very different.

## VirusTotal

- **VT** — VirusTotal.
- **`vhash`** — VT's structural ("variant") file hash. Two files with the same `vhash` are likely from the same family/packer. Capped at 50 copies in any pipeline dataset (`vhash_duplication_allowed`).
- **positives** — number of AV engines (out of ~70) that flagged a file as malicious in a given VT scan.
- **`vt_file_report_feed_1`** — BigQuery table at `vt-feed-pipeline-acfe9f.vt_file_report_feed.vt_file_report_feed_1`. The row source for this whole pipeline.
- **scan_date / first_seen** — sample timestamps used for the temporal sample windows (`timedelta_dict`).

## ML / data

- **AUC** — Area Under the ROC Curve. Threshold-independent ranking-quality metric. The [[06 - Decision Gate]]'s primary metric.
- **FPR** — False Positive Rate.
- **TPR** — True Positive Rate (= recall).
- **operating point / threshold** — the probability cutoff turning `predict_proba` into a decision. Three are picked: aggressive / moderate / cautious. See [[07 - Threshold Optimization]].
- **LightGBM** — gradient-boosted trees library. The model class.
- **scale_pos_weight** — LightGBM's class-imbalance parameter. Set to 1 here because the pipeline pre-balances the dataset to 50/50.
- **time-decay weighting** — sample weighting where newer samples have higher weights. Built but **disabled** today.

## Infra

- **Jenkins** — the orchestrator. Two pipelines: `lin-jenkins-ngav-slave` (Linux) + `ngav-generate-features-windows` (Windows agent).
- **Artifactory** — JFrog. Both PyPI (Python deps) and the model registry. Path: `ngav-pipeline/{files_type}/{model_ID}/`.
- **GCS** — Google Cloud Storage. Bucket `lin-win-ngav` is the data plane between Linux and Windows hosts.
- **BigQuery (BQ)** — used by `build_dataset.py` to query the VT feed.
- **`hanabase`** — internal BigQuery client wrapper.
- **`quicklib`** — internal Python packaging convention. `quicklib_setup.yml` declares the package.

## Pipeline-internal terminology

- **`out_name`** — the prefix used for all stage artefacts in a given run, derived from the model_ID.
- **`is_valuable_model`** — the file written by [[06 - Decision Gate]] to signal whether to upload to the production path.
- **`starting_point`** — Jenkins parameter that lets you restart the pipeline at any stage (for debugging or re-runs).
- **`model_ID`** — `{files_type}_{major}.{minor}_{dd-mm-yyyy}` — the unique identifier of a pipeline run / artefact bundle.

## Cross-reference
- [[../virustotalclassifier-meta/00 - Index|virustotalclassifier]] — sister ML project. Different goal: meta-classify based on *AV-engine consensus*, not PE static features.
