---
tags: [ngav, architecture, pipeline-flow]
type: note
project: ngav-pipeline
---

# Pipeline Architecture

This is the canonical end-to-end flow. Each box is a Jenkins stage backed by one of the scripts in `pipeline_scripts/`. Detailed per-stage commentary lives in [[03 - Pipeline Stages]].

## End-to-end data flow

```
            ┌──────────────────────────────────────┐
            │   Jenkinsfile (lin-jenkins-ngav)     │
            │   inputs: files_type, dates, count   │
            └────────────────────┬─────────────────┘
                                 │
                                 ▼
                ┌──────────────────────────────┐
                │   create_datasets.py         │   ← BigQuery (vt_file_report_feed_1)
                │   - calls build_dataset.py   │
                │   - one EXE pass, one DLL    │
                │   - splits train/val/test    │
                └────────────┬─────────────────┘
                             │ vtindex.pkl, labels_*.pkl
                             ▼
                  GCS  lin-win-ngav  (datasets)
                             │
                             ▼
                ┌──────────────────────────────┐
                │   generate_features.py       │   ← Windows job
                │   ngav-stool-featuregen      │   ← runs PE static analysis
                └────────────┬─────────────────┘
                             │ *_dataset_{exe,dll}.index.pkl.pklbz2
                             ▼
                  GCS  lin-win-ngav  (features)
                             │
                             ▼
                ┌──────────────────────────────┐
                │   data_preparation.py        │
                │   - drop NaNs / duplicates   │
                │   - enforce 50/50 balance    │
                │   - time-based weights       │
                └────────────┬─────────────────┘
                             │ training/validation/test pkls
                             ▼
                ┌──────────────────────────────┐
                │   train_model.py             │   ← crossguard.train.train
                │   LightGBM 300 trees         │
                └────────────┬─────────────────┘
                             │ {out_name}_model.classifier.pkl
                             ▼
                ┌──────────────────────────────┐
                │   threshold_optimization.py  │   ← model_optimization module
                │   aggressive/moderate/       │
                │   cautious thresholds        │
                └────────────┬─────────────────┘
                             │ thresholds_*.pkl + PDFs
                             ▼
                ┌──────────────────────────────┐
                │   model_test.py              │
                │   evaluate test vs targets   │
                │   combine with BitDefender   │
                └────────────┬─────────────────┘
                             │ metrics_*.pkl
                             ▼
                ┌──────────────────────────────┐
                │   generate_allowlist.py      │
                │   uses aggressive threshold  │
                │   merges with prev allowlist │
                └────────────┬─────────────────┘
                             │ allowlist_final_*.csv
                             ▼
                ┌──────────────────────────────┐
                │   decision_gate.py           │   ← compares EXE test-AUC
                │   curr_AUC vs last_AUC       │     against previous model
                │   exit(1) if regressed       │
                └────────────┬─────────────────┘
                             │ is_valuable_model file
                             ▼
                ┌──────────────────────────────┐
                │   model_extraction.py        │   ← protect.exportmodel
                │   .features.conf .model.conf │
                └────────────┬─────────────────┘
                             │
                             ▼
            ┌──────────────────────────────────────┐
            │   Artifactory upload (curl + token)  │
            │   ngav-pipeline/{type}/{model_ID}/   │
            └──────────────────────────────────────┘
```

## The two-host story

The pipeline is split because **PE feature extraction must run on Windows**:

```
  Linux job (Docker)              Windows job
  ─────────────────              ─────────────
  create_datasets ──── GCS ────► generate_features
                                       │
  data_preparation  ◄─── GCS ──────────┘
       │
       ▼
  train_model ▶ threshold_opt ▶ model_test ▶ ...
```

GCS bucket `lin-win-ngav` is the **handoff buffer** between the two hosts.

## Stages, in dependency order

| # | Script | What it produces | Test gate |
|---|--------|------------------|-----------|
| 1 | `create_datasets.py` | `vtindex.pkl`, `labels_*.pkl` | `CreateDatasetsTest` (size ≥ 95%) |
| 2 | `generate_features.py` (Win) | `*.index.pkl.pklbz2` | `GenerateFeaturesTest` (size ≥ 90%, errors < 5%) |
| 3 | `data_preparation.py` | training/val/test pkls + weights | `DataPreparationTest` (size, balance, NaN, weights) |
| 4 | `train_model.py` | `*_model.classifier.pkl` | `TrainModelTest` (artefact exists) |
| 5 | `threshold_optimization.py` | `thresholds_*.pkl` + PDFs | `ThresholdOptimizationTest` (order, bounds, monotonic precision) |
| 6 | `model_test.py` | `metrics_*.pkl` | (logs warnings, doesn't halt — see [[10 - Technical Debt & Open Issues]]) |
| 7 | `generate_allowlist.py` | `allowlist_final_*.csv` | `GenerateAllowlistTest` (size < 1500) |
| 8 | `decision_gate.py` | `is_valuable_model` flag | the gate itself — exits 1 if regressed |
| 9 | `model_extraction.py` | `.features.conf`, `.model.conf` | `ModelExtractionTest` (both files exist) |

## What "production" eats
The artefacts that actually leave this pipeline and end up in the NGAV scanner binary are:
- `*.features.conf` — feature-extraction config the C++ scanner uses.
- `*.model.conf` — the serialized LightGBM tree ensemble.
- `thresholds_*.pkl` — the operating-point thresholds.
- `allowlist_final_*.csv` — the SHA list of confirmed-benign samples.

Everything else (raw datasets, intermediate features, PDFs) is for traceability / debugging.

## Related
- [[03 - Pipeline Stages]] — one paragraph per script
- [[06 - Decision Gate]] — the model promotion gate
- [[08 - Infrastructure & Deployment]] — Jenkins + Docker + GCS specifics
