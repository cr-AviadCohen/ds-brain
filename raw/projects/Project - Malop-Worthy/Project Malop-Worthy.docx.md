# Project Malop-Worthy.docx

🏁 Main

**Project
Malop-Worthy**

#

# General

* **Description:** Malop-Worthy is a module in the [RCE-NG](https://docs.google.com/document/d/1Z6osMAwGlfqZmrxmxknzRF6uhVXFjCH1Ebi7KBecJ9M/edit?tab=t.l2bxajtc8qht) pipeline, which classifies a given correlation as interesting and malicious enough to become a Malop, or not.
* **Owner:** Guy Kapach
* **Code:**
  + [~~https://github.com/cybereason-labs/research\_notebooks/tree/malop\_gateway~~](https://github.com/cybereason-labs/research_notebooks/tree/malop_gateway)
  + <https://github.com/cybereason-labs/research_notebooks/tree/malop_decision_guy_3_9_25/malop_worthy>
* **Jira:**
  + [ENG-2098: Malop-Worthy | Innovation POC](https://cybereason.atlassian.net/browse/ENG-2098?atlOrigin=eyJpIjoiMDM1N2FjMmU1ZGYzNDY0Y2I3M2M2OWJiYmU2ZmYyMWIiLCJwIjoiaiJ9)
  + [ENG-3928: Malop Worthy | Improving Classification Results](https://cybereason.atlassian.net/browse/ENG-3928?atlOrigin=eyJpIjoiM2VlODY1NTM0MmQwNDNjYThlMThmZDdjOThlN2M0MmIiLCJwIjoiaiJ9)
* [#Slack Channel](https://cybereason.enterprise.slack.com/archives/C092ZG29L06)
* **XDR:**
  + [XDR Monitoring](https://lookerstudio.google.com/u/0/reporting/e348169e-27c9-4966-861e-db5c20bcccf7/page/T3cWC)
  + [XDR Risk-Chain Engine Monitoring](https://lookerstudio.google.com/u/0/reporting/004a49e9-e5b9-4550-8629-279459e7d125/page/p_d4zy0g13ad)

# Tasks

* Build the entire pipeline from Feature Extraction ⇒ Classification ⇒ Results
* Collect data 1 year ago and run the evaluation pipeline:
  + Evaluation using 10-Fold-Cross-Validation.
  + Provide TPR, FPR, TPR\*TNR.
  + FPR = 15%
* Start working with Cursor for faster implementation.
* Tag Malops using a human analyst.
* Use GenSpark to explore the problem
* Use OpenAI models (gpt o4) to:
  + Classify the given data
  + Suggest new features
* Pull more data for evaluation from GBQ
* ~~Show the ability of our model to remove false positives specifically (ignore the TPR rate)~~
* Meet with Alon Laufer to review malops.
* ~~Set a meeting with~~ ~~Or Golov~~ ~~to show him the results/~~
* **Later:**
  + Using LSTM to refer the data as sequential
* **Results**

# Current Data

* rce\_triage\_result table contains malops, the detection events that formed each malop, and malop classification by a human analyst.
  This table is stored as a single column SQL, which contains all the data as a nested JSON.
  Table created on 19 May, 2023 and has no expiration.
  There are 3 tables for different regions:

| Table ID | Data location |
| --- | --- |
| global-soc-14311f.xdr\_malop\_apac.rce\_triage\_result | asia-northeast1 |
| global-soc-14311f.xdr\_malop\_amer.rce\_triage\_result | US |
| global-soc-14311f.xdr\_malop\_emea.rce\_triage\_result | EU |

* correlation\_output table contains XDR events, this table is partitioned by day and has retention of 365 days.
  There are 4 tables for different regions (for europe there are 2 tables):

| Table ID | Data location |
| --- | --- |
| dc-as-ne1-1-stack-prod-2d.dc\_rce\_dataset.correlation\_output | asia-northeast1 |
| dc-us-e1-1-stack-prod-e3.dc\_rce\_dataset.correlation\_output | us-east1 |
| dc-eu-w1-1-stack-prod-70.dc\_rce\_dataset.correlation\_output | europe-west1 |
| dc-eu-w3-1-stack-prod-be.dc\_rce\_dataset.correlation\_output | europe-west3 |

* Notice that whereas apac tables are located in the same region, US and EU aren’t.

🤝 Meetings

**Meetings**

# 2025.06.18

Recordings: [GDrive](https://drive.google.com/drive/folders/1eJFUfwJ9UqgCrmLf1oQmaFETIfq40Kw4?usp=drive_link)

Summary: [NotebookLM](https://notebooklm.google.com/notebook/25498207-575a-43aa-9a4e-93348ed09fa5)

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

✅ Tasks

**Tasks**

* Task 1
* Task 2

📊 Results

Results

Training set: 3943 samples

Not Malicious: 2714

Malicious: 1229

![](data:image/png;base64...)

![](data:image/png;base64...)

![](data:image/png;base64...)

|  | **Metric** | **Value** |
| --- | --- | --- |
| 0 | Total Samples | 1690 |
| 1 | Total False Positives (FP) | 1163 |
| 2 | Number of FP Cleaned | 820 |
| 3 | % FP Cleaned (of Total Samples) | 49% |
| 4 | % FP Cleaned (of Total FP) | 71% |
| 5 | % TP Ignored (of Total TP) | 7% |

![](data:image/png;base64...)

|  | **Metric** | **Value** |
| --- | --- | --- |
| 0 | Total Samples | 1690 |
| 1 | Total False Positives (FP) | 1163 |
| 2 | Number of FP Cleaned | 1017 |
| 3 | % FP Cleaned (of Total Samples) | 60% |
| 4 | % FP Cleaned (of Total FP) | 87% |
| 5 | % TP Ignored (of Total TP) | 16% |

![](data:image/png;base64...)

|  | **Metric** | **Value** |
| --- | --- | --- |
| 0 | Total Samples | 1690 |
| 1 | Total True Positives (TP) | 527 |
| 2 | Number of TP Marked | 268 |
| 3 | % TP Marked (of Total TP) | 51% |
| 4 | % TP Marked (of Total Marked Samples) | 78% |
| 5 | % FP Marked (of Total Marked Samples) | 22% |
