## DNS information collection

For Linux kernels prior to 2.6.32-358, DNS information is not


collected.

On Mac machines, the sensor's DNS collector on Mac High


Sierra may cause high CPU use during intensive DNS usage.

Mac sensors do not collect DNS or domain queries.


On sensors on Windows machines, when a Chromium-based

browser (such as Chrome or Microsoft Edge) accesses a


domain, the sensor does not collect the domain name the

browser accessed.


Likewise, if the domain name is on the blocklist or allowlist, the

reputation is not applied and a MalOp not is generated or not


generated correctly for these domains.

## Process information collection


In some scenarios, sensors do not collect data on all short

lived processes, connections, and files.
Sensors collect up to the first 512 characters of the command


line for short-lived processes, for example, PowerShell

commands. In the UI, longer commands appear truncated to


this length.

Command line collection on Linux machines has a limit of


4096 characters.

When viewing details on MalOps raised because of shellcode


injection, there may be times where the process reports the

process as injected shellcode or injected meterpreter, instead


of simply saying injected.

On Linux machines, short lived processes can terminate


before the sensor can collect the full context of modules

loaded by the process.

## Module information collection


In versions 23.2.12x and later, on macOS machines, the following
limitations apply to the collection ofloaded modules:


Modules are not collected from before the sensor initiates

Details on modules for many operating system services are


not collected, including modules signed by Apple for

processes signed by Apple.


when viewing details on the modules collected, the **address**
field always returns a value of **0** .

## File information collection


File hashes are not collected for files larger than 100 MB.
For executable files that were collected and were then


modified, the Cybereason platform does not rehash the new

executable. This affects visibility and detection (e.g. Known by


hash detection).


## Logon session collection

The Cybereason platform does not collect the end time for


Windows logon sessions for the following types of Windows users:


**<machine>system**


**<machine>network service**

**<machine>local service**


**<machine>admin**

**window managerdwm-<number>**


**font driver hostumfd-<number>**


As a result, the end time is missing for the Logon Session Element


in the Investigation screen.

## File event collection


For the file event collection, if the file path is between 80 and


130 characters, the path may be not be reported as the

sensor does not receive the information from the appropriate


Windows API. This may occur more often when the path

contains non-Latin characters.


For file events, there are a number of unexpected file events

collected:


If you create a folder, the Cybereason platform reports a

**Rename** event when the folder is renamed from **New**


**folder** to the new name.

If you delete a folder, the platform reports two events: the


correct **Delete** event and a **Rename** event when the

folder moves to the Recycle Bin.


If you delete a folder using the **SHIFT + DELETE** keys,

the platform does not report a **Delete event** .


If you create a folder from the command line with the

**mkdir** command, the platform does not generate a


**Create** event.

If you rename a folder from the command line using the


**REN** command, the platform does report a **Rename**

event.


If you delete a folder from the command line using the **RD**
command, the platform does not report any file events,


including the deletion operation.
For machines with a heavy stress due to file operations run on


the machine and the file event collection enabled, the

Attempted credential theft Malop might miss collection of up


to 10% of the events related to this MalOp and its related

detections.


For the registry events collection, UTF16 data and values are

not supported for collection.


When a registry key with values is deleted, the **Delete** event is

reported only for the top-level key but not the value of that


top-level key.



