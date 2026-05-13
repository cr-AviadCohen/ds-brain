# group_events_4llm.ipynb

```python
%load_ext autoreload
%autoreload 2
```

```python
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

def pandas_to_pyarrow_schema(df):
    """Convert pandas DataFrame dtypes to PyArrow schema."""
    return pa.schema([
        pa.field(col, pa.int64() if pd.api.types.is_integer_dtype(dtype) else
                     pa.float64() if pd.api.types.is_float_dtype(dtype) else
                     pa.bool_() if pd.api.types.is_bool_dtype(dtype) else
                     pa.timestamp('ns') if pd.api.types.is_datetime64_any_dtype(dtype) else
                     pa.string())
        for col, dtype in df.dtypes.items()
    ])

def read_parquet_with_csv_schema(parquet_file, csv_file):
    """Read parquet file using schema derived from CSV file."""
    try:
        # Read reference file
        reference_df = pd.read_csv(csv_file) if csv_file.endswith('.csv') else pd.read_parquet(csv_file)
        reference_schema = pandas_to_pyarrow_schema(reference_df)

        # Read parquet and find common columns
        problematic_table = pq.read_table(parquet_file)
        common_columns = [col for col in problematic_table.column_names if col in reference_df.columns]

        if common_columns:
            # Use common schema
            common_schema = pa.schema([field for field in reference_schema if field.name in common_columns])
            return pq.read_table(parquet_file, columns=common_columns, schema=common_schema).to_pandas()
        else:
            # Fallback: all strings
            string_schema = pa.schema([pa.field(col, pa.string()) for col in problematic_table.column_names])
            return problematic_table.cast(string_schema).to_pandas()
    except:
        return None
```

```python
sources = [
    "bq-results-20250701-123533-1751373420317.csv",         # Japan
    "malop_america_2025.csv",                               # America
    "../parquets/malop_europe_2025.parquet",                # Europe
]

dfs = [pd.read_csv(file) for file in sources if file.endswith('.csv')]
dfs.append(read_parquet_with_csv_schema(sources[-1], sources[1]))

[df.shape for df in dfs]
```

```python
# For each DataFrame in dfs, sample up to 30 unique matched_malop_id per classification, then concatenate all results

sampled_dfs = []
for df in dfs:
    # Group by classification, then for each group, sample up to 30 unique matched_malop_id
    def sample_ids(group):
        unique_ids = group['matched_malop_id'].drop_duplicates()
        sampled_ids = unique_ids.sample(n=min(30, len(unique_ids)), random_state=42)
        return group[group['matched_malop_id'].isin(sampled_ids)]
    sampled = df.groupby('Classification', group_keys=False).apply(sample_ids, include_groups=True)
    sampled_dfs.append(sampled)

final_df = pd.concat(sampled_dfs, ignore_index=True)
final_df["Classification"] = final_df["Classification"].apply(lambda x: "malicious" if x == "TP" else "benign")
final_df.shape

```

```python
final_df.groupby(["Classification"]).nunique()

```

```python
final_df.to_csv("/Users/guy.kapach/cursor_projects/research_notebooks/malop_worthy/events_for_llm_21_07_2025.csv", index=False)

```
