# orchestrator_benchmark_analysis_2026.04.06.ipynb

# Orchestrator Benchmark Comparison

This notebook provides a **generic comparison** of orchestrator benchmark results across multiple CSV files.

**How to use:** Edit the `FILE_MAP` dictionary in the next cell to specify which benchmark CSVs to compare.
Each entry maps a human-readable display label to a CSV filename in the `benchmark_results/` directory.

**Sections:**
1. **Accuracy Comparison** — Agent Selection, Tool Selection, and Guardrails Passing rates
2. **API Error Rate Comparison** — Success/failure counts and error rates
3. **Execution Time Comparison** — Mean times and distribution overlays
4. **Model Comparison** — Spider/radar chart when multiple models are detected
5. **Summary Table** — All key metrics in one table

```python
import sys
import subprocess
import os

def uv_install_if_needed(package: str):
    """
    Install a package using uv (preferred for this .venv environment)
    if it is not already available.
    """
    try:
        __import__(package)
    except ImportError:
        print(f"Installing missing package via uv: {package}")
        # Ensure we're using .venv if present
        venv_python = os.getenv("VIRTUAL_ENV")
        if venv_python:
            venv_python_path = os.path.join(venv_python, "bin", "python")
            # Use uv from the virtual environment, fallback to system uv
            try:
                subprocess.check_call(["uv", "pip", "install", package])
            except Exception:
                print(f"uv not found in PATH. Trying to run uv via Python in venv for: {package}")
                subprocess.check_call([venv_python_path, "-m", "uv", "pip", "install", package])
        else:
            print("VIRTUAL_ENV not set. Attempting to use system uv.")
            subprocess.check_call(["uv", "pip", "install", package])

uv_install_if_needed("ipykernel")
uv_install_if_needed("matplotlib")
uv_install_if_needed("seaborn")
```

```python
import os
import sys
import matplotlib
matplotlib.use('module://matplotlib_inline.backend_inline')  # Jupyter-compatible backend
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
import re
from pathlib import Path

# ============================================================
# CONFIGURATION — Edit FILE_MAP to select which CSVs to compare
# ============================================================

FILE_MAP = {
    "GPT-5.2 (BM1)": "orchestrator_benchmark_GPT-5.2_Model_2026.03.09_08.37.32.csv",
    "GPT-5.2 (BM2)": "orchestrator_benchmark_GPT-5.2_Model_2026.03.10_09.29.41.csv",
    "GPT-5.2 (BM2_REPEAT)": "orchestrator_benchmark_results_GPT-5.2_Model_2026.03.15_15.24.06.csv",
    "GPT-5.2 (BM2_CISO)": "orchestrator_benchmark_results_GPT-5.2_Model_2026.04.06_08.09.05.csv",
    "GPT-5.4 (BM1)": "orchestrator_benchmark_GPT-5.4_Model_2026.03.09_10.19.44.csv",
    "GPT-5.4 (BM2_REPEAT)": "orchestrator_benchmark_results_GPT-5.4_Model_2026.03.17_11.01.55.csv",
}

RESULTS_DIR = Path("../../src/orchestrator/benchmark_results")

# --- Auto-assigned colors (up to 10 files) ---
AUTO_COLORS = [
    "#3498db",  # Blue
    "#e74c3c",  # Red
    "#2ecc71",  # Green
    "#9b59b6",  # Purple
    "#f39c12",  # Orange
    "#1abc9c",  # Teal
    "#e67e22",  # Dark Orange
    "#2980b9",  # Dark Blue
    "#c0392b",  # Dark Red
    "#27ae60",  # Dark Green
]

# --- Chart Settings ---
FIGURE_SIZE_WIDE = (14, 6)
FIGURE_SIZE_SQUARE = (10, 6)
BAR_LABEL_FONTSIZE = 9
BAR_LABEL_FORMAT = "{:.0f}%"
BAR_EDGECOLOR = "#333"
BAR_LINEWIDTH = 1.5
TITLE_FONTSIZE = 13
AXIS_LABEL_FONTSIZE = 12

# --- Accuracy Column Mapping ---
ACCURACY_METRICS = {
    "Agent Selection": "is_correct_agent",
    "Tool Selection": "is_correct_tool",
    "Guardrails Passing": "is_correct_guardrails",
}

# --- Matplotlib Global Style ---
plt.style.use("seaborn-v0_8-whitegrid")
plt.rcParams.update({
    "figure.facecolor": "#f8f9fa",
    "axes.facecolor": "#ffffff",
    "axes.edgecolor": "#333333",
    "font.family": "sans-serif",
    "font.size": 11,
})

print("Configuration loaded.")
```

