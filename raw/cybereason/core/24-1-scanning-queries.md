## Fake module suspicion

**Goal:** Investigate machines running processes with counterfeit

modules.


**Explanatory statement:** I want to find machines that have

processes which run counterfeit modules.


From the list of assets you gathered in the asset mapping, query

for the following suspicious behaviors:


DB_servers = ["serverName1", "serverName2",....]

Web_servers = ["serverName1", "serverName2",....]


Mail_servers = ["serverName1", "serverName2",....]


Construct this query for every servers list.


**Machine** Element -> filter for Machine name contains _DB_servers_

THEN


**Processes** Element -> filter for Counterfeit module Suspicion is

_True_

## Database external connection


**Goal:** Investigate machines running processes with external


connections.


**Explanatory statement:** I want to find machines that have


processes making a connection to addresses outside my

organization.


From the list of assets you gathered in the asset mapping, query

for the following suspicious behaviors:


DB_servers = ["serverName1", "serverName2",....]

Web_servers = ["serverName1", "serverName2",....]


Mail_servers = ["serverName1", "serverName2",....]


Construct this query for every servers list.


**Machine** Element -> filter for Machine name contains _DB_servers_

THEN


**Processes** Element THEN


**Connections** Element -> filter for Is external is _True_



