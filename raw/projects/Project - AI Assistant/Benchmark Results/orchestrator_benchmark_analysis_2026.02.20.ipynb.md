# orchestrator_benchmark_analysis_2026.02.20.ipynb

# Orchestrator Benchmark Analysis

This notebook analyzes orchestrator benchmark results across two dimensions:

**Section 1 — Agent Configuration Comparison:**
Compare *CR Single Agent* (monolithic) vs *CR Separated Agents* (specialized per-domain agents) on accuracy and speed.

**Section 2 — Model Comparison:**
Compare *GPT-5.2*, *GPT-5-mini*, and *GPT-5-nano* (all using CR Separated Agents config) on accuracy, speed, price, and API success rates.

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
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from pathlib import Path

# ============================================================
# CONFIGURATION - Adjust these settings as needed
# ============================================================

# --- Display Labels ---
LABEL_CR_SINGLE = "CR Single Agent"
LABEL_CR_SEPARATED = "CR Separated Agents"
LABEL_GPT52 = "GPT-5.2"
LABEL_GPT5_MINI = "GPT-5-mini"
LABEL_GPT5_NANO = "GPT-5-nano"
LABEL_GPT52_NEW = "GPT-5.2"
LABEL_GPT54_NEW = "GPT-5.4"

# --- CSV File Names (relative to RESULTS_DIR) ---
FILE_MAP = {
    LABEL_CR_SINGLE:    "orchestrator_benchmark_CR_API_ALL_Agent_2026.02.05_16.51.38.csv",
    LABEL_CR_SEPARATED: "orchestrator_benchmark_CR_API_Separated_Agents_2026.02.05_17.40.40.csv",
    LABEL_GPT52:        "orchestrator_benchmark_GPT-5.2_Model_2026.02.05_18.28.55.csv",
    LABEL_GPT5_MINI:    "orchestrator_benchmark_GPT-5-mini_Model_2026.02.05_19.33.32.csv",
    LABEL_GPT5_NANO:    "orchestrator_benchmark_GPT-5-nano_Model_2026.02.05_20.56.52.csv",
    LABEL_GPT52_NEW:    "orchestrator_benchmark_GPT-5.2_Model_2026.03.09_08.37.32.csv",
    LABEL_GPT54_NEW:    "orchestrator_benchmark_GPT-5.4_Model_2026.03.09_10.19.44.csv",
}

RESULTS_DIR = Path("../../src/orchestrator/benchmark_results")

# --- Colors ---
COLOR_CR_SINGLE    = "#2ecc71"  # Green
COLOR_CR_SEPARATED = "#3498db"  # Blue
COLOR_GPT52        = "#9b59b6"  # Purple
COLOR_GPT5_MINI    = "#e74c3c"  # Red
COLOR_GPT5_NANO    = "#f39c12"  # Orange

COLORS_AGENT_CONFIG = [COLOR_CR_SINGLE, COLOR_CR_SEPARATED]
COLORS_MODELS = [COLOR_GPT52, COLOR_GPT5_MINI, COLOR_GPT5_NANO]

# --- Chart Settings ---
FIGURE_SIZE_WIDE = (14, 6)
FIGURE_SIZE_SQUARE = (10, 6)
BAR_LABEL_FONTSIZE = 9
BAR_LABEL_FORMAT = "{:.0f}%"
BAR_EDGECOLOR = "#333"
BAR_LINEWIDTH = 1.5
TITLE_FONTSIZE = 13
AXIS_LABEL_FONTSIZE = 12

# --- Model Pricing (USD per 1K tokens) - adjust to actual rates ---
MODEL_PRICING = {
    LABEL_GPT52:     {"input": 1.75,  "output": 14.0},
    LABEL_GPT5_MINI: {"input": 0.25,  "output": 2.0},
    LABEL_GPT5_NANO: {"input": 0.05,  "output": 0.04},
}

# --- Accuracy Column Mapping ---
ACCURACY_METRICS = {
    "Agent Selection":    "is_correct_agent",
    "Tool Selection":     "is_correct_tool",
    "Guardrails Passing": "is_correct_guardrails",
    # "API Worked":         "is_api_worked",
}

# --- Matplotlib Global Style ---
plt.style.use("seaborn-v0_8-whitegrid")
plt.rcParams.update({
    "figure.facecolor": "#f8f9fa",
    "axes.facecolor":   "#ffffff",
    "axes.edgecolor":   "#333333",
    "font.family":      "sans-serif",
    "font.size":        11,
})

