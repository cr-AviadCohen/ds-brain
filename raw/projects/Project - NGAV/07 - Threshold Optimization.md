---
tags: [ngav, threshold, operating-points]
type: note
project: ngav-pipeline
---

# Threshold Optimization

## What & why
The LightGBM model in [[04 - ML Model & Hyperparameters]] outputs a probability `P(malicious | features)`. To turn that into a decision, the pipeline picks **three operating thresholds** per PE type:

| Threshold | Meaning | Used for |
|---|---|---|
| **aggressive** | flag at low probability — high recall, high FPR | **allowlist generation** (we want to be sure something is *probably-benign*) |
| **moderate** | the "default" balanced operating point | possible production verdict tier |
| **cautious** | flag only at high probability — high precision, low FPR | strict production verdict tier (auto-block on malicious calls) |

These are picked on the **validation** set, then sanity-checked on the **test** set in [[03 - Pipeline Stages|model_test.py]].

## How they're picked
`pipeline_scripts/threshold_optimization.py` shells out to `python -m model_optimization.threshold_optimization` (external module). The optimizer:
1. Sweeps thresholds across `[0, 1]`.
2. For each, computes precision, recall, FPR.
3. Picks the three thresholds that hit **target operational points** (the thresholds_valid_values bands).
4. Renders TP/FP curves to PDF.

Outputs: `thresholds_{out_name}_{exe,dll}.pkl` — a dict like `{aggressive: 0.42, moderate: 0.78, cautious: 0.97}`.

## Validity bands (`configuration.thresholds_valid_values`)

```python
{
  'exe': { min_cautious: 0.95, min_moderate: 0.5, max_moderate: 0.9, min_aggressive: 0.2, max_aggressive: 0.55 },
  'dll': { min_cautious: 0.98, min_moderate: 0.9, max_moderate: 1.0, min_aggressive: 0.5, max_aggressive: 0.8 },
}
```

These bands are **enforced** by `ThresholdOptimizationTest`:
- `aggressive ≤ moderate ≤ cautious` (ordering)
- `cautious ≥ min_cautious`
- `min_aggressive ≤ aggressive ≤ max_aggressive`
- `min_moderate ≤ moderate ≤ max_moderate`
- precision is monotonically non-decreasing (margin `1e-4`)

If any check fails, the test stage logs and the pipeline halts.

## Why DLL bands are stricter
Pattern across the bands: **DLL minimums are higher**.

| | EXE | DLL |
|---|---|---|
| `min_cautious` | 0.95 | **0.98** |
| `min_aggressive` | 0.2 | **0.5** |
| `min_moderate` | 0.5 | **0.9** |

Two interpretations:
1. **Operational asymmetry.** A false positive on a DLL is more disruptive (whatever loads it breaks). The cost of a wrong "malicious" call is higher → demand higher confidence.
2. **Prior asymmetry.** DLLs are more often legitimately signed and benign. The base rate of "actually malicious" given a flagged DLL is lower → require stronger model evidence.

Both are real; the DLL bands encode both.

## Why precision must be monotonic
A sane probabilistic classifier should yield: as `threshold ↑`, precision ↑ (you're picking only the model's most confident predictions). Non-monotonicity ⇒ either:
- the validation set is too small / unstable,
- the model is poorly calibrated,
- there's a label noise pocket,
- something is wrong upstream (dedup, balance).

The monotonicity test is a **sanity gate** more than an operational requirement.

## How thresholds connect to other stages
- **`generate_allowlist.py`** → uses **aggressive** threshold to generate the malicious-flag-list, then **inverts** that to define the allowlist among benign-pool candidates. The aggressive threshold being low means "anything we even *suspect* might be malicious is excluded from the allowlist" — defensive default.
- **`model_test.py`** → evaluates at all three thresholds on the test set, compares to validation targets.
- Production scanner → consumes thresholds from `thresholds_*.pkl` exported via `protect.exportmodel`.

## How to change a band
1. Edit `configuration.thresholds_valid_values`.
2. Re-run the pipeline from `threshold_optimization` (use Jenkins `starting_point=threshold_optimization`).
3. Watch the [[06 - Decision Gate]] — band changes don't directly affect AUC, but if you simultaneously change training, the gate is still load-bearing.

## Related
- [[03 - Pipeline Stages]] — context.
- [[05 - Configuration Reference]] — the constants.
- [[06 - Decision Gate]] — orthogonal but adjacent QA.
