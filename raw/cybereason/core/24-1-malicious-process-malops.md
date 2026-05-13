## Attempt to stop or disable the

## Cybereason service

The 'Attempt to stop or disable the Cybereason service' MalOp is


triggered when a process makes attempts to try to interfere with

Cybereason services running on a machine. The Sensor has a


number of programs and services to help with the Sensor's data

collection on the machine. Attempts to disable the Cybereason


service should be seen as a precursor to malicious activity as the

attacker attempts to remove barriers to movement on the machine.


**Supported OS for this MalOp:** Windows


The following examples describe behavior that can trigger a

Attempt to stop or disable the Cybereason service MalOp:


Stopping of the Cybereason service

Suspension of Anti-Malware

## Next steps: Attempt to stop or disable the

## Cybereason service


Investigate the process performing these attempts.

Investigate the process hierarchy.


Remediate the process if necessary.

Restart the Cybereason services if necessary.

## Fileless malware


The 'Fileless Malware' MalOp is triggered when a process

executes a malicious payload that exists in the machine memory.


Fileless malware is the execution of malware without the need to

install a program or file on a machine. The malware loads its


payload into memory without dropping the payload on the file

system. Often these attacks are executed with scripting engines,


such as PowerShell, the Windows scripting host, and bash. This

enables attackers to use the operating system functionality


against the machine and evade common security protocols and

programs.


**Supported OS for this MalOp:** Windows


The following examples describe behavior that can trigger a


Fileless Malware MalOp:


Use of the Apfell framework on macOS


Running a payload with Python on macOS

## Next steps: Fileless malware


Investigate the process in question and the process hierarchy.


Examine the loaded modules and command line for the

process.


Investigate whether the process was launched by a

scheduled task or WMI activity to look for persistence.


Check to see if the process has network connections and

compare their details with known threat intelligence.

## Java-based Malware


The 'Java-based Malware' MalOp is triggered when a process

exhibits behaviors similar to a Java-based Remote Access Trojan.


Java-based malware involves packaging the malware program as
a Java .jar file, often sent as an email attachment. This enables the


attacker to hide their malicious programs in what appears to be a
legitimate file that when opened, will silently install and run the


malware in their environments.


**Supported OS for this MalOp:** Windows

## Next steps: Java-based Malware


Investigate the process and process hierarchy.

Check if Java is approved in the environment as well as the


Java details.

## Malicious use of an OS process


The 'Malicious use of an OS process' MalOp is triggered when a


process uses an OS process in an unusual way. The misuse of

operating system features is an attack technique where the


attacker tries to hide their activities under the guise of a legitimate

operating system function.


**Supported OS for this MalOp:** Windows


The following examples describe behavior that can trigger a

Impersonation of an OS process MalOp:


Use of certutil.exe utility to encode/decode data or download
files


Running malicious code with Regsvr32


Opening a reverse shell on macOS

## Next steps: Malicious use of OS process


Investigate the process image file.


Investigate the process hierarchy for evidence of strange

activity.

## Malicious process behavior


The 'Malicious process behavior' MalOp is triggered when

Behavioral execution protection detects unusual process behavior


that may indicate misuse of legitimate software to execute an

attack. The misuse of legitimate software functionality is an attack


technique where the attacker tries to hide their activities under the

guise of a legitimate process.


The **Signature** field contains the rule ID, which indicates the

behavior that triggered the rule.


**Supported OS for this MalOp:** Windows


The following examples describe behavior that can trigger a


'Malicious process behavior' MalOp:

Executing a fileless script with the MSHTA or RunDLL32


utilities

Using **reg.exe** for credential dump activity


Exploiting the Microsoft Exchange application pool

( **MSExchangeOWAAppPool** )

## Malicious exploit attempt


The 'Malicious exploit attempt' MalOp is triggered when

