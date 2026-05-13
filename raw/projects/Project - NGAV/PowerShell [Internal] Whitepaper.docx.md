# PowerShell [Internal] Whitepaper.docx

Cybereason’s NGAV can detect and block PowerShell attacks

**INTERNAL ONLY - DO NOT SHARE EXTERNALLY**

What is PowerShell?

PowerShell is a Windows management framework, and has been around for over a decade. It is a scripting engine that enables IT to automate tasks on a Windows environment using intuitive syntax. PowerShell is built on the .NET framework, and has been designed to access .NET, COM, Windows API, and communicate with remote machines.

Why & How is PowerShell used Maliciously?

Why

Over the past few years we’ve witnessed PowerShell becoming attackers’ favorite post-exploitation tool.

PowerShell enables attackers to execute crucial stages of the attack lifecycle without dropping any proprietary binaries or executables on the target’s environment. PowerShell attacks can range from the basic Download & Execute payloads to APTs and even Ransomware. PowerShell is a powerful hacking tool because it enables adversaries to:

**Live off the land**. PowerShell is a native tool that already exists in every environment. Every modern Windows OS ships with PowerShell by default.

**Take advantage of insecurities.** Windows 7 is still the most popular desktop OS in the world, and comprises roughly [50% of the global market](https://www.netmarketshare.com/operating-system-market-share.aspx?qprid=10&qpcustomd=0). Meaning PowerShell version 2 is still the most popular version in use out does not contain the security improvements of later versions. In addition, many attacks, including those created with Metasploit, perform a downgrade to PowerShell 2 even if a newer version is installed in order to avoid the improved security features in later versions.

**Conduct fileless malware attacks.** PowerShell has built-in commands that enable downloading code and running it in-memory. Meaning attackers can use PowerShell to execute an attack without dropping any binary or executables on the machine.

**Perform any type of administrative activity on a Windows Platform.** PowerShell is built into all Windows environments. PowerShell was designed to access the .NET framework, Windows API, WMI, and more. This means that PowerShell really enables attackers to do pretty much anything they want on a Windows machine some examples include credential dumping, input collection (key logging, video collection/screen capture, etc.) as well as enabling attackers to build custom attack code.

**Evade detection.** PowerShell is a trusted process. PowerShell is a legitimate tool signed by Microsoft and widely used by IT personnel for admin purposes. And scripting languages are notoriously flexible and therefore easy to obfuscate. This makes it very difficult for many detection solutions to decipher legitimate from malicious use.

How

Due to the versatile nature of PowerShell, numerous tools created by attackers and shared by the information security community offer a tremendous opportunity for adversaries to quickly leverage PowerShell in a fileless malware attack and evade detection. To name a few:

* **PowerShell frameworks** such as [Empire](http://www.powershellempire.com/), [PS>Attack](https://github.com/jaredhaight/PSAttack), [PowerSploit](https://github.com/PowerShellMafia/PowerSploit), [PoshC2](https://github.com/nettitude/PoshC2/) and [Nishang](https://github.com/samratashok/nishang) include scripts for code injections, credential theft, keylogging MITM, etc. Some frameworks even provide delivery methods by Office Macros, DLLs, batch files, hta files and more.
* **Obfuscation Tools** such as [Veil](https://github.com/Veil-Framework/Veil), [Magic Unicorn](https://github.com/trustedsec/unicorn) and [Invoke-Obfuscation](https://github.com/danielbohannon/Invoke-Obfuscation) and [Invoke-CradleCrafter](https://github.com/danielbohannon/Invoke-CradleCrafter) focus on generating stealthy payloads to evade signature based detection. There’s even a project that integrates Invoke-Obfuscation and Empire called [ObfuscatedEmpire](https://github.com/cobbr/ObfuscatedEmpire).
* **Social Engineering frameworks** such as  [BeEF (Browser Exploitation Framework)](http://beefproject.com/) and [SET (Social Engineering Toolkit)](https://www.trustedsec.com/social-engineer-toolkit-set/) offer PowerShell stagers to run the main payload.
* **Office Macro Toolkits** such as Microsploit, LuckyStrike and others allow attackers to generate Malicious Office documents for Phishing purposes.
* **PowerShell Without PowerShell** refers to an interesting set of projects, such as [PowerShdll](https://github.com/p3nt4/PowerShdll) (managed) and [PowerShellRunner](https://github.com/leechristensen/UnmanagedPowerShell) (unmanaged), that created to demonstrate that the PowerShell engine can be hosted in processes other than powershell.exe. These projects load *System.Management.Automation.dll* to run the PowerShell engine. Casey Smith (@subTee) took this approach even further, by invoking the PowerShell engine using Microsoft signed executables, such as [Msbuild.exe](https://gist.github.com/subTee/6b236083da2fd6ddff216e434f257614). Since any process can host PowerShell, defenders looking for malicious PowerShell activity should suspect every process on the system. This capability was naturally incorporated into frameworks such as Empire, in combination with reflective DLL loading to covertly host the PowerShell engine. Loading PowerShell to other processes is also commonly used to bypass whitelisting solutions that restrict the use of powershell.exe. CobaltStrike Beacon, Metasploit’s Meterpreter and tools like [Harness](https://github.com/Rich5/Harness) employ similar techniques to run arbitrary PowerShell commands on a compromised machine by loading the engine to the hosting process.

Why do Existing Techniques Fail to Detect/Block Malicious use of PowerShell?

Protection mechanisms offered by security vendors focus their detection on command lines, signatures, or logging features implemented in newer versions of PowerShell. However, these defense mechanisms are continuously bypassed, some examples of this can be found [here](https://cobbr.io/ScriptBlock-Logging-Bypass.html) and [here](http://cn33liz.blogspot.co.il/2016/05/bypassing-amsi-using-powershell-5-dll.html).

The more defenders focus on signature based detections, attackers utilize stealthier payloads, such as obfuscating commands or using various processes to host the PowerShell engine. An example of such an attack is reflectively loading PowerShell Empire DLL into a legitimate process.

This is precisely why Cybereason developed a unique approach to detecting and blocking PowerShell based attacks. Our approach leverages deep visibility into the PowerShell script and continuously monitors for malicious behaviors to ensure we’re not missing any PowerShell abuse. This approach was defined and implemented after our team conducted extensive research on where current methods fail to detect PowerShell based attacks. Some of our findings are described below:

Why command line monitoring fails

Many security vendors monitor the command line of the powershell.exe or powershell\_ise.exe process and look for malicious code. Using this method enables detection of some attacks, but more sophisticated attacks obfuscate or encrypt the command line, or only provide a name of a script file and not the actual script in the command line, or oftentimes they will not even run a PowerShell process but rather load a PowerShell DLL so there is no command line in the first place. To summarize, there are several ways for an attacker to evade command line auditing including:

* **Script files.** Attackers running malicious commands contained in a script file. Command line logging would only disclose the script file path.
* **Interactive Shell.** Any input the user types in the PowerShell console would not appear in command line logs. These are commands being run directly from the PowerShell engine.
* **Loading System.Management.Automation.dll.** These attack vectors load the PowerShell engine and there is no command line to audit since there is no PowerShell process.

Why signature-based detection fails

Traditional AV products can inspect script files that are run on the system and occasionally succeed in detecting malicious script files as they enforce signature-based detection, like searching for the string “Invoke-Mimikatz” (to accomplish tasks like credential dumping). However, most scripted attacks today evade detection by obfuscating their code so it’s harder for AV/NGAV/traditional detection solutions to create a reliable signature. In addition, most offensive activities take a “fileless malware” approach, so there’s no file on disk to scan. In addition to that, most AVs scan binaries, and when it comes to a fileless attack there will be no binaries on disk.

Windows 10 AMSI (Antimalware Scan Interface) is designed to deal with contemporary trends of obfuscation and in-memory attacks, since it gives AV vendors the ability to scan and block input before it is run by the scripting engine (therefore, in-memory scripts are also analyzed). But this approach also fails:

* The most common PowerShell version 2 is not supported
* Several AMSI bypass techniques have been published and integrated in frameworks like Empire
* AMSI is only as good as the detection rules AV vendors create, and most vendors haven’t integrated with AMSI
* Popular obfuscation techniques, such as Token Obfuscation, do not create a new script block, and therefore, are not de-obfuscated by AMSI.

Why PowerShell security/logging features fail

There are many ways to bypass built-in PowerShell security features including logging to describe a few:

* **Eventlogs (PowerShell 2)** cannot be analyzed to determine if a malicious payload was run
* **Module Logging (PowerShell 3)** analysts and security products often cannot handle the amounts of data module logs produce. Module logging often misses important parts of an attack that do not rely on Cmdlets. For example, non-Cmdlet .NET functions, like DownloadString are not logged, and as a result the analyst could miss the attacker’s domain from which the payload was downloaded.
* **Transcript Logging (PowerShell 5)** is easily bypassed. For example, simply using command line PowerShell with the “-encodedcommand” flag (or one of its aliases) and a base64 payload could be used to hide malicious code.
* **ScriptBlock Logging (PowerShell 5)** there are obfuscation techniques that can completely evade logging even if the payload is using suspicious keywords.
* In addition, many attacks, including those created with Metasploit, **perform a downgrade to PowerShell 2 even if a newer version is installed in order to avoid the improved security features in later versions.**

Why Monitoring PowerShell process interaction/injection fails

Various attack techniques rely on spawning the powershell.exe from an uncommon parent process, such as a Microsoft Excel in the case of using Office Macro. Security vendors monitor such uncommon process tree and log/block them. In addition, security vendors will look for when PowerShell injects into another process to pick up on malicious use. Although these approaches would detect some PowerShell attacks, **there are many scenarios where an attacker does not need to leverage injection techniques or spawn a child process to be successful in leveraging PowerShell as part of their attack.**

*For example, say an attacker runs credential dumping from within the Powershell engine itself (e.g. the PowerShell version of Mimikatz). This technique would not require any interaction with another process or spawn any child processes, so traditional solutions including our top competitors (i.e. Crowdstrike & CarbonBlack) would miss this.*

The Cybereason Approach

To detect PowerShell based attacks most efficiently, deep visibility and behavioral analytics is required. Cybereason leverages full visibility into all activities and commands taking place **within the PowerShell engine.** This means we’re not just looking at the raw script or the command line (which oftentimes is encoded or obfuscated), we’re looking at every action taken by the code that’s running within the PowerShell engine. **And the behavioral analysis done by Cybereason is not only done at the process level but also on the PowerShell code level.**

When using only the former detection approach (leveraging behavioral analysis solely at the process level) pose a few major problems:

**These solutions will miss things!** For example, Cybereason is able to determine, at the code level, if a download instruction is followed by an execution instruction (which indicates malicious activity related to payload staging.) In this case, these activities took place inside the powershell process itself and did not lead to any interaction between that PowerShell process and any other processes (e.g. injections or child processes). In this case, our competitors would not flag anything, because they don’t have that visibility into the engine.

**These solutions will generate more false positives!** For example many admin tools use encoded PowerShell commands, and if the detection/prevention solution does not have visibility into what’s actually running inside the PowerShell engine, the detection solution would flag this as a detection even though this is just a normal part of the organization’s security operations.

The Cybereason solution is proactively hunting, 24/7, for patterns of activity that indicate malicious behavior within the script itself in order to decipher legitimate from malicious use with high fidelity. And, in addition to being able to detect a wide range of sophisticated PowerShell attacks including: Empire,PowerSploit, and Nishang, our NGAV solution **automatically blocks PowerShell based attacks up front.**

Today, none of our competitors leverage visibility into the PowerShell script itself for detection or have the ability to block PowerShell attacks from executing. This means that our competitors will not be able to detect and block crucial stages of the attack lifecycle that are executed via PowerShell including persistence, lateral movement, and credential dumping **as these oftentimes take place only within the PowerShell engine itself.**
