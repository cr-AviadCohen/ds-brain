**URL Domains** Element -> filter for Reputation is _Unresolved_

_domain_

## Outbound communication to a hostile


**Goal:** Search for communication to known hostile domains


**Explanatory statement:** I want to find evidence of communication


to hostile domains by finding connections to domains classified as

malicious or hostile.


Construct this query:


**Connection** Element -> filter for Direction is _Outgoing_ or _Outgoing_


_(Guessed)_


**URL Domains** Element -> filter for Reputation is _Blocklisted_ OR


_Malware_ OR _Sinkholed domain_ OR _Unresolved domain_

## Communication with dynamic DNS


**Goal:** Search for connections with a dynamic DNS servers


(usually always an indicator of malicious behavior)


**Explanatory statement:** I want to find evidence of connections


made to servers that use a dynamic DNS configuration.


Construct this query:


**Connection** Element -> filter for Remote Address Type is _Dynamic_
_Configuration_





