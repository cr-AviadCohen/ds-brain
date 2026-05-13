**Process** Element -> filter for Product type is _Microsoft Office_


THEN


**Children** Element -> filter for Product type is _Shell_

## First execution of downloaded file


**Goal:** Find instances of the first execution of downloaded

processes


**Explanatory statement:** I want to find instances of first execution

of a process or processes that were downloaded from


somewhere.


Construct this query:


**Process** Element -> filter for First Execution of Downloaded

Process is _True_

## Processes with autorun registry key


**Goal:** Investigate processes that have an autorun registry key


entry


**Explanatory statement:** I want to look at processes that use an


registry key with autorun.


Construct this query:


**Process** Element -> filter for Has registry entry is _True_


## Autostart services

**Goal:** Search for rare services with an _Auto start_ start type.


**Explanatory statement:** I want to find services that are not


common and that are set to automatically run on machine restart.


Construct this query:


**Service** Element -> filter for Start type is _Auto start_ AND Is active

is _True_ AND Rare Service is _True_ THEN


**Binary File** Element -> filter for Signed is _False_

## Scheduled task executed from temp


**Goal:** Review running tasks with actions executed from temp.


**Explanatory statement:** I want to investigate tasks that are


currently running and that have been run from the //temp folder.


Construct this query:


**Scheduled task** Element -> filter for Task state is _Running_ THEN


**Scheduled task actions** Element


**Executable** Element -> filter for Path is _Temp_


**Goal:** Search for executable files in a location which usually stores

shortcuts.


**Explanatory statement:** I want to search for executable files from

the directories where the operating system normally keeps


shortcuts.


Construct this query:


**File** Element -> filter for Path contains _startup_ AND File name is

_.exe_ THEN


**Machine** Element -> filter for OS version is _Windows_

## External connections from processes


**Goal:** Find external connections coming from processes that host

injected threads.


**Explanatory statement:** I want to find connections to external

addresses that originate in processes that have injected threads.


Construct this query:


**Connection** Element -> filter for Is external is _True_ THEN


**Process** Element -> filter for Hosting Injected Thread is _True_


## External connections from processes

**Goal:** Find external connections coming from processes that have


suspicions.


**Explanatory statement:** I want to find connections to external


sources that are from suspicious processes.


Construct this query:


**Connection** Element -> filter for Is external is _True_ THEN


**Process** Element -> filter for Has Suspicions is _True_

## Injection by browser


**Goal:** Search for processes identified as running code that was


injected by a browser process.


**Explanatory statement:** I want to find processes that have


injected code from a browser.


Construct this query:


**Process** Element -> filter for Product type is _Browser_ AND

Detected injecting process is _True_


Note


Exclude well known browsers using the ! "Not" operator

## Encoded command


**Goal:** Search for processes which are not **powershell.exe** or

**cmd.exe** but are executing PowerShell.


**Explanatory statement:** I want to find processes that are not

PowerShell or the command line that are running PowerShell.


Construct this query:


**Process** Element -> filter for Command line contains _encoded_ OR


_encode_

## Executed from temp evidence


**Goal:** Review processes executed from temporary folders, has a

command line that contains a parameter of a temporary location,


or has a module located in a temporary folder.


**Explanatory statement:** I want to investigate processes running


from a temporary folder that also have a command line parameter

pointing to a temporary location or with a module running from a


temporary location.


Construct the following three queries:


**Process** Element -> filter for Running from temporary folder is

_True_


**Process** Element -> filter for Command Line Contains Temp is


_True_

**Process** Element -> filter for Module in temporary folder is


_True_


Note


The OR operator in this case will not work, this will require you

to execute 3 separate queries or one query which includes all


3 filters.

## Suspicious temp file


**Goal:** Review processes running from a temporary folder that


have external connections and injected processes.


**Explanatory statement:** I want to investigate processes running


in a temporary folder that are connecting with an address that is

external to my organization and that are injected processes.


Construct the following query:


**Process** Element -> filter for Running from temporary folder is


_True_ AND Has external connection is _True_ AND Detected injected

process is _True_


**Goal:** Search for processes with rare extensions.
