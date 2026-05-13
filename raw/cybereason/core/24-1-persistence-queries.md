Attackers use a number of techniques to enable themselves and
their processes to persist inside your environment. Use these
queries to find examples of attack persistence inside your
organization.
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
Unsigned services employing autostart
Registry entry pointing to temporary folders
Unsigned services employing autostart
Goal: Find active services with an unsigned image file and
designated to start automatically.
Explanatory statement: I want to find currently running services
which have an unsigned image file but are designed to start
automatically.
Construct this query:
Service Element -> filter for Start type is Auto start AND Is active
is True THEN
Binary file Element -> filter for Signed is false
