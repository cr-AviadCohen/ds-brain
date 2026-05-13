# LevelBlue-Cybereason-AIDRA.pptx

<!-- Slide number: 1 -->
# AI - Detection & Response Analysis
(AI-DRA)
Itamar Hershko, Hen Ashkenazi, Aviad Cohen, Noa Perach Novogroder

### Notes:

<!-- Slide number: 2 -->
AI for EP Security
The Problem / Motivation
AI-DRA:
Scripts LLM
Assembly LLM
Next steps

![](GoogleShape2456g3928bbd50d6_0_551.jpg)

### Notes:
AI for EP Security
AIDRA as a Framework - #key idea, components, architecture, example (ps scripts as a poc, and noa for assembly)
Powershell scripts DEMO #(as poc)
LLM Assembly DEMO #(noa’s poc)
Next steps

<!-- Slide number: 3 -->
# AI For Endpoint Security (EP)
Objective:
Leverage AI to strengthen endpoint security,improving detection accuracy, accelerating investigations, and maximizing analyst efficiency.
How AI Improves EP Security:
Automates malware and behavioral analysis.
Correlates endpoint activity into a full attack story.
Prioritizes alerts based on real risk and impact.
Reduces manual investigation and noise.
Assists analysts with clear insights and response guidance.
Outcome:
Faster investigations.
Higher detection accuracy.
Scalable, AI-driven security operations.

Detection Engines

Improved Coverage
Better Accuracy
Advanced patterns
1

Security Analytics

Saves Triage time
Detailed Detections & Reports
Reduce costs & Labor
2

UX Simplicity

Native language interfaces
Guidance & Recommendations
Low entry bar - Commodity
3

### Notes:
[Hen]

We need to integrate AI in our products to stay relevant in race (as everybody does)

<!-- Slide number: 4 -->
# Motivation
Analysts juggle hundreds of files, scripts, and memory alerts
as part of the triage process.
Alert Overload & Triage Fatigue:High volume makes it hard to spot truly critical threats while repetitive low-value alerts drain focus and cause mistakes.
Incomplete Context:Raw alerts lack enrichment, forcing analysts to guess intent.
Manual Correlation & Tool Hopping:Stitching file, script, and memory evidence together is slow and might require switching between different tools.
Knowledge Gaps:Some steps requires a higher tier of experty or capability.

### Notes:
[Itamar]

All bullets are because human in the loop, not automated.

<!-- Slide number: 5 -->
# Solution definitions
AI-DRA
A Multi-Agent Framework for Advanced Malware Analysis (scripts/binary), leveraging GenAI
Scripts LLM
Language agnostic LLM pipeline for various scripts languages.
Assembly LLM
Assembly-LLM translates raw assembly code into a structured, human-readable behavioral story of a PE file using program structure and semantic context.

### Notes:
[Aviad]
To solve the problems/motivations presented earlier, we came up with AIDRA.
AIDRA is a multi-agent framework for Advanced Malware Analysis, Leveraging Generative AI.
AIDRA is Language agnostic and can support many types and languages like scripts (e.g., PowerShell) and binary files (e.g., EXE).

We have two concrete implementations for AIDRA:
The first is Scripts LLM which is the pipeline for script analysis.
The second is Assembly LLM which is a pipeline for binary files.

<!-- Slide number: 6 -->
# Use Cases - AIDRA
Customer Sample Submission:
Customers can submit samples directly from the platform into the analysis environment for automated processing.

Security Analyst Workflow (IR/SOC):
A security analyst requiring immediate sample analysis can submit it independently through the platform, where it is prioritized via a dedicated queue for rapid response and assistance.
This enables fast, on-demand investigation workflows.

Security AI Mesh (SAM) Integration:
AI-driven security systems collaborate by sharing samples across tools.

