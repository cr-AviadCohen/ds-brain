# AI Assistant - Gate 1 - Research Impact & Feasibility.docx

# **Gate 1 - Research Impact & Feasibility**

## **Project Information**

**Project Name:** AI Assistant

**Innovation Lead:** Inbar Dekel, Aviad Cohen, Guy Michaela Kassorla

**Date:** 20/4/2026

## **Project Definition & Approach**

**Clear problem statement - What specific problem are you solving?**

Security analysts today are forced to switch between multiple tools, and manually orchestrate investigation steps across different data sources. This creates friction, slows down investigations, and increases dependency on deep platform expertise.

Our AI Assistant is addressing this friction by introducing a natural language interface that sits on top of the entire platform. It allows analysts to both retrieve information and execute investigation actions directly from a single conversational flow, without needing prior knowledge of where features live or how to operate them.

By seamlessly integrating with internal platform APIs and external threat intelligence sources, the assistant transforms investigation workflows from fragmented, UI-driven processes into a guided, end-to-end experience. Analysts can stay focused on decision-making rather than navigation, significantly reducing investigation time and improving efficiency.

Unlike a basic conversational interface, this assistant is deeply integrated with platform capabilities and investigation workflows, enabling not just answers, but real actions and end-to-end task execution.

**Previous attempts - Have there been previous attempts to solve this problem? What happened to them?** (Research what's been tried before, learn from past failures, justify why your approach will be different, avoid known pitfalls)

No previous attempts. There is an AI-Assistant that the engineering team has worked on, but we don’t have any details on how it was implemented and what the capabilities are.

**Success criteria - How will you know if it worked?**

The assistant already meets key success criteria across system performance and safety, and the focus now is on driving product impact and adoption.

From a system perspective, the assistant is capable of reliably answering user questions using Cybereason APIs, with strong orchestration quality:

* Orchestrator agent selection accuracy > 80%
* Agent tool selection accuracy > 80%

These metrics validate that the assistant can correctly translate natural language into concrete investigation actions and API calls, making it operationally effective—not just conversational.

From a safety perspective, guardrails are in place to detect and block out-of-context or unsupported requests, ensuring controlled and predictable behavior aligned with platform capabilities.

Given this foundation, success will now be measured by real user impact: adoption by analysts, integration into daily investigation workflows, and reduction in the need to manually navigate the UI to retrieve information or perform actions.

**Approach - How are you building this?**

The AI Assistant is built as a centralized, hierarchical multi-agent system designed to translate natural language into reliable investigation workflows across the platform.

At its core is an Orchestrator agent that manages a set of independent, specialized agents. This architecture allows us to scale horizontally—new capabilities can be introduced simply by adding new agents, without impacting existing functionality.

End-to-end flow

Every user query goes through a controlled and observable pipeline:

* Guardrails layer - The request is first validated to detect out-of-context or unsupported queries.
* Orchestration & routing - If approved, the Orchestrator determines which agent(s) should handle the request. This routing step is key to mapping natural language into the correct investigation capability.
* Execution - Selected agents independently retrieve data or perform actions (via APIs or internal tools).
* Response composition - The Orchestrator aggregates results into a single, coherent response to the user.
* Tracing & observability - All decisions, actions, and intermediate steps are logged for monitoring, evaluation, and continuous improvement.

This design ensures the system is not only flexible, but also traceable.

Agents design principles:

Each agent is built to be:

* Independent - Can be developed, tested, and deployed in isolation.
* Autonomous - Decides how to achieve its goal, including selecting and chaining tools.
* Specialized - Has a clearly defined role, system prompt, and set of tools.
* Model-optimized - Uses the most appropriate LLM for its task (e.g., lightweight models for simple tasks, stronger models for complex reasoning).

Agents do not communicate directly with each other. Coordination is fully managed by the Orchestrator, which keeps the system predictable and easier to control.

Tools & capabilities

Agents interact with the platform primarily through API-backed tools, enabling them to both retrieve data and execute real investigation actions. This is what allows the assistant to go beyond answering questions and actually operate within the platform.

Memory & conversational context

Both the Orchestrator and agents maintain configurable short-term memory within a session. This enables natural, multi-step investigations without requiring users to restate context at every step.

Configurability & extensibility

The system is highly configurable via a central configuration layer, including:

* Guardrails behavior
* Tracing and observability settings
* Agent composition (which agents are active)
* Model selection per agent and for the Orchestrator

This allows rapid iteration and adaptation without major code changes.

Technology stack

* Built in Python using LangChain and LangGraph.
* Runs efficiently even on a standard laptop (low computational overhead).
* Integrates with LLMs via Microsoft Azure AI Foundry.
* Currently uses models such as GPT-5.2 and GPT-5.4 for optimal speed/accuracy trade-offs, with lighter alternatives available

## **Testing & Validation**

**Real data testing - Tested with actual production-like data (minimum 10% of expected production volume). What data did you test with:**

Currently testing for POC. We run a benchmark dataset which contains 400 questions covering all agents & tools. Below are the results of our benchmark.

**Agent Selection** – The accuracy (%) of the Orchestrator choosing the “right” agent for the user’s request. The “right” agent is the one that is connected to the APIs and is able to answer the user’s query.

**Tools Selection** – The accuracy (%) of an agent in choosing the appropriate tool to use for the user's query.

**Guardrails Passing** – Reflects the percentage of benchmark questions that pass the guardrails – All benchmark questions should pass.

![](data:image/png;base64...)

Legend explanation:

BM1 = Benchmark 1

BM2 = Benchmark 2 (newer version)

REPEAT = experiment repeat.

**Consistent results - Works reliably when you run it multiple times:**

Yes.

**Improvement demonstrated - Clear before/after comparison showing it's actually better:**

N/A

**Quality validation - defining a benchmark:**

*Demonstrate a measurable improvement of [X]% or a quantifiable reduction of [Y] in*

*[specific metric] compared to the [current process/system/baseline].*

N/A

**Validation will be achieved by:**

*briefly describe validation method, e.g., A/B testing, controlled experiment, stress test with defined parameters*

Validation will be done using the benchmark defined above.

## ***\* For certain research, production-ready data may not yet be available for testing. In such instances, we will prioritize business needs over test validation. We can revisit testing validation once the data becomes accessible.***

## **Platform Impact**

**Performance impact - Does this make things faster or slower:**

**Will this reduce or increase false alarms?** Reduce / Increase / No change / Don't know / Not-relevant (circle one)

**Will this miss more real threats?** Yes / No / Same as before / Don't know / Not-relevant (circle one)

**Overall system impact:** Makes things better / Makes things worse / No major change / Unknown (circle one)

## **Architecture & Implementation**

## Complete this section following a meeting with the Architecture Guild

**Scalability validated - Can handle production data volumes and load:**

**Architecture changes identified - What systems/components need changes:**

**Dependencies mapped - All external dependencies identified (IDM, schema changes, infrastructure, APIs, etc.):**

**Major architectural risks assessed - Identified potential failure points and mitigation strategies:**

**Can this scale to production data volume? Yes, tested at scale / Yes, but needs infrastructure changes / No, scaling issues identified / Unknown**

## **Business Value**

**Solves real business problem - This fixes something that actually matters:**

**Improves user experience - Makes life better for analysts, customers, or executives:**

## **Quality & Safety Checks**

**Code/approach reviewed - Other engineers looked at your work:**

**Edge cases handled - Tested weird scenarios and failure conditions:**

**Works across different situations - Tested on different types of data/customers:**

**Reliable performance - Consistent results across different conditions:**

**Can undo changes - Clear way to turn it off if problems happen:**

## **Decision Matrix**

### **Minimum Requirements to Proceed:**

* All 3 Project Definition items answered clearly
* ALL 4 Testing Requirements completed (if production data or equivalent is available)
* ALL 4 Technical Implementation items addressed
* At least 1/2 Business Value items demonstrated
* At least 4/6 Quality & Safety items completed
* No major red flags without solutions

### **Red Flags (Need good solutions to proceed):**

**Does the success justify the architectural risk** ? Yes / No

* Number of new detection? number of customers that will see the new feature? Number of customers waiting for this feature? Passed architect guild review?

**Creates more false alarms?** Yes / No

**Makes system noticeably slower?** Yes / No

**High risk with no backup plan?** Yes / No

**Doesn't solve a real problem?** Yes / No

**Major system changes with no rollback?** Yes / No

## **Final Decision**

**Requirements Met:** \_\_\_/5 categories (4 if not production data)

**Red Flags:** \_\_\_/5 present

**Decision:**

**GO / NO GO** (circle one)

**Approved by:** \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ **Date:** \_\_\_\_\_\_\_\_\_\_\_\_\_

**Notes:**

* This form works for security tools, detection improvements, automation projects, etc.
* Focus is on "does it actually work?"
* Must be tested with real data, not just demos or examples (\*if possible)
