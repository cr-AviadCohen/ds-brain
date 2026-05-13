---
tags: [ngav, pipeline-flow, scripts]
type: reference
project: ngav-pipeline
---

# Pipeline Stages

One paragraph per script in `ngav/pet_ops/pipeline/pipeline_scripts/`. Order matches [[02 - Pipeline Architecture]].

---

## 1. `build_dataset.py` — `DatasetBuilder`
The BigQuery-backed sample picker. Given a date range, sample count, PE type (`Win32 EXE` / `Win32 DLL`) and managed/unmanaged flag, generates a multi-CTE SQL against `vt_file_report_feed_1` and shapes the result into a multi-level DataFrame: `{label, meta, scan}`. Filters samples by imports (managed → exactly `mscoree.dll`; unmanaged → must NOT import it). Caps duplicate `vhash` to **50 copies** per dataset (via `vhash_duplication_allowed`). Includes a `broccoli_compensator()` that **relabels** `(label=benign, positives ≥ 15) → malicious` and **drops** `(label=malicious, positives ≤ 4)` — a workaround for known broccoli-labeller errors.

Key outputs: `vtindex.pkl` (sample metadata), `labels_*.pkl`.

> ⚠ The huge inline BigQuery CTE (~200 lines) is a maintenance hotspot. See [[10 - Technical Debt & Open Issues]].

---

## 2. `create_datasets.py` (orchestrator)
Calls `build_dataset.py` twice: once for EXE, once for DLL. Reads the DLL training count to compensate the EXE target (so the union meets `training_samples_amount`). Disables `--cond-post-bd` for DLL (data scarcity). Then calls `GlobalAllowlistGeneration` to index allowlist candidates, runs the test suite, and uploads to GCS via `store_datasets_in_gcs_bucket()`.

Entry: `python3 -m ngav.pet_ops.pipeline.pipeline_scripts.create_datasets`.

---

## 2b. `create_pipeline_datasets.py` (alternate orchestrator)
Same idea as `create_datasets.py` but with **separate date ranges for train/val vs test** (8 date args). Combines EXE+DLL training into a single dataset via `combine_dll_and_exe_training()`. Used when you want stricter temporal separation.

---

## 3. `generate_features.py` (Windows job, `ngav-generate-features-windows`)
Runs on a Windows Jenkins agent. For each PE type, calls **`ngav-stool-featuregen --single`** three times (EXE dataset, DLL dataset, allowlist pool). Outputs `*.index.pkl.pklbz2` files containing extracted PE static features (entropy, sections, imports, version info, certificates, …). Uploads back to GCS. The `GenerateFeaturesTest` enforces:
- features size ≥ 90% of input dataset (≥ 50% for allowlist pool, since `pe_type` filtering thins it).
- error rate in `*_rest.pklbz2` < 5%.

> The "stool" tool is internal Cybereason — feature definition lives in `featuresinfra`. Treat it as a black box from the pipeline's POV.

---

