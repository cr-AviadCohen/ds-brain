# AI Assistant Demo.pptx

<!-- Slide number: 1 -->
Moved to LevelBlue presentation template
# AI Assistant

Data Science Team

### Notes:

<!-- Slide number: 2 -->

![](GoogleShape339p58.jpg)
# Project Goal
Develop an AI Assistant that can help the user via the UI,in natural language.
Assistant capabilities:
Communicate/Understand natural language.
Navigate the UI.
Utilize Cybereason API:
Answer questions based on data.
Perform actions (e.g., IR tools, Create new detection rules, etc.)
Autonomous investigation of an endpoint.

### Notes:

<!-- Slide number: 3 -->
# Cybereason API
Categories
Hunt and Investigate: File Search | Get File Search Requests, | Download Batch File
Respond to Malops: Query Malops | Get Malop Details | Isolate Malop Machine
Remediate Items: Remediate Items | Check Remediation Progress | Abort Malop Remediation
Respond to Malware: Query Malware Counts | Query Malware Types | Get File Reputation
Manage Reputations: Get Classification For Item | Update Classification Reputation
Get Threat Intelligence: Get File Reputation | Get Domain Reputation | Get Ip Reputation
Manage Sensors: Query Sensors | Upgrade Sensor | Retrieve Sensor Logs
Set Machine Isolation Rules: Get Isolation Rule | Create Isolation Rule | Update Isolation Rule
Manage Incident Response & Forensic Data Ingestion Tools: Run Incident Response Tool
Manage Users: List Users | Create User | Update User
Vulnerability Management: Retrieve Vulnerabilities List | Retrieve Details Vulnerable Machine

### Notes:
Cybereason API contain

<!-- Slide number: 4 -->
# AI Agent
Definition: “An AI Agent is an autonomous or semi-autonomous system, that uses artificial intelligence to perceive its environment, reason about what it observes, and take actions, either physical or digital, to achieve specific goals”.
An AI agent:
Utilizes a LM to reason and to choose actions.
Usually has set of “Tools” that it can utilize.
Advanced capabilities (optional): 	memory (short-term, long-term), RAGlearning & adaptation, etc.
There are several approaches to implement an AI agent: Chain-of-Thought (COT), ReAct, Plan & Execute , multi-agent system, etc.

### Notes:
COT: as it sounds, though (reason) in chain -> final answer.
ReAct: Loop ( Reason (thought) -> Act (action) -> Observe )
Plan & Execute: Plans an entire sequence of actions before execution.

<!-- Slide number: 5 -->
# AI Assistant Architecture
We developed the AI Assistant in Python using Langchain/Langraph packages.
We chose to implement our AI Assistant with a manager agent (a.k.a orchestrator) that utilizes set of ReAct agents, each has list of dedicated tools.

### Notes:
It is not trivial to make a tool from a single API, specifically if the API is complicated and contains a lot of parameters and a lot of options for each parameter.
We currently have 4 agents related to Cybereason, 3 of them uses Cybereason API.
CR API Agent
@Guy reviewed all API documentation via NEST.
Construct a class for each tool with the right description and parameters so the Agent can utilize them well.
Investigation and Detection Rule Agents
These 2 agents were created as ‘investihation’ and ‘detection rule’ APIs were too complicated so we exported them into a separate agents which has additional “assisting” tools that help the agent to utilize better the complicated API.
CR UI Agent
Based on the tools developed by @Shachar for MCP.
@Guy reviewed the entire pages within the UI. For each page understand all the available options, and filters
Construct tools that can build a QUERY URL based on natural language.
Sometimes we needed to add helper tools.
VirusTotal Agent
…
CVE Agent
…
MITRE Agent
…

<!-- Slide number: 6 -->
# AI Assistant

![](GoogleShape363p62.jpg)

### Notes:

<!-- Slide number: 7 -->
# AI Assistant Architecture

![](GoogleShape369p63.jpg)

### Notes:
Here is the architecture of the AI Assistant.
We chose to implement the assistant in Orchestrator architecture. It means that there is a main agent (the orchestrator) that manages a set of other agents.
The system is extensible with more agents and features.

—----------------------
It is not trivial to make a tool from a single API, specifically if the API is complicated and contains a lot of parameters and a lot of options for each parameter.
We currently have 4 agents related to Cybereason, 3 of them uses Cybereason API.
CR API Agent
@Guy reviewed all API documentation via NEST.
Construct a class for each tool with the right description and parameters so the Agent can utilize them well.
Investigation and Detection Rule Agents
These 2 agents were created as ‘investihation’ and ‘detection rule’ APIs were too complicated so we exported them into a separate agents which has additional “assisting” tools that help the agent to utilize better the complicated API.
CR UI Agent
Based on the tools developed by @Shachar for MCP.
@Guy reviewed the entire pages within the UI. For each page understand all the available options, and filters
Construct tools that can build a QUERY URL based on natural language.
Sometimes we needed to add helper tools.
VirusTotal Agent
…
CVE Agent
…
MITRE Agent
…

<!-- Slide number: 8 -->
# Code Architecture: Agents and Tools
Agent (Abstract)
React Agent
Tool (Abstract)
CR API Tool (Abstract)8,000 code lines
CR UI Tool (Abstract)

### Notes:

<!-- Slide number: 9 -->
# AI Assistant
LLM: GPT-5-nano (1/25 (0.04) of price in relation to GPT-5)
Guardrails
Embeddings-based (without LLM)
Orchestrator System-Prompt based (using LLM)
Memory:
Short-Term (session)
Traceability:
LangFuse / LangSmith
Azure AI Foundry

### Notes:

<!-- Slide number: 10 -->
# AI Assistant >> Production
Industry statistics show that most AI Agents do not make it to production:
Security & Safety.
Production requirements:
Traceability & Monitoring.

### Notes:

<!-- Slide number: 11 -->
# Future Enhancements
Saving Costs:
Reduce number of API calls to LLM
Learn from previous mistakes (based on memory)
Memory:
Long-Term (cross-session)

### Notes:

<!-- Slide number: 12 -->
# Live Demo

### Notes:

<!-- Slide number: 13 -->
# Live Demo Intro
Server:
150.136.124.181 (OCI)
Docker 1: AI Assistant – Web Server UI (port 8501)
Docker 2: LangFuse – Web Server UI (port 3000)
Environment:
https://secresearch-231.cybereason.net:443
Maor has executed some malwares.
Use Cases:
AI Assistant Use-Cases

### Notes:

<!-- Slide number: 14 -->
# Hackathon
Time: one single day: <date>
Start at: 10:00
Finish at: 17:00
Your Hackathon task:
Find out how the Assistant can help you with your tasks.
Use the AI Assistant to investigate the environment.
Find bugs and send your feedback.

### Notes:

<!-- Slide number: 15 -->

Questions?

### Notes:
