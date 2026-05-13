|File<br>metadata|Hidden by default.|
|---|---|
|File events|In versions 22.1.16X and earlier, this section is<br>hidden by default.<br>In versions 22.1.18X and later, this section is<br>available.s|
|Registry<br>events|In versions earlier than 22.1.14X, this section<br>is hidden by default.<br>In versions 22.1.14X and later, this section is<br>available.|




Enable file event collection and add exclusions


File event collection exclusion examples

Related resources

## Enable non-executable file metadata


By default, the Cybereason platform collects file metadata
information about executable files to help analyze those files for


malicious activity. In addition, you can enable the sensor to collect
file metadata for other types of files, including Word files, Excel


files, PowerPoint files, Adobe Acrobat files, and PowerShell

scripts.


**To enable file metadata collection, follow these steps:**


1. In your sensor policy, navigate to the **Collection features**


screen.

2. In the **Collection features** screen, locate the **Non-executable**


**file data collection** section and set the toggle to **On** .
3. Select the file types you want:


Word documents (.doc, .dom, .dot, and .rtf types)

Excel spreadsheets (.xls, .xltm, .and .csv types)


PowerPoint files (.ppt types)
Adobe Acrobat files (.pdf types)


PowerShell scripts (.ps types)

## Enable registry event collection and add


Because attackers and attack techniques often modify the


registry, the Cybereason platform can collect details about registry
key creation, deletion, and modification events for specified


registry keys. You use this data to enrich other data collected by

the Cybereason platform to uncover evidence of a potential


attack.


When you use registry event collection, you should understand


the following terminology:


A **registry key** is the higher level 'folder' that contains registry


values. For example, a registry key could be

_HKLM\Software\Microsoft\Windows\CurrentVersions\RunOnce_ .


Registry keys can contain other keys.
A **registry value** is a 'file' under the higher level key. This is a


specific entry under the registry key.

The **registry path** is the combination of the registry key and


value.


**To enable and configure registry collection, follow these**


**steps:**


1. In your sensor policy, navigate to the **Collection features**


screen.


2. In the **Collection features** screen, locate the **Registry**


**collection** section and set the toggle to **On** .


3. If you have sensors running versions 22.1.149 and later, select


the **Enable Registry collection for sensor versions**

**22.1.14X and later** option.


4. If you have sensors running versions earlier than 22.1.149,


select the **Enable registry collection for sensor versions**


**from 19.2 to 22.1.12X** option.


Note


If you are upgrading your Cybereason environment to

version 22.1.149 and later, this option is visible only if you


previously enabled Registry Events collection. If you did

not have the Registry Events collection section enabled