print("Configuration loaded.")
```

```python
# ============================================================
# Data Loading
# ============================================================

datasets: dict[str, pd.DataFrame] = {}

for label, filename in FILE_MAP.items():
    path = RESULTS_DIR / filename
    if path.exists():
        datasets[label] = pd.read_csv(path)
        print(f"  Loaded {label:25s} -> {len(datasets[label]):>4d} rows")
    else:
        print(f"  WARNING: File not found for {label}: {path}")

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
    """Annotate each bar with its value above it (bold, matching notebook-1 style)."""
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
```

---

## Section 1: CR Single Agent vs CR Separated Agents

Comparing two agent architecture strategies on accuracy and execution speed.

```python
# --- Section 1: Accuracy & Execution Time Comparison (side by side) ---

section1_labels = [LABEL_CR_SINGLE, LABEL_CR_SEPARATED]
section1_colors = COLORS_AGENT_CONFIG

fig, axes = plt.subplots(1, 2, figsize=FIGURE_SIZE_WIDE)

# --- Left: Accuracy Comparison ---
acc_df = build_accuracy_df(section1_labels)
acc_df.plot(
    kind="bar",
    ax=axes[0],
    color=section1_colors,
    edgecolor=BAR_EDGECOLOR,
    linewidth=BAR_LINEWIDTH,
    width=0.7,
)
add_bar_labels(axes[0])
axes[0].set_title(
    "Accuracy Comparison",
    fontsize=TITLE_FONTSIZE,
    fontweight="bold",
    pad=10,
)
axes[0].set_ylabel("Accuracy (%)", fontsize=AXIS_LABEL_FONTSIZE, fontweight="bold")
axes[0].set_xlabel("")
axes[0].set_ylim(0, 115)
axes[0].axhline(y=100, color="#95a5a6", linestyle="--", alpha=0.5, linewidth=1)
axes[0].legend(title="Configuration", fontsize=9, framealpha=0.9, loc="lower right")
axes[0].grid(True, alpha=0.3)
axes[0].tick_params(axis="x", rotation=0)

# --- Right: Average Execution Time (with Std Dev) ---
avg_times = [datasets[lbl]["execution_time_ms"].mean() for lbl in section1_labels]
stds = [datasets[lbl]["execution_time_ms"].std() for lbl in section1_labels]
bars = axes[1].bar(
    section1_labels, avg_times, color=section1_colors,
    edgecolor=BAR_EDGECOLOR, linewidth=BAR_LINEWIDTH, width=0.6,
    # yerr=stds,
    capsize=5, error_kw={"linewidth": 2, "capthick": 2},
)
for bar, val in zip(bars, avg_times):
    axes[1].text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 200,
        f"{val:,.0f}ms",
        ha="center", va="bottom",
        fontsize=12, fontweight="bold",
    )
axes[1].set_title("Average Execution Time (with Std Dev)", fontsize=TITLE_FONTSIZE, fontweight="bold", pad=10)
axes[1].set_ylabel("Avg Execution Time (ms)", fontsize=AXIS_LABEL_FONTSIZE, fontweight="bold")
axes[1].grid(True, alpha=0.3)

fig.suptitle(
    f"{LABEL_CR_SINGLE} vs {LABEL_CR_SEPARATED}",
    fontsize=16, fontweight="bold", y=1.02,
)
plt.tight_layout()
plt.savefig(RESULTS_DIR / "agent_config_accuracy_and_time.png", dpi=150, bbox_inches="tight", facecolor="white")
plt.show()

# Print accuracy summary table
print("\nAccuracy Summary (%):\n")
print(acc_df.round(1).to_string())

# Print execution time summary
print("\nExecution Time Summary (ms):\n")
for lbl in section1_labels:
    times = datasets[lbl]["execution_time_ms"]
    print(f"  {lbl:25s}  Mean: {times.mean():>10,.1f}   Median: {times.median():>10,.1f}   Std: {times.std():>10,.1f}")
```

```python
# --- Section 1: Execution Time Distribution (KDE) ---

fig, ax = plt.subplots(figsize=FIGURE_SIZE_SQUARE)

for lbl, color in zip(section1_labels, section1_colors):
    times = datasets[lbl]["execution_time_ms"].dropna()
    sns.kdeplot(times, ax=ax, color=color, label=lbl, fill=True, alpha=0.35, linewidth=2)
    ax.axvline(times.median(), color=color, linestyle="--", linewidth=1.2, alpha=0.8)

ax.set_title("Execution Time Distribution", fontsize=TITLE_FONTSIZE, fontweight="bold", pad=10)
ax.set_xlabel("Time (ms)", fontsize=AXIS_LABEL_FONTSIZE, fontweight="bold")
ax.set_ylabel("Density", fontsize=AXIS_LABEL_FONTSIZE, fontweight="bold")
ax.legend(fontsize=11, framealpha=0.9)
ax.grid(True, alpha=0.3)
fig.suptitle(
    f"Execution Time: {LABEL_CR_SINGLE} vs {LABEL_CR_SEPARATED}",
    fontsize=16, fontweight="bold", y=1.02,
)
plt.tight_layout()
plt.savefig(RESULTS_DIR / "agent_config_execution_time.png", dpi=150, bbox_inches="tight", facecolor="white")
plt.show()
```

---

## Section 2: Model Comparison (GPT-5.2 vs GPT-5-mini vs GPT-5-nano)

All three model benchmarks use the **CR Separated Agents** configuration.
This section compares them on execution time, accuracy, estimated price, and API success/failure rates.

```python
# --- Section 2: Accuracy & Execution Time Comparison (side by side) ---

model_labels = [LABEL_GPT52, LABEL_GPT5_MINI, LABEL_GPT5_NANO]
model_colors = COLORS_MODELS

fig, axes = plt.subplots(1, 2, figsize=FIGURE_SIZE_WIDE)

# --- Left: Accuracy Comparison ---
acc_df_models = build_accuracy_df(model_labels)
acc_df_models.plot(
    kind="bar",
    ax=axes[0],
    color=model_colors,
    edgecolor=BAR_EDGECOLOR,
    linewidth=BAR_LINEWIDTH,
    width=0.7,
)
add_bar_labels(axes[0])
axes[0].set_title(
    "Accuracy Comparison",
    fontsize=TITLE_FONTSIZE,
    fontweight="bold",
    pad=10,
)
axes[0].set_ylabel("Accuracy (%)", fontsize=AXIS_LABEL_FONTSIZE, fontweight="bold")
axes[0].set_xlabel("")
axes[0].set_ylim(0, 115)
axes[0].axhline(y=100, color="#95a5a6", linestyle="--", alpha=0.5, linewidth=1)
axes[0].legend(title="Model", fontsize=9, framealpha=0.9, loc="lower right")
axes[0].grid(True, alpha=0.3)
axes[0].tick_params(axis="x", rotation=0)

# --- Right: Average Execution Time (with Std Dev) ---
avg_times_m = [datasets[lbl]["execution_time_ms"].mean() for lbl in model_labels]
stds_m = [datasets[lbl]["execution_time_ms"].std() for lbl in model_labels]
bars = axes[1].bar(
    model_labels, avg_times_m, color=model_colors,
    edgecolor=BAR_EDGECOLOR, linewidth=BAR_LINEWIDTH, width=0.6,
    # yerr=stds_m,
    capsize=5, error_kw={"linewidth": 2, "capthick": 2},
)
for bar, val in zip(bars, avg_times_m):
    axes[1].text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 200,
        f"{val:,.0f}ms",
        ha="center", va="bottom",
        fontsize=12, fontweight="bold",
    )
axes[1].set_title("Average Execution Time (with Std Dev)", fontsize=TITLE_FONTSIZE, fontweight="bold", pad=10)
axes[1].set_ylabel("Avg Execution Time (ms)", fontsize=AXIS_LABEL_FONTSIZE, fontweight="bold")
axes[1].grid(True, alpha=0.3)

fig.suptitle(
    "Model Comparison: Accuracy & Execution Time\n(CR Separated Agents)",
    fontsize=16, fontweight="bold", y=1.02,
)
plt.tight_layout()
plt.savefig(RESULTS_DIR / "model_accuracy_and_time.png", dpi=150, bbox_inches="tight", facecolor="white")
plt.show()

# Print accuracy summary table
print("\nAccuracy Summary (%):\n")
print(acc_df_models.round(1).to_string())

# Print execution time summary
print("\nExecution Time Summary (ms):\n")
for lbl in model_labels:
    times = datasets[lbl]["execution_time_ms"]
    print(f"  {lbl:15s}  Mean: {times.mean():>10,.1f}   Median: {times.median():>10,.1f}   Std: {times.std():>10,.1f}")
```

```python
# --- Section 2: Execution Time Distribution (KDE) ---

model_labels = [LABEL_GPT52, LABEL_GPT5_MINI, LABEL_GPT5_NANO]
model_colors = COLORS_MODELS

fig, ax = plt.subplots(figsize=FIGURE_SIZE_SQUARE)

for lbl, color in zip(model_labels, model_colors):
    sns.kdeplot(
        datasets[lbl]["execution_time_ms"],
        label=lbl, color=color, linewidth=2.5, fill=True, alpha=0.25, ax=ax,
    )

ax.set_title("Execution Time Distribution (KDE)", fontsize=TITLE_FONTSIZE, fontweight="bold", pad=10)
ax.set_xlabel("Execution Time (ms)", fontsize=AXIS_LABEL_FONTSIZE, fontweight="bold")
ax.set_ylabel("Density", fontsize=AXIS_LABEL_FONTSIZE, fontweight="bold")
ax.legend(fontsize=11, frameon=True, fancybox=True, shadow=True)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(RESULTS_DIR / "model_execution_time_kde.png", dpi=150, bbox_inches="tight", facecolor="white")
plt.show()

print("\nExecution Time Summary (ms):\n")
for lbl in model_labels:
    times = datasets[lbl]["execution_time_ms"]
    print(f"  {lbl:15s}  Mean: {times.mean():>10,.1f}   Median: {times.median():>10,.1f}   Std: {times.std():>10,.1f}")
```

```python
# --- Section 2: Price Comparison ---
#
# The benchmark CSVs do not include token counts.
# This cell uses the MODEL_PRICING constants defined in Cell 1
# to show relative cost and a cost-effectiveness estimate.
# Adjust MODEL_PRICING to match your actual Azure OpenAI rates.

model_labels = [LABEL_GPT52, LABEL_GPT5_MINI, LABEL_GPT5_NANO]
model_colors = COLORS_MODELS

# Compute a blended price per 1K tokens (average of input & output)
blended_price = {
    lbl: (MODEL_PRICING[lbl]["input"] + MODEL_PRICING[lbl]["output"]) / 2
    for lbl in model_labels
}

# Overall accuracy per model (all four metrics correct)
overall_acc = {}
for lbl in model_labels:
    df = datasets[lbl]
    mask = (
        df["is_correct_agent"]
        & df["is_correct_tool"]
        & df["is_correct_guardrails"]
        & df["is_api_worked"]
    )
    overall_acc[lbl] = mask.sum() / len(df) * 100

fig, axes = plt.subplots(1, 3, figsize=(16, 6))

# --- Left: Blended price per 1K tokens ---
prices = [blended_price[lbl] for lbl in model_labels]
bars = axes[0].bar(model_labels, prices, color=model_colors, edgecolor=BAR_EDGECOLOR, linewidth=BAR_LINEWIDTH, width=0.5)
for bar, val in zip(bars, prices):
    axes[0].text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + max(prices) * 0.04,
        f"${val:.4f}",
        ha="center",
        fontsize=BAR_LABEL_FONTSIZE,
        fontweight="bold",
    )
axes[0].set_title("Blended Price per 1K Tokens", fontsize=TITLE_FONTSIZE, fontweight="bold", pad=10)
axes[0].set_ylabel("USD per 1K tokens", fontsize=AXIS_LABEL_FONTSIZE, fontweight="bold")
axes[0].set_ylim(0, max(prices) * 1.3)
axes[0].grid(True, alpha=0.3)

# --- Center: Input vs Output price breakdown ---
x = np.arange(len(model_labels))
width = 0.35
input_prices = [MODEL_PRICING[lbl]["input"] for lbl in model_labels]
output_prices = [MODEL_PRICING[lbl]["output"] for lbl in model_labels]
bars_in = axes[1].bar(x - width / 2, input_prices, width, label="Input", color="#5dade2", edgecolor=BAR_EDGECOLOR, linewidth=BAR_LINEWIDTH)
bars_out = axes[1].bar(x + width / 2, output_prices, width, label="Output", color="#f1948a", edgecolor=BAR_EDGECOLOR, linewidth=BAR_LINEWIDTH)
for bar, val in zip(bars_in, input_prices):
    axes[1].text(bar.get_x() + bar.get_width() / 2, bar.get_height() + max(output_prices) * 0.03,
                 f"${val:.4f}", ha="center", fontsize=BAR_LABEL_FONTSIZE - 1)
for bar, val in zip(bars_out, output_prices):
    axes[1].text(bar.get_x() + bar.get_width() / 2, bar.get_height() + max(output_prices) * 0.03,
                 f"${val:.4f}", ha="center", fontsize=BAR_LABEL_FONTSIZE - 1)
axes[1].set_title("Input vs Output Pricing", fontsize=TITLE_FONTSIZE, fontweight="bold", pad=10)
axes[1].set_ylabel("USD per 1K tokens", fontsize=AXIS_LABEL_FONTSIZE, fontweight="bold")
axes[1].set_xticks(x)
axes[1].set_xticklabels(model_labels)
axes[1].legend(fontsize=10, framealpha=0.9)
axes[1].set_ylim(0, max(output_prices) * 1.35)
axes[1].grid(True, alpha=0.3)

# --- Right: Cost-Effectiveness (Overall Accuracy / Blended Price) ---
cost_eff = [overall_acc[lbl] / blended_price[lbl] for lbl in model_labels]
bars = axes[2].bar(model_labels, cost_eff, color=model_colors, edgecolor=BAR_EDGECOLOR, linewidth=BAR_LINEWIDTH, width=0.5)
for bar, val in zip(bars, cost_eff):
    axes[2].text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + max(cost_eff) * 0.03,
        f"{val:,.0f}",
        ha="center",
        fontsize=BAR_LABEL_FONTSIZE,
        fontweight="bold",
    )
axes[2].set_title("Cost-Effectiveness\n(Overall Accuracy % / Price)", fontsize=TITLE_FONTSIZE, fontweight="bold", pad=10)
axes[2].set_ylabel("Accuracy per $ (higher is better)", fontsize=AXIS_LABEL_FONTSIZE, fontweight="bold")
axes[2].set_ylim(0, max(cost_eff) * 1.25)
axes[2].grid(True, alpha=0.3)

fig.suptitle("Model Price Comparison", fontsize=16, fontweight="bold", y=1.02)
plt.tight_layout()
plt.savefig(RESULTS_DIR / "model_price_comparison.png", dpi=150, bbox_inches="tight", facecolor="white")
plt.show()

# Print summary
print("\nPrice & Cost-Effectiveness Summary:\n")
print(f"  {'Model':15s}  {'Blended $/1K':>14s}  {'Overall Acc %':>14s}  {'Cost-Eff':>10s}")
print(f"  {'-'*15}  {'-'*14}  {'-'*14}  {'-'*10}")
for lbl in model_labels:
    print(f"  {lbl:15s}  ${blended_price[lbl]:>13.4f}  {overall_acc[lbl]:>13.1f}%  {overall_acc[lbl] / blended_price[lbl]:>10,.0f}")
```

```python
# --- Section 2: API Success / Failure Comparison ---

model_labels = [LABEL_GPT52, LABEL_GPT5_MINI, LABEL_GPT5_NANO]
model_colors = COLORS_MODELS

api_success = [datasets[lbl]["is_api_worked"].sum() for lbl in model_labels]
api_failure = [len(datasets[lbl]) - datasets[lbl]["is_api_worked"].sum() for lbl in model_labels]

fig, axes = plt.subplots(1, 2, figsize=FIGURE_SIZE_WIDE)

# --- Left: Stacked bar chart ---
x = np.arange(len(model_labels))
bar_width = 0.5
bars_s = axes[0].bar(x, api_success, bar_width, label="Success", color="#2ecc71", edgecolor=BAR_EDGECOLOR, linewidth=BAR_LINEWIDTH)
bars_f = axes[0].bar(x, api_failure, bar_width, bottom=api_success, label="Failure", color="#e74c3c", edgecolor=BAR_EDGECOLOR, linewidth=BAR_LINEWIDTH)

for bar, val in zip(bars_s, api_success):
    axes[0].text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() / 2,
        f"{val}",
        ha="center", va="center",
        fontsize=BAR_LABEL_FONTSIZE,
        fontweight="bold",
        color="white",
    )
for bar, bot, val in zip(bars_f, api_success, api_failure):
    if val > 0:
        axes[0].text(
            bar.get_x() + bar.get_width() / 2,
            bot + val / 2,
            f"{val}",
            ha="center", va="center",
            fontsize=BAR_LABEL_FONTSIZE,
            fontweight="bold",
            color="white",
        )

