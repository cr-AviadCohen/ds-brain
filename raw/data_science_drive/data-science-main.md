Org



General Knowledge
General Knowledge

# Sensor
Run on endpoint
Core – the legacy – currently in production.
Work with graph-based data stored in Transparency (TR), cost alot.
Detection engines:
VFP (Variant File Protection)
VPP (Variant Payload Prevention)
BEP (Behavioral Execution Prevention)
PRP (Predictive Ransomware Protection)
NGAV (Next-Generation Anti-Virus)
BDP (Behavioral Document Protection)
BDP AI
Fileless (PowerShell, .NET, VBScript, JavaScript)
Anti Ransomware (Canaries - legacy)
BitDefender AV Engine
AIAV – the new sensor.
Event-based (rather than graph-based) – saved money.
We didn’t deploy it as it does not support migration.
Maybe after Phoenix is deployed, we can start migrating to AIAV
# Backend
Core:
Transparency (TR) – holds the entire data in RAM.
Perspective (PR) – manages all the TR in the environment. Also responsible for the UI and API support.
Phoenix:
Multi-tenant – a single instance of a software application serves multiple customers.
Works faster than core
Works on local disk (instead of RAM), but is still faster than Core.
Uses:
RedPands – The Fast, Scalable, Kafka-Compatible Streaming Data Platform
ClickHouse – Fastest DB for Analytics
# XDR
Extended Detection and Response (XDR) is a cybersecurity technology designed to provide holistic threat detection, investigation, and response across multiple security layers. Its main purpose is to centralize and correlate security data from diverse sources, allowing security teams to detect, analyze, and respond to threats more effectively and efficiently.
Current:
Chronicle on GCP
Has a full suite, for example, IDM – very expensive.
Observe on Snowflake on Amazon.
Limited support, missing a few crucial features such as IDM.
New: Work over Phoenix
Using XIS or other technology for connecting 3rd party logs to Phoenix over the Phoenix scheme.
# Systems
Sage - Downloads data from VirusTotal daily.

Azure AI
Azure AI

Account:
Azure AI Foundry
For personal access, ask Shoshana Avni
Nitzan Milchin (also Shoshana Avni) has the permission to deploy models.
For any questions regarding Azure AI, one can talk to Azure’ integrator in israel asaf@aztek.co.il
Available Models:


Our Azure AI account:
Subscription Name: CR-AI
Subscription ID: 7663b00e-8f86-4f1f-a4ac-9bb724c220f7
Azure AI Foundry Service: Request for Quota Increase
Justification:
We are currently leveraging Azure AI Foundry Service to process and tag a large volume of data using LLMs—specifically, tens of thousands of individual requests as part of our research. At the current quota limits, this operation spans several weeks, introducing delays in downstream analysis and decision-making processes. An increase in quota would significantly accelerate our throughput, enabling us to complete these tasks in a fraction of the time. The increased capacity will be used responsibly. We anticipate this adjustment will substantially improve turnaround times and contribute to more timely insights and outcomes.
Azure Content Filtering
https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/content-filters#create-a-content-filter-in-azure-ai-foundry
https://customervoice.microsoft.com/Pages/ResponsePage.aspx?id=v4j5cvGGr0GRqy180BHbR7en2Ais5pxKtso_Pz4b1_xUMlBQNkZMR0lFRldORTdVQzQ0TEI5Q1ExOSQlQCN0PWcu
Security Knowledge
Security Knowledge

Security EPP
https://drive.google.com/drive/folders/1Lfo2sc97JirzqlyYju34OZrBz6jrR_UX
Security Research Group Training
