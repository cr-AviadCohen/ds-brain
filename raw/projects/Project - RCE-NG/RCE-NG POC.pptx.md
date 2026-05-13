# RCE-NG POC.pptx

<!-- Slide number: 1 -->
# RCE-NG POC

Data Science Team

### Notes:

<!-- Slide number: 2 -->
# POC Scope

RCE - NG

1

2

3

4

5

![](GoogleShape554p78.jpg)

![](GoogleShape551p78.jpg)

![](GoogleShape557p78.jpg)

![](GoogleShape563p78.jpg)

![](GoogleShape560p78.jpg)
Normalization
Enrichment for correlation
Correlation
MalOp Detection
Enrichment for investigation
Enhanced Coverage and Precision with Allowlisting and Blocklisting Capabilities
In-depth Attack Phases Analysis
LLM and Human-Assisted Reinforcement

![](GoogleShape565p78.jpg)

![](GoogleShape568p78.jpg)

![](GoogleShape570p78.jpg)

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

<!-- Slide number: 3 -->

![3d White people with dart and target. Success in business. (Provided by Getty Images)](GoogleShape578p79.jpg)
# POC Goals
Demonstrate an attack narrative that the current rule-based RCE solution fails to detect.(This scenario corresponds to the Hagiwara POC, which required custom rules for proper correlation.)
The attack narrative will showcase:
Cross-vendor activity
Multi-step progression (MITRE Attack chain)
A detailed explanation of the entire sequence
Enrichment of IOCs included in the narrative events, along with their verdicts (e.g. VT)
Identification of related non-detection events based on shared entities

New added value

### Notes:
The suggested solution was tested on multiple datasets, and a few different scenarios along the way.
Today, in this POC presentation I want to focus on a scenario that best showcases the abilities of this new solution.
For who of you that remembers, there was a scenario given to us by Hagiwara, asking to show that we are able to detect it. back at the time the RCE solution failed to detect the requested scenario, and new rules had to be written to show that we do detect the scenario.
This poc was running on the exact set of events, and furthermore, we pushed it even more and added some not-related events as an input to our logic, to see that we are able to not only detect the scenario, but also to exclude events that are unrelated to the attack scenario.
This scenario showcases detection of a full attack narrative, containing a few different MITRE steps from the mitre attack chain.
As I mentioned before, the logic also provides some additional value, beyond what we have today- a detailed explanation of the attack, and two different types of enrichment (one is the community reputation of the IOCs included in the attack, and the other is additional non-detection events that we believe may be related to the attack.)
these two enrichments help the analysts do their job more quickly and with a higher quality, we will take a look at these in a few slides.

<!-- Slide number: 4 -->
# The Scenario
Phishing emails sent with malicious attachments.
from email: protection318@icloud.com, IP: 158.220.101.4
targeting multiple users:
chen@acme-corp.com
bill@acme-corp.com
ana@acme-corp.com
Suspicious login activity with compromised credentials.
ana@acme-corp.com
192.168.1.1
Malware downloaded to host.
192.168.1.1 (source IP)
150.136.90.238 (destination IP)
Sharing of sensitive documents externally via BOX.

![](GoogleShape589p80.jpg)

![](GoogleShape590p80.jpg)

![](GoogleShape591p80.jpg)

![](GoogleShape592p80.jpg)

### Notes:
This is how the scenario itself looks like.
At the right side you can see the vendors from which the detection alert was raised.

<!-- Slide number: 5 -->
Original set of events
# Step 3 - Correlation
Correlation
phishing email
(Event 0)

correlation group
+
detailed explanation
Potential
Correlation
phishing email
(Event 0)
login activity
(Event 1)
Filtering Logic

Identities based
potential
correlation
group

LLM

Which events in the potential group are a part of the same attack narrative?
login activity
(Event 1)
phishing email
(Event 0)
malware downloaded
(Event 2)
malware downloaded
(Event 2)
login activity
(Event 1)
discovery evasion
(Event 3)
sensitive file was leaked
(Event 4)
malware downloaded
(Event 2)
sensitive file was leaked
(Event 4)
sensitive file was leaked
(Event 4)
Bitsadmin Activity
(Event 5)
phishing email
(Same recipient, different sender)
phishing email
(Same recipient, different sender)

### Notes:
We will start from the rce-ng point of view, using the new solution instead of the existing one.
We simulated 1+2, normalization and idm.
step 3 is the correlation engine itself.
Each box here represents a detection event that happened in a certain customer environment.
The first step contains a filtering logic that filtered out two detection events that are unrelated to the attack (the grey ones), based on the identities involved, which was previously tested to be correlated by RCE with no filtering.
In the second step here we are sending the reduced set of events to the LLM, which is able to also exclude that extra event that the filtering logic has kept as a potentially related event. (there are optimizations that can be made in order to reduce LLM calls and costs, currently we didn’t include these types of optimizations, they will be made in the engineering stage)

