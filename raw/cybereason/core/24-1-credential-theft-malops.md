Process accessing credential information files via a shadow


copy

Access of registry keys with credential information

## Next steps Attempted credential theft


Investigate the process to see if it is allowed to access

credential resources.


Investigate the process's loaded modules. Use the query

**Malop Process** Element -> **Suspicious Process** Element ->


**Loaded modules** Element to view these modules.

Examine the Element details for the processes and loaded


modules.

Examine the user details for the user associated with the


MalOp/detection and their privilege level.

## Malicious access to the NTDS.dit file


The MalOp for 'Malicious access to the NTDS.dit' file is triggered


when a process attempts to open or access the NTDS.dit file used

by the operating system, which contains credential information for


the operating system and users.


**Supported OS for this MalOp:** Windows

## - Next steps Malicious access to the

## NTDS.dit file


Investigate the process to see if it is allowed to access

credential resources.


Examine the Element details for the processes.

Examine the command line for the process in question.


Examine the user details for the user associated with the

MalOp/detection and their privilege level.

## Malicious access to ntds.dit or SAM

## resources


The MalOp for 'Malicious access to ntds.dit or SAM resources'

MalOp is triggered when a process uses the esenutil utility to gain


access to credential resources on the machine.


**Supported OS for this MalOp:** Windows

## - Next steps Malicious access to the

## NTDS.dit or SAM resources


Investigate the process to see if it is allowed to access

credential resources


Examine the process hierarchy


Kill the process that launched the esenutil utility.





