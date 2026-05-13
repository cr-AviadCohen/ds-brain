# feature_generation.ipynb

```python
%load_ext autoreload
%autoreload 2
```

```python
import json
import joblib
import re
import ipaddress
import pandas as pd
import numpy as np
from collections import Counter
from scipy.signal import find_peaks

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', 50)
```

```python
generic_cols = [
    'Classification',
    'MalopName',
    'matched_malop_id',
    'correlationTimestamp',
    'creationTime',
    'dataSource',
    'alertName',
    'severityScore',
    'severity',
    'tactic',
    'subTechniques',
    'techniques',
    'dataSourceCategory',
    'alert_guid',
    'triggeringRule',
]

involved_host_names = [
    'sourceMachine.computerName',
    'connection.ownerMachine.computerName',
    'connection.remoteMachine.computerName',
]

involved_ips = [
    'sourceIpAddress.address',
    'connection.localAddress.address',
    'connection.remoteAddress.address',
]

involved_users = [
    'sourceUser.username',
    'targetUser.username',
]

involved_entities = [
    'targetProcess.guidString',
    'targetFile.fileHash.sha256Link.sha256',
    'targetProcess.imageFile.fileHash.sha256Link.sha256',
    'connection.urlDomain.url',
]

involved_email_addresses = [
    'sourceUser.emailAddresses',
    "targetUser.emailAddresses",
    'targetGroup.emailAddresses',
    'Message.receipientAddresses',
    'Message.senderAddress',
]

cols = generic_cols + involved_host_names + involved_ips + involved_users + involved_entities + involved_email_addresses
len(cols)
```

```python
errors = {}
```

```python
df = pd.read_parquet("./malop_unified_2025.parquet")
print(df.shape)
features = joblib.load('../reduced_features_classifier_2025-08-14_15-10-31.joblib').feature_names_in_
print(features.shape)
round4 = pd.read_parquet('malops_05_2024_06_2025_round4.parquet')
print(round4.shape)
```

```python
df.Classification.value_counts()
```

```python
df.head()
```

```python
df.columns.intersection(cols)
```

```python
df[list(df.columns.intersection(cols)) + ["event"]].head()
```

```python
print(df.event.iloc[0].replace("}", "}\n"))
```

```python
df = df[list(df.columns.intersection(cols)) + ["event"]]
df.shape
```

```python
def parse_df(input_df):
    df_normalized = pd.json_normalize(input_df.event.apply(json.loads))
    df_normalized = df_normalized.reset_index(drop=True)
    input_df.reset_index(drop=True, inplace=True)
    df_normalized = pd.concat([df_normalized, input_df], axis=1)

    for col in cols:
        if col not in df_normalized.columns:
            df_normalized[col] = None
    assert df_normalized["techniques"].fillna("").str.len().max() < 2
    data = df_normalized[cols].explode("techniques")
    for col in involved_email_addresses:
        data[col] = data[col].apply(lambda x: [item.get("email") for item in x] if isinstance(x, list) else x)

    data["creationTime"] = pd.to_datetime(data["creationTime"]*1e6)
    data["correlationTimestamp"] = pd.to_datetime(data["correlationTimestamp"]*1e6)

    return data
```

```python
def get_unique_values(df, columns):
    # Handle both single column and multiple columns
    if isinstance(columns, str):
        columns = [columns]

    # Get all values from the specified columns
    all_values = []
    for col in columns:
        col_values = df[col].values.flatten()
        all_values.extend(col_values)

    # Filter out None/NaN values
    filtered_values = list(filter(None, all_values))

    # Handle lists within the values
    unique = set()
    try:
        for val in filtered_values:
            if isinstance(val, list) or isinstance(val, set):
                unique.update(val)
            elif pd.notna(val):
                unique.add(val)
    except Exception as e:
        print(f"error in {val}")
        raise e

    return unique

def is_public_ip(ip):
    try:
        ip_obj = ipaddress.ip_address(ip)
        if not (ip_obj.is_private or ip_obj.is_loopback or ip_obj.is_reserved or ip_obj.is_multicast):
            return True
    except Exception as e:
        return False
    return False
```

```python
def calculate_burst_intensity_stats(event_times):
    """Calculate burst intensity based on time intervals between events"""
    if len(event_times) < 2:
        return {
            'interval_cv': 0,
            'mean_interval': 0,
            'interval_variance': 0,
            'burst_ratio': 0
        }

    # Sort events by time
    sorted_times = sorted(event_times)

    # Calculate intervals between consecutive events (in seconds)
    intervals = [(sorted_times[i+1] - sorted_times[i]).total_seconds()
                for i in range(len(sorted_times)-1)]

    if not intervals:
        return {'interval_cv': 0, 'mean_interval': 0, 'interval_variance': 0, 'burst_ratio': 0}

    mean_interval = np.mean(intervals)
    std_interval = np.std(intervals)

    # Coefficient of variation - higher = more bursty
    cv = std_interval / (mean_interval + 1e-6)

    # Burst ratio - fraction of intervals that are much shorter than average
    short_intervals = sum(1 for i in intervals if i < mean_interval * 0.1)
    burst_ratio = short_intervals / len(intervals)

    return {
        'interval_cv': cv,
        'mean_interval': mean_interval,
        'interval_variance': np.var(intervals),
        'burst_ratio': burst_ratio
    }

def calculate_entropy_burst_score(event_times, bins=10):
    """Lower entropy = more clustered/bursty events"""
    if len(event_times) < 2:
        return 0

    sorted_times = sorted(event_times.astype(int))
    total_span = (sorted_times[-1] - sorted_times[0])

    if total_span == 0:
        return 1.0  # All events at same time = maximum burst

    # Create time bins
    bin_edges = pd.date_range(start=sorted_times[0], end=sorted_times[-1], periods=bins+1)

    # Count events in each bin
    event_counts = pd.cut(sorted_times, bins=bin_edges.astype(int), include_lowest=True).value_counts()

    # Calculate entropy
    probabilities = event_counts / len(event_times)
    probabilities = probabilities[probabilities > 0]  # Remove zeros

    entropy = -np.sum(probabilities * np.log2(probabilities + 1e-6))
    max_entropy = np.log2(bins)

    # Convert to burst score (1 - normalized_entropy)
    burst_score = 1 - (entropy / max_entropy)
    return burst_score

def calculate_peak_burst_intensity(event_times, window_minutes=1):
    """Detect peaks in event frequency over time"""
    if len(event_times) < 3:
        return 0

    sorted_times = sorted(event_times)

    # Create time series with minute resolution
    start_time = sorted_times[0].replace(second=0, microsecond=0)
    end_time = sorted_times[-1].replace(second=0, microsecond=0) + pd.Timedelta(minutes=1)

    # Count events per minute
    time_bins = pd.date_range(start=start_time, end=end_time, freq='1min')
    event_counts = pd.Series(0, index=time_bins[:-1])

    for event_time in sorted_times:
        minute_bin = event_time.replace(second=0, microsecond=0)
        if minute_bin in event_counts.index:
            event_counts[minute_bin] += 1

    # Find peaks
    peaks, properties = find_peaks(event_counts.values, height=1)

    if len(peaks) == 0:
        return 0

    # Calculate peak intensity
    peak_heights = properties['peak_heights']
    avg_height = np.mean(event_counts.values)

    return np.max(peak_heights) / (avg_height + 1e-6)

def calculate_frequency_stats(event_times, sampling_rate='15T'):
    event_counts = event_times.to_frame().set_index(event_times.name).resample(sampling_rate).size()
    event_counts = event_counts.asfreq(sampling_rate, fill_value=0)

    stats = {
        'event_frequency_mean': event_counts.mean(),
        'event_frequency_std': event_counts.std(),
        'event_max_per_bin': event_counts.max(),
        'event_density': (event_counts > 0).sum() / len(event_counts),
    }
    return stats

def burst_analysis(time_column, sampling_rate='15T'):
    event_times = pd.to_datetime(time_column)

    # Method 1: Interval statistics
    interval_stats = calculate_burst_intensity_stats(event_times)

    # Method 3: Entropy score
    entropy_burst = calculate_entropy_burst_score(event_times)

    # Method 4: Peak detection
    peak_burst = calculate_peak_burst_intensity(event_times)

    # Method 5: Simple time span vs event count
    if len(event_times) > 1:
        time_span_minutes = (event_times.max() - event_times.min()).total_seconds() / 60
        events_per_minute = len(event_times) / (time_span_minutes + 1e-6)
    else:
        events_per_minute = 0

    freq_stats = calculate_frequency_stats(event_times, sampling_rate)

    res =  {
        'burst_interval_cv': interval_stats['interval_cv'],
        'burst_mean_interval': interval_stats['mean_interval'],
        'burst_interval_variance': interval_stats['interval_variance'],
        'burst_ratio': interval_stats['burst_ratio'],
        'burst_entropy_score': entropy_burst,
        'burst_peak_intensity': peak_burst,
        'events_per_minute': events_per_minute,
    }
    res.update(freq_stats)
    return res
```

```python
def calculate_entropy(items):
    if len(items) <= 1:
        return 0.0, 0.0
    counts = Counter(items)
    total = sum(counts.values())
    probs = [count / total for count in counts.values()]
    entropy = -sum(p * np.log2(p) for p in probs)
    max_entropy = np.log2(len(counts))  # Max possible entropy
    n_entropy = entropy / max_entropy if max_entropy > 0 else 0.0
    return float(entropy), float(n_entropy)

def calculate_string_entropy(entities):
    entropies = np.array([calculate_entropy(entity) for entity in entities if isinstance(entity, str)])
    if not entropies.size:
        return 0, 0, 0, 0
    max_entropy, max_normalized_entropy = entropies.max(0)
    mean_entropy, mean_normalized_entropy = entropies.mean(0)
    return max_entropy, max_normalized_entropy, mean_entropy, mean_normalized_entropy
```

```python
def transform_events(input_df, group_id):

    keywords = {"amazonaws"}
    suspected_pattern = r'\d{3,}'

    group_df = parse_df(input_df).fillna("")
    try:
        unique_ips = get_unique_values(group_df, involved_ips)
        unique_host_names = get_unique_values(group_df, involved_host_names)
        unique_email_addresses = get_unique_values(group_df, involved_email_addresses)
        unique_users = get_unique_values(group_df, involved_users)

        public_ips_list = [ip for ip in unique_ips if is_public_ip(ip)]
        internal_ips_list = [ip for ip in unique_ips if not is_public_ip(ip)]
        public_ips_entropy, public_ips_normalized_entropy = calculate_entropy(public_ips_list)
        internal_ips_entropy, internal_ips_normalized_entropy = calculate_entropy(internal_ips_list)

        rules = group_df.alertName.unique()
        tactics = group_df.tactic.unique()
        techniques = group_df.techniques.unique()
        data_source_category = group_df.dataSourceCategory.unique()

        # max_entropy, max_normalized_entropy, mean_entropy, mean_normalized_entropy
        users_entropies = calculate_string_entropy(unique_users)
        users_entropies = calculate_string_entropy(unique_users)
        emails_entropies = calculate_string_entropy(unique_email_addresses)
        domain_entropies = calculate_string_entropy({email.split("@")[1] for email in unique_email_addresses if "@" in email})

        results = {
            "id": group_id,
            "label": group_df.Classification.iloc[0] == "TP",
            "rules": "|".join(rules),
            "tactics": "|".join(tactics),
            "techniques": "|".join(techniques),
            "data_source_category": "|".join(data_source_category),
            "number_of_rules": len(rules),
            "number_of_tactics": len(tactics),
            "number_of_techniques": len(techniques),
            "number_of_data_source_categories": len(data_source_category),
            "span_time": (group_df.creationTime.max() - group_df.creationTime.min()).total_seconds(),
            "mean_latency": (group_df.correlationTimestamp - group_df.creationTime).mean().total_seconds(),
            "min_latency": (group_df.correlationTimestamp - group_df.creationTime).min().total_seconds(),
            "max_latency": (group_df.correlationTimestamp - group_df.creationTime).max().total_seconds(),
            "related_event_ids":  group_df['alert_guid'].nunique(),
            "detection_engines_number": group_df.dataSource.nunique(),
            "involved_host_names": len(unique_host_names),
            "involved users": len(unique_users),
            "suspected_users": sum(bool(re.search(suspected_pattern, user)) for user in unique_users),
            "users_max_entropy": users_entropies[0],
            "users_mean_entropy": users_entropies[2],
            "users_max_normalized_entropy": users_entropies[1],
            "users_mean_normalized_entropy": users_entropies[3],
            "involved_email_addresses": len(unique_email_addresses),
            "suspected_emails": sum(bool(re.search(suspected_pattern, email)) for email in unique_email_addresses),
            "emails_max_entropy": emails_entropies[0],
            "emails_mean_entropy": emails_entropies[2],
            "emails_max_normalized_entropy": emails_entropies[1],
            "emails_mean_normalized_entropy": emails_entropies[3],
            "domain_max_entropy": domain_entropies[0],
            "domain_mean_entropy": domain_entropies[2],
            "domain_max_normalized_entropy": domain_entropies[1],
            "domain_mean_normalized_entropy": domain_entropies[3],
            "involved_ips": len(unique_ips),
            "public_ips": len(public_ips_list),
            "public_ips_entropy": public_ips_entropy,
            "public_ips_normalized_entropy": public_ips_normalized_entropy,
            "internal_ips": len(internal_ips_list),
            "internal_ips_entropy": internal_ips_entropy,
            "internal_ips_normalized_entropy": internal_ips_normalized_entropy,
            "involved_process_hashes": group_df['targetProcess.guidString'].nunique(),
            "involved_file_hashes": len(get_unique_values(group_df, ['targetFile.fileHash.sha256Link.sha256',
                                                                    'targetProcess.imageFile.fileHash.sha256Link.sha256'])),
            "involved_urls_domains": group_df['connection.urlDomain.url'].nunique(),
            "interesting_domains": sum(1 for domain in group_df['connection.urlDomain.url'].dropna().unique()
                                     if any(keyword in domain for keyword in keywords)),
        }

        # Add burst analysis
        results.update(burst_analysis(group_df.creationTime))

        # Add temporal features
        dayofweek = group_df.creationTime.dt.dayofweek.value_counts(normalize=True)
        for key, value in dayofweek.items():
            results[f"dayofweek_{key}"] = value
        severity =  group_df["severity"].value_counts(normalize=True)
        for key, value in severity.items():
            results[f"severity_{key}"] = value
        severity_score =  group_df["severityScore"].value_counts(normalize=True)
        for key, value in severity_score.items():
            results[f"severity_score_{key}"] = value

        derived_features = {
            "public_ip_ratio": results["public_ips"] / (results["involved_ips"] + 1e-12),
            "rules_events_ratio": results["number_of_rules"] / (results["related_event_ids"] + 1e-12),
            "latency_span_ratio": results["mean_latency"] / (results["span_time"] + 1),
            "attack_complexity_score":  results['number_of_rules'] * 0.3 + \
                                        results['number_of_tactics'] * 0.4 + \
                                        results['number_of_techniques'] * 0.3,
            "multi_vector_score": sum(results[field] > 1 for field in results if "involved" in field),
        }

        results.update(derived_features)

        if group_df.Classification.nunique() != 1:
            results["label"] = None

    except Exception as e:
        print(f"{group_id} error: {e}")
        errors.update({group_id: e})
    return pd.Series(results)
```

```python
def process_data(data):
    groups = pd.concat([
        transform_events(group_df, group_id)  # extract features malop-wise
        .dropna(how="all")                    # omit Ambigious classification cases
        for group_id, group_df in data.groupby("matched_malop_id")   # groupby malop id
        ], axis=1).T.set_index("id")          # transpose and set malop id as index
    return groups
```

```python
groups = process_data(df)
ambiguous = groups[groups.label.isna()].index
groups.to_csv("./groups.csv")
groups = pd.read_csv("./groups.csv")
for column in ["tactics", "techniques", "data_source_category"]:
    groups = groups.drop(column, axis=1).join(groups[column].str.get_dummies().rename(columns=lambda x: f"{column}_{x}"))

frequent_rules = groups.rules.str.get_dummies().sum(0).nlargest(20).index
groups = groups.drop("rules", axis=1).join(
    groups.rules.str.get_dummies()[frequent_rules].rename(columns=lambda x: f"rule_{x}"))

print(f"{ambiguous.shape[0]} ambiguous cases: {ambiguous.tolist()}")
groups = groups.dropna(subset="label").infer_objects()
groups.shape
```

```python
groups.head().T
```

```python
all(round4[features] == groups[features])
```

```python
# groups.to_parquet("./malops_05_2024_06_2025_round4.parquet")
# groups.to_csv("./malops_05_2024_06_2025_round4.csv")
```

```python
set(groups.columns) ^ set(features)
```

```python
len(errors)
```
