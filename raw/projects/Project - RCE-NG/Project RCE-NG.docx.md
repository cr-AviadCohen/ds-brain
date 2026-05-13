# Project RCE-NG.docx

🏁 Main

**Project
Risk Chain Engine (RCE)
Next Generation (NG)**

#

# General

* **Description:** An engine that correlates different detection events, on XDR, to an attack narrative, with a detailed explanation, using an LLM (gpt4o).
* **Owner:** Guy Michaela Kassorla
* **Architecture:**
  + [Link - Google Drive](https://drive.google.com/file/d/1oJxYJ_DmGNJRF5ANj9RRFD_ZDjaixNP9/view?ts=684fc634)
  + [Link - Draw.io](https://app.diagrams.net/?splash=0#G1oJxYJ_DmGNJRF5ANj9RRFD_ZDjaixNP9)
* **Code:**
  + Git: [Link](https://github.com/cybereason-labs/data-science/tree/rce-ng)
  + Machine: [Link](https://2129e71d4136f401-dot-us-east1.notebooks.googleusercontent.com/lab/workspaces/auto-5/tree/data-science/rce_ng)
* [#Slack Channel](https://cybereason.enterprise.slack.com/archives/C085R5DLTEZ)
* [RCE-NG POC](https://docs.google.com/presentation/d/1DK7gAM5xadzWaR-ULIWH9_S99w8naPizid6xz7lupCk/edit?slide=id.g3679849e085_0_1485#slide=id.g3679849e085_0_1485)
* [Pheonix Schema](https://docs.google.com/spreadsheets/d/1ZQgFI4DuSyGY52Bqwmuw4NHOhSBjHkcGJEjwVL5l-7U/edit?gid=197763723#gid=197763723)
* [RCE-NG for Phoenix: Questions](https://docs.google.com/document/d/10rlcJKaocte7uMkl6_ownHOlY_6XhTWBrzpnzlVzqmU/edit?tab=t.0)
* [NotebookLM](https://notebooklm.google.com/notebook/cf757d70-2692-4b3c-a928-60d24b38560a)
* [Documentation of the current RCE](https://cybereason.atlassian.net/wiki/spaces/XDR/pages/3806004172/Risk%2BChain%2BEngine%2BRCE)

# Tasks

* Convert prompt for LLM to COSTAR style

# Next Phase

* **Phoenix adjustments mapping** (Aviad Cohen, Guy Michaela Kassorla)
  + Meet with Ortal Keizman and Tonny Pham and Boaz Yaniv (new architecture) and to

share knowledge regarding the current RCE-NG architecture. Understand what isn’t aligned with the phoenix data structure and pipeline (RCE-NG suggested architecture was developed in consideration of the existing XDR, and will require modifications to be compatible with the Phoenix solution).

* **Evaluate Costs** (Aviad Cohen, Guy Michaela Kassorla)

To complete the POC, we still need to perform a comprehensive cost evaluation for the proposed solution. This assessment should take into account:

* [Costs Evaluation Fields](https://docs.google.com/spreadsheets/d/1jlN8lRaPqIwrKLs0ZBQMnA89dsad55VQqSnFucaMRRM/edit?gid=0#gid=0)
* [ccbji1 customer data](https://2129e71d4136f401-dot-us-east1.notebooks.googleusercontent.com/lab/tree/data-science/rce_ng/correlat%5B%E2%80%A6%5Dcustomer_ccbji1_enrich_output_file.txt)
* Field to extract for each customer:
  + Total number of events per month.
  + Total number of detections per month.
  + Total number of integrations (vendors) and which (e.g., Office365, AzureAD, …)
* More questions:
  + Cost in terms of money? LLM queries? Database/transactions costs??
  + Estimated number of correlations per month????
  + What is the average size of a Potential Correlation Groups????
  + How many queries to LLM in phase #3?
  + Maximal input tokens limit to LLM (depends on LLM).
* Leverage all available data (from Observe) to estimate the average volume of events passing through each stage of the architecture.
  Using these averages — broken down by customer type — and estimating the cost of handling each event across our pipeline, we can then project the total annual cost of the full solution.
* **Phoenix adjustments** (Guy Michaela Kassorla)
  + Adjust the RCE-NG architecture to comply with Phoenix instead of the current XDR EDR.
  + Map the changes that have to be made in the correlation engine (step #3) as an outcome of the note above.
* **Malop Worthy ML solution research** (Guy Kapach with the help of Guy Michaela Kassorla)
  + Work on the features (fields) we are sure we want to test for the “Malop Worthy” ML solution.
  + Start by taking (from the new schema) the data fields that we are already using as a part of the current Malop Worty rules: [Pheonix Schema](https://docs.google.com/spreadsheets/d/1ZQgFI4DuSyGY52Bqwmuw4NHOhSBjHkcGJEjwVL5l-7U/edit?gid=278788667#gid=278788667)
  + Meet with a security specialist to discuss additional data fields (or combinations of them) that may be essential features.
* **Using data flowing from Phoenix to train the model** (Guy Kapachwith the help of Guy Michaela Kassorla)

When Phoenix starts running in customers' environments, we’d like to consume the data that begins to flow and use it to start the training and continue the research process.

# Open Questions – RCE-NG

Guy Michaela Kassorla, Guy Kapach, Aviad Cohen

Inbar Dekel:

* After our meeting regarding RCE-NG, I gathered some open questions for Or Golov to answer.
* Please review his answers (in red) and come prepared to the meeting we have on Thursday with the questions we still want to ask.
* You guys also need to come prepared to explain and answer questions regarding the current [architecture](https://app.diagrams.net/?splash=0#G1oJxYJ_DmGNJRF5ANj9RRFD_ZDjaixNP9), as this is also an important aspect of the meeting.

Questions:

* Are we focusing solely on Phoenix, or also the old XDR? Phoenix
* What assumptions did we make in the current RCE-NG that will no longer be valid for the Phoenix RCE-NG version?
  + What is going to be the input to stage 3? Still detections only? What scheme will be used there? Detections only, Phoenix scheme
  + What is going to be the output from stage 3? Should we follow the phoenix scheme they call ‘detection scheme’? Yes
  + Will we have data like evidence/suspicion? Will we know the MITRE tag as today from DROOL/ACE? Yes, this is our requirement
  + In the meeting on Monday, if I understood correctly, Tal Stavi said something about us not getting detections only, but also benign data? Did I understand correctly? If so, why is that? Phoenix is also ingesting benign data, we will not want to consume it into RCE to reduce cost, as well as for better accuracy.
    - Is it because there will be no distinction, in this stage, between detections / benign events? I don’t know, let’s ask them how they intend to supply it to RCE
    - Is it because they want benign events to take part in the correlations to begin with? (and not only in stage 5 enrichment?) Hopefully, they will be able to separate this for us or find a better solution

# Open Questions – Malop-Worthy:

* The ‘tags’ we currently have for “Malop Worthy” stage (triage of the current RCE), are not good enough for the learning process itself, for a few reasons:
  + The triage is being made only for correlations that passed the Malop Worthy logic (so a big part of the data is left untagged)
  + The scheme is different, meaning extra unnecessary work.

The current plan is to wait for real data to start flowing in Phoenix, and then use:

* The data that passed “Malop worthy” from the triage that will be made as a part of the RCE-NG flow.
* The data that didn’t pass “Malop worthy” tag in a more creative way:
* manually by analysts (limited capacity)
* using an LLM
* Guy and Guy had a meeting with Simeon Tsatskin that shared with them how the current (EDR) scheme looks like.

He told them that what is called in the new scheme “detection” (in Phoenix they no longer want to use the term MalOp) is already a correlation of events.

Should the output of RCE-NG be meeting the ‘phoenix detection’ scheme? I think I have already answered it, yes, but for a malop or something like that. We need to ask engineering how they view this entity in the Phoenix scheme.

If so, then the input of the “Malop Worthy” stage is what they call “detection” in the Phoenix (correlation of events that RCE-NG creates)? We need to check with engineering.

* Who (except for Ortal and Tony) can answer questions regarding the Poenix version of XDR? Tal Stavi

🤝 Meetings

**Meetings**

# Meeting: 2025.07.17 – RCE-NG Architectuer

* [RCE-NG for Phoenix - Questions](https://docs.google.com/document/u/0/d/10rlcJKaocte7uMkl6_ownHOlY_6XhTWBrzpnzlVzqmU/edit)

The meeting served as an explanation of the **RCE-NG (Next Generation Correlation Engine)** architecture to a team from Japan, Ortal, and Tony, an architect for Phoenix XDR. The RCE-NG aims to replace the problematic existing RCE engine by providing a more robust solution for correlating security alerts. Its ultimate goal is to **connect security alerts from various vendors (XDR) and correlate them into a single, comprehensive attack story, or "malop"**.

The RCE-NG architecture is structured into five main stages:

1. **Normalization and Enrichment**:
   * **Unified Data Model (UDM)**: This initial step standardizes the format and fields of event data coming from diverse security products (e.g., Palo Alto, GCP, Microsoft 365, Azure) into a unified schema.
   * **Identity Management (IDM)**: Events are enriched with missing identity information (such as linking a username to an email or IP address). Guy Michaela Kassorla developed a limited, simulated IDM for the Proof of Concept (POC), as this capability was present in Chronicle but is missing in the current Observe platform and needs to be developed for Phoenix.
   * **Concerns**:
     + Tonny Pham highlighted that IDM is a **crucial prerequisite** for the correlation engine to function effectively, and basing a solution on a component that doesn't yet fully exist or is undefined for Phoenix is a significant blocker.
2. **Detection**:
   * Only detection events proceed to this stage.
   * Events are tagged with **MITRE ATT&CK tactics and techniques (TTPs)** and assigned a severity level.
   * This stage uses **static rules (Opal Monitoring/DROOL)**.
   * **Concerns**:
     + Tonny Pham again questioned the accuracy and implementation of these detection rules within the evolving Phoenix schema, noting a lack of detailed understanding of their current operation.
3. **Correlation Logic**:
   * This stage introduces a new approach to correlation, moving away from static, manually written rules.
   * A new event triggers the process and is inserted into an **event database**. This database operates on a **sliding window (e.g., 24 hours in the POC)** to manage the massive volume of data.
   * The system then searches for other events within this window that share a **mutual identity** with the new event, forming **potential correlation groups**.
   * These groups pass through **filtering gates** to ensure quality and reduce costs. Filters include eliminating **known false positives** (based on feedback from past human triage) and applying **additional rules** like event aggregation for high-volume vendors.
   * If a potential group is not filtered out, it is sent to a **Large Language Model (LLM), specifically GPT-4O in the POC**. The LLM then determines if these events truly form a logical correlation and generates a **detailed narrative explanation** of the attack sequence.
   * **Concerns**:
     + Tonny Pham expressed **significant doubts about the scalability of the current correlation approach**, describing it as a "naive flooding algorithm." He suggested exploring more optimized methods like **graph clustering, density-based algorithms, or embedding events into vectors** for efficient similarity calculations, especially given the scale of data (32 billion events daily).
4. **Malop-Worthy Decision Gate**:
   * This stage determines if a correlated group of events is severe enough to be designated a "malop" and sent as an alert to the customer.
   * The **current POC uses a simple, rule-based logic inherited from the existing RCE**.
   * **Future plans** involve developing a more **robust machine learning approach** to make this decision, potentially incorporating a meaningful score or tags generated by the LLM.
   * **Challenges**:
     + The current malop-worthy uses static rules and it is insufficient, and implementing a sophisticated ML model is difficult due to the varied structure of event data and the challenges in consistent feature extraction.
5. **Malop Enrichment**:
   * This is a **new capability** not present in the current RCE solution.
   * For events that are successfully identified as malops, the system provides **additional context and data to analysts** to facilitate their investigation and triage.
   * Enrichment includes: **IOC (Indicators of Compromise) enrichment** (e.g., providing reputation verdicts from external sources like VirusTotal for suspicious files or IPs) and adding **raw, non-detection events** related by shared entities within a short timeframe (e.g., 5 minutes before or after the malop).
   * **Benefit**: This significantly **reduces the manual work for analysts**, saving time and improving the quality of their incident response.

**POC Details and Goals:** The POC used **24 hours of real customer data from Japan**, processed in a bulk manner rather than a real-time stream. The primary goals of the POC were to demonstrate:

* The system's ability to correlate a specific "Hagiwara" attack scenario that the current RCE could not detect without custom rules.
* Showcase **cross-vendor activity** (e.g., Office 365, Azure AD, Cato, Box) and **multi-step attack progression** within a single narrative.
* The LLM's capacity to provide **detailed, clear narrative explanations** for correlated events.
* The new capability of identifying and including **related non-detection events** to provide a more complete picture. The demo scenario simulated a multi-stage attack involving a phishing email, suspicious login attempts, malware download, and data exfiltration.

**Open Questions and Next Steps:** The discussion highlighted several critical points that require further clarification and action:

* **Clarification of IDM and Detection Rules**: A deeper understanding of IDM requirements and implementation, as well as the functionality of detection rules (Opal Monitoring/DROOL) within the Phoenix schema, is crucial before proceeding.
* **Correlation Algorithm Scalability**: Research and propose more optimized correlation algorithms to address Tony's concerns about the current approach's efficiency at scale.
* [**Cost Evaluation Spread Sheet**](https://docs.google.com/spreadsheets/d/1jlN8lRaPqIwrKLs0ZBQMnA89dsad55VQqSnFucaMRRM/edit?gid=0#gid=0)
* **Phoenix Alignment**: The RCE-NG architecture must be adjusted to ensure full compatibility with the evolving Phoenix data structure and pipeline.

# Meeting: 2025.06.26 – RCE-NG Architectuere

* First meeting on architecture. We only present the architecture, didn’t have time for questions.

# Meeting: 2025.06.18

Recordings: [GDrive](https://drive.google.com/drive/folders/1eJFUfwJ9UqgCrmLf1oQmaFETIfq40Kw4?usp=drive_link)

Summary: [NotebookLM](https://notebooklm.google.com/notebook/25498207-575a-43aa-9a4e-93348ed09fa5)

**Summary**

Here is a comprehensive and coherent summary of the meeting, presented in English:

The meeting focused on understanding existing workflows and coordinating the progress of the Phoenix project, specifically concerning the Correlation Engine (RCNG) and Malop-Ready, against its new requirements.

### **1. Existing Data Flow and Schemas**

Currently, two main data schemas are in use: **Events** and **Detections**.

* **Events**: These are essentially raw logs sourced from EDR sensors. They pass through RedPandas, where they may or may not receive a detection, and are then sent to ClickHouse, which functions as a data lake containing all events and detections. These events undergo processing into a specific schema and are not necessarily detections; they can also be intermediate events. Currently, this data originates solely from EDR, without broader integration from other vendors like XDR.
* **Detections**: These can result from correlating multiple events or be a single event, and they adhere to a different schema than events. As of now, the **rules for detections are exclusively written within the sensor** and not in RedPandas. The term "Malop" (Malicious Operation) is considered the "old approach" and has been replaced by "Detection," which describes "a collection of several suspicious events".

### **2. Phoenix Project and the Correlation Engine (RCNG)**

**Phoenix is a new project**, and the correlation component will be the first to be built for it.

* **Key Stakeholders**: Ortal, the engineering team lead in Japan, and Tony, Phoenix's architect, are the primary contacts for this development.
* **RCNG's Role**: The team's responsibility is twofold:
  + Explain the RCNG architecture to Ortal and Tony
  + Precisely understand their input requirements and definitions for Phoenix.
* **Expected Changes to RCNG Input**:
  + Previously, RCNG was expected to receive only detections (UDM IDM) that had already been tagged with MITRE ATT&CK techniques and processed through Drule and ACE.
  + **The most significant change is that RCNG will now receive *all* events, irrespective of whether they are detections or not**. This shift is expected to **substantially increase the volume of data** processed. The underlying understanding is that such solutions should process every incoming event without any preliminary distinction between intermediate or malicious events.
  + It needs to be clarified whether the existing Drule rules are still relevant or if Drule will be entirely bypassed.
* **Project Approval**: The Phoenix project has been approved, and development tasks are slated to commence as part of the next quarter's development missions. The objective is to adapt the existing solution rather than starting from scratch.
* **RCNG Output**: The output of RCNG will be "Correlations," which will serve as input for Guy's Machine Learning (ML) models. Ideally, these correlations should be composed *only* of detections.

### **3. Challenges and Unclear Points**

Several challenges and ambiguities were identified during the discussion:

* **Massive Data Volume and Filtering**: Receiving all events implies handling enormous data volumes. A strategy is needed to perform logical and efficient filtering without aggregating every incoming event, as this would be unfeasible.
* **Distinguishing Between Event Types**: There is a lack of clarity on how Phoenix will differentiate between "intermediate" events and "malicious" events or detections, particularly regarding data storage and filtering practices.
* **"Alert" vs "Detection Event"**: Semion mentioned specific fields like "severity" and "confidence" that are relevant only to "Alert" and "Detection Event." The distinction between these two terms needs to be clarified.
* **XDR Input**: Semion was unable to provide a deep explanation of the input and output structure for XDR. While sensor rules will persist, it will be possible to add logic within RedPandas.
* **Transition to the New Schema**:
  + Phoenix's new schema for detections includes crucial fields such as involved\_ips (a list of involved IP addresses).
  + The new schema appears to be an improvement over the older, more "cluttered" schema which contained redundancies.
  + A key point of discussion is whether to work with simulated data based on the new schema (Guy's preference) or attempt to convert existing old data with current tags to the new schema.
* **Data Labeling (True Positive/False Positive - TP/FP)**:
  + Current TP/FP labels were generated by analysts based on "Malop" occurrences.
  + These labels primarily reflect whether an event was "interesting enough" rather than the accuracy of the correlation itself.
  + **The Problem with Existing Labels**:
    - They are filtered: only events that passed the current "Malop-Ready" process were labeled.
    - They are not considered sufficiently robust for long-term use.
  + A creative and new method for acquiring high-quality labels is necessary if the existing ones prove insufficient (e.g., manual labeling by analysts or advanced ML techniques).

### **4. Next Steps**

**For Guy (Immediate Work)**:

* **Focus on the New Schema**: Guy Kapach should begin working with Phoenix's new detection schema.
* **Feature Identification**:
  + Guy should extract features from the 11 existing Malop-Ready rules that are also present in the new schema, as these are considered definite and important features.
  + He should create simulated data based on the new schema and start building the pipeline for extracting features from this simulated data.
  + Guy should consult with security researchers (such as Semion) to identify additional relevant fields within the new schema that could contribute to determining if something is "Malop-Ready".
  + **Guy's work should operate at the "Malop" level** (i.e., groups of correlated events) rather than at the individual event level.

**Future Meetings and Actions**:

* **Clarification with** **Or Golov**: The meeting participant will confirm with Or (likely Or Friedman) what the input for RCNG will be and whether they will exclusively support Phoenix moving forward.
* **Scheduling a Meeting with Ortal and Tony**: This meeting will serve to:
  + Understand the changes in assumptions regarding RCNG's input.
  + Present the RCNG architecture.
  + Discuss how to adapt the existing solution to meet Phoenix's requirements.
  + Define technical specifications and filtering details.
  + Confirm whether "Detection event" in Phoenix is indeed the desired output for RCNG.
  + Address the issue of existing data labeling and explore alternative methods for obtaining better labels.
* **Private Message to Semion**: Guy will send a private message to Semion to inquire about the difference between "Alert" and "Detection event" and to request simulated data for analysis.
* **Ongoing Collaboration**: The team will continue to collaborate on defining relevant features, incorporating input from security experts.

In summary, the project is moving forward, and the primary goal is to adapt existing solutions to meet Phoenix's new requirements. This involves addressing significant challenges related to data volume, new schemas, and data labeling issues.

✅ Tasks

**Tasks**

* Task 1
* Task 2
