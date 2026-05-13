You can use any of the following network profiles for Personal


firewall control:






|Name|Description|
|---|---|
|**Domains**|Networks associated with a specifc Active<br>Directory domain.|
|**Private**<br>**Networks**|Networks that are not directly accessible by<br>the public, such as isolated home or offce<br>networks.|
|**Public**<br>**Networks**|Shared networks that do not include protection<br>between the endpoint and other endpoints.|



When you select a network profile, the Cybereason platform


triggers default firewall rules for that network profile. Firewall rules
associated with the Public Networks profile are the most


restrictive.


You can also use CSV files to add a set of custom rules for


[inbound and outbound connections. For more details, see Custom](https://nest.cybereason.com/s/knowledge-base?article=24-1-custom-firewall-rules&language=en_US#custom-firewall-rules)

[Firewall Rules (/s/knowledge-base?article=24-1-custom-firewall-](https://nest.cybereason.com/s/knowledge-base?article=24-1-custom-firewall-rules&language=en_US#custom-firewall-rules)


[rules&language=en_US#custom-firewall-rules).](https://nest.cybereason.com/s/knowledge-base?article=24-1-custom-firewall-rules&language=en_US#custom-firewall-rules)

## How the Personal firewall control status

## affects network profile settings


When you switch the Personal firewall feature on or off, the


network profile checkboxes are automatically selected or cleared,
respectively. In addition, the status of the Personal firewall feature


determines whether the Cybereason platform maintains custom
firewall rules, and how the Cybereason platform manages the


network profile settings in the operating system firewall. The table

below describes relevant scenarios and results.


Important


When you switch **Personal firewall control** to **Off**, the


Cybereason platform stops managing the operating system
firewall and removes any existing custom firewall rules. This


change does not affect the network profile settings that
previously existed on the operating system firewall. For more


information, see the **Disable Personal firewall control**

scenario in the table below.


|Scenario|Steps|Result|
|---|---|---|
|Switch on<br>Personal<br>frewall<br>control|1. Set the<br>**Personal**<br>**frewall**<br>**control**<br>toggle to<br>**On**.<br>2. Save the<br>policy.|When you switch on Personal<br>frewall control, the**Domains**,<br>**Private networks**, and**Public**<br>**networks** checkboxes are<br>automatically selected. To use<br>specifc network profles, clear<br>the checkboxes for the networks<br>that you do not want to activate.<br>The Cybereason platform saves<br>previously created custom<br>frewall rules (/s/knowledge-<br>base?article=24-1-custom-<br>frewall-<br>rules&language=en_US#custom-<br>frewall-rules). To update the<br>custom frewall rules, upload a<br>new CSV fle or update the rule.|
||||


|Scenario|Steps|Result|
|---|---|---|
|Disable<br>Personal<br>frewall<br>control|1. Set the<br>**Personal**<br>**frewall**<br>**control**<br>toggle to<br>**Off**.<br>2. Save the<br>policy.|All three checkboxes are<br>cleared.<br>The Personal frewall control<br>feature is disabled.|
|Disable the<br>operating<br>system<br>frewall via<br>the<br>Cybereason<br>platform|1. Set the<br>**Personal**<br>**frewall**<br>**control**<br>toggle to<br>**On**.<br>2. Clear the<br>**Domains**,<br>**Private**<br>**networks**,<br>and**Public**<br>**networks**<br>checkboxes.<br>3. Save the<br>policy.|The Personal frewall control<br>feature is enabled.<br>The Cybereason platform<br>applies custom frewall rules.|
|For more details on the Personal frewall control status that is<br>visible in the**System > Sensors** screen, see View Personal<br>frewall control modes in the Sensors screen.|For more details on the Personal frewall control status that is<br>visible in the**System > Sensors** screen, see View Personal<br>frewall control modes in the Sensors screen.|For more details on the Personal frewall control status that is<br>visible in the**System > Sensors** screen, see View Personal<br>frewall control modes in the Sensors screen.|


## View Personal firewall control modes in

## the Sensors screen

You can view endpoints' Personal firewall control modes for single


endpoints or for groups of endpoints in the **System > Sensors**

screen.


To display the Personal firewall control modes, above the sensors

list, click **Columns** and select the **Firewall control** column.


The Personal firewall control modes are displayed in the sensors

table:


You can see any of the following modes for Personal firewall

control:






|Mode|Description|
|---|---|
|**On**|Personal frewall control is enabled for all<br>network types. The**Personal Firewall**<br>**control** toggle in the**System > Policies**<br>**Management > Endpoint controls** screen<br>is turned on and the**Domains**, **Private**<br>**networks**, and**Public networks**<br>checkboxes are all selected.|


|Mode|Description|
|---|---|
|**Disabled**|The**Disabled** status indicates one of the<br>following options:<br>The**Personal Firewall control** toggle in<br>the**System > Policies Management >**<br>**Endpoint controls** screen is turned off.<br>Personal frewall control is enabled but<br>is not performing any actions. The<br>**Personal frewall control** toggle in the<br>**System > Policies Management >**<br>**Endpoint controls** screen is turned on<br>and no checkboxes are selected.|
|**Advanced**|Personal frewall control is enabled for some<br>network types. The**Personal Firewall**<br>**control** toggle in the**System > Policies**<br>**Management > Endpoint controls** screen<br>is turned on.|
|**Misconfgured**<br>**rules**|This mode indicates either that the custom<br>frewall rules CSV fle includes a rule that<br>Windows API defned as incorrect, or that a<br>user manually removed a custom frewall<br>rule using the operating system frewall. For<br>more details on rule validation, see Custom<br>frewall rules validation (/s/knowledge-base?<br>article=24-1-custom-frewall-<br>rules&language=en_US#custom-frewall-<br>rules-validation).|





