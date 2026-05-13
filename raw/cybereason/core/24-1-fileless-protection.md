## Fileless attack prevention video


|Framework/program|Description|Module|
|---|---|---|
|PowerShell|Attackers use the<br>legitimate PowerShell<br>module to launch<br>advanced, fleless attacks.<br>NGAV prevents malicious<br>PowerShell commands<br>before the commands can<br>execute, even in cases<br>where an attacker<br>obfuscated the PowerShell<br>command.|AMSI,<br>.NET|
|.NET|Attackers increasingly<br>exploit the powerful .NET<br>framework. Cybereason<br>can defend against<br>malicious .NET techniques<br>such as DotNetToJScript,<br>.NET foating modules,<br>and tools such as<br>SharpSploit,<br>SILENTTRINITY, and<br>Internal Monologue.|.NET|
|JScript and VBScript|Attackers use native<br>Windows scripting<br>languages to implement<br>sophisticated, multiple-<br>stage attacks. For<br>example, malicious<br>documents may launch an<br>HTML page containing<br>VBScript code that<br>triggers malicious<br>shellcode. For example, if<br>NGAV exposes these<br>behaviors and identifes<br>the stage where the script<br>needs to supply the<br>scripting engine with plain,<br>unobfuscated code, and<br>can then scan and block<br>this deobfuscated content.|AMSI|


|Framework/program|Description|Module|
|---|---|---|
|Offce macros,<br>including Excel 4.0<br>Macro|Attackers use malicious<br>macros that run within the<br>VBA framework to launch<br>attacks from Offce<br>documents. If NGAV<br>detects specifc Windows<br>API calls that are<br>considered high risk, it<br>analyzes the macro, and<br>prevents the macro from<br>executing if the macro is<br>deemed malicious.|AMSI|
|Windows<br>Management<br>Instrumentation (WMI)|Protects against attacks<br>that exploit WMI, a set of<br>Microsoft specifcations<br>used for administration of<br>Windows systems.<br>Attackers use WMI to<br>interact with local and<br>remote systems, and to<br>perform that assist<br>discovery and lateral<br>movement, such as<br>gathering information or<br>remote fle execution.|AMSI|




Attackers use various modules, frameworks, and programs to
launch advanced, fileless attacks. Attackers can take control of a


module, framework, or program in many ways, often without using
the relevant process. In many cases, fileless attacks never access


the disk, meaning that these attacks can easily elude standard

antivirus tools.


NGAV prevents malicious commands before the commands can

execute, even in cases where an attacker obfuscated the


command. Where relevant, the malicious command or payload is

[displayed within the MalOp. For PowerShell attacks, see Malicious](https://nest.cybereason.com/s/knowledge-base?article=24-1-malicious-process-malops&language=en_US#process-ran-malicious-command)


[Command Malop (/s/knowledge-base?article=24-1-malicious-](https://nest.cybereason.com/s/knowledge-base?article=24-1-malicious-process-malops&language=en_US#process-ran-malicious-command)

[process-malops&language=en_US#process-ran-malicious-](https://nest.cybereason.com/s/knowledge-base?article=24-1-malicious-process-malops&language=en_US#process-ran-malicious-command)


[command) for more information.](https://nest.cybereason.com/s/knowledge-base?article=24-1-malicious-process-malops&language=en_US#process-ran-malicious-command)

## Fileless detection and prevention options


The Cybereason platform allows you to control how and which


types of attacks are detected.


You can instruct the Cybereason platform to both detect and


prevent:


The use of certain commands, such as **InvokeExpression**


and **DownloadString**

Malicious use of scripts


Floating .NET modules


The detection/prevention mechanism is less invasive to processes


themselves, providing better stability and reducing the risk of

application crashes.


Note


If you have legitimate processes that might trigger Fileless


protection, you can also add exclusions so that Fileless

protection does not block legitimate use of these frameworks.


[See Set the Fileless Protection Modes (/s/knowledge-base?](https://nest.cybereason.com/s/knowledge-base?article=24-1-set-the-fileless-protection-modes&language=en_US#set-the-fileless-protection-modes)
[article=24-1-set-the-fileless-protection-](https://nest.cybereason.com/s/knowledge-base?article=24-1-set-the-fileless-protection-modes&language=en_US#set-the-fileless-protection-modes)


[modes&language=en_US#set-the-fileless-protection-modes) to](https://nest.cybereason.com/s/knowledge-base?article=24-1-set-the-fileless-protection-modes&language=en_US#set-the-fileless-protection-modes)
learn how to configure your Fileless protection.


Watch this video for more examples of Fileless protection by EDR

and NGAV components.


## Fileless detection events and

Fileless protection MalOps include descriptions for rule-based


(pattern) Fileless detection events. Descriptions of the malicious

behavior associated with the pattern help analysts better


understand the context of the event.


You can view these descriptions in the MalOps details within the


top left Description area, and in the Investigation screen, in the

Detection event's properties section.


For example, notice the description provided for the

Script_Obfuscation (325) event in the MalOp details screen:


In addition, for Fileless Protection MalOps, in cases where the


Cybereason platform has captured the attack payload that has

triggered the MalOp, analysts can view/download the payload


content in order to conduct analysis of it.


**To analyze the payload, follow these steps:**


1. From the **Malop Details** screen, click the **Process** tab.

2. Click the affected process to open the Process details screen.


3. In the Detection Events section, click items in the **Contents**


list.


4. In the PowerShell section, hover over the payload drop down


to view the payload on screen, or click **Export** to download


the payload content in a text file for analysis.


Note


Handle payloads with care, as they contain malicious code.


[See a full example here: Analyze Payload for Fileless MalOp](https://nest.cybereason.com/s/article/7361776)


[Example (/s/article/7361776)](https://nest.cybereason.com/s/article/7361776)



