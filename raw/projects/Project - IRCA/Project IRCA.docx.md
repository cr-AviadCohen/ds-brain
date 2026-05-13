# Project IRCA.docx

🏁 Main

**Project
Incident Response (IR)
Compromised Assessment**

# General

* **Description:** The core idea is to **automate the generation of incident response reports**, based on information from the Cybereason product (e.g., API, Databases, RAG, etc.) and digest them using AI (LLMs, AI-Agents). The goal is to provide a comprehensive report on a specific machine, if critical malops (malicious operations) are detected.
  + Explanation meeting with Eli Salem
* **Owner:** Guy Michaela Kassorla
* **Code:** [IRCA](https://github.com/cybereason-labs/research_notebooks/tree/IRCA/IRCA)
* **Jira:**
  + [ENG-2134: IRCA | Innovation POC](https://cybereason.atlassian.net/browse/ENG-2134?atlOrigin=eyJpIjoiNTAwMDEzZDUxMzBhNDkxNThlZDM5Yzc1Y2I5NTQzZGYiLCJwIjoiaiJ9)
  + [ENG-3924: IRCA | Support POC -> Production](https://cybereason.atlassian.net/browse/ENG-3924?search_id=9193948e-f507-4a81-b75e-5b5700a1c8ab)
* [AI IDEAS](https://docs.google.com/presentation/d/1VhtXwkaFx37GpKgowOJn8e99sOKRjQPBfh7_f7Xt7wM/edit?slide=id.g35da8df2ce6_0_40#slide=id.g35da8df2ce6_0_40)
* [**Architecture**](https://app.diagrams.net/?splash=0#G1caVqrv2WbVdR9JM_tPrvRHRqzPyYfQ0p#%7B%22pageId%22%3A%222QNm_1jnb87lQeNb1QMT%22%7D)
* [**NotebookLM**](https://notebooklm.google.com/notebook/42d1d791-064b-4f9b-87df-145feeef4896?authuser=0)
* **#**[**Slack Channel**](https://cybereason.enterprise.slack.com/archives/C095JQVCU05)
* **More:**
  + [IRCA fields](https://docs.google.com/presentation/d/1Z1FuY3aVtF5uY27Cqfx34iLMVhZgkgsu4atOZDy4N10/edit?slide=id.g371cdc71f8d_0_1335#slide=id.g371cdc71f8d_0_1335)
  + Security EPP
    <https://drive.google.com/drive/folders/1Lfo2sc97JirzqlyYju34OZrBz6jrR_UX>
  + [Security Research Group Training](https://cybereason.atlassian.net/wiki/spaces/SR/pages/30147117598/Security%2BResearch%2BGroup%2BTraining)
  + [Figma IRCA](https://www.figma.com/design/fF9f6TgthvjH9lV18AWnec/Security-AI-Concepts?node-id=210-7482&t=BxkUUN3kUYZ9aoC4-1)
  + [NEST APIs](https://nest.cybereason.com/s/article/cybereason-api-guide)
  + [EDR MalOps dashboard](https://lookerstudio.google.com/u/0/reporting/6e5eb866-c625-4c81-b479-929967a462e4/page/p_awlcvvxt3c)

# Questions

* Eli Salem
  + What data should be extracted from the endpoint machine, beyond processes, connection? What?
  + What are the set of recommendation steps:
    - Quarantine file?
    - Kill process?
* Or Golov AI-Agent for automatic:
  + Incident response?
  + Investigation (Ofir Tal)
* Or Golov is IRCA process interactive with the user? To get approval for response operations?
* There is a gap on the data collection process - api requests

# Tasks

## Meetings

* Meet with Eli Salem to understand how to collect the data to work on.
* Set a meeting with Chen Aviani to understand how to pull the data:
  + Get what are critical malops
  + API to get info from a certain endpoint:
    - Chosen processes
    - Processes with Malops
    - Processes with Detection Events
  + Google sheet with Possible:
    - Detection Events + Description -[full\_core\_release\_notes\_july\_25](https://docs.google.com/spreadsheets/d/1tLelQZA6TKE-A3UHdIAUFAKzvv-pQaaP8Vh5AsQcRs4/edit?gid=303700267#gid=303700267)(those detections doesn’t have description - maybe we will add description by using llm)
    - Malops + Description
  + Aviad CohenMeet with product to understand the scope of this project (ask Or Golov who from the product is relevant).
* Set a meeting with Andrey Kuznetsov (UI Designer) about IR appearance on UI.
* Set a meeting with Japan to show our POC

## Learn

* Simple AI-Agent using Langraph

## Design

* Understand & complete [**Architecture**](https://app.diagrams.net/?splash=0#G1caVqrv2WbVdR9JM_tPrvRHRqzPyYfQ0p#%7B%22pageId%22%3A%222QNm_1jnb87lQeNb1QMT%22%7D)
* How to generate the final IR report?
  + As the final report has several pages, should we compose different parts of the report using different prompts? (multiple LLM requests)
* AI Agent to act based on the report:
  + Come up with a realistic scenario of a critical malop => incident response with remediation recommendations, and check if there are MCP tools that can be used.

## POC

* Security Research to execute a real scenario of malop on which we can perform real incident response.
* Malop -> system -> llm -> incident report -> response
* IR -> AI Agent
  + Fallback if the action was not performed
* POC with Interactive UI using *Streamlit*
* [IRCA POC](https://docs.google.com/presentation/d/1iQrZfAl7kIuWBN82UTUjVbhvpJcEf2RHFLoDP-rG-a4/edit?slide=id.g3755f450dec_0_5#slide=id.g3755f450dec_0_5)
* [IRCA: Costs Evaluation Fields](https://docs.google.com/spreadsheets/d/1kBt0FLu2fZh_pvOlx0JMacYfLJo8gxp8VqrZ9c3whP4/edit?gid=0#gid=0)

## After POC

* Validation of the generated incident report:
  + Security value
  + Correct GUIDs
  + Correct linksURLs
  + Hashes
* Optimize the whole process to make it more efficient:
  + [?] LLM outputs IR API call with parameters, instead of IR as text to be parsed and built API call with parameters by the agent.
  + Shorter prompts
  + Less API calls, less tokens, less cost

🤝 Meetings

**Meetings**

# 2025.08.18 Guy: Rotem:Chen

1. Check how to extract file guid

# 2025.08.17 Guy: Rotem:Chen

1. Check if there is a way to collect info about if the process alive
2. Check of the agent is kill the process

# 2025.08.12 Guy: Rotem:Chen

[irca- notebooklm](https://notebooklm.google.com/notebook/308b2833-1fd4-4624-8ef1-11c9f6ada989)

**Meeting Summary: Prompt Enhancement for Security Incident Reports**

The meeting focused on identifying and implementing critical improvements to the prompt used for generating automated security incident reports. The goal is to enhance the clarity, accuracy, and actionability of these reports for our security analysts and researchers.

**Key Decisions and Action Items:**

* **Consolidate Repetitive Activities:**
  + **Action:** If the same process performs the same action multiple times concurrently, these actions should be **combined into a single entry** in the report.
  + **Detail:** The consolidated entry must explicitly state **how many times** the specific process executed that action. For example, multiple certutil.exe decoding activities occurring at the same timestamp (like in the provided bb-win11-23h2\_1754341200000\_report (2).pdf) should be merged.
* **Accurate Identification of Files vs. Processes:**
  + **Action:** The prompt needs to differentiate between executable processes and files/scripts.
  + **Detail:**
    - If a detected item is a file (e.g., a DLL or PS1 script) rather than an executable, it should be explicitly referred to as a "**file**" or "**script**".
    - When a DLL is identified, the report should state that "**the process loaded this module**" instead of implying the DLL itself is the process.
    - If possible, the **actual process that loaded the DLL** (e.g., Gadget.exe in the case of sidebar.dll) should be identified and mentioned. For script files like .PS1, it should be explicitly stated that it is a script.
* **Enhance Remediation Information:**
  + **Action:** When suggesting remediation actions like quarantining a file or killing a process, the report must include **more contextual information**.
  + **Detail:** In addition to the GUID, the prompt should include the **name of the process/file** and the **machine name**. This helps the analyst understand what is being quarantined/killed and assess if the proposed remediation is appropriate (e.g., to avoid quarantining legitimate system processes like Reg.exe). The format should be something like: "Quarantine file [File Name] (GUID X) on machine [Machine Name] (GUID Y)".
* **Add an Indicators of Compromise (IOCs) Section:**
  + **Action:** A dedicated section, ideally titled "**IOCs**" (Indicators of Compromise), will be added to the report.
  + **Detail:** This section will list relevant indicators, specifically **file hashes (SHA)** for malicious scripts (e.g., Powerview.ps1) and other non-legitimate files. This information is crucial for security researchers to implement further organizational protections like blocklists.
* **Improve Malware/Attack Chain Link Presentation:**
  + **Action:** For each line item in the activity report, or at least within a summary, provide **hyperlinks to the relevant malware analysis or root cause/attack chain details**.
  + **Detail:** Instead of just listing the URL, the link should be embedded within the text, for example, by making a phrase like "**here**" a hyperlink. If activities are consolidated, **all relevant malware links** for the consolidated activities must be included.
* **Ensure Data Consistency and Correctness:**
  + **Action:** Verify that the reported attack chain and sequence of events align with the actual scenario and observations.
  + **Detail:** This includes confirming the correct ordering of events such as certutil.exe operations followed by sidebar.dll loading malware, and the Mimikatz.exe and Reg.exe credential theft attempts.

These changes are aimed at creating more comprehensive and actionable security reports, facilitating quicker and more informed response actions by our teams.

# 2025.08.10: Aviad:Guy

* Optimize the whole process to make it more efficient:
  + Shorter prompts
  + Less API calls, less tokens, less cost
* LLM -> Report with IR API call (with parameters) -> deterministic.
* LLM/Agent is required for smart user interaction
* What to do if the IR action didn’t succeed?
* Approaches:
  + Or Golov: IRCA Agent connected to MCP and decides which tool to apply autonomously. MCP has 2 tools: action, validate
  + Guy Michaela Kassorla: Agentic workflow with langraph with deterministic steps (action, validate). Doesn’t require tools via MCP.
  + MCP is required only to expose your API to other customers in a standard.
  + If you are implementing your own agent, you don’t need MCP for tools/functions, as you can just call them at will.

# 2025.08.06: SR:Guy

* Following Or Golov’s participation in the daily meeting and his observation that the current data collection method is suboptimal, we held a follow-up session with the Security Research team.
* During the meeting, they attempted to find a more efficient way to retrieve malops for a specific machine.
* Despite efforts, they were unable to resolve the issue.
* for now, we will continue using our current method. Once Noa Perach Novogroder is available, she will be looped in to create a new API request that can retrieve the required data.
* **the data collection process is not production-ready.**
* The SR task of collecting all necessary fields to construct the JSON for the LLM is still incomplete — we currently have only a partial set. They plan to continue working on it tomorrow.
* I received the machine details from Chen Aviani, and Eli Salem has already run the necessary queries on it.
* The remediation API request is still not working. Tomorrow, Chen and I will work on it together.

# 2025.08.05: Aviad:Or:Eli

* Eli Salem will ask the NOC to raise a regular dev environment with the latest sensor for our project (it should happen today)
* They will run a DryRun test on it – it contains many malops executed serially.
* That will provide us with the data we need for the POC.

# 2025.07.31: Aviad:Or

* On IRCA project, the *AI Agent* focuses on IR, NOT ON INVESTIGATION.
  We don’t want to replace our MDR (we won’t get any cooperation if we talk about replacing SOC analysts).
* Change *AI Agent* on diagram to *AI Assistant*
* [Deep Research with ChatGPT on Incident Response](https://chatgpt.com/share/688b67c3-90c8-8003-84a0-3e4453dc6e4d)
* [Figma IRCA](https://www.figma.com/design/fF9f6TgthvjH9lV18AWnec/Security-AI-Concepts?node-id=210-7482&t=BxkUUN3kUYZ9aoC4-1)

# 2025.07.31: Aviad:Or:Azuma

* The AI agent should interact with the user to ask it for more information and approval to do things.
* The IRCA project probably utilize the [Project AI Assistant](https://docs.google.com/document/u/0/d/1373kr8IU9j1cQ28x3lSLXIFd1O9an4MbxyJOs7u689U/edit) agent for the IR.
* POC in 3 weeks.

# 2025.07.28: Aviad:Guy:Eli:Chen:Rotem – Understanding EDR Data

* [NotebookLM](https://notebooklm.google.com/notebook/451d57d3-60cc-405b-aefe-f0524dc98af8)
* [Recordings](https://drive.google.com/drive/u/0/folders/12T4k8hG3RVQVDR5ECROJrTxJJj3K8ksB)
* [IRCA fields](https://docs.google.com/presentation/d/1Z1FuY3aVtF5uY27Cqfx34iLMVhZgkgsu4atOZDy4N10/edit?slide=id.g371cdc71f8d_0_1335#slide=id.g371cdc71f8d_0_1335)

The meeting between the Data Science Team (Aviad and Guy) and the Endpoint Security Team (Eli, Chen, and Rotem) aimed to enhance the Data Science team's understanding of key terminology, particularly concerning **engines and malops**, as they found themselves not fully grasping certain technical terms during discussions with Rotem. The Data Science team sought to organize and clarify information about the various **engines and the differences between sensor-based and server-based malops**. The meeting was recorded to ensure a structured review of the information afterward.

Here's a comprehensive summary of the key topics discussed:

**1. Types of Malops and Detection Events**

* **Two main types of malops** were identified: **sensor-based malops** and **server-based malops**.
  + **Server-based malops** are older and are typically triggered by specific process names and command lines, such as the "Cardinal" example. These are detected through detection events that are verified.
  + **Sensor-based malops** originate from various engines, including EPP (Endpoint Prevention and Protection). Examples of these engines include:
    - **VPP (Variants Process Protection)**: Detects code operating within a process's memory.
    - **VFP (Variants File Protection)**: Scans files on the disk, specifically executables.
    - **Fileless**: Focuses on PowerShell scripts that operate in memory. The name "Fileless" refers to the scan occurring in the PowerShell memory, not on the file itself.
    - **BPF (Behavioral Prevention Framework)**: Based on kernel callbacks, it can block processes based on their characteristics, such as process name, product name, and command line. This logic is similar to EDR but specifically focuses on blocking.
  + There is also an **antimalware engine** (from BitDefender) that is visible in the system, but it is not managed by their team.
* **Malops vs. Detection Events**:
  + Not every detection event becomes a malop. A detection event is converted into a malop if it is "verified".
  + **Verified rules** trigger a malop and block the activity, whereas **Audit rules** do not block.
  + Rules can be categorized into groups (e.g., "POC" for testing, "Verified" for active blocking).
  + A detection event without an associated malop will only be visible if specifically searched for in the investigation screen under "detection event".
  + It's possible for **one process to trigger multiple detection events and even multiple malops**.

**2. The Cybereason Platform (UI)**

* The system being viewed during the meeting is the **Cybereason product**.
* It serves as a **customer-facing environment**, allowing customers to view information from their EDR (Endpoint Detection and Response).
* The UI displays **customer-specific information**, including details about their machines, users, and processes running on those machines.
* Each customer has a single UI to see their own data, without overlap.
* The investigation screen within the UI allows users to **build queries to search for specific events**, such as a CMD opening a reg process.
* The UI centralizes data from all sensors on a customer's many machines.

**3. API Usage for Data Retrieval (for the Data Science Team's POC)**

* The Data Science team's goal is to retrieve all relevant data for a specific machine within a given timeline, including detection events, malops, and chosen processes.
* The proposed process for data retrieval involves:
  1. **Start with the detection inbox API**: This API provides a list of all existing malops in the environment, including both server-side and EPP/sensor-based malops. It also supports filtering by time range.
  2. **Filter by detection\_engine field**: If the detection\_engine field is "EPP", it indicates a sensor-based malop. If it has any other value, it's a server-side malop.
  3. **For Sensor-Based Malops (EPP)**: The detection API provides all necessary information directly, including the process command line, user, machine, process name, creation time, details about whether the engine identified or blocked the activity (depending on customer policy), the signature name (e.g., "Gozi"), and a brief description of the engine.
  4. **For Server-Side Malops**:
     + Use the Rest Crimes Unified API, providing the GUID (Globally Unique Identifier) obtained from the Rest Detection Inbox API.
     + This API provides most information but **lacks the process command line**.
     + To get the command line, an additional query is needed in the investigation screen (UI) using the process GUID. This query aims to find all processes linked to the malop, providing details like process creation time, command line, end time, name, and parent process information.
* The Data Science team is responsible for connecting the data using the API queries and filtering it by machine. The server-side developers might eventually create a unified JSON or SQL database for them, but for the current POC, the Data Science team will perform the data connections themselves.
* The team confirmed that there should **not be duplication** when pulling detection events and malops separately, though a single process could trigger multiple malops.

**4. Resources and Next Steps**

* **Existing resources**: Confluence pages and old videos on a shared drive were mentioned as resources for understanding engines.
* **Technical demonstration**: The Endpoint Security team will provide a **Jupyter Notebook** with Python code demonstrating how to interact with the APIs, make queries, and retrieve data. This will serve as a practical starting point for the Data Science team.
* They also planned a **joint demo** to identify a "critical malop" together and pull all relevant information to see the complete data flow.

The meeting concluded with an agreement for continued collaboration and the provision of the technical resources as discussed.

# 2025.07.14: Aviad:Guy:Eli:Chen

* **Why “Compromise Assessment”?**
* **Questions:**
  + Processes information:
    - From where we pull the information?
  + RAG:
    - Why is RAG needed? Isn’t that information available in the API, same as the processes infor?
  + Incident Response Report:
    - Example of expected output, what should it contain?
* **Knowledge:**
  + [Eli's ChatGPT](https://chatgpt.com/share/68517b0c-cefc-800f-a441-2e6c8df4bec1)
  + [full\_core\_release\_notes\_july\_25](https://docs.google.com/spreadsheets/d/1tLelQZA6TKE-A3UHdIAUFAKzvv-pQaaP8Vh5AsQcRs4/edit?gid=303700267#gid=303700267)

# 2025.06.30: Aviad:Eli

* [Recordings](https://drive.google.com/drive/u/0/folders/10p4MWo45rtz00ounGn6mBrmQmgxkkjY2)
* [NotebookLM](https://notebooklm.google.com/notebook/96bd8363-6e43-4a13-9482-86310a01920d)

The discussion outlines a proposed solution to significantly **reduce the time it takes for security incident response teams to generate comprehensive reports** after a cyber event.

**The Problem:** Currently, when a cyber incident occurs in an organization, it takes a considerable amount of time for Incident Response (IR) teams to arrive and provide a structured report with recommendations. Security Operations Center (SOC) teams, who analyze incidents daily, operate on tickets, and it can take time for an analyst to get to the right ticket and begin an investigation. If a major incident is identified, more professional IR teams are brought in, but if they are external, it can take hours to days just for them to start working due to legal and financial considerations. Even after they begin, it takes additional hours to days to deliver a full report detailing what happened, what was stolen, who breached, where they breached, and recommended remediation actions like changing passwords or hardening rules. Importantly, these IR teams only provide recommendations; they do not perform the actual mitigation actions.

**The Proposed Solution:** The core idea is to **automate the generation of incident response reports** using information from Cybereason. The goal is to provide a comprehensive report on a specific machine if critical malops (malicious operations) are detected.

![](data:image/png;base64...)

**How the Solution Works:**

1. **Trigger Event**: The process begins when a critical malop is detected on a machine.
2. **Data Collection**:
   * Specific processes from the affected computer are selected, including all processes on which malops were detected.
   * "Detection events" (non-malicious actions from the sensor) are also collected.
   * The raw data collected includes process names, their command lines, and timestamps.
3. **Contextualization and Enrichment**:
   * This raw data is supplemented by information from two "regs" (registries or knowledge bases).
   * **Malop Meaning Reg**: One reg will contain the names of malops and their significance (e.g., "Use of Power" indicates a malicious PowerShell operation, and "Credential Dumping" indicates a dump of credentials from the registry or LSASS memory).
   * **Detection Event Context Reg**: Another reg will provide context for detection events (e.g., if a "qbot" detection event from "ps\_prevent" occurs, the reg will explain that a PowerShell process ran Mimikatz in memory).
4. **Report Generation**: All the raw data and contextual information are fed into a **language model** (such as GPT). The model uses a suitable prompt to generate a full incident report. Fine-tuning the model may not even be necessary.

**Report Content and Scope:** The generated report is expected to detail **what happened, what was stolen, who breached, where the breach occurred, the impact, mitigation methods, and necessary next steps**. While the current focus is on reports for a **single machine**, multiple machine-specific reports can be combined to form a larger, systemic report.

**Proof of Concept (POC) and Data Acquisition:**

* The project is currently a **concept**.
* It's believed to be relatively simple to create a POC.
* To build the POC, **data from an environment where malops have occurred is needed**.
* APIs are available to query entire environments and retrieve necessary data, including malops, chosen processes, and processes associated with malops.
* The team plans to use their **"Dry Run" environment** (used for MITRE ATT&CK testing) for data, as it contains relevant malop and process data all on the same machine.
* Exporting data to CSV from the UI is an alternative, but it might not contain malop information directly.

**Team and Future Plans:**

* **Andrey Restman Kuzavtsov** prepared a Figma design for a dashboard visualization of this system.
* A team member named **Guy (Gai)** is learning about the project and has strong security knowledge; she is being considered to work on the RAG (Retrieval Augmented Generation) implementation.
* The project is expected to officially start when Guy has more capacity after her exam period.
* The team has submitted their work to **Black Hat**, a top cybersecurity conference, and are hopeful for acceptance, which would be a significant achievement. They also plan to submit to "Low Code" and then focus on writing a more comprehensive academic paper.

…

✅ Code Tasks

**Tasks**

### **1. Data Collection Layer**

**Goal:** Collect raw data from the target machine via API and file ingestion.

#### **Tasks:**

* **~~1.1 API requests:SR~~**
  + ~~Malops:~~
    - ~~sensor~~
    - ~~server~~
  + ~~Detection events~~
    - ~~They need to give us more fields~~
  + ~~Important processes~~
* **~~1.2 Create detection explanations~~**
  + ~~Malops explanations json~~
  + ~~Detection events explanations json - we generate explanations with llm- SR should check them.~~ [~~detections event explanations~~](https://drive.google.com/drive/folders/1_rw277ZSM0lPcID6-f3mpNTyJv_PR2f9)

### **2. Data Structuring & Contextualization**

**Goal:** Prepare data into a format suitable for LLM consumption.

#### **Tasks:**

* ~~2.1 Map the relevant fields from each type of api request- SR~~[~~IRCA fields~~](https://docs.google.com/presentation/d/1Z1FuY3aVtF5uY27Cqfx34iLMVhZgkgsu4atOZDy4N10/edit?slide=id.g371cdc71f8d_0_1335#slide=id.g371cdc71f8d_0_1335)
* ~~2.2 Create a configuration json file include all the relevant fields~~
* ~~2.3 Prepare the data- filter the relevant fields and add the detections/malops explanation: we have got problem with the processes fields~~

### **3. Prompt Engineering Layer**

**Goal:** Convert structured context into a well-formed prompt for the LLM.

#### **Tasks:**

* **~~3.1 Design prompt template~~**

### **4. LLM Interaction Layer**

**Goal:** Use the LLM to generate the IR report.

#### **Tasks:**

* **~~4.1 Query the LLM~~**
* **~~4.2 Validate output with SR~~**

### **5. Apply AI-Agent on Remediation Steps**

**Goal:** Trigger API-based actions based on LLM's recommended steps.

#### **Tasks:**

* **~~5.1 Parse remediation section-~~** ~~Extract structured actions and their parameters~~
* **~~Apply Remediation Steps:~~**
  + **5.2 Use a deterministic approach to iterate over remediation steps and do them.**
  + **~~5.3 Apply Auto AI-Agent on the remediation step~~**
    - **Fix the api remediation**

#### **SR Tasks:**

ELI

* ~~Collect the data~~ [~~IRCA~~](https://docs.google.com/spreadsheets/d/1_t-JJ96rLDo3d1sWNQNFuhU_gwkA0eUcy4sjKSEQ8dY/edit?gid=0#gid=0)
  + ~~Api requests+Map the relevant fields~~
    - ~~Malops~~
    - ~~Detection events- api done, relevant fields~~
    - ~~Important processes~~
  + Create a list of critical Malops that will trigger the pipeline
  + How many critical malops (that trigets IRCA) per day? we can get statistics from [@Chen Aviani](https://cybereason.enterprise.slack.com/team/U01CS20GRTQ) [@Rotem Rostami](https://cybereason.enterprise.slack.com/team/U020LGQDTPX)):
    - for a specific large customer?
    - for all of our customers?
  + ~~Make sure we collected all the remediations steps~~
* ~~Check the detection events explanations-~~[~~detections event explanations~~](https://drive.google.com/drive/folders/1_rw277ZSM0lPcID6-f3mpNTyJv_PR2f9)
* ~~Build a few scenarios that trigger the pipeline so we can check him.~~

Agent

# Evaluation: Should We Use an AI Agent for the IR Automation Project?

## Project Overview

The goal of this project is to **automate the generation of Incident Response (IR) reports** based on data collected from a specific machine. The input includes:

* Detection events and active processes (fetched via API)
* External files that contain short explanations for each detection

The output should be:

* A clear, detailed IR report explaining the incident and its timeline
* Recommended response actions
* Optional execution of those actions through API integrations

The system uses an LLM (Large Language Model) to generate the IR report and may integrate with internal APIs to automate remediation.

## Key Question

**Should we implement the logic using a dynamic AI Agent (e.g., LangGraph or LangChain agent) or build a traditional modular pipeline in Python?**

## Benefits of Using an AI Agent

| **Benefit** | **Description** |
| --- | --- |
| **Dynamic Decision-Making** | The agent can decide which tools/actions to use based on the context of the incident. |
| **Easier to Scale & Extend** | Adding new capabilities (e.g., querying additional data, trying multiple response paths) doesn’t require rewriting logic. |
| **Natural Integration with LLMs** | The agent can interpret the IR report and decide on appropriate responses directly, reducing hardcoded logic. |
| **Conversation-Aware** | Agents support memory and multi-turn interaction, which can be helpful if user approval is needed before execution. |
| **Tool-based Structure** | Encourages clean separation between tools (e.g., get\_processes, kill\_process) and decision-making logic. |

## Drawbacks of Using an AI Agent

| **Drawback** | **Description** |
| --- | --- |
| **Complexity** | Agent frameworks introduce new abstractions and may require more debugging, especially for multi-step reasoning. |
| **Resource Overhead** | If not well-constrained, agents may make multiple unnecessary LLM calls, increasing latency and cost. |
| **Less Predictable** | Behavior is more dynamic and may vary depending on the model’s interpretation of context. This can be risky in sensitive response operations. |
| **Harder to Control** | In high-stakes environments (like killing processes or isolating endpoints), deterministic logic may be preferable. |

## Analysis: Fit for This Project

| **Factor** | **Relevance** | **Assessment** |
| --- | --- | --- |
| **Structured Input Data** | Processes and detections are predefined via API | ✔ Suitable for deterministic logic |
| **LLM Required for Report Generation** | Yes, needed to summarize and write narrative | ✔ Can be embedded in either approach |
| **Action Execution** | Requires calling predefined API endpoints | ✔ Could be done with or without an agent |
| **Dynamic Decision Flow** | Future expansion may include choosing different actions per incident type | ✔ Favorable for agent architecture |
| **Resource Constraints** | Efficiency is important | ⚠ Agent must be tightly managed to avoid waste |

## Recommendation

**Start with a modular, deterministic pipeline** (e.g., functions for detection, data collection, LLM reporting, and response execution). This provides:

* Full control over logic
* Efficient use of resources
* Easier debugging and validation in early stages

Then, as the system matures and more **dynamic behavior or scalability** is required (e.g., branching logic, new tools, user interaction), consider **transitioning to an Agent architecture** using LangGraph or LangChain.

## Hybrid Option

You can also combine both:

* Use a **static Python pipeline** for detection → data collection → LLM
* Use a **simple agent step** *only* for interpreting the LLM output and choosing actions (with clear guardrails)

## Conclusion

While an AI agent offers flexibility and future-proofing, it adds complexity and cost. For the current scope — where the data is structured and the flow is predictable — a **modular Python pipeline is the best starting point**. If the system evolves toward more complex logic, agents can be incrementally introduced.

Prompt issues (agentic report)-

Presentations

# IRCA POC for Japan

**PRESENTATION NOTES:**

* **IRCA POC:**
  + As I showed earlier in the IRCA architecture, there are 2 phases:
    - 1) Data collection phase.
    - 2) AI:
      * Automatic Generator of Incident Response Report
      * Automatic-Interactive Response
  + Now we will ask IRCA to collect the data from the target machine, within a chosen time-range, it will take about 20 seconds.
    Next, we will generate an Incident Response report.
* **Data Collection**
  + We collected all of the malops, detection events and critical processes from a specific machine, at a specific time range.
  + We collected the data using multiple API requests.
  + Since currently, there is no way to pull the data for a specific machine, we pull ALL malops, for ALL machines, from the environment, than filter them on the specific machine – it is not the optimal, but will be solved by creating a new API that allows getting malops from a specific machine.
  + We develop the data collection for the EDR, and we can adapt it, with minor changes, to any other products (e.g., XDR, Phoenix, etc.)
  + ![](data:image/png;base64...)
* **Report Generation:**
  + [Report](https://drive.google.com/file/d/18jfjR1PCe2AYE0Atc9Y3gyKW0A6_YqpO/view?usp=drive_link)
  + We created the report using LLM (gpt-4o), and designed it according to the UI Figma.
  + The report includes the following sections:
    - **Executive Summary:**
      * A basic summary of what occurred in the incident
    - **Narrative of Events:**
      * Shows all of the MalOps that were involved in the incident (show link)
    - **Impact Analysis:**
      * How does the incident impact the machine?
    - **Root Causes & Attack Chain:**
      * This section is divided according to MITRE tactics (show link)
    - **Remediation Recommendations:**
      * Also divided based on the remediation capabilities of the platform (e.g., Kill process, quarantine, etc.)
    - **Artifacts Triggering Detection MalOps:**
      * This includes all of the IOCs that were involved in the incident – we can see here the paths/hashes of the artifacts.
    - **Next steps:**
      * General recommendations
* **Interactive Remediation**
  + We created an AI agent (agentic workflow using *Langraph*) that parses the natural language remediation requests, extracts the parameters, and builds the API request for remediation.
  + The agent asks for user approval for each remediation step.

Tasks

IRCA TASKS: Inbar Dekel

* Ziv Request- Run IRCA ON Real malware
  **Use case**[IRCA Use Cases - DryRuns](https://docs.google.com/spreadsheets/d/117uiZCVmaFkpB6oGuIAyBjI5j_EEz4Nz3JUvcsioeLQ/edit?gid=0#gid=0)

**Reports** :[IR Report](https://drive.google.com/drive/folders/1Fwe3v9DVryaz2w6KjoChgps44_kZClO6)

Following a run of IRCA on this use case and an examination of the results with Maor Gabay, the following gaps were identified:

* **Artifacts List Gap:** The final report's artifacts list does not include suspicious .exe files. This should be resolved by verifying if the files or executables are malicious (e.g., using VT/signature checks).
* **Remediation Gap:** Malicious executables are not included in the remediation steps.
* **Data Collection Gap:** More environmental data needs to be collected, specifically connections and DNS information.
