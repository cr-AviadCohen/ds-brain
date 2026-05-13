## Renamed processes

**Goal:** Find renamed processes.


**Explanatory statement:** I want to find examples of processes that
were renamed or had their image file/binary file renamed


Construct one of the following queries:


**Query 1:**


**Process** Element


**Loaded modules** Element


**File** Element


**File Event** Element -> filter for Event type is _Rename file_


**Query 2:**


**Process** Element


**Image File** Element


**File Event** Element -> filter for Event type is _Rename file_


**Query 3:**


**File** Element -> filter for File name contains ______ Internal name

contains ______


## Legitimate applications repurposed for

**Goal:** Find when a legitimate application (such an operating

system process or application) is used in a malicious manner.


**Explanatory statement:** I want to find instances where processes

that are considered legitimate are used in an unusual and


malicious way


Construct one of the following queries:


**Query 1:**


**Process** Element -> filter for Use of legitimate OS process for


persistence is _True_


**Query 2:**


**Process** Element -> filter for Process integrity is _Protected_ or
_System_ AND (select Feature filter for malicious behavior)

## Script execution


**Goal:** Find malicious script execution.


**Explanatory statement:** I want to find instances where a process


ran a script marked as malicious or ran a script that was not

expected.


Construct one of the following queries:


**Query 1:**


**Process** Element -> filter for Malicious script execution is _True_


**Query 2:**


Unexpected script execution is _True_

## Process has a listening port


**Goal:** Find applications that have opened listening ports


**Explanatory statement:** I want to find instances and details when

a process opens a listening connection.


Construct this query:


**Process** Element -> filter for Has opened socket is _True_

## Malicious services for a process


**Goal:** Find malicious services.


**Explanatory statement:** I want to find instances of malicious


services due to their rare nature or changes in the service

characteristics.


Construct one of the following queries:


**Query 1:**


**Process** Element


**Service** Element -> filter for Rare service is _True_


**Query 2:**


**Process** Element


**Service** Element -> filter for Rare active service is _True_


**Query 3:**


**Process** Element


**Service** Element -> filter for Rare start type is _True_


**Query 4:**


**Process** Element


**Service** Element -> filter for Binary file was changed is _True_


**Query 5:**


**Process** Element


**Service** Element -> filter for Service start name was changed is

_True_