### Notes:
[Aviad]
Here are several cases that comes from daily activity that shows the opportunity to use AIDRA to answer a need.
The solutions that we saw previously come to answer the following 3 use cases.
The first use-case isCustomer Sample Submission:
Think about a case that happens daily, in which a customers wants to investigate a suspicious file.
So, we propose AIDRA as an analysis sandbox for suspicious files.
The customer will be able to submit a file for analysis through the UI.
The seconds use-case isSecurity Analyst Workflow (IR/SOC):
Think of a scenario where a LevelBlue security analyst is in the middle of an investigation currently happening,and found a sample that can assist the investigation, he needs to analyse a file fast.
In this case, the security analyst gets priority while he submit the sample to AIDRA.
Security AI Mesh (SAM) Integration:
Collaboration of more solutions and AI frameworks to use and share information with AIDRA (kind of mcp, integration)

<!-- Slide number: 7 -->
# AI-DRA Architecture

![](GoogleShape2516g386cce6285d_0_616.jpg)

### Notes:
[Aviad]
A Multi-Agent Framework for Advanced Malware Analysis, leveraging Generative AI.
AIDRA works in 2 stages. Stage1: multi-agent analysisStage2: Risk Assessment & Security Report.
On stage 1:
AIDRA applies an Orchestrator agent, which manages a set of pre-selected agents.
Each agents has its own tools that it can apply to reach its goal.
In the Orchestrator’s brain lies an SLM (usually up to 8B parameters), which is fine-tuned for the specific purpose.
Stage 1 architecture is also extendable - it can be easily extended with new agents and tools to support more and new cases.
Stage 1 also can incorporate an AI classification model that produces benign/malicious classification for the given file (without explanation).
When an input file comes into the system, the Orchestrator analyses it and select the appropriate agents and their corresponding tools to use.
Each agent has a different role and has a different and distinct contribution to the analysis of the given file.
All the evidence produced by all agents are pooled to the Universal Evidence-based Analysis Framework (or in short UEBAF).
After all agents finished their analysis, all of their collected evidence / raw-findings are passed to the Stage 2, theRisk Assessment agent which combines all the data and produces a clear and trusted report.
The report is generated in both json and human readable PDF format.

<!-- Slide number: 8 -->
# Scripts LLM
Itamar Hershko

### Notes:

<!-- Slide number: 9 -->
# Architecture

![](GoogleShape2530g3be11a39e6d_5_131.jpg)

### Notes:
CodeAnalyst (Gemma-3-9B)
Analyzes code structure, functions, classes, and execution flow
Detects dangerous commands and suspicious system interactions
Identifies credential access and persistence mechanisms
ThreatClassifier (Mistral-7B)
Classifies malware type (RAT, Stealer, Ransomware, Dropper,etc’)
Maps attacks to MITRE ATT&CK framework
Identifies kill chain stage and threat sophistication
SecurityAnalyst (starcode2-7b)
Decodes obfuscation (Base64, XOR, encrypted payloads, etc’)
Extracts network indicators (URLs, IPs, domains, C2 servers)
Detects command-and-control communication patterns
RiskAssessor (Phi-4)
Aggregates findings from all other agents using consensus logic
Applies weighted scoring to determine overall threat severity
Evaluates business impact and data sensitivity (PII, credentials, financial)
Provides final verdict with response priority and recovery recommendations

<!-- Slide number: 10 -->

![](GoogleShape2537g3cc01bfd755_0_1874.jpg)
# Demo - Input
Sample sourced from Fa2y/Malicious-PowerShell-Dataset

PowerShell RAT
Disables Defender/AMSI
Steals browser creds
Exfiltrated data and Persistence

### Notes:
a public research repository containing real-world malicious PowerShell samples collected for security analysis and detection research

<!-- Slide number: 11 -->
# Demo - Terminal Output

![](GoogleShape2545g3cc01bfd755_0_1881.jpg)

### Notes:

<!-- Slide number: 12 -->

![](GoogleShape2556g3cc01bfd755_0_1890.jpg)
# Demo - Terminal Output

![](GoogleShape2555g3cc01bfd755_0_1890.jpg)

### Notes:

<!-- Slide number: 13 -->
# DEMO PDF

### Notes:

<!-- Slide number: 14 -->
# Fine Tune - Evaluation Results

