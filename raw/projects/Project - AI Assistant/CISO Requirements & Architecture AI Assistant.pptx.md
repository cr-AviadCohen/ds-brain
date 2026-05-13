# CISO Requirements & Architecture AI Assistant.pptx

<!-- Slide number: 1 -->
Managed Threat Research

# AI Assistant
Security AI Agent for the EDR platform

### Notes:

<!-- Slide number: 2 -->
# Project Goal
Develop an AI Assistant that can assist the user, within the UI.

![](GoogleShape718g3ca52424160_0_0.jpg)

### Notes:
Develop an AI Assistant that can assist the user, within the UI.

<!-- Slide number: 3 -->
# Project Goal
AI Assistant Capabilities:
Communicate/Understand natural language.
Navigate the Cybereason UI.
Utilize Cybereason API:
Answer questions.
Perform actions (e.g., Apply IR tools, Create new detection rules, etc.)
Autonomous investigation of an endpoint.
Utilize external security APIs

### Notes:
All what I show you today regarding AI Assistant and Cybereason API, can be applied also to any other API.

<!-- Slide number: 4 -->
# AI Assistant Architecture

![](GoogleShape733g3ca52424160_0_625.jpg)

### Notes:
In this slide you can see a high-level architecture of the AI assistant.The AI Assistant is a multi-agent system which contains an Orchestrator agent (management) and a set of Independent agents.
The flow:
When the user sends an input query to the AI Assistant, it is first passed through a Guardrails mechanism that is aimed to block unwanted question (OOC).
The decision of the guardrails (allow/block) is passed to the orchestrator.
If the Guardrails decision is to Block the request, then the Orchestrator will response with "I can’t assist with that request. You may rephrase or ask something else."
If the Guardrails decision to to Allow the request, the Orchestrator will choose which agent(s) to call in order to answer the users request.
The process of choosing the right agent for the user’s query is called Routing.
Once an agent/agents return their response, the orchestrator sends the response to the User.
The Orchestrator also send data to a tracking system so all the data is saved for monitoring/benchmarking/testing. I’ll talk about traceability later.
Now let's talk about the Agents:
Each agent in our system is independent. We can run/test it separately without the Orchestrator.
Uses ReAct approach: The agent alternates between reasoning (“what to do next”) and acting (calling a tool), until it can produce a final answer.
Has it’s own Language Model to reason and call tools.
Is initialized with a unique system prompt, and set of dedicated tools that are relevant to its purpose.
In our system, tools usually call some API, to retrieve data or do actions.
Examples for the agents you will see in the next slides.
Configuration file:
Guardrails configuration
Tracing configuration
Which agents to load?
What LLM to use for the Orchestrator and for each agent
and more..

<!-- Slide number: 5 -->
# Data Security Controls
Using Azure AI

![](GoogleShape744p4.jpg)
Enterprise-grade compliance – SOC 2, ISO 27001, GDPR, HIPAA eligibility.
Data isolation – Your data stays within your Azure tenant.
No training on your data – Prompts and outputs aren’t used to train foundation models.
Private networking – VNet, Private Link, and firewall integration.
Identity & access control – Azure AD / RBAC integration.
Regional control – Deploy models in specific geographic regions.
Centralized monitoring – Azure Monitor + Defender integration.

https://aws.amazon.com/bedrock/security-compliance/

### Notes:

<!-- Slide number: 6 -->
# Data Security Controls
Security controls already in place
Web App
LLM
MCP (VS APIs in our context)
Only accessible via TW Chicago / Warsaw VPN
Access is whitelisted
Users need to sign up for an account for access
Have Role-Based Access Controls (RBAC) in place
FILL ALL with guy and aviad
No data is being sent back to Anthropic
Uses Trustwave Spiderlab AWS account
Requires IAM permissions to access AWS Bedrock service
Encrypted EBS volume of the EC2 instance
LLM API requires an API key to be used by the web app
LiteLLM component for imposing rate limits, monitor usage/spending, verbose logging, etc.

All MCP servers used are hosted by us
Uses Trustwave Spiderlab AWS account
Tool prompts are configured by us
Read-only access
All MCP servers are authenticated and is only accessible by the web app
Web search tool is only scoped to specific sites in Google PSE

### Notes:

<!-- Slide number: 7 -->
# Data Security Controls
Other security controls to be put in place

Add LLM guardrails to mitigate prompt injections  - we already have Guardrails
Add SSL certificate and domain for web app - relevant for us? ask guy
Switch to private search engines e.g., DuckDuckGo, SearXNG - what are these?
  (web search is currently disabled)
Examine project by SpiderLabs penetration testers - sounds relevant for us

### Notes:

<!-- Slide number: 8 -->

![](GoogleShape770p7.jpg)
# Prompt Injection Attacks:
ask aviad to put his
Hunter like any other LLMs is susceptible to prompt injection attacks
The scope of such attacks is strictly related to the tools available for the model and datasets it operates
Read-Only access to tools prevents damage
Potential for data leaks
LLM guardrails will be implemented to minimize the risk of those attacks

### Notes:

<!-- Slide number: 9 -->
# Fusion OpenSearch Tool
Details and Available tools from MCP server
Connected to the SIEM-AF AMS cluster (Findings/Alerts) (via VPC Private Link)
Connected to the SIEM-PM AMS cluster (Events) (via VPC Private Link)
Connected to the Cybereason environment: __
Uses OpenSearch-py
Configured by us - us too
Available tools:
All CR APIs
Several TI APIs (such as VT, ..)
UI Navigation
- **SearchFinding**: Query Fusion SIEM for findings (alerts)
- **SearchEvents**: Query Fusion SIEM for events
 - **SearchAsset**: Search IPs/hostnames/MACs
- **GetFindingIndexMapping**: Retrieves index mapping and setting information for an index

### Notes:

<!-- Slide number: 10 -->

![](GoogleShape791p9.jpg)
# Web Search Capability
Hunter can now search the web
Uses Google PSE (Programmable Search Engine)
Limited to 10,000  search queries per day
Scoped to specific sites:

TODO:
Prevent any client sensitive information from being passed to the search engine
Switch to private search engines e.g., DuckDuckGo, SearXNG
Bleeping Computer
Malpedia
Mandiant
The Hacker News
Cybersecurity News

### Notes:

<!-- Slide number: 11 -->

![](GoogleShape801p10.jpg)
# Hunter
Finding analysis

![](GoogleShape798p10.jpg)

![](GoogleShape802p10.jpg)

### Notes:

<!-- Slide number: 12 -->
# Applicability of Hunter’s Capabilities to F2 (Fusion 2)

Search for specific findings / events via Natural Language Query
Summarize the findings and generate reports
Perform aggregations and generate plots
Craft KQL queries
Analyze exported raw logs from customer
Identify phishing emails
Search for specific information:
ServiceNow:  eg: specific keywords in notes
SharePoint:  eg: reports related to specific actor or IOC
Web search: eg: threat groups, CVEs, external threat reports

### Notes:

<!-- Slide number: 13 -->

Architecture Pros & Cons:  AWS Bedrock vs Google ADK
GTO Huntsman
SLR Hunter

![](GoogleShape820p12.jpg)

![](GoogleShape821p12.jpg)

5. FedRAMP compliant, data does not leave the AWS instance
5. Data sent to Google, may be used for training the models (free tier)

### Notes:
Generated using ChatGPT

<!-- Slide number: 14 -->

![](GoogleShape834p13.jpg)

![](GoogleShape835p13.jpg)

### Notes:
Generated using ChatGPT

<!-- Slide number: 15 -->

Hybrid Architecture Design: ADK & AWS Bedrock

![](GoogleShape845p14.jpg)

![](GoogleShape846p14.jpg)

![](GoogleShape847p14.jpg)
Hunter

### Notes:
Place the spider logo here

<!-- Slide number: 16 -->

### Notes:

<!-- Slide number: 17 -->
# Backup Slides

### Notes:
