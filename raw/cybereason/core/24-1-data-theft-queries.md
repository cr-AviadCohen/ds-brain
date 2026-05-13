Hunt for malicious behavior occurring in the data theft stage of a
cyber attack.
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
High data transfer by injected process
Find Java-based malware attempting remote access
High data transfer by injected process
Goal: Search for process with a high data transmission rate and
that have a detected injected process.
Explanatory statement: I want to find processes that are
transmitting a lot of data and are being injected into by a process
that has been detected as an injecting process.
Construct this query:
Process Element -> filter for High Data Transmitted is True AND
filter for Detected injected process is True
