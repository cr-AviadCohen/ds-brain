Analysts should address events with High severity scores first, as


these are identified by the Cybereason platform as the most

threatening events. Medium events may not be as threatening to


your environment, or may not require immediate attention. Low

and Informational events are relevant for threat visibility and


provide additional context for an end-to-end attack story.


Important


The Cybereason Severity Score is meant as a guide for
analysts and are not definitive representations of how


threatening an event is to your organization.

## Severity score calculation


The Cybereason platform calculates a severity score based on the


following:


1. The threat activity's associated MITRE ATT&CK tactic,


technique, or sub-technique

2. Any actions that were taken by the other platform/product (if


any)

3. How often the event is reported (event prevalence)

## Threat activity


First, the platform assigns each suspicious event a threat activity

score based on the associated MITRE ATT&CK tactic, technique,


or sub-technique. An event's associated tactic or technique can

provide insight into the event's threat level, and the Cybereason


platform maps the behaviors accordingly.


For example, the Cybereason platform assigns phishing attempts


a Low threat score, as phishing occurs in the initial stage of an
attack, while exfiltration events receive a higher threat score as


they represent the most advanced attack stage where the attacker

gains or compromises data.


The following table provides general information on how specific

MITRE ATT&CK tactic categories map to severity levels. In some


cases, the threat activity is calculated differently for different

techniques and sub-techniques within a single tactic category.


|Tactic|Risk|
|---|---|
|Impact|High|
|Exfltration|High|
|Collection|Medium|


|Tactic|Risk|
|---|---|
|Persistence|Medium|
|Lateral Movement|Medium|
|Credential Access|Medium|
|Command and Control|Medium|
|Discovery|Medium|
|Privilege Escalation|Low|
|Defense Evasion|Low|
|Execution|Low|
|Initial Access|Low|
|Resource Development|Informational|
|Reconnaissance|Informational|

## Mitigation actions

After assigning a threat score, the Cybereason platform checks if

the reporting platform or product applied any mitigation actions.


Many of the platforms or products that integrate with Cybereason

XDR respond to behaviors based on the platform or product


features. If the other platform or product mitigated a threat, the

Cybereason platform reduces the event threat score. For example,


if your other platform or product quarantined a file in response to

the suspicious event, the Cybereason platform lowers event


overall severity score accordingly.

## Suspicious event prevalence


The Cybereason platform also takes into account event


prevalence: how often a particular event is being reported. For

example, the fact that an event is very common may reduce the


severity score, while a rare event might indicate that the detection

is more accurate and thus even increase the severity score in


some cases.

## Suspicious event severity examples


The following examples demonstrate how the Cybereason


platform may assign a specific severity score to a specific

scenario.


|Scenario|MITRE<br>ATT&CK|Thirdy-<br>party Tool<br>Action|Cybereason<br>Severity Score|
|---|---|---|---|
|A third-party<br>tool reported<br>that it<br>detected a<br>phishing<br>attempt in an<br>email in an<br>employee's<br>inbox.|Phishing|After<br>detection,<br>the third-<br>party tool<br>immediately<br>quarantined<br>any<br>associated<br>fles.|The Cybereason<br>platform initially<br>scores this event<br>as Low, as the<br>'Phishing' MITRE<br>technique is<br>considered an<br>initial stage of an<br>attack. In other<br>words, the attack<br>has not<br>progressed to<br>more dangerous<br>stages.<br>Because the<br>third-party tool<br>quarantined the<br>email, the<br>Cybereason<br>platform will<br>lower the score to<br>Informational, as<br>the risk was<br>already handled<br>by the third-party<br>tool.<br>Final score:<br>INFORMATIONAL|


|Scenario|MITRE<br>ATT&CK|Thirdy-<br>party Tool<br>Action|Cybereason<br>Severity Score|
|---|---|---|---|
|A third-party<br>tool reported<br>that it<br>detected a<br>targeted<br>phishing<br>attempt in the<br>CEO's inbox.<br>This scenario<br>represents a<br>'Spearphishing<br>attempt' and is<br>not common in<br>this<br>environment.|Phishing |<br>Spearphishing<br>attachment|None|While phishing<br>techniques by<br>themselves are<br>considered initial<br>stages of an<br>attack, attacks<br>customized for<br>specifc<br>individuals<br>(spearphishing)<br>are more<br>concerning. In<br>addition, the<br>prevelance of the<br>attempted attack<br>is low. These<br>factors cause the<br>Cybereason<br>platform to<br>assign this event<br>a Medium score.<br>Final score:<br>MEDIUM|
|A third-party<br>tool reported<br>that a user<br>noticed a<br>suspicious<br>login attempt.<br>This attempt<br>was<br>successful<br>and<br>represents the<br>'Valid<br>Accounts'<br>MITRE<br>technique. In<br>addition, the<br>prevelance of<br>this event is<br>low.|Valid<br>Accounts|None|Like scenario 2,<br>this event could<br>be considered a<br>Low-scoring<br>event, as the<br>'Valid Accounts'<br>technique<br>represents the<br>initial stage of a<br>potential attack.<br>However, since<br>this event is rare<br>in this<br>environment, the<br>Cybereason<br>platform<br>increases the<br>score to Medium.<br>Final score:<br>MEDIUM|


|Scenario|MITRE<br>ATT&CK|Thirdy-<br>party Tool<br>Action|Cybereason<br>Severity Score|
|---|---|---|---|
|A third-party<br>tool reported a<br>network event<br>with the 'Multi-<br>hop Proxy'<br>MITRE sub-<br>technique,<br>which was<br>prevalent in<br>the<br>environment.|Proxy | Multi-<br>hop proxy|The tool<br>denied<br>network<br>traffc|Although the<br>associated<br>MITRE sub-<br>technique could<br>represent the<br>Command and<br>Control stage of<br>an attack, the<br>fact that the tool<br>denied the traffc,<br>along with the<br>event's relative<br>prevelance<br>results in an<br>Informational<br>score.<br>Final score:<br>INFORMATIONAL|
