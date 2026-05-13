If **USB Mass Storage Device** is not visible in the


**Location** field, the device is not a mass storage device.

For example:


You can also look for the **USBSTOR** value in the Device instance


path to check if the device is a USB storage device. For more

information on how to view the Device instance path, see Use


Device Manager.

## Find the device vendor and product

## information on Windows machines


To find a device's vendor and product information, do one of the


following:


Use Device Manager


Use Remote Shell

## Use Device Manager


1. In Windows, open **Device Manager**, and do one of the


following:


For USB storage devices, click **Disk Drives** to view the


USB storage devices connected to your endpoint

machine.


For MTP devices, find the MTP devices connected to your


endpoint machine, and perform the following steps for

each device.


If a physical connection of one MTP device creates

several components in **Device Manager**, you might need


to retrieve device details for all components. For example,

the following MTP device is located under **Portable**


**Devices** . Additional components might be visible in

additional sections of **Device Manager** .


For other USB devices (devices with the **All** device type),
find the USB devices connected to your endpoint


machine, and perform the following steps for each device.


Important


If you want to manage a USB device with the **All**

device type, in **Device Manager**, right-click the device


and locate the **Disable** option. If the **Disable** option is

visible, continue to the next steps. If the **Disable**


option is not visible and even if the **Uninstall** option is

visible, you cannot manage this device.


2. Right-click the USB device, and click **Properties** .

3. In the **Properties** window, click the **Details** tab.


4. From the **Property** drop-down menu, select **Device instance**


**path** .


5. Retrieve the USB device details, according to the following


table.


|Device<br>details|Values|Example|
|---|---|---|
|Serial<br>number<br>Vendor<br>name<br>Product<br>name|The**Value** area<br>displays the<br>device<br>instance path<br>value.<br>The serial<br>number<br>begins<br>after the<br>last<br>backslash<br>and ends<br>before the<br>last<br>ampersand<br>character.<br>This is<br>relevant to<br>a unique<br>serial<br>number, as<br>shown in<br>this<br>example.<br>For<br>information<br>about non-<br>unique<br>serial<br>numbers,<br>see Unique<br>and non-<br>unique<br>serial<br>numbers.<br>The vendor<br>name<br>begins<br>after**VEN_**<br>and ends<br>before the<br>ampersand<br>character.<br>The<br>product<br>begins<br>after<br>**PROD_**<br>and ends|For a device with the path<br>**USBSTOR\DISK&VEN_SANDISK**<br>**\082E5F232F1BF361C7F64916&0**<br>**SANDISK** is the vendor name<br>**ULTRA_FIT** is the product nam<br>**082E5F232F1BF361C7F6491**<br>Note<br>The serial number in this exampl<br>on serial numbers, see Unique a|


|Device<br>details|Values|Example|
|---|---|---|
||before the<br>ampersand<br>character.||
|Vendor<br>ID<br>Product<br>ID|The**Value** area<br>displays the<br>parent value.<br>The vendor<br>ID begins<br>after**VID_**<br>and ends<br>before the<br>ampersand<br>character.<br>The<br>product ID<br>begins<br>after**PID_**<br>and ends<br>before the<br>backslash.<br>Note<br>The value<br>displayed<br>under<br>**Parent**<br>does not<br>include the<br>serial<br>number.<br>You can<br>only<br>retrieve the<br>serial<br>number<br>from the<br>**Device**<br>**Instance**<br>**Path** value.|**USB\VID_0781&PID_5583\81a886**<br>In this example:<br>**0781** is the vendor ID<br>**5583** is the product ID|
||||


device:


|Device<br>details|Values|Example|
|---|---|---|
|Mass<br>storage<br>device<br>(**USBSTOR**)|If the<br>**USBSTOR**<br>value is<br>visible in<br>the**Value**<br>area, the<br>device is a<br>USB<br>storage<br>device.<br>If the<br>**USBSTOR**<br>value is not<br>visible in<br>the**Value**<br>area, the<br>device is<br>not a USB<br>storage<br>device.|This device instance path begins w<br>storage device:<br>**USBSTOR\DISK&VEN_STOREJE**<br>**WXQ2A907SE5F&0**<br>This device instance path begins w<br>device:<br>**SCSI\DISK&VEN_NVME&PROD_**|
|e Remote Shell<br>Set up and open the Remote Shell command line utility<br>(/s/knowledge-base?article=24-1-respond-to-threats-on-a-<br>machine-with-remote-shell&language=en_US#use-the-<br>remote-shell-utility).<br>Contact Technical Support to add the**Get-PnpDevice**<br>PowerShell command to your allowlist.<br>Do one of the following:<br>For USB storage devices, run the**Get-PnpDevice**<br>command with the following syntax:<br>`Get-PnpDevice -PresentOnly -Class`<br>`"DiskDrive" | Format-Table -Wrap -`<br>`AutoSize -Property InstanceID`<br>The**InstanceID** column displays a list of connected USB<br>storage devices including the vendor name, product<br>name, and serial number.<br>For MTP devices and other USB devices, run the**Get-**<br>**PnpDevice** command.<br>following is an example output for the Ultra Fit USB storage<br>ce:|e Remote Shell<br>Set up and open the Remote Shell command line utility<br>(/s/knowledge-base?article=24-1-respond-to-threats-on-a-<br>machine-with-remote-shell&language=en_US#use-the-<br>remote-shell-utility).<br>Contact Technical Support to add the**Get-PnpDevice**<br>PowerShell command to your allowlist.<br>Do one of the following:<br>For USB storage devices, run the**Get-PnpDevice**<br>command with the following syntax:<br>`Get-PnpDevice -PresentOnly -Class`<br>`"DiskDrive" | Format-Table -Wrap -`<br>`AutoSize -Property InstanceID`<br>The**InstanceID** column displays a list of connected USB<br>storage devices including the vendor name, product<br>name, and serial number.<br>For MTP devices and other USB devices, run the**Get-**<br>**PnpDevice** command.<br>following is an example output for the Ultra Fit USB storage<br>ce:|e Remote Shell<br>Set up and open the Remote Shell command line utility<br>(/s/knowledge-base?article=24-1-respond-to-threats-on-a-<br>machine-with-remote-shell&language=en_US#use-the-<br>remote-shell-utility).<br>Contact Technical Support to add the**Get-PnpDevice**<br>PowerShell command to your allowlist.<br>Do one of the following:<br>For USB storage devices, run the**Get-PnpDevice**<br>command with the following syntax:<br>`Get-PnpDevice -PresentOnly -Class`<br>`"DiskDrive" | Format-Table -Wrap -`<br>`AutoSize -Property InstanceID`<br>The**InstanceID** column displays a list of connected USB<br>storage devices including the vendor name, product<br>name, and serial number.<br>For MTP devices and other USB devices, run the**Get-**<br>**PnpDevice** command.<br>following is an example output for the Ultra Fit USB storage<br>ce:|


```
 USBSTOR\DISK&VEN_SANDISK&PROD_ULTRA_FIT&

 REV_1.00\0101DD69E466E9D273FE5C334FD6F81

 03812AD30D1A975E217B9E01998B6717

```

Note


The serial number in this example is a unique serial number.


For more details on serial numbers, see Unique and non
unique serial numbers.


The following is an example output for a USB device:

```
 USB\VID_17EF&PID_3072\8&140CDB29&0&3

```

For more details on how to extract the USB device details from this

path, see the table on device details above.

## Find the device vendor and product

## information on macOS machines


1. From the Apple menu in the corner of your screen, select


**About This Mac** .


2. Click **System Report** (In older versions of macOS, click **More**


**Info** ). The System Information app is displayed.


3. In the System Information app select **Hardware > USB** .

4. Select the device. The **Product ID**, **Vendor ID** and **Serial**


**number** are displayed.


Note


The **Vendor ID** and **Product ID** can be added to the **Manage**


**devices** table or CSV file as the respective value for Vendor

and Product.

## Unique and non-unique serial numbers


A USB device's serial number may be unique or non-unique.


A unique serial number remains the same regardless of any


changes or user actions.

A non-unique serial number may change in some scenarios,


such as when a user restarts the system or removes and

inserts the USB device into a new USB port. For support


information, see Unique and non-unique serial numbers.


To find out whether a USB device's serial number is unique, see


Check whether a USB device's serial number is unique.


If the serial number includes the ampersand ( **&** ) character:


For USB devices with a unique serial number, the serial

number begins after the last backslash and ends before the


last ampersand character. For example, for a USB device with

the path


**USBSTOR\DISK&VEN_SANDISK&PROD_ULTRA_FIT&REV**

**_1.00\082E5F232F1BF361C7F64916&0**, the serial number is


**082E5F232F1BF361C7F64916** .

For USB devices with a non-unique serial number, the serial


number begins one character before the first ampersand

character, and ends with the digit in front of the second


ampersand character. For example, for a USB device with the

path


**USBSTOR\DISK&VEN_GENERAL&PROD_UDISK&REV_5.0**

**0\6&1E2A3&0&_&0** the serial number is **6&1E2A3** .


The Cybereason platform supports devices with non-unique serial

numbers, but does not support setting a different mode for the


device under the **Manage devices** table in a scenario where the

serial number changes. If your end-users are using USB devices


with non-unique serial numbers, see Manage USB devices with

non-unique serial numbers.

## Manage USB devices with non-unique

## serial numbers


You cannot set a different mode for USB devices manufactured

with a non-unique serial number, because every time the user


removes and inserts the USB device into a different USB port or

computer, the serial number changes. The next time the


Cybereason platform identifies the USB device, Cybereason

disregards the new mode set for the device under the **Manage**


**devices** area, and reapplies the mode set for all USB devices

under the **Device control** .


If your organization is using USB devices with non-unique serial


numbers:


Provide only the product and vendor name and not the serial


number to manage USB devices in the same group as this
USB device. **However, note that this does not configure a**


**specific USB device** . For example, if you provide the product

ID and vendor ID for the following USB device instance path,


the Cybereason platform configures all Ultra Fit products from

the SanDisk vendor.


**/USBSTOR\DISK&VEN_SANDISK&PROD_ULTRA_FIT&RE**

**V_1.00**


For more details on how to find the product and vendor IDs,

see Find the device vendor and product information on


Windows machines or Find the device vendor and product

information on macOS machines.


If you still need to manage a USB device based on a specific

serial number, ensure that users do not move USB devices


from one USB port to another, and that they do not change

computers. In this case, the serial number stays the same.

## Check whether a USB device's serial

## number is unique


**To check whether a USB device's serial number is unique,**

**follow these steps:**


1. In Windows, open **Device Manager** and locate the relevant


USB device.


2. Right-click the relevant USB device, and click **Properties** .

3. In the **Properties** window, click the **Details** tab, and from the


**Property** drop-down menu, click **Capabilities**, and then look

for the following text under **Value** :


**CM_DEVCAP_UNIQUEID**


If **CM_DEVCAP_UNIQUEID** is visible in the **Value** area, the


USB device serial number is unique. For example:


If **CM_DEVCAP_UNIQUEID** is not visible, the USB device


serial number is non-unique. For example:



