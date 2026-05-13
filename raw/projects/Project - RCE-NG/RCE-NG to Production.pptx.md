# RCE-NG to Production.pptx

<!-- Slide number: 1 -->
# RCE-NG

Data Science Team

### Notes:
RCE-NG for Production – raw informationhttps://docs.google.com/document/d/1xYlV6ZiVhkpt8o7LS7pOO4fe_TXbl-Ja7aVUe-tkAGc/edit?tab=t.0

<!-- Slide number: 2 -->
# Risk Chain Engine (RCE) - Workflow
GUI
Data lakes

Observe
Connectors
Drool
RCE
“D3” SOC
Chronicle

### Notes:
https://cybereason.atlassian.net/wiki/spaces/XDR/pages/3806004172/Risk+Chain+Engine+RCE
XDR Dashboard

<!-- Slide number: 3 -->
# Risk Chain Engine (RCE) Solution - Drawbacks
Based on static rules to correlate detections:
Not robust - Cannot catch correlations that are not backed by rules.
Not scalable - over 4.2K rules imposible to maintain and scale.
Very High False Positives:
US
EU
Asia

![](GoogleShape557p79.jpg)

![](GoogleShape558p79.jpg)

![](GoogleShape556p79.jpg)

### Notes:
https://cybereason.atlassian.net/wiki/spaces/XDR/pages/3806004172/Risk+Chain+Engine+RCE
XDR Dashboard

<!-- Slide number: 4 -->
# Risk Chain Engine (RCE) Solution - Drawbacks
Correlations has no explanation at all or Raw logs ⇒ Avg. of 8 hour to triage per case.
MalOps complexity is low:
Few cross-vendor malops.
Few multi-step attacks malops.
Very complicated code ⇒
No maintenance for features.
No new rules are being added.

### Notes:
https://cybereason.atlassian.net/wiki/spaces/XDR/pages/3806004172/Risk+Chain+Engine+RCE
XDR Dashboard

<!-- Slide number: 5 -->
# RCE-NG

RCE - NG

1

2

3

4

5

![](GoogleShape597p81.jpg)

![](GoogleShape594p81.jpg)

![](GoogleShape600p81.jpg)

![](GoogleShape606p81.jpg)

![](GoogleShape603p81.jpg)
Normalization
Enrichment for correlation
Correlation
MalOp Detection
Enrichment for investigation
Enhanced Coverage and Precision with Allowlisting and Blocklisting Capabilities
In-depth Attack Phases Analysis
LLM and Human-Assisted Reinforcement

![](GoogleShape608p81.jpg)

![](GoogleShape611p81.jpg)

![](GoogleShape613p81.jpg)

### Notes:
The suggested solution here relies on the following 5 steps:
Step 1 and 2 - has to be implemented as a part of the RCE solution, was tested in other poc datasets, out of scope in this specific poc.
Step 3 - correlation itself, including data filtering logic + llm capabilities. this step is generating the correlation made of events, along with a detailed explanation of the attack narrative (which does not exist in the current RCE solution).
Step 4 - filtering the correlations made in the last step- the purpose is to create Malops only out of interesting enough correlations. the implementation used in the POC is rules based as in the current RCE solution, for parity. My team is already starting to work on the next ML solution.
Step 5 - today, gsoc analysts are unable to determine the verdict of a correlation Malop, without some additional data work crucial for the quality of their verdict. this makes their work harder and requires longer time for each triage process. In this step this data work will be made for the analyst and will enrich the Malop with all the necessary details for them to do their best work, in a smaller effort and triage time. This does not exist in the current RCE – an extra value.
we know that triage today rakes a few hours.
which is far from being the SLA we committed to 1:5:30.
these enrichment can bring us closer to manage to meet this committed SLA.
[[1 minute for the malop to pop
5 minutes for a TF/FP verdict
30 minutes for a response]]

this solution also allows us:
The ability to learn based on results (triage and studies made in the SR group) and integrate easily and automatically into the product
integrate custom rules - either by SR analysts or by the customers themselves.
explain why we generated the malop.

<!-- Slide number: 6 -->
# RCE-NG Architecture

![](GoogleShape623p82.jpg)
link to the pipeline

### Notes:

<!-- Slide number: 7 -->
# Proposed RCE-NG Solution - Advantages
Utilizing LLM to correlate unknown behaviors / groups of detection events
Backed up by rule lists for TP / FP known cases
Potential reduction of False Positives:
Filtering gateway based on Triaged Investigation (stage 3)
ML-based Malop-Worthy classification model (stage 4)
Reinforcement Learning – triaged malops are used to improve the model (Stage 5)

### Notes:

<!-- Slide number: 8 -->
# Proposed RCE-NG Solution - Advantages
More information for each MalOp
Smart, LLM-based, security-logic, and make-sense explanations of the correlated events → construct attack story (stage 3)
Enrich malops IOCs with Community reputation data (stage 5)
Relevant raw logs (stage 5)
Using LLM can cover more use-cases as it agnostic to vendors.
The RCE-NG is now developed from a production perspective (non-POC),for long-term support.

### Notes:

<!-- Slide number: 9 -->
# Proposed RCE-NG Solution - Advantages
Scalability:
The number of initial detection events  is significantly lower than the number of events
Reduction of LLM calls over time due to constantly improving Filtering Gateway with the combination of reinforcement learning
Processing Time:
Designed for near real-time
Aggregation and sliding window techniques applied
Deterministic gates enable predictable performance

### Notes:

<!-- Slide number: 10 -->
# Cost Evaluation
Cost Evaluation spreadsheet
OpenAI models reduction of costs over time.

![](GoogleShape648p86.jpg)
|  | GPT 4o | GPT 5 |
| --- | --- | --- |
| W/O optimization/filter gate 24h | $14,694.17 | $4,031.76 |
| [GPT-4o] cost per single correlation group | [GPT-5] cost per single correlation group | [GPT-4o] cost per avg correlation groups in 24h - Single Customer | [GPT-5] cost per avg correlation groups in 24h - Single Customer |
| --- | --- | --- | --- |
| $0.0793 | $0.02 | $3.9625 | $1.04 |
| $0.1843 | $0.05 | $1.1055 | $0.28 |
| $0.0280 | $0.01 | $0.2800 | $0.08 |
| $0.0143 | $0.00 | $0.2708 | $0.09 |
| $0.0118 | $0.00 | $0.0118 | $0.00 |
| $0.0105 | $0.00 | $0.0315 | $0.01 |

### Notes:

<!-- Slide number: 11 -->

Questions?

### Notes:
in the current implementation, all the architecture and the transitions between steps is very quick, a matter of seconds, which enables the gsoc analyst to meet the committed SLA of 1:5:30, which we don’t do today.
any questions?
