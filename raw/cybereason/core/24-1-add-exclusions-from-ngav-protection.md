## What exclusions can I add?

When you consider whether to add an exclusion, you often have a


specific program, file, domain, or other item you know can be

exempt from detection and prevention of malicious activity, or that


is causing problems due to false positive detection or prevention.


When you add an exclusion, you can add the following exclusions


for specific types of NGAV detection and prevention:
















|Item|Description|NGAV Engines|
|---|---|---|
|File|A fle or directory|Anti-Malware|
|Process|A process<br>(identifed by<br>process name or<br>directory)|Exploit Protection<br>Fileless Protection<br>Behavioral<br>Execution<br>Prevention|
|Process command<br>line|A command in a<br>process's<br>command line|Predictive<br>Ransomware<br>Protection|
|Domain|A name of a<br>domain (but not<br>specifc URLs in<br>the domain)|Fileless Protection|
|Loaded module|A module loaded<br>by a process,<br>identifed by<br>module name|Fileless Protection|
|Script pattern|A pattern in a<br>script fle|Fileless Protection|
|Fingerprint|A genetic<br>fngerprint for a<br>binary fle found<br>by fle analysis|Anti-Malware<br>(Variant File<br>Prevention)|
|Rule ID|A Rule ID for a<br>specifc detection<br>rule used by<br>Behavioral<br>Document<br>Protection or<br>Behavioral<br>Execution<br>Prevention|Anti-Malware -<br>Rule-based<br>Behavioral<br>Document<br>Protection<br>Behavioral<br>Execution<br>Prevention|


|Item|Description|NGAV Engines|
|---|---|---|
|Behavior ID|An identifer for a<br>behavior identifed<br>by Behavioral<br>Document<br>Protection|Anti-Malware - AI-<br>based Behavioral<br>Document<br>Protection|


## View and filter exclusions

When you open the **Policy exclusions** screen, you can see all


your exclusions that you add (both exclusions that you added

previously and exclusions you add in the **Policy exclusions**


screen).


You can filter these exclusions as needed, both by the **Type** of


exclusion, as well as the protection **Engine** :

## Add an exclusion manually


You can add each exclusion individually as needed in the **Policy**

**exclusions** screen:


**To add an exclusion, follow these steps:**


1. In your sensor policy, open the **Policy exclusions** screen.


Note


If you previously added exclusions in the other sensor

policy screens, you will see the existing exclusions already


displayed in the **Policy exclusions** screen.


2. In the **Policy exclusions** screen, click **New exclusion** .


3. In the **New exclusion** dialog box, in the **Exclusion type** field,


select the type of exclusion to add.


As you select an exclusion type, the Cybereason platform

selects the type of protection engine to which to apply the


exclusion.


If you are adding an exclusion for a protection engine that you


have not enabled yet, the Cybereason platform informs you

that the protection engine is not enabled:


4. In the value field, enter the syntax for the exclusion.


Note


The name of this field updates depending on the type of


exclusion. For example, for a **File (Name or path)**
exclusion, the field is named **File (Name or Path)** .


Likewise, for the **Command line** exclusion, the field is

named **Command line** .


The format of the exclusion differs depending on the type of

exclusion


|Exclusion<br>type|Syntax|
|---|---|
|File (name<br>or path)|Enter one of the following:<br>Path to a specifc directory<br>Full path to a specifc fle (fle names only are not s<br>You can use wildcard characters, including:<br>Asterisk (*****): Add the asterisk in a fle path to match<br>of characters and any value.<br>For example, adding an exclusion***:/folder** will ex<br>**dijorgidrg:/folder** or**C:folder**.<br>Likewise, an asterisk at the end of the exclusion w<br>folders and fles in the path. For example, adding<br>**C:Test(asterisk)** will exclude the subfolders and f<br>C:Testfolder.<br>Note<br>Previous versions of the documentation used do<br>asterisks in wildcard examples. The double aste<br>wildcard examples. The double asterisk syntax i<br>but single asterisks still work for the exclusion.<br>Question mark (**?**): Add a question mark characte<br>character and any value. For example, adding an<br>**?:/folder** matches**C:folder** or**D:folder**.<br>Cybereason does not recommend the use of fle exten<br>to exclude all fles under a fle extension (such as***.ex**<br>expose your system to attacks or breaches. In additio<br>extension wildcards might affect performance. Cybere<br>recommends excluding specifc folders instead of usin<br>extension wildcards.<br>For items on Windows machines, you can use the<br>**%ALLUSERSPROFILE%** environment variables in fle<br>exclusions. For example, adding an exclusion<br>**%ALLUSERSPROFILE%CustomLogFilesfle.exe** wi<br>**fle.exe** fle with the**%ALLUSERSPROFILE%** variable<br>user profle folder on machines.|
|||


|Exclusion<br>type|Syntax|
|---|---|
|Process|Enter one of the following:<br>For**Behavioral Execution Prevention**: The proce<br>path to a process, or a folder path for a specifc d<br>which to exclude ALL processes.<br>Note<br>For behavior-based execution prevention, proce<br>and folder path exclusions are case-insensitive.<br>characters (such as Japanese characters) cann<br>for folder path exclusions.<br>For**Fileless Protection**: Enter the name of the pro<br>including the fle extension (for example,**process**<br>use a regular expression or regular expression pa<br>exclusion.<br>For example, to add an exclusion for a script nam<br>**arguments-example3.ps1**, you add the exclusion<br>**rgx:unnamed-arguments-example3.ps1**.<br>Likewise, to add a regular expression pattern excl<br>process named**internaltool-v107.exe**, you add**r**<br>**(InternalTool-v)*(.exe*)**. Using this format applies<br>to other versions of the tool or process.<br>Note<br>You cannot use 2-byte letters (such as Japanes<br>characters) and underscores (**_**) in path exclusio<br>regular expressions.<br>Note<br>Ensure you use specifc values (process name,<br>in regular expression-based exclusions to ensur<br>specifc process is excluded.<br>For**Exploit Protection**: Enter the full path to the p<br>full process name.<br>Note|


|Exclusion<br>type|Syntax|
|---|---|
||If you are using Windows versions before the Wi<br>Fall Creators Update (Windows 7 SP1, Windows<br>8.1, or Windows 10 before the Fall Creators upd<br>must enter the full path to the process.|
|Command<br>line|Enter the exact command line syntax to exclude. For e<br>could enter a command line like this in quotes:<br>**C:\Users\12345\AppData\Local\Microsoft\OneDrive\**<br>**/background**.<br>If you are unsure of the exact command line syntax, lo<br>MalOp containing the item you want to excuse. In the<br>the MalOp details, click**Investigate**. In the query resu<br>display, the command line syntax displays in the**Com**<br>column for the process.<br>You can use Regex-based expressions or wildcards fo<br>command name for Predictive Ransomware Protection|
|Domain|Enter the domain name.<br>The exclusion must be a domain name, but not a full U<br>example, you would enter**s3.amazonaws.com**<br>**(https://s3.amazonaws.com)** instead of the URL<br>**https://s3.amazonaws.com/example/example**<br>**(https://s3.amazonaws.com/example/example)**.<br>If you enter a full URL, the Cybereason platform does<br>exclusion for the domain in the URL.|
|Floating<br>module|Enter the full module name. For example, you could en<br>**program.inception**.<br>If you are unsure of the module name, in a**Malicious**<br>**PowerShell** MalOp, open the**MalOp details** screen, a<br>**Loaded modules** feld. The name of the module you n<br>found in that feld.|
|Rule ID<br>(for<br>Behavioral<br>Document<br>Protection)|Add the rule ID the Cybereason platform uses for the<br>triggered the false positive detection.<br>The rules use a format like**doc_aut_09** or**doc_obf_1**<br>If you are unsure of the rule name, in the MalOp in que<br>navigate to the**Document** section and fnd the**Prope**<br>**Detection** value feld. The detection rule is in that feld|
|||


|Exclusion<br>type|Syntax|
|---|---|
|Behavior<br>ID|Add the behavior ID the Cybereason platform uses for<br>triggered the false positive detection.<br>The Behavioral ID is a hash value.<br>If you are unsure of the rule name, in the MalOp in que<br>navigate to the**Document** section and fnd the**Prope**<br>**Detection** value feld. The detection rule will be in that|
|Rule ID<br>(for<br>Behavioral<br>Execution<br>Prevention)|The exact text of the rule ID for the behavior to exclud<br>The rule ID uses a syntax like**accessibility_features**.<br>If you are unsure of the rule ID, in the**Malicious proce**<br>MalOp details screen, locate the**Pattern** feld. The rul<br>feld.|
|Fingerprint|The exact name for the fngerprint to exclude.<br>If you are unsure of the fngerprint name, in the MalOp<br>MalOp, in the**Description** feld, fnd the fngerprint na|
|Pattern|The exact pattern name.<br>If you are unsure of the pattern name, in the**Malicious**<br>alert in the**Malware alerts** screen or in the**Pattern** fe<br>MalOp details for the MalOp, fnd the fngerprint name|
|<br>Rule ID (for<br>Behavioral<br>Execution<br>Prevention)<br>The exact text of the rule ID for the<br>behavior to exclude.<br>The rule ID uses a syntax like<br>**accessibility_features**.<br>If you are unsure of the rule ID, in the<br>**Malicious process behavior** MalOp<br>details screen, locate the**Pattern** feld.<br>The rule ID is in that feld.<br>Fingerprint<br>The exact name for the fngerprint to<br>exclude.<br>If you are unsure of the fngerprint name,<br>in the MalOp details for the MalOp, in the<br>**Description** feld, fnd the fngerprint<br>name.|<br>Rule ID (for<br>Behavioral<br>Execution<br>Prevention)<br>The exact text of the rule ID for the<br>behavior to exclude.<br>The rule ID uses a syntax like<br>**accessibility_features**.<br>If you are unsure of the rule ID, in the<br>**Malicious process behavior** MalOp<br>details screen, locate the**Pattern** feld.<br>The rule ID is in that feld.<br>Fingerprint<br>The exact name for the fngerprint to<br>exclude.<br>If you are unsure of the fngerprint name,<br>in the MalOp details for the MalOp, in the<br>**Description** feld, fnd the fngerprint<br>name.|


|Rule ID (for<br>Behavioral<br>Execution<br>Prevention)|The exact text of the rule ID for the<br>behavior to exclude.<br>The rule ID uses a syntax like<br>accessibility_features.<br>If you are unsure of the rule ID, in the<br>Malicious process behavior MalOp<br>details screen, locate the Pattern field.<br>The rule ID is in that field.|
|---|---|
|Fingerprint|The exact name for the fngerprint to<br>exclude.<br>If you are unsure of the fngerprint name,<br>in the MalOp details for the MalOp, in the<br>**Description** feld, fnd the fngerprint<br>name.|


5. In the **Description**, enter a meaningful description.


6. If needed, in the **Assign to engine** field, select the protection


engines to which the exclusion applies.


If the exclusion is valid for only one type of protection engine,


you do not need to select an engine value. The Cybereason

platform automatically applies the exclusion to the one


protection engine type.


7. Click **Create** .


8. In your sensor policy, click **Save and publish** to ensure the


exclusions take effect.


The Cybereason platform adds the exclusion to the list of

exclusions in the table. In addition, the Cybereason platform adds


the exclusion in the relevant section of the sensor policy, such as

adding **File** exclusions in the **Anti-Malware** screen.


You can later edit or delete any exclusion. In the row for the

exclusion, click the three dot at the right side of the row and select


**Edit** or **Delete** .

## Import exclusions from a CSV file


If you have exclusions that you are adding from a different sensor


policy or you want to manage exclusions separately for all sensor
policies in your organization, you can import a CSV file containing


exclusion details. This enables you to easily add exclusions for all


sensor policies at scale, instead of needing to manually create

each exclusion in each sensor policy.


**To import exclusions, follow these steps:**


1. If needed, in the **Policy exclusions** screen in the sensor


policy from which you want to use the existing exclusions, at

the right of the **Add exclusion** button, click the three dots and


select **Export to CSV** .


A CSV file downloads to your machine.

2. If you do not have existing exclusions, click **Download a CSV**


**template** to download the CSV template file you can use to

add exclusions.


3. In the CSV file, ensure the file has a header row with four


columns:


type

value


description

engines


4. In a new row for a new exclusion, in the **type** column, add the


type of exclusion. You must use one of these values:


file

processBep


processFilelessProtection

processExploitProtection


command

domain


module

ruleId


ruleIdbBep

behaviorID


fingerprint

pattern


5. In the same row, in the **value** column, enter the value to


exclude. The format of the exclusion differs depending on the


type of exclusion:


|Exclusion<br>type|Syntax|
|---|---|
|File (name<br>or path)|Enter one of the following:<br>Path to a specifc directory<br>Full path to a specifc fle<br>You can use wildcard characters, including:<br>Asterisk (*****): Add the asterisk in a fle path to match<br>of characters and any value.<br>For example, adding an exclusion***:/folder** will ex<br>**dijorgidrg:/folder** or**C:folder**.<br>Likewise, an asterisk at the end of the exclusion w<br>folders and fles in the path. For example, adding<br>**C:Test(asterisk)** will exclude the subfolders and f<br>C:Testfolder.<br>Note<br>Previous versions of the documentation used do<br>asterisks in wildcard examples. The double aste<br>wildcard examples. The double asterisk syntax i<br>but single asterisks still work for the exclusion.<br>Question mark (**?**): Add a question mark characte<br>character and any value. For example, adding an<br>**?:/folder** matches**C:folder** or**D:folder**.<br>Cybereason does not recommend the use of fle exten<br>to exclude all fles under a fle extension (such as***.exe**<br>expose your system to attacks or breaches. In addition<br>extension wildcards might affect performance. Cybere<br>recommends excluding specifc folders instead of usin<br>extension wildcards.<br>For items on Windows machines, you can use the<br>**%ALLUSERSPROFILE%** environment variables in fle<br>exclusions. For example, adding an exclusion<br>**%ALLUSERSPROFILE%CustomLogFilesfle.exe** wil<br>**fle.exe** fle with the**%ALLUSERSPROFILE%** variable<br>user profle folder on machines.|
|||


|Exclusion<br>type|Syntax|
|---|---|
|Process|Enter one of the following:<br>For**Behavioral Execution Prevention**: The proce<br>path to a process, or a folder path for a specifc d<br>which to exclude ALL processes.<br>For**Fileless Protection**: Enter the name of the pro<br>including the fle extension (for example,**process**<br>use a regular expression or regular expression pa<br>exclusion.<br>For example, to add an exclusion for a script name<br>**arguments-example3.ps1**, you add the exclusion<br>**rgx:unnamed-arguments-example3.ps1**.<br>Likewise, to add a regular expression pattern excl<br>process named**internaltool-v107.exe**, you add**rg**<br>**(InternalTool-v)*(.exe*)**. Using this format applies<br>to other versions of the tool or process.<br>Note<br>You cannot use 2-byte letters (such as Japanese<br>characters) and underscores (**_**) in path exclusio<br>regular expressions.<br>Note<br>Ensure you use specifc values (process name,<br>in regular expression-based exclusions to ensur<br>specifc process is excluded.<br>For**Exploit Protection**: Enter the full path to the p<br>full process name.<br>Note<br>If you are using Windows versions before the Wi<br>Fall Creators Update (Windows 7 SP1, Windows<br>8.1, or Windows 10 before the Fall Creators upd<br>must enter the full path to the process.|
|||


|Exclusion<br>type|Syntax|
|---|---|
|Command<br>line|Enter the exact command line syntax to exclude. For e<br>could enter a command line like this in quotes:<br>**C:\Users\12345\AppData\Local\Microsoft\OneDrive\**<br>**/background**.<br>If you are unsure of the exact command line syntax, lo<br>MalOp containing the item you want to excuse. In the<br>the MalOp details, click**Investigate**. In the query resu<br>display, the command line syntax displays in the**Com**<br>column for the process.|
|Domain|Enter the domain name.<br>The exclusion must be a domain name, but not a full U<br>example, you would enter**s3.amazonaws.com**<br>**(https://s3.amazonaws.com)** instead of the URL<br>**https://s3.amazonaws.com/example/example**<br>**(https://s3.amazonaws.com/example/example)**.<br>If you enter a full URL, the Cybereason platform does<br>exclusion for the domain in the URL.|
|Floating<br>module|Enter the full module name. For example, you could en<br>**program.inception**.<br>If you are unsure of the module name, in a**Malicious u**<br>**PowerShell** MalOp, open the**MalOp details** screen, a<br>**Loaded modules** feld. The name of the module you n<br>found in that feld.|
|Rule ID<br>(for<br>Behavioral<br>Document<br>Protection)|Add the rule ID the Cybereason platform uses for the r<br>triggered the false positive detection.<br>The rules use a format like**doc_aut_09** or**doc_obf_15**<br>If you are unsure of the rule name, in the MalOp in que<br>navigate to the**Document** section and fnd the**Prope**<br>**Detection** value feld. The detection rule is in that feld|
|Behavior<br>ID|Add the behavior ID the Cybereason platform uses for<br>triggered the false positive detection.<br>The Behavioral ID is a hash value.<br>If you are unsure of the rule name, in the MalOp in que<br>navigate to the**Document** section and fnd the**Prope**<br>**Detection** value feld. The detection rule will be in that|
|||


|Exclusion<br>type|Syntax|
|---|---|
|Rule ID<br>(for<br>Behavioral<br>Execution<br>Prevention)|The exact text of the rule ID for the behavior to exclude<br>The rule ID uses a syntax like**accessibility_features**.<br>If you are unsure of the rule ID, in the**Malicious proce**<br>MalOp details screen, locate the**Pattern** feld. The rule<br>feld.|
|Fingerprint|The exact name for the fngerprint to exclude.<br>If you are unsure of the fngerprint name, in the MalOp<br>MalOp, in the**Description** feld, fnd the fngerprint na|
|Pattern|The exact pattern name.<br>If you are unsure of the pattern name, in the**Malicious**<br>alert in the**Malware alerts** screen or in the**Pattern** fe<br>MalOp details for the MalOp, fnd the fngerprint name|
|Optionally, in the**description** column, enter a meaningful<br>description.<br>Optionally, in the**engines** column, add the engine that is<br>relevant for your exclusion:<br>**Exclusion type**<br>**Value for engines column**<br>fle<br>antiMalware<br>processBep<br>behavioralExecutionPrevention<br>processFilelessProtection<br>flelessProtection<br>processExploitProtection<br>exploitProtection<br>command<br>predictiveRansomwareProtection<br>antiRansomware<br>domain<br>flelessProtection<br>module<br>flelessProtection<br>ruleId<br>antiMalware<br>ruleIdBep<br>behavioralExecutionPrevention<br>behaviorId<br>antiMalware|Optionally, in the**description** column, enter a meaningful<br>description.<br>Optionally, in the**engines** column, add the engine that is<br>relevant for your exclusion:<br>**Exclusion type**<br>**Value for engines column**<br>fle<br>antiMalware<br>processBep<br>behavioralExecutionPrevention<br>processFilelessProtection<br>flelessProtection<br>processExploitProtection<br>exploitProtection<br>command<br>predictiveRansomwareProtection<br>antiRansomware<br>domain<br>flelessProtection<br>module<br>flelessProtection<br>ruleId<br>antiMalware<br>ruleIdBep<br>behavioralExecutionPrevention<br>behaviorId<br>antiMalware|


|Exclusion type|Value for engines column|
|---|---|
|fle|antiMalware|
|processBep|behavioralExecutionPrevention|
|processFilelessProtection|flelessProtection|
|processExploitProtection|exploitProtection|
|command|predictiveRansomwareProtection<br>antiRansomware|
|domain|flelessProtection|
|module|flelessProtection|
|ruleId|antiMalware|
|ruleIdBep|behavioralExecutionPrevention|
|behaviorId|antiMalware|



