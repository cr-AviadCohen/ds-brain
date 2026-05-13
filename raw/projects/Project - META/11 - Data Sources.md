---
tags: [virustotalclassifier, data, bigquery, innodb]
type: reference
project: virustotalclassifier-meta
---

# Data Sources

What feeds this project, and how.

## Primary: VirusTotal BigQuery feed (used by `meta/`)

- **Project**: `vt-feed-pipeline-acfe9f`
- **Dataset**: `vt_file_report_feed`
- **Table**: `vt_file_report_feed_1`

### Schema (relevant columns only)
| Column | Type | What |
|---|---|---|
| `sha1` | string | the file hash (primary index) |
| `positives` | int | how many engines flagged it |
| `first_seen` | timestamp | first time VT saw it |
| `scan_date` | timestamp | this scan's timestamp |
| `scans` | repeated record `{name, detected, result}` | per-engine verdicts (~70 engines) |
| `tags` | array<string> | VT-curated tags (`cve-...`, `macros`, `powershell`, …) |
| `type` | string | file type (e.g. `Win32 EXE`, `MS Excel Spreadsheet`, `ELF`) |
| `vhash` | string | VT's structural hash (variant family) |

### Used by
- `meta/build_dataset.py` (all three builders).
- `meta/vtreferees.py` (referee selection).
- Optionally by `broccoli/data/vtindex.py` (newer addition; broccoli mainly uses InnoDB).

### Query mechanics
Queries are wrapped via internal `hanabase` (BigQuery client). Decorated with `@mark_as_query` and registered via `@query_registrar_class` so the configuration JSON can refer to them by name.

## Secondary: InnoDB / MySQL (used by `broccoli/`)

- **Database**: internal Cybereason MySQL.
- **ORM**: internal `innovationdb` package.
- **Table**: `vt_files_scans` (legacy — predates the BigQuery feed).
- **Class**: `broccoli/data/innodb.py:SamplesFetcher` — filters by date range and positive-detection thresholds.
- **Static query**: `broccoli/data/query.sql`.

### Used by
- `broccoli/build_dataset.py` and downstream broccoli pipeline.

### Why two sources?
History. Broccoli was built on InnoDB; meta was built when BigQuery feed became available. Both still work; the broccoli stack is older.

## Tertiary: VT raw v2 responses (MsgPack)

- Stored as MsgPack files (offline cache of VT API v2 responses).
- Parsed by `broccoli/vtv2.py:VTv2SampleParser`.
- Used to bootstrap broccoli's hand-crafted features when scanning new files.

## "Back to the future" sample selection (meta-specific)

Specific to `RefereesDatasetBuilder` in `meta/build_dataset.py`. Pulls samples where:
- `min_positives ≤ 2` at first scan
- `max_positives ≥ 8` at last scan
- `last_scan_date > first_scan_date`

The query uses BigQuery `WINDOW` functions to compute per-`sha1` `min_positives` and `max_positives` over the scan history. Filters down to samples whose detections **genuinely grew** (not just noise).

This selection is **the** distinguishing feature of how the meta system gets its referee labels (see [[05 - Referee Selection]]).

## Caching layer

Both the **referees list** and the **training datasets** are cached on disk. Cache invalidation is parameter-based (date ranges, file types, thresholds). Without caching, a single `meta.run()` can take hours due to BigQuery scan volume.

Cache location is configured via `configuration['output_path']`.

## Credentials

- BigQuery: GCP service-account JSON (path provided externally, not committed).
- InnoDB: internal connection string (probably env-var driven).
- VT API v2: API key for raw v2 fetching.

None of these are in the repo (correctly).

## Coverage gotchas

- **VT engine churn**: engines come and go. The `group_names_mapper` in `vtreferees.py` and the 95% null filter in `VerdictTransformer` are both reactions to this. Periodic recomputation of referees is required.
- **File-type biases**: not all engines submit verdicts on all file types. ELF coverage is weaker than PE coverage on VT. This is part of why each wrapper recomputes referees per file type.
- **Tag drift**: VT's tag taxonomy evolves. New tags may not be picked up by `TagsTransformer`'s aggregation rules until manually added.

## Mental model
> "The whole project sits downstream of VirusTotal's data lake. Meta uses BigQuery (modern); broccoli uses MySQL + MsgPack (legacy). Caching is essential because the queries are heavy."

## Related
- [[04 - Meta Pipeline Flow]] — how this data is consumed
- [[05 - Referee Selection]] — the back-to-future query
- [[10 - Broccoli Subsystem]] — InnoDB consumer
- [[14 - Glossary]] — `hanabase`, `innovationdb`, vhash
