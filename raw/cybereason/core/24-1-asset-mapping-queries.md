## Servers mapping

**Goal:** Find machines running certain services.


**Explanatory statement:** I want to find certain server services


running on Windows Server 2012 R2 machines.


Construct this query:


**Machine** Element -> filter for OS version is _Windows Server 2012_

_R2_ THEN


**Services** Element -> filter for Service name contains _Apache_ OR
_nginx_ OR _IIS_ OR _tomcat_ AND filter for Is active is _True_

## Network connection mapping


**Goal:** Find connections from external addresses toward internal


machines.


**Explanatory statement:** I want to find connections from


addresses outside my organization to machines inside my

organization.


Construct this query:


**Process** Element THEN
