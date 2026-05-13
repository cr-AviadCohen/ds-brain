## Find attempts to delete Windows

**Goal:** Find strange admin behavior and potentially some

ransomware.


**Explanatory statement:** I want to find admin processes behaving

strangely like ransomware.


Construct this query:


**Process** Element -> filter for Process name contains _wmic.exe_ OR


_vssadmin.exe_ AND filter for Command line contains _delete_ OR

_shadowcopy_

## Find attempts to modify the firewall
## (including port forwarding)


**Goal:** Find active attackers who are pivoting through your network.


**Explanatory statement:** I want to find processes attempting to


change firewall settings.


Construct this query:


**Process** Element -> filter for Process name contains _netsh.exe_
and filter for Command line contains _portproxy_ OR _firewall_



