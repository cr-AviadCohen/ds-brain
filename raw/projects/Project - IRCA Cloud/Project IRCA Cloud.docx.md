# Project IRCA Cloud.docx

**🏁 Main**

Project
IRCA Cloud

# General

* **Description:**
  + Similar to [IRCA project](https://docs.google.com/document/d/1TGQQtkWq0in9PWVcHhaCIT4LHjve2XzpUBGWssQ_R5Q/edit?tab=t.l2bxajtc8qht), for cloud detections, based on our Observe \ XDR.
* **Owner:** Guy Michaela Kassorla
* **Code:** <https://github.com/cybereason-labs/research_notebooks/tree/irca_cloud>
* **Jira:**
  + [ENG-3945: Detection Engineering - (GenAI) Cloud IRCA](https://cybereason.atlassian.net/browse/ENG-3945)
* [**#Slack Channel**](https://cybereason.enterprise.slack.com/archives/C09LF4Y3PND)

# Data

* [Observe APAC](https://131377279880.ap-1.observeinc.com/workspace/41001237/log-explorer?datasetId=41042193&s=501154-uxd4acg4)
* [Observe EU](https://111638659092.eu-1.observeinc.com/workspace/41000004/home)
* [Observe US](https://121530154444.observeinc.com/workspace/41029375/home)

# Tasks

* Create a new project under research-notebook.

**🤝 Meetings**

Meetings

* [NotebookLM](https://notebooklm.google.com/notebook/7e284e5f-7324-4028-be9b-cf40f4d40460)

# 2025.10.26

* Attendees: Eli SalemAviad CohenGuy Michaela KassorlaItamar HershkoChen AvianiAlon LauferDaniel Hay
* [Recordings](https://drive.google.com/drive/u/0/folders/1jE-iV5Gdf_yzKPPE5ecyuhWB1cjAHnLx)

Project goal is to generate a IRCA report, for cloud events.

## Core Challenges and Strategy Shift

* **Unscalable Data Volume:** The current method relies on summarizing massive volumes of complex AWS CloudTrail logs (hundreds of thousands to millions daily). The previous approach of summarizing summaries is not scalable or logical.
* **Need for Filtering:** To handle the scale, the team must shift focus from processing all logs to concentrating only on very specific event names, applying a Pareto-like principle to cover the most likely attack events (80–90%).
* **Need for Focus for POC.**
* **Testing:** No way to generate/inject malicious activity to cloud environment as we did for EDR-IRCA fuwing MITRE Dryrun, there is no dirty env.

## Security Team Responsibilities

* Research raw data logs.
* Research what vendors should we focus in the POC:
  + AWS Cloud Trail
  + Cisco Firewall
  + Microsoft Office 365
  + Microsoft Azure Identity
* Create detections for the relevant events from the selected data sources.
* Truncate the logs from irrelevant data.
* \*\* estimation research time: 1 month
* Figure out how what should be the best format for IR report for cloud.

## Data Science Team Responsibilities

* **UDM:** Data Science team will get the events in Unified Data Model (UDM) format, and can get only the filtered data from a specific Opal filtering.
* **[Optional] Scoring Mechanism:** Data Science will develop a scoring mechanism that will provide each event with a relevancy score. Events with score beyond a certain threshold will be move to the next step. We need to determine if and how
* **IRCA Report Generation Mechanism:**
  + Figure out how to handle huge amounts of data:
    - We May have preprocessing stage, which takes the selected UDM events and prepare them before prompt building.
    - Decide how to arrange the data as prompt for LLM

**Aviad Cohen** **DS comments:**

* We would like to detect anomalies in cloud events.
* Consider the timestamp of events: time series.
  We may train a BERT model on sequence of event names.
* Extract distribution of different events.
* Consider internal vs external events.
* On POC we should focus on specific scenario.
* Build architecture for the solution. Also consult with an architect to build a robust architecture for production.

# [Title]

…

**✅ Tasks**

Tasks

* Task 1
* Task 2
