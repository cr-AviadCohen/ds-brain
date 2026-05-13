# AI Assistant - LevelBlue.pptx

<!-- Slide number: 1 -->

![](GoogleShape633p2.jpg)
# AI Assistant
Security AI Agent for the EDR platform

### Notes:
Hi everyone!My name is Aviad Cohen, I’m a Tech Lead at the Data Science team, and will deliver this presentation.

Guy Kassorla and I have been working on this project for the last 8 months,and we are very proud of it, and excited to present it to you.

<!-- Slide number: 2 -->
Project Goal
AI Assistant
Live Demo
Next Steps
Q&A

### Notes:
[Aviad]Here is the agenda of this presentation.
I will start with Project Goal.
Than I’ll elaborate on the AI Assistant we developed and its different components.
We will then move to a LIVE DEMO of the assistant.
Than, finally, talk about next steps.

<!-- Slide number: 3 -->
# Project Goal
Develop an AI Assistant that can assist the user, within the UI.

![](GoogleShape649g3bfc492ba8d_0_57.jpg)

AI Assistant

### Notes:
Before I’ll dive into project’s goal, I would like to say few words on Cybereason product.
Cybereason is an EDR solution that protects endpoint machines from harmful files and malicious activities.
Cybereason has a web-based UI platform, that can control and manage the EDRs, connected to a specific environment.
On the right side of the platform, you can see an illustration of the AI Assistant, which is an AI chatbot, that can answer questions based on data from the environment.
—
So, The goal of this project is to develop the AI Assistant that can help ther user within the CR Platform.
By chatting with the AI Assistant, users doesn’t need to be familiar deeply with the system to do things.It is another convenient way of working with the system, similar to what you already doing with ChatGPT and more..
—------
I would like two define at least two personas that can utilize this AI Assistant:
Admins: manage users and permissions.
SOC Analyst: Investigation of malops and activities.

FIGMA

<!-- Slide number: 4 -->
# AI Assistant Requirements
Communicates & understands natural language
Utilizes Cybereason Functionality within the platform
Navigates within the Cybereason UI
Utilizes 3rd party security APIs

** Cybereason Core API >>  Cybereason Phoenix API
LevelBlue API

### Notes:
So, What are the required capabilities of the AI Assistant:
The First and obvious is to communicate and understand natural language.
Second,The AI assistant should utilize the Cybereason functionality within the platform:
Investigate.
Get data
Perform actions (e.g., Create new detection rules)
Third,We would like the Assistant to know the Cybereason UI, and help the user to navigate it.For example, in case the user is not fully familiar with the UI, he can ask the assistant to take him to a specific page, or to do some actions for him.
And Last,We would like to utilize 3rd party security APIs, like threat intel.
Note that everything presented today about the AI Assistant and the Cybereason Core API
can also be applied to any other API, such as the Cybereason Phoenix APIs or LevelBlue APIs.

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
Definition: “An AI Agent is an autonomous or semi-autonomous system, that uses artificial intelligence to perceive its environment, reason about what it observes, and take actions, either physical or digital, to achieve specific goals”.
An AI Agent:
Has System Prompt that defines it role/character, guidelines, limitations, expected output.
Utilizes a Language Model, to reason and to choose actions.
Usually has a set of Tools that it can utilize.A tool for example can:
Do some calculations
Pull data from an information source (locally or remotely)
Interact with other systems
more…
An AI Agent can have more advanced capabilities which are optional.For example:
Planning – Ability to make a plan of how to solve the user request (hierarchical, or multi-step approach)
Memory – short-term /  long-term
Learning & Adaptation – Feedback loop, etc.
RAG
… more …
There are several approaches to implement an AI Agent, and agentic systems.We chose to build our AI Assistant as a Multi-Agent System,Were each agent in the system uses the ReAct approach (Reason >> Act)
ReAct agent: The agent alternates between reasoning (think “what to do next”) and acting (calling a tool), until it can produce a final answer.
In one word, we are developing “Harness”.

<!-- Slide number: 6 -->
# AI Assistant Architecture

![](GoogleShape676g3c839ae09bc_0_30.jpg)

### Notes:
In this slide you can see a high-level architecture of the AI assistant we developed.

The AI Assistant is a Centralized & Hierarchical Mediated Multi-Agent Aystem, containing an Orchestrator agent (management) and a set of Independent agents.
The architecture allows to easily add more and more agents if needed.

