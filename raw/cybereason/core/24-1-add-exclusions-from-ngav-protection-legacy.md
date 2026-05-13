Exclude files and paths from Anti-Malware

Exclude processes from Anti-Malware


Exclude Behavioral document protection using a rule ID

Exclude behavior ID from Behavioral Document Protection


Exclude paths from Fileless Protection

Exclude domains from Fileless Protection


Exclude detection patterns from Fileless protection

Exclude modules from .NET protection


Exclude processes from Fileless protection with regular

expressions


Exclude processes from Fileless protection

Exclude processes or paths from Behavioral execution


protection

Exclusions by rule ID for Behavioral execution protection


Exclude commands from Anti-Ransomware/Predictive

Ransomware protection


Exclude processes from Exploit protection
Exclude by fingerprint for Variant File Prevention


Exclusion examples


Anti-Malware exclusions


Anti-Ransomware exclusions

Related resources

## Exclude files and paths from Anti

If you find that Anti-Malware continues to generate false positive
detections for a specific folder or file or cause performance


problems on your machine, you can add an exclusion for a
specific file or folder.


**To add an Anti-Malware exclusion, follow these steps** :


1. In your sensor policy, navigate to the **Anti-Malware** screen.


2. In the **Anti-Malware** screen, locate the **Exclusions** section.

3. In the **Exclusions** section, under **Exclude path or file**, click


**Add New** .

4. In the **File/folder name** column, type the path to the file or


folder.


You can also use wildcard characters or environment


variables:


|Method|Details|
|---|---|
|Wildcards|You can use the following wildcard<br>characters:<br>Asterisk (*): When used in a path, the<br>asterisk can match any amount of<br>characters and any value. For example,<br>***:/folder** can match**dijorgidrg:/folder**<br>or**C:\folder**.<br>When using wildcard characters,<br>Cybereason recommends using fle or<br>folder names that are as complete as<br>possible. For example, adding a<br>exclusion with***.docx** or<br>***scriptname.ps1** will exclude the fle.<br>Using a format like**xxxx-*-yyyy**,<br>**myfle*.docx**, ***-yyyy**, **fle_*** will not<br>exclude the fle or folder.<br>Note<br>Previous versions of the<br>documentation used double<br>asterisks (**) in a wildcard example.<br>Using a double asterisk is still valid,<br>however using a single asterisk<br>accomplishes the same task.<br>Question mark (?): Can match one<br>character and any value. For example,<br>**?:/folder** can match**C:\folder** or<br>**D:\folder**.<br>Important<br>Cybereason does not recommend the<br>use of fle extension wildcards to<br>exclude all fles under a fle extension<br>(such as *.exe) as this may expose your<br>system to attacks or breaches. In<br>addition, using fle extension wildcards<br>might affect performance. Cybereason<br>recommends to exclude specifc folders<br>instead of using fle extension wildcards<br>as shown in the following example.|


