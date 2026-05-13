|Mode<br>name|Mode name - CSV file|Description|
|---|---|---|
|**Full**<br>**access**|**USB_ACTION_ALLOW_ALL**|The Cybereason platform<br>to fully access USB stora<br>devices inserted into end<br>the policy applies. While<br>Cybereason platform mo<br>storage or MTP devices,<br>interfere with the device's<br>behavior on the machine|
|**Read**<br>**only**|**USB_ACTION_READ_ONLY**|The Cybereason platform<br>only access to the USB s<br>Note<br>If you set the Device co<br>**Read**<br>**only**/**USB_ACTION_RE**<br>on a sensor using a ver<br>than 21.1.103, the Cybe<br>platform automatically c<br>mode to**Full access**. T<br>**only** mode, the sensor<br>version 21.1 and later.|
|**Block**|**USB_ACTION_BLOCK_ALL**|The Cybereason platform<br>to the USB device on the<br>which the policy applies,<br>allow any interaction with<br>Note<br>When you set the mode<br>**Block**/**USB_ACTION_B**<br>the Cybereason platfor<br>the USB device. The de<br>remain visible momenta<br>**This PC** while the Cybe<br>platform dismounts the<br>use the USB device ag<br>and reinsert the device<br>endpoint.|
||||


Note


When you modify the Device control mode, and a USB

storage or MTP device is inserted into the endpoint


machine, the Cybereason platform may set a different
mode for a specific device. For more information, see


Modify the Device control mode.

## Manage individual devices


When you select the Device control mode, you specify the default


mode for access to all USB storage devices or all MTP devices on

the machines to which the policy applies.


If you want to specify a different mode and set additional fields for
a specific USB device, you can add that device to the table or


import a CSV file in the **Manage devices** area.


You can manage USB devices in one of the following ways:


Add USB devices directly in a sensor policy
Add devices with the Device control CSV file that includes a


list of devices to manage


Important


If you upload a Device control CSV file, the Cybereason

platform deletes any USB devices you previously added to the


table with the **Add New** button. To save the previous USB

device details, click **Export** .

## Add USB devices directly in a sensor


If you want to maintain all the details for individual devices, you

can add these individual devices in the sensor policy.


**To add devices in a sensor policy, follow these steps:**


1. In the Endpoint Controls screen, in the **Device control >**


**Manage devices** area, and click **Add New** .
2. Fill in the fields in the table. For more information, see Manage


USB devices - fields description.


