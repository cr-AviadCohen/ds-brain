Credential Theft MalOps are triggered by actions that attempt to
access or take credential information from a machine.
These MalOps are part of the Research group.
In this topic:
Abnormal process invocation using DCOM
Active Directory Abuse
Process performed a malicious read/write memory access to
a sensitive process
Abnormal process invocation using
DCOM
The 'Abnormal process invocation using DCOM' MalOp is
triggered when a process uses an MS-RPC request to access a
machine's DCOM layer and then uses another program to launch
a process through DCOM.
Supported OS for this MalOp: Windows
Next steps - Abnormal process
invocation using DCOM
Investigate the processes in question, including parent and
child processes.
Examine the Element details for the processes.
Active Directory Abuse
The 'Active Directory Abuse' MalOp is triggered when a process
attempts to retrieve or update information on the Active Directory
of a machine.
Supported OS for this MalOp: Windows
Examples of behavior that can trigger this MalOp:
