# AI Assistant - LevelBlue - Export.pptx

<!-- Slide number: 1 -->

![](GoogleShape633p2.jpg)
# AI Assistant
Security AI Agent for the EDR platform

### Notes:

<!-- Slide number: 2 -->
Project Goal
AI Assistant
Live Demo
Next Steps
Q&A

### Notes:

<!-- Slide number: 3 -->
# Project Goal
Develop an AI Assistant that can assist the user, within the UI.

![](GoogleShape649g3bfc492ba8d_0_57.jpg)

AI Assistant

### Notes:

<!-- Slide number: 4 -->
# AI Assistant Requirements
Communicates & understands natural language
Utilizes Cybereason Functionality within the platform
Navigates within the Cybereason UI
Utilizes 3rd party security APIs

** Cybereason Core API >>  Cybereason Phoenix API
LevelBlue API

### Notes:

<!-- Slide number: 5 -->

![](GoogleShape668g3c6a89c8cc6_0_37.jpg)
# AI Assistant Main Properties
An AI Agent:
Has a System Prompt
Utilizes a Language Model to reason and to choose actions
Usually has a set of “Tools” that it can utilize
Advanced capabilities [optional]
AI Assistant:
Multi-Agent System (MAS)
Agents: ReAct (Reasoning + Acting)

ReAct Agent

![](GoogleShape667g3c6a89c8cc6_0_37.jpg)

### Notes:

<!-- Slide number: 6 -->
# AI Assistant Architecture

![](GoogleShape676g3c839ae09bc_0_30.jpg)

### Notes:

<!-- Slide number: 7 -->
# Implementation
Frameworks:
Python
LangChain (LM)
Langgraph (Orchestrator / Agents)
Language Models:
Microsoft Azure AI Foundry:
GPT-5.2 / GPT-5.4
GPT-5-mini
GPT-5-nano

Local SLMs (insufficient):
mistralai/mistral-3-3b
openai/gpt-oss-20b
mlx-community/Meta-Llama-3.1-8B-Instruct-4bit

### Notes:

<!-- Slide number: 8 -->

![](GoogleShape691g3c839ae09bc_0_16.jpg)
# Guardrails
Embedding Model:
BAAI/bge-small-en-v1.5 (384 dimensions)
Guardrails
Blocklist (configurable)
Allowlists:
Conversational phrases (configurable)
Allowlist Tools (dynamic loading)

### Notes:

<!-- Slide number: 9 -->
# AI Assistant Agents
Cybereason
📚  Knowledge Base RAG				0 tools
🌐  UI Navigation                                    	26 tools
🕵️  Investigation Query Builder         		2 tools
🔍  Custom Detection Rule Builder  		9 tools
🔍  Hunt & Investigate 				9 tools
🚨  Respond to Malops 				19 tools
🛠️  Remediate Items 					4 tools
🦠  Respond to Malware 				2 tools
⭐  Manage Reputations 				4 tools
🎯  Threat Intelligence 				12 tools
📡  Manage Sensors 					32 tools
🔒  Isolation Rules 					4 tools
🔬  IR & Forensics 						9 tools
👥  Manage Users 					5 tools
🛡️  Vulnerability Management 			5 tools

![](GoogleShape700g3c839ae09bc_0_265.jpg)

### Notes:

<!-- Slide number: 10 -->
# AI Assistant Agents
Threat Intelligence
👽  OTX AlienVault Threat Intelligence 		12 tools
🦠  VirusTotal Threat Intelligence 			7 tools
🚨  CVE Vulnerability Intelligence 			5 tools
📄  GitHub Security Advisory 				4 tools
🛰️  EPSS Threat Intelligence 				3 tools
🧨  Abuse.ch Malware Intelligence 			17 tools
🔐  Certificate Transparency 				3 tools
🌫️  GreyNoise IP Intelligence 				6 tools
⚠️  AbuseIPDB IP Reputation 				7 tools
🔗  URLScan Phishing & Malware Detection 	6 tools
🥋  Shodan Internet Discovery 				6 tools
🛰️  Censys Asset Discovery 				16 tools
🗺️  SecurityTrails DNS Intelligence 			17 tools
🌊  Pulsedive OSINT Intelligence 			11 tools
🎣  OpenPhish Phishing Detection 			5 tools
🚫  Spamhaus Reputation 					8 tools
🛰️  OpenCTI 								35 tools

MITRE Knowledge base
🎯  ATT&CK Intelligence 		25 tools
🛡️  D3FEND Intelligence 		15 tools
🕳️  CWE Weakness Analysis 	25 tools
🧨  MITRE CAPEC Intelligence 	27 tools

### Notes:

<!-- Slide number: 11 -->

![](GoogleShape717g39540d46af3_0_14.jpg)

![](GoogleShape715g39540d46af3_0_14.jpg)
# Cybereason MCP
Cybereason Tools >> MCP (FastMCP).
Can be consumed by:
Claude Desktop
Cursor
LM-Studio
… more …

### Notes:

<!-- Slide number: 12 -->
# Traceability & Observability
Traceability: Capture every LLM call, agent step, tool call, prompt, response, and metadata into a trace store
Observability: Continuously monitor agent + tool performance in production
⇒ Cost monitoring & FinOps management

![](GoogleShape725g3c839ae09bc_0_1532.jpg)

### Notes:

<!-- Slide number: 13 -->

![](GoogleShape732g3cb54e64023_0_25.jpg)

### Notes:

<!-- Slide number: 14 -->
# Security
Security Measures in Place:
Guardrails
Prompt injection defense (partial)
Permission-based tool filtering
Agent & Tool call limits
Context trimming
Traceability (Langfuse)

Security Measures for Production:
Dedicated ML-based injection detection classifier (e.g., Rebuff / LakeraGuard | MS Prompt Shield)
Indirect injection sanitization for EDR and external API data
Human confirmation gate
Tamper-evident audit logging
Dedicated AI audit log store.
Data anonymization proxy

### Notes:

<!-- Slide number: 15 -->
# Cost Evaluation
Cost distribution based on AI Assistant benchmark with 400 questions,covering all agents & tools (CR, MITRE, TI).
Model: GPT-5.2
Average cost single query: $0.0525 (median = $0.0392)

![](GoogleShape749g3cdf595eae6_0_6.jpg)

### Notes:

<!-- Slide number: 16 -->
# POC Summary
✅  Communicates & understands natural language
✅  Navigates within the Cybereason UI
✅  Utilizes Cybereason Functionality within the platform
✅  Utilizes 3rd party security APIs

### Notes:

<!-- Slide number: 17 -->
# LIVE DEMO
Demo:
http://150.136.124.181:8501/
Server:
150.136.124.181 (OCI)
Docker 1: AI Assistant – Web Server UI (port 8501)
Docker 2: LangFuse – Web Server UI (port 3000)
Cybereason Environment:
https://secresearch-231.cybereason.net:443** Some malware were already executed within

### Notes:

<!-- Slide number: 18 -->
# Next Steps

### Notes:

<!-- Slide number: 19 -->
# Next Steps
Enhancements:
Feature Parity with Hunter
Security (In Progress)
Production ready

### Notes:

<!-- Slide number: 20 -->
# Q&A

### Notes:

<!-- Slide number: 21 -->

### Notes:
