# IRCA POC - 2026.01.01.pptx

<!-- Slide number: 1 -->

![](GoogleShape625p2.jpg)
# IRCA POC
Data Science Team

### Notes:

<!-- Slide number: 2 -->
Challenges in Incident Response (IR)
Our IRCA Solution
IRCA Solution Architecture
Live Demo

### Notes:

<!-- Slide number: 3 -->
# Current Challenges in Incident Response
Human IR teams take hours to days to respond
SOC ticketing delays investigations
External IR teams face legal & financial hurdles
Human teams give recommendations, not direct actions

### Notes:
Hi all, thank you very much for joining this meeting.
I will start with the current challenges in Incident Response.
When a cybersecurity incident occur in an organization, it takes IR human teams hours to days to response.During that window, the risk increases.
In addition, SOC ticketing delays the investigation.
When finally the external IR team arrives, they face legal & financial hurdles.
At the end, the IR team provide only recommendations, they do not take actual actions.
Reports arrive as PDFs and checklists - the execution depends on other teams.
Only advices, without actions, prolongs the exposure.

<!-- Slide number: 4 -->
# Solution: AI-based Automated IRCA
AI-Generated Incident Response reports based on data from Cybereason product.
Triggered by critical malops (e.g., credential theft) or user request for CA.
An IR Report is generated quickly & automatically using AI, with minimal effort.
Use interactive AI-Agent for near immediate remediation response.

### Notes:
Our solution for that problem is: AI-based, automated Incident Response & Compromise Assessment
Our IRCA solution is triggered by critical malops (for example credential theft) OR by user request for Compromise Assessment.
Our solution provides a comprehensive Incident Response report (PDF), based on data from our product.
The IR report is generated relatively quickly, within 1-2 minutes, using AI, with minimal effort.
Finally, we apply an interactive AI-agent for near immediate remediation response, and depends on the capabilities of the EDR solution.

<!-- Slide number: 5 -->
# IRCA Architecture

![](GoogleShape652g3bc91fc2389_0_7.jpg)

### Notes:
Here I’ll show you the IRCA abstract architecture.
As I explained before, the system is triggered in two cases: 1) a critical malops, 2) User ask for CA.
We collect data from the endpoint machine, using Cybereason API (processes, malops, detection events | with timestamps) and cross-reference it (enrich it) with data from the Server – internal knowledge base (description of malops & detection events).
All the relevant raw data is now sent to AI analytics that generates to IR report.
The report is then saved as PDF into artifacts DB, and also sent to Cybereason API to be used later by the UI.
The IR report contains also recommendation steps and they are sent to the interactive AI agent, for response.
Draw.io plot: https://app.diagrams.net/?splash=0#G1caVqrv2WbVdR9JM_tPrvRHRqzPyYfQ0p#%7B%22pageId%22%3A%222QNm_1jnb87lQeNb1QMT%22%7D

<!-- Slide number: 6 -->
# Report Generation Prompt

![](GoogleShape659g3bc91fc2389_0_16.jpg)

### Notes:

<!-- Slide number: 7 -->
# Report Generation Prompt

![](GoogleShape666g3bc91fc2389_0_23.jpg)

### Notes:

<!-- Slide number: 8 -->

![](GoogleShape674g3bc91fc2389_0_30.jpg)
# Incident Response Report
Tell the story:
What happened on the machine?
Consequences
Provide clear remediation steps

### Notes:
The IR report comes to tell the full story of what happened on the endpoint machine, and what are the consequences.
The report also contains clear remediation steps.
On the right side you can see a demonstration of the report, as it designed in Figma.On the live demo later I will show you the full report we produced in our POC.

<!-- Slide number: 9 -->
# AI-Driven Response Actions
Depends on the customer Policy, utilizing Agentic AI for:
kill_process
quarantine_file
unquarantine_file
block_file
delete_registry_key
kill_prevent_unsuspend
unsuspend_process

### Notes:

<!-- Slide number: 10 -->
# Efficiency & Impact
Reduce reliance on human manual processes
Faster, more precise incident analysis
Standardized deliverables
Enable near immediate remediation if chosen.
Strengthen overall cyber defense posture

### Notes:

<!-- Slide number: 11 -->
# Limitations
We ran our POC on a research environment.

### Notes:
X machines.
Y actives users.
No real busy activity.
No much background noise.

<!-- Slide number: 12 -->
# Cost Estimation
Cost Estimation
Model Pricing (per token)
Average Tokens Per Request
TODO: what is most interesting here?
Single Request Cost
 GPT 4o
1M INPUT tokens		$5.00
1M OUTPUT tokens	$20.00

| IR Report - Request Prompt Size (Tokens) | 1,406 |
| --- | --- |
| IR Report - Request Data Size (Tokens) - MAX | 16,075 |
| IR Report - Request INPUT Tokens | 17,481 |
| IR Report - Request Estimated OUPUT tokens per | 5,000 |
| AI Agent - Request MAX number of Remediation Steps | 8 |
| AI Agent - Request INPUT Tokens | 524 |
| AI Agent - Request OUTPUT Tokens | 82 |
Cost of IR Report 	$0.072
Cost of AI Agent	$0.012
Total Cost		$0.084

 GPT 5