## 4. `data_preparation.py`
The dataset-cleaning stage. Loads `(features, vtindex)` pairs from GCS and:
1. Fills BitDefender NaN with `0.0` (BD's score is sometimes missing).
2. Drops feature-NaN rows.
3. Calls `crossguard.utils.general.drop_duplicates_pe()` to dedup by **feature vector** (catches repacked binaries).
4. Drops by SHA1 too.
5. Calls `sample_with_distribution()` to enforce **50/50 malicious/benign**.
6. Splits via `split_vtindex()` into training / EXE-validation / EXE-test / DLL-validation / DLL-test.
7. Detects > 15% data loss (logs warning).
8. Computes time-based sample weights via `calculates_weights_time_resolution_based()` (day-resolution, newer samples weighted higher, weights sum to 1.0).

Tested by `DataPreparationTest`: size ≥ 90%, balance in [0.45, 0.55], no NaNs, weight invariants (sum=1±0.001, all 0<w<1, oldest day → minimum weight).

> ⚠ **Live merge conflict in this file** at the weighting block. See [[10 - Technical Debt & Open Issues]].

---

## 5. `train_model.py`
Tiny wrapper that shells out to `python -m crossguard.train.train` with the prepared features + labels. The weights flag is **commented out** in the call site, suggesting the time-decay weighting infrastructure is built but disabled in production today. Tested by `TrainModelTest` (artefact existence). See [[04 - ML Model & Hyperparameters]] for the LightGBM config.

---

## 6. `threshold_optimization.py`
Wraps `python -m model_optimization.threshold_optimization`. Computes three operating thresholds — **aggressive**, **moderate**, **cautious** — for both EXE and DLL on the validation set, plus a precision-recall sweep. Renders TP/FP-rate PDFs and joins them. Heavily tested:
- thresholds ordered: `aggressive ≤ moderate ≤ cautious`
- bands: see `thresholds_valid_values` in [[05 - Configuration Reference]]
- precision must be **monotonically non-decreasing** in threshold (margin `1e-4`).

See [[07 - Threshold Optimization]].

---

## 7. `model_test.py`
Evaluates the trained model on the test sets at all three thresholds, **combined with BitDefender's verdict** (`combine_model_prediction_with_AV()`). Computes precision / recall / FPR. Compares each test metric against the validation target:
- recall ≥ validation_recall − 2pp
- FPR ≤ validation_FPR + 10pp

Logs warnings on mismatch but does **not** halt the pipeline (`exit(1)` is commented out). See [[10 - Technical Debt & Open Issues]].

---

## 8. `generate_allowlist.py`
Loads the model, the **allowlist candidate features**, and the **aggressive threshold**. Splits by PE type, runs `GlobalAllowlistGeneration.create_allowlist()` per type, merges, then **unions with the previous PE-type allowlist** fetched from Artifactory (so the allowlist accumulates trustworthy benigns over time). Outputs `allowlist_final_{out_name}.csv`. Enforced max size: 1500 entries (sanity check).

---

## 9. `decision_gate.py` ★ central QA gate
Loads the **current** model and the **last shipped** model (path inferred by walking one level up in the Artifactory `model_ID` namespace). Runs both on the EXE test set, computes AUC for each via `calc_auc_score_wrapper()`, and:
- writes `is_valuable_model` flag file (`true` / `false`)
- if `curr_auc > last_auc` → continue
- if `curr_auc ≤ last_auc` and `--upload-lower-auc` is **not** set → `exit(1)` (pipeline fails, model is discarded)
- if `--upload-lower-auc` is set, log `is_valuable_model=false` and continue (manual override)

Also logs DLL metrics for traceability. See [[06 - Decision Gate]] for nuances.

---

## 10. `model_extraction.py`
Calls `python -m protect.exportmodel` (NGAV-internal serializer) to produce `.features.conf` and `.model.conf` from the pickled LightGBM. Aggregates accumulated `error_messages_*.txt` into PDFs and merges them into the report. Tested by `ModelExtractionTest`: both `.conf` files must exist.

---

## Cross-stage utilities

### `utils/pipeline_utils.py`
- `pred_by_threshold(model, X, thr)` — apply a probability threshold to `predict_proba`.
- `calc_malicious_proba(df)` — extract the "malicious" column.
- `is_df_size_roughly_as_expected(actual, expected, error_margin)` — used by every test gate.
- `is_classification_distribution_balanced(df)` — checks 45–55% per `configuration.malicious_benign_distribution_min`.

### `utils/gcp_bucket_utils.py`
Hardcoded bucket: `lin-win-ngav`. OS-aware credential paths:
- Windows: `C:/users/admin/pipeline_creds/gcs_bucket_credentials.json`
- Linux: `/opt/jenkins/workspace/ngav-model-generator/research/ngav/pet_ops/pipeline/utils/gcs_bucket_credentials.json`

Functions: `store_datasets_in_gcs_bucket`, `fetch_features_from_gcp_bucket`, `store_features_in_gcp_bucket`, `fetch_datasets_from_gcs_bucket`.

---

## Related
- [[02 - Pipeline Architecture]] — the diagram
- [[09 - Testing Strategy]] — the test gates per stage