[Cybereason Exploit protection (/s/knowledge-base?article=24-1-](https://nest.cybereason.com/s/knowledge-base?article=24-1-exploit-protection&language=en_US#exploit-protection)


[exploit-protection&language=en_US#exploit-protection) detects](https://nest.cybereason.com/s/knowledge-base?article=24-1-exploit-protection&language=en_US#exploit-protection)

and blocks an exploit attempt on a process.


The following examples describe behavior that can trigger a

"Malicious exploit attempt" MalOp:


A user opens a malicious Word document or a PDF file that

contains an exploit.


An attacker that previously gained code execution on the host

machine injects shellcode to one of the processes protected


by exploit protection.

## Next steps: Malicious exploit attempt


Investigate the exploit attempt and ensure that the exploit


attempt was not a false positive.

If the exploit attempt is valid, assess other malicious activities


around the vulnerable software and make sure to apply

relevant patches.


## Malicious floating module

The 'Malicious floating module' MalOp is triggered when the


Cybereason platform's NGAV component detects the presence of
a floating module used in a malicious manner on a machine.

## Next steps: Malicious floating module


Investigate the process that loaded the module
Investigate the specific module identified as malicious


Remove the module from the machine if necessary

## Malicious InstallUtil process execution


The 'Malicious InstallUtil process execution' MalOp is triggered


when a process launches the InstallUtil utility program to make

external connections.


**Supported OS for this MalOp:** Windows

## Next steps: Malicious InstallUtil process


Investigate the process that launched the InstallUtil utility


Examine the command line used by the process.

Kill the process if necessary.

## Malicious execution of MSBuild process

## by MS Office process


The 'Malicious execution of MSBuild process by MS Office

process' MalOp is triggered when the MSBuild program is


launched by an MS Office program.


**Supported OS for this MalOp:** Windows

## Next steps: Malicious execution of

## MSBuild process


Examine the process that launched MSBuild and the process

hierarchy.


Kill the process that launched MS Build if necessary.

## Malicious .NET process compilation


The 'Malicious .NET process compiler' MalOp is triggered when a


process launches a .NET-based compiler process that then

performs malicious activity.


**Supported OS for this MalOp:** Windows


## Next steps: Malicious .NET process

Examine the process that launched the .NET compiler.


Examine the process hierarchy.

Kill the proces that launched the compiler and the compiler


process.

## Malicious MSBuild process execution


The 'Malicious MSBuild process execution with outgoing


connections' MalOp is triggered when the MSBuild process runs

with temporary parameters in the command line and the process


makes external connections.


**Supported OS for this MalOp:** Windows

## Next steps: Malicious MSBuild process

## execution with outgoing connection


Examine the MSBuild process.

Examine the command line used for the MSBuild process.


Isolate the machine if needed.

## Msmpeng.exe process mismatch


The 'Msmpeng.exe process mismatch' MalOp is triggered when


the msmpeng.exe operating system process is renamed to

another process.


**Supported OS for this MalOp:** Windows

## Next steps: Msmpeng.exe process


Investigate the renamed process.


Kill the process if necessary.

## Process was initiated by a malicious

## packed binary


The 'Process was initiated by a malicious packed binary' MalOp is


triggered when a process runs a DLL file that was found to be

packed using a special packer process. Packed processes


involve packing a process file or binary file as an attempt to hide

malicious content.


**Supported OS for this MalOp:** Linux


## Next steps: Packed process

Investigate the process loading the DLL file.


Remediate the malicious DLL file on the machine if necessary.

## Process opened a malicious file


The 'Process opened a malicious file' MalOp is triggered when a


process opens a file that either Cybereason Threat Intelligence or
Cybereason behavioral document protection has classified as


malicious. Malicious processes commonly use non-executable
files, such as documents or scripts, to run malicious code that


executes problematic or malicious files.


**Supported OS for this MalOp:** Windows


The following examples describe behavior that can trigger a


"Malicious by opening malicious file" MalOp:

Running malicious files for known hacking tools


Opening a Word, Excel, or PowerPoint file that includes a

malicious macro

## Next steps: Malicious file


Investigate the files through the Suspicion details.

Examine the process hierarchy.


Investigate the process to see if the process is making any

network connections.


If Cybereason determines that the file is malicious, quarantine
or remove the file.

## Process ran malicious command


The 'Process ran malicious command' MalOp is triggered when a
PowerShell process was identified trying to run a malicious


command or payload that contains either a malicious function or

malicious content.


**Supported OS for this MalOp:** Windows

## Next steps: Process ran malicious


Investigate the payload identified as malicious content.


Review connection activity associated with the PowerShell

process and child processes.


## Process has loaded Cobalt Strike Beacon

The 'Process has loaded Cobalt Strike Beacon' MalOp is triggered


when a process loads the Cobalt Strike Beacon tool on a machine.

The Cobalt Strike Beacon is a known malicious tool framework for


Command and Control operations.


**Supported OS for this MalOp:** Windows

## Next steps: Cobalt Strike Beacon


Isolate the machine as soon as possible.


Investigate the process loading the Cobalt Strike tool, using

the platform (not through an investigation query).


Remediate/remove the Cobalt Strike tool.

Examine the process hierarchy to see what other activities the


process is attempting to perform.

Contact the Cybereason GSOC and IR services for further


recommendations.

## Process has loaded PowerShell Empire


The 'Process has loaded PowerShell Empire' MalOp is triggered


when the PowerShell Empire agent is launched on a machine. The

PowerShell Empire is a malicious agent loaded on a machine


loaded after penetration on a machine that enables an attacker to

run PowerShell commands remotely from the machine. The use of


this is part of Command and Control operations.


**Supported OS for this MalOp:** Windows

## Next steps: PowerShell Empire


Investigate the process loading PowerShell Empire.

Examine the process hierarchy to see what other activities the


attacker is trying to perform.

Isolate the machine if necessary.


Remediate the PowerShell Empire agent.

## Process has loaded a Meterpreter agent


The 'Process has loaded a Meterpreter Agent' MalOp is triggered


when the Meterpreter agent is started on a machine. The

Meterpreter agent is part of the Meterpreter framework. The agent


is loaded on a machine start and enables a remote attacker to

gain persistence on a machine.


**Supported OS for this MalOp:** Windows

## Next steps: Meterpreter


Investigate the process loading the Meterpreter agent.

Examine the process hierarchy to see what other activities the


attacker is trying to perform.

Isolate the machine if necessary.


Remediate the Meterpreter agent.

## Process has loaded Mimikatz


The 'Process has loaded Mimikatz' MalOp is triggered when a


process loads the Mimikatz framework on a machine. The

Mimikatz framework is a malicious utility that enables an attacker


to view and steal credential information from the Windows LSASS

resources.


**Supported OS for this MalOp:** Windows

## Next steps: Mimikatz


Investigate the process loading Mimikatz.


Examine the process hierarchy to see what other activities the

attacker is trying to perform.


Isolate the machine if necessary.

Remediate the programs related to Mimikatz.

## Process has loaded a PeddleCheap agent


The 'Process has loaded a PeddleCheap agent' MalOp is

triggered when a Peddle Cheap agent launches on a machine.


The PeddleCheap agent is an agent used after penetration on a

machine to help with Command and Control with another server.


**Supported OS for this MalOp:** Windows

## Next steps: PeddleCheap


Investigate the process that loaded the PeddleCheap agent.


Examine if the process is making external connections.

Examine the process hierarchy to see what other activities the


attacker is trying to perform.

Isolate the machine if necessary.


Remediate the programs related to the PeddleCheap agent.


## Process has loaded a malicious tool

The 'Process has loaded a malicious tool' MalOp is triggered


when the Cybereason platform detects the presence of a
malicious tool on a machine. Certain specific tools, such as


Mimikatz, Meterpreter, Cobalt Strike, and PeddleCheap trigger

unique MalOps for that tool.


**Supported OS for this MalOp:** Windows

## Next steps: Process has loaded a


Investigate the process that loaded the malicious agent.


Examine if the process is making external connections.

Examine the process hierarchy to see what other activities the


attacker is trying to perform.

Isolate the machine if necessary.


Remediate the programs related to the malicious agent.

## Remote Access Trojan


The MalOp for Remote Access Trojan is triggered when a process


exhibits behavior like a Remote Access Trojan. Remote Access

Trojans are software set to invisibly invade a machine and then


allow remote access to the same machine.


**Supported OS for this MalOp:** Windows, Mac OS, and Linux

## Next steps: Remote Access Trojan


Investigate the process.

Examine the process hierarchy.


Investigate the connections the process is making

Isolate the machine as necessary.

## Shellcode execution


The MalOp for 'Shellcode execution' is triggered when a process

is found to be running injected shellcode. Shellcode enables an


attacker to open a command window after code is injected into a

process. From there, this attacker can perform the commands he


or she needs as needed.


**Supported OS for this MalOp:** Windows



