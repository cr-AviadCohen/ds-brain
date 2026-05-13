# RCE NG.pptx

<!-- Slide number: 1 -->

![](GoogleShape685g329fa3b5dda_0_1344.jpg)
# RCE-NG
May 2025

### Notes:

<!-- Slide number: 2 -->
# Solution

RCE - NG

1

2

3

4

5

![](GoogleShape723g336271fa27c_0_61.jpg)

![](GoogleShape720g336271fa27c_0_61.jpg)

![](GoogleShape726g336271fa27c_0_61.jpg)

![](GoogleShape732g336271fa27c_0_61.jpg)

![](GoogleShape729g336271fa27c_0_61.jpg)
Normalization
(Out Of Scope)
Enrichment for correlation
Correlation
MalOp Detection
Enrichment for investigation
Enhanced Coverage and Precision with Allowlisting and Blocklisting Capabilities
In-depth Attack Phases Analysis
LLM and Human-Assisted Reinforcement

![](GoogleShape734g336271fa27c_0_61.jpg)

![](GoogleShape737g336271fa27c_0_61.jpg)

![](GoogleShape739g336271fa27c_0_61.jpg)
‹#›
‹#›

### Notes:
Normalization - udm, idm
Enrichment for correlation - MITRE, Identity, Severi, victim/performer
Correlation for MalOps = limited. E1 + E2
Malop Worthy? Detection of MalOp on Correlation G1:E1+E2 =? MalOp
Enrichment for investigation G1 (En attach)
*LLM and Human-Assisted Reinforcement
*Enhanced Coverage and Precision with Allowlisting and Blocklisting Capabilities

<!-- Slide number: 3 -->
# Suggested pipeline

![](GoogleShape746g34e6b9a81c9_0_0.jpg)
link to the pipeline

### Notes:
1 normalization 1 generic schema that is unified - xdr, edr all types of events- we want to be able to go back you this data in a later step to enrich.
2 1# enrichment of row data and classification
3 כרגע הגייטס הם רק של פילטור איכותני, אין פה התייחסות לאופטימיזציה של עלויות
פרומפט יכולים לנקות פרייבט דאטה לפני ששולחים ל llm
4 מתחילים בחוקים הקיימים, פתרון סטטי, כל קבוצה מסתכלים האם היא מאלופ וורדי על בסיס חוקים סטטים- כל מאלופ שנוצר ב rce יווצר גם פה מינוס ה fpr.
לא סיימנו את התהליך של הלימוד בסט הזה של החוקים, היינו רוצים שבהמשך יהיה פה משהו חכם יותר עם llm יכולת למידה / מכיר תבניות / למה זה מאלופ וורדי / אנליסט מטייב אותו
5 מה שהיה חסר ברסא כל החיים- נותן אנריצמנט (בין אם זה מאירועי סייבריזן הraw data) בחזרה לאנליסט שיקצר משמעותית את זמני הטריאז ויספק מידע נוסף. גם ההסבר יגיע יחד עם הקורלציה מה שיקל על האנליסט ולא קיים היום.
5/5 אנליסט יכול להחליט אם tp או לא ולהזין את הפילוטורים שלנו שיש פה בעצם תהליך למידה הסוק אנליסט מלמד את המערכת

<!-- Slide number: 4 -->
# RCE-NG POC

### Notes:

<!-- Slide number: 5 -->
# POC Scope
POC Data
24 hours of customers data (2025-02-25)
Detections were enriched by MITRE Att&ck and Severity
Cross Identity enrichment
Correlation Potential
for each customer, correlation potential was calculated based on selected identities fields:
source_ip, remote_ip, source_ad_sid, remote_ad_sid, source_computer_name, remote_computer_name, recipient_email_address, sender_email_address, source_user_sid, target_user_sid, source_username, target_username, url, link_url, url_domain_name
LLM Correlation Engine
each customer’s correlation potential groups were sent to gpt 4o to determine correlations and provide a narrative.
‹#›

### Notes:
Japan

<!-- Slide number: 6 -->
# XDR Correlation Detection Engine example

![](GoogleShape765g359a909ad4b_1_0.jpg)
‹#›

### Notes:

<!-- Slide number: 7 -->
# Next Phases
POC’s Correlations were processed by our new “MalOp worthy”,
Currently triaged and analyzed by SR for:
Harden Malop-Worthiness logic/rules to lower FPR
include more filtering rules prior to the LLM

Evaluate and compare Self-Hosted Fine-Tuned Models vs. API-Based LLMs, in terms of costs, quality, privacy and maintenance, for the specific task, data volumes and our goals.
‹#›

### Notes:
starting with API-based models to validate use cases quickly, then exploring open-source options for long-term sustainability or specific constraints (e.g., privacy, cost, control). The choice depends on what we value most at each stage — speed, cost, control, or performance.

<!-- Slide number: 8 -->
# Moving forward in replacing RCE
MVP for parity:

![](GoogleShape779g336271fa27c_0_41.jpg)

### Notes:

<!-- Slide number: 9 -->
# Self-Hosted Fine-Tuned Models
vs.
API-Based LLMs

### Notes:

<!-- Slide number: 10 -->
| Category | Self-Hosted Open-Source LLM | API-Based LLM (e.g., GPT/Claude/Gemini) |
| --- | --- | --- |
| Reasoning Performance | Varies by model and tuning; may require significant effort | Typically high out-of-the-box, especially for complex tasks |
| Fine-Tuning Flexibility | Full control over fine-tuning and model behavior | Limited to prompt tuning or selective fine-tuning if supported |
| Infrastructure Needs | Requires compute, storage, and MLOps setup | None; fully managed by provider |
| Total Cost of Ownership | Higher upfront and maintenance costs; lower per-query cost | Lower startup cost; cost scales with usage |
| Deployment Speed | Longer; involves setup, evaluation, and tuning | Immediate; ready to integrate via API |
| Scalability | Dependent on internal infrastructure | Scales automatically with demand |
| Data Control & Privacy | Full data control; can run fully on-prem or private cloud | Depends on provider’s policies; often encrypted and compliant |
| Maintenance Load | Internal responsibility for updates, patches, and scaling | Offloaded to the provider |
| Talent Requirements | Requires in-house ML expertise and DevOps resources | Minimal; integration-focused engineering |
‹#›

### Notes:

<!-- Slide number: 11 -->

### Notes:
