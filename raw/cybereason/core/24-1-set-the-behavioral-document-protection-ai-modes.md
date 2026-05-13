|Mode|Description|When to u<br>this settin|Col4|
|---|---|---|---|
|Disabled|Do not use Behavioral document protection<br>AI to prevent malicious documents.|You want t<br>collect dat<br>static fles<br>include<br>malicious c<br>such as m||
|Detect|Detect integrated code in documents and<br>identify documents with malicious content,<br>such as malicious macros. Trigger MalOps<br>with information on the malicious content<br>that was detected.<br>Note<br>If**Anti-Malware > Signatures** mode is<br>set to**Disabled**, the Cybereason<br>platform collects document data as part<br>of the Non-executable fle data collection<br>(/s/knowledge-base?article=24-1-<br>confgure-additional-endpoint-data-<br>collections&language=en_US#confgure-<br>additional-endpoint-data-collections)<br>feature and triggers MalOps, evidences,<br>and suspicions. For more information,<br>see When do you use Behavioral<br>Document Protection.|You w<br>identif<br>static f<br>that in<br>malicio<br>code,<br>as ma<br>You w<br>be aw<br>docum<br>that in<br>code (<br>non-<br>malicio<br>code)<br>use th<br>data fo<br>investi<br>and<br>huntin<br>more<br>inform<br>see<br>Behav<br>Docum<br>Protec||
|Prevent|Detect integrated code in documents and<br>prevent documents from running malicious<br>content, such as malicious macros. Trigger<br>Malops with information on the malicious<br>content that was prevented.|You want t<br>identify an<br>block stati<br>that includ<br>malicious c<br>such as m||
|||||


|Mode|Description|When to u<br>this settin|Col4|
|---|---|---|---|
|Quarantine|Detect integrated code in documents and<br>quarantine documents with malicious<br>content, such as malicious macros. Trigger<br>Malops with information on the malicious<br>content that was quarantined.<br>The Cybereason platform moves<br>quarantined documents to the**Quarantine**<br>folder. For more information, see Set Anti-<br>Malware Signatures mode (/s/knowledge-<br>base?article=24-1-set-the-anti-malware-<br>modes&language=en_US#set-anti-malware-<br>signatures-mode).|You w<br>quaran<br>static f<br>that in<br>malicio<br>code,<br>as ma<br>You w<br>be aw<br>docum<br>that in<br>code (<br>non-<br>malicio<br>code)<br>use th<br>data fo<br>investi<br>and<br>huntin<br>more<br>inform<br>see<br>Behav<br>Docum<br>Protec||
|Because of optimization algorithms, when you enable Behavioral<br>document protection, the Cybereason platform might not re-scan<br>documents that**Anti-Malware > Signatures** classifes as benign<br>until you restart the Cybereason sensor.<br>Set the Behavioral document protection<br>AI sensitivity level<br>You can confgure the level of sensitivity that the Behavioral<br>document protection AI feature uses to handle suspicious code in<br>documents. The sensitivity levels determine whether the<br>Behavioral document protection AI feature is triggered and<br>whether to detect, prevent, and generate MalOps for suspicious<br>documents. This is different from the Behavioral document<br>protection AI mode, which determines how to handle the<br>suspicious document. For example, if the Behavioral document<br>protection AI mode is set to**Quarantine** and the sensitivity level is<br>set to**Cautious**:|Because of optimization algorithms, when you enable Behavioral<br>document protection, the Cybereason platform might not re-scan<br>documents that**Anti-Malware > Signatures** classifes as benign<br>until you restart the Cybereason sensor.<br>Set the Behavioral document protection<br>AI sensitivity level<br>You can confgure the level of sensitivity that the Behavioral<br>document protection AI feature uses to handle suspicious code in<br>documents. The sensitivity levels determine whether the<br>Behavioral document protection AI feature is triggered and<br>whether to detect, prevent, and generate MalOps for suspicious<br>documents. This is different from the Behavioral document<br>protection AI mode, which determines how to handle the<br>suspicious document. For example, if the Behavioral document<br>protection AI mode is set to**Quarantine** and the sensitivity level is<br>set to**Cautious**:|Because of optimization algorithms, when you enable Behavioral<br>document protection, the Cybereason platform might not re-scan<br>documents that**Anti-Malware > Signatures** classifes as benign<br>until you restart the Cybereason sensor.<br>Set the Behavioral document protection<br>AI sensitivity level<br>You can confgure the level of sensitivity that the Behavioral<br>document protection AI feature uses to handle suspicious code in<br>documents. The sensitivity levels determine whether the<br>Behavioral document protection AI feature is triggered and<br>whether to detect, prevent, and generate MalOps for suspicious<br>documents. This is different from the Behavioral document<br>protection AI mode, which determines how to handle the<br>suspicious document. For example, if the Behavioral document<br>protection AI mode is set to**Quarantine** and the sensitivity level is<br>set to**Cautious**:||


1. The Cybereason platform determines that the document


includes integrated code with a very high level of certainty.
2. Behavioral document protection AI is triggered, and the file is


quarantined.


Note


Behavioral document protection AI generates evidences and

suspicions as usual, regardless of the selected mode. For


example, if you select **Cautious** mode and Behavioral

document protection AI detects integrated code in a


document, the Cybereason platform generates evidences and

suspicions that can be used for visibility and analysis, without


triggering MalOps on those events.


Select one of the following options:








|Mode|Description|When to use this<br>setting|
|---|---|---|
|Cautious|Detect, prevent, and<br>trigger MalOps for only<br>those documents that<br>the Cybereason<br>platform determines<br>are malware with a very<br>high level of certainty.<br>This is the setting with<br>the lowest sensitivity.|You want to detect<br>documents with<br>integrated code, but<br>want to avoid<br>handling many false-<br>positive results and<br>multiple MalOps that<br>report legitimate<br>documents.|
|Moderate|Detect, prevent, and<br>trigger MalOps for only<br>those documents that<br>the Cybereason<br>platform determines<br>are malware with a high<br>level of certainty.|You want to detect<br>integrated code in<br>documents, and can<br>tolerate handling<br>some false-positive<br>results and some<br>MalOps that report<br>legitimate<br>documents.|
|Aggressive|Detect, prevent, and<br>trigger MalOps for any<br>documents that the<br>Cybereason platform<br>determines are likely to<br>include integrated<br>code. This is the setting<br>with the highest<br>sensitivity.|You want to detect<br>documents with<br>malicious code. You<br>prefer to assess and<br>analyze all false<br>positives, as well as<br>documents that are<br>likely, but not certain,<br>to be legitimate.|


## View Behavioral document protection AI

## modes in the Sensors screen

You can view endpoints' Behavioral document protection AI


modes and/or sensitivity levels for single endpoints or for groups

of endpoints in the Cybereason UI, from the **System > Sensors**


screen.


The **Behavioral doc mode** column shows the Behavioral


document protection AI mode, specifying whether the feature

is enabled, disabled, and so on.


The **Behavioral doc sensitivity** column shows the Behavioral

document protection AI sensitivity level, specifying whether


the sensitivity level is aggressive, cautious, and so on.


To display the Behavioral document protection AI modes or


sensitivity level, select **Columns** to the right of the sensors table,

and select the **Behavioral doc mode** column and/or the


**Behavioral doc sensitivity** column.


The Behavioral document protection modes are visible in the


sensors table.


The information in the **Behavioral doc mode** and **Behavioral doc**


**sensitivity** columns is also used as metadata if you export the
table to a CSV file.


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


The Behavioral doc mode column and the Behavioral doc


sensitivity column show the mode and sensitivity level of a specific

endpoint. Depending on the sensor version these columns can


show different information for sensors on the same policy.

## Behavioral document protection modes

## and Signatures modes


The Cybereason platform takes different actions according to the


Behavioral document protection AI mode and the Anti-Malware >

Signatures mode.


Note


The Behavioral document protection AI mode cannot be more


sensitive than the Signatures mode. For example, if **Anti-**

**Malware > Signatures mode** is set to **Detect**, the **Anti-**


**Malware > Behavioral document protection** mode can be

set to **Disabled** or **Detect**, but not to **Prevent** or **Quarantine** .


The following table specifies which Behavioral document

protection AI modes are allowed with each of the Signatures


modes.






|Signatures<br>Mode|Allowed Behavioral document<br>protection mode|
|---|---|
|Disabled|Disabled<br>Detect|
|Detect|Disabled<br>Detect|
|Prevent|Disabled<br>Detect<br>Prevent|
|Quarantine|Disabled<br>Detect<br>Prevent<br>Quarantine|
|Disinfect|Disabled<br>Detect<br>Prevent<br>Quarantine|



