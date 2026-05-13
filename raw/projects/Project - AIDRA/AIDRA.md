# AI-DRA — Advanced Intelligence-Driven Risk Assessment

> **AI-DRA** is a multi-agent AI system that analyzes potentially malicious scripts (primarily PowerShell) and produces structured threat reports. It combines a custom fine-tuned LLM orchestrator with a panel of specialized analysis agents, MITRE ATT&CK mapping, live threat-intelligence lookups, and PDF report generation — all running locally on GPU-accelerated hardware.
---

## Table of Contents

1. [Overview](#overview)
2. [Key Capabilities](#key-capabilities)
3. [Architecture](#architecture)
4. [Agent Panel](#agent-panel)
5. [Technology Stack](#technology-stack)
6. [Project Structure](#project-structure)
7. [Getting Started](#getting-started)
8. [Usage](#usage)
9. [Output & Reports](#output--reports)
10. [Configuration](#configuration)
11. [Test Scripts](#test-scripts)

---

## Overview

AI-DRA accepts a script file (PowerShell, batch, or other formats) and runs it through an orchestrated pipeline of large language models, each specialised in a different dimension of threat analysis. The results are merged through a consensus engine and rendered as both a rich terminal report and a professional PDF document.

The orchestrator is a **custom fine-tuned CodeLlama-7B** (PEFT/LoRA adapter, see `Orchestrator/`) that triages the script and coordinates downstream agents. All models run locally with 4-bit quantisation to fit on a single GPU.

---

## Key Capabilities

| Capability | Description |
|---|---|
| **Multi-agent analysis** | Seven specialised agents analyse the script in parallel and their findings are merged via a weighted consensus engine |
| **Orchestrator triage** | Fine-tuned CodeLlama-7B classifies the script type (Ransomware, RAT, Backdoor, Dropper, …) before any agent runs |
| **Deobfuscation** | Detects and decodes Base64, XOR, string-concatenation, and other obfuscation layers |
| **MITRE ATT&CK mapping** | Deterministic pattern matching maps findings to ATT&CK technique IDs with evidence provenance (line numbers + code snippets) |
| **Threat-intelligence lookups** | Live IOC lookups against VirusTotal, AlienVault OTX, and MalwareBazaar |
| **Hallucination prevention** | Every agent claim must be grounded in an actual line of the input script; the HallucinationGuard and ScriptGroundingSystem enforce this |
| **False-positive mitigation** | Context-aware scoring distinguishes administrative/educational scripts from genuine malware |
| **Evidence-based confidence** | Multi-dimensional evidence evaluation produces calibrated confidence scores per finding |
| **PDF report** | Generates a professional, Blue-Chip-style PDF report with code snippets, MITRE IDs, IOC tables, and risk scoring |
| **Verbose logging** | Every run is captured in a timestamped log file for audit and debugging |
| **CLI interface** | User-friendly, Analyst, and Debug verbosity modes via a rich terminal UI |

---

## Architecture

```
Input Script
     │
     ▼
┌─────────────────────────────────────────────────┐
│              CLI / ui_enhanced_cli              │
└──────────────────────┬──────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────┐
│          Orchestrator (Fine-tuned CodeLlama-7B) │
│  • Script triage & classification               │
│  • ScriptContext broadcast to all agents        │
└──────────────────────┬──────────────────────────┘
                       │  LangGraph StateGraph
          ┌────────────┼────────────────────┐
          ▼            ▼                    ▼
  Functional     Deobfuscation         Network
  Analysis       Analysis              Security
  (IBM Granite)  (Stable-Code-3B)      (EXAONE-7.8B)
          │            │                    │
          ▼            ▼                    ▼
  Behavioral     Malware               Threat
  Analysis       Analysis              Intelligence
  (Mistral-7B)   (Mistral-7B)          (Phi-4-Reasoning)
                                            │
                                            ▼
                                    Risk Assessment
                                    (Zephyr-7B)
                                            │
                       ┌────────────────────┘
                       ▼
┌─────────────────────────────────────────────────┐
│  Consensus Engine                               │
│  • Evidence-based weighting                     │
│  • False-positive mitigation                    │
│  • Context-aware threat scoring                 │
│  • MITRE ATT&CK deterministic mapper            │
└──────────────────────┬──────────────────────────┘
                       │
          ┌────────────┼─────────────┐
          ▼            ▼             ▼
     Terminal      JSON file     PDF Report
     Report        output        (ReportLab)
```

The workflow is implemented with **LangGraph** (`StateGraph`) and an internal **AgentBus** for inter-agent communications. A `MemorySaver` checkpoint keeps state across graph steps.

---

## Agent Panel

| Agent | Model | Primary Role |
|---|---|---|
| **Orchestrator** | Fine-tuned CodeLlama-7B (LoRA) | Script triage, threat classification, agent coordination |
| **Functional Analysis** | IBM Granite-8B Code Instruct | Deep code comprehension, function extraction, logic-flow analysis |
| **Deobfuscation Analysis** | Stability AI Stable-Code-3B | Decodes Base64, XOR, string-split obfuscation; reconstructs hidden payloads |
| **Malware Analysis** | Mistral-7B Instruct v0.2 | Malware classification, IOC extraction, threat-signature validation |
| **Network Security** | LG AI EXAONE-Deep-7.8B | Protocol analysis, C2 discovery, DNS/IP/URL indicator extraction |
| **Behavioral Analysis** | Mistral-7B Instruct v0.2 | Attack-chain correlation, behavioral pattern recognition |
| **Threat Intelligence** | Microsoft Phi-4-Reasoning | TTP mapping, campaign linkage, threat-actor attribution |
| **Risk Assessment** | HuggingFace Zephyr-7B Beta | Risk scoring, business-impact analysis, final verdict |

All agents use **4-bit quantisation** (`bitsandbytes`) and share a context window of 8 192 tokens.

---

## Technology Stack

### AI / ML
| Library | Purpose |
|---|---|
| `transformers` 4.43 | Model loading, inference, tokenisation |
| `peft` 0.11 | LoRA adapter loading for the fine-tuned orchestrator |
| `bitsandbytes` 0.45 | 4-bit & 8-bit model quantisation |
| `accelerate` 0.31 | Distributed / multi-GPU utilities |
| `torch` 2.2 + CUDA 12.1 | Deep-learning backend |
| `safetensors` 0.4 | Efficient model weight storage |
| `optimum` 1.19 | Inference optimisations |

### Orchestration & Workflow
| Library | Purpose |
|---|---|
| `langgraph` | StateGraph-based multi-agent workflow |
| `langchain-core` | Message types for inter-agent communication |

### Threat Intelligence APIs
| Source | Usage |
|---|---|
| **VirusTotal** | File hash, domain, IP, and URL reputation |
| **AlienVault OTX** | Threat pulses, IOC lookups, threat-actor correlation |
| **MalwareBazaar** | Malware sample and hash lookups |
| **MITRE ATT&CK** | Local technique database with deterministic pattern mapping |

### Reporting
| Library | Purpose |
|---|---|
| `reportlab` / `fpdf2` | PDF generation |
| `matplotlib` | Charts embedded in reports |
| `Jinja2` | HTML/template rendering |
| `rich` | Terminal UI (tables, progress bars, panels) |

### Supporting Libraries
`fastapi`, `uvicorn`, `pydantic`, `httpx`, `aiohttp`, `requests`, `numpy`, `pandas`, `scikit-learn`, `faiss-cpu`, `pefile`, `capstone`, `lief`, `nltk`, `networkx`, `psutil`, `python-dotenv`, `PyYAML`, `loguru`, `colorama`

---

## Project Structure

```
AI-DRA/
├── src/                          # Main application source
│   ├── __main__.py               # Module entry point  (python3 -m src)
│   ├── cli.py                    # CLI argument parsing & pipeline kick-off
│   ├── ui_enhanced_cli.py        # Rich terminal UI & startup animation
│   ├── settings.py               # Config: model paths, API keys, agent registry
│   └── core/
│       ├── agents/               # Specialised agent classes
│       │   ├── base.py           # BaseAgent + ScriptGroundingSystem
│       │   ├── functional.py     # Functional analysis (IBM Granite)
│       │   ├── deobfuscation.py  # Deobfuscation (Stable-Code-3B)
│       │   ├── malware.py        # Malware analysis (Mistral-7B)
│       │   ├── network.py        # Network security (EXAONE)
│       │   ├── behavioral.py     # Behavioral analysis (Mistral-7B)
│       │   ├── threat.py         # Threat intelligence (Phi-4)
│       │   └── risk.py           # Risk assessment (Zephyr-7B)
│       ├── workflow.py           # LangGraph StateGraph orchestration
│       ├── consensus.py          # Multi-agent consensus & voting
│       ├── mitre_mapper.py       # Deterministic MITRE ATT&CK mapping
│       ├── hallucination_guard.py# LLM hallucination detection & prevention
│       ├── confidence.py         # Evidence-based confidence calibration
│       ├── false_positive_*      # False-positive mitigation subsystem
│       ├── script_context.py     # ScriptContext dataclass (type, goals, indicators)
│       ├── artifacts.py          # AgentResult / AgentCommunication types
│       ├── agent_bus.py          # Internal inter-agent communication bus
│       ├── pdf_report_generator.py # PDF report builder
│       ├── ti/                   # Threat Intelligence integrations
│       │   ├── vt.py             # VirusTotal client
│       │   ├── otx.py            # AlienVault OTX client
│       │   ├── malwarebazaar.py  # MalwareBazaar client
│       │   └── aggregator.py     # Multi-source IOC aggregator
│       ├── deobf/
│       │   └── engine.py         # Deobfuscation engine
│       ├── detection/
│       │   └── threat_detector.py
│       ├── render/               # Output rendering
│       │   ├── console.py        # Rich terminal output
│       │   ├── json_out.py       # JSON export
│       │   └── report.py         # Report assembly
│       └── ui/
│           └── components.py     # Terminal UI components
├── Orchestrator/                 # Fine-tuned LoRA adapter weights
│   ├── adapter_config.json       # PEFT config (base: CodeLlama-7b-Instruct-hf)
│   └── adapter_model.safetensors # LoRA weights
├── Test Scripts/                 # Sample scripts for testing & demos
│   ├── encryptor.txt             # Ransomware sample
│   ├── reverse_shell_2025.txt    # Reverse shell
│   ├── lsass.txt                 # LSASS credential dumping
│   ├── AMSI_bypass_2021_09.txt   # AMSI bypass
│   └── …                        # More malware archetypes
├── Archive/
│   ├── requirements_linux_versioned.txt
│   └── requirements_linux_unversioned.txt
├── data/
│   ├── logs/                     # Per-run verbose logs
│   ├── mitre_cache/              # Cached MITRE ATT&CK data
│   └── tmp/
├── Verbose Logs/                 # Analysis run logs
├── run_aidra.sh                  # Shell launcher (sets CUDA env)
└── .env                          # API key overrides (not committed)
```

---

## Getting Started

### Prerequisites

- Linux x86\_64 with an NVIDIA GPU (≥ 16 GB VRAM recommended; 24+ GB for parallel agents)
- CUDA 12.1 drivers
- Python 3.10+

### Installation

```bash
# 1. Clone the repo
git clone https://github.com/cr-ItamarHershko/AI-DRA.git
cd AI-DRA

# 2. Create a virtual environment
python3 -m venv .venv && source .venv/bin/activate

# 3. Install dependencies (GPU build)
pip install -r Archive/requirements_linux_versioned.txt

# 4. (Optional) Copy and edit the .env file
cp .env.example .env   # Set VT_API_KEY, MB_API_KEY, etc.
```

> **CPU-only**: Replace the three `torch*` lines in `requirements_linux_versioned.txt` with the CPU wheels from [pytorch.org](https://pytorch.org/get-started/locally/). Inference will be significantly slower.
### Environment Variables

| Variable | Description |
|---|---|
| `VT_API_KEY` | VirusTotal API key |
| `MB_API_KEY` | MalwareBazaar API key |
| `HF_HOME` | HuggingFace cache directory |
| `TRANSFORMERS_CACHE` | Transformers model cache |
| `AIDRA_CONFIG_DIR` | Override config directory |
| `AIDRA_CACHE_DIR` | Override application cache |
| `CUDA_VISIBLE_DEVICES` | GPU selection (default: `0`) |

---

## Usage

### Run via shell launcher (recommended)

```bash
./run_aidra.sh <script_file> [options]
```

### Run as Python module

```bash
python3 -m src <script_file> [options]
```

### CLI options

```
positional:
  script_file           Path to the script to analyse
options:
  --output-dir DIR      Directory for report output (default: ./data/logs)
  --format {pdf,json,console}
                        Output format(s); may be repeated
  --verbosity {user_friendly,analyst,debug}
                        Controls how much detail is shown (default: user_friendly)
  --no-ti               Skip live threat-intelligence lookups
  --agents AGENT [...]  Run only a subset of agents
```

### Examples

```bash
# Analyse a PowerShell script with default settings
./run_aidra.sh "Test Scripts/encryptor.txt"

# Analyst mode with JSON + PDF output
./run_aidra.sh "Test Scripts/reverse_shell_2025.txt" --verbosity analyst --format pdf --format json

# Skip TI lookups (offline / air-gapped)
./run_aidra.sh myScript.ps1 --no-ti
```

---

## Output & Reports

Every run produces:

| Output | Description |
|---|---|
| **Terminal report** | Colour-coded threat summary with MITRE IDs, agent verdicts, and confidence scores |
| **PDF report** | Professional Blue-Chip-style document with code snippets (line numbers), evidence tables, IOC listings, MITRE ATT&CK matrix highlights, and risk score |
| **JSON** | Machine-readable full analysis result including all agent findings and consensus data |
| **Verbose log** | Timestamped full text log saved to `Verbose Logs/` for every run |

### Threat Classifications

The system classifies scripts into one of:

`RANSOMWARE` · `SURVEILLANCE` · `CREDENTIAL_THEFT` · `RAT` · `BACKDOOR` · `DROPPER` · `WIPER` · `CRYPTOMINER` · `UNKNOWN`

Severity levels: **CRITICAL** → **HIGH** → **MEDIUM** → **LOW** → **BENIGN**

---

## Configuration

Agent-to-model assignments, quantisation settings, and VRAM budgets are defined in `src/settings.py` in the `AGENT_MODEL_CONFIGS` dictionary.

To swap a model, update the `"model"` field for the relevant agent and add the new model path to `REGISTERED_MODELS`. All models must be reachable via HuggingFace Hub or a local path.

To use the fine-tuned orchestrator, place the LoRA adapter files under `/mnt/localdisk/datascience/jupyterlabenv/AI-DRA/Orchestrator/` (or override the path in `settings.py`). When the adapter is not found, the system automatically falls back to the vanilla `codellama/CodeLlama-7b-Instruct-hf` model.

---

## Test Scripts

The `Test Scripts/` directory contains representative PowerShell samples for development and demonstration:

| File | Threat Type |
|---|---|
| `encryptor.txt` | Ransomware with AES file encryption |
| `reverse_shell_2025.txt` | TCP reverse shell |
| `reverse_tcp.txt` | Meterpreter-style reverse TCP |
| `lsass.txt` | LSASS memory dump / credential theft |
| `AMSI_bypass_2021_09.txt` | AMSI bypass / defense evasion |
| `minidump.txt` | Process memory dumping |
| `memorymanipulation.txt` | In-memory execution techniques |
| `spy.txt` | Surveillance / keylogging |
| `harvesting.txt` | Credential & data harvesting |
| `xor_ez.txt` | XOR-obfuscated payload |
| `obfuscated_payload_test.txt` | Multi-layer obfuscation |
| `test 1 simple bening script.txt` | Benign baseline |
| `test 2 obfuscated.txt` | Obfuscated benign script |
| `test 3 malicious.txt` | Generic malicious script |

> ⚠️ These scripts are **for analysis testing only**. Never execute them on a production system.
---

## License

See repository licence file for terms.