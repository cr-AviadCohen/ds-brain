|Item|Description|
|---|---|
|File or fle<br>path|When Anti-Malware identifes a fle as malicious<br>or Anti-Malware scans cause performance<br>issues in your organization, you can add fle or<br>fle path exclusions to help you:<br>Prevent activity by legitimate fles or fles in<br>folders from causing the Cybereason<br>platform to trigger a MalOp for those fles<br>before fle execution<br>Remove legitimate fles and folders form<br>the amount of scanned fles/folders to<br>improve machine and scan performance<br>After you add the fle or folder path as an Anti-<br>Malware exclusion, the Cybereason platform<br>does not modify, move, block, or trigger alerts<br>for the fle or folder.<br>Anti-Malware exclusions apply to fles and<br>folders analyzed by Signature analysis, Artifcial<br>Intelligence, and Behavioral Document<br>Protection.<br>In addition, on Linux machines, Anti-Malware<br>automatically excluded network shares from<br>Anti-Malware scans, in addition to the**/sys** and<br>**/proc** mount points. If you need to exclude<br>additional mount points, open a Technical<br>Support (/s/support) case.|
|Processes|If you face issues with a process being marked<br>as malicious, high CPU usage on machines, or<br>issues with certain processes not running with<br>Fileless Protection enabled, you can exclude<br>these processes (either by process name or by<br>a regular expression pattern). You can also<br>exclude processes, identifed by name, from<br>Behavioral Execution Prevention or Exploit<br>Protection.|
|Commands|When using Anti-Ransomware or Predictive<br>Ransomware Protection, the Cybereason<br>platform may block the use of legitimate<br>programs and commands if the platform thinks<br>that the program/command behavior is similar<br>to ransomware activity. To help you avoid these<br>situations, add a command line exclusion.|


|Item|Description|
|---|---|
|Domains|With the Cybereason platform's Fileless<br>Protection, the Cybereason platform analyzes<br>activity related to the**Download** command.<br>However, if you have legitimate PowerShell<br>activity that needs to access domains that the<br>Cybereason platform things are malicious, you<br>add an exclusion for these domains.|
|Modules|At times, Fileless Protection will identify a<br>specifc module as malicious, but you know the<br>module to be legitimate. To help these modules<br>run as needed, you add an exclusion for the<br>module/namespace.|
|Rule<br>ID/Behavior<br>ID|If Rule-based Behavioral Document Protection,<br>Behavioral Execution Prevention or Variant<br>Payload Prevention analyzes a process, the<br>Cybereason platform may trigger rules if the<br>Cybereason platform found any malicious<br>activity. Each rule includes information for a<br>very specifc behavior for several processes, or<br>a single process may trigger multiple rules.<br>If you fnd that the process is legitimate and<br>Behavioral Execution Prevention or Variant<br>Payload Prevention are generating MalOps for<br>these behaviors, you add an exclusion for the<br>specifc rule ID/behavior ID and the<br>Cybereason platform will ignore the specifc<br>rule ID.<br>Behavioral Execution Prevention and Variant<br>Payload Prevention may analyze the process or<br>similar processes in the future, not related to the<br>excluded rule ID.|
|Fingerprint|As part of Variant File Prevention, the<br>Cybereason platform analyzes**fngerprints**<br>inside a fle that give the true nature of the fle,<br>and are often resistant to other changes by<br>attackers. If you fnd that a specifc fngerprint<br>for a fle continues to cause the Cybereason<br>platform to generate MalOps but you know the<br>fle to be legitimate, you can add an exclusion<br>for that fngerprint. The Cybereason platform<br>will then ignore the fngerprint in the future.|


|Item|Description|
|---|---|
|Script<br>pattern|If Fileless Protection blocks the use of a<br>legitimate command as part of the script<br>analysis feature, you add a pattern exclusion to<br>instruct the Cybereason platform to ignore the<br>pattern.|


## Obfuscation of exclusion lists

When a path, file or process is added to the exclusion list, it is

included in the logs.


To ensure that attackers are not able to view details on exclusions

and know items that are protected from NGAV protection engines,


the Cybereason platform obfuscates the path, file or process that

has been excluded in the logs.


If you need to know the actual exclusion, you can still view the
name of path, file or process that is added to the exclusion list in a


sensor policy.


Obfuscation of exclusion lists is supported on supported versions


of Windows, macOS, and Linux sensors.


When a path, file or process is added to the exclusion list, a line


such as the following was added to the logs:

```
 INFO 2022-09-12_13:24:31

 exclusionservice.cpp:185 General config:

 Parsed paths:

 c:\users\pycharmprojects\test, were

 added to the exclusions list.

```

This line is now obfuscated and will appear similar to the following:

```
 2022-09-12_13:24:31

 exclusionservice.cpp:185 General config:

 !$^ZSNkkj876DJDKS0h3ksjdkvckjwidjkvd8dwk

 j8ds8fJDFjdddcsSDJSKeJDKD988sd2k8wlijfwj

 ldkKSJFkdwksjdiuwJFKS=^$!

```

Exclusion lists are obfuscated in the following logs:


NGAV.log

AcScanner.log


CRExecPrev.log

AvSvc.log



