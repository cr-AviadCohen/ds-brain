**Parent process** Element -> filter for Unsigned is _True_

## Wmiprvse.exe with unsigned parent

## process executed by SYSTEM user


**Goal:** Find wmiprvse processes executed by an unsigned parent

process that is executed by SYSTEM user.


**Explanatory statement:** I want to find WMI processes run by a

parent process that is unsigned and the user that is running the


process is a SYSTEM level user.


Construct this query:


**User** Element -> filter for Local system is _True_ THEN


**Process** Element -> filter for Unsigned image file is _True_ THEN


**Children** Element -> filter for Process name is _wmiprvse.exe_

## Unsigned child or grandchild process of

## wmiprvse.exe executed by SYSTEM user


**Goal:** Find unsigned processed which are children or


grandchildren of wmiprvse.exe processes and are executed by

SYSTEM user.


**Explanatory statement:** I want to find descendant processes of

WMI that are unsigned and are run by a SYSTEM-level user


Construct this query:


**Child processes:**


**User** Element -> filter for Local system is _True_ THEN


**Process** Element -> filter for Unsigned image file is _True_ THEN


**Parent process** Element -> filter for Process name is


_wmiprvse.exe_


**Grandchild processes:**


**User** Element -> filter for Local system is _True_ THEN


**Process** Element -> filter for Unsigned image file is _True_ THEN


**Parent process** Element THEN


**Parent process** Element -> Process name is _wmiprvse.exe_

## Execution of unsigned child or grandchild

## process by wmic.exe


**Goal:** Find unsigned child or grandchild processes executed by

wmic.exe.


**Explanatory statement:** I want to find descendant processes run

from WMI activity.


Construct these queries:


**Child processes:**


**Process** Element -> filter for Unsigned image file is _True_ THEN


**Parent process** Element -> filter for Process name is _wmic.exe_


**Grandchild processes:**


**Process** Element -> filter for Unsigned image file is _True_ THEN


**Parent process** Element THEN


**Parent process** Element -> Process name is _wmic.exe_

## Find processes executed by WMI


**Goal:** Find processes that have been executed by WMI on your

machines.


**Explanatory statement:** I want to find processes that have been

run because of WMI activity on my environment.


Construct this query:


**Process** Element -> filter for Executed by WMI is _True_



