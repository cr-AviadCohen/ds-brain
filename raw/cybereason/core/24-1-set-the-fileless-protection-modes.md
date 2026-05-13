## Select the Fileless protection mode

To help you better tailor your Fileless protection options, the


Cybereason platform uses both the AMSI and .NET modules,

which allow you to choose the type of protection suitable for your


organization. Select the **AMSI** checkbox, **.NET** checkbox, or both

checkboxes.


Note


Cybereason recommends that you use both modules for full


protection, or at least one module for basic protection.


When you select a checkbox for a module, you instruct Fileless


protection to protect your environment from attacks launched by
specific programs and frameworks relevant to that module. Each


module includes PowerShell protection. For more information

about the frameworks and programs that each module protects,


see Protected frameworks and programs.

## Select the .NET module sensitivity level


Note


This feature is available in versions 23.1.8x and later. Sensors


prior to version 23.1.8x will function on Extended mode only.


Select the sensitivity level for the .NET module, as follows:








|Mode|Description|When to use this setting|
|---|---|---|
|Basic|Select this mode to<br>protect PowerShell<br>and PowerShell ISE<br>processes only, as<br>these processes<br>provide the most<br>security value and<br>the highest security<br>risk.|You want to detect<br>and prevent<br>processes with the<br>most security value.<br>You do not want to<br>manage exclusions.<br>When frst enabling<br>Fileless protection,<br>Cybereason recommends<br>the following workfow:<br>1. In the Fileless<br>protection screen, set<br>the .NET module<br>sensitivity level to<br>**Basic** mode.<br>2. Search for legitimate<br>processes monitored<br>by Fileless protection<br>(/s/article/6294276)<br>3. Exclude the legitimate<br>processes.<br>4. Set the .NET module<br>sensitivity level to<br>**Extended** mode.|
|Extended|Select this mode to<br>protect all<br>PowerShell and<br>.NET apps, except<br>for those you<br>excluded.|You want to detect and<br>prevent all processes.<br>Note: Cybereason<br>recommends adding<br>relevant exclusions when<br>selecting this option.|


## Detect and prevent download commands

## and content execution

With Fileless protection, you can analyze activity for specific


malicious use of patterns around script download commands.


**To detect and prevent download commands and content**


**execution, follow these steps:**


1. In the **Fileless protection** screen, navigate to the **Download**


**payload** section.

2. In the **Download payload > Download and execute** section,


define whether the Cybereason platform should detect or

prevent downloaded payloads:


**Disabled**

**Detect:** Detect the sequence of download commands but


does not prevent the command execution

**Prevent** (recommended): Detect and prevent the


download commands

3. In the **Malicious downloads** section, select the option that


you want:


**Disabled**


**Detect:** Detect the execution of Download commands if

they contain an IP or domain that appears in the


reputations list.

**Prevent** (recommended): Detect and prevent the


execution of Download commands if they contain an IP or

domain that appears in the reputations list.

## Analyze scripts


Fileless protection can analyze scripts for potentially malicious

activity, including malicious patterns of text or code.


**To configure script analysis, follow these steps:**


1. In the **Fileless protection** screen, navigate to the **Script**


**analysis** section.
2. In the **Script analysis** section, define whether the


Cybereason platform should detect or prevent malicious

patterns of text or code in various scripts:


**Disabled**

**Detect:** Detect malicious commands and scripts but do


not prevent script execution

**Prevent** (recommended): Detect and prevent malicious


commands and scripts

## Protect against floating module payloads


With Fileless protection, you can prevent floating modules from


loading their payloads.


**To detect and prevent floating module payloads, follow these**


**steps:**
