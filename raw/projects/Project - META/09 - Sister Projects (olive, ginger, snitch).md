---
tags: [virustotalclassifier, wrappers, configurations]
type: reference
project: virustotalclassifier-meta
---

# Sister Projects — `olive`, `ginger`, `snitch`

Each of these is a **thin wrapper** around `meta.run()`. The architectural code is in `meta/`; these wrappers just supply different JSON configurations.

## Pattern (every wrapper looks the same)

```python
# virustotalclassifier/<wrapper>/main.py
import json
from virustotalclassifier.meta.run import run, validate_configuration

with open('<wrapper>_configuration.json') as f:
    config = json.load(f)

validate_configuration(config)
run(config)
```

Differences live entirely in the JSON config: `task` (binary or multiclass), referee query, training-dataset query, file types, classes, conditions, thresholds.

## The four wrappers

| Wrapper | File type | Task | Domain notes |
|---|---|---|---|
| **`ginger/main.py`** | Linux ELF binaries | binary | Catches Linux malware. Different VT engine performance profile (some engines are weaker on Linux). |
| **`olive/black_olive/main.py`** | Scripts | binary | Trained to flag malicious scripts (PowerShell, JS, VBA, …). "Black" = malicious. |
| **`olive/green_olive/main.py`** | Scripts | binary | The flip side: trained to identify *benign* scripts confidently. "Green" = harmless. |
| **`snitch/main.py`** | MS Office documents | **multiclass** | Fine-grained: downloader / dropper / exploit / benign. Most complex configuration. |

## Why two olives?
"Black" and "green" olives both classify scripts but with **different objectives**:
- **Black olive** is recall-oriented for malicious — catch every bad script.
- **Green olive** is precision-oriented for benign — confidently bless scripts as harmless (used for allowlisting).

Two models, two thresholds, two operating points — better than one model with two thresholds because the **referee selection** can differ between them. Engines that are good at detecting malicious scripts are not necessarily good at confidently calling something benign.

## Why ginger uses binary, snitch uses multiclass
- **Ginger / olive**: the operational decision is binary — block or allow. No need for sub-typing at the gate.
- **Snitch**: the operational decision is "where does this Office doc fit in the threat taxonomy?" — analysts and downstream automations want the sub-type to drive different responses (rebuild / quarantine / alert).

## Configuration shape (the actual difference between wrappers)
Reusing the schema from [[04 - Meta Pipeline Flow]], the per-wrapper differences are:

| Field | ginger | olive (black/green) | snitch |
|---|---|---|---|
| `task` | binary | binary | **multiclass** |
| referee query: file_types | `['ELF']`-ish | script types | `['MS Excel Spreadsheet', 'Office Open XML Document', ...]` |
| `classes` | n/a | n/a | `['downloader', 'dropper', 'exploit', 'benign']` |
| `classes_tags`, `conditions` | n/a | n/a | populated |
| referee selection | re-runs per file type | re-runs per file type | re-runs per file type |
| Phase 2 | absent | absent | `MetaMultiEstimator` with rules |

## Implication for the codebase
- **Adding a new wrapper** = creating a new directory with a `main.py` and a JSON config. No need to touch `meta/`.
- **Bug fixes in `meta/`** automatically benefit every wrapper.
- This is a **good separation** — domain knowledge lives in JSON, machinery lives in Python.

## Caveat: separate model artefacts
Each wrapper produces its own pickled (dill) pipeline + its own referees + its own training-dataset cache. They don't share state at runtime. So:
- Re-running referee selection for one wrapper doesn't affect others.
- Bumping a hyperparameter in one config doesn't affect others.
- Quality regressions in one wrapper are contained.

## Mental model
> "`meta/` is a framework. `ginger`, `olive`, `snitch` are configuration files dressed as Python entry points. The 'project' is one machine, four uses."

## Related
- [[02 - Architecture - Five Subsystems]]
- [[04 - Meta Pipeline Flow]] — the flow each wrapper kicks off
- [[08 - Multiclass Estimator]] — only `snitch` uses this
