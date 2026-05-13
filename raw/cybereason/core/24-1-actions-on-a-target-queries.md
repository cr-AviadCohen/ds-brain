Hunt to find execution of specific attacks on a given target.
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
Kovter and Poweliks Detection
Injected by a Browser
Kovter and Poweliks Detection
Goal: Search for Javascript in the command line, running
Powershell and Windows processes with injected code.
Explanatory statement: I want to find processes using Javascript
in the command line which then run PowerShell and Windows
procedures in injected code
Construct this query:
Process Element -> filter for Powershell process is True THEN
Parent Process Element -> filter for Command line contains
Javascript
