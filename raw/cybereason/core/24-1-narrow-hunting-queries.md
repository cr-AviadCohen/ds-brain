These query examples yield low false positives, but may rarely
produce results.
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
Find Trickbot by Module
Find fileless malware persistence via MSHTA
Find Trickbot by Module
Goal: Search for processes with Trickbot's malicious module
(core-dll.dll)
Explanatory statement: I want to find processes that use the
Trickbot malicious module named core-dll.dll.
Construct this query:
Process Element THEN
Loaded modules Element -> filter for Name contains core-dll.dll