![](GoogleShape2571g3be11a39e6d_5_113.jpg)

### Notes:
[Aviad]
Here you can see the evaluation results of the AI classification model on PowerShell scripts.
The test set for evaluation contains ~800 files.
In this slide you can see in general the:
Confusion matrix (top left),which basically shows metrics: TPR, TNR, FPR, FNR.
Probability Distribution of Benign vs Malicious Samples
ROC Curve
At the top right you can see the classification metrics on the optimal threshold of the classifier:
TNR = 98.9%TPR = 97.8%FPR = 1%

<!-- Slide number: 15 -->
# Pricing

### Notes:

<!-- Slide number: 16 -->
# AI-DRA
Open Source Models

### Notes:

<!-- Slide number: 17 -->
# Multiple Requests
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
[Aviad]

…

<!-- Slide number: 18 -->
# Training Hardware Costs
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
[Aviad]

…

<!-- Slide number: 19 -->
# Submission Cost
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
[Aviad]

…

<!-- Slide number: 20 -->
# Annual Total Cost
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
[Aviad]

…

<!-- Slide number: 21 -->
# Assembly LLM
Noa Perach Novogroder

### Notes:

<!-- Slide number: 22 -->
# Assembly LLM
Motivation

![](GoogleShape2693g3cc01bfd755_0_2514.jpg)