The Flow:
When the user sends an input query to the AI Assistant, it is first passed through a Guardrails mechanism that is aimed to block unwanted question (OOC).
The decision of the guardrails (allow/block) is passed to the Orchestrator.
If the Guardrails decision is to Block the request, then the Orchestrator will response with "I can’t assist with that request. You may rephrase or ask something else."
If the Guardrails decision to Allow the request, the Orchestrator will then choose which agent(s) to call, in order to answer the users request.
The process of choosing the right agent for the user’s query is called Routing.
Once an agent/agents return their response, the orchestrator organizes the answer and sends a response to the User.
The Orchestrator also send data to a tracing system so all the data is saved for monitoring/benchmarking/testing.
Now let's talk about the Agents:
Each agent in our system:
Is independent – we can run OR test it separately.
Is autonomous – it will aim to achieve its goal, by trying different ways, and call different tools.
Has it’s own Language Model to reason and call tools.We can define a different model for a different agent.For example, use GPT-5-Nano for one simple agent, and the GPT-5.2 to a more complicated agent.
Each agent has its own unique System Prompt which configure its role.
has its own dedicated Tools that are relevant to its purpose.
Agents do not “talk” to each other, only the orchestrator call them.

In our system, tools mostly call some API, to retrieve data or do actions, but it it not mandatory, tools can also use data stored locally.
At the right side you can see examples of known APIs that we use.
Memory:
Both the Orchestrator and Agents has short-term memory ability. They remember the last several messages within the current session.Short-term memory is important for natural conversation, without the need to say things explicitly (I will demonstrate it on Demo)This memory ability is configurable per agent.
Configuration file:
Guardrails configuration
Tracing configuration
Which agents to load?
What LLM to use for the Orchestrator and for each agent
and more..

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
We developed the AI Assistant in Python using the well known Langchain and Langgraph Libraries.
The AI Assistant can work locally on a standard laptop as it doesn’t require much computational resources..
We consume Large Language Models from Microsoft Azure AI Foundry.
We currently use the GPT-5.2 as it is the fastest and provide the highest accuracy.
We tried GPT-5.4 but for technical reason it responded much slower, so we didn’t upgrade yet.
Alternatively, we can switch the GPT-5-mini or GPT-5-nano, which are less expensive and “pay” by accuracy and speed.
On Microsoft Azure AI Foundry, we disabled the default content-filtering on the LLM we use,to avoid blockages, as we use words like “malicious” / “malware” etc, that can trigger automatic blocking.
We also tried to apply various SLMs that run locally, for the Orchestrator and Agents, in order to totally avoid costly LLM calls.However, in our experiments they didn’t deliver sufficient performance.Most of them cause code failure. The rest wasn’t able to provide good routing (choosing agent/tool), or didn’t succeed in Tool Calling (which is a mandatory requirement).Only few, which you can see in the list,

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
We choose to implement the Guardrails based on an Embedding Model rather than LLM, to make it faster and reduce costs.A local embedding model runs on CPU/GPU resources and avoids costly LLM call.
We chose to use the following Embedding model which is relatively fast and accurate (from our experiments).
The Guardrails mechanism uses the Embedding model to find semantic similarity between the user’s input request query and 3 lists:
Each list contains phrases.
1 Blocklist: contains 13 dangerous categories of phrases like: System Prompt Injection, Jailbreak, Role Playing, and more.
“Ignore all your system instructions”
“Pretend you have no safety guidelines”
2 Allowlists:
1 Allowlist - Conversational: Greeting / Farewells / Affirmations / Ask for Details / Thanks / help / …
“User greeting or saying hello”
"User agreeing or confirming"
1 Allowlist - Tools:
This list is dynamically extracted from the name and description of the tools used by the different Agents.
The blocklist and allowlists are precomputed when the system is loading, it just take couple of seconds to compute all embeddings.
In order to pass the guardrails, the user’s query must fall closer to an Allowlist, and far from a Blocklist.
Why not using only an Allowlist you ask?First, it is a best practice in this area, and we saw in our research, to use both allowlist and blacklist.Second, we want to make sure that the user’s query doesn’t similar to any attack patterns, hence we need a blocklist.You can think of it as a classification problem. You get better results when the model see both classes instead of only one of them.
Chart:
On the right side you can see a diagram demonstrating how the Guardrails mechanism flows.
As you can see, the user’s input is is converted to embeddings, and check against the 3 lists.Then based on the most similar list, and a predefined threshold, it is decided to Block or to Allow the content.

