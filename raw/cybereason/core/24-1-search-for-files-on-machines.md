The Cybereason platform's file search performs a live file


search and is available only when a machine is online and the

sensor is connected to the Cybereason platform.


**To perform a file search, follow these steps:**


[1. Open a Technical Support (/s/support) to upgrade your](https://nest.cybereason.com/s/support)


environment and add the DFIR package to your environment.

As part of the DFIR package enablement, Live File Search is


also enabled for your environment.
2. After you enable file search, have a user admin assign you the


**Responder L1**, **Responder L2**, or **Local Responder** role (if

your Cybereason environment uses sensor grouping.


Note


If you have the **Responder L1/L2** or **Local Responder**


role required to use the **Live File Search** screen, and then
your role is set to a predefined role, such as **Super user**,


the permission for file search is removed and Technical
Support must re-enable file search access for you.


3. In your Cybereason platform, navigate to the **Live File Search**


screen.


4. Select the **Standard Search** tab.


5. In the **File Properties** section, in the **Name** field, enter the


string for the search. Options for search strings include:


The full file name
Partial file name


File format type
(Version 23.2.163 and later) Multiple file names separated


by a semicolon ( **;** ) character to search for multiple files

with the **OR** operator.


Absolute correct capitalization is not mandatory, as searches

are not case-sensitive.


The Cybereason platform does not find partial matches. If you
are unsure of the full file name, include a wildcard character


**(*)** .


Cybereason searches only by file name, not by the path to the


file.


1. Below the **Name** field, optionally use the relevant field to add


any of the filters to your search:






|File Size|In the Size field, select an operator<br>(Greater than, Less than, Equals, or<br>Between), a file size unit (Bytes, KB,<br>MB, or GB), and a file size.|
|---|---|
|**File creation or**<br>**modifcation**<br>**time**|In the**Time** feld, select**Created** or<br>**Modifed**, an operator (**Before**, **After**,<br>or**Between**), and then enter a time<br>from the calendar widget.<br>On Windows machines, this value is the<br>time when the fle was created. On<br>Linux machines, this value is the time<br>the fle status changed.|
|**Folder**|In the**Folders** feld, enter one or more<br>folder paths, separated by a comma.<br>In the folder path, you can enter<br>specifc paths and/or use environment<br>variables, such as_%userprofle%_ or<br>_C:UsersPublicLibraries_.<br>Using this format enables you to<br>narrow down searches and improve<br>search performance.|



2. In the **Location** section, create a filter to limit the search to

specific machines.


Cybereason recommends that you use this field to limit the
effect the file search has on your servers. If you do not set a


filter for machines for a file search operation, the file search

operation runs on all machines currently connected to your


Cybereason platform.


In the **Machines** field, you can specify machines in a number


of ways:


|Search all<br>machines|In the dropdown list, select All.<br>If you select this option, there is a maximum<br>of 5000 machines for the file search<br>operation.|
|---|---|
|**Search**<br>**machines**<br>**that meet a**<br>**specifc**<br>**flter**<br>**criteria**|In the dropdown list, select**Query**.<br>You should use this option when you know<br>the parameters of a fle search operation,<br>such as machines of a certain operating<br>system, online machines, and so forth.<br>This option enables you to search any<br>machine based on machine<br>characteristics. Available characteristics for<br>fltering include:<br>**Machine name**<br>Machine**FQDN**<br>**Sensor version**<br>**CPU usage**<br>**Memory usage**<br>**OS**<br>**OS version**<br>**Anti-Ransomware mode**<br>**PowerShell mode**<br>**Remote Shell mode**<br>**Data collection** mode<br>**Internal IP address** of the machine<br>**External IP address** of the machine<br>**Isolated** status of the machine<br>**App control mode**<br>**Sensor status**<br>**Service status**<br>**Outdated** status of the machine<br>**Signatures mode** for the Anti-Malware<br>> Signatures mode<br>**Signatures DB version**<br>**Anti-Malware mode**<br>**Exploit Protection mode**<br>**Behavioral doc mode**<br>**Behavioral doc sensitivity**<br>**AI Detect mode**<br>**AI Prevent mode**<br>**Signatures mode origin**<br>For a more detailed description of these<br>options, see Export Sensor Metadata<br>(/s/knowledge-base?article=24-1-export-<br>sensor-<br>metadata&language=en_US#export-<br>sensor-metadata).|


3. Next to the **Search** button, click the clock icon and select the


timeout interval for the file search operation.


Note


If you set a lower timeout interval, the effect on your


server's performance will be lower.


By default, the search timeout is 10 minutes. You can select
any interval from five minutes to sixty minutes and click **Apply** .


The time interval means that the Cybereason platform

performs a simultaneous search on all selected machines, for


up to the time limit specified.

4. Click **Search** .


The Cybereason platform sends the search parameters to the


machines you specified.


Note


The Cybereason platform searches only the file system,

including external drives, but does not search network drives.


The file search operation runs in the background, using only CPU

resources that are not used by other processes. The Cybereason


platform limits CPU usage so as not to interfere with machine
functionality. If the machine is undergoing intensive activity, the file


search operation slows significantly.


While the Cybereason platform searches, view the progress of the


search in the progress bar. Click **Abort** to abort searches that are

in progress. This is useful if you have reached the limit of 10


searches in the queue per sensor, or if a search is taking too long.


You can run up to 10 multiple concurrent searches on any given


machine.


The Cybereason platform displays search results when the


platform finds the file on a machine. For each file, Cybereason
lists the file name, machine, file path, size, and creation and


modification dates:


Note


If your environment uses sensor grouping and you have the

**Local Responder** role assigned for your Cybereason user,


you can view only the results from sensors in the groups to

which you are assigned.


Click **Export results** to download a CSV list of all results.


You can also see the overall success for the file search on the


machines above the results grid:


As the file search runs or after it finished, view the status:


















|Search status|Description|
|---|---|
|Aborted|Search was aborted|
|Aborting|The abort button was pressed, search is<br>being aborted|
|Aborted with too<br>many results|The fle search operation was stopped<br>because too many results were returned.|
|Disconnected|The sensor was disconnected from the<br>Cybereason platform|
|Ended with<br>sensor timeout|No results were returned from the server<br>befor the timeout period was reached.|
|Failed sending|The fle search operation was able to be<br>sent to the sensors.|
|In Progress|Search is in progress|
|Succeeded|File search operation was successful|
|Timeout|The fle search operation reached its<br>timeout period|
|Too many results|Search was aborted since since the<br>results limit was exceeded|
|Unknown sensor|The fle search operation was sent to a<br>sensor that is not recognized by the<br>platform, such as an archived or<br>decommissioned sensor.|



Click **Export search status** to download a CSV list of the statuses
and details on the file search operation for each machine. The


search status export is always available even if there are no
results from the file search operation.


## Perform a file search with YARA rules

You can search for suspicious files using YARA rules. You can


upload a YAR file and filter according to the rules in that file. You
can also use YARA rule searches together with the other filters on


the File search screen.


Note


File search with YARA rules is not supported for machines

running supported versions of Linux on versions 23.1.148 and


earlier.


You use YARA rules to identify:


Malware

IOCs of malware


Any suspicious files that could be a sign of an attack an

analyst would like to identify


YARA rules enable you to use binary patterns to identify malware.
This is helpful in cases where a malware file was slightly tampered


with (e.g. its hash was altered) compared with the file known to

threat intelligence sources, making it hard to detect using other


methods.


**To search with YARA rules, follow these steps:**


1. In the **File search** screen, select the **YARA search** tab.


2. In the **YARA search** tab, in the **YAR file** option section, click


**Upload YAR file** to upload a YAR file containing the YARA
rules to use in the search. The YAR file size must be less than


5 MB.

3. If needed, for the **Time** option, select **Created** or **Modified**, an


operator ( **Before**, **After**, or **Between** ) and then enter a time

from the calendar widget.


4. In the **Size** field, select an operator ( **Greater than**, **Less than**,

**Equals**, or **Between** ), a file size unit ( **Bytes**, **KB**, **MB**, or **GB** )


and a file size.

5. In the **Folders** option, add at least one folder path.


The folder path is necessary since otherwise, the search

would take too much time and resources. A warning is


displayed if no folder is enter and the **Search** button is


disabled without entering a folder path.


6. In the **Location** section, create a filter to limit the search to

specific machines.


Cybereason recommends that you use this field to limit the file
search effect on your servers. If you do not set a filter for


machines for a file search operation, the file search operation

runs on all machines currently connected to your Cybereason


platform.


In the **Machines** field, you can specify machines in a number


of ways:






By default, the search timeout is 10 minutes. You can select
any interval from five minutes to sixty minutes and click **Apply** .


7. Click **Search** .


While the Cybereason platform scans files against the YARA


rules, files are temporarily locked for a few seconds, and end
users cannot delete the file.


For large files, only the first 100 MB of each file is scanned.


If a file takes over 10 seconds to scan, the file search


operation times out and proceeds to the next file.


Note


If your environment uses sensor grouping and you have

the **Local Responder** role assigned for your Cybereason


user, you can view only the results from sensors in the

groups to which you are assigned.


In search results, the **Matched YARA rules** column displays the
YARA rules that matched the rules in the YAR file:



