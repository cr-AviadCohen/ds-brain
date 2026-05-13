# Project AI Assistant.docx

🏁 Main

**Project
AI Assistant**

#

# General

* **Description:**
  + Develop a Customer-facing (interactive) AI agent for Cybereason.
  + Agent capabilities:
    - Investigate:
      * “Think” and Investigate like Cybersecurity / GSOC analyst.
      * Utilizes Cybereason MCP tools.
      * Ability to solve complex tasks, such as:
        + SOC analyst investigation of a Malop, to determine if something malicious happen.
        + Incident Response
        + Compromise Assessment.
      * Reach the target goal autonomously, step-by-step (plan&execute / ReAct).
        Has the ability to interact with the user to ask for more information and clarifications, if needed, at any step.
    - UI:
      * UI Exploration/Navigation in natural language.
    - —-----
  + Quality:
    - Precision
    - Cost-effectiveness
    - Inter-session & cross-session memory, cross-customer learning.
  + **Design an AI Agent architecture that deliver the capabilities above, based on GPT-4o/GPT-5.**
  + **Challenge:**
    - **Guardrails: Stay only within the CR security context.**
    - **An autonomous agent is unpredictable of the count of requests it will use => unpredictable cost.**
* **Owner:** Guy Michaela KassorlaAviad Cohen
* **Architecture**: [AI Assistant Architecture](https://app.diagrams.net/#G1P9Rj0lkNdLYfxgjZonAQCO3jv7Lajuxo#%7B%22pageId%22%3A%22t69_rAp72j97BxaYh5y8%22%7D)
* [#Slack Channel](https://cybereason.enterprise.slack.com/archives/C096D7JD448)
* **Related Projects:**
  + [Project MCP](https://docs.google.com/document/d/10rsQ_rsij_7h-uq8Wd2AR53ZrOV5QxGrKBhwJA8RrKw/edit?tab=t.l2bxajtc8qht)
  + [Project IRCA](https://docs.google.com/document/u/0/d/1TGQQtkWq0in9PWVcHhaCIT4LHjve2XzpUBGWssQ_R5Q/edit)
* **Code:** <https://github.com/cybereason-labs/research_notebooks/tree/ai-assistant>
* **Jira:**
  + [ENG-2136: AI Assistant | Innovation POC](https://cybereason.atlassian.net/browse/ENG-2136?atlOrigin=eyJpIjoiMTUxMzA0MmJhZjhlNDRlYWIzNTAyZTc3N2MwMGM5NjYiLCJwIjoiaiJ9)
* **NEST API:** <https://nest.cybereason.com/s/article/cybereason-api-guide>
* **UI:**
  + [UI](https://docs.google.com/presentation/d/1uiNsqKPM9XG-zouRLYBxMEqVcPAni8R8-WOAI8xoteg/edit?slide=id.p#slide=id.p)
  + [Figma UI Owly](https://www.figma.com/design/fF9f6TgthvjH9lV18AWnec/Security-AI-Concepts?node-id=19-2331&p=f&t=DKjc9AMBcX5bMpVi-0)
* **More:**
  + [ChatGPT Deep Research on AI Assistant for Security](https://chatgpt.com/share/6890c4d6-e694-8003-b72a-22ce2dd81774)
  + [Using Route LLM to optimize LLM Usage](https://www.marktechpost.com/2025/08/10/using-routellm-to-optimize-llm-usage/)
* [**Cybereason Nest**](https://nest.cybereason.com/s/knowledge-base?language=en_US&article=incident-response-api-token-manage-incident-response-and-forensic-data-ingestion-tools#manage-incident-response-and-forensic-data-ingestion-tools&language=en_US)
* [**CISO Requiremenst**](https://docs.google.com/document/d/1SiSfBJ8fKFPMfj3qYhO9Msa4zbDGOUQnScuHNG4Or90/edit?tab=t.0)
* **Code:**
  + **AI Agents in Production:**
    - [https://diamantai.substack.com/](https://diamantai.substack.com)
    - [NirDiamant/agents-towards-production](https://github.com/NirDiamant/agents-towards-production/tree/main/)
    - <https://userjot.com/blog/best-practices-building-agentic-ai-systems>
    - [Best Practices for Building Agentic AI Systems: What Actually Works in Production](https://userjot.com/blog/best-practices-building-agentic-ai-systems)
    - <https://www.geektime.co.il/how-to-build-production-ready-ai-agents/>
  + **Frameworks:**
    - [Cybersecurity AI (CAI)](https://github.com/aliasrobotics/cai)
    - <https://github.com/openai/openai-agents-python>
    - <https://github.com/crewAIInc/crewAI>
    - <https://github.com/pydantic/pydantic-ai>
    - [GitHub - agno-agi/agno: Open-source framework for building multi-agent systems with memory, knowledge and reasoning.](https://github.com/agno-agi/agno)
  + [Langraph Plan&Execute](https://github.com/langchain-ai/langgraph/blob/main/docs/docs/tutorials/plan-and-execute/plan-and-execute.ipynb)
  + [Langchin – Hierarchical Agent Teams](https://github.com/langchain-ai/langgraph/blob/main/docs/docs/tutorials/multi_agent/hierarchical_agent_teams.ipynb)
  + —---------------------------------------
  + <https://github.com/langchain-ai/langgraph/blob/main/docs/docs/tutorials/rewoo/rewoo.ipynb>
  + <https://github.com/langchain-ai/langgraph/blob/main/docs/docs/tutorials/customer-support/customer-support.ipynb>

# OR

* **General**
  + An interactive AI Assistant, that can “think” and act (ReACT) by itself is unpredictable, can do mistakes, can call tools over and over, however, it can solve almost any problem, given that the relevant tools are in hand. Deterministic agent is more predictable but less sophisticated.
  + Product request: Develop an AI Assistant, similar to our competitors.
* **Questions:**
  + How is the product of the AI Assistant.
  + Who is the user? How does it consume our AI Assistant? Via UI? Via Claude Desktop?
  + How is going to use the AI Assistant? GSOC Analyst? Cybereason customer?
  + Why doing complicated things on natural language while I can do things easily on UI?
* **APIs:**
  + API wasn’t designed for AI.
  + Part of the APIs has too much parameters, Huge json files for parameters.
  + From where we can get the possible values for the parameters.
  + We have difficulties to validate the tools (e.g., POST tools):
    - Automatic check are too simple, and cannot true validate that the API works.
      * Code 200 is not enough.
    - We have to check it manually one-by-one and need help from env expert.
  + Investigation API:
    - This is the heart of the product for investigation, too complicated as a tool for AI assistant for professional & unprofessional use cases
    - Investigation UI Agent VS Investigation Agent (natural language)
* **Our needs:**
  + Provide real use-cases scenarios that we should strive to solve?
  + Prioritization of the use-cases to work on. We are spreading across too many cases: professional/unprofessional | UI/non-UI.
* **Suggestions:**
  + We can figure out what queries analysts to on the UI product and use that statistics to focus on specific scenarios.
    Search for Nest Step Project (ask Inbar Dekel)
  + Tool: Write relevant data to file.
  + Prioritize tools to work on (with Or).
    Come to the meeting with or with APIs table filled with “complexity” & “solution approach” (e.g., separate agent, methodology)
  + NEST API - Who can help us with understanding the APIs (Chen/Rotem)?
    - [@helena.makkaveev](https://cybereason.enterprise.slack.com/team/UA4563US3) (ortal) — consult on API on observe.
* **AI Assistant for Production:**
  + Assistant in natural language VS UI — do you want me to update the policy to X? Approve action on UI.
  + AI Assistant to production
  + Kobi’s expectations
  + Advanced capabilities (e.g., memory) | takes more requests / Money
  + Core -> Phoenix API

# Use-Cases

\*\* Idea: Guy Michaela Kassorla When the Assistant uses tools for investigation, it will also search for UI tools to “show” the user what is needed.

## Research

* [#AI Assistant for Security](https://cybereason.enterprise.slack.com/archives/C09804SN61Z)
* Meet Christie Kelly SOC manager to get use-cases.
* Get customer requirements from PRODUCT (Japan) based on users’ needs.
* Ask ChatGPT for use cases.

## Use-Cases Examples

### UI

* <https://eli-sal.cybereason.net:443> (Example)
* Show me XYZ
* Take me / go / jump /switch to:
  + hunt and investigate page
  + Investigation page
* Queries: Show me all processes that their parent
  + Build query -> URL

### General/Abstract Investigation (unprofessional)

* **Auto Investigation:**
  + <https://github.com/cybereason-labs/research_notebooks/tree/ai-assistant/ai_assistant/data/user_prompts>
  + Use the DryRun for IRCA project as a real scenario on which the AI Assistant can automatically investigate what happened on the machine.
    - Abstract investigation query: “I have a machine with malops and I want to know what happened on the machine and figure out if it is part of a malicious activity.

### Deep Investigation (Professional)

* **Claude:**
  + I want the command line of the process that triggered malop on ai hunt- AAAA07t0p4ZsnYnS
    <https://claude.ai/share/c47f141f-eda6-4e65-991a-58d750aa4cd7>
  + [Investigation with Claude & MCP](https://claude.ai/share/7fb0242f-2a8d-40cd-a9b5-3aa3df28db9c)
* Why Malop X was triggered?
* Ofir Tal
  + On how many machines did this file run?

On how many machines did cmd.exe run?
<https://claude.ai/share/3441a471-f449-4509-9124-9dc10bc2be93>

* + Where there any connections to this IP in the last 3 months?

where there any connections to this ip- 104.18.11.118 in the last 3 months?- <https://claude.ai/share/a778c2de-b40d-43c8-aa93-4de93a5ede5f>

* + Does this process tree is common in my organization?
  + Did this user ever executed this program?

did this user- solar1 ever executed powershell.exe?- <https://claude.ai/share/a15a310c-3c48-4926-b08d-611e88c26a69>

### Complex

* Investigation
  + UI
  + API
* Non-Investigation
  + Create new policy
  + Set custom detection rules

### More

* Add label (to UI)
* Guy Michaela Kassorla provide more use-cases like “add label

### More

* Tristan Madani
  + Help a beginner SOC analysis to investigate. Example:
    - Analysis: “This is the information I see on the endpoint machine. Does it look malicious?”
    - Analysis: “What should I check next?”
  + Scenario 1:
    - LSASS memory dump → credential theft detection.
    - Pivoting investigations using IP addresses or threat intel.
    - AI explaining events and guiding next steps can be a **game changer**.

# Questions

* LLM:
  + Local LLM on Prem or Cloud-based LLM?
  + Strong LLM vs Week LLM – ability to properly select tools.
  + Which abilities do we want to add to the agent?
* User approval logic:
  + Where to draw the line between more automated flow and mandatory human review? List all actions that require human review
  + Read-only actions: auto execute? else: require review?
* Long-Term memory (cross-session):
  + Assuming the retrieval is from a remote DB (and not local Mongo the customer runs), where is it located? GCP? OCI?
  + Each customer of Cybereason will have a dedicated long-term memory folder in a bucket? And within each customer folder, each of their users will have their own dedicated subfolder?
  + Automatic decision-making of allocating new information to the long-term memory
    - What are the signals for info to be added as a memory?
    - Criteria to consider whether the provided information throughout a conversation is viable to be a ‘memory’?
      * What content is relevant?
      * What the minimum/maximum structure required (length, etc.)
  + Architecture:
    - Do we need Vector DB vs. Graph vs. Hybrid?

# Tasks

## General

* Get access to the APIs documentation on [NEST](https://nest.cybereason.com).
* Request quota increase to GPT-5:
  <https://ai.azure.com/resource/quota?wsid=/subscriptions/7663b00e-8f86-4f1f-a4ac-9bb724c220f7/resourceGroups/rg-ai-research/providers/Microsoft.CognitiveServices/accounts/Cybereason-AI-Research-Sweden&tid=f34b03d6-27d4-4c65-ad49-f6252378a721>

## Exploration

* Examine develop agents on prompts:
  + <https://github.com/cybereason-labs/research_notebooks/tree/ai-assistant/ai_assistant/data/user_prompts>
* Shachar Wirzeberger Existing public implementations of AI Agents for Security (e.g., langraph community)
  + <https://chatgpt.com/share/68907287-9138-8003-85ee-67830eed402b>
  + Examples for Cyber AI Agents can be found in tab [Project AI Assistant](https://docs.google.com/document/d/1373kr8IU9j1cQ28x3lSLXIFd1O9an4MbxyJOs7u689U/edit?tab=t.tkannafy73l1)
* Shachar Wirzeberger Review the Xbot Project for relevant components that we may use
* Explore Cybersecurity AI agent <https://github.com/aliasrobotics/cai>
* How to build an autonomous AI agent, in general?
  + RE-ACT agent?
* How to build an autonomous AI agent for Cybereason?
  + What Python package to use in the implementation?
    - Langraph
    - Agno
* Ohav Peri What capabilities should the agent have?
  + CR MCP
  + Planning – divide mission to sequential tasks
  + Memory
    - User:
      * Short-Term (session-wise)
      * Long-Term (cross-session):
        + preferences
    - Cross-User:
      * Insights
      * Avoid mistakes
  + RAG-based memory which holds:
    - Cybereason terminology

## Milestones

* **Develop Tools for agents:**
  + Arrange all developed CR tools (MCP) as classes (instead of functions) so they can be used later by agents..
  + Create adapters to convert our tools to agent tools (e.g., Langgraph, etc.)
  + Validate all tools:
    - Make sure that the tools are working properly with the agent: Proper tool selection and proper application of the tool.
      * Develop a tool testing mechanism that receives a dataframe with user queries and validates that the proper tools is selected, and that the results are OK.
    - Improve the tools:
      * *\*\* specifically complicated tools such as hunt\_and\_investigate() which has a lot of params.*
      * Description, parameters
      * Add Few shot prompt if needed
    - Write automatic tests.
* **Examine different AI Agent architectures:**
  + RE-ACT
  + Plan&Execute agent
* **Examine AI Agent with different LLMs:**
  + GPT-4o
  + GPT-5
  + Open source SLM with [Ollama](https://ollama.com/) / [LM-Studio](https://lmstudio.ai/):
    - [Google-gemma3-270m](https://medium.com/data-science-in-your-pocket/google-gemma3-270m-the-best-smallest-llm-for-everything-efcf927a74be)
    - [gpt-oss-20b](https://huggingface.co/openai/gpt-oss-20b)
* **Examine different complex use-cases:**
  + [General/Abstract investigation prompts](https://github.com/cybereason-labs/research_notebooks/tree/ai-assistant/ai_assistant/data/user_prompts) (may use only simple GET tools)
  + Deep Investigation prompt (may use more complex tools (GET with params)
* **Improve agent capabilities:**
  + See “Advanced” below

## Advanced Capabilities

* Guardrails:
  + Using RAG/Router
  + \*\* require more requests = money
* Memory:
  + Short-Term (session-wise)
  + Long-Term (cross-session)
  + \*\* require more requests = money
* Self-improve / Learn from previous conversations:
  + How to select the right tools
  + Do not repeat the same mistakes
  + Cross-customer learning. Learn from mistakes made on other customers.
  + Leverage user-feedback to improve the model.
* Cope with Failures:
  + Limit tool calling retries.
  + Set a fallback when tool call fails after X retries.
* Cost-Reduction:
  + Deterministic Investigation to make a predictable amount of LLM calls.
    - The agent can in any case pull information from the end-point machine (needs the user to provide these details)
  + Reduce costs by choosing the right model to use for each case:
    [Using Route LLM to optimize LLM Usage](https://www.marktechpost.com/2025/08/10/using-routellm-to-optimize-llm-usage/)
  + Using Caching ([OpenAI](https://platform.openai.com/docs/guides/prompt-caching), [Gemini](https://ai.google.dev/gemini-api/docs/caching?lang=python))
  + Reduce model thinking (GPT-5)
  + Limit output tokens
  + Using SLMs
* Arrange all tools as classes instead of functions.
* Validate all tools:
  + Make sure that the tools are working properly with the agent: Proper tool selection and proper application of the tool.
* Investigation screen:
  + Meet with SR and examine popular cases and queries uses the investigation screen
  + Investigate the json of the investigation screen

## Hackathon

* \*\* Only after we deliver a working AI Assistant with all tools working properly.
* Test the Assistant guardrails – try to bypass and make the assistant be out of CR scope.
* Harness Security team to test whether the tools work properly:
  + All the tools at level 2/3 (not simple)
  + hunt\_and\_investigate()
* Technical:
  + Option 1: hackathon participants clone AI Assistant repo, play with it, and send us their results via mail, Google Form / Sheet
  + Option 2:
    - Raise our AI Assistant on a server, using Docker, with streamlit UI:
      * *\*\* we must verify that our server & CR Environement can handle multiple requests in parallel without crashing*
    - All conversations and feedback will be saved to a database.

## Memory

Ohav Peri

**Cost-Benefit Analysis:**

* Memory implementation initially seemed like a cost-saver by learning from past tool selection errors
* Reality: Additional API calls for memory management could actually *increase* costs (decision whether new input+llm response hold meaningful information worth memorizing - this process requires intelligent decision making, hence llm is a MUST)
* The juice may not be worth the squeeze

**Technical Concerns:**

* Learning from errors across multiple users risks introducing bias
* Generalizations from past mistakes may not apply correctly to new contexts
* Memory system adds complexity to an already multi-step process (embedding → memory decision)

**Project Scope Issues:**

* Proper memory implementation requires extensive testing and dedicated maintenance teams
* This level of investment exceeds the goals of a proof-of-concept project

## Guardrails

* System prompt
* Blacklist
* Allowlist

Ohav Peri

Initial exploration steps

* General research on guardrails
* Look for existing python packages
* Implement as a Class integrated seamlessly VS wrapper or other

Objectives

“Guardrails” is a concept - aiming to control:

* Costs
  + Number of LLM API calls, avoid unnecessary loops
  + Number of input tokens from requests and output tokens (both actual output and internal reasoning)
* Appropriate usage as intended by us
  + Malicious operations
  + Out-Of-Scope requests

Strategies

* Costs control
  + Set maximum iteration limits to prevent infinite loops
  + Add timeouts for long-running operations
  + Track token usage and enforce budgets
* Usage control
  + Input/Output validation
    - Nodes
      * Dedicated node at the start of the graph (orchestrator) that validates/sanitizes inputs
      * Exit node that validates responses before returning to users
    - Output match to response schema
    - Separate LLM call to judge response quality/safety
  + Prompt injection detection and inappropriate content
    - Libraries like *rebuff* or *llm-guard or Nvidia NeMO*
  + Prompt Instructions: Define explicit task boundaries and reject requests outside scope

Possible architectures

* Wrapper - wrapping the orchestrator
* Validation Nodes for input and/or output
* Separate LLM to critique actions before execution

Tool call guardrails

* Input parameters validation
* Require approval for "risky" actions - DB CRUD operations, etc.
* Rate limiting per tool (?)

Semantic “topic” guardrails

* Maintain a "forbidden topics" vector store and use embedding similarity to detect off-topic requests

Principals

* Rely on several guardrails, not a single one
* Default to rejecting request if unsure

<https://medium.com/data-science-collective/essential-guide-to-llm-guardrails-llama-guard-nemo-d16ebb7cbe82>

Main Risks for Cybereason Agents

* Hallucinations - leading to missed detections
* Off topic
* Jail break
* Send PII (?)

“Some guardrails (especially those involving additional LLM calls or complex external systems) can add latency and cost. Factor this into your design, especially for real-time applications.”

## Traceability

Aviad Cohen

* ~~Explore the best ways to bring traceability to our agent implementation.
  Focus on Langgraph agents.~~[~~https://chatgpt.com/share/690ed2ee-4784-8003-9c42-06b1135d7d2b~~](https://chatgpt.com/share/690ed2ee-4784-8003-9c42-06b1135d7d2b)
* ~~Traceability using~~ [~~LangFuse~~](https://langfuse.com/changelog/2025-11-05-langfuse-for-agents)
* ~~Traceability using~~ [~~LangSmith~~](https://smith.langchain.com/)
* ~~Custom Traceability using LLM hooking.~~

**Open Tasks:**

**Integrate the rag agent to the server:**

1. <https://cybereason.atlassian.net/browse/ENG-9037>
2. https://cybereason.atlassian.net/browse/ENG-9112

🤝 Meetings

**Meetings**

# Aviad:Ohav – 2025.09.21

* [Meeting NotebookLM](https://notebooklm.google.com/notebook/3dcd0ed2-04a3-4da6-a683-b211c304c53e)
* [Meeting Recordings](https://drive.google.com/drive/u/0/folders/1R6RQRvcLcYtMriePCRz_Xm-J4aFOaG4r)

The meeting between Aviad (Data Science team lead) and Ohav (Data Science team member) covered several technical, infrastructural, and procedural points related to agent development, testing, and tool utilization.

Meeting Summary

**1. Model Usage and Performance**

Initially, Ohav's code was using GPT-5, which took a significant amount of time to run. Although Ohav reported latency issues even with GPT-4o, they agreed to switch the working environment to **GPT-4** to see how performance progresses. Aviad noted that Shachar likely worked with GPT-5.

**2. Nest Access and Documentation**

Ohav required access to the Nest system to view structured documentation regarding various APIs, noting issues with understanding required parameters. They encountered difficulties accessing Nest. Aviad confirmed receiving new login credentials via email on July 31 and August 26, but Ohav did not receive them. When Ohav requested access, the system treated him as a customer. Aviad also noted that his attempts to log in redirected him to Salesforce, making the connection between Salesforce and Nest API access unclear. They have yet to successfully gain API access.

**3. Use Cases and Tool Complexity**

They reviewed the executed use cases:

* **Use Case Type:** Ohav was running a "more professional" use case found in the AI Assistant document, specifically the prompt: "I want the command line of process that triggers malop on AI hunt". Aviad moved this prompt to be categorized solely under "Professional".
* **Abstract vs. Professional:** Abstract, generic questions (like asking the model to extract information from a machine within a time frame) were separated into their own category. These abstract questions worked relatively well for Shachar because the agent chose simple tools that likely do not require parameters, reducing the chance of execution failure.
* **Complexity:** Professional use cases (like the command line prompt or Ofer Tal's questions) activate more complex tools that demand specific parameters, leading to higher potential failure rates.
* **Testing Necessity:** It is difficult to verify GPT-assisted tests if the model lacks specific environment information beforehand, often leading to general queries without concrete machine IDs or parameters. This results in a "blind spot" regarding the specific capabilities of tools for concrete use cases.

**4. Execution Strategy (Plan and Execute vs. ReAct)**

They compared the results of Plan and Execute (P&E) versus ReAct. P&E generates a plan before running. Aviad also demonstrated Shachar's basic ReAct, which Gai is familiar with, as her ReAct code is a copy of Shachar's but adapted for U-Z tools.

**5. Infrastructure and Logging**

* **404 Error:** Aviad experienced a 404 ("resource not found") error when trying to run Shachar's ReAct code. However, Ohav was able to successfully run the Plan and Execute strategy on their environment (Alice/Cell), which uses the same building blocks (tools, authentication) as the ReAct code, suggesting that Aviad's issue is likely a simple, small failure.
* **Logging Standard:** They concluded that all prints (to the console and to the file) must utilize a **logger** instead of direct print statements to ensure consistency. The console display should show simple INFO and ERROR messages, while the log file should include full DEBUG level information, detailing tool parameters and execution outcomes.

**6. Memory**

They determined that the Memory functionality **does not need to be integrated with Plan and Execute** and can be implemented separately or in isolation.

**Action Items**

Based on the discussion, the following action items and conclusions were established:

| **Area** | **Action Item** | **Details/Context** | **Source** |
| --- | --- | --- | --- |
| **Model Usage** | Continue working with **GPT-4**. | This is the current path forward following latency issues with GPT-5 and GPT-4o. |  |
| **Nest Access** | Aviad needs to check if **Gai has access** to Nest. | The issue of access to Nest documentation and APIs must be resolved. |  |
| **Use Cases** | Ohav is to continue working on the **more abstract Professional use case**. | This replaces the previous Professional use case Ohav was testing. |  |
| **Handover** | Pass information about tool execution complexity (abstract vs. professional prompts) to **Gai**. | This information will be used during the overlap/handover process. |  |
| **P&E Execution** | Modify Plan and Execute (P&E) to **print the full plan before execution starts**. | Currently, steps are only seen sequentially. The goal is to see the structured plan, then individual steps/results, and finally all steps and results upon completion. |  |
| **Logging** | Implement a **logger** for all output (console and file) instead of using print. | All console output should appear in the log file, ensuring full compatibility. |  |
| **Logging Levels** | Ensure console output shows simple **INFO** and **ERROR** messages. | The log file should contain **DEBUG** level information, including details about tool parameters and execution. |  |
| **Memory** | **Define what is desired** for the Memory feature. | Memory should be developed separately from Plan and Execute. |  |
| **Testing** | Generate **specific examples based on concrete data from the environment**. | This will address the blind spot caused by GPT models using general queries without specific parameters. |  |
| **Testing Generation** | Use **Cloud Desktop and MCP** to run a general investigation, then request it generates specific test questions (input) with concrete parameters and expected outputs. | This will provide a table of inputs and expected outcomes for verifying agent performance on concrete use cases. |  |
| **Testing Strategy** | Develop comprehensive **test sets for Cyberreason tools** that include both parameterized and non-parameterized questions. | This initiative, started by Shachar and continued by Gai, is crucial for testing the tools and ensuring no functionality is broken during development and fixes. |  |

# [Title]

…

XBot

# XBot Project

* **Description:** <complete>
* **Code:** <https://github.com/cybereason-labs/CybereasonAI/releases/tag/v1.1.0-beta>
* [**Zoom Meetings Recording**](https://cybereason.zoom.us/rec/share/FwFcVPHxRiisQ10d8PGWwUmn2NuM6s6Sq6xGvnZYQ5c6mJCJbSiIskUIHsPjwHBk.B-YJJXGfjc-Ybi7o?pwd=_llCpFojkgH3iMxfRChDnk-xme1JZgHF)
* [**Presentation**](https://docs.google.com/presentation/d/1ODdQmtyqXQFIvw0PQXr4G-OB7BvvjCCm/edit?usp=sharing&ouid=101899960277755867345&rtpof=true&sd=true)
* **XBot:** <http://cybereasonai.eng.cybereason.net/>(currently not active)
* **Confluence:** [https://cybereason.atlassian.net/wiki/spaces/PROD/pages/30752997694/XBot+Resources+GenAI](https://cybereason.atlassian.net/wiki/spaces/PROD/pages/30752997694/XBot%2BResources%2BGenAI)
* More Info:
  + Ask Seifeld (another name given to Xbot by the prior management. XBot is better)
  + Xbot also has an integration with slack, that is not working currently because the server is down.
  + NEST (Cybereason documentation): [https://nest.cybereason.com](https://nest.cybereason.com/user/login?destination=/)
  + the address for NEST questions / access: Rob Cameron / Jeremy Brown
  + NEST is going through changes now- so in case it’s back on the table, we need to modify the scraping code to scrape the documentation in the new structure of the NEST documentation.

Examples for Cyber AI Agents

הנה לינקים עדכניים (לרוב רשמיים, מאתרים אלו או מאגרי קוד מוכרים) עבור הדוגמאות שהוזכרו – כל קישור מוביל למקור ישיר:

### 🚀 מימושים של סוכנים בתחום הסייבר

| **דוגמה** | **תיאור** | **מקור (לינק)** |
| --- | --- | --- |
| **1. MITRE CALDERA / סוכן Sandcat** | Caldera הוא כלי קוד־פתוח לניסויי Red‑Team, וסוכן *Sandcat* הוא הסוכן הסטנדרטי שמפיץ את הפעילות מהשרת ל־host. | <https://github.com/mitre/sandcat> ([GitHub](https://github.com/mitre/sandcat?utm_source=chatgpt.com)) |
| **2. DARPA CASTLE** | פרויקט פיתוח סוכני AI להגנת רשת מבוססי reinforcement learning, המציע סביבה אמתית ללמידה והגנה אוטונומית. | [https://www.darpa.mil/research/programs/cyber‑agents-for-security-testing-and-learning-environments](https://www.darpa.mil/research/programs/cyber%E2%80%91agents-for-security-testing-and-learning-environments) ([DARPA](https://www.darpa.mil/research/programs/cyber-agents-for-security-testing-and-learning-environments?utm_source=chatgpt.com)) |
| **3. Nebulock** | סטארט‑אפ חדש (2025) שמתמקד בסוכני AI אוטונומיים לצייד ותגובה לאיומים בזמן אמת, משולב ב‑XDR. | [https://nebulock.io](https://nebulock.io/) ([nebulock.io](https://nebulock.io/?utm_source=chatgpt.com)) |
| **4. ReliaQuest GreyMatter (Agentic AI)** | פלטפורמת XDR שמפעילה סוכני AI תפקידיים אשר מבצעים זיהוי, ניתוח ותגובה אוטומטיים למקרים ברמות Tier 1–2. | <https://reliaquest.com/security-operations-platform/agentic-ai/> ([ReliaQuest](https://reliaquest.com/security-operations-platform/agentic-ai/?utm_source=chatgpt.com)) |
| **5. Microsoft Security Copilot – סוכני SOC** | מיקרוסופט הוסיפה 11 סוכנים (6 מבית Microsoft ועוד של שותפים) שמשולבים ב‑Security Copilot לביצוע משימות כמו טיוג, Phishing, ניטור פגיעויות וכו׳ באוטומציה. | [https://www.microsoft.com/security/blog/2025/03/24/microsoft‑unveils‑microsoft‑security‑copilot‑agents‑and‑new‑protections‑for‑ai/](https://www.microsoft.com/security/blog/2025/03/24/microsoft%E2%80%91unveils%E2%80%91microsoft%E2%80%91security%E2%80%91copilot%E2%80%91agents%E2%80%91and%E2%80%91new%E2%80%91protections%E2%80%91for%E2%80%91ai/) ([microsoft.com](https://www.microsoft.com/en-us/security/blog/2025/03/24/microsoft-unveils-microsoft-security-copilot-agents-and-new-protections-for-ai/?utm_source=chatgpt.com)) |
| **6. HoneyAgents (PoC על GitHub)** | מערכת תצוגת‑קוד (proof‑of‑concept) שמשלבת honeypot עם סוכן LLM, שמאתר פעילות זדונית, מוסיף deny‑list אוטומטית ומפיק סיכומי NL. | <https://github.com/mrwadams/honeyagents> ([GitHub](https://github.com/mrwadams/honeyagents?utm_source=chatgpt.com)) |
| **7. LLM Agent Honeypot (Palisade Research)** | מאמר ב־arXiv שתיעד ניסוי של honeypot עם מנגנוני prompt‑injection וגילוי AI-hacking agents (זוהו 8 סוכנים מתוך מעל 8 מיליון ניסיונות). | <https://arxiv.org/abs/2410.13919> ([arxiv.org](https://arxiv.org/html/2410.13919v2?utm_source=chatgpt.com)) |

Tasks-Guy

Inbar Dekel

Tasks:

* Examine how short term memory for react agent works.-

The agent’s memory is stored in LangGraph’s internal state (keyed by a thread\_id), which keeps the full conversation history, including user messages, assistant replies, tool outputs, and intermediate agent state.
 On each invocation, a selected portion of this history (after filtering and trimming) is passed as messages in the prompt, which is the only context the LLM actually “remembers” and uses to generate its response.

* Find a way how to decrease agent memory- take out the ToolMessage
* Research and implement memory for Orchestrator
* Add investigation screen UI Tool
* Check bug : Agent completed successfully