[previously, open a Technical Support (/s/support) case.](https://nest.cybereason.com/s/support)


After you enable the registry events collection, by default, the


inclusions grid contains a number of registry keys that relate

to autoruns. These registry keys are the default values for


registry event collection.


You can keep the existing keys, exclude all keys, or add your


own registry keys to collect:


To keep the existing keys, make sure you do not delete


the existing registry keys in the grid.

To exclude all registry keys, enter a non-existent registry


key path in the grid. The non-existent registry key ensures

that the platform does not automatically repopulate the


grid with the default system registry keys for collection. If

you leave the grid blank, the platform will repopulate


these keys.

To restore the default system registry keys automatically,


leave the grid completely empty.

5. In the **Add registry key inclusions** section, click **Add new** .


You can add up to 250 registry key inclusions (including the

default entries that your Cybereason platform includes).


6. In the grid, add the registry key to include. The entered key


has a maximum length of 200 characters.


When adding a registry key, you must enter the full explicit


path to the key. The use of wildcards in registry key paths is

not supported.


7. Optionally, to limit the key collection to specific values, in the


**Value** box, enter the values to collect. You can enter up to 5


values.


If you enter multiple values, press the **ENTER** key after each


entry. When you save all your changes, the grid displays

these values as a comma-separated list.


If you do not enter values, all values are collected for the
specified registry key.


8. Optionally, to search for a specific value in all keys and

subkeys of the specified key, select the **Depth** checkbox and


enter the values in the **Value** box.

9. Click the checkmark option to save your changes.


Watch this video to learn more about Registry events collection.

## Registry collection inclusion examples


The table below includes examples for creating inclusions:


|Outcome|Procedure|Example Result|
|---|---|---|
|Collect a<br>key and all<br>values|Add a key but do not add<br>any values.<br>In the Key column, enter<br>the registry key path.<br>Leave the Value column<br>empty.||
|Collect only<br>a single<br>value|You add a key and a<br>single value.<br>1. In the Key column,<br>enter the registry key<br>path.<br>2. In the Value column,<br>enter the registry key<br>value.||
|Collect a<br>key and<br>multiple<br>values|Add a key and the<br>specifc values.<br>1. In the Key column,<br>enter the registry key<br>path.<br>2. In the Value column,<br>enter the values to<br>collect.|In the example,<br>note that one of the<br>values set in the<br>**Value** feld is not<br>collected - this is<br>not a valid value for<br>that registry key<br>and was ignored.|
|Collect<br>specifc<br>values from<br>subkeys|You add a key, select the<br>**Depth** option and enter<br>specifc values:||


## Enable file event collection and add

The sensor can collect details on file events for specific types of


files related to security needs. The sensor collects details when a
file is created, renamed or deleted.


**To enable the file event collection, follow these steps:**


1. In your sensor policy, navigate to the **Collection features**


screen.

2. In the **Collection features** screen, navigate to the **File**


**collection** section and set the toggle to **On** .

3. If you have sensors running versions 22.1.18X and later,


select the **Enable collection for sensor versions 22.1.18X**

**and later** option.


4. If you have sensors running versions 22.1.16X and earlier,


select the **Enable collection for sensor versions 22.1.16X**


**and earlier** option.


Note


If you are upgrading your Cybereason environment to

version 22.1.18X and later, this option is visible only if you


previously enabled File events collection. If you did not

have the File Events collection section enabled previously,


[open a Technical Support (/s/support) case.](https://nest.cybereason.com/s/support)


5. As needed, in the **File event exclusion** grids, click **Add New**


and enter the relevant details to add exclusions to not collect

any events:


Cybereason recommends that you exclude known legitimate
browsers or anti-virus programs because file events from such


programs produce a large amount of data.


**Process name:** The exact process name. To exclude all


events that a process initiates, enter the exact name of

the process, such as **chrome.exe** .


The process name must match the name in the exclusion

exactly. If the names only partially match, the exclusion


does not take effect.

**File or folder path:** The path to a folder or file to exclude.


To exclude events that an item in a folder or file initiate,
specify the path to the folder or file, such as


**C:\Windows\System32\drivers\** or

**C:\Windows\System32\drivers\driver.dll** . This excludes


events initiated by items in the folder or the file.


This match is applied against any path that contains the


specified path. If there are other paths or
subdirectories/folders in the specified exclusion path, the


exclusion takes effect on these paths and files also.

**Process name and path:** A path and a process on that


path. To exclude a specific process in a specific path,

specify both the path and the process name.


Exclusions apply to all file events, including create, delete,
and move/rename events as well as file metadata collection.


Note


Exclusions do not support wildcard characters or the


asterisk character.


Watch a video demo of file events collection:

## File event collection exclusion examples


The table below includes a number of examples for creating

exclusions:








|Process<br>name|Path|Description|
|---|---|---|
|_chrome.exe_||Any event<br>initiated by<br>Chrome.exe<br>across the<br>environment<br>will not be<br>collected.|
||_C:\Users\User1_|Any event<br>associated<br>with this path<br>by any<br>process will<br>not be<br>collected.|


|Process<br>name|Path|Description|
|---|---|---|
|_chrome.exe_|_C:\UsersUser1\Downloads_|Any event<br>initiated by<br>chrome.exe<br>on a fle in<br>the<br>Downloads<br>folder will not<br>be collected.|
|_chrome.exe_|_Downloads_|Any event<br>initiated by<br>chrome.exe<br>on a fle in<br>the<br>_Downloads_<br>folder of any<br>user will not<br>be collected.|
|_chrome.exe_|_C:\Users\User1Downloads\myfle.docx_|Any event<br>initiated by<br>**chrome.exe**<br>on<br>**myfle.docx**<br>in this<br>specifc pah<br>will not be<br>collected.|
|_chrome.exe_|_Downloads\myfle.docx_|Any event<br>initiated by<br>_chrome.exe_<br>on<br>_myfle.docx_<br>in the<br>Downloads<br>folder of any<br>given user<br>will not be<br>collected.|
|_Chrome_||No exclusion<br>added|


|Process<br>name|Path|Description|
|---|---|---|
||_C_|Any event<br>initiated by<br>any process<br>on a fle or<br>folder<br>containing<br>the letter_C_<br>will not be<br>colledted.<br>Cybereason<br>recommends<br>not using<br>this type of<br>exclusion.|
||_C:\_|Any event<br>initiated by<br>any process<br>on a fle or<br>folder under<br>the_C:\_ drive<br>across the<br>environment<br>will not be<br>collected.|
||_.exe_|Any event<br>initiated by<br>any process<br>on any_.exe_<br>fle across<br>the<br>environment<br>will not be<br>collected.|


|Process<br>name|Path|Description|
|---|---|---|
||_.doc_|Any event<br>initiated by<br>any process<br>on a fle<br>containing<br>this<br>extension<br>(including<br>_.docx_,<br>_.docm_, etc.)<br>will not be<br>collected<br>across the<br>environment.|





