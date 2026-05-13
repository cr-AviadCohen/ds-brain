Persistence MalOps are triggered for behaviors that enable an
attacker to have continued access to the machine, network,
environment, and so forth. The Cybereason platform detects a
number of different behaviors resembling persistence.
These MalOps are part of the Verified group.
The Cybereason platform detects a number of different behaviors
resembling persistence. Persistence MalOps include:
Malicious fake module: triggered when a process loads a
false module (correct module name but different metadata)
such as a fake Outlook Web App (OWA).
Masquerading as a Windows accessibility feature:
triggered when the process uses an identified and known
method for abusing Windows accessibility features and then
the process executes as a shell process.
Supported OS for these MalOps: Windows
Next steps
Investigate the Process Element Details, paying special
attention for unsigned DLL files that have a signed version
Remediate any malicious DLL files.
Investigate the process hierarchy.
