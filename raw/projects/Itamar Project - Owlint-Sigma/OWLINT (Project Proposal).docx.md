# OWLINT (Project Proposal).docx

# **OWLINT - Cyber Threat Intelligence Engine**

Automated CTI pipeline that ingests threat articles and feeds, filters noise using AI, and generates production-quality YARA detection rules.

## **Table of Contents**

1. Overview
2. Features
3. Architecture
4. Installation
5. Configuration
6. Usage
7. Output Structure
8. YARA Rule Quality
9. Feed Ingestion
10. Docker Deployment
11. Observability
12. Testing
13. Project Structure
14. Troubleshooting
15. License

## **Overview**

OWLINT is an end-to-end threat intelligence automation tool that transforms raw threat articles and IOC feeds into actionable YARA detection rules. The pipeline uses a dual-agent AI system to filter noise, extract indicators, and generate validated rules ready for production deployment.

Key Capabilities:

* Ingest threat intelligence from URLs or bulk feeds
* AI-powered triage to classify actionable vs. noise content
* Automated YARA rule generation with Red Team validation
* Syntax verification and false positive checking
* Structured output with full metadata and source tracking

## **Features**

### Streamlit Web UI

Modern web interface for threat intelligence operations:

* Quick Test - Paste any threat article URL and generate YARA rules in real-time
* Bulk Feeds - Fetch IOCs from abuse.ch feeds (MalwareBazaar, ThreatFox, URLhaus, Feodo Tracker)
* Results Library - Browse, download, and manage generated YARA rules
* Live Activity - Real-time pipeline execution monitoring

### Dual-Agent System

* Triage Agent - Classifies content as actionable or noise using AI
* Forge Agent - Generates precision YARA rules with Red Team validation

### Feed Ingestion (abuse.ch)

* MalwareBazaar - Malware sample hashes with signatures and variants
* ThreatFox - IOCs (IPs, domains, URLs) with threat classification
* URLhaus - Malicious URL tracking
* Feodo Tracker - Botnet C2 server tracking

## **Architecture**

The pipeline processes threat intelligence through five sequential stages:

URL > INGEST > TRIAGE > FORGE > QA > DELIVER

1. Ingest - Scrapes article content and deduplicates against previously processed URLs
2. Triage - AI classification using a lightweight LLM to filter out non-actionable content
3. Forge - Generates YARA rules using a smart loop with Red Team false positive validation
4. QA - Syntax validation and optional VirusTotal integration
5. Deliver - Exports rules (.yar) and metadata (.json) to structured output directories

## **Installation**

### Prerequisites

* Python 3.9 or higher
* Redis (optional, for URL deduplication)
* PostgreSQL (optional, for persistent storage)

### Steps

# Clone the repository

git clone https://github.com/levelblue/owlint.git

cd OWLINT

# Install dependencies

pip install -r requirements.txt



## **Configuration**

Create a .env file in the project root with the following variables.

### Required: LLM Provider

Choose one of the following:

OpenAI:

OPENAI\_API\_KEY=sk-...

Azure OpenAI:

AZURE\_OPENAI\_API\_KEY=your-key

AZURE\_OPENAI\_ENDPOINT=https://your-endpoint.openai.azure.com/

AZURE\_OPENAI\_API\_VERSION=2025-04-01-preview

AZURE\_OPENAI\_DEPLOYMENT=gpt-4o-mini

### Optional: Observability

LANGFUSE\_PUBLIC\_KEY=pk-lf-xxx

LANGFUSE\_SECRET\_KEY=sk-lf-xxx

LANGFUSE\_HOST=https://cloud.langfuse.com

### Optional: Infrastructure

REDIS\_URL=redis://localhost:6379/0

DATABASE\_URL=postgresql://localhost:5432/owlint



## **Usage**

### Web UI (Recommended)

python3 -m website

This opens a browser at http://localhost:8501

Features:

* LevelBlue branded interface
* Graceful shutdown with Ctrl+C
* API key validation on startup
* Real-time log streaming

### Command Line Interface

Single URL:

python3 -m owlint "https://thehackernews.com/2026/01/example-malware.html"

Interactive mode:

python3 -m owlint

Skip deduplication:

python3 -m owlint "https://example.com/article" --skip-dedupe



## **Output Structure**

output/

├── rules/ # YARA rules (named by threat)

│ └── rule\_AmnesiaRAT\_V1.yar

├── events/ # Event metadata JSON

│ └── event\_AmnesiaRAT\_V1.json

├── logs/ # Pipeline logs

│ └── session\_current.log

└── usage/ # LLM usage reports

└── usage\_20260201\_175400.json



## **YARA Rule Quality**

Generated rules follow professional standards:

rule AmnesiaRAT\_V1