<!-- Slide number: 6 -->
# Step 3 - Correlation
Correlation potential: [0, 1, 2, 4, 6] (size: 5)
{
  "attack_narrative_1": {
    "explenation": "The attack begins with a phishing attempt targeting multiple users, including   ana@acme-corp.com, bill@acme-corp.com, and chen@acme-corp.com, from the email address email.protection318@icloud.com. This is followed by a high-risk login attempt for the user ana from Israel, indicating potential unauthorized access using valid credentials. Subsequently, suspicious activity is detected with a possible malicious executable file downloaded from a WordPress site, originating from the IP address 192.168.1.1, which matches the source IP of the high-risk login event. Finally, there is a violation of content workflow sharing policy, suggesting data exfiltration to a cloud account by the user ana, who shares the same username and IP address as the previous events.",
    "events": [0, 1, 2, 4]
  }
}

### Notes:
Here we see the detailed explanation that will be a part of the Malop.
This is an untouched, real LLM result.
These four marked parts demonstrates how similar it is to the intended scenario.
we can see that the LLM sais what the scenario was, in a very high similarity to the original scenario given to us.

<!-- Slide number: 7 -->
# Step 4 - MalOp Detection

Malop Candidate
Actual New Malop

correlation group
+
detailed explanation

correlation group
+
detailed explanation
phishing email
(Event 0)
phishing email
(Event 0)
Malop Worthy rule:
“has high severity event”
Passed as True
login activity
(Event 1)
login activity
(Event 1)
malware downloaded
(Event 2)
malware downloaded
(Event 2)
sensitive file was leaked
(Event 4)
sensitive file was leaked
(Event 4)

### Notes:
Step 4 is essentially a gate - passing only correlations that are important and significant enough to become a real malop.
Here we can see that one of the Malop detection rules has declared the correlation to be Malop Worthy, therefore an actual new malop will be generated in the system.

<!-- Slide number: 8 -->
# Step 4 - MalOp Detection

The current "Malop Worthy" logic is rule-based.
Inherited from the existing RCE solution.

The Data Science team started working on a more robust solution ⇒
Machine Learning–driven approach.

### Notes:
As we mentioned earlier, the current malop worthy decision logic is rule based as a parity to the existing RCE solution.
But the data science team is already starting to look at the data to build a robust ML solution for that step as well.

<!-- Slide number: 9 -->
# Step 5 - Enrichment for investigation

correlation group
+
detailed explanation

correlation group
+
detailed explanation
phishing email
(Event 0)
IOC 0
reputation  verdict
phishing email
(Event 0)
login activity
(Event 1)
login activity
(Event 1)
IOC 2
reputation + verdict
malware downloaded
(Event 2)
malware downloaded
(Event 2)
sensitive file was leaked
(Event 4)
sensitive file was leaked
(Event 4)
Raw Log Event
not a detection event

### Notes:
going forward to step 5
As I mentioned before, today gcos analysts are unable to determine the verdict of a correlation Malop, without some additional data work crucial for the quality of their verdict. this step makes their work harder and requires longer time for each triage process, which brings us to not meeting the 1:5:30 sla we committed to. In this step we do this data work for the analyst - we basically enrich the Malop with all the necessary details for them to do their best work, in a smaller effort and triage time. This does not exist in the current RCE – an extra value.
We see here two types of enrichment done:
One is taking IOCs existing in the events of the correlation,
The other is an event that is not a detection, but is possibly related to the attack narrative and can help seeing the bigger picture.

<!-- Slide number: 10 -->
# Step 5 - Enrichment for investigation

![](GoogleShape676p86.jpg)
IOC VT verdict

### Notes:

in this example, the generated correlation contains a file downloaded. here we have the verdict of that file as it appears in VT.
In the UI we can select what we’d like to show.

<!-- Slide number: 11 -->
# Step 5 - Enrichment for investigation

![](GoogleShape683p87.jpg)
raw log event

### Notes:
in this example, the chosen raw log is selected to be shown because the same sender from the attack narrative sent an email to another  user in the organization.
not a detection event, but might indicate on a bigger story hidden.
This is the raw log as it exists in the Observe, in the UI we can select what we’d like to show.

<!-- Slide number: 12 -->
# Suggested pipeline

![](GoogleShape693p88.jpg)
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

<!-- Slide number: 13 -->

Questions?

### Notes:
in the current implementation, all the architecture and the transitions between steps is very quick, a matter of seconds, which enables the gsoc analyst to meet the committed SLA of 1:5:30, which we don’t do today.
any questions?