1M INPUT tokens		$1.25
1M OUTPUT tokens	$10.00

### Notes:
API pricing per token has been going down over time and most experts and leaders in the industry expect it to continue declining, due to Better hardware efficiency, Stronger competition, More model variants at cheaper tiers.
The rest of the calculation here is for gpt5, as it is not only better economics, but it also provides better performance and future support.

<!-- Slide number: 13 -->
# Cost Estimation
Cost Estimation
Single Request Cost
Annual Estimated Malops Amount
All customers / Endpoints
Annual Estimated Total Cost
~ $15,230

~ $25,095
~ 182K requests (Average)

~ 300K requests
(conservative estimate)
$0.084

### Notes:
we found that over 6 months, the amount of Malops was ±91K, deducing over 12 months is ±182K. (both EDR and BEP included).
Current average: ~182K requests. Rounded up to reflect peak usage and growth.

<!-- Slide number: 14 -->

![](GoogleShape737g3bc91fc2389_0_49.jpg)
# Cost Estimation
Cost Estimation

### Notes:
We made a cost evaluation of the IRCA solution, the presentation contains a link to the source Spreadsheet.
At the top of the table you can see the costs for 1M INPUT & OUPUT tokens, on both GPT-4o and GPT-5
Then we calculated the amount of data we send to the LLM (input) and the size of the response we get,For both IR report and the AI-agent.
From these numbers we calculated the cost for IR report & AI agent, separately, and together.
Lets focus on the GPT-5 cost per one single request, which is .084$You should multiply it by the number of requests we will send per day (and it is controllable).
Note also that the costs drop as LLM generation progress.GPT-5 costs dramatically less than GPT-4o, and we can assume that GPT-6 will costs even less than GPT-5.
GPT-5-mini/nano. We didn’t check it yet.
Additional costs:
Computations infrastructure -
Estimation of how many requests per month?
13 malop types | different infrastructures per region.
Using 120,000$ a year, we can support 5.5M endpoints, 2.5K customers – up to 300,000 requests per year.

<!-- Slide number: 15 -->

![](GoogleShape743g3928bbd50d6_0_578.jpg)
# LIVE DEMO

### Notes:

<!-- Slide number: 16 -->
# Live Demo Intro
For this IRCA demonstration we raised a dedicated environment, installed with the latest sensor, on which we execute a real attack scenario (dry-run for MITRE Exam).
MACHINE_NAME = ‘bb-win11-23h2’
START_TIME = 1754341200000
END_TIME= 1754514000000

### Notes:
https://docs.google.com/document/d/1TGQQtkWq0in9PWVcHhaCIT4LHjve2XzpUBGWssQ_R5Q/edit?tab=t.nna94ycq4plp

IRCA POC:
As I showed earlier in the IRCA architecture, there are 2 phases:
1) Data collection phase.
2) AI:
Automatic Generator of Incident Response Report
Automatic-Interactive Response
Now we will ask IRCA to collect the data from the target machine, within a chosen time-range, it will take about 20 seconds to complete.Next, we will generate an Incident Response report.
Data Collection
We are collecting all malops, detection events and critical processes from a specific machine, at a specific time range.
We collecting the data using multiple API requests.
Currently, there is no way to pull the data for a specific machine, we pull ALL malops, for ALL machines, from the environment, than filter them on the specific machine – it is not the optimal, but will be solved by creating a new API that allows getting malops from a specific machine.
We develop the data collection for the EDR, and we can adapt it, with minor changes, to any other products (e.g., XDR, Phoenix, etc.).
IRCA POC:
As I showed earlier in the IRCA architecture, there are 2 phases:
1) Data collection phase.
2) AI:
Automatic Generator of Incident Response Report
Automatic-Interactive Response
Now we will ask IRCA to collect the data from the target machine, within a chosen time-range, it will take about 20 seconds.Next, we will generate an Incident Response report.
Report Generation:
Report
We created the report using LLM (gpt-4o), and designed it according to the UI Figma.
The report includes the following sections:
Executive Summary:
A basic summary of what occurred in the incident
Narrative of Events:
Shows all of the MalOps that were involved in the incident (show link)
Impact Analysis:
How does the incident impact the machine?
Root Causes & Attack Chain:
This section is divided according to MITRE tactics (show link)
Remediation Recommendations:
Also divided based on the remediation capabilities of the platform (e.g., Kill process, quarantine, etc.)
Artifacts Triggering Detection MalOps:
This includes all of the IOCs that were involved in the incident – we can see here the paths/hashes of the artifacts.
Next steps:
General recommendations
Interactive Remediation
We created an AI agent (agentic workflow using Langraph) that parses the natural language remediation requests, extracts the parameters, and builds the API request for remediation.
The agent asks for user approval for each remediation step.

<!-- Slide number: 17 -->

### Notes:

<!-- Slide number: 18 -->

![](GoogleShape764g3bc91fc2389_0_310.jpg)
# Title
text
TITLE
text

### Notes:
