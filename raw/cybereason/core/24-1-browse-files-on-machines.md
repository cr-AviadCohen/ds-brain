To enable the DFIR package, you must upgrade your


environment. You cannot enable the DFIR package on an

existing version without a version upgrade.


After you purchase the DFIR package, in order to browse files on

[a machine, you must open a Technical Support (/s/support) case](https://nest.cybereason.com/s/support)


to upgrade your environment and enable the DFIR package to

your environment.

## Assign the appropriate role


The ability to see the Browse Files feature to browse file systems is

available for users with the Responder L2 role.


User admins assign the **Responder L2** role to Cybereason users

from the **Users** screen.


Note


Users with the Responder L2 role cannot be assigned the


**Sensor Admin L1**, **Local Analyst L1**, **Local Analyst L2**, or

**Local Responder** roles.

## Browse files from the Element Details

## screen


When running investigation queries, you can browse files on a
machine through the Element **Details** pane for a specific machine.


Note


You can only browse the file system for machines that are


currently online.


**To browse files from the Element Details screen, follow these**


**steps:**


1. Access the Element **Details** pane using one of the following


options:


|Option|Steps|
|---|---|
|Option<br>1|a. From the**Investigation** screen, build a<br>query based on the**Machine** Element.<br>You can add flters for the**Machine** Element<br>as needed, or add other Elements in the<br>query. However, before you run the query to<br>retrieve results, ensure you select the<br>**Machine** Element.<br>b. Double-click a machine in the query results.<br>The Element**Details** pane appears for that<br>machine.|
|Option<br>2|a. Navigate to the**System > Sensors** screen<br>b. Select a sensor.<br>c. Above the sensor list, click**Actions** and<br>select**Investigate**. The**Details** pane<br>appears for that machine.|



2. In the **Details** pane, to the right of the machine name, you will


see the option to Browse files:


3. Click **Browse files** . The Cybereason platform opens the file


directory in a separate tab:


4. Navigate around the file directory as needed.


## Browse files during a file search

The Live File search feature also allows you to browse through


folders and files on a machine. This is useful in cases where you
are aware that there is suspicious activity on a specific machine,


or within a specific folder on a machine.


**To browse and download files from file search results, follow**


**these steps:**

[1. Run a live file search (/s/knowledge-base?article=24-1-](https://nest.cybereason.com/s/knowledge-base?article=24-1-search-for-files-on-machines&language=en_US#search-for-files-on-machines)


[search-for-files-on-machines&language=en_US#search-for-](https://nest.cybereason.com/s/knowledge-base?article=24-1-search-for-files-on-machines&language=en_US#search-for-files-on-machines)
[files-on-machines).](https://nest.cybereason.com/s/knowledge-base?article=24-1-search-for-files-on-machines&language=en_US#search-for-files-on-machines)


2. In the results list for a file search operation, click the folder


icon.


A new browser tab opens, displaying the root of the file

structure on the machine. This is the same location displayed


when a user navigates to My Computer on their machine.


Note


You can view a maximum of 1000 files by default. Open a

[Technical Support (/s/support) ticket to increase this limit.](https://nest.cybereason.com/s/support)


Folders are indicated with a **+** symbol before the name. Click

a folder to display the folder contents.


3. To download a file, click the file. The Cybereason platform

downloads the file to your local machine.


You cannot download critical OS files, or files that are in use
or locked for reading. The maximum file size for the download


is 2 GB.


Note


The downloaded file is not stored on Cybereason servers.


When you open the downloaded archive folder, ensure you


use a program, such as Zip or WinRAR, that enable you to

open (not extract) and view the folder contents and add a


password as part of their standard use.

4. To navigate to a Windows shortcut destination:


a. Download the shortcut file.
b. Retrieve the target path from the file properties.


c. Update the URL with the target path.


Note


|If you receive any errors during browsing, please consult<br>Technical Support.<br>Filter file search browsing results<br>You can filter the results displayed in the browser window by<br>adding query strings to the end of the URL in your address bar.<br>This can be helpful for narrowing down results in folders with a<br>large number of files.<br>For example, you can enter this query string to search for the file<br>Techpub.txt in the C:/s/support folder:<br>https://46.155.122.10/c:/support?find=Techpub.txt<br>(https://46.155.122.10/c:/support?find=Techpub.txt)<br>If the file Techpub.txt exists in this folder, only it will be displayed.<br>Query string filters include:|Col2|Col3|
|---|---|---|
|**Query String**|**Description**|**Examples**|
|?fnd=<string>|Searches<br>for fle<br>name(s)<br>that match<br>the string<br>value.<br>You can use<br>the special<br>characters:<br>* and**?** in<br>your search,<br>as follows:<br>***** - wildcard<br>for one or<br>more<br>characters.<br>? - wildcard<br>for one<br>character.|**?fnd=*.bak**<br>Displays all the fles with a**.bak**<br>extension.<br>**?fnd=exam?le.pdf**<br>Displays all the fles that match the<br>string, such as:<br>_example.pdf_<br>_examsle.pdf_|
||||


|Query String|Description|Examples|
|---|---|---|
|?limit=<br><number>|Limits the<br>results<br>displayed to<br>a specifc<br>number of<br>results.|**?limit=50**<br>Displays the frst 50 fles/folders in the<br>folder.<br>If you do not enter a limit, the default<br>limit is 1000. The maximum limit is<br>20000.|
|?fles=true|Displays<br>only fles in<br>the results,<br>and not<br>folders.||
|?<br>directories=true|Displays<br>only folders<br>in the<br>results, and<br>not fles.||
|?creationafter=<br><epoch time>|Displays<br>fles that<br>were<br>created<br>after the<br>specifed<br>time. Use<br>epoch time<br>format (The<br>number of<br>seconds<br>that have<br>elapsed<br>since<br>00:00:00<br>Coordinated<br>Universal<br>Time (UTC),<br>Thursday, 1<br>January<br>1970, not<br>counting<br>leap<br>seconds)|**?creationafter=1492068983**<br>Displays fles and folders created afte<br>the specifed time.|
||||


|Query String|Description|Examples|
|---|---|---|
|?modifedafter=<br><epoch time>|Displays<br>fles that<br>were<br>modifed<br>after the<br>specifed<br>time. Use<br>epoch time<br>format.|**?creationafter=1492068983**<br>Displays fles and folders modifed<br>after the specifed time.|
|<query<br>string>&<query<br>string>|You can<br>concatenate<br>multiple<br>query<br>strings<br>using the &<br>symbol.|**?**<br>**fnd=*.txt&creationafter=1492068983**<br>Displays all fles with a .txt extension<br>that were created after the specifed<br>time.|





