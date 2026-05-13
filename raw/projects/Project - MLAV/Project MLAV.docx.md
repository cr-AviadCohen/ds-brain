# Project MLAV.docx

🏁 Main

**Project
MLAV**

# General

* **Description:**
  + A malware classifier (LGBM) for PE & DLL files (managed & unmanaged), used by the Cybereason sensor Anti-Virus on client’s endpoint. The classifier leverages features extracted using STool metadata extractor (extracting from the files) + feature engineering (one-hot encoding, etc.).
  + MLAV doesn’t Depend on BitDefender (as NGAV was).
  + MLAV design to detect known hacking tools: it is trained on them, and if it doesn’t classifies them well, add them to Blacklist.
* **Owner:** Guy Kapach
* **Confluence:** [https://cybereason.atlassian.net/wiki/spaces/IN/pages/31668535304/MLAV+automated+model+generator+-+.net+logic+distinction+by+unmanaged+managed](https://cybereason.atlassian.net/wiki/spaces/IN/pages/31668535304/MLAV%2Bautomated%2Bmodel%2Bgenerator%2B-%2B.net%2Blogic%2Bdistinction%2Bby%2Bunmanaged%2Bmanaged)
  It contains the links to the Jenkins job. repositories and everything else, with deep explanation.
* **Jenkins Job:** [https://jenkins-irelease.eng.cybereason.net/view/Data Science/job/mlav-model-generator/](https://jenkins-irelease.eng.cybereason.net/view/Data%20Science/job/mlav-model-generator/)
  + The full pipeline takes ~20 hours.
* **Code:** <https://github.com/cybereason-labs/data-science/tree/mlav_14_5_25/mlav>
* **More details:**
* Questions on Artifactory sensor-local (link from confluence) - Itay Baranes
* Questions on S3 - Ofir Tal
* [NGAV Analysis.docx](https://docs.google.com/document/d/1CGJuBejUmMxm8G9Y22YERCSHeGOhp4_Z/edit)

# NGAV

* NGAV is a Machine Learning-based detection engine that comes as a second layer after BitDefender Anti-Virus. Only If BitDefender has no determined classification (benign/malicious), NGAV acts on it.
* BitDefender provided an accuracy of approximately 85% detecting malicious files.
  From the rest 15% of undetected files that BitDefender detects as benign, there are FN that the NGAV is able to detect as TP, thus raising the overall detection rate significantly.
* NGAV was built to classify PE & DLL files, managed (.NET) & unmanaged.
* NGAV extracts between 125-311 static features from the file, depending on its type.
  + [Features Examples](https://drive.google.com/drive/u/0/folders/1J46UQiFZAfniRjc3RPZGMoUBM-Xp89KU)
  + **Managed & Unmanaged features:** cryptographic identifiers, digital signatures, PE structural metadata, COFF and optional headers, import tables, section characteristics, YARA matches, and extensive pipeline telemetry — all designed to support malware detection, anomaly detection, and behavioral inference.
* NGAV detection model was trained only on files that were tagged as “benign” on BitDefender, divided into Malicious & Benign based on *Broccoli* detection model.
* *Broccoli* is a classification algorithm that learns how to weight the decision of different engines from the VirusTotal report, in order to provide a final decision as Benign/Malicious.
* NGAV detection model (ML) outputs a maliciousness score. If the score is above a certain predefined, the file is classified as “malicious”, otherwise “benign”.
* In order to cope with concept drift - model performance degradation over time, we may update the model from time to time by training it with newer files.

# BDP-AI

* **Info:**
  + <https://nest.cybereason.com/knowledgebase/6184036>
  + [https://cybereason.atlassian.net/wiki/spaces/NS/pages/30036951044/BDP+AI+White+List](https://cybereason.atlassian.net/wiki/spaces/NS/pages/30036951044/BDP%2BAI%2BWhite%2BList)
  + [https://cybereason.atlassian.net/wiki/spaces/IN/pages/30362534375/BDP+AI+-+document+unique+identifier+mechanism](https://cybereason.atlassian.net/wiki/spaces/IN/pages/30362534375/BDP%2BAI%2B-%2Bdocument%2Bunique%2Bidentifier%2Bmechanism)
  + <https://chatgpt.com/share/6919d722-03d8-8003-99c6-05d58e408f3c>
  + <https://github.com/cybereason-labs/data-science/blob/meta/BDP/train_new.ipynb>
* **Questions:**
  + From which version of the sensor BDP-AI is available?
  + What is the advantage of BDP-AI over BDP?
  + How is the model trained?
  + Hoe do we update the model?
* BDP stands for Behavioral Document Protection – It is a detection engine, based on YARA signatures, for the detection of malicious Office documents such as: Word / Excel / Powerpoint.
* BDP was based on a single strict signature, while every change to the document, also changed it’s signature. This approach make it difficult to sign the malicious behaviour it self.
* BDP is mostly obsolete, and now it is under NGAV with BDP-AI.
* The BDP-AI:
  + Uses the legacy BDP rule-based logic
    With
    Feature-based Machine Learning detector with smarter exclusions (allowlist, policy-based)
  + Computes Hash on macros & executable components inside the Office file.
  + Caching - to avoid re-scanning of the same contents.
  + Deduplication - avoid multiple reports on the same doc.
  + The BDP-AI needs a stable document unique identifier (UID) for:
    - **Allowlisting / exclusions** (policy-based).
    - **Caching**
    - **Deduplication**
  + UID (Unique Identifier) for a document:
    - BDP-AI extracts BDP model features (based on Yara rules) and computes UID from selected 137 features.
    - UID is checked against:
      * Policy exclusions (behavior ID / hash list).
      * Caches & Dedeuplication filters.
    - If UID is allowlisted:
      * BDP-AI returns “allow open” before prediction
        (AV signature flow remains active).
    - If not allowlisted:
      * Run the ML model using the full feature set.
      * Apply policy (Status/Mode) → Detect / Prevent / Quarantine / None.
    - Advantages:
      * Robustness to minor document changes.
      * Cross-machine stability (same content → same features → same UID).
      * Low overhead, since features are already computed for detection.
* Cope with False Positives
  + To cope with False Positives to calibrate the threshold of the ML for the appropriate balance between TP and FP.
  + In addition, as any other ML model, it should be updated with recent samples labeled correctly.

# Tasks

* Test new STool <https://cybereason.atlassian.net/browse/ENG-979> and report to Aaron Montsarj
* Pull request for branch [mlav\_14\_5\_25](https://github.com/cybereason-labs/data-science/tree/mlav_14_5_25/mlav)

🤝 Meetings

**Meetings**

# [Title]

…

# [Title]

…

✅ Tasks

**Tasks**

* Task 1
* Task 2