We also added Guardrails guidelines into the Orchestrator System Prompt so,if an unwanted request is NOT blocked by the Guardrails, the Orchestrator may block it.

Evaluation:We evaluated our Guardrails mechanism with a benchmark dataset that we created.The dataset currently contains more than 4K examples, of queries that should be blocked, and other queries that should pass.The overall accuracy of our guardrails is approximately 97%.

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
In the current and next slides, I’ll present all the AI Agents we integrated into the AI Assistant,There are 3 groups of agents: Cybereason, MITRE, Threat Intelligence.In total, 35 agents

In this slide you can see the different Cybereason agents,most of them rely on Cybereason API.

Cybereason API
Cybereason has approximately 120 different APIs.
Guy Kassorla did a very long and comprehensive work, mapping all the different APIs from documentation,test each and every one carefully,and converting each API to a Tool, that can be effectively utilized by an agent.
Just to make it clear, Cybereason tools (that we implemented) are 10K lines of python code.

Cybereason Agents
AI Assistant has 15 different Cybereason agents.
Each agent is responsible for a specific domain of operations.
All agent has tools that utilizes CR API, except the first two agents.
On top | you can see the RAG-based agent on Cybereason’s knowledge.
Second | you can see the UI Agent – which helps the user navigate the Cybereason UI. this agent has 26 tools, but non-of them connect an API.These tools uses internal knowledge of how the UI is constructed.
The rest 13 agents, uses cybereason API.Each agent is responsible for a separated category of APIs.

Moreover regarding CR API:
When the CR agents are loaded, the system filters only the relevant tools (out of all tools), according to user permissions and environment.
Single CR Agent vs Separated CR Agents (detailed)
At the beginning we created one single agent which contained all Cybereason tools (~120).
The agent worked pretty well when we did simple testing.However, this approach is problematic for couple of reasons:
It makes the tool selection more complicated.
Agent’s System Prompt gets very long as it contains info of all 120 tools.
While some CR APIs are very simple and works great, there are other APIs which are much more complicated (like the investigation API).Complicated APIs gets many different parameters and options, and the general CR agent is struggling with them and cannot apply them well.
We decided to split the single agent into 13 separated agents, by category.So each agent was responsible on a bunch of tools related to the same topic.Specific complicated APIs got also separated agents with additional tools that assist the agent using the complicated tool.In our evaluation we, proved that this approach provides better accuracy.

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
On the left side you can see the 17 Threat Intelligence agents:
On top I put the OTX AlienVault, VirusTotal, CVE, and other famous threat intelligence platforms.
On the right side you can see the 4 MITRE framework agents:
MITRE ATT&CK – Adversary Tactics and Techniques based on real-world observations.
MITRE D3FEND – A knowledge graph of Cybersecurity countermeasures
MITRE CWE – Common Weakness Enumeration
MITRE CAPEC – Common Attack Pattern Enumerations and Classifications

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
Now that we have covered the full scope of the 35 agents and their dedicated toolsets, let's look at how we easily converted the underlying Cybereason tool code into the Model-Context-Protocol (MCP).

MCP (Model-Context-Protocol), is an open standard of enabling language models access external sources such as APIs, in natural language.
Based on our tool architecture in AI Assistant, we converted, very easily, all the Cybereason tools we developed (10K lines of code) to MCP format with FastMCP python library.
On the right side you can see an example of how we loaded our CR MCP to Claude Desktop:
You can see that I asked how many malops (malicious operations) in the last 6 month,and Claude is able to answer based on CR API via MCP.
Cybereason MCP tools can be consumed also by any other supporting platforms:
Cursor
LM-Studio
.. more ..
Note that that AI assistant project uses its own tool architecture and not the MCP.That provides us better control of the tools and ability to leverage them with different types of agents from different platforms.

<!-- Slide number: 12 -->
# Traceability & Observability
Traceability: Capture every LLM call, agent step, tool call, prompt, response, and metadata into a trace store
Observability: Continuously monitor agent + tool performance in production
⇒ Cost monitoring & FinOps management

![](GoogleShape725g3c839ae09bc_0_1532.jpg)

### Notes:
Before jumping to the live demo I want to talk about Traceability and Observability.
Traceability
Traceability capture every LLM call, agent step, tool call, prompts, responses and metadata into a trace store.
Traceability is important for us as researchers and developers to be able to trace what happened in the system,So we can:
Locate problems, errors and bugs
Collect and store user feedback.
Monitor costs.
Improve the Assistant accordingly
We explored several tracing systems:
We chose to use LangFuse (acquired by ClickHouse) – presented by Itamar previously.
LangFuse LangSmith (Langchain)
Azure AI Foundry (preview)
Observability:
Observability goes beyond logging, It’s continuous monitoring of quality and performance: Agent and Tool performance in production.
success rate, error rate, latency, and cost, broken down per agent and per tool.
We didn’t incorporate observability capabilities yet as we are in POC,but it is a must for production.

<!-- Slide number: 13 -->

![](GoogleShape732g3cb54e64023_0_25.jpg)

### Notes:
Here you can see an example of LangFuse tracing environment. We use it for free with some limitations.
It stores each and every call to LLM, and allows us to see what data sent to LLM, and what was received.
We added tags to the data we send, so we can easily filter call by specific user, session, agent, etc.

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
[Aviad]
CISO Collaboration:
We worked with the CISO team to review the project code and its current implementation.
An official CISO requirements document (24 pages) was produced – we currently reviewing it.
These requirements applies to production environments, not to the POC.However, we have already started integrating suggested security measures.

We divided the security measures to:
Security Measures in Place – that we already implemented.
Security Measures for Production

—----—----—----—----—----—----—----—----—----—----—----—----—----—----—----—----—----—----—----—----—----—----—----
Security Measures in Place
Guardrails based on both:
System Prompt
Semantic Blocklist+whitelist.
Permission-based tool filtering (also explained before)
Tool call limitour agents has built-in safety mechanism to limit both agent and tool calls, so infinite loop cannot take place.
Context trimming to avoid context flooding.- Built-in trimming of retrieved Tool data from context (can be very long).- For short-term memory – we keep in context only the last X previous messages.
Traceability with Langfuse (already explained)

Security Measures for Production
Dedicated ML-based injection detection classifier
Indirect injection sanitizationCurrently, EDR data and threat intel API responses flow unsanitized into LLM context
Human confirmation gateDESTRUCTIVE actions (isolation, remediation) should require user approval
Tamper-evident audit loggingTamper-evident audit logging, is a security control that ensures every action taken by the AI system is recorded in a way that cannot be secretly modified or deleted after the fact. If anyone tries to alter the logs, the tampering will be immediately detectable.
Dedicated AI audit log storeIs a separate, purpose-built sink, used only for security-relevant AI events.
Data anonymization proxyCustomer data (IPs, hostnames, Mac addresses, etc.) should be tokenized before send to LLM on cloud.(sometimes you have to send)

<!-- Slide number: 15 -->
# Cost Evaluation
Cost distribution based on AI Assistant benchmark with 400 questions,covering all agents & tools (CR, MITRE, TI).
Model: GPT-5.2
Average cost single query: $0.0525 (median = $0.0392)

![](GoogleShape749g3cdf595eae6_0_6.jpg)

### Notes:
[Aviad]

In this slide you can see the cost evaluation for a single request to AI Assistant.
We used the GPT-5.2 LLM.
The average cost for a single user query is 0.0525$
This cost is based on our evaluation with a benchmark dataset which has 400 questions, covering all agents and tools.
At the bottom you can see the distribution of the cost.
To reduce AI Assistant costs we can switch to GPT-5-nano which costs approximately 4% of GPT-5.2and can be used for the AI Assistant, with some trade-off in accuracy.

<!-- Slide number: 16 -->
# POC Summary
✅  Communicates & understands natural language
✅  Navigates within the Cybereason UI
✅  Utilizes Cybereason Functionality within the platform
✅  Utilizes 3rd party security APIs

### Notes:
Here is a summary of our POC:All the requirements from the AI Assistant for the POC are accomplished.The AI Assistant:
Communicate in natural language.
Allows the user to navigate within the Cybereason UI.
Utilizes Cybereason Functionality within the platform
Utilizes 3rd party security APIs.

<!-- Slide number: 17 -->
# LIVE Demo

