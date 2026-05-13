Phishing MalOps are triggered for behaviors that represent the
attacker's use of different techniques to achieve access to a
machine.
These MalOps are part of the Research group.
In this topic:
Malicious execution of a shell process
Malicious document detected
Malicious execution of a shell process
The 'Malicious execution of a shell process' MalOp is triggered
when a process is found to be running a shell process but the
process itself is not a shell runner process. Phishing includes the
use of shell processes as part of a phishing campaign to gain
information from a machine. These campaigns convince a user to
install something on their machine which then launches a shell
process and gives the attacker control of the machine.
Then, the shell processes work at a different level on the machine
and send commands to the machine to perform activities. The
Cybereason platform detects use of shell processes, including
shells with unexpected parents, elevated privileges, or shell
processes deleting shadow copies.
This MalOp is part of the Research group.
Supported OS for this MalOp: Windows
Next steps: Malicious execution of a shell
process
Investigate the process
Examine the process hierarchy, especially to find the root
cause or start point of the activity.
