# IRCA - Gate 1 - Research Impact & Feasibility.docx

IRCA

# **Gate 1 - Research Impact & Feasibility**

## **Project Information**

**Project Name:** IRCA- Incident Response Compromise Assessment

**Innovation Lead:** Inbar Dekel, Aviad Cohen, Guy Michaela Kassorla

**Date:** 20/04/2026

## **Project Definition & Approach**

**Clear problem statement - What specific problem are you solving?**

Incident response (IR) in EDR environments is manual, slow, and inconsistent. Human analysts spend significant time pivoting between Cybereason, writing up incident narratives, mapping activity to MITRE ATT&CK, producing customer-facing reports, and executing remediation actions one-by-one via the UI or API. This introduces a mean-time-to-repair (MTTR) delays, human error, and inconsistent report quality across analysts.

We developed an automated Incident Response and Compromise Assessment end-to-end flow. Data collection from Cybereason, AI-driven threat analysis, professional PDF report generation, and agent-driven remediation execution — so analysts can respond to incidents in several minutes rather than hours/days.

**Previous attempts - Have there been previous attempts to solve this problem? What happened to them?** (Research what's been tried before, learn from past failures, justify why your approach will be different, avoid known pitfalls)

**NO**

**Success criteria - How will you know if it worked?**

The generated PDF report contains all the raw relevant information of what happened in the environment, with correct analysis of how the different malops are related to each other, with a correct decision whether the behaviour is malicious or not.

**Approach - How are you building this?**

Four-stage pipeline (Python 3.11, Streamlit UI, LangGraph agent):

1. **Data Collection** — data\_collector.py pulls malops, detection events, and process details from Cybereason REST APIs (/rest/detection/inbox, /detection/details, /crimes/unified, /visualsearch/query/simple); json\_arranger.py normalizes into a structured incident object.
2. **AI Analysis** — prompt\_builder.py + Azure OpenAI (GPT-5) produces threat assessment, chronological narrative, and MITRE ATT&CK mapping grounded in the collected JSON.
3. **Report Generation** — report\_generator\_figma.py renders a branded PDF (ReportLab).
4. **Remediation** — LangGraph agent (agent.py) parses the LLM's remediation recommendations into a whitelisted action set (KILL\_PROCESS, QUARANTINE\_FILE, DELETE\_REGISTRY\_KEY, ISOLATE\_MACHINE, UNQUARANTINE\_FILE) and executes via Cybereason API after analyst approval. Two UIs: streamlit\_ui\_poc.py (demo, fallback data, content-filter-safe) and streamlit\_ui.py (live ops).

## **Testing & Validation**

**Real data testing - Tested with actual production-like data (minimum 10% of expected production volume). What data did you test with:**

We raised a dedicated environment, installed with the latest sensor, on which we execute a real attack scenario, dry-run for MITRE Exam.

* [Dry-run details](https://docs.google.com/spreadsheets/d/1wttP-mKxOQrUgncHyYqChmu0OaGUNFjekwXhcCBW0nE/edit?gid=378148433#gid=378148433)
* [Generated IRCA Report](https://drive.google.com/file/d/1Li4Z_CkKqcsN7XdjvMa2T5O7I00_G7Tp/view?usp=drive_link)

**Consistent results - Works reliably when you run it multiple times:**

Since AI models are not deterministic, the results may not be fully the same when we run the process multiple times. However, from our experimentation the results are consistent.

**Improvement demonstrated - Clear before/after comparison showing it's actually better:**

Yes

**Quality validation - defining a benchmark:**

*Demonstrate a measurable improvement of [X]% or a quantifiable reduction of [Y] in*

*[specific metric] compared to the [current process/system/baseline].*

N/A

**Validation will be achieved by:**

*Briefly describe the validation method, e.g., A/B testing, controlled experiment, stress test with defined parameters*

N/A

## **\* For certain research, production-ready data may not yet be available for testing. In such instances, we will prioritize business needs over test validation. We can revisit testing validation once the data becomes accessible.**

## **Platform Impact**

**Performance impact - Does this make things faster or slower:**

The goal is to allow analysts to respond to incidents in minutes rather than hours.

**Will this reduce or increase false alarms?** Not-Relevant / Reduce / Increase / No change / Don't know (circle one)

**Will this miss more real threats?** Yes / No / Same as before / Don't know (circle one)

**Overall system impact:** Makes things better / Makes things worse / No major change / Unknown (circle one)

## **Architecture & Implementation**

## *Complete this section following a meeting with the Architecture Guild*

**Scalability validated - Can handle production data volumes and load:**

**Architecture changes identified - What systems/components need changes:**

**Dependencies mapped - All external dependencies identified (IDM, schema changes, infrastructure, APIs, etc.):**

**Major architectural risks assessed - Identified potential failure points and mitigation strategies:**

**Can this scale to production data volume? Yes, tested at scale / Yes, but needs infrastructure changes / No, scaling issues identified / Unknown**

## **Business Value**

**Solves real business problem - This fixes something that actually matters:**

**Human IR teams take hours to days** to investigate, triage, and produce a customer-ready response.

**SOC ticketing queues delay investigation start times.** A critical malop can sit in a queue behind lower-severity tickets until an analyst is free. The detection exists; the response doesn't start.

**Improves user experience - Makes life better for analysts, customers, or executives:**

Makes life better for analysts.

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