### Notes:
Live demo questions:
…

<!-- Slide number: 18 -->
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
We will demonstrate the AI Assistant using a website we built for testing and hackathon.
We raised the AI Assistant on an OCI server.
The AI Assistant is connected to a security research dedicated cybereason environment.

Live Demo:
Questions

<!-- Slide number: 19 -->
# Next Steps

### Notes:
Live demo questions:
…

<!-- Slide number: 20 -->
# Next Steps
Enhancements:
Feature Parity with Hunter
Security (In Progress)
Production ready

### Notes:
In this slide I’ll talk about the next steps in AI Assistant development.
Feature parity with Hunter:
We would like to integrate Hunter capabilities into AI Assistant.Hunter(OpenWebUI + MCPs)
Fusion
Community Threat Intilligence
and more..
Security
I talked about security previously regarding CISO, we continue that work.
Explore how to make our agent more secure:Search for our code vulnerabilities, and more.
Production ready
Although AI Assistant is currently a POC, we would like to prepare it to be production-ready.
Saving Costs:
We can reduce costs in several ways:
Reduce the number of API calls to LLM.Currently, for each use query, we do 2N+1 LLM calls,when N is the number of tools the agent selected to apply.We have an idea to reduce the number of API calls: by doing the routing within the orchestrator using embedding instead of LLM call.
Reduce the size of queries we send to LLM – for example by simple condensing the long system prompt.
We can also save costs by improving accuracy.A more accurate agent, requires less attempts/retries to provide the right answer - it saves costs.

<!-- Slide number: 21 -->
# Q&A

### Notes:

<!-- Slide number: 22 -->

### Notes:

<!-- Slide number: 23 -->
# END

### Notes:
Live demo questions:
…

