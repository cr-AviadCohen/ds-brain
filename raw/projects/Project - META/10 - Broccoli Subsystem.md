---
tags: [virustotalclassifier, broccoli, knn, annoy]
type: reference
project: virustotalclassifier-meta
---

# Broccoli Subsystem

The "other lineage" inside `virustotalclassifier`. Pre-dates the meta system; uses a different ML approach.

Module: `virustotalclassifier/broccoli/`.

## Big idea
Instead of meta-learning over AV-engine verdicts (the meta system's approach), broccoli builds **hand-crafted features** from VT reports and classifies via **K-nearest-neighbours over an Annoy index**. Pure similarity-based classification.

If the meta system is "learn from the panel of voters", broccoli is "find the closest known samples and copy their label".

## Architecture

```
                       VT report rows
                              │
                              ▼
                  ┌────────────────────────┐
                  │  BroccoliFeatureMaker  │
                  │  ~200 hand-crafted      │
                  │  features:              │
                  │   - times_submitted    │
                  │   - community_reputation│
                  │   - votes              │
                  │   - PE entropy         │
                  │   - file size          │
                  │   - tags (one-hot)     │
                  │   - signing info       │
                  │   - malware-name TFIDF │
                  └────────┬───────────────┘
                           │
                           ▼
                ┌─────────────────────────┐
                │  sklearn pipeline:      │
                │   TfidfVectorizer       │
                │   ManyHotEncoder        │
                │   StandardScaler        │
                │   TruncatedSVD(500)     │
                │   Normalizer            │
                │   ──►  Annoy index      │
                └────────┬────────────────┘
                         │
                         ▼
                ┌─────────────────────────┐
                │ KNeighborsClassifier-   │
                │ Annoy(n=10)             │
                └────────┬────────────────┘
                         │
                         ▼
                  label per sha1
                  (typically 'indifferent' / 'malware')
```

## Data sources (different from meta!)
- **InnoDB / MySQL** via internal `innovationdb` package.
  - Query in `broccoli/data/query.sql`.
  - Table: `vt_files_scans` (legacy — pre-BigQuery feed).
  - Class: `SamplesFetcher` filters by date range and detection thresholds.
- Optionally BigQuery via `vtindex.py` (newer addition).
- MsgPack files for engine results, parsed by `VTv2SampleParser`.

The fact that broccoli queries InnoDB while meta queries BigQuery is a strong signal of their relative ages.

## Files at a glance

| File | Role |
|---|---|
| `build_dataset.py` | dataset construction from InnoDB / VT v2 |
| `features.py` | `BroccoliFeatureMaker` — the ~200 features |
| `train.py` | `BroccoliTrainer` — builds and fits the sklearn + Annoy pipeline |
| `classify.py` | `VirusTotalBroccoliClassifier` — production wrapper, loads dill + Annoy index |
| `cluster.py` | clustering utilities (likely DBSCAN/HDBSCAN over the SVD space) |
| `label.py` | label generation utilities |
| `grid_search.py` / `manual_grid_search.py` | hyperparam tuning |
| `vtv2.py` | parses VT API v2 responses |
| `plot.py` | visualisation |
| `test_load_annoy.py` | smoke test for the Annoy index |

## The pipeline (concrete)
```python
Pipeline([
    FeatureUnion([
        TfidfVectorizer(tokens, min_df=3),     # malware-name tokens
        ManyHotEncoder(tags),                   # tag indicators
        StandardScaler(numerical_features),     # ~ normalised
    ]),
    TruncatedSVD(n_components=500),            # dim reduction
    Normalizer(),                              # unit-length vectors
    KNeighborsClassifierAnnoy(n_neighbors=10, annoy_index=...)
])
```

`KNeighborsClassifierAnnoy` is from internal `sklearn_extras`. Annoy (from Spotify) provides **approximate nearest-neighbour** search — much faster than exact KNN, with controllable accuracy/speed tradeoff.

## Output labels
Typically two:
- `indifferent` — benign / harmless.
- `malware` — malicious.

The exact taxonomy is configurable; the typical use is binary.

## Why broccoli still exists alongside meta
Possible reasons (interpretive — neither is documented in code):
1. **Speed at inference**: Annoy lookup is fast and scales to billions of indexed samples.
2. **Different signal**: broccoli's features capture *file metadata* (size, entropy, signing, …); meta's features capture *engine consensus*. They're partially independent.
3. **Disagreement is signal**: `meta/samples.py:rand_samples()` selects samples where snitch and broccoli disagree — analysts review those as "interesting" cases. So broccoli is alive at least as a dissenting voice.

## Limitations
- KNN over Annoy is **non-parametric** — quality depends on the index, which depends on the training data. Fresh malware families with no neighbours produce noisy votes.
- The 500-dim SVD is fixed — no easy way to add new features without re-projecting.
- Heavy dependence on `innovationdb` / MySQL is operationally awkward (compared to meta's BigQuery).
- TF-IDF over malware names with `min_df=3` keeps a lot of rare tokens — index can grow large.

## Mental model
> "Broccoli is a similarity-search baseline: 'I've seen something like this before, here's its label.' Meta is a stacking baseline: 'here's what the panel of AV engines votes.' Either is reasonable; the system keeps both partly because they fail in different ways."

## Related
- [[02 - Architecture - Five Subsystems]] — broccoli is "lineage B"
- [[03 - Meta Model Concept]] — the alternative approach
- [[11 - Data Sources]] — InnoDB vs BigQuery
- [[14 - Glossary]] — Annoy, KNN