[If you do not have the details on the device, see Find Device](https://nest.cybereason.com/s/knowledge-base?article=24-1-find-device-details&language=en_US#find-device-details)


[Details (/s/knowledge-base?article=24-1-find-device-](https://nest.cybereason.com/s/knowledge-base?article=24-1-find-device-details&language=en_US#find-device-details)
[details&language=en_US#find-device-details) to learn how to](https://nest.cybereason.com/s/knowledge-base?article=24-1-find-device-details&language=en_US#find-device-details)


find those details.


Note


If you add an MTP device to the table, and several


components are visible for the device under Windows

**Device manager**, you might need to add more than one


component to the table. For more information, contact

Technical Support.


3. Click the check mark () to save.


The **Modified by** and **Last modified** fields display the user


name and date for this USB device.

4. To add more USB devices, repeat steps 1-2 for each


additional USB device.


You can then view the USB device or devices in the table.


5. To disable or enable a USB device, hover over the USB


device row on the right side of the table, and click the

**Enabled** or **Disabled** toggle:


6. To delete USB devices, do one of the following:


To delete a single USB device, click the Delete icon ( ).


To delete the entire list of USB devices, click **Clear**

**devices** . This command clears the set of USB devices


you previously added or uploaded.

## Add devices with the Device control CSV


You can import USB device settings using a CSV file.


**To add devices with a CSV file, follow these steps:**


Note


You can import up to 200 entries in a single CSV file. You can

add more entries manually directly in the sensor policy.


1. In the **Endpoint Controls** screen, in the **Device control**

section, find the **Manage devices** area, .


2. If you previously added USB devices to the table under


**Manage devices**, click **Export** to save the details of these


USB devices before you import a CSV file (when you import a


new CSV file, the new file overrides any existing USB device


details).

3. Click **Download Template**, and in a CSV file editor, open the


CSV file template, fill in the fields, and save the template with
the .csv suffix (for example, **usbdevices.csv** ).


For more information about the CSV file fields, see Manage
[USB devices - fields description and Find Device Details](https://nest.cybereason.com/s/knowledge-base?article=24-1-find-device-details&language=en_US#find-device-details)


[(/s/knowledge-base?article=24-1-find-device-](https://nest.cybereason.com/s/knowledge-base?article=24-1-find-device-details&language=en_US#find-device-details)
[details&language=en_US#find-device-details).](https://nest.cybereason.com/s/knowledge-base?article=24-1-find-device-details&language=en_US#find-device-details)


4. In the **Device control** section, click **Import**, navigate to the

file that you created, and click **Open** .


If a dialog with an error is visible, fix the issues on the relevant
columns or rows, and upload the CSV file again. To review the


field descriptions and requirements, see Manage USB
devices - fields description.


After the import, you can view the USB devices in the table.


5. To disable or enable a USB device, hover over the USB


device row on the right side of the table, and click the


**Enabled** or **Disabled** toggle:


6. To delete USB devices, do one of the following:


To delete a single USB device, click the Delete icon ( ).


To delete the entire list of USB devices, click **Clear**


**devices** . This command clears the set of USB devices

you previously added or uploaded.

## - Manage USB devices fields description


The following table describes the fields in the **Manage devices**
area and in the Device control CSV file. **UI** refers to the fields or


values under the **Manage devices** area in the sensor policy and
**CSV** refers to the fields or values in the CSV file.


|Field name|Description|Required/Optional|Values|
|---|---|---|---|
|UI:**Class**<br>CSV:<br>**classType**|Defnes the<br>USB device<br>class or<br>type.|Required|**USB (Mass s**<br>value) or<br>**USB_CLASS**<br>(CSV): Indica<br>is a USB stor<br>more informa<br>whether a de<br>storage devic<br>machines (/s<br>article=24-1-<br>details&lang<br>whether-a-de<br>storage-devi<br>machines).<br>**Mobile/Medi**<br>**USB_CLASS**<br>Indicates tha<br>Media Transf<br>device, whic<br>media device<br>**All** (UI) or<br>**USB_CLASS**<br>Indicates tha<br>USB device t<br>storage devic|
|||||


|Field name|Description|Required/Optional|Values|
|---|---|---|---|
|Vendor|Defnes the<br>vendor<br>name.|Required|Type the vendor<br>following formats<br>The vendor n<br>not case-sen<br>type either**S**<br>The vendor I<br>**0781**.<br>Note<br>The format mus<br>both the vendo<br>felds/columns.<br>you type an ID<br>must also type<br>product.<br>To retrieve the ve<br>see Find the dev<br>product informati<br>machines (/s/kno<br>article=24-1-fnd-<br>details&language<br>device-vendor-an<br>information-on-w<br>Find the device v<br>information on m<br>(/s/knowledge-ba<br>fnd-device-<br>details&language<br>device-vendor-an<br>information-on-m<br>an online list of U<br>vendor and prod<br>USB vendors<br>(https://devicehu<br>vendors).|
|||||


|Field name|Description|Required/Optional|Values|
|---|---|---|---|
|Product|Specifes<br>the model<br>or specifc<br>product for<br>this vendor.|Required|Type the product<br>following formats<br>The product<br>name is not c<br>example, typ<br>**ULTRA_FIT**.<br>The product<br>type**5583**.<br>Note<br>The format mus<br>both the vendo<br>felds/columns.<br>you type an ID<br>must also type<br>product.<br>To retrieve the ve<br>see Find the dev<br>product informati<br>machines (/s/kno<br>article=24-1-fnd-<br>details&language<br>device-vendor-an<br>information-on-w<br>Find the device v<br>information on m<br>(/s/knowledge-ba<br>fnd-device-<br>details&language<br>device-vendor-an<br>information-on-m<br>an online list of U<br>vendor and prod<br>USB vendors<br>(https://devicehu<br>vendors).|
|||||


|Field name|Description|Required/Optional|Values|
|---|---|---|---|
|UI:**Serial**<br>**number**<br>CSV:<br>**serial**|Specifes<br>the serial<br>number of<br>the USB<br>device.|Optional;<br>recommended|Type the serial nu<br>type**12345**.<br>When you provid<br>a USB device, yo<br>security effective<br>control capability<br>potential risk. If y<br>serial number, an<br>the**Serial Numb**<br>click the check m<br>To fnd the serial<br>the device vendo<br>information on W<br>(/s/knowledge-ba<br>fnd-device-<br>details&language<br>device-vendor-an<br>information-on-w<br>Find the device v<br>information on m<br>(/s/knowledge-ba<br>fnd-device-<br>details&language<br>device-vendor-an<br>information-on-m|
|UI:**Mode**<br>CSV:<br>**action**|Select the<br>Device<br>control<br>mode for<br>this USB<br>device<br>specifcally.<br>This setting<br>allows you<br>to defne a<br>different<br>mode than<br>the mode<br>you set for<br>all USB<br>devices<br>under<br>**Device**<br>**control**.|Required|Select one of the<br>**Full access** <br>**USB_ACTIO**<br>(CSV)<br>**Read only** (U<br>**USB_ACTIO**<br>(CSV)<br>**Block** (UI) or<br>**USB_ACTIO**<br>(CSV)|
|||||


|Field name|Description|Required/Optional|Values|
|---|---|---|---|
|Modifed by|Displays the<br>user name<br>of the last<br>user that<br>modifed<br>the<br>exclusion.<br>The<br>**Modifed**<br>**by** feld<br>displays the<br>user name<br>after you<br>click to<br>save. You<br>cannot<br>modify this<br>value.|N/A|N/A|
|Last modifed|Displays the<br>date of the<br>last<br>modifcation<br>for this<br>exclusion.<br>The**Last**<br>**modifed**<br>feld<br>displays the<br>date after<br>you click to<br>save. You<br>cannot<br>modify this<br>value.|N/A|N/A|
|Modify the Device control mode<br>When you modify the Device control mode, and a USB storage or<br>MTP device is inserted into the endpoint machine, the Cybereason<br>platform may set a different mode for a specifc device. The<br>following tables describe the relevant scenarios.|Modify the Device control mode<br>When you modify the Device control mode, and a USB storage or<br>MTP device is inserted into the endpoint machine, the Cybereason<br>platform may set a different mode for a specifc device. The<br>following tables describe the relevant scenarios.|Modify the Device control mode<br>When you modify the Device control mode, and a USB storage or<br>MTP device is inserted into the endpoint machine, the Cybereason<br>platform may set a different mode for a specifc device. The<br>following tables describe the relevant scenarios.|Modify the Device control mode<br>When you modify the Device control mode, and a USB storage or<br>MTP device is inserted into the endpoint machine, the Cybereason<br>platform may set a different mode for a specifc device. The<br>following tables describe the relevant scenarios.|


|From<br>mode|To<br>mode|Scenario|Recommended<br>action|
|---|---|---|---|
|**Full**<br>**access**|**Read**<br>**only**|In some cases,<br>due to permission<br>issues or other<br>issues, the<br>Cybereason<br>platform cannot<br>successfully set<br>the mode to**Read**<br>**only** for a specifc<br>USB storage<br>device.<br>In these cases, the<br>Cybereason<br>platform<br>automatically<br>blocks the USB<br>storage device to<br>protect the device.|Remove and<br>reinsert the USB<br>storage device into<br>the endpoint.|
|**Full**<br>**access**|**Read**<br>**only**|If you set the<br>Device control<br>mode to**Read only**<br>on a sensor using a<br>version earlier than<br>21.1, the<br>Cybereason<br>platform<br>automatically<br>changes the mode<br>to**Full access**.|To use**Read only**<br>mode, the sensor<br>must use version<br>21.1 and later.|
|**Block**|**Full**<br>**access**|After you modify<br>the mode to**Full**<br>**access**, the USB<br>storage or MTP<br>device remains<br>blocked until you<br>reinsert the device.<br>This occurs<br>because the<br>Cybereason<br>platform dismounts<br>blocked USB<br>storage or MTP<br>devices.|After the<br>Cybereason<br>platform completes<br>the policy update,<br>remove and<br>reinsert the USB<br>storage or MTP<br>device.|


|From<br>mode|To<br>mode|Scenario|Recommended<br>action|
|---|---|---|---|
|**Block**|**Read**<br>**only**|After you modify<br>the mode to**Read**<br>**only**, the USB<br>storage device<br>remains blocked<br>until you reinsert<br>the device. This<br>occurs because<br>the Cybereason<br>platform dismounts<br>blocked USB<br>storage or MTP<br>devices.<br>In addition, in some<br>cases, due to<br>permission issues<br>or other issues, the<br>Cybereason<br>platform cannot<br>successfully set<br>the mode to**Read**<br>**only** for a specifc<br>device. In these<br>cases, the<br>Cybereason<br>platform<br>automatically<br>blocks the USB<br>storage device to<br>protect the device.|1. After the<br>Cybereason<br>platform<br>completes the<br>policy update,<br>remove and<br>reinsert the<br>USB storage<br>device.<br>2. If the<br>Cybereason<br>platform did<br>not<br>successfully<br>modify the<br>mode to**Read**<br>**only**, remove<br>and reinsert<br>the USB<br>storage device<br>again.|
|**Read**<br>**only**|**Full**<br>**access**|The Cybereason<br>platform may not<br>automatically apply<br>the change.|If the Cybereason<br>platform does not<br>update the mode,<br>remove and<br>reinsert the USB<br>storage device into<br>the endpoint.|







