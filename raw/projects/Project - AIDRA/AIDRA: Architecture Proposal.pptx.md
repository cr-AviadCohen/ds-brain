# AIDRA: Architecture Proposal.pptx

<!-- Slide number: 1 -->
# Architecture Proposal for AIDRA

Slack channel: #aidra

### Notes:

<!-- Slide number: 2 -->
Motivation
Analysts juggle hundreds of files, scripts, and memory alerts each day,
making consistent high-quality triage a challenge.
Alert Overload – sheer volume makes it hard to spot truly critical threats.
Tool Hopping – jumping between consoles to gather context wastes minutes per alert.
Incomplete Context – raw alerts lack enrichment, forcing analysts to guess intent.
Manual Correlation – stitching file, script, and memory evidence together is slow.
Triage Fatigue – repetitive low-value alerts drain focus and cause mistakes.
Knowledge Gaps – insights stay in individual heads, so handoffs lose vital detail.

![](GoogleShape236p53.jpg)

### Notes:

<!-- Slide number: 3 -->
Our Approach - AI-DRA
AI-DRA, A Multi-Agent Framework for Advanced Malware Analysis
AIDRA replaces one-size-fits-all models with a team of specialized SLM agents managed by an Orchestrator.
Each agent in our system acts as a specialist, analyzing a distinct aspect of the script parsed into separate inputs, offering a unique perspective on the same malware (binary, behavior, threat-intel, network, etc.).
Agents’ findings then passes to a Consensus Engine that produces a clear, trusted report, enriched by local analysis tools. (e.g., IOC extraction, MITRE mapping).

### Notes:

<!-- Slide number: 4 -->
AIDRA Architecture

![](GoogleShape251p55.jpg)

### Notes:
AIDRA Architecturehttps://app.diagrams.net/#G1DOd6I-BwK0xCdqlvuZnXcoBogCeir0s6#%7B%22pageId%22%3A%22GY5NjVtAObg3Nfaqt_wO%22%7D

<!-- Slide number: 5 -->
# Example Results
Slack channel: #aidra

### Notes:

<!-- Slide number: 6 -->
PDF Report Example - AIDRA

### Notes:

<!-- Slide number: 7 -->
PDF Report Example - Assembly LLM

![](GoogleShape268p58.jpg)

### Notes:

<!-- Slide number: 8 -->
Use cases
Customer Sample Submission:Customers can submit samples directly from the platform into the analysis environment for automated processing.
Service Engineer Workflow (IR/SOC):A service engineer who needs an immediate analysis for a sample can submit it independently, either through the platform, via API, or by mcp server. This enables fast, on-demand investigation workflows.
SAM Security AI Mesh Integration:AI-driven security systems collaborate by sharing samples across tools.Wrapped API with an MCP server so AI-DRA and other AI agents can access, analyze, and return structured JSON outputs.

### Notes:

<!-- Slide number: 9 -->
Fine Tune - Evaluation Results

![](GoogleShape279p60.jpg)

### Notes:

<!-- Slide number: 10 -->

Architecture

MCP (API)
Web UI
REST API
▼

API Gateway
Redis Queue
→
FastAPI
P1-P4 Priority
▼

AIDRAOrchestrator + 4 Agents

Orchestrator
Code Analyst
Threat Class
Security
Risk
CodeLlama 4GB
Gemma 5GB
Mistral 4GB
StarCoder 4GB
Phi-4 7GB
▼

JSON + PDF
S3 Storage

### Notes:

<!-- Slide number: 11 -->

Submission Pipeline

STAGE 1
STAGE 2
STAGE 3
STAGE 4
STAGE 5
Submit
Queue
Triage
Analyze
Report
Script uploaded via API or UI
Priority assigned, job created
Orchestrator analyzes script
4 agents run in parallel
Consensus + output
<100ms
instant
5-10s
15-30s
10s

Total End-to-End Time: ~45 seconds

Async Response
Retry on Failure
Output Formats
Client gets job_id immediately, polls or uses WebSocket for status
Auto-retry 3x with exponential backoff, then dead letter queue
JSON API response, PDF report, stored in S3

### Notes:

<!-- Slide number: 12 -->

Analysis Stages

CodeLlama-7B - Initial Triage

5-10s
ORCHESTRATOR
Entropy analysis, artifact extraction, pattern matching, capability detection, semantic parsing, task planning

AGENT 1
AGENT 2
AGENT 3
AGENT 4
Code Analyst
Threat Classifier
Security Analyst
Risk Assessor
Gemma-3-4B (5GB)
Mistral-7B (4GB)
StarCoder2-7B (4GB)
Phi-4 (7GB)
Deobfuscation, control flow, data flow, API calls
Malware family, MITRE ATT&CK mapping, IOC extraction
Vuln patterns, privilege escalation, persistence
Risk scoring, business impact, recommendations

Weighted Voting + Final Report

10s
CONSENSUS
Conflict resolution, confidence scoring, JSON + PDF generation, S3 upload

### Notes:

<!-- Slide number: 13 -->

Multiple Requests
How It Works
Capacity Per Node

Queue-Based Processing

All requests go to Redis queue. Workers pull jobs as capacity frees. No request lost.
Concurrent jobs: 3-5
Jobs per hour: 40
Jobs per day: 960
Jobs per month: 30,000

Execution
4 agents run per job. Models share GPU. 3-5 jobs process simultaneously.

Scaling
Priority Scheduling
Each GPU node adds ~40 jobs/hour. 2 nodes ≈ 80/hr.
P1 jobs jump queue. Bulk uploads run background. Fair scheduling per customer.

### Notes:

<!-- Slide number: 14 -->

Training Hardware Costs
Cost Options

Cloud Spot (Recommended)
Training Requirements
OCI VM.GPU.A100.40G.A preemptible (1X A100 40GB), 72 hrs
$100-120

Fine-tuning LoRA adapters needs: GPU: 1x A100 40GB
RAM: 64 GB
Storage: 500GB NVMe
Time: 24-72 hours
per training session

Cloud On-Demand
OCI VM.GPU.A100.40G.A preemptible (1X A100 40GB), 72 hrs
$220

Training is One-Time
per training run
Fine-tune once, deploy forever. Re-train only for major updates.

Own Hardware (Long-term)
A100 workstation: ~$15,000 one-time. ROI after 6-8 runs.

### Notes:

<!-- Slide number: 15 -->

Submission Cost
Monthly Operating Cost
Per Analysis Cost

STANDARD
COMPONENT          STANDARD    BUDGET
GPU (g5 xlarge)           $1,006          $500
Storage+LB+Network     $50             $50
Monitoring                       $10             $10
─────────────────────────────────────
TOTAL                             $1,066      $560
$0.04

BUDGET (SPOT)
$0.02

Scaling
Per additional node: 30k/mo for ~$1,000

at 30K analyses/month

### Notes:

<!-- Slide number: 16 -->

Annual Total Cost
Per Analysis Cost

360k requests
Annual Operating Cost

1 kubernetes = 1,066$ x 12 months = 12,792$

$0.06

Annual Training
800$ X 10 times a year = 8,000$

Add ~1 GPU node per 30k additional analyses/month (~$1,000 per node)
Scaling
720k requests (2x kubernetes)
$0.045

### Notes:

<!-- Slide number: 17 -->
Questions:
https://cybereason.atlassian.net/wiki/spaces/CE/pages/32199147523/2025-12-02+Design+Review+-+AIDRA+Initiative

### Notes:

<!-- Slide number: 18 -->
# Thank You!
Slack channel: #aidra

### Notes:

<!-- Slide number: 19 -->

![](GoogleShape518p70.jpg)

### Notes:

<!-- Slide number: 20 -->
# Architecture Proposal
for Assembly LLM

Slack channel: #aidra

### Notes:

<!-- Slide number: 21 -->

![](GoogleShape529p72.jpg)

### Notes:

<!-- Slide number: 22 -->

![](GoogleShape534p73.jpg)

### Notes:
