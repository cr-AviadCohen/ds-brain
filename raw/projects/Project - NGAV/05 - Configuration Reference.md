---
tags: [ngav, configuration, reference]
type: reference
project: ngav-pipeline
---

# Configuration Reference

The single source of truth for the pipeline's "knobs" is **`ngav/pet_ops/pipeline/configuration.py`**. Treat it as the project's constitution — every other script imports from here.

## The constants

### Dataset taxonomy
```python
datasets_types = ["training", "dll_validation", "dll_test", "exe_validation", "exe_test"]
```
Five named datasets per pipeline run. `training` is unified across PE types; validation/test are PE-type-specific.

### Date windows (`timedelta_dict`)
```python
{
  'unmanaged': {'exe_start_date': 13, 'exe_end_date': 0, 'dll_start_date': 24, 'dll_end_date': 0},
  'managed':   {'exe_start_date': 13, 'exe_end_date': 0, 'dll_start_date': 24, 'dll_end_date': 0},
}
```
"Days back from today" sampling windows. **DLL needs ~2× the window** to hit sample-count targets — DLLs are scarcer in the VT feed.

### Sample-count targets
```python
validation_amount_of_samples = {
  'unmanaged': {'Win32 EXE': 40000, 'Win32 DLL': 40000},
  'managed':   {'Win32 EXE': 40000, 'Win32 DLL': 30000},
}
test_amount_of_samples = { ...same shape... }
```
40k / 30k per PE type.

### Training-set minimums
```python
minimal_training_total_amount_of_samples = {
  'unmanaged': 1_000_000,
  'managed':     500_000,
}
training_samples_relative_partition = {  # 50/50 EXE/DLL
  'unmanaged': {'Win32 EXE': 0.5, 'Win32 DLL': 0.5},
  'managed':   {'Win32 EXE': 0.5, 'Win32 DLL': 0.5},
}
safety_extra_samples = {'unmanaged': 1.5, 'managed': 1.5}  # over-fetch ratio
```
Pipeline always over-fetches by 50% to compensate for downstream dropouts (NaN, dedup, distribution rebalance).

### Deduplication
```python
vhash_duplication_allowed = 50
```
Cap any one `vhash` to ≤50 copies. **VirusTotal's `vhash` is a structural family hash** — without this cap, a single packer family could dominate the dataset. (See [[11 - Glossary]].)

### Distribution check
```python
malicious_benign_distribution_min = 0.45  # ⇒ acceptable band [0.45, 0.55]
```
Used by `is_classification_distribution_balanced()`. The dataset must be 45–55% malicious or `DataPreparationTest.test_classification_distribution` fails.

### Precision monotonicity
```python
precision_monotonic_increasing_error_margin = 0.0001
```
Allowed slack when verifying that `precision(threshold)` is non-decreasing in `threshold`.

### Threshold validity bands ★ critical
```python
thresholds_valid_values = {
  'exe': {
    'min_cautious':   0.95,
    'min_moderate':   0.5,    'max_moderate':   0.9,
    'min_aggressive': 0.2,    'max_aggressive': 0.55,
  },
  'dll': {
    'min_cautious':   0.98,
    'min_moderate':   0.9,    'max_moderate':   1.0,
    'min_aggressive': 0.5,    'max_aggressive': 0.8,
  },
}
```

The interpretation is critical — see [[07 - Threshold Optimization]]:
- **DLL bars are stricter** than EXE bars across the board (cautious 0.98 vs 0.95, aggressive ≥ 0.5 vs ≥ 0.2). Reflects: (a) DLL false positives are operationally worse (a wrongly flagged DLL takes down whatever loads it) and (b) DLLs are more often signed/legit so the prior on "benign" is higher.
- An aggressive threshold of 0.2 for EXE means **anything with ≥20% malicious probability is flagged** — used for allowlist generation, not for production scanning.

### Sizing tolerances (constants used by tests)
- `df_size_criteria = 0.95` — `CreateDatasetsTest`
- `0.9` — `DataPreparationTest`, `GenerateFeaturesTest` (datasets)
- `0.5` — `GenerateFeaturesTest` (allowlist pool, since `pe_type` filtering thins it)
- `0.05` — error-rate ceiling for `_rest.pklbz2`

## Where each constant gets read

| Constant | Read by |
|---|---|
| `datasets_types` | `data_preparation.py`, all test files |
| `timedelta_dict` | `create_datasets.py` (default date offsets) |
| `validation_amount_of_samples`, `test_amount_of_samples` | `create_datasets.py` |
| `minimal_training_total_amount_of_samples` | `create_datasets.py` (minimum check) |
| `training_samples_relative_partition` | `create_datasets.py` (EXE/DLL split) |
| `safety_extra_samples` | `build_dataset.py` (over-fetch multiplier) |
| `vhash_duplication_allowed` | `build_dataset.py` (sql vhash cap) |
| `malicious_benign_distribution_min` | `pipeline_utils.is_classification_distribution_balanced` |
| `thresholds_valid_values` | `test_threshold_optimization.py` |
| `precision_monotonic_increasing_error_margin` | `test_threshold_optimization.py` |

## How to safely change a value
1. Read [[09 - Testing Strategy]] to know which gate currently enforces this constant.
2. Re-run the pipeline with `--starting_point` set far enough back to regenerate dependent artefacts.
3. Decision gate ([[06 - Decision Gate]]) will catch performance regressions automatically.

## Related
- [[03 - Pipeline Stages]] — where these knobs are read.
- [[09 - Testing Strategy]] — what enforces them.
- [[07 - Threshold Optimization]] — `thresholds_valid_values` deep dive.
