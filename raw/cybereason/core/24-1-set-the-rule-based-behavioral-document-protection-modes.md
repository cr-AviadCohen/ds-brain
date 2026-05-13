|Mode|Description|When to u<br>this settin|Col4|
|---|---|---|---|
|Disabled|Do not use Behavioral document protection<br>to prevent malicious documents.|You want t<br>collect dat<br>static fles<br>include<br>malicious c<br>such as m||


|Mode|Description|When to u<br>this settin|Col4|
|---|---|---|---|
|Detect|Detect integrated code in documents and<br>identify documents with malicious content,<br>such as malicious macros. Trigger MalOps<br>with information on the malicious content<br>that was detected.<br>Note<br>If**Anti-Malware > Signatures** mode is<br>set to**Disabled**, the Cybereason<br>platform collects document data as part<br>of the Non-executable fle data collection<br>(/s/knowledge-base?article=24-1-<br>confgure-additional-endpoint-data-<br>collections&language=en_US#confgure-<br>additional-endpoint-data-collections)<br>feature and triggers MalOps, evidences,<br>and suspicions. For more information,<br>see When do you use Behavioral<br>Document Protection ().|You w<br>identif<br>static f<br>that in<br>malicio<br>code,<br>as ma<br>You w<br>be aw<br>docum<br>that in<br>code (<br>non-<br>malicio<br>code)<br>use th<br>data fo<br>investi<br>and<br>huntin<br>more<br>inform<br>see<br>Behav<br>Docum<br>Protec<br>().||
|Prevent|Detect integrated code in documents and<br>prevent documents from running malicious<br>content, such as malicious macros. Trigger<br>Malops with information on the malicious<br>content that was prevented.|You want t<br>identify an<br>block stati<br>that includ<br>malicious c<br>such as m||
|||||


|Mode|Description|When to u<br>this settin|Col4|
|---|---|---|---|
|Quarantine|Detect integrated code in documents and<br>quarantine documents with malicious<br>content, such as malicious macros. Trigger<br>Malops with information on the malicious<br>content that was quarantined.<br>The Cybereason platform moves<br>quarantined documents to the**Quarantine**<br>folder. For more information, see Set Anti-<br>Malware Signatures mode (/s/knowledge-<br>base?article=24-1-set-the-anti-malware-<br>modes&language=en_US#set-anti-malware-<br>signatures-mode).|You w<br>quaran<br>static f<br>that in<br>malicio<br>code,<br>as ma<br>You w<br>be aw<br>docum<br>that in<br>code (<br>non-<br>malicio<br>code)<br>use th<br>data fo<br>investi<br>and<br>huntin<br>more<br>inform<br>see<br>Behav<br>Docum<br>Protec<br>().||
|Because of optimization algorithms, when you enable Behavioral<br>document protection, Cybereason might not re-scan documents<br>that**Anti-Malware > Signatures** classifes as benign until you<br>restart Cybereason.<br>Set the Behavioral document protection<br>sensitivity level<br>You can confgure the level of sensitivity that the Behavioral<br>document protection feature uses to handle suspicious code in<br>documents. The sensitivity levels determine whether the<br>Behavioral document protection feature is triggered and whether<br>to detect, prevent, and generate MalOps for suspicious<br>documents. This is different from the Behavioral document<br>protection mode, which determines how to handle the suspicious<br>document. For example, if the Behavioral document protection<br>mode is set to**Quarantine** and the sensitivity level is set to<br>**Cautious**:|Because of optimization algorithms, when you enable Behavioral<br>document protection, Cybereason might not re-scan documents<br>that**Anti-Malware > Signatures** classifes as benign until you<br>restart Cybereason.<br>Set the Behavioral document protection<br>sensitivity level<br>You can confgure the level of sensitivity that the Behavioral<br>document protection feature uses to handle suspicious code in<br>documents. The sensitivity levels determine whether the<br>Behavioral document protection feature is triggered and whether<br>to detect, prevent, and generate MalOps for suspicious<br>documents. This is different from the Behavioral document<br>protection mode, which determines how to handle the suspicious<br>document. For example, if the Behavioral document protection<br>mode is set to**Quarantine** and the sensitivity level is set to<br>**Cautious**:|Because of optimization algorithms, when you enable Behavioral<br>document protection, Cybereason might not re-scan documents<br>that**Anti-Malware > Signatures** classifes as benign until you<br>restart Cybereason.<br>Set the Behavioral document protection<br>sensitivity level<br>You can confgure the level of sensitivity that the Behavioral<br>document protection feature uses to handle suspicious code in<br>documents. The sensitivity levels determine whether the<br>Behavioral document protection feature is triggered and whether<br>to detect, prevent, and generate MalOps for suspicious<br>documents. This is different from the Behavioral document<br>protection mode, which determines how to handle the suspicious<br>document. For example, if the Behavioral document protection<br>mode is set to**Quarantine** and the sensitivity level is set to<br>**Cautious**:||


1. The Cybereason platform determines that the document


includes integrated code with a very high level of certainty.
2. Behavioral document protection is triggered, and the file is


quarantined.


Note


Behavioral document protection generates evidences and

suspicions as usual, regardless of the selected mode. For


example, if you select **Cautious** mode and Behavioral

document protection detects integrated code in a document,


the Cybereason platform generates evidences and suspicions

that can be used for visibility and analysis, without triggering


MalOps on those events.


Select one of the following options:








|Mode|Description|When to use this<br>setting|
|---|---|---|
|Cautious|Detect, prevent, and<br>trigger MalOps for only<br>those documents that<br>Cybereason<br>determines are<br>malware with a very<br>high level of certainty.<br>This is the setting with<br>the lowest sensitivity.|You want to detect<br>documents with<br>integrated code, but<br>want to avoid<br>handling many false-<br>positive results and<br>multiple MalOps that<br>report legitimate<br>documents.|
|Moderate|Detect, prevent, and<br>trigger MalOps for only<br>those documents that<br>Cybereason<br>determines are<br>malware with a high<br>level of certainty.|You want to detect<br>integrated code in<br>documents, and can<br>tolerate handling<br>some false-positive<br>results and some<br>MalOps that report<br>legitimate documents.|
|Aggressive|Detect, prevent, and<br>trigger MalOps for any<br>documents that<br>Cybereason<br>determines are likely to<br>include integrated<br>code. This is the<br>setting with the highest<br>sensitivity.|You want to detect<br>documents with<br>malicious code. You<br>prefer to assess and<br>analyze all false<br>positives, as well as<br>documents that are<br>likely, but not certain,<br>to be legitimate.|


## Add Behavioral document protection

You can exclude files or folders from Behavioral document


protection scans in the following ways:

Use Anti-Malware exclusions to exclude files or folders from


Behavioral document protection scans. For more information,
[see Exclude files and paths from Anti-Malware (/s/knowledge-](https://nest.cybereason.com/s/knowledge-base?article=24-1-add-exclusions-from-ngav-protection-legacy&language=en_US#exclude-files-and-paths-from-anti-malware)


[base?article=24-1-add-exclusions-from-ngav-protection-](https://nest.cybereason.com/s/knowledge-base?article=24-1-add-exclusions-from-ngav-protection-legacy&language=en_US#exclude-files-and-paths-from-anti-malware)
[legacy&language=en_US#exclude-files-and-paths-from-anti-](https://nest.cybereason.com/s/knowledge-base?article=24-1-add-exclusions-from-ngav-protection-legacy&language=en_US#exclude-files-and-paths-from-anti-malware)


[malware).](https://nest.cybereason.com/s/knowledge-base?article=24-1-add-exclusions-from-ngav-protection-legacy&language=en_US#exclude-files-and-paths-from-anti-malware)

Use Behavioral document protection rules to indicate specific


scenarios in which the Behavioral document protection scans

[should not be active. For more information, see Exclude](https://nest.cybereason.com/s/knowledge-base?article=24-1-add-exclusions-from-ngav-protection-legacy&language=en_US#exclude-behavioral-document-protection-using-a-rule-id)


[Behavioral document protection using a rule ID](https://nest.cybereason.com/s/knowledge-base?article=24-1-add-exclusions-from-ngav-protection-legacy&language=en_US#exclude-behavioral-document-protection-using-a-rule-id)

[(/s/knowledge-base?article=24-1-add-exclusions-from-ngav-](https://nest.cybereason.com/s/knowledge-base?article=24-1-add-exclusions-from-ngav-protection-legacy&language=en_US#exclude-behavioral-document-protection-using-a-rule-id)


[protection-legacy&language=en_US#exclude-behavioral-](https://nest.cybereason.com/s/knowledge-base?article=24-1-add-exclusions-from-ngav-protection-legacy&language=en_US#exclude-behavioral-document-protection-using-a-rule-id)

[document-protection-using-a-rule-id).](https://nest.cybereason.com/s/knowledge-base?article=24-1-add-exclusions-from-ngav-protection-legacy&language=en_US#exclude-behavioral-document-protection-using-a-rule-id)

## View Behavioral document protection

## modes in the Sensors screen


You can view endpoints' Behavioral document protection modes

and/or sensitivity levels for single endpoints or for groups of


endpoints in the **System > Sensors** screen.


The **Document protection status** column shows the


Behavioral document protection mode, specifying whether the

feature is enabled, disabled, and so on.


The **Document protection mode** column shows the

Behavioral document protection sensitivity level, specifying


whether the sensitivity level is aggressive, cautious, and so

on.


To display the Behavioral document protection modes or

sensitivity level, select **Columns** to the right of the sensors table,


and select the **Document protection status** column and/or the

**Document protection modes** column.


The Behavioral document protection modes are visible in the

sensors table.


The information in the **Document protection status** and


**Document protection modes** columns is also used as metadata
if you export the table to a CSV file.


Note


Sensors on versions earlier than 22.1.105 use Rule-Based


Behavioral Document Protection. Sensors on version 22.1.105

and later use Behavioral Document Protection AI.


If a sensor policy contains sensors on versions earlier than

22.1.105 and also sensors on versions 22.1.105 and later, your


Cybereason environment uses both Rule-Based Behavioral

Document Protection and Behavioral Document Protection AI. The


type of Behavioral Document Protection that the Cybereason

platform uses is based on the sensor version.


The Document protection status column and the Document

protection mode column show the mode and sensitivity level of a


specific endpoint. Depending on the sensor version the Document

protection status column and the Document protection mode


column can show different information for sensors on the same

policy.

## Behavioral document protection modes

## and Signatures modes


The Cybereason platform takes different actions according to the

Behavioral document protection mode and the **Anti-Malware >**


**Signatures** mode.


Note


The Behavioral document protection mode cannot be more

sensitive than the Signatures mode. For example, if **Anti-**


**Malware > Signatures mode** is set to **Detect**, the **Anti-**

**Malware > Behavioral document protection** mode can be


set to **Disabled** or **Detect**, but not to **Prevent** or **Quarantine** .


The following table specifies which Behavioral document


protection modes are allowed with each of the Signatures modes.






|Signatures<br>Mode|Allowed Behavioral document<br>protection mode|
|---|---|
|Disabled|Disabled<br>Detect|


|Signatures<br>Mode|Allowed Behavioral document<br>protection mode|
|---|---|
|Detect|Disabled<br>Detect|
|Prevent|Disabled<br>Detect<br>Prevent|
|Quarantine|Disabled<br>Detect<br>Prevent<br>Quarantine|
|Disinfect|Disabled<br>Detect<br>Prevent<br>Quarantine|







