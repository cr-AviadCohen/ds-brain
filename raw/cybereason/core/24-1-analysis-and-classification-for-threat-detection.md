The Cybereason platform's malicious activity models include:






|Model|Details|
|---|---|
|**Malware**<br>**models**|This model looks for tell-tale signs of<br>known and unknown malware, malicious<br>tools, and zero-day exploits that attackers<br>use to get an initial foothold in your<br>environment.|
|**Privilege**<br>**escalation**<br>**models**|This model examines user and process<br>behavior to identify an attacker's attempt<br>to gain a higher level of access to<br>resources in your environment.|
|**Lateral**<br>**movement**<br>**models**|This model identifes attackers trying to<br>expand their foothold in your environment<br>by using legitimate tools, a method that<br>traditional security programs cannot<br>detect.|
|**Command and**<br>**control models**|This model detects network traffc between<br>your environment and an attacker's<br>command and control servers. This model<br>identifes behaviors such as domain<br>generated algorithms (DGA).|
|**Data exfltration**<br>**models**|This model identifes the attacker's attempt<br>to exfltrate data or cause other types of<br>damage in your environment.|
|**Ransomware**<br>**models**|This model identifes malware that<br>encrypts fles in an attempt to extort users.|



The platform continues to evaluate and add additional models as


additional techniques and attacker behaviors are found.


Once the CMC Engine analyzes the behavior, the engine


compares the behavior patterns found against the platform's

proprietary detection rules to generate evidence, suspicions, and


Malops that you can investigate and remediate.

## Threat intelligence enrichment


For events found throughout your organization's environment, the


Cybereason platform must determine a number of things,

including (but not limited to):


1. Is the process/file/module/service associated with this event


malicious or benign?


2. If the event is malicious, is it a known item (such as known


malware or a known malicious framework)?

3. What else is this event/Element doing?


How does the Cybereason platform reach this conclusion?


For items that are known, such as known malware or known


malicious files, a key element in the Cybereason platform's

decision is the real-time querying of global threat intelligence


sources. The Cybereason Global Threat Intel server receives

reports from sources such as Virus Total. These reports from


additional threat intelligence sources are useful as they are used

by many security vendors and represent an aggregation of


intelligence from a wide range of sources. If a majority of vendors
determine a file to be malicious, it most likely is, and security


products must make use of this information.


However, some reports might contain conflicting information, and


different vendors may disagree.

## Platform classification through artificial


In addition to information from threat intelligence sources, the

Cybereason platform uses a statistical machine learning


classification algorithm that is trained over large sets of data and

analyst feedback. The algorithm gives scores to the information


contained in threat intel reports, enabling the Global Threat Intel
server to reach a confident classification, even when vendors


disagree.


The algorithm includes a set of complex calculations that:


Assess the accuracy of previous classifications
Address the strengths and weaknesses of specific vendors


Perform sophisticated analysis of text tokens within the report

in order to understand the meaning behind each vendor's


verdict string. For example, if the report text includes the
string 'Bad Rabbit', this increases the likelihood that the file


will be classified as ransomware.


Use additional metadata from intel reports apart from vendor


verdicts


The result is an intelligent classification into a number of


categories, such as:


Malware


Hack tool

Ransomware


Unwanted (PUP)

Indifferent


This classification model provides a more detailed and nuanced
description of malicious events to reflect real world complexity, as


opposed to a simple 'Good/Bad' identification.


The accuracy of the classification improves over time, and the


algorithm is updated on a periodic basis based on new data. In

some cases, this means that the Cybereason platform


retroactively re-classifies a process that ran previously, based on

new data.

## Classification on the endpoint


On an endpoint machine, the Cybereason platform's NGAV
component uses artificial intelligence to classify file hashes as


malicious or benign. This machine learning algorithm analyzes file

properties and additional metadata to determine the likelihood that


the file is a new, unknown type of malware that has not yet been

discovered in global threat intel sources.


The Cybereason platform's NGAV's AI model is trained using the

results of the machine learning algorithm based on threat intel


sources. In this way, both the platform's threat intelligence and

NGAV components work hand in hand, using AI to prevent


malware before it can execute.

## Related resources


[IOC and threat intelligence feeds (/s/article/2454398)](https://nest.cybereason.com/s/article/2454398)


[How does Cybereason determine if an IP address or domain](https://nest.cybereason.com/s/article/14192)

[is malicious? (/s/article/14192)](https://nest.cybereason.com/s/article/14192)


[How Does Cybereason detect attempts to exploit a known](https://nest.cybereason.com/s/article/2403678)

[CVE? (/s/article/2403678)](https://nest.cybereason.com/s/article/2403678)



