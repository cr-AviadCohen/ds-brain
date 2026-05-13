## Detection logic and suspicions and

Suspicions and evidence use a similar logic-based approach. For


the platform to generate a suspicion, the platform must also

generate evidence as part of the suspicion logic.


For evidence, the same logic-based approach is used. However,

evidence may take Element properties into account as well as


classification. For example, evidence may require a certain file
hash value identified as malicious by threat intelligence, but also a


specific process name, or classification of the process as

malicious.


Suspicions may take Element properties into account also, but the

detection logic of suspicions usually requires evidence and places


less emphasis on Element properties.


In addition, most evidence and suspicions require fewer detection


"conditions" than MalOps, because they are a lower level

detection and may or may not be malicious. You will still want to


view evidence and suspicions, but you need to understand and

analyze these evidence and suspicions to determine whether they


are malicious.


For example, the platform detects Facts F1, F2, and F3.


Individually, these facts are benign. However, F1 and F2 together

could indicate malicious activity. The platform generates evidence


E1. For F3, the platform generates evidence E2. After you review

these evidence, you decide that E1 is benign and E2 is malicious.


Likewise, the platform detects evidences E1 and E2. Although E1

is benign by itself, the presence of E2 at the same time could


indicate malicious activity. The platform generates suspicion S1.

The platform also generates suspicion S2 for evidence E2. After


you review these suspicions, you determine that suspicion S1 is

benign and S2 is malicious.


For a list of Features for any Element in the Cybereason platform,

[including all suspicions and evidence, see Query Elements and](https://nest.cybereason.com/s/knowledge-base?article=query-api-token-query-elements-and-features-version-232148-and-later)


[Features (/s/knowledge-base?article=query-api-token-query-](https://nest.cybereason.com/s/knowledge-base?article=query-api-token-query-elements-and-features-version-232148-and-later)

[elements-and-features-version-232148-and-later).](https://nest.cybereason.com/s/knowledge-base?article=query-api-token-query-elements-and-features-version-232148-and-later)

## Detection logic and Malops


MalOps typically include multiple suspicions and possibly

evidence as part of their detection logic. For the Cybereason


platform to trigger a MalOp, the platform must detect a number of
"conditions"-multiple specific suspicions or evidence for the same


item (such as a process or file).


For example, for MalOp A, the detection logic for the MalOp


requires suspicion S1, evidence E1, and suspicion S2. If the

platform generates suspicion S1 and evidence E1, but not


suspicion A2, the platform does not generate a MalOp. For a use
case example explaining this logic for a Cybereason Malop, see


[Understand MalOp Detection Logic - Use Case (/s/knowledge-](https://nest.cybereason.com/s/knowledge-base?article=24-1-understand-malop-detection-logic-use-case&language=en_US#understand-malop-detection-logic-use-case)

[base?article=24-1-understand-malop-detection-logic-use-](https://nest.cybereason.com/s/knowledge-base?article=24-1-understand-malop-detection-logic-use-case&language=en_US#understand-malop-detection-logic-use-case)


[case&language=en_US#understand-malop-detection-logic-use-](https://nest.cybereason.com/s/knowledge-base?article=24-1-understand-malop-detection-logic-use-case&language=en_US#understand-malop-detection-logic-use-case)

[case).](https://nest.cybereason.com/s/knowledge-base?article=24-1-understand-malop-detection-logic-use-case&language=en_US#understand-malop-detection-logic-use-case)


Using this complex detection logic that requires multiple

conditions ensures with a high degree of probability that the


detected behavior is actual malicious behavior. Likewise, using

this more complex detection logic ensures fewer false positive


results.


The Cybereason security team is continually evaluating and


updating detection rules based on additional research, false

positive rates among your and other customer environments, and


internal testing to ensure that MalOps both:


1. Accurately detect the malicious behaviors they are meant to


detect

2. Represent likely malicious behavior


[For a list of MalOps in the Cybereason platform, see MalOp Types](https://nest.cybereason.com/s/knowledge-base?article=24-1-malop-types-in-depth&language=en_US#malop-types-in-depth)

[in Depth (/s/knowledge-base?article=24-1-malop-types-in-](https://nest.cybereason.com/s/knowledge-base?article=24-1-malop-types-in-depth&language=en_US#malop-types-in-depth)


[depth&language=en_US#malop-types-in-depth).](https://nest.cybereason.com/s/knowledge-base?article=24-1-malop-types-in-depth&language=en_US#malop-types-in-depth)



