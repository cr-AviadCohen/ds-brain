Persistence behaviors include actions by processes to persist on
a machine when the machine restarts. The MalOp types listed in
this topic are triggered by various persistence behaviors.
These MalOps are part of the Research group.
In this topic:
Async Rat malware detected
User login/logout hook detected
Async Rat malware detected
The 'Async Rat Malware detected' MalOp is triggered when the
Cybereason platform detects the presence or execution of
suspicious behaviors by MSHTA that result in the creation of
PowerShell downloader programs.
This MalOp is supported for machines running supported
Windows operating systems.
Supported OS for this MalOp: Windows
Next steps: Async Rat malware detected
Investigate the process in question to see what other
processes are created from the process.
Isolate the machine if necessary.
Kill the process to stop the creation of other PowerShell
processes.
User login/logout hook detected
The 'User login/logout hook' MalOp is triggered when a process
creates a login or logout hook on a macOS machine that enables
the process to automatically persist on the machine on a user's
login or logout from the machine.
Supported OS for this MalOp: macOS
