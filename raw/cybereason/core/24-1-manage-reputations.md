## What items can you add to your custom

You can add custom reputations for the following items:


|Item|Item type|Example|
|---|---|---|
|File|File hash (MD5,<br>SHA-1, or SHA-<br>256)<br>Note<br>To ensure that<br>the<br>Cybereason<br>platform is<br>able to allow<br>or block SHA-<br>1/SHA-256<br>hash values<br>and also add<br>these hash<br>values to the<br>allowlist or<br>blocklist, you<br>must have the<br>Threat Intel<br>service<br>enabled in<br>your<br>environment.<br>Contact your<br>Customer<br>Success<br>Manager to<br>enable this<br>feature.<br>If you do not<br>have the<br>Threat Intel<br>service<br>enabled, the<br>SHA-1 or SHA-<br>256 fle hash<br>values are still<br>prevented by<br>the sensor, but<br>the values are<br>not added to<br>the allowlist.|3f63e9f09fe59f5|


|Item|Item type|Example|
|---|---|---|
|Process|File hash (MD5,<br>SHA-1, or SHA-<br>256)|cc273fe9d442850|
|Domain (not<br>including<br>subdomains)|Domain|mydomain.com<br>(https://mydomain.com).<br>The platform triggers a<br>MalOp for an exact<br>match of the domain<br>name, and does not<br>trigger a MalOp for<br>subdomains.|
|IP address|IP address|198.20.10.54|

## Reputation management options

You manage your custom reputation list from the **Reputations**


screen. You can also set reputations for specific items during

investigation using the **Element details** pane.


Likewise, if you use Cybereason XDR, XDR response actions may

also add IP addresses to the blocklist automatically.


The following table describes reputation options:










|Desired<br>Platform<br>Response|How to configure|Description|
|---|---|---|
|**Allow:** Do<br>not trigger a<br>MalOp for<br>this item|Perform one of the<br>following:<br>Add the item<br>using the<br>**Reputations**<br>screen and set<br>Action to**Allow**<br>Add the item to<br>a CSV fle with<br>**whitelist** in the<br>**reputation**<br>column|The item may appear<br>in other MalOps if the<br>item takes part in the<br>malicious activity. For<br>example, if a process<br>in the custom<br>reputation list injects<br>into another process,<br>a MalOp of type<br>**Injected Process**<br>may be generated.|


|Desired<br>Platform<br>Response|How to configure|Description|
|---|---|---|
|**Detect only:**<br>Trigger a<br>MalOp for<br>this item, but<br>do not<br>prevent it<br>from<br>executing|Perform one of the<br>following:<br>Add the item<br>using the<br>**Reputations**<br>screen and set<br>Action to**Detect**<br>**Only**<br>Add the item to<br>a CSV fle with<br>**blacklist** in the<br>**reputation**<br>column and<br>**False** in the<br>**Prevent**<br>**execution**<br>column|The Cybereason<br>platform creates a<br>MalOp for all<br>occurrences of the<br>item currently in the<br>environment, as well<br>as all subsequent<br>instances of the item.<br>The item name<br>appears as the root<br>cause of the MalOps.<br>In environments with<br>sensor grouping<br>enabled, if you add a<br>group assignment for<br>this reputation, the<br>Cybereason platform<br>triggers a MalOp only<br>if the item for the<br>reputation is part of a<br>sensor group to which<br>you are assigned.|
|**Detect and**<br>**prevent:**<br>Trigger a<br>MalOp for<br>this item, and<br>prevent it<br>from<br>executing|Perform one of the<br>following:<br>Add the item<br>using the<br>**Reputations**<br>screen and set<br>Action to**Detect**<br>**& Prevent**<br>Add the item to<br>a CSV fle with<br>**blacklist** in the<br>**reputation**<br>column and<br>**True** in the<br>**Prevent**<br>**execution**<br>column.|You must have<br>Application Control<br>enabled to block<br>items from executing.<br>In environments with<br>sensor grouping<br>enabled, if you add a<br>group assignment for<br>this reputation, the<br>Cybereason platform<br>triggers a MalOp only<br>if the item for the<br>reputation is part of a<br>sensor group to which<br>you are assigned.|


Important








Be careful when setting reputations for critical applications


such as cmd.exe, explorer.exe, and PowerShell. Detecting or

preventing these applications may cause legitimate processes


to trigger MalOps.


Note


Changing the reputation of an item will not affect the status of

previously created MalOps. However, if the item is involved in


other MalOps, the reputation update will be reflected in the

details of new MalOps.

## Manage reputations in the Reputations

## screen


In the **Custom Reputation List** tab, you can perform the following


tasks:


1. Filter by one or more of the following properties:








|Property|Items to Update|
|---|---|
|Type|IP address<br>Domain<br>File Hash|
|Action|Allow<br>Detect Only<br>Detect & Prevent|
|Expiration|Active<br>Expired|



2. Search your custom reputation list by value or description.


3. Add a new item.

4. Edit or delete an item.


5. Change a reputation using the **EDR Action** column.


6. Upload a CSV file, download a CSV template, or export the


items to a CSV file.

## Add an item


To add an item, such as an IP address or domain, to your custom


reputation list, follow these steps:


1. From the **Reputations** screen **Custom Reputation List** tab,


select **Add item** . The **Add Reputation Item** window appears:


2. Select the type of item you want to add.

3. Add the value, such as the domain name.


4. For the **EDR Action**, select an action. Options include:


**Allow** : The platform does not trigger a MalOp when it


encounters this item.

**Detect Only** : The platform triggers a MalOp when it


encounters this item.

**Detect & Prevent** : The platform triggers a MalOp when it


encounters this item. In addition, the platform prevents the

item from executing.


Note


If you have Cybereason XDR in your environment, you


cannot set a value for the **XDR Action** . Cybereason XDR

sets this value when performing a response action in an


XDR MalOp.


5. (Optional) Add a description.


6. (Optional) Add an expiration date. The expiration date is the


date at which the item will be removed from the custom


reputation list. The date displayed in the UI reflects the local

timezone.


Note


Because the platform checks the expiration date every


few hours, the item may not expire on the exact date that
you specified.


7. Click **Save** .


If two or more hash values point to the same item, the Cybereason


platform will combine these values into one record in the custom
reputation list. For example, if a file's MD5 hash is marked as


allowed and you allow an SHA-1 hash value that points to the
same file, the platform will add the second hash value to the


existing record instead of creating a new entry in the reputation
list. Furthermore, when a file runs on a sensor, the sensor


calculates the MD5, SHA-1, and SHA-256 values for the file. The
platform will add the file hash values that match with the existing


hash value (if the existing hash value is in the list of custom

reputations).

## Edit or delete an item


To edit a reputation, select an option from the drop-down menu in

the **Action** column.


**To edit the properties for an item, follow these steps:**


1. Select the checkbox to the left of the item. The **Edit** button


appears above the list.

2. Select **Edit** and make your changes.


3. Click **Save** .


**To delete an item from a custom reputation list, follow these**


**steps:**


1. Select one or more check boxes to the left of the items. The


**Delete** button appears above the list.


Note


Use the **Shift** key and select two check boxes to activate


all check boxes between the two selected.


2. Select **Delete** .


3. Confirm deletion.

## Manage reputations in bulk using a CSV


You can manage reputations in bulk by uploading a CSV file that


contains reputation information. You can download a CSV

template to get started, or download your current custom


reputation list to make updates. These files are available in the

**Reputation** screen:


Important


Cybereason is in the process of changing the terms "blacklist"


and "whitelist" to "blocklist" and "allowlist", respectively.
Currently, these changes are not reflected in the CSV template


and you must use the terms "blacklist" and "whitelist" when

updating reputations in bulk.


The CSV template file includes the following columns:








|Column|Description|
|---|---|
|**Key**|The item's IP address, domain, or hash. Values<br>entered in this column are case-insensitive and<br>are saved by the system in lowercase.|
|**Reputation**|The reputation you are applying to the item.<br>Enter**whitelist** to add or remove the relevant<br>item to the allowlist. Enter 'blacklist' to add or<br>remove the item to the blocklist. You specify<br>whether to add or remove the item in the<br>**Remove** column.|
|**Prevent**<br>**execution**|An option to prevent the item's execution. You<br>must have Application Control enabled for<br>prevention to work.<br>This option is only applicable for fle hash keys.|
|**Comment**|A comment related to the reputation<br>classifcation.|


|Column|Description|
|---|---|
|**Remove**|Indicates whether or not the item should be<br>removed from the list specifed in the<br>**Reputation** column.**True** means the item<br>should be removed from the specifed list.<br>**False** means the item should stay on the list, or<br>be added to the list if the item is a new entry.|
|**Expiration**<br>**date**|The date and time, according to UTC, on which<br>the platform will remove the item from the<br>reputation list. The date must be in the date<br>format**yyyy-mm-dd hh:mm:ss**.|



The columns in the CSV template are slightly different from the


columns in the **Custom Reputation List** screen. The following

table describes how the CSV columns correlate to values in the


UI:













|UI Values|CSV Values|
|---|---|
|Value|Key|
|EDR Action: Allow|reputation:**whitelist**<br>Remove: 'False'|
|EDR Action: Detect|reputation:**blocklist**<br>Prevent execution:**False**<br>Remove:**False**|
|EDR Action: Detect &<br>Prevent|reputation:**blocklist**<br>Prevent execution:**True**<br>Remove:**False**|
|Description|Comment|
|Expiration Date (local<br>time)|Expiration Date (**yyyy-mm-dd**<br>**hh:mm:ss** format and UTC)|
|Created by|N/A|


Note


On Mac, editing the CSV using the Numbers application may


cause the CSV to have an unsupported format. Cybereason

recommends using TextEdit or editing on Windows instead.


**To add or remove items in bulk, follow these steps:**

1. Download your reputation CSV file from the **Reputations**


screen. If you are adding items for the first time, download the

custom reputation list CSV template.


2. In the CSV file, specify the key for the item to add or remove

from a custom reputation list in the **Key** column of the CSV file.


3. In the **reputation** column, specify the custom reputation list to


which you want to add or remove the item in the Key column.


Enter **whitelist** to prevent the item from triggering a MalOp, or

_blacklist_ if you want the item to always trigger a MalOp. See


the **Important** note above for an explanation of CSV terms.

4. In the **remove** column, specify whether or not the item in the


**Key** column should be removed from the custom reputation
list specified in the **Reputation** column. Enter **false** to add the


item, or **true** to remove the item.

5. In the **prevent execution** column, specify whether or not you


want the Cybereason platform to prevent the item from

executing.


6. Optionally, in the **expiration date** column, specify a time and


date to remove the item from the custom reputation list. When


editing this value in the CSV column, use the date format

**yyyy-mm-dd hh:mm:ss** .


Note


In the CSV file, the **expiration date** uses Coordinated


Universal Time (UTC). The platform translates this time to

local time in the UI, however you must specify the UTC


date/time in the CSV file.


7. From the **Reputations** screen, upload the revised CSV file for


your changes to take effect.


The Cybereason platform validates the values in the CSV file and


presents an error message if items are invalid. For example:


**CSV Example**


In the following example, the Cybereason platform will remove the


hash **3f63e9f09fe59f5** from the custom reputation list. The

platform will add the IP address **198.20.10.54** to the custom


reputation list and trigger a MalOp when it encounters the item.



|key|reputation|prevent<br>execution|comment|remove|
|---|---|---|---|---|
|3f63e9f09fe59f5|whitelist|FALSE|my<br>comment<br>on hash|TRUE|
|198.20.10.54|blacklist|FALSE|my<br>comment<br>on ip|FALSE|


Note







If an item already exists in a list, the configuration in the CSV
file will replace the current configuration.

## Manage reputations from the Element

## details screen


You can also set the reputation for a single item from the **Element**

**details** pane in the **Investigation** screen. You can access an


item's element details from the **Malop details** screen in the

associated MalOp, or by building a query in the **Investigation**


**screen** .

## Access an item's Element details pane

## from the Malop details screen


1. If needed, from the **Malops management screen**, select the


MalOp associated with the item you want to add or remove

from the allowlist or blocklist. The **Malop details** screen


appears.

2. From the **Process** tab, select the process to add to or remove


from the allowlist or blocklist, and click the **Investigate** button.

The **Investigation** screen appears with the query populated


to show the selected process.

3. Click the process in the query results list to bring up the


**Element details** pane.


## Access an item's Element details pane

## from the Investigation screen

1. Build a query to search for the item you want to add to or


remove from the allowlist or blocklist.

2. From the query results, select the item to bring up the


**Element details** pane.

## Set the reputation


On the top right of the **Element details** pane, click **Set**


**reputation**, and select whether to add the item to the allowlist or

blocklist, or remove the reputation of the item.


Important


The blocklist is for detection purposes only. Adding an item to

the blocklist will not prevent that item from executing. See


[Prevent File Execution with Application Control (/s/knowledge-](https://nest.cybereason.com/s/knowledge-base?article=24-1-prevent-file-execution-with-application-control&language=en_US#prevent-file-execution-with-application-control)
[base?article=24-1-prevent-file-execution-with-application-](https://nest.cybereason.com/s/knowledge-base?article=24-1-prevent-file-execution-with-application-control&language=en_US#prevent-file-execution-with-application-control)


[control&language=en_US#prevent-file-execution-with-](https://nest.cybereason.com/s/knowledge-base?article=24-1-prevent-file-execution-with-application-control&language=en_US#prevent-file-execution-with-application-control)

[application-control) for details on preventing execution.](https://nest.cybereason.com/s/knowledge-base?article=24-1-prevent-file-execution-with-application-control&language=en_US#prevent-file-execution-with-application-control)

## Search reputation information


All analysts, including local analysts, can search for IOCs that

currently exist in the system and verify the reputation.


**To search for an item's reputation, do one of the following**

**from the Reputations screen:**


To search within your organization's private reputations list,
enter the MD5, SHA-1, or SHA-256 file hash, domain, or IP


address in the **Custom Reputation List** tab **Find reputation**
field.