### Notes:
So far a PE file was a misterious object, as an endpoint product we had to follow the marks and hints he's leaving all over the system to uncover it's charactaristics and purpose (like registry keys, files it's changing etc)
there are many techniques that can be used to evade our "sight" and make it very complex to understand the flow like list of dropped files, code injection, algorithms running directly from blobs in the memory and so on.
for the first time, cybereason built an AI agent that can read a PE file as an open book
we trained an LLM model to understand assembly code and malwares behaviour as it's native language.
The agent starts by unwrapping the pe file assembly code, building basic blocks and then connecting them using CFG nucleus algorithms to functions and then to the entire flow.
After the breakdown process the translation process is starting
each basic block is a word
a function is a sentence
a pe file is a story
the analysis is bring enriched using ghidra open source framework to include api calls, strings, and rules.
functions similiarity, known malwares techniques, access to different resources and detection of malware families are all included in the agent to enhance the security capabilities of our product.
Let's move forward to a new era in cyber security

<!-- Slide number: 23 -->
# Architecture

![](GoogleShape2700g3c3265d9eb7_1_9.jpg)

### Notes:
Here you can see the AIDRA architecture and how Assembly LLM will be integrate within it.
You can see here the same AIDRA architecture, while we grayed the un

<!-- Slide number: 24 -->
# Assembly LLM
Flow

![](GoogleShape2708g3cc01bfd755_0_2521.jpg)

### Notes:
So far a PE file was a misterious object, as an endpoint product we had to follow the marks and hints he's leaving all over the system to uncover it's charactaristics and purpose (like registry keys, files it's changing etc)
there are many techniques that can be used to evade our "sight" and make it very complex to understand the flow like list of dropped files, code injection, algorithms running directly from blobs in the memory and so on.
for the first time, cybereason built an AI agent that can read a PE file as an open book
we trained an LLM model to understand assembly code and malwares behaviour as it's native language.
The agent starts by unwrapping the pe file assembly code, building basic blocks and then connecting them using CFG nucleus algorithms to functions and then to the entire flow.
After the breakdown process the translation process is starting
each basic block is a word
a function is a sentence
a pe file is a story
the analysis is bring enriched using ghidra open source framework to include api calls, strings, and rules.
functions similiarity, known malwares techniques, access to different resources and detection of malware families are all included in the agent to enhance the security capabilities of our product.
Let's move forward to a new era in cyber security

<!-- Slide number: 25 -->
# Assembly LLM Demo

### Notes:

<!-- Slide number: 26 -->

![](GoogleShape2720g3cc01bfd755_0_2534.jpg)

![](GoogleShape2721g3cc01bfd755_0_2534.jpg)

### Notes:

<!-- Slide number: 27 -->

![](GoogleShape2729g3cc01bfd755_0_2542.jpg)
#

### Notes:

<!-- Slide number: 28 -->
# AI-DRA Next Steps
Hen Ashkenazi

### Notes:

<!-- Slide number: 29 -->
# Next Steps - Current Status
Current status of AIDRA (we need to fill the actual status here, what works and what’s missing).
Take AI-DRA to production – engineering capabilities. (steps we do for production, create webpage, service,etc)
Optional integrations for AI-DRA:
IRCA - Automatic IR report generation using GenAI.
AI Assistant - Submit script samples.
Tipper - (owlints collaboration and how we can advance in that area)

### Notes:
[Hen]

IRCA – automatic generation of IR report using GenAI.

<!-- Slide number: 30 -->
# Next Steps - Future Steps
Current status of AIDRA (here we mention how we can advance in the future)
Take AI-DRA to production – engineering capabilities. (steps we do for production, create webpage, service,etc)
Optional integrations for AI-DRA:
IRCA - Automatic IR report generation using GenAI.
AI Assistant - Submit script samples.
Tipper - (owlints collaboration and how we can advance in that area)

### Notes:
[Hen]

IRCA – automatic generation of IR report using GenAI.

<!-- Slide number: 31 -->
# Q&A

### Notes:

<!-- Slide number: 32 -->

### Notes:

<!-- Slide number: 33 -->
# Problem / Motivation
Analysts juggle hundreds of files, scripts, and memory alerts each day,
making consistent high-quality triage a challenge.
Alert Overload:High volume makes it hard to spot truly critical threats.
Tool Hopping:Jumping between consoles to gather context wastes minutes per alert.
Incomplete Context:Raw alerts lack enrichment, forcing analysts to guess intent.
Manual Correlation:Stitching file, script, and memory evidence together is slow.
Triage Fatigue:Repetitive low-value alerts drain focus and cause mistakes.
Knowledge Gaps:Insights stay in individual heads, so handoffs lose vital detail.

### Notes:
[Itamar]

All bullets are bucause human in the loop, not automated.

<!-- Slide number: 34 -->
# What is AI-DRA?
A Multi-Agent Framework for Advanced Malware Analysis (scripts/binary)
AIDRA replaces one-size-fits-all models with a team of specialized SLM agents managed by an Orchestrator.
Each agent in our system acts as a specialist, analyzing a distinct aspect of the script parsed into separate inputs, offering a unique perspective on the same malware (binary, behavior, threat-intel, network, etc.).
Agents’ findings then passes to a Consensus Engine that produces a clear, trusted report, enriched by local analysis tools. (e.g., IOC extraction, MITRE mapping).

### Notes:
[Aviad]

…

<!-- Slide number: 35 -->
# AI-DRA Architecture

![](GoogleShape2783g3c3265d9eb7_1_1.jpg)

### Notes:
A Multi-Agent Framework for Advanced Malware Analysis using Generative AI.
AIDRA works in 2 stages. Stage1: multi-agent analysis | Stage2: Risk Assessment & Security Report
On stage 1: AIDRA applies Orchestrator agent, which manages a set of pre-selected agents.
Stage 1 architecture is also extendable - it can be easily extended with new agents and tools to support more and new cases.
In the Orchestrator’s brain lies an SLM (usually up to 8B parameters), which is fine-tuned for the specific purpose.
Stage 1 also can incorporate an AI classification model that produces benign/malicious classification for the given file (without explanation).
When an input file comes into the system, the Orchestrator analyses it and select the appropriate agents and their corresponding tools to use. Each agent has a different role and has a different and distinct contribution to the analysis.
All the evidence produced by the agents are pooled to a bucket (we call it Universal Evidence-based Analysis Framework).
After all agents finished their analysis, all of their collected evidence / raw-findings are passed to the Risk Assessment agent which combines all the data and produces a clear and trusted report.
The report is generated in both json and PDF format.
Next, Itamar will elaborate deeply on all the components I mentioned.
