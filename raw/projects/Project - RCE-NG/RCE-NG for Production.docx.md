# RCE-NG for Production.docx

RCE-NG for Production

* The RCE should serve the XDR.

# Current RCE:

* [https://cybereason.atlassian.net/wiki/spaces/XDR/pages/3806004172/Risk+Chain+Engine+RCE](https://cybereason.atlassian.net/wiki/spaces/XDR/pages/3806004172/Risk%2BChain%2BEngine%2BRCE)
* [XDR Dashboard](https://lookerstudio.google.com/u/0/reporting/004a49e9-e5b9-4550-8629-279459e7d125/page/p_d4zy0g13ad)
* The correlation engine is based on static rules – it is not robust and cannot catch correlations that are not hard-coded.
* High false positives:
  + US
  + ![](data:image/png;base64...)
  + EU
  + ![](data:image/png;base64...)
  + ASIA
  + ![](data:image/png;base64...)
* The True Positives are not really interesting:
  + No cross-vendor malops.
  + No multi-step attacks malops.
* Very complicated code.
* No maintenance (no adding rules)
* Correlations has no explanations at all – GSOC analyst hard to investigate.

# Suggested RCE-NG:

* Smart LLM-Based:
  + Correlation of detections into an attack story + explanation that make sense to GSOC analyst.
* Potential reduction of False Positives
  + Filtering gateway based on Triaged Investigation (stage 3)
  + ML-based Malop-Worthy classification model (stage 4)
* Reinforcement Learning – triaged malops are used to improve the model:
  + …
* Performance should be at least equivalent, probably better, than the current solution.
* Malop Enrichment (step 5):
  + \*\* In this step this data work will be made for the analyst and will enrich the Malop with all the necessary details for them to do their best work, in a smaller effort and triage time. **This does not exist in the current RCE – an extra value.**
  + Raw logs
  + Match IOCs with Community Reputation
* Scalability.
* Cost Evaluation (spread sheet)
  + GPT-5 costs less than GPT-4o
* Processing Time

The suggested solution here relies on the following 5 steps:

* Step 1 and 2 - has to be implemented as a part of the RCE solution, was tested in other poc datasets, out of scope in this specific poc.
* Step 3 - correlation itself, including data filtering logic + llm capabilities. this step is generating the correlation made of events, along with a detailed explanation of the attack narrative (**which does not exist in the current RCE solution**).
* Step 4 - filtering the correlations made in the last step- the purpose is to create Malops only out of interesting enough correlations. the implementation used in the POC is rules based as in the current RCE solution, for parity. My team is already starting to work on the next ML solution.
* Step 5 - today, GSOC analysts are unable to determine the verdict of a correlation Malop, without some additional data work crucial for the quality of their verdict. this makes their work harder and requires longer time for each triage process. In this step this data work will be made for the analyst and will enrich the Malop with all the necessary details for them to do their best work, in a smaller effort and triage time. **This does not exist in the current RCE – an extra value.**

**we know that triage today rakes a few hours.**

**which is far from being the SLA we committed to 1:5:30.**

**these enrichment can bring us closer to manage to meet this committed SLA.**

**[[1 minute for the malop to pop**

**5 minutes for a TF/FP verdict**

**30 minutes for a response]]**

**this solution also allows us:**

* **The ability to learn based on results (triage and studies made in the SR group) and integrate easily and automatically into the product**
* **integrate custom rules - either by SR analysts or by the customers themselves.**
* **explain why we generated the malop.**