```python
# ============================================================
# Data Loading & Helper Functions
# ============================================================

datasets: dict[str, pd.DataFrame] = {}

for label, filename in FILE_MAP.items():
    path = RESULTS_DIR / filename
    if path.exists():
        datasets[label] = pd.read_csv(path)
        print(f"  Loaded {label:30s} -> {len(datasets[label]):>4d} rows  [{filename}]")
    else:
        print(f"  WARNING: File not found for {label}: {path}")

ALL_LABELS = list(datasets.keys())
COLORS = {label: AUTO_COLORS[i % len(AUTO_COLORS)] for i, label in enumerate(ALL_LABELS)}

print(f"\nTotal datasets loaded: {len(datasets)}")

# ============================================================
# Helper Functions
# ============================================================

def calc_accuracy_pct(df: pd.DataFrame, column: str) -> float:
    """Return the percentage of True values in a boolean column."""
    return df[column].sum() / len(df) * 100

def add_bar_labels(
        ax: plt.Axes,
        fmt: str = BAR_LABEL_FORMAT,
        fontsize: int = BAR_LABEL_FONTSIZE,
        padding: float = 3,
) -> None:
    """Annotate each bar with its value above it."""
    for container in ax.containers:
        ax.bar_label(
            container, fmt=fmt, fontsize=fontsize,
            padding=padding, fontweight="bold",
        )

def build_accuracy_df(labels: list[str]) -> pd.DataFrame:
    """Build a DataFrame of accuracy percentages for the given dataset labels."""
    rows = []
    for metric_name, col in ACCURACY_METRICS.items():
        row = {"Metric": metric_name}
        for label in labels:
            row[label] = calc_accuracy_pct(datasets[label], col)
        rows.append(row)
    return pd.DataFrame(rows).set_index("Metric")

def detect_model(filename: str, df: pd.DataFrame) -> str:
    """Detect the model name from filename or CSV 'model' column."""
    if "model" in df.columns:
        models = df["model"].dropna().unique()
        if len(models) == 1:
            return str(models[0])
        elif len(models) > 1:
            return ", ".join(str(m) for m in models)
    # Try filename pattern: orchestrator_benchmark_<ModelName>_Model_<date>.csv
    match = re.search(r"orchestrator_benchmark_(.+?)_Model_", filename)
    if match:
        return match.group(1)
    return "Unknown"

# --- Detect models for each file ---
model_map: dict[str, str] = {}
for label, filename in FILE_MAP.items():
    if label in datasets:
        model_map[label] = detect_model(filename, datasets[label])

print("\nDetected Models:")
for label, model in model_map.items():
    print(f"  {label:30s} -> {model}")
```

---

## Accuracy Comparison

Agent Selection Accuracy, Tool Selection Accuracy, and Guardrails Passing rate across all loaded benchmark files.

```python
# --- Accuracy Comparison (Grouped Bar Chart) ---

acc_df = build_accuracy_df(ALL_LABELS)
colors_list = [COLORS[lbl] for lbl in ALL_LABELS]

fig, ax = plt.subplots(figsize=FIGURE_SIZE_WIDE)
acc_df.plot(
    kind="bar",
    ax=ax,
    color=colors_list,
    edgecolor=BAR_EDGECOLOR,
    linewidth=BAR_LINEWIDTH,
    width=0.7,
)
add_bar_labels(ax)
ax.set_title("Accuracy Comparison Across Benchmark Runs", fontsize=TITLE_FONTSIZE, fontweight="bold", pad=10)
ax.set_ylabel("Accuracy (%)", fontsize=AXIS_LABEL_FONTSIZE, fontweight="bold")
ax.set_xlabel("")
ax.set_ylim(0, 115)
ax.axhline(y=100, color="#95a5a6", linestyle="--", alpha=0.5, linewidth=1)
ax.legend(title="Benchmark Run", fontsize=9, framealpha=0.9, loc="lower right")
ax.grid(True, alpha=0.3)
ax.tick_params(axis="x", rotation=0)

plt.tight_layout()
plt.savefig(RESULTS_DIR / "comparison_accuracy.png", dpi=150, bbox_inches="tight", facecolor="white")
plt.show()

# Print accuracy summary table
print("\nAccuracy Summary (%):\n")
print(acc_df.round(1).to_string())
```

---

## API Error Rate Comparison

API success/failure counts and error rates across all benchmark runs.

```python
# --- API Error Rate Comparison ---

api_success = [datasets[lbl]["is_api_worked"].sum() for lbl in ALL_LABELS]
api_failure = [len(datasets[lbl]) - datasets[lbl]["is_api_worked"].sum() for lbl in ALL_LABELS]
colors_list = [COLORS[lbl] for lbl in ALL_LABELS]

fig, axes = plt.subplots(1, 2, figsize=FIGURE_SIZE_WIDE)

# --- Left: Stacked bar chart (success vs failure) ---
x = np.arange(len(ALL_LABELS))
bar_width = max(0.3, 0.8 / len(ALL_LABELS))
bars_s = axes[0].bar(x, api_success, bar_width, label="Success", color="#2ecc71", edgecolor=BAR_EDGECOLOR,
                     linewidth=BAR_LINEWIDTH)
bars_f = axes[0].bar(x, api_failure, bar_width, bottom=api_success, label="Failure", color="#e74c3c",
                     edgecolor=BAR_EDGECOLOR, linewidth=BAR_LINEWIDTH)

for bar, val in zip(bars_s, api_success):
    axes[0].text(bar.get_x() + bar.get_width() / 2, bar.get_height() / 2, f"{val}",
                 ha="center", va="center", fontsize=BAR_LABEL_FONTSIZE, fontweight="bold", color="white")
for bar, bot, val in zip(bars_f, api_success, api_failure):
    if val > 0:
        axes[0].text(bar.get_x() + bar.get_width() / 2, bot + val / 2, f"{val}",
                     ha="center", va="center", fontsize=BAR_LABEL_FONTSIZE, fontweight="bold", color="white")

axes[0].set_title("API Success vs Failure (Count)", fontsize=TITLE_FONTSIZE, fontweight="bold", pad=10)
axes[0].set_ylabel("Number of Tests", fontsize=AXIS_LABEL_FONTSIZE, fontweight="bold")
axes[0].set_xticks(x)
axes[0].set_xticklabels(ALL_LABELS, rotation=15, ha="right")
axes[0].legend(fontsize=10, framealpha=0.9)
axes[0].grid(True, alpha=0.3)

# --- Right: API Error Rate (%) ---
api_error_pct = [100 - calc_accuracy_pct(datasets[lbl], "is_api_worked") for lbl in ALL_LABELS]
bars = axes[1].bar(ALL_LABELS, api_error_pct, color=colors_list, edgecolor=BAR_EDGECOLOR, linewidth=BAR_LINEWIDTH,
                   width=0.5)
for bar, val in zip(bars, api_error_pct):
    axes[1].text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.5,
                 f"{val:.1f}%", ha="center", fontsize=BAR_LABEL_FONTSIZE, fontweight="bold")
axes[1].set_title("API Error Rate (%)", fontsize=TITLE_FONTSIZE, fontweight="bold", pad=10)
axes[1].set_ylabel("Error Rate (%)", fontsize=AXIS_LABEL_FONTSIZE, fontweight="bold")
axes[1].tick_params(axis="x", rotation=15)
axes[1].grid(True, alpha=0.3)

fig.suptitle("API Error Rate Comparison", fontsize=16, fontweight="bold", y=1.02)
plt.tight_layout()
plt.savefig(RESULTS_DIR / "comparison_api_error_rate.png", dpi=150, bbox_inches="tight", facecolor="white")
plt.show()

# Print failed test IDs per file
print("\nFailed API Test IDs per Benchmark Run:\n")
for lbl in ALL_LABELS:
    df = datasets[lbl]
    failed = df[~df["is_api_worked"]]["test_id"].tolist()
    print(f"  {lbl} ({len(failed)} failures):")
    if failed:
        for tid in failed:
            print(f"    - {tid}")
    else:
        print(f"    (none)")
    print()
```

---

## Execution Time Comparison

Average execution time and distribution across all benchmark runs.

```python
# --- Average Execution Time Comparison ---

colors_list = [COLORS[lbl] for lbl in ALL_LABELS]
avg_times = [datasets[lbl]["execution_time_ms"].mean() for lbl in ALL_LABELS]

fig, ax = plt.subplots(figsize=FIGURE_SIZE_WIDE)
bars = ax.bar(
    ALL_LABELS, avg_times, color=colors_list,
    edgecolor=BAR_EDGECOLOR, linewidth=BAR_LINEWIDTH, width=0.6,
)
for bar, val in zip(bars, avg_times):
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + max(avg_times) * 0.02,
        f"{val:,.0f}ms",
        ha="center", va="bottom",
        fontsize=12, fontweight="bold",
    )

ax.set_title("Average Execution Time", fontsize=TITLE_FONTSIZE, fontweight="bold", pad=10)
ax.set_ylabel("Avg Execution Time (ms)", fontsize=AXIS_LABEL_FONTSIZE, fontweight="bold")
ax.tick_params(axis="x", rotation=15)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(RESULTS_DIR / "comparison_avg_execution_time.png", dpi=150, bbox_inches="tight", facecolor="white")
plt.show()

# Print execution time summary
print("\nExecution Time Summary (ms):\n")
print(f"  {'Run':30s}  {'Mean':>10s}   {'Median':>10s}   {'Std':>10s}   {'Min':>10s}   {'Max':>10s}")
print(f"  {'-' * 30}  {'-' * 10}   {'-' * 10}   {'-' * 10}   {'-' * 10}   {'-' * 10}")
for lbl in ALL_LABELS:
    times = datasets[lbl]["execution_time_ms"]
    print(
        f"  {lbl:30s}  {times.mean():>10,.1f}   {times.median():>10,.1f}   {times.std():>10,.1f}   {times.min():>10,.1f}   {times.max():>10,.1f}")
```

```python
# --- Execution Time Distribution (KDE) ---

fig, ax = plt.subplots(figsize=FIGURE_SIZE_SQUARE)

for lbl in ALL_LABELS:
    color = COLORS[lbl]
    times = datasets[lbl]["execution_time_ms"].dropna()
    sns.kdeplot(times, ax=ax, color=color, label=lbl, fill=True, alpha=0.25, linewidth=2.5)
    ax.axvline(times.median(), color=color, linestyle="--", linewidth=1.2, alpha=0.8)

ax.set_title("Execution Time Distribution (KDE)", fontsize=TITLE_FONTSIZE, fontweight="bold", pad=10)
ax.set_xlabel("Execution Time (ms)", fontsize=AXIS_LABEL_FONTSIZE, fontweight="bold")
ax.set_ylabel("Density", fontsize=AXIS_LABEL_FONTSIZE, fontweight="bold")
ax.legend(fontsize=11, frameon=True, fancybox=True, shadow=True)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(RESULTS_DIR / "comparison_execution_time_kde.png", dpi=150, bbox_inches="tight", facecolor="white")
plt.show()
```

---

## Model Comparison

Groups benchmark runs by their detected language model and compares them using a spider/radar chart.
Model is auto-detected from the CSV filename or a `model` column if present.

