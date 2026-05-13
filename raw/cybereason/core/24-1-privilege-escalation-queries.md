The following examples show how to hunt for malicious behavior
occurring in the privilege escalation stage of a cyber attack.
The example queries in this section are meant to be a starting
point for your investigations. You may need to update the Features
(filters) in each query to use indicators specific to your
environment or situation.
Each of these examples is formatted with the individual Element in
the query on its own separate line, in bold text. Features (filters)
applied to the Element follow the Element name in regular weight
text. Each example also contains a description of the goal of the
hunt and the explanatory statement of what you want to find.
In this topic:
Malicious use of Psexec
Attempt to run as
Escalation to SYSTEM privileges
Malicious use of Psexec
Find processes executed by PsExec service and are suspected of
being executed maliciously.
Process THEN Malicious use of PsExec is True
Attempt to run as
Find processes with a RunAs product type.
