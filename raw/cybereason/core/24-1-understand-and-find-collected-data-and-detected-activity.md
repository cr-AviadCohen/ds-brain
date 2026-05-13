Properties such as the name of a specific process
Classification, such as threat intelligence sources classifying a


file as ransomware
Specific behaviors, such as a process opening connections to


a malicious domain


Data collected from sensors is telemetry data on the properties of


items on a machine and data on what items are doing on the

machine.


The Cybereason platform presents collected data as properties of

an Element.


If the Element is associated with a MalOp, the Cybereason

platform displays the associated data for that Element in different


parts of the **Malop Details** screen:


For example, here are some process details in a MalOp, including


the command line, and times:


If the Element is not associated with a MalOp, you see the


Element's associated data in the **Element Details** screen when

you run an investigation query:


Process name and ID

Process times


Command line for the process


You can build an investigation query to report numerous pieces of
collected data, using filters such as an Element's properties:


For details on what data the Cybereason platform collects from a

[sensor, see Collected System-Level data (/s/knowledge-base?](https://nest.cybereason.com/s/knowledge-base?article=24-1-endpoint-data-collection&language=en_US#collected-system-level-data)


[article=24-1-endpoint-data-](https://nest.cybereason.com/s/knowledge-base?article=24-1-endpoint-data-collection&language=en_US#collected-system-level-data)

[collection&language=en_US#collected-system-level-data). For a](https://nest.cybereason.com/s/knowledge-base?article=24-1-endpoint-data-collection&language=en_US#collected-system-level-data)


[full list of all Elements and Features, see Query Elements and](https://nest.cybereason.com/s/knowledge-base?article=query-api-token-query-elements-and-features-version-232148-and-later)


[Features (/s/knowledge-base?article=query-api-token-query-](https://nest.cybereason.com/s/knowledge-base?article=query-api-token-query-elements-and-features-version-232148-and-later)

[elements-and-features-version-232148-and-later).](https://nest.cybereason.com/s/knowledge-base?article=query-api-token-query-elements-and-features-version-232148-and-later)

## View and understand detected activity


The Cybereason platform reports detected activity, represented by

evidence, suspicions, and Malops, in several ways.


The Cybereason platform's "operation-centric" view centers on
MalOps, or "malicious operations". MalOps represent a definite


pattern of malicious activity that requires multiple conditions and

behaviors. Requiring a pattern of behavior instead of one


condition helps reduce the number of "false positive" MalOps that

the platform generates.


MalOps are visible in the Malops management screen. From this

screen, you can open the MalOp Details screen for each MalOp to


view the evidence and suspicions that the Cybereason platform

associates with that MalOp.


For example, this MalOp displays the evidence and suspicions

that the platform detected directly in the Malop Details screen for


that MalOp:


In the Malop Details screen, you can investigate each evidence

and suspicion associated with the MalOp. You can also look for


other items that have the same evidence and suspicions.

## Additional suspicions and evidence


The Cybereason platform reports not just MalOps, which require


multiple "events" or conditions to be present, but also potentially

malicious individual activities.


To locate evidence and suspicions that are not related to a MalOp,

you can build a query based on the Element for which the


platform generated the evidence or suspicion.


The results return items that exhibit the same behavior as the

evidence or suspicion.


If query results return multiple instances of items for a specific

evidence or suspicion, or you see that the same evidence or


suspicions occurs multiple times over a long period of time, you

can create a custom detection rule that will generate a MalOp in


your environment.





