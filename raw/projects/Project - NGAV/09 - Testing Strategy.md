---
tags: [ngav, testing, qa]
type: reference
project: ngav-pipeline
---

# Testing Strategy

The pipeline ships **inline test gates** between stages. Tests are not just for CI — they are the contract that data is "fit" to flow to the next stage. Failures aggregate into per-PE-type `error_messages_{exe,dll}.txt` files that get rendered into the final PDF report in `model_extraction`.

## Test pattern
Tests inherit from `ParametrizedTestCase` and are run via `unittest.TestSuite` + `TextTestRunner`. Each stage's test is **co-located** with its script under `pipeline/tests/`.

## Tests by stage

### `CreateDatasetsTest` — `tests/test_create_dataset.py`
- `test_df_size`: vtindex size ≥ `0.95 * expected_size` (i.e. ≤5% loss tolerated at sampling).

### `GenerateFeaturesTest` — `tests/test_generate_features.py`
- `test_size`:
  - For datasets: features-row-count ≥ 90% of input dataset.
  - For the allowlist pool: ≥ 50% (slack because the `pe_type` filter thins it).
- `test_error_rate_in_rest`: error rate in `*_rest.pklbz2` < 5%.

### `DataPreparationTest` — `tests/test_data_preparation.py`
- `test_df_size`: features ≥ 90% of expected.
- `test_classification_distribution`: malicious ratio ∈ `[0.45, 0.55]` (per `configuration.malicious_benign_distribution_min`).
- `test_nans`: zero NaN values in features.
- `test_training_weights`: only when training-weights present, validates:
  - `|sum(weights) - 1.0| < 0.001`
  - `min(weights) < max(weights)`
  - the **earliest day has the minimum weight** (time decay direction is correct)
  - all weights strictly in `(0, 1)`.

### `TrainModelTest` — `tests/test_train_model.py`
- `test_artifacts`: `{out_name}_model.classifier.pkl` exists.
- (Doesn't validate model behaviour — that's the [[06 - Decision Gate]]'s job.)

### `ThresholdOptimizationTest` — `tests/test_threshold_optimization.py`
The richest test suite. Enforces:
- `test_thresholds_order`: `aggressive ≤ moderate ≤ cautious`.
- `test_cautious_value`: `cautious ≥ thresholds_valid_values[pe_type]['min_cautious']`.
- `test_aggressive_value`: `min_aggressive ≤ aggressive ≤ max_aggressive`.
- `test_moderate_value`: `min_moderate ≤ moderate ≤ max_moderate`.
- `test_is_precision_monotonic_increasing`: precision non-decreasing in threshold (margin `1e-4`).

### `GenerateAllowlistTest` — `tests/test_generate_allowlist.py`
- `test_artifacts`: `allowlist_final_{out_name}.csv` exists.
- `test_size`: < 1500 entries (sanity ceiling).

### `ModelExtractionTest` — `tests/test_model_extraction.py`
- `test_features_artifact`: `{out_name}.features.conf` exists.
- `test_model_artifact`: `{out_name}.model.conf` exists.

## What is **not** tested (but probably should be)
- **`model_test.py` outcomes don't fail the pipeline** — recall/FPR mismatches are logged but the `exit(1)` is commented out.
- **DLL is never gated**. AUC gate uses EXE only (see [[06 - Decision Gate]]).
- **No drift test on the feature distribution** between runs — a major distribution shift would silently degrade the model.
- **No leakage check** between training-window and test-window dates.

See [[10 - Technical Debt & Open Issues]] for more.

## Where test failures surface
1. Per-stage `*.txt` error message files are written.
2. They're converted to PDFs in `model_extraction` and **merged** into the final report.
3. `show_test_res_status()` summarises pass/fail at the end of each stage.
4. Critical stages (`ThresholdOptimizationTest`, `GenerateFeaturesTest`, etc.) cause the Jenkins stage itself to fail and halt the pipeline.

## Adding a new test
1. Add a method to the relevant `tests/test_*.py` file.
2. Use `is_df_size_roughly_as_expected()` from `pipeline_utils.py` for size checks (consistent with the others).
3. Append to the relevant `error_messages_*.txt` on failure.
4. If it should halt the pipeline, raise / `exit(1)`. If it's advisory, log and continue (today's pattern for `model_test.py`).

## Mental model
> "Tests are validation gates between data-flow stages. Most halt the pipeline; a few are advisory. Failure messages are aggregated into the PDF report so the final artefact is self-documenting."

## Related
- [[03 - Pipeline Stages]]
- [[05 - Configuration Reference]] — the constants tests enforce.
- [[06 - Decision Gate]] — the model-quality gate (separate from these data-quality gates).
