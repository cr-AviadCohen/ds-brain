# AIDRA-GPT Integration

> 🛡️ AIDRA (AI-Driven Risk Assessment) — A production-grade, language-agnostic malware analysis framework powered by a multi-agent AI system using Azure OpenAI GPT-5.2. Because it leverages GPT's universal code understanding, AIDRA analyzes any scripting or programming language — not just PowerShell. Evidence-first threat analysis with 200+ MITRE ATT&CK techniques, 8 detection engines, and professional reporting.

---

### Quick Stats

Metric
	
Value
	
Metric
	
Value

Python Files
	
296
	
Detection Engines
	
8

Lines of Code
	
100,000+
	
Deobfuscation Layers
	
6

AI Agents
	
4
	
Script Languages
	
Any (GPT-powered)

MITRE Techniques
	
200+
	
TI Integrations
	
3

Ransomware Detection
	
97%
	
False Positive Rate
	
Under 2%

RAT Detection
	
94%
	
Azure Analysis Time
	
10-15s

---

### 4-Agent System

Agent
	
Model
	
Role
	
Weight

Code Analyst
	
google/gemma-3-9b-it
	
Code structure, behavioral patterns, system interactions
	
30%

Threat Classifier
	
mistralai/Mistral-7B-v0.3
	
Malware families, MITRE ATT&CK mapping, threat attribution
	
30%

Security Analyst
	
StarCoder2-7B
	
Obfuscation analysis, network IOCs, injection techniques
	
25%

Risk Assessor
	
Phi-4 (reasoning-focused)
	
Business impact, compliance, validates other agents
	
15%

---

### LLM Backends

#### Azure OpenAI (Recommended)
- Model: GPT-5.2 via Azure API
- GPU: Not required
- Speed: 10-15 seconds per analysis
- Quality: Enterprise-grade, production-ready scaling

#### Local HuggingFace
- Models: 4-bit quantized via bitsandbytes
- GPU: 24 GB VRAM required (NVIDIA)
- Speed: 30-45 seconds per analysis
- Control: Full model ownership, no external API calls

---

### Key Capabilities

<details><summary>Evidence-First Analysis</summary>

</details>

<details><summary>Multi-Layer Deobfuscation (6 Layers)</summary>

</details>

<details><summary>8 Specialized Detection Engines</summary>

</details>

<details><summary>Malware Family Detection</summary>

</details>

<details><summary>MITRE ATT&CK Mapping (200+ Techniques)</summary>

</details>

<details><summary>Threat Intelligence Integration</summary>

</details>

<details><summary>Professional Report Generation</summary>

</details>

<details><summary>Language-Agnostic Analysis (GPT-Powered)</summary>

</details>

<details><summary>Behavioral Intent Engine</summary>

</details>

<details><summary>Langfuse Observability (Optional)</summary>

</details>

---

### Analysis Pipeline
1. Script Input and Validation — File size check, encoding detection, script type detection, hash calculation for TI lookups
1. Context Analysis — Demo vs real threat detection, entropy calculation, threat goal inference, agent routing strategy
1. Artifact Extraction — PowerShell AST parsing, function/variable/cmdlet extraction, IOC detection (URLs, domains, IPs, hashes, file paths, registry keys)
1. Deobfuscation — 6-layer cascade with execution flow tracing, variable dependency resolution, iterative layer peeling
1. Agent Analysis — 4 specialized agents analyze deobfuscated script independently with evidence collection and confidence scoring
1. Consensus and Reporting — Weighted verdict aggregation (MALICIOUS/SUSPICIOUS/BENIGN/UNKNOWN), finding deduplication, PDF/JSON/console output

---

### Configuration

```
# LLM Backend Selection
LLM_BACKEND=azure  # "azure" or "hf"

# Azure OpenAI
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
AZURE_OPENAI_API_KEY=your_api_key
AZURE_OPENAI_DEPLOYMENT=your-deployment-name

# Threat Intelligence
VT_API_KEY=your_virustotal_key
MB_API_KEY=your_malwarebazaar_key

# Langfuse Observability (optional)
LANGFUSE_SECRET_KEY=sk-lf-...
LANGFUSE_PUBLIC_KEY=pk-lf-...

​
```

---

### Quick Start

```
cd AI-DRA
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python3 -m aidra --demo          # Test with demo script
python3 -m aidra --script malware.ps1  # Analyze a file
python3 -m aidra --health-check  # System health check

​
```

---

### Full Documentation

AIDRA - AI-Driven Risk Assessment: Complete Project Documentation — Full project structure, all components, configuration, dependencies

AIDRA Technical Deep Dive: Architecture & Implementation Details — Data structures, prompt engineering, detection engines, deobfuscation internals

AIDRA: Features, Capabilities & Usage Guide — Detailed feature breakdown, usage examples, troubleshooting

---

> 📂 Repository: github.com/cr-ItamarHershko/AI-DRA | Branch: aidra-LLM | Language: Python 3.9+
- 📄 [AIDRA - AI-Driven Risk Assessment: Complete Project Documentation](https://www.notion.so/AIDRA-AI-Driven-Risk-Assessment-Complete-Project-Documentation-339ae23bae1d81b0b1b3e30c9fbcab49?pvs=25)
- 📄 [AIDRA Technical Deep Dive: Architecture & Implementation Details](https://www.notion.so/AIDRA-Technical-Deep-Dive-Architecture-Implementation-Details-339ae23bae1d8117b2a1ffde26431c48?pvs=25)
- 📄 [AIDRA: Features, Capabilities & Usage Guide](https://www.notion.so/AIDRA-Features-Capabilities-Usage-Guide-339ae23bae1d81e9b116df312fd78bea?pvs=25)

Git - https://github.com/cybereason-labs/itamar-h/tree/AIDRA-DEV
