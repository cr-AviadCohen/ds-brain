# Project CMD Classification.docx

Main

**Project
CMD Classification**

#

# General

* **Description:** <complete>
* **Owner:** Aviad Cohen
* **Code:** <https://github.com/cybereason-labs/research_notebooks/tree/cmd-classification-aviad>
* **Machine:**
* **Presentation:** [LINK](https://docs.google.com/presentation/d/1wCEmuDcw1AfjvNAud-xeHwXyqdWxqdMYqYkBs_iq5xY/edit)

…

# Tasks

* **…**

💤 Current Status

**Current Status**

#

* **Gathering data:**
  + Working with Raz Isaac on extracting processes’ command lines from Elastic to Google Big Query.
  + Extracted data from GBQ:
    - **'global-soc-14311f.hunting\_amer.triage\_result'**,
    - **'global-soc-14311f.hunting\_apac.triage\_result'**,
    - **'Global-soc-14311f.hunting\_emea.triage\_result'**,
* **Feature Extraction:**
  + Developed feature extraction with very long and detailed configuration file containing keywords related to attacks using cmd. Finished work on that conf file.
* **Experiments:**
  + An experiment on both VirusTotal & GBQ data provided poor results.
  + ![](data:image/png;base64...)
* **Future work:**
  + Creating a dataset of validated benign & malicious cmd process command lines => experiment. As current

🧑‍🏫 Presentation

**Presentation**

# Short Progress Presentation

* **What is our goal?**
  + to classify process command lines as benign/malicious, at end-point machine, using ML/AI
  + It is considered a difficult task as maliciousness depends on context, which is not always available.
* **To types of command lines:**
  + Process command lines – commands used to initiate a new process – collected.
  + Interactive shell command / scripts executed via cmd.exe – not collected
* **OS:**
  + We will begin with Windows CMD / Powershell
  + We continue with MacOS – most beneficial for the product.
* **Data Collection:**
  + GitHub (Powershell)
  + VirusTotal (\*.bat files)
  + Customers:
    - Observe Ruslan Rustchev
    - Transarency
    - DI – Elastic
    - Google BigQuery
* **Solution:**
  + NOT CHOSEN YET
  + Classic ML-based model
  + LLM based:
    - LLM / Fine-Tuned LLM
    - RAG
* **Current:**
  + Collected data from VirusTotal: 10K
  + Collected customers data from BigQuery, a sample of 1 day: 95K records
  + Using LLM to label VirusTotal commands
  + Using Sigma rules to label
* **Help:**
  + ObserveRuslan Rustchev
  + Security research: Ofir Tal Eli Salem Chen Aviani
  + Elastic: Raz Isaac

❓ Questions

**Questions**

# Questions

1. **What is our goal?**
   to classify process command lines (used to execute a process)
   OR/AND
   Any command lines / scripts executed via cmd.exe?

   Currently, our system only collect processes command line – we have that data on all processes executed on customers. We do not collect (or monitor?) all command lines executed via cmd.exe.

   Inbar Dekel
   As the first step, let's focus on process command line. Commands that were run from an interactive shell and created a process are included also, as we will get them in the existing data and also in the future.

❗ Issues

**Issues**

# Issues

1. **In order to get a decision on a command line, we should also have the context in which the process was executed, including:**
   1. **Parent process:** ...
   2. **Grant Parent Process:** The *Grant Parent Process* (often termed Grandparent Process) refers to the parent of the parent of a given process.
      1. This is particularly useful in behavioral analysis and anomaly detection. For instance, if a command-line tool (like cmd.exe) was spawned by explorer.exe, that may be typical user behavior. However, if cmd.exe was spawned by a less common or suspicious grandparent (e.g., excel.exe → cmd.exe → powershell.exe), it might suggest malicious activity like Living off the Land Binaries (LOLBins) usage.
   3. **Process Image Path:** The *Process Image Path* is the full file system path to the executable file that initiated the process. It includes the drive letter, directories, and filename (e.g., C:\Windows\System32\notepad.exe).
      1. Used to verify the legitimacy of the running process. Attackers may attempt to masquerade malicious executables with trusted names but store them in unexpected directories.
   4. **Parent Image Path**
   5. **File Company:** This field represents the company name listed in the metadata (version info resource) of the executable or DLL file. It’s extracted from the PE (Portable Executable) headers under the CompanyName field.
      1. This metadata can help validate if a file was authored by a reputable vendor (e.g., Microsoft Corporation). However, it can be faked, so it’s best used in conjunction with digital signatures and file path validation.
   6. **File Product:** The *File Product* field specifies the product name associated with the executable or DLL. This is also metadata from the version information block embedded in the PE file.
      1. Used to further contextualize the file’s purpose or suite (e.g., “Microsoft Office Word” or “Google Chrome”). Anomalies or generic entries here may hint at obfuscation or unauthorized tools.
   7. **Internal Name:** The *Internal Name* is another metadata field in the PE file’s version resource, representing the original name assigned by the developer—often the filename used during the build process.
      1. Attackers may rename binaries for camouflage, but the internal name may remain unchanged. Detecting mismatches between the filename, internal name, and image path is useful for identifying tampering or masquerading techniques.

**HOWEVER, most of the above list canot be extracted.**

🧑‍🎓 Research

**Research**

# Research

* Connected Papers: <https://www.connectedpapers.com/main/f7ba64393e1c9fde5288aa0c95cafbdaaa41a92d/Detection-of-Malicious-Remote-Shell-Sessions/graph>
* GenSpark.ai report: <https://www.genspark.ai/spark?id=47a31f83-4c29-47ce-92b1-a900b003e6d8>

# Academic Papers

## Paper: Detection of Malicious Remote Shell Sessions (2019)

<https://ccdcoe.org/uploads/2019/06/Art_26_Detection-of-Malicious-Remote-shell-Sessions.pdf>

This paper discusses methods to differentiate between malicious and benign sequences of commands in remote shell sessions. The researchers describe feature selection techniques and classifier variations, including a one-command classifier and an N-command classifier, to effectively identify malicious activities.

**Abstract:**
Remote shell sessions via protocols such as SSH are essential for managing systems, deploying applications, and running experiments. However, combined with weak passwords or flaws in the authentication process, remote shell access becomes a major security risk, as it allows an attacker to run arbitrary commands in the name of an impersonated user or even a system administrator. For example, remote shells of weakly protected systems are often exploited in order to build large botnets, to send spam emails, or to launch distributed denial of service attacks. Also, malicious insiders in organizations often use shell sessions to access and transfer restricted data.

In this work, we tackle the problem of detecting malicious shell sessions based on session logs, i.e., recorded sequences of commands that were executed over time. Our approach is to classify sessions as benign or malicious by analyzing the sequence of commands that the shell users executed. We model such sequences of commands as n-grams and use them as features to train a supervised machine learning classifier. Our evaluation, based on freely available data and data from our own honeypot infrastructure, shows that the classifier reaches a true positive rate of 99.4% and a true negative rate of 99.7% after observing only four shell commands.

## Paper: Command-line Risk Classification using Transformer-based Neural Architectures (2024)

<https://arxiv.org/pdf/2412.01655>

This recent study proposes a transformer-based neural network approach for classifying command-line inputs as malicious or benign. The authors highlight the effectiveness of large language models in understanding command-line context, leading to improved classification accuracy.

**Abstract:**
To protect large-scale computing environments necessary to meet increasing computing demand, cloud providers have implemented security measures to monitor Operations and Maintenance (O&M) activities and therefore prevent data loss and service interruption. Command interception systems are used to intercept, assess, and block dangerous Command-line Interface (CLI) commands before they can cause damage. Traditional solutions for command risk assessment include rule-based systems, which require expert knowledge and constant human revision to account for unseen commands. To overcome these limitations, several endto-end learning systems have been proposed to classify CLI commands. These systems, however, have several other limitations, including the adoption of generalpurpose text classifiers, which may not adapt to the language characteristics of scripting languages such as Bash or PowerShell, and may not recognize dangerous commands in the presence of an unbalanced class distribution.

In this paper, we propose a transformer-based command risk classification system, which leverages the generalization power of Large Language Models (LLM) to provide accurate classification and the ability to identify rare dangerous commands effectively, by exploiting the power of transfer learning. We verify the effectiveness of our approach on a realistic dataset of production commands and show how to apply our model for other security-related tasks, such as dangerous command interception and auditing of existing rule-based systems.

## Paper: Detecting Malicious PowerShell Commands using Deep Neural Networks (2018)

<https://dl.acm.org/doi/10.1145/3196494.3196511>

**Abstract:**

Microsoft's PowerShell is a command-line shell and scripting language that is installed by default on Windows machines. Based on Microsoft's .NET framework, it includes an interface that allows programmers to access operating system services. While PowerShell can be configured by administrators for restricting access and reducing vulnerabilities, these restrictions can be bypassed. Moreover, PowerShell commands can be easily generated dynamically, executed from memory, encoded and obfuscated, thus making the logging and forensic analysis of code executed by PowerShell challenging. For all these reasons, PowerShell is increasingly used by cybercriminals as part of their attacks' tool chain, mainly for downloading malicious contents and for lateral movement. Indeed, a recent comprehensive technical report by Symantec dedicated to PowerShell's abuse by cybercrimials [52] reported on a sharp increase in the number of malicious PowerShell samples they received and in the number of penetration tools and frameworks that use PowerShell. This highlights the urgent need of developing effective methods for detecting malicious PowerShell commands.

In this work, we address this challenge by implementing several novel detectors of malicious PowerShell commands and evaluating their performance. We implemented both "traditional" natural language processing (NLP) based detectors and detectors based on character-level convolutional neural networks (CNNs). Detectors' performance was evaluated using a large real-world dataset. Our evaluation results show that, although our detectors (and especially the traditional NLP-based ones) individually yield high performance, an ensemble detector that combines an NLP-based classifier with a CNN-based classifier provides the best performance, since the latter classifier is able to detect malicious commands that succeed in evading the former. Our analysis of these evasive commands reveals that some obfuscation patterns automatically detected by the CNN classifier are intrinsically difficult to detect using the NLP techniques we applied. Our detectors provide high recall values while maintaining a very low false positive rate, making us cautiously optimistic that they can be of practical value.

# Blogs

## Obfuscated Command Line Detection Using Machine Learning (2018)

<https://cloud.google.com/blog/topics/threat-intelligence/obfuscated-command-line-detection-using-machine-learning/>

This blog post presents a machine learning (ML) approach to solving an emerging security problem: detecting obfuscated Windows command line invocations on endpoints. We start out with an introduction to this relatively new threat capability, and then discuss how such problems have traditionally been handled. We then describe a machine learning approach to solving this problem and point out how ML vastly simplifies development and maintenance of a robust obfuscation detector. Finally, we present the results obtained using two different ML techniques and compare the benefits of each.

📚 Datasets

# Collection of Malicious Command-Lines

## VirusTotal.com

VT file search modifiers: <https://docs.virustotal.com/docs/file-search-modifiers>

* CMD:
  + *type: bat name: .bat positives: 10+*
* Powershell:
  + *type: powershell name: .ps1 positives: 10+ (returns also bat/js files for some reason)*
* MacOS:
  + *Type: shell positives: 10+*

*\*\* VT search sometimes returns files with extensions different from the requested type. The type is determined by magic signature, so the file type is sometimes doesn’t correspond to the actual true file type.*

*\*\* We can look at the [behavoir >> Activity Summary >> Shell Commands] section for a positive file. There is a list of shell commands (considered malicious) executed by the malware. Example:* [*https://www.virustotal.com/gui/file/706f3eec328e91ff7f66c8f0a2fb9b556325c153a329a2062dc85879c540839d/behavior*](https://www.virustotal.com/gui/file/706f3eec328e91ff7f66c8f0a2fb9b556325c153a329a2062dc85879c540839d/behavior)

*\*\* We would like to have a dataset of single commands. However, most of the malicious files in VT contain scripts, which have multiple commands. These datasets can be used for evaluation by separating command-by-command and checking whether the avg/max maliciousness score is above the threshold.*

*\*\* RECOMMENDED: filter VT for ransomware malware and extract the cmd commands from the behavior section.*

### **Filter only process command lines**

<https://chatgpt.com/share/67cec5b3-e73c-8003-9e85-e38f7ddd469c>

![](data:image/png;base64...)

##

## Data From Customers

### **F5 UI**

* Request access via Apono, select customer name and get temporary access almost immediately.
  There is also a Slack plugins for quick request.

![](data:image/png;base64...)

Example of Motorola UI:
<https://c-motorola-ui-admin.ui.cybereason.dom/#/EPP-overview>

### **GSOC**

* Slack conversation with Ruslan Rustchev:
  <https://cybereason.slack.com/archives/C08ER8H9E07/p1741086124584149>

### **Transparency (TR)**

* Shir Elmaliach has access to TR
* Data from Customers’ Endpoints is being sent to TR and held in-memory for fast retrieval but with low retention.
* From the TR the data is streamed to Kafka.
* **Graph:**
  + Information from TR is uploaded to a Graph.

### **DI**

* The data from Kafka is streamed to and collected by the Data Infrastructure (DI) for retrieval with longer retention (3 days). DI = [Earospike](https://aerospike.com/) and [ElasticSearch](https://www.elastic.co/)
* The ***Elasticsearch*** holds production data, and has 30 clusters.
  Each cluster contains lots of servers, and lots of different customers' data.
* Table of servers by regions and customers can be found here: <https://monithor.cybereason.net:8443/hammer/servers> (Requires VPN + Cybereason Google)

![](data:image/png;base64...)

* We found processes command lines data of customers in Elastic.
* To get access to Elastic, one should get access to [https://keepersecurity.com/vault/#](https://keepersecurity.com/vault/) by IT.

![](data:image/png;base64...)

* IT also needs to add you to the ‘*Luminate-Kibana*’ group, then you will be able to see it on Okta:
  [https://cybereason.**luminatesec**.com/home?filter=&page=0](https://cybereason.luminatesec.com/home?filter=&page=0)
  Here you can see all Kibana servers for different regions and production / dev envs

![](data:image/png;base64...)

* Example of one environment:
  <https://cr-prod-hp1-eu-west1-b-kibana.cybereason.luminatesec.com/app/dev_tools#/console>

![](data:image/png;base64...)

* General Qeury for all data structure

GET niceincontact-prod.benign/\_search

{

"\_source": [],

"query": {

"bool": {

"must": [

{ "match": { "elementType": "Process" } }

]

}

}

}

* Query to get Process.commandLine:

GET niceincontact-prod.benign/\_search

{

"\_source": ["Process.commandLine"],

"query": {

"bool": {

"must": [

{ "match": { "elementType": "Process" } }

]

}

}

}

Michal Ossowski

I believe there's no way to connect to ES using credentials (only cert authentication is allowed). Also you can't connect to prod ES from non-prod environment

<https://cybereason.slack.com/archives/C02M633K6LV/p1742198823391309?thread_ts=1742126944.477919&cid=C02M633K6LV>

### **Google Big Query**

* On meeting with Raz Isaac, he explained the data the data is collected from customers end-point >> Transparency >> DI (Elasticsearch / aerospike) >> BigQuery
* I searched for table containing the command\_line of processes and found:

![](data:image/png;base64...)

Storage info:

* Number of rows: 476,242,121
* Number of partitions: 549
* Total logical bytes: 393.43 GB

![](data:image/png;base64...)

# ChatGPT: Malicious Command-Line Command Datasets

Malicious command-line command datasets for Windows CMD, PowerShell, and macOS Terminal are valuable for developing threat detection tools and research. Below, we outline sources for these datasets, how they are collected, labeling schemes, comparisons of real vs synthetic data, and important legal/ethical considerations.

## Publicly Available Datasets and Sources

Malicious command-line command datasets for Windows CMD, PowerShell, and macOS Terminal are valuable for developing threat detection tools and research. Below, we outline sources for these datasets, how they are collected, labeling schemes, comparisons of real vs synthetic data, and important legal/ethical considerations.

* **Splunk Attack Data (GitHub)** – Splunk maintains a public repository of curated attack datasets containing host logs from various simulated and real attacks . This collection (over 9 GB of data) includes Windows event logs (e.g., Sysmon, Security 4688, PowerShell logs) capturing malicious command executions. Each dataset is annotated with MITRE ATT&CK technique IDs and descriptions for context . For example, a dataset for credential dumping maps to technique T1003.001 and provides the associated Windows event logs (Sysmon, PowerShell, etc.) that recorded those malicious commands . The repository enables analysts to download specific attack scenarios or logs via Git Large File Storage. These datasets help quickly test detection rules without having to run the attacks live.
  + <https://github.com/splunk/attack_data>
  + <https://aclanthology.org/2024.emnlp-main.1126.pdf>
    - *This research addresses command-line embedding in cybersecurity, a field obstructed by the lack of comprehensive datasets due to privacy and regulation concerns. We propose the first dataset of similar command lines, named CyPHER.*
    - Dataset:
      * <https://github.com/cycraft-corp/CmdCaliper/tree/main/data>
      * <https://huggingface.co/datasets/CyCraftAI/CyPHER>
* **Atomic Red Team (Red Canary’s Atomic Tests)** – Atomic Red Team is an open library of simple adversary technique tests mapped to the MITRE ATT&CK framework . While not a log dataset per se, it provides a large repository of known malicious commands and scripts that can be executed on Windows, macOS, and Linux for testing purposes. Each “atomic test” includes one or more command-line strings to emulate a specific attack technique. For example, Atomic tests cover Windows CMD misuse (T1059.003), PowerShell abuse (T1059.001), and macOS/Linux Bash commands (T1059.004). Researchers often use Atomic Red Team as a source of ground-truth malicious commands, since it spans **55+**<https://github.com/redcanaryco/atomic-red-team>
* **OTRF Security Datasets (securitydatasets.com)** – The Open Threat Research Forge provides an open-source collection of malicious and benign logs from different platforms, aimed at expediting threat analysis . The Security Datasets project includes Windows attack traces captured during adversary emulation exercises (using tools like Empire, Cobalt Strike, etc.). Data is organized by ATT&CK tactic (e.g. defense evasion, credential access) and scenario. Each scenario’s host events are stored in JSON format and compressed (zip) for easy sharing . For instance, a dataset might contain the sequence of Windows process creation events (with full command-line arguments) for an “Empire Mimikatz Kerberos key extraction” technique, along with a description of the scenario . Downloads are provided via GitHub, and the datasets often include a “Host” log of all commands executed during the simulation.
  <https://opencybersecurityalliance.org/fun-with-securitydatasets-com-and-the-kestrel-powershell-deobfuscator/#:~:text=,data%20analysis%20and%20threat%20research>
* **Malicious PowerShell Script Repositories** – There are community datasets focusing on PowerShell, given its prevalent use in attacks. For instance, a GitHub project released a *Malicious PowerShell Script Dataset* containing numerous harmful PS1 scripts used in deep learning research . This dataset aggregated scripts from offensive security tool repos on GitHub (e.g., PowerSploit, Empire, Nishang) as well as real malware samples from sandbox platforms and malware databases. It includes both the original malicious scripts and their obfuscated variants (~25% were obfuscated using tools like Invoke-Obfuscation) to mimic real attacker techniques . The dataset is available in source code form (collection of .ps1 files with hashes as filenames) for researchers to use in malware detection experiments.
  <https://github.com/Fa2y/Malicious-PowerShell-Dataset>
  <https://github.com/das-lab/mpsd> (malicious & Benign PowerShell scripts)
* **Honeypot-Captured Command Datasets** – Honeypot projects can capture real-world malicious commands, especially for Unix-like shells (which parallel macOS Terminal usage). For example, the Cowrie SSH/Telnet honeypot records attacker keystrokes and shell commands. Kaggle and academic repositories have shared Cowrie honeypot data, including thousands of malicious shell commands recorded over weeks of internet-exposed honeypot operation . One such dataset collected a year’s worth of attacks from 50 honeypot nodes (across the US and EU), logging every command entered by attackers (stored in structured JSON with timestamps and session IDs) . While these honeypot datasets mostly capture Linux commands (busybox, Bash), many of those commands (e.g., file downloads via curl | sh, adding users, launching crypto miners) are relevant to macOS as well due to its Unix underpinnings. They provide insight into opportunistic attack behavior “in the wild.”
  <https://zenodo.org/records/3687527#:~:text=This%20dataset%20contains%20all%20data%C2%A0collected,May%202019%20to%20February%202020>
  (I didn’t find any cmd commands there. I checked a sample [cyberlab\_2019-05-13.json.gz](https://zenodo.org/records/3687527/files/cyberlab_2019-05-13.json.gz?download=1))
* **Threat Intelligence Feeds and Sandboxes** – Public malware databases and sandboxes can be mined for command-line artifacts. Platforms like [*VirusTotal*](https://www.virustotal.com/), [*Hybrid Analysis*](https://www.hybrid-analysis.com/), [Any.RUN](https://any.run/) and [*MalwareBazaar*](https://bazaar.abuse.ch/) allow searching for specific command-line strings within submitted samples. Researchers have programmatically queried such services to gather malicious commands – for instance, scraping Hybrid Analysis for execution reports that contain PowerShell or CMD usage. In the PowerShell dataset mentioned above, the authors used a sandbox (“Triage”) API and Hybrid Analysis filters to retrieve malicious PowerShell invocations tied to known malware (Metasploit, Cobalt Strike). Similarly, VirusTotal Intelligence queries can find samples that invoke cmd.exe or osascript, yielding a collection of real malware command lines (though access requires proper licensing). Some open threat feeds (and vendor blogs) also publish high-level IOBs (Indicators of Behavior), which may list the exact commands used by threat actors during campaigns.

## Methods for Generating and Collecting Command-Line Datasets

Collecting malicious command-line data can be challenging, but several methods are used in practice:

* **Honeypots and Deception Systems**: Deploying honeypots is a direct way to capture real attacker commands. For Windows, one might use an SMB/RDP honeypot or instrument a decoy Windows VM to record command-line execution (e.g., via Sysmon or Powershell transcription logging). For Unix/Mac, tools like Cowrie (SSH/Telnet honeypot) log every shell command attackers type, producing real-world malicious command sequences . Honeypots can attract brute-force logins and post-exploitation commands (such as downloading payloads, creating backdoors, etc.), which are invaluable for assembling real attacker command datasets. The drawback is that honeypots mostly capture opportunistic or automated attacks rather than targeted intrusions.
* **Security Log Mining**: Many organizations collect extensive logs from endpoints and servers (via EDR, SIEM, Sysmon, etc.). Researchers can mine these logs for malicious or suspicious command lines. For example, Windows Event ID 4688 (process creation) and Sysmon Event ID 1 logs include the full command-line of each process. By filtering those logs for known bad patterns (like PowerShell with -EncodedCommand, or cmd.exe spawning unusual utilities), one can compile a dataset of real malicious commands seen in production. Some detection content, like Splunk’s analytic for “unusual command lines”, is built on EDR data that flags commands with rare or malware-like tokens . Aggregating such alerts over time yields a labeled set of malicious vs benign command lines. However, privacy and proprietary concerns usually prevent raw enterprise log data from being publicly released (researchers often must use it internally or in anonymized form).
  <https://research.splunk.com/endpoint/9c53c446-757e-11ec-871d-acde48001122/#:~:text=The%20following%20analytic%20detects%20potentially,exfiltration%2C%20or%20further%20system%20compromise>
* **Malware Analysis and Reverse Engineering**: Analyzing malware samples can reveal the command-line actions they perform. Reverse engineers often extract command strings from malware (e.g., the commands a Trojan issues via cmd.exe or the script a macro executes in Terminal). Dynamic analysis in sandboxes will record any OS commands invoked by the malware. By running a variety of malware in a controlled environment, one can log all cmd/Powershell/bash calls and aggregate those as a dataset of malicious commands. For example, if a malware batch script tries to add a user (net user /add ...) or disable security tools (sc config WinDefend start= disabled), those get captured in sandbox logs. Over many samples, a collection of distinct malicious command lines can be built. Some public datasets have leveraged this approach – e.g., scraping sandbox outputs for PowerShell commands or using VirusTotal’s API to retrieve the execution traces of malware that use scripting.
* **Adversary Emulation and Red Teaming**: Security teams and researchers often generate synthetic datasets by executing known attack techniques in a lab. Projects like [Atomic Red Team](https://www.atomicredteam.io/) and [Splunk Attack Range](https://github.com/splunk/attack_range) automate running of hundreds of malicious commands (from trivial to sophisticated) in test VMs and collect the resulting telemetry. This method yields high-quality labeled data (you know which technique each command corresponds to) and can cover a broad range of attack behaviors. For instance, one can simulate a pass-the-hash attack or a Mac persistence script, and capture all commands issued. The **OTRF Security Datasets** and **Splunk attack\_data** were largely built via such adversary emulation – using tools (Atomic tests, Covenant, Empire, etc.) to perform attacks and logging everything . The advantage is full control and labeling, but the commands, while realistic, may lack the creativity or variability of real criminals (they’re often idealized examples from the ATT&CK framework).
* **Manual Threat Research and Compilation**: Another method is manually collecting malicious commands from threat intelligence reports, blogs, and databases. Many published incident reports by security companies include the actual commands attackers ran on victim systems (for example, a report might show an attacker ran ipconfig /all & net group "Domain Admins" /domain during recon). Researchers can gather these documented commands across many reports to form a dataset. Additionally, community projects (like LOLBAS for Windows and its equivalent for macOS/Linux) list living-off-the-land binaries and how they are abused, effectively providing examples of malicious command usage. Although manually curated, these collections can be invaluable as they are drawn from real-world cases. The limitation is that this process is labor-intensive and may bias towards well-known attacks (since stealthy or unpublished ones won’t be in open sources).

## Availability of Labeled Datasets (Attack Categories & Frameworks)

Labeled datasets (where each command is tagged with an attack technique or category) are extremely useful for supervised learning and analytics. Several sources provide or utilize such labeled command data:

* **MITRE ATT&CK Mappings**: Datasets derived from adversary emulation are often labeled by MITRE ATT&CK technique. For example, each Atomic Red Team test is inherently labeled with the technique ID it emulates (T-number). The Splunk attack\_data repository explicitly includes an array of ATT&CK technique IDs in each dataset’s metadata . This means one can filter the data by tactic or technique (e.g., grab all commands related to Privilege Escalation vs Defense Evasion). The Cybereason C2 matrix and Red Canary’s Threat Detection Report also classify malicious command usage by ATT&CK. Having commands categorized (such as “Credential Dumping” commands vs “Persistence” commands) allows training models to recognize patterns specific to each class.
* **Academic Datasets with Labels**: Academic researchers have begun releasing command-line datasets tailored for machine learning, often with labels. The *CmdCaliper* study (2024) introduced **CyPHER**, a dataset of paired similar command lines for embedding training . Their **testing set** of 2,807 real malicious commands was sourced from the Splunk Attack Data and thus carries MITRE technique context . In their experiments, they treat each known malicious command and its associated technique as a class for retrieval tasks . Another example is an earlier Malicious PowerShell Scripts Database (MPSD) by a research lab, which labeled PowerShell scripts as malicious or benign for detection evaluation. While such academic datasets may not always be broadly labeled by technique, they usually at least distinguish malicious vs legitimate, and sometimes group malicious samples by family or behavior (e.g., tagging a command as associated with ransomware vs RAT activity).
* **Tagged Honeypot/Attack Logs**: When researchers share honeypot data or generated attack logs, they often accompany it with meta-labels. For instance, the Cowrie honeynet dataset on Zenodo tags each session with a “sensor type” (low or high interaction) and could be post-processed to label commands as part of brute-force attacks, botnet malware installs, etc. Similarly, OTRF’s Security Datasets include descriptive titles (like “Empire Invoke PSInject – Defense Evasion”) which implicitly label the commands with their goal/tactic. There are also community detection rule repositories (Sigma, YARA, etc.) where each rule targeting a malicious command pattern is mapped to ATT&CK—these could be seen as labeled examples of commands that trigger the rule, although not a structured dataset in the conventional sense.
* **Framework-Specific Categories**: Some datasets categorize commands by the tool or framework used. For example, a collection of commands extracted from Cobalt Strike or Metasploit might label each entry by the tool’s module or the stage of attack (reconnaissance, exploitation, etc.). The PowerShell script datasets sometimes note whether a script is from a known offensive toolkit (like PowerSploit) versus an unscripted malware. MITRE’s CAR (Common Attack Pattern Repository) and other frameworks might provide schemas to label commands as well (like “cleanup command”, “lateral movement command”). Overall, labeled datasets exist primarily in research and specialized community projects, often tying each malicious command to a higher-level classification (attack technique, malware family, or intent).

## Real-World vs Synthetic Datasets

There is an important distinction between **real-world command data** (collected from actual attacks) and **synthetic data** (generated via simulation or automation):

* **Real-World Data**: These commands come from real attacker activity, whether observed in honeypots, incident response logs, or sandbox executions of live malware. Real-world datasets tend to capture the messy, varied nature of attacks. They include genuine adversary quirks — e.g. typo errors, mixed languages, context-specific paths, heavy obfuscation, or multi-step one-liners strung together. This makes them highly valuable for building robust detection (they reflect what true attacks look like). For instance, a real attack might use powershell.exe -EncodEdCoMMAND ... (random capitalization) or a macOS malware might use atypical directories for payloads, which a simulation might not anticipate. However, real data can be **incomplete** (we might only capture what was logged, missing context of what succeeded or failed) and **skewed** toward known threats (if it’s based on known malware samples or common attack tools). Also, obtaining large real-world datasets is hard due to privacy and legal hurdles – often resulting in smaller sample sizes. In the CyPHER study, the authors note the scarcity of comprehensive real command-line data due to privacy/regulation issues . Their use of a real-world sourced test set introduced higher variability (significantly different distribution) compared to the training data generated by AI, underscoring how unpredictable real attacker inputs can be .
* **Synthetic Data**: Synthetic command datasets are generated by defenders or researchers. This could be running Atomic Red Team tests, writing custom scripts to simulate attacks, or even using AI to produce plausible malicious commands. The benefit of synthetic data is **controllability** – one can ensure all major attack techniques are represented and label them easily. They are also free of sensitive information. Projects like Atomic Red Team cover a broad range of tactics systematically, including many edge-case commands that real attackers might rarely use (but are possible). Additionally, recent work has shown you can leverage Large Language Models to generate diverse malicious commands from a seed list . The CmdCaliper project, for example, synthetically generated tens of thousands of command-line pairs using LLMs to augment their training data . This approach produced a high diversity of commands (covering 73.5% of all Windows command types by their measure) which might surpass what any single organization could observe in the wild. The downside is that synthetic commands might **lack context or subtlety**. Attack simulation scripts often run the “happy path” of an attack technique (minimal obfuscation, ideal conditions). Real attackers may chain multiple techniques in one line or use unconventional syntax to evade detection, whereas a lab simulation might run one technique at a time in isolation. Thus, models trained only on synthetic data can sometimes misjudge real-world inputs. Researchers usually acknowledge this gap and aim to validate on real data when possible .

In practice, a combination is best: using synthetic datasets to cover the full landscape of attacks, and mixing in real-world samples to ensure authenticity. Some studies explicitly compare performance on synthetic vs. real data – often finding that models need fine-tuning on real logs to handle the noise and variability. Synthetic data is excellent for covering known knowns (all documented techniques), while real data often reveals unknown quirks or blends of techniques not anticipated. There’s also the aspect of **frequency**: real-world datasets show which commands are most common in attacks (e.g., whoami or nslookup appear very frequently in real intrusions), whereas a synthetic set might treat all included commands equally. This can affect how detection rules are prioritized.

## Legal and Ethical Considerations

Working with malicious command-line datasets raises several legal and ethical points:

* **Authorization and Consent**: Data should only be collected from systems and networks with proper permission. Logging attacker commands on your honeypot or network is generally acceptable (and often legal, as the attacker has no authorization), but one must ensure no laws are broken in the process of luring or interacting with attackers. If data is collected from a corporate environment, even if it’s “malicious” activity, there may be privacy implications for employees or third parties. Always follow applicable privacy laws and get consent or approvals for using internal security logs in research .
* **Privacy and Anonymization**: Malicious commands could inadvertently contain sensitive information. For example, an attacker’s command might include hardcoded credentials, IP addresses, or file paths unique to a victim. Before sharing such data, researchers should sanitize it (anonymize IPs, redact credentials or company-specific names). The maintainers of the CyberLab honeynet dataset did exactly this by pseudonymizing all IP addresses and hostnames in the logs . Ethically, we must protect not just victim identities but even attacker identities or infrastructure from unwarranted exposure if not necessary for the research.
* **Malware Handling and Distribution**: If the dataset includes actual malicious scripts or binaries (e.g. a PowerShell script that downloads malware), special care is needed. Hosting and distributing malware code can be legally restricted. In some jurisdictions, mere possession of active malware source code might be considered illegal or subject to misuse law . Therefore, many public datasets stick to *observables* (like command strings) rather than packaging live malware. If sharing malicious scripts, ensure they are disabled (for instance, remove or neutralize the destructive part) or clearly mark them for research use. Platforms like GitHub often take down repositories that contain live malware, so dataset curators sometimes provide hashes and require users to download dangerous samples from malware databases under controlled conditions.
* **Usage Restrictions and Licensing**: Public datasets often come with licenses (Splunk’s and OTRF’s are Apache 2.0 or similar) that allow free use for research and detection development. However, using data from services like VirusTotal is subject to their Terms of Service – typically forbidding republishing the data without permission. It’s important to respect any user agreements when collecting data (e.g., API usage agreements for sandboxes or OSINT feeds). Also, if you incorporate others’ data (say, screenshots or logs from a vendor report), be mindful of copyright. Generally, factual lists of commands have low copyright concerns, but the surrounding context from reports could be protected text.
* **Ethical Sharing**: When releasing a dataset of malicious commands, document what it contains and the potential risks. Researchers consuming the dataset should be warned if any commands could accidentally execute harmful actions (for example, a command like rm -rf / is dangerous if someone ran it blindly). In published datasets, it’s good practice to include a disclaimer that the data is for defensive/security research only, and any misuse is not endorsed by the creators. Additionally, consider the impact: sharing attacker TTPs helps defenders, but could it aid less-skilled malicious actors? Generally, command-line lists alone are unlikely to enable new attacks (attackers already know them), whereas withholding such data would hurt defensive research more. Still, this balance is worth contemplating especially if the dataset includes novel or not widely known attack techniques.

## Summary

In summary, there are several rich sources for malicious command-line data – from open repositories by the security community to custom collections via honeypots and malware analysis. These datasets come in various formats (raw event logs, lists of commands, scripts, JSON records) and often include labels aligning with frameworks like ATT&CK. Using a mix of real-world and synthetic data can provide comprehensive coverage for research, but it’s crucial to handle all data ethically and legally. By leveraging these resources, defenders and researchers can improve detection of malicious CMD, PowerShell, and Terminal usage and better understand how attackers operate on the command line.

## Sources

* Splunk Attack Data – Curated attack logs (Windows Sysmon, etc.) on GitHub
* OTRF Security Datasets – Adversary emulation logs in JSON format
* Atomic Red Team by Red Canary – Library of malicious command tests mapped to ATT&CK
* Malicious PowerShell Script Dataset – Research collection of PS scripts from GitHub, sandboxes, etc., including obfuscated variants
* Cowrie Honeypot Data (CyberLab) – Real attacker SSH commands captured over 9+ months (academic dataset on Zenodo)
* Splunk/EDR Logs for Malicious CMDs – Example detection using EDR data for long suspicious commands
* CmdCaliper Research – Discussion of dataset generation via LLMs vs real attack command data
* SentinelOne Labs – Examples of macOS Terminal commands abused by malware (chmod, chown with MITRE technique mapping)
* Ethical and legal analysis of sharing security data – need for privacy, handling malware code carefully.

🤝 Meetings

**Meetings**

# Raz Issac: 16.3.2025

Attentdees: Aviad, Isaac

Record:
<https://drive.google.com/drive/u/0/folders/1Rzy-JmvTFKbgBi9_g53wsNAW0bqxE1iJ>
<https://drive.google.com/drive/u/0/folders/1Wr9E8taKejxdaydHropvC3rfTf5Lhpg0>

NotebookLM: <https://notebooklm.google.com/notebook/e36379e5-590a-40e1-ae96-47a0bafe39b9>

Summary:

במהלך הפגישה, אביעד ורז דנו בדרכים שונות לאתר מידע על שורות פקודה של תהליכים (process command line) עבור צורך מסוים, ככל הנראה אימון מודל או ניתוח נתונים.

בתחילת השיחה, אביעד ציין שדיבר עם עומרי מצוות פלטפורם, והם הציעו לו לבדוק את **אלסטיק סרצ' (Elasticsearch)**, מאחר שכל המידע מהטרנספרנסי (Transparency) נשלח לשם. רז הבהיר כי **אלסטיק סרצ' שומר נתונים רק עד שלושה ימים אחורה**, מה שאביעד מצא כמגבלה משמעותית.

רז הציע לאביעד לבדוק את **"סייד צ'אנל" (side channel)** בביג קוורי (BigQuery), שלדבריו **שומר נתונים עד שלוש שנים אחורה ומכיל מידע מכל הלקוחות**. אביעד הביע עניין רב באפשרות זו, מאחר שהיא נראית הרבה יותר מתאימה מבחינת היקף הזמן ומקורות המידע. רז הסביר שהסייד צ'אנל אכן מיועד לצורך אימונים ומכיל דטה מכל הלקוחות.

השניים דנו בקצרה על ההבדל בין **סינגל טננט (single-tenant) למולטי-טננט (multi-tenant)**, כאשר במולטי-טננט הדטה מהאנדפוינט (endpoint) עובר דרך הטרנספרנסי ומשם לאלסטיק סרצ'. רז ציין כי בארוספייק (Aeroscope), הנתונים נרשמים לפי שם לקוח, מה שמקשה על שליפת נתונים מקרוס לקוחות. לכן, צוות הסקיוריטי פיתח את הסייד צ'אנל בביג קוורי.

האתגר הבא היה **למצוא את המידע הרצוי בתוך ביג קוורי**. רז ציין שהוא זוכר שהמידע נמצא בתוך משהו שנקרא VFP, אך לא היה בטוח באיזו טבלה ספציפית. הם דנו בכמות המידע העצומה בביג קוורי, שמגיעה למיליארדי רשומות ולמאות טרה-בייט. רז הזהיר מפני **העלויות הגבוהות של סריקת נתונים בביג קוורי**, כאשר כל טרה-בייט סרוק עולה כ-6 דולר. הוא הדגיש את החשיבות של עבודה זהירה על טבלאות דמה קטנות לפני הרצת שאילתות על כמויות גדולות של מידע.

השניים בחנו את ממשק המשתמש של ביג קוורי על מנת לנסות לאתר את שדה ה-"process command line". הם ראו שיש טבלה עם כ-21 מיליארד רשומות, ובחנו את הסכמה של טבלאות שונות, כולל טבלה עם שמות של פרוססים. עם זאת, שדה ה-"process command line" לא נמצא באופן ישיר בסכמה. רז העריך שהוא עשוי להיות כלול בתוך שדה אחר.

\*\* היה בחברה בחור בשם שיר ירושלמי שכבר עזב את החברה שיכול לעזור לנו להבין איך למצוא את המידע של process command line ב-BigQuery.

בהמשך, אביעד העלה את האפשרות של **גישה ישירה לאלסטיק סרצ' דרך קוד פייתון** כדי למשוך את המידע. רז **התנגד לכך בתוקף**, והבהיר שהוא לא ייתן גישה ישירה לפרודקשן מחשש לפגיעה במערכת. הוא הציע **חלופה**: שאביעד יכתוב קוד פייתון שירוץ באופן מקומי, ידגום את המידע הרצוי, ורז יריץ את הקוד הזה בסביבת דב (dev) בשעות לא עמוסות ויספק לאביעד את התוצאות. רז הדגיש את הצורך בקוד בטוח, שניתן לעצירה והמשך, ואף הציע לתעד את התהליך.

השיחה עברה לדון בארכיטקטורה של אלסטיק סרצ' וכיצד לגשת למספר רב של אינדקסים השייכים לאותו לקוח. רז הסביר כי **כל לקוח מחזיק שלושה אינדקסים עיקריים (Benign, Persistent, Malop)**, אך בפועל ישנם אינדקסים מפוצלים רבים בשל מגבלות גודל. הוא הסביר את קונספט ה**אליאסים (aliases)**, שמאפשרים להתייחס לקבוצת אינדקסים כאילו היו אינדקס אחד, ובכך מפשטים את הגישה לנתונים של לקוח מסוים.

אביעד תהה כיצד לקבל רשימה של כל האינדקסים הקיימים. רז הציע להשתמש בפקודת **curl מול ה-API של קיבנה (Kibana)** כדי לקבל את רשימת האינדקסים. הוא אף הציג דוגמאות לשימוש בפקודות curl עם פרמטרים כמו -V, -H, ו---present s כדי לקבל את המידע בפורמט טבלאי וממוין. השניים דנו בשאלת האותנטיקציה מול קיבנה בעת שימוש ב-curl.

*GET \_cat/indices?v*

*GET \_cat/aliases?v*

אביעד הביע בלבול לגבי הצורך לעבור על מספר רב של URL-ים של קיבנה. רז הבהיר כי **חיבור ל-URL אחד של קיבנה מאפשר גישה לכל המידע בקלאסטר**. הוא ציין שישנם כ-30 קלאסטרים של אלסטיק סרצ', אך הדגיש כי אביעד יצטרך להתמקד בכתיבת קוד שירוץ באופן מקומי ורז ידאג להרצה מול כל הקלאסטרים.

בסיום הפגישה, רז **חזר והמליץ לאביעד לבדוק לעומק את נושא הסייד צ'אנל מול צוות הדאטה אינג'נירינג (Hadas's team, במיוחד עומרי ואורן)**, מאחר שהוא עשוי להכיל כבר את כל המידע הדרוש בצורה מסודרת ולחסוך לאביעד ולצוות משאבים רבים. אביעד אישר שהוא כבר דיבר עם עומרי אך יבדוק את הנושא שוב. רז הדגיש את החשיבות של הבנת מהות הסייד צ'אנל, אילו נתונים מגיעים אליו ולאן.

לסיכום, הפגישה התמקדה באיתור נתוני שורות פקודה. מספר אפשרויות נדונו, כאשר האפשרות המועדפת על רז היא שאביעד יכתוב סקריפט פייתון בטוח ויעיל שרז יריץ בסביבת דב. עם זאת, רז הדגיש מספר פעמים את הפוטנציאל של הסייד צ'אנל בביג קוורי כפתרון יעיל יותר ודחק באביעד להשקיע מאמץ נוסף בחקירת אפשרות זו לפני המשך פיתוח סקריפטים.

BigQuery Side Channel:
<https://console.cloud.google.com/bigquery?ws=!1m4!1m3!3m2!1sside-channel-env-deaeaf5c!2sglobal_data_prod>

הקוד שמאכלס את ה-side channel של ה-BigQuery
<https://github.com/cybereason-labs/research/blob/python3/sidechannel/gcf/main.py>

# Ofir Tal: 5.3.2025

Attentdees: Aviad, Ofir

Record: <https://drive.google.com/drive/u/0/folders/1h_H1rq7D6vmcmyUBW991BCtyMkI4npFS>

NotebookLM: <https://notebooklm.google.com/notebook/2909addb-e907-485a-a760-38d06c95f437>

Summary:

במהלך הפגישה, הנושא המרכזי היה **הבנת אופן פעולת שורת הפקודה (Command Line) בהקשר של יצירת תהליכים (Processes) וכיצד ניתן לנצל מידע זה לזיהוי פעולות זדוניות (Malicious)**. הדוברים הסכימו כי **כל תהליך שמתחיל במערכת מלווה בשורת פקודה, גם אם היא ריקה (אין פרמטרים)**. הודגש כי **יש להבחין בין פקודות שורת פקודה שמפעילות תהליך חדש לבין פקודות פנימיות של CMD שאינן יוצרות תהליכים חדשים** (כגון cd, dir, copy). נכון לעכשיו, **איסוף המידע מתמקד בפקודות שמפעילות תהליכים חדשים**.

הצדדים דנו ב**פרויקט שמטרתו לזהות פקודות זדוניות**, וההנחה הראשונית הייתה להתמקד בסוג הפקודות הראשון, שכן מידע לגביהן כבר נאסף. עלתה סוגיית **השגת נתונים (Data) לצורך בניית מערך נתונים (Dataset) של פקודות זדוניות ותמימות**. אחת האפשרויות שנדונו הייתה **איסוף נתוני שורות פקודה מלקוחות החברה**. דובר על כך שרוסלן כבר סיפק מידע חלקי בנושא (200 רשומות לערך), אך צוין כי **היקף המידע עשוי להיות עצום ולגרום לקריסת מערכות אם לא יבוצע בצורה מבוקרת**. אופיר הציע את אפשרות לבצע שאילתות (Queries) ישירות על מאגר הנתונים (Data Lake) של הלקוחות.

בנוגע ל**תיעוג (Tagging) הנתונים כזדוניים או תמימים**, עלה כי **המידע שנאסף מהלקוחות אינו מתויג באופן אוטומטי**. פתרון אפשרי הוא **להריץ את חוקי האבטחה (Security Rules) הקיימים של החברה על נתוני שורות הפקודה ולאחר מכן לתייג את הפקודות שהחוקים מזהים כחשודות**. עם זאת, הועלה החשש כי גישה זו עלולה להוביל למודל שבעיקר מזהה איומים שהמערכת כבר יודעת לזהות (אביעד).

כדי **להוסיף ערך מעבר ליכולות הזיהוי הקיימות**, נדונה האפשרות להשתמש ב**מאגרי קוד פתוח (Open Source Repositories) של חוקי שורות פקודה זדוניות**. כמו כן, עלה הרעיון של שימוש ב**מודלים של שפה גדולים (LLM)** שיכולים להבין את ההקשר של פקודה ולזהות פעילות זדונית גם אם היא כוללת שינויים קלים שמטרתם לעקוף כללים ספציפיים. נבחנה בקצרה גם האפשרות של שימוש ב**מאגרי וקטורים (Vector Stores)** כפתרון RAG להשוואת פקודות חדשות לפקודות ידועות.

הוסבר כי **חוקי האבטחה הקיימים מוגדרים בפורמט מסוים וניתנים להמרה לשפות שאילתה שונות (כמו סיגמה) המתאימות למאגרי נתונים שונים**.

בצד המעשי של **השגת הנתונים**, הוסכם כי **יש לפנות לרוסלן לעזרה בשליפת נתוני שורות פקודה ייחודיות (Distinct) מהלקוחות**, תוך הקפדה על הגבלת כמות השאילתות כדי למנוע עומס על מערכות הלקוחות. הוערך כי **כמות הנתונים הנדרשת לבניית מערך נתונים משמעותי עשויה להגיע למאות מיליוני רשומות**, בהתחשב בהערכה של שכיחות נמוכה יחסית של פקודות זדוניות. הוצע **למקד שאילתות גם לתהליכים שסומנו כ"חשודים" (Suspicious) במערכת**, מה שעשוי להגדיל את הסיכוי למצוא פקודות זדוניות.

בנוסף לנתונים מלקוחות, הועלה רעיון **לנצל מאגרי מידע חיצוניים של סקריפטים זדוניים (Malicious Scripts)**. ההצעה הייתה **לנתח סקריפטים אלה ולחלץ מהם את שורות הפקודה שמפעילות קבצי הרצה (.exe) עם הפרמטרים שלהם**, תוך התעלמות משורות אחרות כגון פקודות echo. כמו כן, הוזכר השימוש בפרמטר -C בפקודת PowerShell להרצת קוד מקודד ישירות משורת הפקודה, כנקודה רלוונטית לזיהוי פעילות זדונית.

בסיום הפגישה, הוחלט להמשיך בהתכתבות כדי לתאם את המשך הפעולות.

* CMD line Type1: a command line that inits a Process. Data which is already collected from customers.
* CMD line Type2: a command that is inserted to a cmd.exe. NOT COLLECTED AT ALL
* Focus only on execution of processes
* Offir’s recommendation:
  + …
  + Open source repositories of suspicious commands lines to catch.
  + Extract commands lines from customers. DI - customers data lake.
  + Ask Ruslan Rustchev to extract distinct process command line from customers. Limited query not to crash the system. 1 to million.
  + Query targeted to malicious ‘suspicious’

# Ruslan: 4.3.2025

Attentdees: Aviad, Ruslan

Record: <https://drive.google.com/drive/u/0/folders/1MeMbxhPKnLBwJTm6hijKcLOSEL2sYyn1>

NotebookLM: <https://notebooklm.google.com/notebook/e12a12fc-1c54-421e-b4d4-8dfd7160b484>

Summary:

This audio excerpt captures a meeting between Aviad and Ruslan where they discuss extracting malicious command-line data for a project.

The conversation begins with Ruslan showing Aviad the results of a query. Ruslan explains that the output includes a timestamp, the query name, the URL indicating the environment and the number of results returned, and a parsed command line extracted from the first result. He clarifies that the number next to "cmd" (like 19) indicates the number of command IDs in that specific result set.

Ruslan then explains how to parse the JSON data to find the actual command lines. Aviad needs to go into the "result" section, then to a specific GUID, and within that GUID, under "process" and then "command line," he will find the command. More specifically, the command line is located under "values" within the "filter data" associated with the GUID. Ruslan believes this structure should be consistent across the different GUIDs, at least in the data he sent.

Aviad confirms his understanding of how to extract the command lines. He then asks what it means if a raised event occurs when there are, for example, 19 commands, and Ruslan clarifies that **if a malop (malicious operation) is triggered, it means all the associated command lines in that set are considered malicious**. Ruslan elaborates that the query he ran pivots on "melo process" (a process that triggered a malop) and then looks for associated processes with a command line that is "cmd.exe," meaning every command line returned in that context has an associated malop.

Ruslan also mentions that this information can be checked in the SCS UI. He points out that some of the malops might be based on custom rules set by the environment owner, which could potentially lead to overly broad detections.

Aviad acknowledges that the data is not extensive but is a starting point. He inquires about the possibility of extracting more data for a longer period, noting the decreasing number of results in subsequent lines (19, 16, 12, 10). Ruslan explains that **he is hesitant to run very broad queries on their production hunting system because it is volatile and lacks an active maintainer, increasing the risk of crashing it and losing their hunting capabilities for paying customers**. This is his primary concern.

Ruslan suggests that if Aviad has his own hunting framework, he might be able to assist. He expresses a willingness to try and expand the data in the next few days but cannot promise anything that might jeopardize their hunting platform. He mentions that a more reliable, previous system called Cyber API could handle such data generation outside of regular hunting schedules, but this capability is currently limited to MDR customers and cannot be executed against the wider customer base, a limitation he has raised multiple times. Ruslan asks for patience.

Aviad thanks Ruslan for his time and efforts, stating that expanding the data would be beneficial. Ruslan reiterates that he will try to gradually expand the data, perhaps by a year, to see the increase in results, as the current execution did not take much time. However, he cautions that **they might hit data retention limitations on the platform, as it's uncertain how long command-line data remains queryable**.

Aviad clarifies that if they query and save the data on their side, retention limits on the platform shouldn't be an issue, as the data would be preserved locally. Ruslan confirms that his concern about retention is specifically regarding the availability of the data on the cyber platform they are querying from, as they do not store the data dynamically but query it from the detection server, where it is only available for a limited time.

Aviad expresses his understanding and thanks Ruslan again. Ruslan offers further help with hunting for data but emphasizes the need to be cautious due to the limitations and volatility of their current tool. Aviad concludes by stating he will continue working with the received data, and they will stay in touch.

# Rafi: 26.2.2025

Attentdees: Inbar, Aviad, Rafi

Summary:

* Extract from VirusTotal
* We can start by exploring the problem for Windows as we have more data,
  But, at the end, it would be more beneficial to solve it for MacOS
* We should also build a Command Line Normalizer/Cleaner that should deal with obfuscation techniques.
* Rafi showd us a very obfuscated malicious script. It can be cached on high entropy.
  <https://raw.githubusercontent.com/danielbohannon/Invoke-DOSfuscation/refs/heads/master/Samples/STATIC_1-of-4_Out-DosConcatenatedCommand.txt>
* Please schedule a meeting with Ofir Tal (might be a little bit challenging as he moved to Japan recently), to see if he can help with getting CMD convicted data from the fileless and BEP engines. According to Rafi, we can focus on the customers: AXA, Mitsubishi Chemical. taking all commands and with some manual work, getting to the interesting malicious ones.
* He also mentioned that in VirusTotal behaviour tag, according to ‘ransomware’/’malware’ we can take all the commands, you can consult with Ofir Tal or Eli Salem regarding that filtering if you need to.

# Eli Salem: 26.2.2025

Attentdees: Inbar, Aviad

Summary:

* Detection of malicious commands from:
  + CMD
  + Powershell
* Ruslan will retrieve commands from customers that raised MALOP.
  Meands that the dataset we get represents only commands that were already recoginzed by Cybereason. However, we would like to catch extra.
* Atomic Red Team
* Dataset Generation:
  + Use Caldera (free) to simulate attacks => cmd commands
  + Download from VT malicious BAT files. Extract commends.
  + Extract data from customers:

ℹ️ Relevant Info

**Information**

# Information

* MAL-CL<https://github.com/3CORESec/MAL-CL>
* Microsoft Defender for Endpoint uses advanced machine learning models to block malicious command lines and protect against a wide variety of threats, including ransomware and living off the land binary (LOLBin) attacks. Defender for Endpoint uses the **CommandLineBerta**, a model that evaluates suspicious command lines to determine the probability that they are malicious. If they are classified as malicious, they are blocked.
  <https://x.com/MsftSecIntel/status/1894447267504849020?t=rP9JxnLbgvavSZL2uXe8Ww&s=31>
  <https://techcommunity.microsoft.com/blog/microsoftdefenderatpblog/block-malicious-command-lines-with-microsoft-defender-for-endpoint/4373943>
* —--
* Rafel Ivgi
  + Command Line MLAV
  + <https://www.revshells.com/>
  + <https://wadcoms.github.io/>
  + <https://lolbas-project.github.io/>
  + Static Version:
    <https://github.com/SigmaHQ/sigma/tree/master/rules/windows/process_creation>
  + <https://amsi.fail/>
  + <https://jsfuck.com/>
  + <https://github.com/danielbohannon/Invoke-DOSfuscation>
  + —
  + Why do we need a command line normalizer?
    Detecting the powershell obfuscation techniques for malicious commands:
    - PowerShell Execution Argument Obfuscation (& How It Can Make Detection Easier!)
      *Invoke-Obfuscation*, a tool for generating obfuscated PowerShel
      <https://www.danielbohannon.com/blog-1/2017/3/12/powershell-execution-argument-obfuscation-how-it-can-make-detection-easier>
    - Pulling Back the Curtains on **EncodedCommand** PowerShell Attacks
      <https://unit42.paloaltonetworks.com/unit42-pulling-back-the-curtains-on-encodedcommand-powershell-attacks/>
* Oded Waiser
  + [https://learn.microsoft.com/en-us/windows/security/application-security/application-co[…]or-business/design/microsoft-recommended-driver-block-rules](https://learn.microsoft.com/en-us/windows/security/application-security/application-control/app-control-for-business/design/microsoft-recommended-driver-block-rules)
  + <https://github.com/magicsword-io/LOLDrivers/blob/main/detections/sigma/driver_load_win_vuln_drivers.yml>
  + <https://lolad-project.github.io/>
  + <https://dl.acm.org/doi/fullHtml/10.1145/3471621.3471858>
  + פה יש רשימה של קומנדים שמריצים בpt בדרך כלל:
  + <https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1059.001/T1059.001.md>
  + <https://github.com/0xfke/Malware-Detection-and-Analysis-using-Machine-Learning>
  + <https://github.com/Kiinitix/Malware-Detection-using-Machine-learning>
  + <https://github.com/Kunal-Attri/Malware-Detection-ML-Model>
  + <https://cloud.google.com/blog/topics/threat-intelligence/obfuscated-command-line-detection-using-machine-learning/>

✅ Tasks

**Tasks**

* ~~Add to hosts file to allow access to VT:~~
  + #0.0.0.0 [virustotal.com](http://virustotal.com/)
  + #0.0.0.0 [www.virustotal.com](http://www.virustotal.com/)
  + #::1 [virustotal.com](http://virustotal.com/)
  + #::1 [www.virustotal.com](http://www.virustotal.com/)
* ~~Ask~~ ~~Shon Avri~~ ~~to grant access to VT Entrprise.~~
* ~~Create a VM for cmd\_classification~~
* **Generate a dataset of malicious CMD commands:**
  + Review <https://github.com/3CORESec/MAL-CL/tree/master/Descriptors/Other/CleanWipe>
    The idea for this project stemmed from our analyses of threat intel reports where we were able to identify that, most of the time, threat actor activities were leveraging **LOLBINs** and "free" tools to perform their actions.

    In our analyses it became evident that the same command-line arguments **and tools were being used in the majority of adversary activity**. With this in mind we decided to document these common use cases and provide actionable context for the blue team.
  + Extract malicious scripts or command lines from VT
  + ChatGPT Deep Research on collecting

💡 Possible Solutions

**Solutions**

# Classic ML-Based Solution

* **Feature Extraction:**
  + Based on keywords relevant to malicious intents: elsas, pykatz, mimikatz
  + Detect framework
* **Solution:**
  + A first layer ML classifier provides a maliciousness score for a single command.
    - Different models for CMD, Powershell
  + A seconds upper layer is sending one command line to the first layer, and holds the history of all commands and their maliciousness score.
  + The system should “see” the whole “story” of what happened and the session and has the information:
    - The User that execute the command
    - The parent process who execute the command
* **Proc:**
  + Relatively easy to implement.
  + Computationally acceptable.
* **Cons:**
  + We should define a knowledge-based features for each attack we know. It might not be good for new attacks. However, if we define general statistic features which extract metadata on commands, such as command length, num of params, etc, it might be good enough for generalization.

# KNN Classifier based on signatures

Use KNN to classify commands.

The features

# RAG-Based Solution

Upload all benign and malicious commands into a RAG vectorstore. For each command to classify we may extract the most near commands and take a majority vote for classification.

* **Proc:**
  + The solution may find the distance between commands even if there is a variance between commands.
* **Cons:**
  + It requires using a good enough LLM, but it might be heavy to run locally.