axes[0].set_title("API Success vs Failure (Count)", fontsize=TITLE_FONTSIZE, fontweight="bold", pad=10)
axes[0].set_ylabel("Number of Tests", fontsize=AXIS_LABEL_FONTSIZE, fontweight="bold")
axes[0].set_xticks(x)
axes[0].set_xticklabels(model_labels)
axes[0].legend(fontsize=10, framealpha=0.9)
axes[0].grid(True, alpha=0.3)

# --- Right: API success rate percentage ---
api_pct = [calc_accuracy_pct(datasets[lbl], "is_api_worked") for lbl in model_labels]
bars = axes[1].bar(model_labels, api_pct, color=model_colors, edgecolor=BAR_EDGECOLOR, linewidth=BAR_LINEWIDTH, width=0.5)
for bar, val in zip(bars, api_pct):
    axes[1].text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 1,
        f"{val:.1f}%",
        ha="center",
        fontsize=BAR_LABEL_FONTSIZE,
        fontweight="bold",
    )
axes[1].set_title("API Success Rate (%)", fontsize=TITLE_FONTSIZE, fontweight="bold", pad=10)
axes[1].set_ylabel("Success Rate (%)", fontsize=AXIS_LABEL_FONTSIZE, fontweight="bold")
axes[1].set_ylim(0, 105)
axes[1].axhline(y=100, color="#95a5a6", linestyle="--", alpha=0.5, linewidth=1)
axes[1].grid(True, alpha=0.3)

fig.suptitle("Model API Success / Failure Comparison", fontsize=16, fontweight="bold", y=1.02)
plt.tight_layout()
plt.savefig(RESULTS_DIR / "model_api_success.png", dpi=150, bbox_inches="tight", facecolor="white")
plt.show()

# Print failed test IDs per model
print("\nFailed API Test IDs per Model:\n")
for lbl in model_labels:
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

```python
# --- Section 2: Spider Chart — Model Comparison Overview ---
# Costs per 1M tokens sourced from OpenAI pricing (Feb 2026):
#   GPT-5.2:    $1.75 input  + $14.00 output = $15.75
#   GPT-5-mini: $0.25 input  + $2.00  output = $2.25
#   GPT-5-nano: $0.05 input  + $0.40  output = $0.45

model_labels = [LABEL_GPT52, LABEL_GPT5_MINI, LABEL_GPT5_NANO]
model_colors = COLORS_MODELS

# --- 1. Tool Selection Accuracy (%) ---
tool_acc = [calc_accuracy_pct(datasets[lbl], "is_correct_tool") for lbl in model_labels]

# --- 2. Average Execution Time (ms) ---
avg_times = [datasets[lbl]["execution_time_ms"].mean() for lbl in model_labels]

# --- 3. Cost per 1M tokens (combined input + output) ---
COST_PER_1M = {
    LABEL_GPT52:     1.75 + 14.00,
    LABEL_GPT5_MINI: 0.25 + 2.00,
    LABEL_GPT5_NANO: 0.05 + 0.40,
}
costs = [COST_PER_1M[lbl] for lbl in model_labels]

# Normalize to 0-100 (higher = better on all axes)
norm_acc  = tool_acc
norm_time = [min(avg_times) / t * 100 for t in avg_times]
norm_cost = [min(costs) / c * 100 for c in costs]

dimensions = [
    "Tool Selection\nAccuracy",
    "Execution Speed\n(faster → higher)",
    "Cost Efficiency\n(cheaper → higher)",
]

angles = np.linspace(0, 2 * np.pi, len(dimensions), endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

for i, lbl in enumerate(model_labels):
    values = [norm_acc[i], norm_time[i], norm_cost[i]]
    values += values[:1]
    ax.plot(angles, values, "o-", linewidth=2, label=lbl, color=model_colors[i])
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
plt.savefig(RESULTS_DIR / "model_comparison_spider_chart.png", dpi=150, bbox_inches="tight", facecolor="white")
plt.show()

# Print raw values
print("\nSpider Chart — Raw Values:\n")
print(f"  {'Model':15s}  {'Tool Acc %':>12s}  {'Avg Time (ms)':>14s}  {'Cost/1M ($)':>12s}")
print(f"  {'-'*15}  {'-'*12}  {'-'*14}  {'-'*12}")
for i, lbl in enumerate(model_labels):
    print(f"  {lbl:15s}  {tool_acc[i]:>11.1f}%  {avg_times[i]:>14,.1f}  ${costs[i]:>11.2f}")

print("\nNormalized Scores (0-100, higher = better):\n")
print(f"  {'Model':15s}  {'Accuracy':>10s}  {'Speed':>10s}  {'Cost Eff.':>10s}")
print(f"  {'-'*15}  {'-'*10}  {'-'*10}  {'-'*10}")
for i, lbl in enumerate(model_labels):
    print(f"  {lbl:15s}  {norm_acc[i]:>9.1f}%  {norm_time[i]:>9.1f}%  {norm_cost[i]:>9.1f}%")
```

---

## Section 3: Per-Agent Accuracy Breakdown (CR Separated Agents)

Agent Selection Accuracy and Tool Selection Accuracy for each agent, using the **CR Separated Agents** benchmark dataset.

- **Agent Selection Accuracy** — percentage of queries intended for an agent where the orchestrator routed to the correct agent.
- **Tool Selection Accuracy** — percentage of queries directed to an agent where the correct tool was selected.

```python
# --- Section 3: Per-Agent Accuracy (CR Separated Agents) ---

df_sep = datasets[LABEL_CR_SEPARATED]

per_agent = (
    df_sep
    .groupby("expected_agent")
    .agg(
        total_queries=("is_correct_agent", "count"),
        agent_correct=("is_correct_agent", "sum"),
        tool_correct=("is_correct_tool", "sum"),
    )
)
per_agent["Agent Selection Accuracy"] = per_agent["agent_correct"] / per_agent["total_queries"] * 100
per_agent["Tool Selection Accuracy"] = per_agent["tool_correct"] / per_agent["total_queries"] * 100
per_agent = per_agent.sort_values("Tool Selection Accuracy", ascending=True)

pretty_labels = [
    name.replace("agent_", "").replace("_", " ").title()
    for name in per_agent.index
]

# --- Plot ---
fig, ax = plt.subplots(figsize=(16, max(8, len(per_agent) * 0.38)))

y_pos = np.arange(len(per_agent))
bar_height = 0.36

bars_tool = ax.barh(
    y_pos - bar_height / 2,
    per_agent["Tool Selection Accuracy"],
    height=bar_height,
    label="Tool Selection Accuracy",
    color="#e74c3c",
    edgecolor=BAR_EDGECOLOR,
    linewidth=1,
)
bars_agent = ax.barh(
    y_pos + bar_height / 2,
    per_agent["Agent Selection Accuracy"],
    height=bar_height,
    label="Agent Selection Accuracy",
    color="#3498db",
    edgecolor=BAR_EDGECOLOR,
    linewidth=1,
)

for bars in [bars_tool, bars_agent]:
    ax.bar_label(bars, fmt="%.0f%%", fontsize=8, fontweight="bold", padding=4)

ax.set_yticks(y_pos)
ax.set_yticklabels(pretty_labels, fontsize=10)
ax.set_xlabel("Accuracy (%)", fontsize=AXIS_LABEL_FONTSIZE)
ax.set_xlim(0, 115)
ax.set_title(
    "Per-Agent Accuracy — Agent Selection vs Tool Selection\n"
    f"({LABEL_CR_SEPARATED})",
    fontsize=TITLE_FONTSIZE, fontweight="bold",
)
ax.legend(loc="lower right", fontsize=11, framealpha=0.9)
ax.invert_yaxis()

plt.tight_layout()
plt.savefig(
    RESULTS_DIR / "per_agent_accuracy_breakdown.png",
    dpi=150, bbox_inches="tight", facecolor="white",
)
plt.show()

# Print summary table
print(f"\nPer-Agent Accuracy — {LABEL_CR_SEPARATED}:\n")
print(f"  {'Agent':30s}  {'Queries':>8s}  {'Agent Sel.':>10s}  {'Tool Sel.':>10s}")
print(f"  {'-'*30}  {'-'*8}  {'-'*10}  {'-'*10}")
for agent, row in per_agent.sort_values("Tool Selection Accuracy", ascending=False).iterrows():
    pretty = agent.replace("agent_", "").replace("_", " ").title()
    print(
        f"  {pretty:30s}  {int(row['total_queries']):>8d}  "
        f"{row['Agent Selection Accuracy']:>9.1f}%  "
        f"{row['Tool Selection Accuracy']:>9.1f}%"
    )
```

```python

```

```python

```
