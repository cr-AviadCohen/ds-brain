|Mode|Description|Recommendation|
|---|---|---|
|Disabled<br>(default)|Predictive ransomware<br>protection is disabled.|Not recommended.<br>Can be used in cases<br>where Predictive<br>ransomware<br>detection is not<br>required.|
|Detect|Predictive ransomware<br>protection is enabled in<br>detect-only mode.<br>When ransomware is<br>detected, a MalOp is<br>generated, but no<br>further action is taken.|Not recommended.<br>Use for testing<br>purposes only.|
|Prevent|When ransomware is<br>detected, a MalOp is<br>generated, and the<br>process is prevented<br>from running in on the<br>same endpoint<br>machine. In a scenario<br>where the ransomware<br>is running from a<br>legitimate process or<br>enabler process, the<br>relevant threads are<br>killed, and the process<br>can still run.|Recommended.|
|Quarantine|When ransomware is<br>detected, a MalOp is<br>generated, the process<br>is quarantined, and the<br>process is prevented<br>from running in the<br>system. In a scenario<br>where the ransomware<br>is running from a<br>legitimate process or<br>enabler process, the<br>relevant threads are<br>killed, and the process<br>can still run.|Recommended|


## Set the Predictive ransomware

## protection sensitivity level

You can configure the level of sensitivity that the Predictive


ransomware protection uses to detect and prevent ransomware.

The sensitivity levels determine whether the Predictive


ransomware protection feature is triggered and whether to

generate MalOps for suspicious processes. This is different from


the Predictive ransomware protection mode, which determines

how to handle the suspicious process.


Select one of the following options:








|Mode|Description|When to use this<br>setting|
|---|---|---|
|Cautious|This is the setting with<br>the lowest sensitivity.<br>With this setting, more<br>fle encryption events<br>trigger MalOps,<br>compared to the<br>**Recommended**<br>**(default)** option. As a<br>result, the<br>Cybereason platform<br>detects the<br>ransomware at a later<br>stage.|You want to detect<br>processes that<br>indicate<br>ransomware<br>behavior with a<br>very low false<br>positive rate.<br>When you select<br>this option,<br>additional fles<br>may become<br>encrypted before<br>the Cybereason<br>platform responds.|
|Recommended<br>(default)|This is the setting with<br>the recommended<br>sensitivity. With this<br>setting, the<br>Cybereason platform<br>triggers MalOps for<br>processes that<br>indicate a<br>ransomware attack<br>with a high level of<br>certainty.<br>As a result, the<br>Cybereason platform<br>detects the<br>ransomware at an<br>early stage of the<br>attack.|You want to detect<br>processes that<br>indicate<br>ransomware<br>behavior, while<br>streamlining<br>analysis of the<br>MalOps. With this<br>setting, the<br>Cybereason<br>platform can<br>detect<br>ransomware<br>quickly, and<br>provide the best<br>protection.|


|Mode|Description|When to use this<br>setting|
|---|---|---|
|Aggressive|Trigger MalOps for<br>any processes that<br>Cybereason<br>determines are likely<br>to indicate a<br>ransomware attack.|You want to detect<br>a ransomware<br>attack. You prefer<br>to assess and<br>analyze some<br>false positives, as<br>well as processes<br>that are likely, but<br>not certain, to be<br>ransomware.|



With Predictive ransomware protection, the Cybereason platform
checks that a defined number of files were encrypted over a


defined period of time, for a defined amount of different file

extensions. These numbers are smaller for higher sensitivity levels.


For example, if the sensitivity level is **Aggressive**, the Cybereason

platform triggers Predictive ransomware protection where only a


few files with the same file extension were encrypted in a relatively

long period of time.


While you cannot tune each of these numbers specifically, the
sensitivity level allows you to define how frequently the


Cybereason platform triggers Predictive ransomware protection.

Cybereason keeps monitoring the threat landscape and will


update these MalOp trigger values if needed.


To show how the Predictive ransomware protection mode and


sensitivity level work together, in an example scenario, the

Predictive ransomware mode is set to **Quarantine** and the


sensitivity level is set to **Cautious** :

1. The Cybereason platform determines that the file indicates a


ransomware attack with a very high level of certainty.
2. Predictive ransomware protection is triggered, and the file is


quarantined.

## Configure Predictive ransomware

## protection options


You can also instruct the Cybereason platform to detect


ransomware based on the following behaviors:


The ransomware attempts to delete shadow copies on the


machine as part of its behavior.

The ransomware attempts to edit the Master Boot Record


(MBR) on Windows machines.

The ransomware attempts to encrypt user files on the


machine.


**To enable Predictive ransomware protection features, follow**


**these steps:**


1. In the **Predictive ransomware protection** screen, locate the


**Shadow copy** option and set the toggle to **On** .


This option enables the Cybereason platform to find


ransomware that attempts to delete or manipulate the shadow

copies on the machine as part of its pattern.


2. In the **Rapid recovery** section, set the toggle to **On** .


Note


To use the **Rapid recovery** option, you must set the

Predictive ransomware protection mode to **Prevent** or


**Quarantine** .


This option restores encrypted files. For more information, see


Enable Rapid recovery.

3. In the **MBR** section, set the toggle to **On** .


This option enables you to find ransomware that attempts to

edit the Master Boot Record (MBR) on Windows machines.


Note


If you need to install applications that edit the MBR, such


as BitLocker, Cybereason recommends that you disable

this option prior to the installation or enablement of the


application. After you install or enable the application, you

can enable this setting again.

## Enable Rapid recovery


Predictive ransomware protection allows you to restore end-users'
encrypted files through the Volume Shadow Copy Service (VSS).


In order to restore files from the VSS, the VSS service must be

running on the user's machine. To learn more about how VSS


[works, see the Microsoft VSS documentation](https://learn.microsoft.com/en-us/windows-server/storage/file-server/volume-shadow-copy-service)

[(https://learn.microsoft.com/en-us/windows-server/storage/file-](https://learn.microsoft.com/en-us/windows-server/storage/file-server/volume-shadow-copy-service)


[server/volume-shadow-copy-service). Please see our Legal](https://learn.microsoft.com/en-us/windows-server/storage/file-server/volume-shadow-copy-service)

[Disclaimer (/resource-documents/legal-disclaimer-third-party-web-](https://nest.cybereason.com/resource-documents/legal-disclaimer-third-party-web-sites)


[sites).](https://nest.cybereason.com/resource-documents/legal-disclaimer-third-party-web-sites)


Note


Rapid recovery is supported on local drives on the endpoint

machine. Rapid recovery is also available if the ransomware is


detected by Variant Payload Prevention.


Predictive ransomware protection creates the restored file in the


same path as the encrypted file, and appends **.restored** to the
original file name. For example, the **Jon.txt** file was encrypted,


and Predictive ransomware protection creates a file named

**Jon.restored.txt** .


In the MalOp details screen, all files restored by Predictive

Ransomware Protection appear at the top of the Affected Files


section, followed by the files that were not restored (starting from
version 23.1.124). This helps you quickly identify the files that were


successfully restored.


To use the **Rapid recovery** option, you must set the Predictive


ransomware protection mode to **Prevent** or **Quarantine** .


You can either use the Cybereason platform backup service to


restore encrypted files, or you can integrate with a predefined VSS

used in your organization. The Cybereason platform backup


service is the default option.


Note


If you deactivate Rapid recovery, Cybereason does not

automatically delete the shadow copies it has generated. You


may choose to delete these manually.


**To configure the Rapid recovery option** :


1. Select the backup type for encrypted files:


To use the Cybereason platform backup service, leave


the **Use Cybereason backup service** option selected.

If your organization is using a backup service and you


would like to continue using this service, select **Use**

**existing backup service** .


Note


If you already have System Protection enabled in


Windows, you should use the **Use existing backup**

**service** option.



