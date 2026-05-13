|Type|Details|
|---|---|
|General|When setting Anti-Malware modes (Anti-<br>Malware, Signatures, AI Detect, AI<br>Prevent), you must provide values for all<br>four Anti-Malware settings.<br>If you use invalid installer parameters<br>when you install the sensor, the<br>Cybereason platform ignores the<br>parameters and sensors remain<br>confgured as before. If no prior<br>confguration exists, the Cybereason<br>platform follows the default sensor policy.<br>Some types of malware are not fully<br>removed from a machine until a machine<br>reboot.<br>Allowlisting sometimes only takes effect<br>after a machine reboot. If malware is<br>disinfected and then added to the<br>allowlist, and then the same malware<br>reappears in the same path where the<br>malware originally appeared,<br>Cybereason may again recognize the fle<br>as malware.<br>(Japanese environments only) The<br>Malware alerts CSV is not translated to<br>Japanese.|


|Type|Details|
|---|---|
|Signatures<br>mode|If Anti-Malware > Signatures mode is<br>enabled and the sensor's minionhost.exe<br>process is killed (which is unlikely),<br>Windows Security Center detects that no<br>AV is installed and enables Windows<br>Defender, which may cause conficts<br>with Cybereason AV.<br>When a machine is isolated, you cannot<br>download/update the Signatures (AV)<br>database on that machine. To update the<br>Signatures database on an isolated<br>machine, you must remove it from<br>isolation, then update.<br>On Windows Server 2016 and on<br>Windows 7 in some scenarios, enabling<br>Signatures mode (AV) does not disable<br>Windows Defender. As a best practice,<br>Cybereason recommends that you make<br>sure that Windows Defender is disabled<br>before you enable Anti-Malware ><br>Signatures mode.<br>If a machine has been isolated, the<br>machine cannot download updates to its<br>signatures database from the NGAV<br>Update server.<br>Sensors with Signatures mode enabled<br>manually (not via sensor policies) do not<br>support scheduled scans.<br>When quick/full scans are in progress,<br>the end user does not see the status of<br>the scan in the system tray.<br>Administrators can view scan status in<br>the**System > Sensors** screen in the<br>'Last quick scan' and 'Last full scan'<br>columns.<br>When a fle is prevented (by Anti-<br>Malware > Signatures > Prevent mode),<br>and then the fle is added to the allowlist,<br>a machine restart is required before<br>users can access the fle.<br>On Windows Servers, when Folder<br>Redirection is enabled, fles detected in<br>redirected folders are not quarantined<br>(even if Quarantine mode was selected).|


|Type|Details|
|---|---|
|Supported<br>operating<br>systems|If Cybereason does not recognize<br>whether a specifc OS version supports<br>Anti-Malware confguration, Cybereason<br>still sends the command to the sensor. If<br>the OS version does not support Anti-<br>Malware, the sensor will not perform the<br>command..<br>Artifcial intelligence is not supported on<br>endpoints with Cluster Shared Volume<br>(CSV).|
|Simultaneous<br>changes|If two users change the mode for the same<br>sensor at the same time, the resulting<br>confguration may vary. In this case, the<br>correct confguration should be re-sent to the<br>sensor after the issue is discovered.|
|Action log|The "Success" message in the action log<br>on the**Sensors** screen refects<br>successful communication to the sensor<br>and does not necessarily mean the<br>sensor has applied the new settings.|
|Exclusions|Paths must be a valid folder or directory.<br>The path must end with a forward slash<br>or a backslash. For example, you can<br>use**C:\Users\temp\** or**/var/www/html/**.<br>Ensure you do not mix forward slashes<br>and backslashes in the same exclusion,<br>for example,**C:\Users\temp,**<br>**/var/www/html/**<br>You can add exclusions for local<br>volumes only, not network drives.<br>If you exclude a folder that does not<br>currently exist, and later this folder is<br>created, Cybereason does not exclude<br>the folder from scans until the Anti-<br>Malware confguration is updated. As a<br>workaround, you can add and remove<br>another folder from the exclusions list.<br>This action refreshes the original<br>exclusion.<br>Excluding a path on Mac does not<br>support environment variables.<br>If you have disabled the Filter extensions<br>option, some fle exclusions are not<br>supported, such as .lnk extensions and<br>fles without extensions.|


When Anti-Ransomware prevents ransomware that has


already encrypted some files, in the Malop Details screen, it
shows that there are 0 affected files.

## Predictive ransomware protection


In heavy load Windows Server based environments, Predictive

ransomware protection may cause an increase in resource


demand and degradation of the sensor performance, which

can degrade the overall server performance. On such


environments, we recommend using the Canary Files-based

[Anti-Ransomware instead. For more information see PRP on](https://nest.cybereason.com/s/article/8993456)


[Heavy Load Servers (/s/article/8993456).](https://nest.cybereason.com/s/article/8993456)
When first installing the sensor package, the previous canary

based Anti-ransomware solution will be enabled for

approximately two minutes. This may cause some canary files


to be installed on the disk. After a few minutes, the canary files

will be deleted and the Predictive ransomware protection


solution will be functional. This issue is only relevant for the

Beta version of Predictive ransomware protection, and will be


fixed in future versions.

Network and cloud-based drives protection is activated once


the feature is activated.

When the Cybereason platform analyzes a cloud drive, the


response time is slightly slower than the analysis of a local

drive.


Rapid recovery is supported on local drives.

The Cybereason platform prevents overwriting of the MBR


under the assumption that legitimate cases of MBR
modification are very rare, and only performed once per


endpoint (e.g., while enabling/installing specific apps such as

Bitlocker). To install applications that modify the MBR,


Cybereason recommends disabling MBR protection

immediately prior to a planned disk encryption installation and


enabling it following installation (assuming that this is a one
time installation).


When resizing a disc, an MBR protection MalOp may be

created. To allow this behavior, you can create an exclusion


for vds.exe or disable the feature before performing this

action.


If MBR is enabled, and an end user attempts to expand drives

on their endpoints, the user may receive an **Access denied**


error. The reason is that this action affects the size of sector0

on the disk, which is where the MBR is nested. This type of


behavior can be related to malicious rootkits activity, therefore,

it is prevented. To allow this behavior, you can turn MBR


protection off for the time of the activity.
Customers that use .pst files (for Outlook) are advised to


create an exclusion "By command" for "outlook.exe" to reduce

performance impact of this feature.



