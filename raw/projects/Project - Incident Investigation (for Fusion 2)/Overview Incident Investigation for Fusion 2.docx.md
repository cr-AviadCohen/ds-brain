# Overview Incident Investigation for Fusion 2.docx

Overview

## **Overview**

The thread discusses a **potential integration between Fusion 2 and multiple AI-driven security analysis components**, with the goal of enhancing analyst workflows through **automated enrichment, correlation, and reasoning**.

## **1. Proposed Fusion 2 Workflow**

Atchuta proposed positioning **Fusion 2 as the central analyst platform**, where:

* Alerts originate from **external EDR/SIEM systems** (e.g., Defender, Cortex)
* Fusion 2 ingests **high-fidelity alerts (incidents)**
* An **AI-driven pre-analysis phase** occurs before analyst review

### **AI Pre-Analysis Goals**

* Suggest **false positive resolutions**
* Recommend **next response actions**
* Provide **supporting evidence and detailed reports**

### **6-Step Flow**

1. Alert ingestion into Fusion 2
2. Fetch incident details via vendor APIs
3. Enrichment (IOCs, threat intel, historical data)
4. Automated AI analysis
5. AI-generated initial verdict
6. Analyst review and final decision

## **2. AI Capabilities Presented (Platform-Agnostic)**

The Cybereason/LevelBlue team introduced several AI projects designed to integrate into this flow:

* **IRCA (Incident Response Compromise Assessment)** – automated incident analysis
* **AI-DRA** – deep AI analysis for scripts and PE files with detailed reporting
* **AI Assistance** – multi-agent AI assistant for analysts (API actions, navigation, threat intel, etc.)
* **RCE-NG (Risk Chain Engine – Next Gen)** –
  + Correlates alerts/events
  + Performs enrichment, reasoning, and triage
  + Enables **multi-vendor incident unification**

## **3. Correlation & Multi-Vendor Vision**

* RCE-NG enables **combining alerts from multiple vendors into a single incident**
* Based on:
  + Shared identities
  + Time windows
  + AI reasoning

## **4. Data & Enrichment Challenges**

* A major gap identified:
  + **Missing entities and IOCs** in vendor alerts (e.g., Sentinel, Defender, Cortex)
* Without this data:
  + AI analysis quality and verdict accuracy are significantly limited
* **Historical context (past incidents, analyst notes)** is critical for correct classification
* Enrichment must aggregate:
  + Threat intelligence
  + IOC context
  + Historical case data

## **5. APIs & Data Access**

* APIs are available for:
  + Retrieving **alerts and incidents filtered by identity and timeframe**
* Need for:
  + Structured schemas (**Incident, Alert, Evidence**)
  + Additional APIs to support **AI enrichment and analysis**

## **6. AI Output (AI Notes)**

The AI system (RCENG) will produce structured outputs stored in Fusion 2:

* **Confidence score**
* **Verdict** (TP / FP / benign / unknown / needs review)
* **Reasoning / explanation**

## **7. Analyst Feedback Loop**

* Analysts will:
  + Review AI outputs
  + Provide feedback via API
* Feedback will:
  + Improve filtering (e.g., Known TPs / FPs)
* Requirement:
  + At least **one human validation step** before feedback is applied

## **8. Integration Approach**

* AI components are designed to be **platform-agnostic**
* Integration points:
  + Before analyst review (pre-analysis)
  + As part of enrichment/analysis pipeline
  + Feeding results into **Fusion 2 case management**

## **9. Open Questions / Next Steps**

* Define:
  + Feedback API design
  + Data schemas (Sunrize DB)
  + AI Notes structure in detail
* Validate:
  + Data availability from vendors
  + Enrichment completeness
* Continue:
  + Architecture design for RCE-NG integration
  + Joint discussions and technical deep dives

## **Bottom Line**

The collaboration aims to build a system where:

* Alerts from multiple vendors are **enriched, correlated, and analyzed by AI**
* AI provides **explainable verdicts and recommendations**
* Analysts remain **in the loop for validation**
* The system **continuously improves via feedback**
* Fusion 2 becomes a **central AI-augmented investigation hub**

important emails

Atchuta:

Hello Or,

Thank you again for the introduction. I would like to propose a workflow for Fusion2 and the analyst investigation process and gather your thoughts on potential integration points.

In this model, raw events and logs remain ingested and stored within third-party EDR/SIEM platforms (like how USM and Phoenix operate alongside ecosystems such as Microsoft or Cortex). High-fidelity alerts (incidents) are generated within those systems and then pulled to Fusion2 for analyst review and investigation.

We are proposing the introduction of an AI-driven pre-analysis (or enrichment) phase before the analyst begins working the alert. This AI activity could be positioned either immediately after the alert is generated or once it reaches Fusion2, but prior to analyst engagement. The objective would be to:

* Suggest resolution if the alert is determined to be a false positive
* Recommend response actions or next steps for the analyst
* Provide supporting evidence and a report to substantiate the findings

The analyst would then review the AI’s recommendations, provide feedback, and proceed with any required follow-up actions, leveraging the generated report as supporting evidence.

Our vision is to position Fusion2 as the operational hub for analysts handling high-fidelity alerts from third-party EDR/SIEM platforms, enhanced through automated enrichment wherever possible. We are also considering implementing playbooks to enable integrations across LevelBlue offerings, creating a cohesive ecosystem that streamlines and strengthens the investigation workflow.

We would appreciate your feedback on this proposed flow and look forward to a call to discuss potential integration approaches between Fusion2 and the AI analysis capabilities you are building.

Looking forward to your thoughts.

Best regards,
-Atchuta

Pawel:

Hi Atchuta,

I'm seeing a major problem here: lack of Entities and IOCs, especially in MS and Cortex alerts. As mentioned in the last Indigo Kinetic meeting, alerts won't be pre-enriched and would require manual action.
We can't produce accurate AI analysis and verdicts without that data, meaning we'd have to exclude EDR/SIEM products like Sentinel, Defender, and Cortex!

Another mandatory requirement for accurate verdicts is historical context from similar incidents (analyst notes). This is critical because some suspicious activities may be a standard within a customer's environment.

Our analysts currently look for similar cases in ServiceNow (where we store incident tickets) to make that determination.

By the way, I attached output from our Hunter agent. This isn't a production-ready solution like IRCA, but it validates the concept of using Claude with MCP tools and produces very good results. OpenWebUI provides an API interface, and we're leveraging this in our research tools.

Atchuta:

Pawel,

Just so we are clear, we are both in agreement about the need to collect the information about the incident. I think there are total of six steps involved in the process of taking an incident from an EDR/SIEM vendor and taking it to final verdict by analyst. I will list the six steps we have; I believe steps 3-6 must be implemented as the “Automated analysis phase".

1. Ingestion of the high-fidelity alert/incident. The incident arrives at F2.
2. Incident detail is fetched by F2 from the vendor using the vendor’s APIs. Note the purpose of this is not to do any correlation in F2. The correlation is expected to be done external to F2.
3. Enrichment of the incident: The intent here is to collect enough information from the intel data store about the IOCs, correlate that with the past enrichment events that have occurred.
4. Automated analysis : The analysis to be performed using the AI projects at LevelBlue, to create a report that includes information to allow analyst to make an informed decision on the next steps.
5. Initial verdict by the automation: This information will be included in the report.
6. Report is sent back to F2 for human review and final verdict by an analyst review.

What you are referring to here is the data that is collected during enrichment phase is very specific to the needs of analysis and report generation. Also, as you mentioned, there is correlation involved in the analysis. The incident detail collected from the vendor APIs by F2 depends on the available APIs from the vendor.

Here is a high-level data-flow diagram. Also attached is the vendor API comparison on what is available from Vendor for the ‘incident\_detail'. We can discuss this further during our call that setup by Or.

Looking forward to a productive conversation.

![](data:image/png;base64...)