```python
# --- Model Comparison (Spider Chart) ---

unique_models = list(set(model_map.values()))

if len(unique_models) <= 1:
    print(f"All benchmark files use the same model: {unique_models[0] if unique_models else 'Unknown'}")
    print("Skipping spider chart — no cross-model comparison needed.")
else:
    # Aggregate metrics per model (average across runs using the same model)
    model_metrics = {}
    for model in unique_models:
        labels_for_model = [lbl for lbl, m in model_map.items() if m == model]
        agent_acc = np.mean([calc_accuracy_pct(datasets[lbl], "is_correct_agent") for lbl in labels_for_model])
        tool_acc = np.mean([calc_accuracy_pct(datasets[lbl], "is_correct_tool") for lbl in labels_for_model])
        guard_acc = np.mean([calc_accuracy_pct(datasets[lbl], "is_correct_guardrails") for lbl in labels_for_model])
        avg_acc = np.mean([agent_acc, tool_acc, guard_acc])
        avg_time = np.mean([datasets[lbl]["execution_time_ms"].mean() for lbl in labels_for_model])
        api_success = np.mean([calc_accuracy_pct(datasets[lbl], "is_api_worked") for lbl in labels_for_model])
        model_metrics[model] = {
            "avg_accuracy": avg_acc,
            "avg_time": avg_time,
            "api_success": api_success,
        }

    # Normalize: higher = better for all dimensions
    all_times = [m["avg_time"] for m in model_metrics.values()]
    min_time = min(all_times)

    dimensions = [
        "Avg Accuracy\n(higher = better)",
        "Speed\n(faster = higher)",
        "API Success\n(higher = better)",
    ]

    angles = np.linspace(0, 2 * np.pi, len(dimensions), endpoint=False).tolist()
    angles += angles[:1]

    model_colors = AUTO_COLORS[:len(unique_models)]

    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

    for i, model in enumerate(unique_models):
        m = model_metrics[model]
        norm_acc = m["avg_accuracy"]
        norm_speed = min_time / m["avg_time"] * 100 if m["avg_time"] > 0 else 0
        norm_api = m["api_success"]
        values = [norm_acc, norm_speed, norm_api]
        values += values[:1]
        ax.plot(angles, values, "o-", linewidth=2, label=model, color=model_colors[i])
        ax.fill(angles, values, alpha=0.15, color=model_colors[i])

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(dimensions, fontsize=11, fontweight="bold")
    ax.set_ylim(0, 110)
    ax.set_yticks([20, 40, 60, 80, 100])
    ax.set_yticklabels(["20", "40", "60", "80", "100"], fontsize=9, color="grey")
    ax.legend(loc="upper right", bbox_to_anchor=(1.3, 1.1), fontsize=11, framealpha=0.9)
    ax.set_title(
        "Model Comparison — Spider Chart\n(normalized, higher = better)",
        fontsize=14, fontweight="bold", pad=20,
    )

    plt.tight_layout()
    plt.savefig(RESULTS_DIR / "comparison_model_spider.png", dpi=150, bbox_inches="tight", facecolor="white")
    plt.show()

# Print model summary
print("\nModel Summary:\n")
print(f"  {'Model':20s}  {'Runs':>5s}  {'Avg Accuracy':>14s}  {'Avg Time (ms)':>14s}  {'API Success':>12s}")
print(f"  {'-' * 20}  {'-' * 5}  {'-' * 14}  {'-' * 14}  {'-' * 12}")
for model in unique_models:
    labels_for_model = [lbl for lbl, m in model_map.items() if m == model]
    agent_acc = np.mean([calc_accuracy_pct(datasets[lbl], "is_correct_agent") for lbl in labels_for_model])
    tool_acc = np.mean([calc_accuracy_pct(datasets[lbl], "is_correct_tool") for lbl in labels_for_model])
    guard_acc = np.mean([calc_accuracy_pct(datasets[lbl], "is_correct_guardrails") for lbl in labels_for_model])
    avg_acc = np.mean([agent_acc, tool_acc, guard_acc])
    avg_time = np.mean([datasets[lbl]["execution_time_ms"].mean() for lbl in labels_for_model])
    api_succ = np.mean([calc_accuracy_pct(datasets[lbl], "is_api_worked") for lbl in labels_for_model])
    print(f"  {model:20s}  {len(labels_for_model):>5d}  {avg_acc:>13.1f}%  {avg_time:>14,.1f}  {api_succ:>11.1f}%")
```

---

## Summary Table

Comprehensive metrics for all benchmark runs in a single table.

```python
# --- Comprehensive Summary Table ---

summary_rows = []
for lbl in ALL_LABELS:
    df = datasets[lbl]
    times = df["execution_time_ms"]
    summary_rows.append({
        "Benchmark Run": lbl,
        "Agent Sel. Acc (%)": round(calc_accuracy_pct(df, "is_correct_agent"), 1),
        "Tool Sel. Acc (%)": round(calc_accuracy_pct(df, "is_correct_tool"), 1),
        "Guardrails (%)": round(calc_accuracy_pct(df, "is_correct_guardrails"), 1),
        "API Error Rate (%)": round(100 - calc_accuracy_pct(df, "is_api_worked"), 1),
        "Avg Time (ms)": round(times.mean(), 1),
        "Median Time (ms)": round(times.median(), 1),
        "Detected Model": model_map.get(lbl, "Unknown"),
    })

summary_df = pd.DataFrame(summary_rows).set_index("Benchmark Run")
display(summary_df)
```

```python

```

```python

```

```python

```

```python

```
