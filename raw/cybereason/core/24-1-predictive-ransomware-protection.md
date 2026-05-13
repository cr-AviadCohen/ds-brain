To learn how to configure Predictive ransomware protection, see


[Set the Predictive Ransomware Protection Levels (/s/knowledge-](https://nest.cybereason.com/s/knowledge-base?article=24-1-set-the-predictive-ransomware-protection-levels&language=en_US#set-the-predictive-ransomware-protection-levels)

[base?article=24-1-set-the-predictive-ransomware-protection-](https://nest.cybereason.com/s/knowledge-base?article=24-1-set-the-predictive-ransomware-protection-levels&language=en_US#set-the-predictive-ransomware-protection-levels)


[levels&language=en_US#set-the-predictive-ransomware-](https://nest.cybereason.com/s/knowledge-base?article=24-1-set-the-predictive-ransomware-protection-levels&language=en_US#set-the-predictive-ransomware-protection-levels)

[protection-levels).](https://nest.cybereason.com/s/knowledge-base?article=24-1-set-the-predictive-ransomware-protection-levels&language=en_US#set-the-predictive-ransomware-protection-levels)


Watch this video to learn more about how Predictive ransomware

protection protects against the Conti strand of ransomware.


disabled (set to **Off** ) by default.


**Rapid Recovery:** Automatically restores the user's encrypted
files through the VSS, which allows the organization to access


files that were backed up in various scenarios. To configure

[this feature, see Enable Rapid recovery (/s/knowledge-base?](https://nest.cybereason.com/s/knowledge-base?article=24-1-set-the-predictive-ransomware-protection-levels&language=en_US#enable-rapid-recovery)


[article=24-1-set-the-predictive-ransomware-protection-](https://nest.cybereason.com/s/knowledge-base?article=24-1-set-the-predictive-ransomware-protection-levels&language=en_US#enable-rapid-recovery)

[levels&language=en_US#enable-rapid-recovery).](https://nest.cybereason.com/s/knowledge-base?article=24-1-set-the-predictive-ransomware-protection-levels&language=en_US#enable-rapid-recovery)


Note


Rapid recovery is supported on local drives on the


endpoint machine.


**Master Boot Record (MBR) protection:** Allows organizations


to protect their endpoints against bootkits and respond early

in the attack lifecycle, even before the attacker attempts to


encrypt the files. This feature protects against all bootkit

attacks, including ransomware attacks. This feature is


disabled (set to **Off** ) by default.


Predictive ransomware protection monitors all relevant file events


on the endpoint, and performs the following checks:

1. The Cybereason platform monitors all relevant file events for


all processes, to identify activity that might indicate a

ransomware attack.


2. For each relevant process, the Cybereason platform checks

whether the process is encrypting the file. The Cybereason


platform compares the state of the file before and after the file
was edited against a number of file characteristics, and


determines whether the file was modified as part of a regular
user operation, or whether the modification was an actual


encryption.
3. To define whether the process is behaving like ransomware,


the Cybereason platform checks whether a defined number of
files were encrypted over a defined period of time, for a


defined amount of different file extensions. These numbers

change according to the sensitivity level. For more


[information, see Set the Predictive ransomware protection](https://nest.cybereason.com/s/knowledge-base?article=24-1-set-the-predictive-ransomware-protection-levels&language=en_US#set-the-predictive-ransomware-protection-sensitivity-level)

[sensitivity level (/s/knowledge-base?article=24-1-set-the-](https://nest.cybereason.com/s/knowledge-base?article=24-1-set-the-predictive-ransomware-protection-levels&language=en_US#set-the-predictive-ransomware-protection-sensitivity-level)


[predictive-ransomware-protection-](https://nest.cybereason.com/s/knowledge-base?article=24-1-set-the-predictive-ransomware-protection-levels&language=en_US#set-the-predictive-ransomware-protection-sensitivity-level)

[levels&language=en_US#set-the-predictive-ransomware-](https://nest.cybereason.com/s/knowledge-base?article=24-1-set-the-predictive-ransomware-protection-levels&language=en_US#set-the-predictive-ransomware-protection-sensitivity-level)


[protection-sensitivity-level).](https://nest.cybereason.com/s/knowledge-base?article=24-1-set-the-predictive-ransomware-protection-levels&language=en_US#set-the-predictive-ransomware-protection-sensitivity-level)


Note


When Predictive ransomware protection is enabled, canary
files are installed for two minutes and then disappear.


As soon as Ransomware protection detects a malicious process,


the platform can automatically suspend the process and generate

a Malop. The Malop details show whether the ransomware


affected any user files, and how many user files the ransomware

affected. In this scenario, Ransomware protection automatically


suspends or prevents the process.


You can then perform additional remediation actions. If you enable


Application Control, and mark the process for prevention from the

**Malop details** screen or the **Investigation** screen, the


Cybereason platform sends the hash of the ransomware to all

endpoints across your installation and prevents the ransomware


from executing in the future.

## Kernel based protection


Modern ransomware attacks execute increasingly faster. Modern


ransomwares can encrypt files at a speed of 300-400 MB per

second.


To address this risk, Predictive ransomware protection works at the

kernel level, which allows the Cybereason platform to detect a


ransomware attack significantly faster than the time it would take

to detect manipulation of canary folders on different endpoint


machines.


In addition, attackers are learning how to bypass decoy files,


making the canary file solution less effective. While canary files

may confuse endpoint users, Predictive ransomware protection is


not visible to the endpoint user and works seamlessly behind the

scenes.


Cybereason recommends that you upgrade to the most recent

product version to leverage Predictive ransomware protection. To


understand which type of ransomware protection you need to use

according to your sensor version, see Ransomware protection


types per version. For more information on the previous Anti[Ransomware solution based on canary files, see Anti-](https://nest.cybereason.com/s/knowledge-base?article=24-1-anti-ransomware-protection-canary-files&language=en_US#anti-ransomware-protection-canary-files)


[Ransomware Protection (Canary Files) (/s/knowledge-base?](https://nest.cybereason.com/s/knowledge-base?article=24-1-anti-ransomware-protection-canary-files&language=en_US#anti-ransomware-protection-canary-files)

[article=24-1-anti-ransomware-protection-canary-](https://nest.cybereason.com/s/knowledge-base?article=24-1-anti-ransomware-protection-canary-files&language=en_US#anti-ransomware-protection-canary-files)


[files&language=en_US#anti-ransomware-protection-canary-files).](https://nest.cybereason.com/s/knowledge-base?article=24-1-anti-ransomware-protection-canary-files&language=en_US#anti-ransomware-protection-canary-files)

## Protection for network and cloud-based


Some ransomware strains have evolved and target shared


network and cloud drives in addition to local drives.


Predictive ransomware protection protects network and cloud

based drives. At this point, you cannot configure protection

settings of network and cloud-based drives.


Note


When the Cybereason platform analyzes a cloud drive, the

response time is slightly slower than the analysis of a local


drive.


Network and cloud-based drive protection is valid only for network


drives that are mapped on the endpoint. A mapped network drive:


Points to resources found on your network / Cloud storage


drive.

Has a drive letter assigned like any other partition in your


system.


From version 23.2.6x, Predictive Ransomware Protection can


prevent ransomware in cases where another machine on the

network is that is not protected by Predictive Ransomware


Protection attempts to execute the ransomware on a machine that

is protected by Predictive Ransomware Protection (for example,


by using shared folders). In previous versions, this behavior was

detected, but not prevented.

## Ransomware MalOps detai


For ransomware MalOps, the MalOp Details screen presents
information about the encryption process, encrypted files,


prevention/remediation actions, and more, including:


**Root cause:** Ransomware behavior


**Process information:** The encrypting process and the

original ransomware process


**Encrypted files:** List of files (full path) that were encrypted by

the ransomware before it was blocked


**Restored files** including which files were successfully / not

successfully restored


**File information:** The files of the encrypting process and the

original ransomware process


**Network information:** Network connections and DNS queries

of the encrypting process and the original ransomware


process

**Machine information:** Machines on which the Ransomware


was executed

**User information:** The users associated with the execution of


the encrypting process and the original ransomware process

## Ransomware protection types per


The following table describes which type of ransomware


protection you can use according to your Cybereason platform

version.


|Server<br>version|Protection type<br>available|Sensor version usage<br>notes|
|---|---|---|
|23.1.10x<br>and<br>higher|Predictive<br>Ransomware<br>Protection and Anti-<br>Ransomware are<br>both available by<br>default in the<br>Sensor Policy<br>screen.|Predictive Ransomware<br>Protection is recommended<br>for sensors version<br>23.1.124 and higher. Older<br>sensors should use Anti-<br>Ransomware. Make sure to<br>update your sensors to the<br>latest version before<br>enabling Predictive<br>Ransomware Protection, to<br>avoid endpoint<br>compatibility issues.|
|23.1.8x<br>and<br>lower|Anti-Ransomware is<br>available in the<br>Sensor Policy<br>screen. To make<br>Predictive<br>Ransomware<br>Protection available<br>in this screen,<br>contact<br>Cybereason<br>Support.|Predictive Ransomware<br>Protection is recommended<br>for sensors version<br>23.1.124 and higher. Older<br>sensors should use Anti-<br>Ransomware. Make sure to<br>update your sensors to the<br>latest version before<br>enabling Predictive<br>Ransomware Protection, to<br>avoid endpoint<br>compatibility issues.|