|Method|Details|
|---|---|
|Environment<br>variables|On Windows endpoints only, you can use<br>the**%ALLUSERSPROFILE%** environment<br>variables in fle and folder exclusions.<br>For example, the following exclusion<br>excludes the**fle.exe** fle with the<br>**%ALLUSERSPROFILE%** variable to<br>specify the user profle folder on all<br>machines.<br>`%ALLUSERSPROFILE%\CustomL`<br>`ogFiles\file.exe`<br>In this example,<br>**%ALLUSERSPROFILE%\CustomLogFiles**<br>indicates the<br>**%PROFILESFOLDER%\Public** or<br>**%PROFILESFOLDER%\all** users folder.<br>For more information on environment<br>variables, see the Microsoft documentation<br>(https://docs.microsoft.com/en-<br>us/windows/deployment/usmt/usmt-<br>recognized-environment-variables).|


Note





All supported operating systems (Windows, macOS, and

Linux) enable you to use both forward slashes and


backslashes for folder or directory paths. However, ensure

you do not add forward slashes and backslashes in the


same exclusion.


5. Click the checkmark () to save the exclusion.


6. Click **Save and Publish** .


For a list of known limitations for exclusions, see Anti-Malware.

## Exclude processes from Anti-Malware


The Cybereason platform excludes a predefined list of trusted

processes that are commonly used by compilers, integrated


developer environments (IDEs), security products, and so on.

These exclusions improve performance in scenarios where


legitimate tools or products trigger multiple alerts. The


Cybereason platform excludes these processes by default, and

no additional action is required.


In addition, you can exclude a specific process from Anti-Malware

scans. This capability is not generally available. To enable and


use this capability, contact your Customer Success Manager.

## Exclude Behavioral document protection

## using a rule ID


When Behavioral document protection analyzes a document, the


Cybereason platform triggers rules that indicate whether any

malicious content was found. For example, the **doc_mal_08** rule


indicates that the Cybereason platform detected malware in a
document. Each rule includes information on a very specific use

case that may apply to several files. Alternatively, the same file

may trigger several rules.


With Behavioral document protection rule exclusions, you specify
rule IDs to disable Behavioral document protection in the specific


scenario indicated by the rule.


For example, a document named


**GeneralCompany_Salaries_2020.xlsx** triggered two rules:


**doc_mal_08**, which indicates that the Cybereason platform


detected malware in the file.

**doc_obf_23**, which indicates that the Cybereason platform


detected an obfuscated macro in the file.


If you add both of the rule IDs in the **Exclude behavioral**


**document rule ID** area, Behavioral document protection ignores
these specific scenarios or behaviors for the


**GeneralCompany_Salaries_2020.xlsx** document and for other

documents with similar behaviors. Behavioral document protection


may analyze this or similar documents in the future, but the code

that was previously found malicious is now ignored.


Note


When your organization begins using Behavioral document


protection, we recommend to initially set **Behavioral**

**document protection** to **Detect**, and then retrieve all of the


rule IDs for the rules triggered in your environment. You can
then use the rule exclusions to indicate which files are trusted


and reduce false positives.


**To add an exclusion for a rule ID, follow these steps:**


1. From in your sensor policy, in the **Anti-Malware** screen, find


the **Behavioral document protection** section.


2. In the **Behavioral document protection** section, in the


**Exclude behavioral document rule ID** area, click **Add New** .


A new row is added to the table.


3. In the **Rule ID** field, type the rule ID.


To retrieve the rule ID, in the relevant Malop, click the


**Document** evidence, and locate the **Properties > Detection**
**value** field. For example, the **Detection value** field displays


the **["doc_aut_09","doc_obf_15"]** value, where the rule IDs

are **doc_aut_09** and **doc_obf_15** .


4. To save, click the check mark (). To cancel, click **x** .


The **Modified by** and **Last modified** fields display the user


name and date for this rule.

5. To add more rule IDs, repeat steps 1-2 for each additional


rule.

## Exclude behavior ID from Behavioral

## Document Protection


You can add exclusions for Behavioral document protection using


the behavior ID displayed in the MalOp. The behavior ID is a hash

value.


**To add an exclusion for a behavioral ID, follow these steps:**


1. In your sensor policy, navigate to the **Anti-Malware** screen.


2. In the **Anti-Malware** screen, find the **Behavioral document**


**protection** section.


3. In the **Behavioral document protection** section, in the


**Exclusions by behavior ID** table, click **Add New** .


4. Add the **Behavior ID** you wish to exclude. Optionally, add a


**Comment** .


5. Click the checkmark () to save the exclusion.

6. Click **Save and Publish** .

## Exclude paths from Fileless Protection


**To add a process exclusion by path, follow these steps:**


1. In your sensor policy, navigate to the **Fileless Protection**


screen.

2. In the **Fileless Protection** screen, navigate to the **Process**


**exclusions** section.

3. In the **Process exclusions** table, click **Add New** .


4. In the **Process name** column, do one of the following:

Type the name of the process including the file extension,


for example: processname.exe.

Enter the path to the process. You must include the **path:**


prefix, for example: **path:c:\temp\file.exe** .


The path exclusions can be regex-based.


Note


You cannot use 2-byte letters (such as Japanese


characters) and underscores ( **_** ) in path exclusions with

regular expressions.


For example, you can enter this exclusion with a regular

expression: **path:c:\john\.*\example.exe** .


With the regular expression, this exclusion would apply to this
file path **c:\john\doe\example.exe** .


Note


It is recommended to validate your regex using a regex


validator.


5. Click the checkmark () to save the exclusion.


6. Click **Save and Publish** .

## Exclude domains from Fileless


If a legitimate PowerShell activity needs to access certain


domains, you can add exceptions for these domains.


**To add a domain exclusion, do the following:**


1. In your sensor policy, navigate to the **Fileless protection**


screen.


2. In the **Fileless protection** screen, locate the **Domain**


**exclusions** section.


3. In the **Domain exclusions** section, click **Add New** .

4. In the **URL/Domain** column, enter the domain name.


Important


The Cybereason platform currently supports exclusions for


domains only, and not for full URLs. For example, exclude the

domain **[s3.amazonaws.com (https://s3.amazonaws.com)](https://s3.amazonaws.com/)**


and not the full URL


**[http://s3.amazonaws.com/example/example](http://s3.amazonaws.com/example/example)**

**[(http://s3.amazonaws.com/example/example)](http://s3.amazonaws.com/example/example)** . If you type a


full URL, the Cybereason platform does not apply the

exclusion.

## Exclude detection patterns from Fileless


If Fileless protection blocks a legitimate command as part of script

analysis, you can add a pattern exclusion to prevent this problem.


You can find the detected pattern to exclude in the **Malicious**

**command** alert in the **Malware alerts** screen, or in the **Pattern**


field in the **MalOp details** screen.


**To add a pattern exclusion, follow these steps:**


1. In your sensor policy, navigate to the **Fileless protection**


screen.


2. In the **Fileless protection** screen, locate the **Script analysis**


section.


3. In the **Script analysis** section, locate the **Pattern exclusions**


option.


4. Above the grid, click **Add New** .

5. In the **Pattern name** column, enter the pattern to exclude.


6. Click the checkmark icon to save the exclusion.

## Exclude modules from .NET protection


If the Cybereason platform is raising false-positive alerts for those


modules or namespaces you identified as non-malicious, you can

exclude the module or namespace.


**To add a module exclusion, follow these steps:**


1. In the **Malops management** screen, locate a **Malicious use**


**of PowerShell Malop**

2. Open the **Details** screen for that MalOp.


3. In the **Details** screen, click the **Loaded modules** field and


locate the name of the module.


For example, the name of the module might be

**program.inception** .


4. In your sensor policy, navigate to the **Fileless protection**


screen.


5. In the **Fileless protection** screen, locate the **Module**


**exclusions** section.


6. In the **Module exclusions** section, above the grid, click **Add**


**New** .


7. Enter the module to exclude, for example,


**program.inception** .


8. Click the checkmark () to save.

## Exclude processes from Fileless

## protection with regular expressions


We recommend using this feature primarily to exclude PowerShell

commands and not the PowerShell process (since PowerShell is


usually only the enabler and not the actual malicious process).


**To add a regular expression process exclusion, follow these**


**steps:**


1. In your sensor policy, navigate to the **Fileless protection**


screen.

2. In the **Fileless protection** screen, locate the **Process**


**exclusions** section.

3. Above the grid, click **Add New** .


4. In the **Process name** column, add the regular expression


exclusion or regular expression pattern exclusion.


Your exclusion must be at least five characters long.


To add an exclusion for a script named


**unnamed_arguments_example_3.ps1**, you add the

exclusion **rgx:unnamed_arguments_example_3.ps1** .


Likewise, to add a regular exclusion pattern exclusion for a

process named **internatltool_v107.exe**, you add **rgx:**


**(InternalTool_v)*(.exe*)** . This format enables the exclusion to

apply to other versions of the tool.


Note


Ensure that you use specific values (process name, script,


etc.) and not common values to ensure that only the
specific process is excluded.


5. Click tbe checkmark () to save the exclusion.


The **rgx:** exclusions analysis is applied at the beginning of the


command line for the first 250 characters.

## Exclude processes from Fileless


If Fileless protection reports a process as malicious, but you know


that the activity is non-malicious, you can add an exclusion for the

process.


**To add a process exclusion, follow these steps:**


1. In your sensor policy, navigate to the **Fileless protection**


screen.


2. In the **Fileless protection** screen, locate the **Process**


**exclusions** section.

3. In the **Process exclusions** section, above the grid, click **Add**


**New** .

4. In the **Process name** column, type the name of the process


including the file extension, for example: **processname.exe** .

5. Click the checkmark () to save the exclusion.

## Exclude processes or paths from

## Behavioral execution protection


If Behavioral execution protection or Variant payload prevention
prevents a legitimate process or processes under a specific


folder, you can add an exclusion for that process or folder.


**To add a process or path exclusion, follow these steps:**


1. In your sensor policy, navigate to the **Behavioral execution**


**protection** screen.


2. In the **Behavioral execution protection** screen, locate and


expand the **Exclude process or path** section.


3. Click **Add New** .

4. In the **File/folder name** column, enter one of the following:


The process name to exclude, for example:

**processname.exe** .


The full path to the process to exclude, for example:

**C:\ExampleFolder\processname.exe** .


The path to the folder under which you want to exclude all

processes, for example: **C:\ExampleFolder** .


Note


The process name and folder path exclusions are not


case-sensitive. In addition, double-byte characters (such

as Japanese characters) cannot be used for folder path


exclusions.


5. Click the check mark () to save the exclusion.


Note


To obtain the process name or path, copy the process name


or locate and copy the path to the relevant process. The
**Command line** field in the Malop might not include the


process name and should not be used for exclusions.


## Exclusions by rule ID for Behavioral

## execution protection

If a specific rule is causing false positive alerts for you, add an


exclusion for this rule ID>


**To add an exclusion for a rule ID, follow these steps:**


1. To find the ID for the rule you want to exclude, do one of the


following:


Locate the relevant **Malicious process behavior** MalOp,

and in the **Malop details** screen, copy the rule ID from the


**Pattern** field.

Select and copy the relevant rule ID from the Rule IDs and


descriptions section.

2. In the sensor policy, in the **Behavioral execution prevention**


section, in the **Exclusions by rule ID** area, click **Add New** .

A new row is added to the table.


3. In the **Rule ID** field, type the rule ID.

4. Click the check mark () to save the rule.


The **Modified by** and **Last modified** fields display the user

name and date for this rule.


5. To add more rule IDs, repeat steps 1-3 for each additional


rule.


You can also delete ( ) or search rule IDs. To search rule IDs, type


the rule ID in the search box and press **ENTER** .

## Exclude commands from Anti

Note


This section is relevant to the **Anti-Ransomware** screen and

the **Predictive ransomware protection** screen. To learn


which ransomware protection type to use according to your

sensor version, see Ransomware protection types per version.


Sometimes, if the Cybereason platform blocks the use of

legitimate programs or commands, you can exclude legitimate


files or commands from Anti-Ransomware or Predictive

Ransomware protection.


**To add an command exclusion, follow these steps:**


1. In your sensor policy, navigate to the **Anti-Ransomware** or


**Predictive ransomware protection** screen

2. In the **Anti-Ransomware/Predictive Ransomware**


**protection** screen, locate the **Exclusions** section.

3. In the **Exclusions** section, above the grid, click **Add New** .


4. In the **Command** column, enter the command name and an


optional description.


The command name must include the exact command line

syntax. For example:


**"C:\Users\12345\AppData\Local\Microsoft\OneDrive\OneDr**

**ive.exe" /background** .


Note


You can use Regex-based expressions or wildcards for


the command name.


To find the command line syntax, locate the MalOp that was


triggered by your legitimate files or commands, and from the

**Processes** tab, click **Investigate** .


Then, in the query results, the command line syntax is visible

in the **Command line** column for each of the suspicious


processes.

5. Click the checkmark () to save the exclusion.

## Exclude processes from Exploit


If you have enabled Exploit protection, you can add an Exploit

protection exclusion to instruct the Cybereason platform not to


apply mitigations to the process. The Cybereason platform then

does not detect or block exploit attempts for the excluded


process.


You cannot add Exploit protection exclusions if you are using the


**Existing endpoint configuration** mode. The **Process**

**exclusions** area is grayed out unless you select either the


**Cautious (OS recommended)** or the **Aggressive (Cybereason**

**recommended)** mode.


Important


Exploit protection exclusions are relevant in cases where


Exploit protection blocks a legitimate process or the process

otherwise incorrectly triggers Exploit protection due to


unexpected behavior. However, excluding a process might

expose the process to potential attacks. Before you exclude a


process because the process seems to be functioning


incorrectly when Exploit protection is enabled, make sure that

the process is not under attack.


**To add a new Exploit protection exclusion, follow these steps:**


1. In your sensor policy, navigate to the **Exploit protection**


screen.

2. In the **Exploit protection** screen, locate the **Process**


**exclusions** area.

3. In the **Process exclusions** area, click **Add New** .


4. In the **Process name** column, enter the process name:


If you are using Windows versions released prior to


Windows 10 Fall Creators Update (Windows 7 SP1,

Windows 8, Windows 8.1, or Windows 10 versions


released prior to the Fall Creators Update), enter the full

path of the process.


If you are using Windows 10 Fall Creators Update and

later versions, enter the full process name or the full path


of the process. The process name is not case-sensitive.

5. Click the check mark () to save the exclusion.

## Exclude by fingerprint for Variant File


You can add exclusions for Variant File Prevention by fingerprint,
to exclude specific scenarios. The fingerprint name is displayed in


the MalOp details screen in the Description area (e.g. BOF

Payload, Conti_Ransomware).


1. In your sensor policy, navigate to the **Anti-Malware** screen.
2. In the **Variant file prevention** section, under **Exclusions by**


**fingerprint**, click **Add New** .
3. Enter the fingerprint to exclude.

## Exclusion examples


The sections below show use-cases or specific examples of how

to add exclusions.

## Anti-Malware exclusions


When you add an exclusion, you can exclude a specific folder, or
use wildcards to exclude files within specific folders, nested


folders, file extensions, and more.


**See the following examples for common exclusion scenarios** :


1. Exclude files in a specific folder
2. Exclude any folder path that contains a specific string


3. Exclude files in a path that ends with a specific folder
4. Exclude files with specific folders within the path


5. Excludes files with a specific file extension in a specific folder


Note


Folder, file, and process names are not case-sensitive.










|Scenario|Description|Exclusion|Col4|
|---|---|---|---|
|1|**Option 1**: Exclude fles<br>under specifcfolder,<br>without nested folders.<br>**Option 2**: Exclude a<br>specifc folder and its<br>nested folders,**on**<br>**Windows endpoints**<br>**using Anti-Malware >**<br>**Signatures mode**<br>**only**.|**Option 1**: Type the folder path, e<br>with a forward slash. For example<br>**/foldera/folderb/folderc/specifc**<br>**Option 2**: Type the folder path in<br>following format, ending with a<br>backslash:**C:\storage\temp\**||
|2|Exclude all paths that<br>contain the<br>**/foldera/specifcfolder/**<br>string.|***/foldera/specifcfolder/***||
|3|Exclude fles and<br>folders under any path<br>that ends with<br>**/program fles/**.|***/program fles/**||
|4|Exclude fles under any<br>path that begins with<br>the**program fles**<br>folder, and includes the<br>**somefolder** folder in<br>the middle of the path.|**/program fles/*/somefolder/***||
|5|Exclude all fles with the<br>**.pkg** extension in any<br>Folder1 folder.|Use one of the following formats.<br>wildcard character is supported i<br>version 21.1.244 and later.<br>1.***/Folder1/*.pkg**<br>2.**?:/Folder1/*.pkg**||
|6|Exclude fles when the<br>location changes|Use the following format:<br>**C:Program fles<folder>*<folde**<br>**<process name**||



