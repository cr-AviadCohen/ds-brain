**outbound_connections_template_GA.csv** . To download


[Cybereason GA templates, see Custom Firewall Rules](https://nest.cybereason.com/s/article/2027636)

[CSV Template (/s/article/2027636).](https://nest.cybereason.com/s/article/2027636)


3. In a CSV file editor, open the CSV file template, fill in the fields,

and save the template with the .csv suffix (for example,


**inboundconnections.csv** ).


For more information about the CSV file fields, see Custom


firewall rules - fields description.


Note


If you add Japanese rules, the header row must be in
English, and the file must use the UTF-8 encoding before


you import the file. If any Japanese characters do not

display properly, Cybereason recommends that you edit


the file using a text editor.


4. In the **Add custom firewall rules - inbound connections**


area or the **Add custom firewall rules - outbound**

**connections**, click **Import** .


5. Navigate to the file that you created, and click **Open** .


The Cybereason platform checks if the number of columns in


the header of the CSV file matches the number of columns in

one or more of the rows. If there is a mismatch in the number


of columns, the Cybereason platform does not import the CSV
and uses the previously imported CSV file. The **Error**


**uploading CSV file** dialog box is visible, and lists the rows

that include errors:


If a mismatch exists, fix the rules on the specified rows and


upload the file again. For a list of restrictions and solutions for
potential errors, see Address problems with custom firewall


rules.


When you upload a new custom firewall rules CSV file, the


Cybereason platform deletes any rules you added previously

with the **Add New** button. If you still need those rules, ensure


you back up existing rules.


After the upload completes successfully, you can then view the


rules in a table.


You can look at the Windows Firewall on a relevant endpoint to


verify whether a rule was successfully applied. For more details,

[see Block FTP access ().](https://nest.cybereason.com/s/knowledge-base?language=en_US&article=24-1-custom-firewall-rules&version=24.1)


Note


If a user manually removes a custom firewall rule using


Windows Firewall, the Cybereason platform sets the **Firewall**

**control** mode in the **System > Sensors** screen to


**Misconfigured rules** . For more details, see Custom firewall

rules validation.


On Linux machines, the Cybereason platform applies Linux
custom firewall rules in priority order from the top of the rules list to


the bottom of the list (both in the CSV file and for rules added

directly in the sensor policy. If the top rule's condition statement


matches a network traffic connection, the Cybereason platform

activates the top rule, and overwrites any subsequent rules that


contradict the top rule. When writing custom firewall rules for Linux

endpoints, make sure that the highest priority rule is on


top.Likewise, in a scenario where a Linux endpoint machine is

isolated, the Cybereason platform prioritizes the isolation higher


than the custom firewall rules applied to that endpoint.


However, on Windows machines, the machines apply the logic of


the custom firewall along with Microsoft's proprietary logic for
firewall rules. For details on the Microsoft priority order for firewall


[rules, see Windows Firewall Rules (https://learn.microsoft.com/en-](https://learn.microsoft.com/en-us/windows/security/operating-system-security/network-security/windows-firewall/rules)

[us/windows/security/operating-system-security/network-](https://learn.microsoft.com/en-us/windows/security/operating-system-security/network-security/windows-firewall/rules)


[security/windows-firewall/rules).](https://learn.microsoft.com/en-us/windows/security/operating-system-security/network-security/windows-firewall/rules)

## Add custom firewall rules directly in the

## sensor policy


Important


If you upload a new custom firewall rules CSV file, the

Cybereason platform deletes any rules you added previously


by using the **Add New** button.


If you do not want to use the CSV file to add rules, you can also


add these rules using the sensor policy.


**To add a new custom firewall rule in a sensor policy, follow**


**these steps:**


1. In your sensor policy, in the **Endpoint controls** screen, under


the **Personal firewall control** option, locate the **Add custom**
**firewall rules - inbound connections** area or the **Add**


**custom firewall rules - outbound connections** area

(depending on whether you want to add inbound or outbound


rules).

2. Click **Add New** .


3. In the **Add rule** window, fill in the fields for this rule and click


**Save** .


If you do not fill in a required field or if you fill in a field incorrectly,
the field text box is marked in red and an error message provides


information about the problem. For example, a **Required field**
error is visible if a required field is empty. The **Save** button is


disabled until you fill in all of the fields correctly.


For information on how to fill in the fields, see Custom firewall rules


- fields description.


After you successfully save a rule, the rule is visible at the top of


the table of custom firewall rules.

## ## Custom firewall rules fields description


When you add a custom firewall rule, you must use the following
fields:


|Field Name|Description|Required/Optional|Format/Va|
|---|---|---|---|
|Name|The identifer for<br>the rule|Required|A string wit|


|Field Name|Description|Required/Optional|Format/Va|
|---|---|---|---|
|Group|**For system use**<br>**and non-**<br>**confgurable**.<br>Specifes the<br>group name,<br>used to tag rules<br>in the same<br>category.|N/A|You cannot<br>**Cybereaso**<br>When you e<br>this feld is<br>be change<br>When you u<br>you add an<br>Cybereaso<br>value to the|
|Profle|Specifes the<br>network profle<br>to which this<br>custom frewall<br>applies.|Optional|Enter one o<br>the CSV fle<br>sensor poli<br>**All**: Sp<br>on pub<br>types.<br>**Public**<br>**Private**<br>**Domai**<br>**Private**<br>**Private**<br>**Public**<br>**Important:**<br>network pro<br>list with quo<br>**"Private,D**<br>This feld is<br>If you provi<br>endpoint, t<br>apply this f|
|Enabled|Specifes<br>whether the rule<br>is active.|Optional|Enter or se<br>**Yes**<br>**No**<br>Disabled ru<br>under**Inbo**<br>However, e<br>**Monitoring**<br>Only active<br>network pro<br>**Firewall**.|
|||||


|Field Name|Description|Required/Optional|Format/Va|
|---|---|---|---|
|Action|Specifes the<br>action for the<br>rule.|Required|Type or sel<br>**Allow**: <br>setting<br>**Block**:<br>setting<br>**Secure**<br>for def<br>current<br>**conne**<br>operati<br>The**Se**<br>Linux e<br>value f<br>platform<br>If you set th<br>**users** or**A**<br>**computers**<br>you must e|
|Override|**For system use**<br>**and non-**<br>**confgurable**.<br>Specifes<br>whether to<br>override default<br>system<br>specifcations.|N/A|The default<br>When you e<br>this feld is<br>cannot cha<br>rules using<br>platform wi<br>feld autom|
|Program|Provides the full<br>path of the fle or<br>process to<br>which the rule<br>applies.|Optional|Example fo<br>**C:\window**<br>**Important**:<br>a value for<br>this feld on<br>platform do<br>rule.|
|||||


|Field Name|Description|Required/Optional|Format/Va|
|---|---|---|---|
|LocalAddress<br>(in the CSV fle)<br>Local address<br>(in a sensor<br>policy)|The IP address<br>of the local<br>machine.|Optional|Enter one o<br>An IP a<br>An IP a<br>examp<br>An IP r<br>examp<br>A list o<br>ranges<br>**192.16**<br>**Important:**<br>addresses<br>quotation m<br>**"192.168.1**|
|RemoteAddress<br>(in the CSV fle)<br>Remote<br>Address (in a<br>sensor policy)|The IP address<br>of the remote<br>machine.|Optional|Type one o<br>An IP a<br>An IP a<br>examp<br>An IP r<br>examp<br>A list o<br>ranges<br>**192.16**<br>**Important:**<br>the CSV fle<br>marks, for e<br>**"192.168.1**|
|Protocol|The network<br>protocol|Required|Example va<br>**TCP**<br>**UDP**<br>**ICMPv**<br>When you a<br>policy, you<br>a protocol f|
|||||


|Field Name|Description|Required/Optional|Format/Va|
|---|---|---|---|
|LocalPort (in<br>the CSV fle)<br>Local port (in a<br>sensor policy)|Specifes the<br>port on the local<br>machine (the<br>endpoint<br>running the<br>sensor).<br>If the<br>**Protocol**<br>feld is<br>defned as<br>either**TCP**,<br>**UDP**, **6** or<br>**17**, fll in the<br>local port.<br>If the<br>**Protocol**<br>feld is set to<br>another<br>value, do<br>not modify<br>the<br>**LocalPort**<br>feld in the<br>CSV fle (the<br>**Local port**<br>feld is<br>disabled in<br>the sensor<br>policy).|Optional|Type a sing<br>values:<br>**21**<br>**45-55**<br>**80,443**<br>**Important:**<br>fle, surroun<br>example,**"**|
|||||


|Field Name|Description|Required/Optional|Format/Va|
|---|---|---|---|
|RemotePort (in<br>the CSV fle)<br>Remote port (in<br>a sensor policy)|Specifes the<br>port on the<br>remote machine.<br>If the<br>**Protocol**<br>feld is<br>defned as<br>either**TCP**,<br>**UDP**, **6** or<br>**17**, fll in the<br>remote port.<br>If the<br>**Protocol**<br>feld is set to<br>another<br>value, do<br>not modify<br>the<br>**RemotePort**<br>feld in the<br>CSV fle (the<br>**Remote**<br>**port** feld is<br>disabled in<br>the the<br>sensor<br>policy).|Optional|Type a sing<br>a list of por<br>surround th<br>values:<br>**21**<br>**45-55**<br>**80,443**<br>**Important:**<br>fle, surroun<br>example,**"**|
|The following felds are used only in advanced cases:<br>**AuthorizedUsers** (CSV) or**Authorized users** (UI): Available<br>only for inbound connections<br>**AuthorizedComputers** (CSV) or**Authorized computers** (UI)<br>**AuthorizedLocalPrincipals** (CSV) or**Authorized local**<br>**principals** (UI)<br>**LocalUserOwner** (CSV)**Local user owner** (UI)<br>**ApplicationPackage** (CSV)<br>Note<br>These felds for advanced cases are not supported on Linux<br>endpoints. If you provide a value for any of these felds for a<br>Linux endpoint, the Cybereason platform does not apply the<br>feld to the rule.|The following felds are used only in advanced cases:<br>**AuthorizedUsers** (CSV) or**Authorized users** (UI): Available<br>only for inbound connections<br>**AuthorizedComputers** (CSV) or**Authorized computers** (UI)<br>**AuthorizedLocalPrincipals** (CSV) or**Authorized local**<br>**principals** (UI)<br>**LocalUserOwner** (CSV)**Local user owner** (UI)<br>**ApplicationPackage** (CSV)<br>Note<br>These felds for advanced cases are not supported on Linux<br>endpoints. If you provide a value for any of these felds for a<br>Linux endpoint, the Cybereason platform does not apply the<br>feld to the rule.|The following felds are used only in advanced cases:<br>**AuthorizedUsers** (CSV) or**Authorized users** (UI): Available<br>only for inbound connections<br>**AuthorizedComputers** (CSV) or**Authorized computers** (UI)<br>**AuthorizedLocalPrincipals** (CSV) or**Authorized local**<br>**principals** (UI)<br>**LocalUserOwner** (CSV)**Local user owner** (UI)<br>**ApplicationPackage** (CSV)<br>Note<br>These felds for advanced cases are not supported on Linux<br>endpoints. If you provide a value for any of these felds for a<br>Linux endpoint, the Cybereason platform does not apply the<br>feld to the rule.|The following felds are used only in advanced cases:<br>**AuthorizedUsers** (CSV) or**Authorized users** (UI): Available<br>only for inbound connections<br>**AuthorizedComputers** (CSV) or**Authorized computers** (UI)<br>**AuthorizedLocalPrincipals** (CSV) or**Authorized local**<br>**principals** (UI)<br>**LocalUserOwner** (CSV)**Local user owner** (UI)<br>**ApplicationPackage** (CSV)<br>Note<br>These felds for advanced cases are not supported on Linux<br>endpoints. If you provide a value for any of these felds for a<br>Linux endpoint, the Cybereason platform does not apply the<br>feld to the rule.|


If you use custom firewall rules CSV file, if you modify the


**AuthorizedUsers** field or the **AuthorizedComputers** field (you
set one of these fields to a value other than **Any** ), set the **Action**


field to **Secure** . For example, if you created a firewall rule named
TestRule and you modified the **AuthorizedUsers** field, you must


also set the **Action** field to **Secure** .

## Custom firewall rules validation


When you add a custom firewall rule, the Cybereason platform


performs checks to ensure that custom firewall rules are applied
and configured correctly and takes action to address issues in the


following scenarios:








|Scenario|System Behavior|Next Steps|
|---|---|---|
|You import a<br>custom frewall<br>rules CSV fle<br>where the number<br>of columns for a<br>custom frewall<br>rule does not<br>match the number<br>of columns in the<br>header row.|The**Error uploading**<br>**CSV fle** dialog box is<br>visible, indicating the<br>rows that include<br>errors. In addition,<br>the Cybereason<br>platform does not<br>upload the CSV fle.|Fix the errors on<br>the specifed<br>rows and<br>upload the fle<br>again. For a list<br>of restrictions<br>and solutions<br>for potential<br>errors, see<br>Address<br>problems with<br>custom frewall<br>rules.|


|Scenario|System Behavior|Next Steps|
|---|---|---|
|An administrator<br>defnes a custom<br>frewall rule<br>incorrectly, saves<br>the rule or the CSV<br>fle, and publishes<br>the policy. The<br>Windows API<br>applies default<br>values or<br>otherwise modifes<br>the rule.<br>For example,<br>when Windows<br>detects a frewall<br>rule that defnes a<br>port number<br>without a protocol,<br>Windows API<br>updates the**Port**<br>value to**Any**, and<br>uses the default<br>**Protocol** value,<br>which is also**Any**.<br>These settings<br>might disconnect<br>the endpoint<br>machine from the<br>Cybereason<br>platform and might<br>even block the<br>internet<br>connection.|The Cybereason<br>platform does not<br>apply the<br>misconfgured rule.,<br>but the custom<br>frewall rule is still<br>visible in the table of<br>rules in the**Personal**<br>**frewall control**<br>section.<br>In addition, the<br>Cybereason platform<br>shows the**Firewall**<br>**Control** mode for<br>sensors assigned the<br>policy with the rule<br>error as<br>**Misconfgured rules**<br>in the**System >**<br>**Sensors** screen.|Find the name<br>of the custom<br>frewall rule that<br>failed validation<br>in the<br>endpoint's log<br>fles, retrieved<br>via the**Fetch**<br>**sensor log**<br>action in the<br>**System >**<br>**Sensors**<br>screen.<br>Then, fx the<br>rule error. For<br>details on how<br>to resolve the<br>errors, see<br>Address<br>problems with<br>custom frewall<br>rules.|


|Scenario|System Behavior|Next Steps|
|---|---|---|
|An administrator<br>adds custom<br>frewall rules, and<br>then saves the rule<br>or the CSV fle and<br>publishes the<br>policy. An<br>endpoint user then<br>manually removes<br>a custom frewall<br>rule that belongs<br>to the Cybereason<br>group by using<br>Windows Firewall.|The Cybereason<br>platform does not<br>reapply manually<br>deleted rules as part<br>of the default<br>Personal frewall<br>functionality.<br>However, the<br>Cybereason platform<br>may add the deleted<br>custom frewall rule<br>again as part of a<br>policy update or<br>other automatic<br>update. However, the<br>custom frewall rule is<br>still visible in the table<br>of rules under the<br>**Personal frewall**<br>**control** section.<br>In addition, the<br>Cybereason platform<br>displays the status<br>**Firewall Control**<br>mode for sensors<br>assigned to this<br>policy as<br>**Misconfgured rules**<br>in the**System >**<br>**Sensors** screen.|To add back the<br>custom frewall<br>rule, add the<br>rule in the<br>sensor policy<br>and save the<br>policy again.<br>If the<br>Cybereason<br>platform<br>reapplied the<br>custom frewall<br>rule, and you<br>want to remove<br>this custom<br>frewall rule, you<br>can delete the<br>rule in a sensor<br>policy, or import<br>a new custom<br>frewall rules<br>CSV fle that<br>does not<br>include the<br>undesired rule.|


## Address problems with custom firewall

If you have issues with custom firewall rules, such as the status of


**Misconfigured rules** for a sensor in the **System > Sensors**

screen, you can verify any of the following:


|Issue|What to Check|Incorrect|Col4|
|---|---|---|---|
|Specifc<br>ports with<br>incorrect<br>protocol|If you add a rule that<br>specifes remote or<br>local ports, ensure you<br>defne the protocol<br>correctly.|You added a frewall rule<br>with the following settings:<br>**LocalPort/Local Port** or<br>**RemotePort/Remote**<br>**Port** set to**21**<br>**Protocol** set to**Any**<br>When Windows Firewall<br>detects this rule with the<br>**Protocol** feld value set to<br>**Any**, the Windows Firewall<br>disregards the specifc port<br>values and sets both values<br>to**Any**. These settings might<br>disconnect the endpoint<br>machine from the<br>Cybereason platform.||
|Mismatch<br>on<br>columns in<br>the CSV<br>fle|When you add a<br>custom frewall rules<br>with the CSV fle, make<br>sure that the number of<br>columns for each rule<br>matches the number of<br>columns in the header<br>row. If the Cybereason<br>platform cannot match<br>the number of columns<br>in the header row with<br>the number of columns<br>for a specifc rule, the<br>Cybereason platform<br>does not upload the<br>CSV fle.|The table includes 16<br>columns in the header row,<br>and the frst rule in the table<br>includes 15 columns.||
|Spaces in<br>names in<br>the header<br>row|When you add custom<br>frewall rules with a<br>CSV fle, ensure that<br>the names in the<br>header row do not<br>contain spaces.|You added values in the<br>header row such as**Local**<br>**Port**.||
|Incomplete<br>IP<br>addresses<br>in IP<br>ranages|Make sure that the IP<br>ranges used for rules<br>contains two complete<br>IP addresses.|You added the IP range of<br>**192.168.1.1-50**||
|||||


|Issue|What to Check|Incorrect|
|---|---|---|
|Incorrect<br>**Action**<br>feld for<br>specifc<br>advanced<br>felds|When you add custom<br>frewall rules with the<br>CSV fle, if you modify<br>the**AuthorizedUsers**<br>or<br>**AuthorizedComputers**<br>of these felds for a<br>rule, set the**Action**<br>feld to**Secure**.|You create a frewall rule with<br>the following settings:<br>**AuthorizedUsers** set to<br>a value other than**Any**<br>**Action** set to**Block**|
|Lists of<br>vales not<br>grouped<br>with<br>quotes|When using a custom<br>frewall rules CSV fle, if<br>you use a comma-<br>separated list, ensure<br>you surround the list<br>with quotation marks.|You entered the values<br>**192.168.1.501,192.168.1.100**<br>and**21,22**|







