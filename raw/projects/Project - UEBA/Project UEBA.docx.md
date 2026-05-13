# Project UEBA.docx

**🏁 Main**

Project
User & Entity Behavioral Analytics

# General

* **Description:** Applying User & Entity Behavioral Analytics to detect anomalies in user/entity activity.
* **Owner:** Aviad CohenGuy Kapach
* **Code:** first draft of ueba code translated to Python: <https://github.com/cybereason-labs/data-science/tree/ueba/ueba_python>
* **Jira:**
  + [ENG-3925: UEBA | Get & Explore data for POC](https://cybereason.atlassian.net/browse/ENG-3925?atlOrigin=eyJpIjoiM2Y3YTMyODA1M2QyNDczYWFhM2YwOGVlYWI1NmRhOTIiLCJwIjoiaiJ9)
* **Relevant Info:**
  + <https://github.com/Cybereason-Empow>
  + <https://github.com/Cybereason-Empow/main/tree/master/sst/empow/ueba>
* **Relevant Project:**
  + [IRCA Cloud](https://docs.google.com/document/d/1XCBTYJ-l-ZejwbuLCNB02bZ3_yLaszC4CXMeteYgCkQ/edit?tab=t.3pmv6qwy9sgg#heading=h.9354s7t7a0mj)

# Data

* [Observe APAC](https://131377279880.ap-1.observeinc.com/workspace/41001237/log-explorer?datasetId=41042193&s=501154-uxd4acg4)
* [Observe EU](https://111638659092.eu-1.observeinc.com/workspace/41000004/home)
* [Observe US](https://121530154444.observeinc.com/workspace/41029375/home)

# Old Tasks

# Tasks

* Aviad Cohen:
  + Ask Shoshana Avni to get access to all Sivan Omer documentation.
  + Aviad Cohen to assist in locating and obtaining access to old Empow files, including patents and code, possibly involving IT and legal teams:
    - <https://github.com/Cybereason-Empow/main/tree/master/sst/empow/ueba>
  + Involving Guy Kapach for assistance in UEBA research and development.
* Todd Leetham to research and draft UEBA business use cases and examples of behavioral anomalies to target:
  [UEBA Business Case](https://docs.google.com/presentation/d/1gDJNlZlWzXCouPswjFPTSH-G2T3qLBDRhNcXibsEqyg/edit?slide=id.g370dfadc396_1_474#slide=id.g370dfadc396_1_474)
* Team to engage with Kaoru Azuma for business validation and support of the UEBA initiative.
* Explore Empow code regarding UEBA: <https://github.com/Cybereason-Empow/main/tree/master/sst/empow/ueba>
* **Learn:**
  + Explore how to do UEBA on data from XDR in order to detect anomalies.
  + <https://www.linkedin.com/learning/insider-threat-hunting-detecting-and-responding-to-internal-security-risks/user-and-entity-behavior-analytics-ueba?u=62250692>
  + <https://www.linkedin.com/learning/implementing-and-administering-microsoft-sentinel/ueba-and-machine-learning?u=62250692>
* **Obtaining Data:**
  + Provide access to the relevant data.
  + Get permissions to Observe.
  + Get API to Observe.
* **Data:**
  + Filter Microsoft Windows Events using hueristic/technique, like Eli Salem did for AWS.
* **Code:**
  + Develop pipeline for code: Feature Extraction -> Dataset Creation (for X users) -> Anomaly Detection Algorithms. Implement code as classes (Feature Extractor, etc..)
* **Sanity Check:**
  + Does the features that we use allow us to distinguish between different users?
  + Based on our features, can we cluster the users to groups? Where similar users fall in the same group?
  + Based on our features, can we detect anomalies within user behavior over time?
* **Feature Extraction:**
  + Guy Michaela Kassorla
    - An event has detections and severity/risk scores – we can use them.
    - Use Raw logs.
    - Combine XDM data from multiple vendors together (ask Tue Luu)
* **Anomaly Detection:**
  + Explore/Research using ChatGPT/Claude:
    - Explain our data and formats.
    - Explore how to do anomaly detection on our use case.
    - Challenges: we have lots of users, lots of data per minute.
    - We are looking for an AD model that can work fast.
  + Event-wise anomaly detection:
    - Set an anomaly score per event.
  + Time-range-wise anomaly detection:
    - Feature Extraction:
      * Distribution (normalized histogram) of feature values in time range (set of events):
        + <https://docs.google.com/spreadsheets/d/1pISWqwnjr2NhR9Yot0kE25jrs3mqqqCiTDzhM3Tl0JA/edit?usp=sharing>
    - Train a baseline model, per user, on set of events on past time-range, a model per feature.
    - Test the model, per user, on future time-range.
    - Get an anomaly detection score/decision for the entire time-range. Can be done using HBOS algorithm.
    - For test aggregation (HBOS) - compare distributions
    - Guy Kapach - check aws data relevance to our data
    - **HBOS:**
      * Fit model per 1 week
      * Predict for 1 hour?
  + Distribution of Windows Events per user over time.
  + **[2025.12.07]**
    - Work with several selected different vendors
    - Extract features from each vendor
    - …
    - Run anomaly detection pipeline that produces an anomaly score per previous time-window.
    - Histogram of categorical features???
  + **Sesmograph / feedback simulation for each feature → action potential for anomaly**
    - [Example Excel](https://docs.google.com/spreadsheets/d/1pISWqwnjr2NhR9Yot0kE25jrs3mqqqCiTDzhM3Tl0JA/edit?gid=2059773285#gid=2059773285)
    - Check rate metrics per user.
    - Check the feasibility for implementation within Observe.
    - ![](data:image/png;base64...)
    - ![](data:image/png;base64...)
    - Does this approach feasible in terms of cost???
  + **[2026.01.21]**
    - Heatmap for AD Model per user over time:
      * Train: X weeks
      * Test: sequence of 4 hours windows
* **UEBA:**
  + What is UEBA vs Anomaly Detection???
  + Recommendation System
  + Vendors in Observe log events.
    Are these regular behavioral events or trigger/anomaly events?
    We would like to model the baseline behavioral events to detect anomalies.
* **QA:**
  + A model that can distinguish between different users.
  + A model that can detect anomalies in the behaviour of a specific user.
  + Simulate anomalies and attacks, then test whether the model detects them.

# Milestones

* **Current 2026.01.21:**
  + We have 30-days data (Observe Fortinet FortiGate Firewall)
    of 500 users, 4-hour interval.
  + Feature Extraction + Manipulation + Feature Elimination
  + AD ML Pipeline: Feature Extraction >> Train-Test Split >> Apply AD Models >> Visualization & Comparison Metrics (heatmaps, histograms, etc.)
* **Milestone 2026.02.05:**
  + Fix the pipeline:
    - Calibrate the hyperparameters of each model to achieve.
    - Fix feature scaling and more.
  + Expected results:
    - Cross-User: Train on user X (X-past weeks) | Test on user Y (remaining)
      * Heatmap:
        + AD model shows low-anomaly diagonal (user X Train-Test anomaly score)
        + Diversity of anomaly score. We expect to see both cases where different users are similar, or totally different (anomalous). We do not expect to see total red or total green.

User Clustering:

To validate that the diversity of anomaly scores is aligned with user clusters.

* + - * + Generate several 100 users heatmaps, per each model.
        + Mark only the diagonal with grid.
      * Have an agreement between some of the models:
        + High Pearson correlation.
        + Similar distribution of normalized**(?)** anomaly score.
    - Select the best models to continue with.
    - Train on user X (X-past weeks) | Test on user X on following times (4 hours)
      * Decide on how much time you need to train the model.
* **Core development:**
  + PER CLUSTER / USER model approach
    - Switch to model per-cluster instead of per-user:
      * Check feasibility of it:
        + In terms of detection:

outliers

* + - * + In terms of production: indeed training per-cluster is more feasible, but the clustering and choosing the correct cluster for each user might be challenging.
  + cluster rethinking (by simple, intuitive features: work periods and transmission volume).
    - Are clusters the way to go? is there
  + Calibrate user model threshold by cluster instead of global.
    - optimal threshold selection (per cluster threshold, per user model)
  + Try our AD model on another dataset (other than FortiNet). (OR?)
  + Analyze results using AI (it’s better to use an agent such as cursor than plain LLM such as chatGPT) - anomaly users, and some high score non-anomaly.
* **optimizations:**
  + Explore feature selection, and perhaps adding cluster -1 (or cluster overall) as a feature. outliers indication as a feature
  + Use sequential first seen etc. - stats that are dependent on history - did I see this IP in the past? - Inbar fill this rephrase
  + Repeat experiment on data in 1 hour intervals.
    - Find out the industry standard
    - determine the right time interval to work with (compare 4 hours?)
* Evaluation:
  + Generate synthetic anomalies to test the model on them.
  + Consult professionals how to inject anomalies
* Tests:
  + implement a unit test (inject synthetic anomalies, both trivial and sophisticated)
* **Future:**
  + go from a notebook experience to a proper code structure - Inbar should give the cue.

**birch (the clustering model)**

**Project Notebooks**

# fortinet\_pipeline\_no\_pruning.ipynb

Load raw aggregated data (csv file from Observe Fortinet Fortigate dataset e.g. fortinet\_30days.csv).

In case it wasn’t done on query, the script concatenates dev\_id with user\_id.

It takes only users which have more than 14 days of data (the days are not necessarily full, as we don’t expect all users to be active the same amount of hours, but it is important that their activity will be spread on a large portion of raw data’s dates).

The data was split to train/test based on 70% of the data range (the split was done time-wise and not randomly). The need to split to train and test data in this case is mainly because of the implementation of first-seen and KL divergence. Another notebook (fortinet\_pipeline.ipynb) is addressing this issue without prior separation to train/test but for each sample calculates these features based on previous observations).

Extract features - all resulting features are numerical.

After feature extraction, feature pruning takes place. However, in this case, feature pruning of a grid combination of variance and correlations is done without actually removing the features, but rather save them for later use (for each combination: list of features to remove, full pruning decision report).

The resulting data (users, extracted features, some metadata) was serialized to fortinet\_pipeline\_output\_full.csv and the suggested features to be removed to pruned\_features.pkl.

**NumericFeatureEngineering**

Compute mean, std, rates, EMA, residuals, z-scores, and rolling window statistics.

Most relevant hyperparameter: rolling\_windows : list of int, default=[3, 6, 12]

**CategoricalFeatureEngineering**

Compute array-based metrics: counts, unique, entropy, top-k coverage, concentration, KL divergence.

Most relevant hyperparameters: jsd\_windows=[12, 24], kl\_columns=None

**FirstSeenFeatures**

Track first-seen items using Bloom filters per user with serialization support.

**TimeFeatures**

Extract temporal features: hour/day cyclical encoding, per-user hour/day distributions.

*Notice that this class produces some low variance, static features such as day\_of\_week\_{x}\_ratio and hour\_of\_day\_{x}\_ratio.*

**UserAggregationFeatures**

Per-user aggregate statistics (mean, std, min, max) and deviation from baseline.

**FeatureCleaner**

Remove raw features that are not needed for the model.

*Notice that it currently removes arrays but perhaps for HBOS they should be retained (or at least formatted to be input for HBOS model, currently HBOS model uses their derived numerical features and not the raw distributions).*

**FeaturePruner**

Remove low-variance and highly correlated features. For correlated features, keep the one with highest variance.

Hyperparameters:

variance\_threshold : float, default=0.01

Threshold below which features are considered low-variance

correlation\_threshold : float, default=0.95

Correlation coefficient above which features are considered highly correlated

remove\_correlated : bool, default=True

Whether to remove correlated features. If False, only variance-based pruning is applied

Special methods:

This class, in addition to fit/transform Scikit-Learn API methods, also has get\_feature\_report() and print\_report() methods which generates and prints a detailed report of feature pruning decisions.

# fortinet\_pipeline.ipynb

Same as fortinet\_pipeline\_no\_pruning.ipynb, it contains some sanity checks - but they are aimed for integrity of raw data, I actually meant for sanity checks for engineered features - they were not implemented. So it should be implemented and tested.

Pruning conditions are fixed here, and the features are actually removed.

Except for that it contains SequentialFirstSeenFeatures and SequentialKLDivergenceFeatures which calculate these features based on previous observations rather than train/test data split. These features are not fully integrated in the pipeline and the whole notebook should be reviewed and revisited before run.

In spite of the above, this notebook should be used next time as its feature extraction is superior to the previous notebook.

**Treshold considerations**

## 1. What went wrong with the original per-user threshold?

Per-user models *do not imply* per-user comparable scores.

Even if every user has their own model:

* Score **scale**, **variance**, and **tail behavior** can differ significantly per user
* Some users are inherently more stochastic (admins, power users, service accounts)
* Some models are data-poor → noisier score distributions

So a naïve “same percentile / same numeric cutoff” per user almost always fails.

Your observation that the threshold “was not suitable” is expected.

## 4. Global vs per-cluster vs per-user — trade-off matrix

### **Global threshold**

**Pros**

* Simple
* Stable
* Easy to reason about operationally

**Cons**

* Implicitly assumes score comparability
* Penalizes:
  + noisy users
  + sparse users
  + highly variable roles

**Verdict** ❌ Only defensible if you first **explicitly normalize scores** (see §6)

### **Per-user threshold**

**Pros**

* Maximum personalization
* Works well for mature, data-rich users

**Cons**

* Extremely unstable for:
  + new users
  + role changes
  + concept drift
* Encourages overfitting
* Hard to govern at scale

**Verdict** ⚠️ Use only as a *refinement layer*, not as the primary control

### **Per-cluster threshold**

**Pros**

* Balances bias vs variance
* Threshold has consistent meaning *within a behavioral regime*
* Operationally tractable
* Naturally absorbs role-based heterogeneity

**Cons**

* Requires cluster stability monitoring
* Users drifting between clusters complicates alert history

**Verdict**

**✅ Best default choice for UEBA systems**

# Part A — How to determine per-cluster thresholds

## 1. First principle (non-negotiable)

**Never threshold raw scores.** Thresholds must live in **tail-probability space**.

For each cluster c:

p=P(S≥s∣c)

Where S is the anomaly score distribution for that cluster (or user→cluster mapped).

This makes thresholds **comparable and stable**.

### **1. What EVT is**

**Extreme Value Theory** is a branch of statistics that focuses on modeling the **behavior of the extreme tails** of a distribution — the very high or very low values — instead of the center (mean/variance).

In UEBA:

* Most events are normal → scores near 0 (or low tail probability)
* Anomalies are extreme → scores in the **far tail**

EVT gives you a **principled way to model the tail**, especially when:

* The tail is sparse (few anomalies)
* The raw score distribution is skewed or heavy-tailed
* You want a **probabilistic threshold** rather than an ad-hoc percentile

### **2. How EVT applies to per-cluster thresholds**

For a given cluster ccc:

1. Collect self-scores ScS\_cSc​ (all events scored by the model trained on that cluster)
2. Identify the **upper tail** of the scores (e.g., top 1% or 5%)
3. Fit an EVT distribution, typically a **Generalized Pareto Distribution (GPD)**, to that tail
4. Compute the **tail probability** of any score using this GPD
5. Choose your threshold τc\tau\_cτc​ based on a tiny tail probability ϵ\epsilonϵ (e.g., 10−610^{-6}10−6)

This way, your threshold is **statistically principled**:

* It adapts automatically to the cluster’s score distribution
* Works well for clusters with very few anomalies
* Avoids arbitrary percentile cutoffs

### **3. Why EVT is useful here**

* **Self-consistency**: ensures thresholds correspond to *extremely unlikely self-events*
* **Cluster heterogeneity**: each cluster can have its own EVT-fitted tail
* **Sparse anomalies**: even if you have almost no anomalies, EVT extrapolates a robust extreme cutoff
* **Operational stability**: thresholds don’t fluctuate wildly with minor changes in the cluster score distribution

P(S≥sτ​∣c)≤ϵ

while self-user anomaly is expected to be zero, in-cluster low anomaly rate is expected, and clustering should reflect a generalization of user behavior (so we don't expect User A (stable, narrow behavior) and User B (broad, variable behavior) to be in same cluster).

therefor, choosing threshold per-cluster base on a robust aggregation (e.g. median instead of mean) should keep my assumptions valid while calibrating in the cluster level. the question is how to optimize the correct threshold beside minimizing within-cluster anomaly.

perhaps manually inspection of cross-cluster anomalies under different thresholds?

## Primary constraint

A self (τ) ≤ ϵ1​

## Secondary constraint

A within (τ) ≤ ϵ

Where:

* ϵ1 ≪ ϵ2
* Both small
* No assumption about expected anomaly rate

## Objective (soft)

Maximize **separation margin**:

Δ(τ) = Across(τ) − A within(τ)

But only over the feasible region defined by constraints above.

So formally:

Τc∗ = arg⁡max ⁡τΔ(τ) s.t. Aself(τ) ≤ ϵ1,  A within(τ) ≤ ϵ2

🤝 Meetings

Meetings

# 2025.08.14 – UBA ignition meeting

Participants: Or Golov, Todd Leetham

## Overall Summary

The team discussed User and Entity Behavior Analytics (UEBA) focusing on anomaly detection through first-time user activities, volume, and temporal anomalies. They emphasized defining a clear business use case, leveraging previous work from [Empow](https://www.cybereason.com/press/cybereason-acquires-empow-to-enhance-xdr-offerings), and integrating UEBA with current XDR and EDR platforms. Action items include researching old Empower files and drafting use cases to present for business approval.

## Key Points

* UEBA success relies on detecting first-time user activities, volume, activity type, and temporal anomalies to identify suspicious behavior and potential compromises.
* Classifying users by persona and behavior patterns helps detect deviations and anomalies
* Previous Empow patents and code on UEBA provide a foundation; retrieving these files is critical to avoid starting from scratch
* Defining the business use case is essential before any proof of concept to ensure resource efficiency and alignment with business goals
* Integration with existing XDR and EDR platforms is planned, with a focus on demonstrating value to business stakeholders like Azuma-san.

![](data:image/png;base64...)

## Action Items

* Todd Leetham to research and draft UEBA business use cases and examples of behavioral anomalies to target
* Aviad Cohen to assist in locating and obtaining access to old Empow files, including patents and code, possibly involving IT and legal teams
* Team to engage with Kaoru Azuma for business validation and support of the UEBA initiative
* involving Guy Kapach for assistance in UEBA research and development.
* Ask Shoshana Avni to get access to all Sivan Omer documentation.

## Open Questions

* Where exactly are the old Empow files stored, and what is the process to gain access?
* How will UEBA capabilities be technically integrated with existing XDR and EDR solutions?
* What are the specific behavioral indicators and data types that will be prioritized for anomaly detection?

# [Title]

…

**Guy/Tue - 5/1/2026**

* What kind of datasets are in Observe?
* Which of them contain baseline data - i.e. normal activity alongside suspected?
* What fields are safe to ignore, which are critical? Which values have a special interest? I.e. - how can I use domain knowledge to detect anomalies?

✅ Tasks

Tasks

* Task 1
* Task 2

**UEBA code**

UEBA code was inspected:

* With cursor reading the project and summarizing it
* With cursor translating java source code into python code and then read by Guy Kapach

Cursor summary of java code:

### 🎯 Detection Engines:

1. Brute Force/Password Guessing (BfPwg) Engine:

* Uses sliding window analysis to track login attempts
* Features analyzed: Hash Frequency (HF), Count, Frequency
* Detects both brute force attacks and password guessing patterns
* Employs fuzzy logic scoring with trapezoidal/triangular membership functions

2. Geo-Location Engine:

* Analyzes impossible travel patterns between user logins
* Calculates minimum travel time vs actual time between geographic locations
* Uses longitude/latitude distance calculations
* Detects when users appear to travel faster than physically possible

3. Fuzzy Logic Scoring:

* Each engine uses fuzzy logic controllers (.fcl files)
* Converts behavioral features into Suspicion of Attack (SoA) scores
* Uses Center of Gravity defuzzification method
* Provides nuanced scoring rather than binary alerts

The code therefore provides non deterministic engines for detection of brute force logging attempts and peculiar geolocation connections. These are not anomaly detection in a statistical sense - which is the detection of outliers from a population, but rather engines for detection of pre-defined unusual user behavior.

The correspondence with Cursor was exported to a [markdown](https://drive.google.com/open?id=1BfjNNV_X5tkis2UXcBF8OvTpeNbm5G_A) file.

Generated python code should be reviewed, I’ve noticed that the fuzzy logic rules are not precisely in line with their java source’s.

**What competitors do**

What competitors do

[Microsoft](https://learn.microsoft.com/en-us/azure/sentinel/identify-threats-with-entity-behavior-analytics) prioritize for relevant attack vectors and scenarios based on security research aligned with the MITRE ATT&CK framework of tactics, techniques, and subtechniques that puts various entities as victims, perpetrators, or pivot points in the kill chain

I.e. - the data is not ingested naively but rather filtered to known mitre techniques.

**mitre-anomaly correlation by gemini**

I prompted Gemini with the intention to rephrase the following text, but incidentally it made a small research about relating mitre attacks with anomaly detection so I keep it here for later reference:

*Microsoft prioritize for relevant attack vectors and scenarios based on security research aligned with the MITRE ATT&CK framework of tactics, techniques, and subtechniques that puts various entities as victims, perpetrators, or pivot points in the kill chain*

To prioritize relevant attack vectors and scenarios for Microsoft UEBA, aligned with the MITRE ATT&CK framework, we need to consider how UEBA capabilities can detect malicious behaviors across various entities (victims, perpetrators, pivot points). This prioritization should be based on security research and the effectiveness of UEBA in identifying these patterns.

Here's a prioritized approach focusing on common and impactful attack vectors and scenarios:

**High Priority Attack Vectors & Scenarios (Leveraging UEBA Strengths):**

1. **Insider Threat Detection (Compromised or Malicious Users):**
   * **MITRE ATT&CK Focus:** T1078 (Valid Accounts), T1098 (Account Manipulation), T1134 (Access Token Manipulation), T1053 (Scheduled Task/Job), T1071 (Application Layer Protocol), T1036 (Masquerading), T1567 (Exfiltration Over Web Service).
   * **UEBA Value:** UEBA excels at establishing baselines for user behavior. Deviations like unusual access to sensitive data (e.g., accessing files outside of their typical working hours or from an unusual location), mass data exfiltration attempts, privilege escalation, or attempts to access systems they don't normally interact with are prime for UEBA detection.
   * **Scenarios:**
     + **Disgruntled Employee:** Suddenly accessing competitor information, intellectual property, or financial records.
     + **Compromised Account:** An attacker gaining access to an employee's account and performing actions significantly different from the legitimate user's historical behavior (e.g., logging in from a new country, attempting to create new accounts, accessing a high volume of uncommon files).
     + **Privilege Abuse:** A user with legitimate access to a system using that access for unauthorized purposes (e.g., an IT admin accessing personal data without a business need).
2. **Credential Theft & Lateral Movement:**
   * **MITRE ATT&CK Focus:** T1003 (OS Credential Dumping), T1021 (Remote Services), T1078 (Valid Accounts), T1087 (Account Discovery), T1059 (Command and Scripting Interpreter), T1550 (Use Alternate Authentication Material).
   * **UEBA Value:** Identifying abnormal logon patterns, failed authentication attempts across multiple accounts, unusual use of administrative tools (e.g., PsExec, RDP to non-standard hosts), and privilege escalation attempts. UEBA can detect when an account, typically used for a specific function, starts behaving like an administrator or attempts to access multiple hosts sequentially.
   * **Scenarios:**
     + **Pass-the-Hash/Ticket:** A compromised workstation's credentials are used to access other systems in the network, leading to unusual login patterns for that user account.
     + **Brute Force/Password Spraying:** Multiple failed login attempts against a set of accounts, followed by successful logins from a suspicious source.
     + **Service Account Abuse:** A service account, normally used for automated tasks, suddenly authenticating interactively or performing actions outside its defined scope.
3. **Data Exfiltration & Ransomware Prep:**
   * **MITRE ATT&CK Focus:** T1041 (Exfiltration Over C2 Channel), T1048 (Exfiltration Over Alternative Protocol), T1074 (Data Staged), T1567 (Exfiltration Over Web Service), T1486 (Data Encrypted for Impact).
   * **UEBA Value:** Detecting unusual file access volumes, attempts to copy large amounts of data to cloud storage, external drives, or unusual network shares. UEBA can identify "staging" behavior before exfiltration or encryption.
   * **Scenarios:**
     + **Mass Data Copy:** A user or service account suddenly copying an unusually large number of files from a sensitive share to an external cloud storage service.
     + **Renaming/Compressing Files:** Multiple files being renamed or compressed in preparation for exfiltration or encryption.
     + **Access to Archive Utilities:** Unusual use of archiving tools (e.g., 7-Zip, WinRAR) on sensitive data by an entity that doesn't typically perform such actions.
4. **Persistent Access & Command and Control (C2) Detections:**
   * **MITRE ATT&CK Focus:** T1071 (Application Layer Protocol), T1573 (Encrypted Channel), T1090 (Proxy), T1072 (System Network Configuration), T1053 (Scheduled Task/Job).
   * **UEBA Value:** While primarily network-focused, UEBA can contribute by identifying unusual network connections (e.g., connections to known malicious IPs, unexpected outbound traffic to non-corporate destinations, unusual DNS queries) or recurring automated activities (e.g., scheduled tasks that execute unusual commands or connect to external hosts).
   * **Scenarios:**
     + **Long-Lived, Low-Volume Traffic:** An internal host consistently communicating with an external IP address with very low, sporadic data transfer, potentially indicative of C2.
     + **Unusual External Connections:** A workstation or server initiating outbound connections to a country or IP range it has never communicated with before.

**Medium Priority Attack Vectors & Scenarios (Augmented by UEBA):**

1. **Initial Access through Phishing/Malware (Post-Compromise Behavior):**
   * **MITRE ATT&CK Focus:** T1566 (Phishing), T1189 (Drive-by Compromise), T1204 (User Execution).
   * **UEBA Value:** While not directly detecting the initial phishing email, UEBA is critical for detecting the *subsequent actions* after a user falls victim. This includes the execution of malware, creation of persistence mechanisms, or attempts at privilege escalation immediately after initial access.
   * **Scenarios:**
     + **Execution of Unusual Process:** After clicking a malicious link, a user's machine executes a never-before-seen process that attempts to establish a connection to an external IP.
     + **Credential Harvesting Attempt:** A user's machine attempts to access the local security authority (LSASS) process.
2. **Discovery & Reconnaissance:**
   * **MITRE ATT&CK Focus:** T1087 (Account Discovery), T1046 (Network Service Discovery), T1018 (Remote System Discovery), T1069 (Permission Groups Discovery).
   * **UEBA Value:** Detecting unusual and extensive internal scanning activity, excessive querying of Active Directory for user or group information, or an account attempting to enumerate a large number of network shares.
   * **Scenarios:**
     + **Internal Port Scan:** A user's workstation initiating scans against a wide range of internal IP addresses or ports.
     + **Excessive Active Directory Queries:** An account performing an unusually high volume of LDAP queries, particularly for sensitive groups or accounts.

**Prioritization Criteria for Microsoft UEBA:**

* **Behavioral Anomaly Detection:** Prioritize scenarios where deviations from an established baseline are a strong indicator of compromise. This is where UEBA truly shines.
* **Contextualization:** UEBA's ability to correlate activities across multiple data sources (logs, network, endpoint) for a specific entity adds significant value.
* **Low False Positive Rate Potential:** Focus on scenarios where the anomalies are less likely to be legitimate user behavior.
* **Impact of the Attack:** Prioritize scenarios that could lead to significant data loss, system compromise, or business disruption.
* **MITRE ATT&CK Coverage:** Ensure a broad range of tactics, techniques, and sub-techniques are covered, with a focus on those that are commonly observed in real-world attacks.

By focusing on these prioritized attack vectors and scenarios, organizations can effectively leverage Microsoft UEBA to enhance their detection capabilities against sophisticated and evolving threats, aligning their security research and efforts with the MITRE ATT&CK framework.

**anomaly detection resources**

<https://github.com/david-cortes/isotree>

Features can be selected by their kurtosis (especially important for models like EllipticEnvelope which requires n\_samples > n\_features \*\* 2).

[https://scikit-learn.org/stable/auto\_examples/miscellaneous/plot\_anomaly\_comparison.html#](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_anomaly_comparison.html)

Subsampling should be researched, according to <https://en.wikipedia.org/wiki/Isolation_forest#Properties> it performs well, but one should test it empirically.

מודלים deep learning <https://chatgpt.com/share/68f4f5e3-cae4-8003-ae2c-624365ab4476>

ֿהתייעצות כללית לגבי הפרויקט

<https://chatgpt.com/share/68f4f643-b428-8003-bcdb-66cf69c1cfc8>

**models**

הערה כללית: שים לב שניתן לשנות את ערך סף כדי לקבוע אם נקודה היא אנומליה, זה יכול להיות קריטי!

OneClassSVM

**מניח שכל הדאטה שעליו הוא מאומן הוא תקין**, ואתה רוצה לזהות דוגמאות חדשות לא מוכרות (novelty detection).

outlier detection:

The training data contains outliers which are defined as observations that are far from the others. Outlier detection estimators thus try to fit the regions where the training data is the most concentrated, ignoring the deviant observations.

novelty detection:

The training data is not polluted by outliers and we are interested in detecting whether a **new** observation is an outlier. In this context an outlier is also called a novelty.

אם יש לך דאטה שכבר כולל גם חריגים —
 scikit-learn ממליצה להשתמש במודלים אחרים, למשל:

* **IsolationForest**
* **LocalOutlierFactor (LOF)**
* **EllipticEnvelope** (אם הנתונים בערך גאוסיים)

אלה בנויים להתמודד עם “contamination” (כלומר נוכחות של חריגים באימון).

| **נושא** | **OneClassSVM** | **SGDOneClassSVM** |
| --- | --- | --- |
| **אלגוריתם** | פתרון קונבקס מלא (dual form) | אימון ב־SGD, פתרון מקורב |
| **מורכבות חישובית** | O(n2)O(n^2)O(n2) בזיכרון ו־O(n3)O(n^3)O(n3) בזמן 😬 | O(n)O(n)O(n) בזמן ו־זיכרון — סקלבילי מאוד 🚀 |
| **Kernel** | תומך בכל kernel (RBF, polynomial וכו’) | **רק ליניארי** (אין kernel trick) |
| **התאמה ל־Large scale** | לא מתאים — מתפוצץ בזיכרון | מתאים מאוד — אפשר לעבוד באצוות (mini-batches) |
| **דיוק (בנתונים קטנים)** | גבוה, “גבול חלק” ומורכב | מקורב, גבול גס יותר (ליניארי) |
| **שימושים טיפוסיים** | novelty detection מורכב, גבולות לא ליניאריים | מערכות real-time, online learning, סקייל גבוה |
| **Hyperparameters** | nu, gamma, kernel, kernel\_params | רק nu ופרמטרי SGD (eta0, max\_iter וכו’) |

**OneClassSVM** — חזק, מדויק, תומך בגבולות לא ליניאריים,
 אבל כבד מאוד ומוגבל ל־datasets קטנים/בינוניים.

**SGDOneClassSVM** — גרסה מודרנית וקלילה,
 רצה על דאטה ענק, אבל היא **רק ליניארית**, ולכן פחות מדויקת אם הנתונים לא ליניאריים.

**SGDOneClassSVM** implementation is meant to be used with a kernel approximation technique (e.g. sklearn.kernel\_approximation.Nystroem)

READ carefully LocalOutlierFactor documentation, especially *novelty* hyperparameter and how to use the algorithm in outlier vs. novelty detection. In short, LOF with novelty=False find outliers in dataset with fit\_predict while LOF with novelty=True assumes dataset to be inliers (I think) and generalizes distances to find anomalies in new data.

GMM

Autoencoder

HBOS

**Tab 9**

Data in observe:

Data arrives from several vendors, each vendor has a specific schema of data, the data is parsed into a unified structure, the raw data is in <data> field while the parsed data is in <xdm> field, of course that due to the unified nature of the data, some of the data in might be missing - some of the raw data would not be present in the xdm and vice cersa - some of the unified data might be NA because the vendor didn’t provide it.

An anomaly detection solution can consider XDM data as a primary data source for feature extraction, however, due to the nature of anomaly detection, perhaps the detection engine can learn the normal data from a vendor. In the future, a purposed model can have all the data (both xdm and raw - but beware of duplicates) or comprised from several models, generic one that will be using xdm data and specific to vendors.

**Tab 10**

POC:

Data source: windows events

Entities: there are several possible entity types, e.g. host and user. Each entity has its own features and I don’t want to mix them. For this poc I’ll start with host id as an entity and top 10-users as entities. Due to the mentioned difference in features I’ll do it in parallel.

XDM: even though logs have raw data that might be absence in the unified field (xdm), I’ll start with xdm data only for the POC.

Sometimes the anomaly is not a single event but a group of them, e.g. multiple logins attempts for a single user, moreover multiple login failures and then one successful.

Entity can be both principal (i.e. source) or target - it is important to include both roles in anomaly detection and it is important to differentiate between them (e.g. entity A commit acts x,y,z as principal and w,u,v as target)

One way to test model is to differentiate between users.

<code for later EDA>
col = "principal.ip"

xdm[col].explode().apply(**pd**.Series).agg(["nunique", "count"])

Values with $:
principal.application: array(['BIZP2018$', nan, 'Kerberos', 'NTLM', 'krbtgt', 'HECDC6$',

'HEG-N24-0200$', 'KUMI0007$', 'DCS-2SCM-004$', 'HECDC5$',

target.application: array(['BIZP2018$', nan, 'krbtgt', 'HECDC6$', 'HEG-N24-0200$',

'KUMI0007$', 'DCS-2SCM-004$', 'HECDC5$', 'ROOT-6$', 'ROOT-3$',

target.process.command\_line: ['BIZP2018$', nan, 'krbtgt', 'HECDC6$', 'HEG-N24-0200$', 'KUMI0007$', 'DCS-2SCM-004$', 'HECDC5$', 'ROOT-6$', 'ROOT-3$',

[target.resource.name](http://target.resource.name): array(['BIZP2018$@HEC.LOCAL', '0144326', '0141560', ..., 'AVD-386$',

**Feature engineering**

## For categories:

Unique counts

topK coverage: % of events covered by top-K most frequent ports

rare/first seen events

Entropy

KL-divergence

Domain knowledge - Category Semantic, Application Identity

## For numerical:

Aggregation by window of:

* Value (e.g. average)
* EMA (expected level for this user now)
* Residual: how abnormal this level is vs. expectation. (value - ema)
* Bucket rate: how quickly the level is moving.
* Volatility: standard deviation, how noisy / bursty the raw points were inside this bucket.​

Ratio (e.g. bytes sent/received)

Average

Standard deviation