<!-- Slide number: 24 -->
# Points for Presentation
Limitations: (long-conversations increase context, long tool response.
Challenges: Agent selection, tool selection.
Orchestrator Langraph Workflow Logic
Review Pavel presentation to take ideas for presentation.
AI Assistant architecture is Generic and can work with other platforms using API. We just need to develop the proper tools.
Next steps: production requirements, security privacy, data leakage.
Industry statistics show that most AI Agents do not make it to production:
Security & Safety.
Production requirements:
Traceability & Monitoring.
Local SLMs with Assistant

### Notes:

<!-- Slide number: 25 -->
# AI Assistant >> Production
Security & Safety
Traceability
Observability

### Notes:
Industry statistics show that most AI Agents do not make it to production, for many reasons.
Security & Safety:
After an Assistant reached production, it is important to have the following capabilities:
Traceability:
It is very important to have all data logged into a system (e.g., LangFuse/Langsmith/AzureAI) so the
User feedback.
Observability:
It is very important to have observability (continuous monitoring) over the performance of:
Agents & Tools.
Tracing Errors.
Monitor Costs.
Also when we decide to move to a new model, or “improve” prompts, we would like to know that performance remain.

<!-- Slide number: 26 -->
# Hackathon
Time: one single day: <date>
Start at: 10:00
Finish at: 17:00
Your Hackathon task:
Find out how the Assistant can help you with your tasks.
Use the AI Assistant to investigate the environment.
Find bugs and send your feedback.

### Notes:

<!-- Slide number: 27 -->
# ARCHIVE

### Notes:

<!-- Slide number: 28 -->
# AI Assistant Architecture

![](GoogleShape837g3c839ae09bc_0_6.jpg)

### Notes:
On the Guardrails mechanism and how it is built and work I’ll elaborate later in a different slide.
Agents (35):
Cybereason = 14
MITRE = 4
Threat Intelligence = 17

<!-- Slide number: 29 -->
# AI Assistant Costs
…

### Notes:
…

<!-- Slide number: 30 -->
# Security
Cylestio for AI Agent(s) security.
Take info from Shani

### Notes:
Address Cybereason API user permissions
Cylestio for AI agent security

<!-- Slide number: 31 -->
# Evaluation

### Notes:

<!-- Slide number: 32 -->
# Evaluation

![](GoogleShape866g3c839ae09bc_0_1553.jpg)

### Notes:
For evaluation we created a benchmark dataset which contains X questions. For each question we defined the correct expected agent and tool to be chosen.
Our first experiment come to answer the research question: what is better, one single CR agent with all the tools OR dividing the tools to categories, and set a separated agent for each category.

<!-- Slide number: 33 -->
# Evaluation

![](GoogleShape873g3c839ae09bc_0_1563.jpg)

### Notes:
Our second experiment come to compare the following Language models: GPT-5.2 | GPT-5-mini | GPT-5-nano
Left Chart:
…
Right Chart:
…

<!-- Slide number: 34 -->
# Evaluation

![](GoogleShape882g3c8f2ef7f31_0_0.jpg)

![](GoogleShape880g3c8f2ef7f31_0_0.jpg)

![](GoogleShape881g3c8f2ef7f31_0_0.jpg)

### Notes:
Left Chart:
…
Right Chart:
…

<!-- Slide number: 35 -->
# AI Assistant Architecture

![](GoogleShape889g3c8f2ef7f31_1_0.jpg)

### Notes:
In this slide I will go over the full pipeline, starting from the point a user sends a query to the AI Assistant, until he gets back an answer.
When the Orchestrator gets an input query from the user

<!-- Slide number: 36 -->
# Requirements
Cybereason environment (requires VPN)
Credentials to Cybereason environment.
.env:
API Keys to various services:

### Notes:
…

<!-- Slide number: 37 -->
# Code Architecture
Abstract Agent
React Agent
Concrete agents
Abstract Tool
Abstract Tool Category
Concrete tools implementation
AI Assistant Class Diagram

![](GoogleShape904g3c8f2ef7f31_1_9.jpg)

### Notes:
We chose to create our own abstract classes for Agent and Tool.
This approach allows us to:
Extend those classes easily to future unpredictable use-cases.
Also convert classes when needed to other formats. For example, we easily converted our tools to one format required by Langchain React Agent, Or to another format required by Agno (another python package for agents)
At the bottom you can see the big class diagram of the AI Assistant. The purpose is to show you how big it is, and not the specific details.
After we implemented all Cybereason Tools …..

<!-- Slide number: 38 -->
# AI Assistant Integrated Agents
Cybereason 120 API and UI navigation with 14 AI Agents
MITRE … 4 AI Agents
Threat Intelligence (OTX, OCTI, etc.) with 17 AI Agents

![](GoogleShape913g3c839ae09bc_0_1540.jpg)

### Notes:
In this slide you can see 3 groups of agents we integrated into the AI Assistant,in total 34 agents from 3 categories:
Cybereason Contains 14 agents.
4 Agents for which utilizes the knowledge of MITRE Framework
and 17 additional agents related to threat intelligence.
Now we will dive into each category in more details.

<!-- Slide number: 39 -->
# Cybereason API
Categories
Hunt and Investigate
Respond to Malops
Respond to Malware
Remediate Items
Manage Reputations
Get Threat Intelligence

Manage Users
Manage Sensors
Manage Incident Response & Forensic Data Ingestion Tools
Set Machine Isolation Rules
Vulnerability Management

### Notes:
Before I talk about Cybereason agents, I’ll provide a short background on the Cybereason API.
Cybereason API contains approximately 120 different APIs.
Guy Kassorla did a very long comprehensive work, mapping all the different Cybereason APIs from documentation,test each and every one carefully,and converting each API to a tool that can be effectively utilized by the agent.Cybereason tools are 10K lines of python code.
In this slide you can see the different categories of Cybereason API:
Manage Users:
List Users | Create User | Update User
Hunt and Investigate:
File Search | Get File Search Requests, | Download Batch File
Respond to Malops:
Query Malops | Get Malop Details | Isolate Malop Machine
Respond to Malware:
Query Malware Counts | Query Malware Types | Get File Reputation
Remediate Items:
Remediate Items | Check Remediation Progress | Abort Malop Remediation
Manage Reputations:
Get Classification For Item | Update Classification Reputation
Get Threat Intelligence:
Get File Reputation | Get Domain Reputation | Get Ip Reputation
Manage Sensors:
Query Sensors | Upgrade Sensor | Retrieve Sensor Logs
Manage Incident Response & Forensic Data Ingestion Tools:
Run Incident Response Tool | Monitor Incident Response Tool | Delete Tool Package
Set Machine Isolation Rules:
Get Isolation Rule | Create Isolation Rule
Vulnerability Management:
Retrieve Vulnerabilities List | Retrieve Details Vulnerable Machine
