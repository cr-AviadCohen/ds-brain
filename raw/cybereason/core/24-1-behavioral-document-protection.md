## Behavioral document protection analysis


The Cybereason platform first identifies documents that contain

code, such as macros, and then analyzes the potential behavior of


the identified macros. If a macro within a document is detected as

malicious, the document is immediately quarantined.


The Cybereason platform analyzes documents when they are

accessed, such as when they are written to disk, which ensures


that all such documents are analyzed before any application can

load them.


The Cybereason platform empowers security analysts to

investigate and hunt by collecting and providing detailed


information about document-related risks. This information applies

both to documents that contain threats that the Cybereason


platform has already detected or prevented and to any document

that includes code, even if the Cybereason platform eventually


classifies the code as non-malicious.


Behavioral document protection is part of the Cybereason


platform's Anti-Malware solution, which analyzes every file as it is

being accessed. Anti-Malware is also used for Signature-based


analysis. Behavioral document protection is available with on
access scans, but is not available with on-demand and scheduled


scans.


Note


If the **Anti-Malware > Signatures mode** is set to **Disabled**,

Behavioral document protection continues to collect data but


does not prevent malicious documents from running. For more

details, see When do you use Behavioral Document


Protection.

## Behavioral Document Protection AI


The Cybereason platform utilizes a machine learning algorithm to


analyze documents to identify if they contain malicious macros.


The machine learning algorithm is based on a deep neural


network to provide data driven and automated selection of rules to

provide enhanced protection from malicious macros contained


within documents.


For more information on how to manage Behavioral


[Documentation Protection AI, see Set the Behavioral Document](https://nest.cybereason.com/s/knowledge-base?article=24-1-set-the-behavioral-document-protection-ai-modes&language=en_US#set-the-behavioral-document-protection-ai-modes)

[Protection AI Modes (/s/knowledge-base?article=24-1-set-the-](https://nest.cybereason.com/s/knowledge-base?article=24-1-set-the-behavioral-document-protection-ai-modes&language=en_US#set-the-behavioral-document-protection-ai-modes)


[behavioral-document-protection-ai-modes&language=en_US#set-](https://nest.cybereason.com/s/knowledge-base?article=24-1-set-the-behavioral-document-protection-ai-modes&language=en_US#set-the-behavioral-document-protection-ai-modes)

[the-behavioral-document-protection-ai-modes).](https://nest.cybereason.com/s/knowledge-base?article=24-1-set-the-behavioral-document-protection-ai-modes&language=en_US#set-the-behavioral-document-protection-ai-modes)


If a sensor policy contains sensors on versions earlier than 22.1.80


and also sensors on versions 22.1.80 and later, your Cybereason

environment uses both Rule-Based Behavioral Document


Protection and Behavioral Document Protection AI. The type of

Behavioral Document Protection that the Cybereason platform


uses is based on the sensor version:


For sensors on versions earlier than 22.1.80, sensors **only** use


Rule-based Behavioral Document Protection.

For sensors on versions 22.1.80 until 22.1.28X/23.1.83, if you


enabled Behavioral Document Protection AI for your

environment, sensors **only** use Behavioral Document


Protection AI. If you did not enable Behavioral Document

Protection AI, the sensor use **only** Rule-based Behavioral


Document Protection.

For sensors on versions 22.1.28X/23.1.83 and later, sensors


**only** use Behavioral Document Protect AI.

## Rule-Based Behavioral Document


Behavioral Document Protection utilizes over 100 Yara rules to


analyze documents to identify if they contain malicious macros.


These Yara rules are developed by the Cybereason security


research team based on the latest security intelligence to protect

your environment from attack from malicious macros contained


within documents.


For more information on how to manage Rule Based Behavioral


[Documentation Protection, see Set the Rule-Based Behavioral](https://nest.cybereason.com/s/knowledge-base?article=24-1-set-the-rule-based-behavioral-document-protection-modes&language=en_US#set-the-rule-based-behavioral-document-protection-modes)

[Document Protection Modes (/s/knowledge-base?article=24-1-](https://nest.cybereason.com/s/knowledge-base?article=24-1-set-the-rule-based-behavioral-document-protection-modes&language=en_US#set-the-rule-based-behavioral-document-protection-modes)


[set-the-rule-based-behavioral-document-protection-](https://nest.cybereason.com/s/knowledge-base?article=24-1-set-the-rule-based-behavioral-document-protection-modes&language=en_US#set-the-rule-based-behavioral-document-protection-modes)

[modes&language=en_US#set-the-rule-based-behavioral-](https://nest.cybereason.com/s/knowledge-base?article=24-1-set-the-rule-based-behavioral-document-protection-modes&language=en_US#set-the-rule-based-behavioral-document-protection-modes)


[document-protection-modes).](https://nest.cybereason.com/s/knowledge-base?article=24-1-set-the-rule-based-behavioral-document-protection-modes&language=en_US#set-the-rule-based-behavioral-document-protection-modes)

## Behavioral Document Protection


The type of Behavioral Document Protection available is


dependent on the sensor version:


Versions earlier than 22.1.105: Only rule-based Behavioral


Document Protection is available.

Versions 23.1.x through 23.1.4x: Rule-based Behavioral


Document Protection is the default. AI-based Behavioral

Document Protection can be made available by opening a


[Technical Support (/s/support) case.](https://nest.cybereason.com/s/support)

Version 23.1.8X and higher: Rule-based and AI-based


Behavioral Document Protection are both available in the UI.

Customers can enable one or the other, or both. If both are


enabled, rule-based Behavioral Document Protection is used


for sensors earlier than 22.1.28X or 23.1.8X. AI-based


Behavioral Document Protection is used for sensors 22.1.28X

and 23.1.8X and later.

## When do you use Behavioral Document


When Behavioral document protection is enabled, documents are

analyzed in one of the following scenarios:






|Scenario|Details|
|---|---|
|A user attempts to download or open a<br>Microsoft Offce document, and<br>Signature-based analysis scans the<br>document|If the<br>Signatures<br>scan detects<br>malware,<br>Cybereason<br>performs an<br>action based<br>on the<br>Signatures<br>mode.<br>If the<br>Signatures<br>scan does not<br>detect<br>malware,<br>Behavioral<br>document<br>protection<br>analyzes the<br>document for<br>the existence<br>of malicious<br>macros, and<br>Cybereason<br>performs an<br>action<br>according to<br>the Behavioral<br>document<br>protection<br>mode.|


|Scenario|Details|
|---|---|
|A user opens a Microsoft Offce<br>document, and Cybereason collects<br>data on the document as part of the<br>Non-executable fle data collection<br>(/s/knowledge-base?article=24-1-<br>confgure-additional-endpoint-data-<br>collections&language=en_US#confgure-<br>additional-endpoint-data-collections)<br>feature|This scenario<br>occurs only when<br>**Non-executable**<br>**fle data**<br>**collection** is set to<br>**On**, and one or<br>more of the<br>following options<br>is selected:<br>**Word**<br>**documents**<br>**Excel**<br>**spreadsheets**<br>**PowerPoint**<br>**fles**<br>Note<br>In this<br>scenario,<br>Behavioral<br>document<br>protection<br>continues to<br>collect data<br>but does not<br>prevent<br>malicious<br>documents<br>from running.<br>In this<br>scenario, the<br>**Signatures**<br>mode under<br>**System >**<br>**Policies**<br>**Management**<br>**> Create/Edit**<br>**Policy > Anti-**<br>**Malware** is set<br>to**Disabled**,<br>and the<br>Behavioral<br>document<br>protection<br>mode is set to<br>**Detect**.|


**Scenario 1 example**


1. An organization is using Cybereason with the following


settings:


The **Anti-Malware > Signatures mode** is set to **Disinfect**

or **Quarantine** .


The **Behavioral document protection** mode is set to

**Quarantine** .


The **Behavioral document protection** sensitivity level is

set to **Aggressive** .


2. A user receives an email that contains a Microsoft Office


document as an attachment. The document includes


malicious macros that are invisible to the user.

3. The user double-clicks the attachment.


4. Cybereason triggers Behavioral document protection to check


for malicious macros.


5. Cybereason quarantines the document.


For a list of actions that Cybereason takes if **Anti-Malware >**


**Signatures mode** is set to a value other than **Quarantine**, see

[Behavioral document protection modes and Signatures modes](https://nest.cybereason.com/s/knowledge-base?article=24-1-set-the-rule-based-behavioral-document-protection-modes&language=en_US#behavioral-document-protection-modes-and-signatures-modes)


[(/s/knowledge-base?article=24-1-set-the-rule-based-behavioral-](https://nest.cybereason.com/s/knowledge-base?article=24-1-set-the-rule-based-behavioral-document-protection-modes&language=en_US#behavioral-document-protection-modes-and-signatures-modes)

[document-protection-modes&language=en_US#behavioral-](https://nest.cybereason.com/s/knowledge-base?article=24-1-set-the-rule-based-behavioral-document-protection-modes&language=en_US#behavioral-document-protection-modes-and-signatures-modes)


[document-protection-modes-and-signatures-modes).](https://nest.cybereason.com/s/knowledge-base?article=24-1-set-the-rule-based-behavioral-document-protection-modes&language=en_US#behavioral-document-protection-modes-and-signatures-modes)


**Related Detections:**


The Cybereason platform triggers a **Malicious document**

Endpoint Protection MalOp with the **Quarantined** detection status.


The Cybereason platform triggers a **Document contains macro**
Evidence. For a list of Evidences, see the File and Image file


[element under Feature Values per Element (/s/knowledge-base?](https://nest.cybereason.com/s/knowledge-base?article=query-api-token-query-elements-and-features-version-232148-and-later&version=#feature-values-per-element)

[article=query-api-token-query-elements-and-features-version-](https://nest.cybereason.com/s/knowledge-base?article=query-api-token-query-elements-and-features-version-232148-and-later&version=#feature-values-per-element)


[232148-and-later&version=#feature-values-per-element).](https://nest.cybereason.com/s/knowledge-base?article=query-api-token-query-elements-and-features-version-232148-and-later&version=#feature-values-per-element)


The Cybereason platform triggers a **Document contains autorun**


**malicious macro** suspicion For a list of Suspicions, see the File
[and Image file element under Feature Values per Element](https://nest.cybereason.com/s/knowledge-base?article=query-api-token-query-elements-and-features-version-232148-and-later&version=#feature-values-per-element)


[(/s/knowledge-base?article=query-api-token-query-elements-and-](https://nest.cybereason.com/s/knowledge-base?article=query-api-token-query-elements-and-features-version-232148-and-later&version=#feature-values-per-element)

[features-version-232148-and-later&version=#feature-values-per-](https://nest.cybereason.com/s/knowledge-base?article=query-api-token-query-elements-and-features-version-232148-and-later&version=#feature-values-per-element)


[element).](https://nest.cybereason.com/s/knowledge-base?article=query-api-token-query-elements-and-features-version-232148-and-later&version=#feature-values-per-element)

**Scenario 2 example**


1. An organization is using Cybereason with the following


settings:


[The Non-executable file data collection (/s/knowledge-](https://nest.cybereason.com/s/knowledge-base?article=24-1-configure-additional-endpoint-data-collections&language=en_US#configure-additional-endpoint-data-collections)
[base?article=24-1-configure-additional-endpoint-data-](https://nest.cybereason.com/s/knowledge-base?article=24-1-configure-additional-endpoint-data-collections&language=en_US#configure-additional-endpoint-data-collections)


[collections&language=en_US#configure-additional-](https://nest.cybereason.com/s/knowledge-base?article=24-1-configure-additional-endpoint-data-collections&language=en_US#configure-additional-endpoint-data-collections)

[endpoint-data-collections) feature is enabled](https://nest.cybereason.com/s/knowledge-base?article=24-1-configure-additional-endpoint-data-collections&language=en_US#configure-additional-endpoint-data-collections)


The **Anti-Malware > Signatures mode** is set to **Disabled**

The **Behavioral document protection** mode is set to


**Detect** .

The **Behavioral document protection** sensitivity level is


set to **Aggressive** .