{

meta:

id = "unique-uuid"

author = "OWLINT"

creation\_date = "2026-01-31"

source\_url = "https://article.url"

score = 75

stability = "Verified"

description = "Detection for AmnesiaRAT trojan"

classification = "RAT"

tags = "amnesia,rat,stealer"

mitre = "T1055,T1082"

strings:

// Group 1: Unique identifiers

$id1 = "AmnesiaRAT\_mutex"

$id2 = "config.dat"

// Group 2: IOCs (from article)

$ioc1 = "malicious.c2.com"

// Group 3: Behaviors

$behav1 = "screenshot\_capture"

condition:

2 of ($id\*) or (1 of ($ioc\*) and 1 of ($behav\*))

}

### Quality Guarantees

* Targeted Strings - 5-10 specific strings, no generic Windows paths
* Smart Conditions - Logical combinations, not "any of them"
* Grouped Strings - Organized by type: $id\*, $ioc\*, $behav\*
* Red Team Validated - False positive check before export
* IOC Extraction - Indicators extracted from article content
* Source Tracking - Original URL preserved in metadata

## **Feed Ingestion**

### Smart Item Limiting

Choose how many IOCs to fetch per request: 10, 25, 50, 100, 250, 500, 1000, or All items.

### Data Display

* Variant and signature names shown prominently
* Full URLs displayed without truncation
* Complete hashes: SHA256, MD5, SHA1
* Clickable links to original sources
* CSV export with complete data

## **Docker Deployment**

### Using Docker Compose

docker-compose up --build

### Standalone Container

docker build -t owlint .

docker run -p 8501:8501 --env-file .env owlint



## **Observability**

OWLINT integrates with LangFuse for pipeline observability.
A free tier is available at cloud.langfuse.com.

Tracked Metrics:

* Token usage per agent (triage/forge)
* Cost per LLM call
* Input/output character counts
* Session-based grouping

## **Testing**

# Run unit tests

pytest tests/ -v

# Test single URL (skip deduplication)

python3 -m owlint "https://example.com/threat-article" --skip-dedupe



## **Project Structure**

OWLINT/

├── owlint/ # Core pipeline package

│ ├── core/

│ │ ├── config.py # Settings (Azure, LangFuse, etc.)

│ │ ├── graph.py # LangGraph pipeline orchestration

│ │ ├── logger.py # Structured logging with session support

│ │ ├── models.py # Pydantic data models

│ │ ├── observability.py # LangFuse integration

│ │ ├── sources.py # Feed source definitions

│ │ └── llm/ # Modular LLM providers

│ │ ├── base.py # BaseLLM abstract class

│ │ ├── factory.py # get\_llm() factory

│ │ └── providers/

│ │ ├── azure\_openai.py

│ │ ├── openai\_provider.py

│ │ └── huggingface.py

│ ├── services/

│ │ ├── ingestion/

│ │ │ ├── dedupe.py # Redis URL deduplication

│ │ │ ├── feed\_service.py # abuse.ch feed handlers

│ │ │ └── scraper\_service.py # Article scraping

│ │ ├── triage/

│ │ │ └── classifier.py # AI noise filter

│ │ ├── forge/

│ │ │ └── generator.py # YARA rule generator

│ │ ├── qa/

│ │ │ ├── validator.py # Syntax validation

│ │ │ └── virustotal.py # VT integration

│ │ └── delivery/

│ │ └── exporter.py # File export

│ ├── main.py # Pipeline entry point

│ └── cli.py # Interactive CLI

│

├── website/ # Streamlit Web UI

│ ├── \_\_main\_\_.py # Server launcher with signal handling

│ ├── app.py # Main Streamlit application

│ └── assets/ # Static assets (logos)

│

├── output/ # Generated artifacts

├── tests/ # Unit tests

├── requirements.txt # Python dependencies

├── Dockerfile # Container build

├── docker-compose.yml # Container orchestration

└── .env # Environment config (not in git)



## **Troubleshooting**

API Key Errors - Ensure your .env file contains valid credentials. The web UI validates API keys on startup and will display an error if they are missing or invalid.

Redis Connection Issues - If Redis is unavailable, deduplication will be skipped. Use the --skip-dedupe flag to explicitly bypass this check.

YARA Syntax Errors - The QA stage validates all generated rules. If syntax errors persist, check the logs in output/logs/ for detailed error messages.

Web UI Not Loading - Verify that port 8501 is not in use by another application. Use lsof -i :8501 to check for conflicts.

**Archive Information (old):**

The Problem: Traditional Threat Intelligence (CTI) is noisy, expensive, and passive. Security teams are drowning in duplicate news reports, and manual rule creation (YARA) is too slow to catch modern threats.

The Solution: OWLINT is a "Zero-Cost" Cyber Intelligence Pipeline. It is an automated, self-healing system that ingests raw data, filters out 85% of the noise using cheap compute, and uses high-end AI only when necessary to generate valid detection rules.

Why It Is Necessary:

* Cost Efficiency: "Filter Early, Compute Late." By using Redis caching and Small Language Models (SLMs) at the edge, it reduces cloud AI costs by ~90% compared to sending everything to GPT-4.
* Operational Security: It uses "Western-only" models (Llama, Mistral) in production, ensuring full data sovereignty for defense/government use cases.
* Reliability: Unlike standard AI tools that hallucinate broken code, OWLINT features a Self-Healing QA Loop that automatically fixes syntax errors and prevents False Positives before a human ever sees the rule.

### Architectural Walkthrough (Step-by-Step)

#### 1. INGESTION LAYER (The Gatekeeper)

* Goal: Stop duplicates and sanitize data to minimize token usage.
* How it works:
  + API Gateway & Auth: All incoming traffic is immediately tagged with a TenantID, ensuring customer data is strictly isolated (Multi-Tenancy).
  + Redis Cache (Zero-Cost Dedupe): Before processing a URL, the system checks its hash against a 24-hour cache. If the report has been seen before, it is dropped instantly. This saves compute resources on viral news stories.
  + MCP Scraper: We use a specialized stack (Puppeteer + Readability.js) to strip ads and HTML clutter, converting the report into clean Markdown. This reduces the "reading cost" for the AI by ~40%.

#### 2. TRIAGE LAYER (The Smart Filter)

* Goal: Filter out non-threats using the cheapest possible hardware.
* How it works:
  + Redis Queue: Acts as a shock absorber for high-volume traffic bursts.
  + Small AI Agent: Instead of a massive brain, we use a specialized "Small Language Model" (Llama-3.2-3B / Phi-4 / Gemma-3). It performs a fast binary check: *"Is this a technical threat report?"* vs. *"Is this a marketing blog?"*
  + The Outcome: Noise (marketing, patch notes) is archived immediately. Only high-signal technical data is promoted to the next stage.

#### 3. THE FORGE (The Intelligence Engine)

* Goal: Securely extract logic and generate high-fidelity detection rules.
* How it works:
  + OWLINET Engine: The core reasoning unit. In production, this runs on a Self-Hosted Fine-Tuned Model (Llama-3-70B or Mistral Codestral), ensuring no sensitive data leaves the secure environment.
  + RAG (Retrieval Augmented Generation): The AI doesn't guess syntax. It queries a Vector DB to retrieve "Golden Templates" (verified YARA examples) and strict syntax guides to ensure the generated code follows professional standards.
  + Orchestration: Managed by LangGraph to handle complex logic states and LangFuse to track exact costs per tenant.

#### 4. SELF-HEALING QA (The Safety Net)

* Goal: Guarantee 100% executable code without human intervention.
* How it works:
  + Syntax Check: The system attempts to compile the YARA rule. If it fails, the error is captured and sent *back* to the AI engine to fix itself (Self-Correction Loop).
  + False Positive (FP) Check: The valid rule is tested against a Clean File Index (a database of known safe files like calc.exe). If the rule matches safe files, it is rejected and hardened to prevent operational disruption.

#### 5. DELIVERY & ALERTING (Active Response)

* Goal: Turn static reports into active defense.
* How it works:
  + Final Output: The customer receives a valid .yar file and an enriched JSON report.
  + Active Enrichment (The "Killer Feature"): The system doesn't just store data; it pushes extracted IOCs directly to the XDR / MalOp API. It automatically updates open investigations if the new intelligence matches active alerts, effectively acting as an automated Tier-2 Analyst.

Architecture Proposal

https://app.diagrams.net/#G1hpzezWbxjNNa3I9i31wpmGheOxd1TMVK#%7B%22pageId%22%3A%229v0DR0Yg2YtPIHWuoYc1%22%7D

![](data:image/png;base64...)

![](data:image/png;base64...)

New architecture

<https://app.diagrams.net/#G1d3OEYzom_qLpmFM7Qq22Y30r-PtPJU1o#%7B%22pageId%22%3A%22BdP_quTBt4sy-8ITzKuk%22%7D>

Old architecture

<https://app.diagrams.net/#G1hpzezWbxjNNa3I9i31wpmGheOxd1TMVK#%7B%22pageId%22%3A%229v0DR0Yg2YtPIHWuoYc1%22%7D>

Simplified Architecture

<https://app.diagrams.net/#G1fjUjYt1NVPue6E2x4JhHNVSmTTZD95rb#%7B%22pageId%22%3A%22DFIVSFgR_qa1bM05ao0R%22%7D>

For any assistance please contact Itamar Hershko at itamar.hershko@cybereason.com
