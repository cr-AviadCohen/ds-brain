## Review supported operating systems for sensors (all OSs)

Cybereason sensors are supported on numerous different


operating systems. For the full list of supported operating

[systems, see Supported OS Versions for the Sensor](https://nest.cybereason.com/s/knowledge-base?article=24-1-supported-os-versions-for-the-sensor&language=en_US#supported-os-versions-for-the-sensor)


[(/s/knowledge-base?article=24-1-supported-os-versions-for-the-](https://nest.cybereason.com/s/knowledge-base?article=24-1-supported-os-versions-for-the-sensor&language=en_US#supported-os-versions-for-the-sensor)

[sensor&language=en_US#supported-os-versions-for-the-sensor).](https://nest.cybereason.com/s/knowledge-base?article=24-1-supported-os-versions-for-the-sensor&language=en_US#supported-os-versions-for-the-sensor)

## Understand the system requirements (all


The minimum system requirements for endpoints depend on

whether you enable Endpoint Prevention features or not.


Note


The resource requirements stated below may differ from the


actual sensor resource usage in practice. For actual resource

[usage estimates, see Sensor Resource Usage (/s/knowledge-](https://nest.cybereason.com/s/knowledge-base?article=24-1-sensor-resource-usage&language=en_US#sensor-resource-usage)


[base?article=24-1-sensor-resource-](https://nest.cybereason.com/s/knowledge-base?article=24-1-sensor-resource-usage&language=en_US#sensor-resource-usage)

[usage&language=en_US#sensor-resource-usage).](https://nest.cybereason.com/s/knowledge-base?article=24-1-sensor-resource-usage&language=en_US#sensor-resource-usage)

## - Minimum requirements Endpoint data

## collection only






|Component|Requirement|
|---|---|
|Machine RAM|4 GB|
|CPU|Dual core 2 Ghz core i3 and<br>above or equivalent|
|Available disk space|2 GB minimum|
|Network connectivity|Ethernet or Wi-Fi|
|Virtual memory|Do not restrict virtual memory<br>manually, but allow your<br>system to automatically<br>adjust to provide the needed<br>amount of virtual memory.|


|Component|Requirement|
|---|---|
|Endpoint machine RAM|8 GB|
|Server machine RAM|16 GB|
|Endpoint machine CPU|8 cores 2.5 Ghz or equivalent|
|Server machine CPU|8 cores 2.5 Ghz or equivalent|
|Available disk space (both for<br>endpoint and server<br>machines)|2 GB minimum|
|Network connectivity|Ethernet or Wi-Fi|
|Virtual memory|Do not restrict virtual memory<br>manually, but allow your<br>system to automatically<br>adjust to provide the needed<br>amount of virtual memory.|


## Minimum requirements - EDR and Endpoint Prevention






|Component|Requirements|
|---|---|
|Machine RAM|4 GB|
|CPU|Dual core 2 Ghz core i3 and<br>above or equivalent|
|Available disk space|2 GB minimum|
|Network connectivity|Ethernet or WiFi|
|Virtual memory|Do not restrict virtual memory<br>manually, but allow your the<br>system to automatically<br>adjust to provide the needed<br>amount of virtual memory.|


## Optimal requirements - EDR and Endpoint Prevention












|Component|Requirement|
|---|---|
|Endpoint machine RAM|16 GB|
|Server machine RAM|32 GB|
|Endpoint machine CPU|8 cores 2.5 Ghz or equivalent|
|Server machine CPU|16 cores 2.5 Ghz or<br>equivalent|
|Available disk space (both for<br>endpoint and server<br>machines)|2 GB minimum|
|Network connectivity|Ethernet or Wi-Fi|
|Virtual memory|Do not restrict virtual memory<br>manually, but allow your<br>system to automatically<br>adjust to provide the needed<br>amount of virtual memory.|


## Update additional endpoint machine
## requirements (Windows and Linux)






|Requirement|OS|
|---|---|
|The endpoints must meet the<br>Transport Layer Security (TLS)<br>communication requirements. For<br>more information, see Select your<br>TLS communication preferences<br>(/s/knowledge-base?article=24-1-<br>enable-communication-with-<br>cybereason-<br>servers&language=en_US#select-<br>your-tls-communication-<br>preferences).|Windows|


|Requirement|OS|
|---|---|
|On Windows endpoints, for the<br>Cybereason system tray icon and<br>notifcations to display, the<br>endpoint must have .NET<br>Framework 4.0<br>(https://www.microsoft.com/en-<br>us/download/details.aspx?<br>id=42642) or higher enabled.|Windows|
|On Windows endpoints, for<br>sensor versions earlier than<br>24.1.26X, you must have the<br>Microsoft C++ Runtime installed.|Windows|
|If EMET is not installed, we<br>recommend upgrading your<br>machine operating system to the<br>latest Windows version, because<br>Windows no longer offcially<br>supports EMET. If you are using<br>Exploit Guard on Windows 10 Fall<br>Creators Update (RS3) and later<br>versions, EMET is not required.<br>If EMET is not installed, we<br>recommend upgrading your<br>machine operating system to the<br>latest Windows version, because<br>Windows no longer offcially<br>supports EMET. If you are using<br>Exploit Guard on Windows 10 Fall<br>Creators Update (RS3) and later<br>versions, EMET is not required.|Windows|
|On Linux endpoints, you must<br>install the GNU C library (**glibc**).|Linux|

## Verify that Windows Event Log is running

Verify that the Windows Event Log service is running on the

endpoint and do not disable this service. If you disable this


service before or after the sensor installation, the sensor does not

install or function properly.


## Install the required certificates (all OSs)

[For more information, see Required Certificates for Cybereason](https://nest.cybereason.com/s/article/3140241)


[Sensor Installation (/s/article/3140241).](https://nest.cybereason.com/s/article/3140241)

## Install additional KBs (Windows)


If you are installing or upgrading a sensor on August 20, 2024 or


later, on supported version of Microsoft Windows, ensure you have

the following minimum KB version/patches installed on your


machines.


[For details on the minimum KBs required, see Windows Support](https://support.microsoft.com/en-us/topic/kb5022661-windows-support-for-the-trusted-signing-formerly-azure-code-signing-program-4b505a31-fa1e-4ea6-85dd-6630229e8ef4)


[for Trusted Signing (https://support.microsoft.com/en-](https://support.microsoft.com/en-us/topic/kb5022661-windows-support-for-the-trusted-signing-formerly-azure-code-signing-program-4b505a31-fa1e-4ea6-85dd-6630229e8ef4)

[us/topic/kb5022661-windows-support-for-the-trusted-signing-](https://support.microsoft.com/en-us/topic/kb5022661-windows-support-for-the-trusted-signing-formerly-azure-code-signing-program-4b505a31-fa1e-4ea6-85dd-6630229e8ef4)


[formerly-azure-code-signing-program-4b505a31-fa1e-4ea6-85dd-](https://support.microsoft.com/en-us/topic/kb5022661-windows-support-for-the-trusted-signing-formerly-azure-code-signing-program-4b505a31-fa1e-4ea6-85dd-6630229e8ef4)

[6630229e8ef4). Note that other KB update versions or patches will](https://support.microsoft.com/en-us/topic/kb5022661-windows-support-for-the-trusted-signing-formerly-azure-code-signing-program-4b505a31-fa1e-4ea6-85dd-6630229e8ef4)


also provide the same support.


Note


If you do not have the minimum KB patch/version installed on

the machine, the sensor will not work after


installation/upgrade.








|OS|Required KB version|
|---|---|
|Windows 7.0 SP1|KB 5006743 or later updates<br>KB 5006728 or later updates<br>Note<br>According to Microsoft<br>guidelines, you must also have<br>ESU support for your machine.<br>For more details on ESU<br>support, see FAQ about<br>Windows 7 ESU<br>(https://learn.microsoft.com/en-<br>us/troubleshoot/windows-<br>client/windows-7-eos-<br>faq/windows-7-extended-<br>security-updates-faq).|
|Windows 8|KB 5006739 or later updates|


|OS|Required KB version|
|---|---|
|Windows 8.1|KB 5006714 or later updates<br>KB 5006729 or later updates|
|Windows 10 (version<br>2004, 20H2, or 21H1)|KB 5005611 or later updates|
|Windows 10 (version<br>1507)|KB 5006675 or later updates|
|Windows 10 (version<br>1607)|KB 5006669 or later updates|
|Windows 10 (version<br>1809)|KB 5005625 or later updates|
|Windows 10 (version<br>1909)|KB 5005624 or later updates|
|Windows Server 2008 R2<br>SP1|KB 5006743 or later updates<br>KB 5006728 or later updates<br>Note<br>According to Microsoft<br>guidelines, you must also have<br>previously purchased ESU<br>support for your machine. For<br>more details on ESU support,<br>see FAQ about Windows 7<br>ESU<br>(https://learn.microsoft.com/en-<br>us/troubleshoot/windows-<br>client/windows-7-eos-<br>faq/windows-7-extended-<br>security-updates-faq).|
|Windows Server 2012|KB 5006739 or later updates<br>KB 5006732 or later updates|
|Windows Server 2012 R2|KB 5006714 or later updates<br>KB 5006729 or later updates|
|Windows Server 2016|KB 5006669 or later updates|
|Windows Server 2019|KB 5005625 or later updates|


|OS|Required KB version|
|---|---|
|Windows Server 2022|KB 5005619 or later updates|

## Install required packages (Linux)

Note


The Cybereason Linux sensor packages are not supported for

Linux 32-bit operating systems.


Before you install the Cybereason Linux sensor package on Linux

operating systems, verify that the following languages and


packages are installed on the endpoint:












|Language/Package/Utility|Notes|
|---|---|
|Python 2.6+ or Python 3.x|The Cybereason platform<br>supports all Python 3<br>versions, up to the latest<br>Python version.<br>**Note:**If you are using Python<br>3.11 or later, ensure your<br>Python distribution also has<br>the**distutils**or<br>**setuptools** modules<br>installed.|
|iptables|Required for machine<br>isolation to work.|
|libcurl.so.4||
|libnsl.so.1|If you experience installation<br>issues on RHEL or CentOS<br>8.3 or 8.4, see Sensor Fails to<br>Start on RHEL 8 Distributions<br>(/s/article/2943473).|
|librt.so.1||
|libpthread.so.0||
|libm.so.6||
|libgcc_s.so.1||


|Language/Package/Utility|Notes|
|---|---|
|libc.so.6||
|ld-linux-x86-64.so.2||
|libdl.so.2||
|libpopt.so.0||
|libelf.so.1||
|libattr.so.1||
|libz.so.1||
|libudev.so.1|This library is part of the<br>**systemd** package supported<br>on CentOS 7 and later|
|libcap.so.2|Enables retreiving and setting<br>Linux capabilities|
|librpm.so (https://librpm.so)|Allows RPM metadata<br>enrichment for the supported<br>operating system. Applicable<br>for RPM-based Linux<br>distributions.|
|librpmio.so<br>(https://librpmio.so)|Allows RPM metadata<br>enrichment for the supported<br>operating system. Applicable<br>for RPM-based Linux<br>distributions.|
|gdb|Required for Debian only -<br>Allows maximum debugging<br>capabilities. Recommended<br>for all Linux operating<br>systems.<br>**WARNING:** The Cybereason<br>sensor can function without<br>the**gdb** package but will<br>have reduced debugging<br>capabilities. We recommend<br>installing the**gdb** package to<br>enable these capabilities.|


|Language/Package/Utility|Notes|
|---|---|
|policycoreutils-devel|Required (CentOS/RHEL 7.6-<br>7.9, Ubuntu 20.04/22.04) to<br>use the eBPF framework. See<br>the table below for steps to<br>perform for the eBPF<br>framework.|



[If the installation fails, see Linux Sensor Installation Failures](https://nest.cybereason.com/s/article/144)

[(/s/article/144).](https://nest.cybereason.com/s/article/144)


In addition, in versions 23.2.65 and later, to use the eBPF-related

features on Linux machines running Centos/RHEL 7.6, 7.7, 7.8, or


7.9 or Ubuntu 20.04/22.04 (with kernel 5.15), you must do the

following:


```
  # for latest Centos7

  version (kernel version

  3.10.0-1160) use:

  wget

  http://mirror.centos.org/ce

  ntos/7/os/x86_64/Packages/k

  ernel-devel-`uname -r`.rpm

  # for latest Centos7

  version (kernel version

  3.10.0-1160) with patch

  version, use:

  wget

  http://mirror.centos.org/ce

  ntos/7/updates/x86_64/Packa

  ges/kernel-devel-`uname 
  r`.rpm

  # for lower kernels

  (<3.10.0-1160) use:

  wget

  https://vault.centos.org/`c

  at /etc/centos-release |

  awk {print

  $4}`/os/x86_64/Packages/ker

  nel-devel-`uname-r`.rpm

  # for lower kernels

  (<3.10.0-1160) with patch

  version, use:

  wget

  https://vault.centos.org/`c

  at /etc/centos-release |
  awk {print

  $4}`/updates/x86_64/Package

  s/kernel-devel-`uname 
  r`.rpm

```

2. Install the package using this command:


## Add sensor processes to third-party tool
## allowlists (all OSs)

When you install the Cybereason sensor, some third-party antivirus


tools may mistakenly prevent the execution of some Cybereason

installation processes and sensor processes. Cybereason


recommends that you add the Cybereason sensor processses,
files, and folders as an exclusion on the third-party security tools.


You should add the following as exclusions as needed before


installing the sensor to avoid perforomance issues and conflicts

between other security tools and the sensor.


**For machines running Windows:**






|Item|Exclusion|
|---|---|
|Sensor<br>processes|C:\Program Files\Cybereason<br>ActiveProbe\minionhost.exe<br>C:\Program Files\Cybereason<br>ActiveProbe\ActiveConsole\ActiveConsole.exe<br>C:\Program Files\Cybereason<br>ActiveProbe\ActiveConsole\PylumLoader.exe<br>C:\Program Files\Cybereason<br>ActiveProbe\AmSvc.exe<br>C:\Program Files\Cybereason<br>ActiveProbe\Execution<br>Prevention\ExecutionPreventionSvc.exe<br>C:\Program Files\Cybereason<br>ActiveProbe\CrsSvc.exe<br>C:\Program Files\Cybereason<br>ActiveProbe\Nnx.exe (used for Behavioral<br>Execution Prevention and Variant<br>Payload/Variant File Protection)<br>C:\Program Files\Cybereason<br>ActiveProbe\ProtectedSvc.exe<br>C:\Program Files\Cybereason<br>ActiveProbe\WscIfSvc.exe<br>C:\Program Files\Cybereason<br>ActiveProbe\ActiveConsole\CrDrvCtrl.exe<br>C:\Program Files\Cybereason<br>ActiveProbe\ActiveConsole\CrEX3.exe<br>C:\Program Files\Cybereason<br>ActiveProbe\ActiveConsole\SigCheck.exe<br>C:\Program Files\Cybereason<br>ActiveProbe\ActiveCLIAgent.exe<br>C:\Program Files\Cybereason<br>ActiveProbe\CrAmTray.exe|
|Sensor fle<br>directories|C:\Program Files\Cybereason ActiveProbe\<br>C:\ProgramData\apv2\<br>C:\ProgramData\crb1\<br>C:\ProgramData\crs1\|
|Sensor<br>drivers|C:\Windows\System32\drivers\crdrv.sys<br>C:\Windows\System32\drivers\CrElam.sys<br>C:\Windows\System32\drivers\gzft.sys|


**For machines running macOS**







|Item|Exclusion|
|---|---|
|Sensor processes|CybereasonSensor<br>CybereasonActiveConsole<br>CybereasonAVKext (in<br>macOS earlier than<br>versions 11 - Big Sur)<br>CybereasonAv (in macOS<br>version 11 - Big Sur and<br>later)|
|Sensor directories|/usr/local/cybereason/|


For machines running Linux







|Item|Exclusion|
|---|---|
|Sensor processes|cybereason-<br>activeconsole<br>cybereason-sensor<br>cbram|
|Sensor directories|/opt/cybereason/sensor|


Note


Cybereason recommends that on machines running

supported versions of Windows, you add the following


exclusions regardless of whether Windows Defender is

enabled or disabled. Adding these exclusions ensures that the


system is protected even if Anti-Malware is disabled or the

sensor fails to update Windows Defender.


For information about how to resolve conflicts between

[Cybereason sensors and third-party tools, see Troubleshooting](https://nest.cybereason.com/s/article/2125061)


[Conflicts between Third-Party Applications and Cybereason](https://nest.cybereason.com/s/article/2125061)

[(/s/article/2125061).](https://nest.cybereason.com/s/article/2125061)


## Open ports for sensor communication

On Windows machines, the following ports are used by Windows


sensors on the localhost for internal endpoint communication.

These ports cannot be used by third-party products while the


sensor is installed:


10556


10557

10560


30972

39378


40270

Ports in the range: 49152-65535

## Configure your firewall and network to
## allow sensor communication (all OSs)






|Proxy communication|If sensors will connect to<br>Cybereason servers via proxy<br>servers, you must also complete<br>these tasks:<br>Add the sensor connection on<br>the proxy servers to the allowlist.<br>If your organization uses a PAC<br>server, provide Customer<br>Success with its URL for the PAC<br>server.<br>If your organization uses an<br>HTTP proxy list, provide<br>Customer Success with the<br>hostname and port for each<br>proxy.<br>See Configure Proxy Connection<br>Details (/s/knowledge-base?<br>article=24-1-configure-proxy-<br>connection-<br>details&language=en_US#configure-<br>proxy-connection-details) for more<br>details.|
|---|---|
|Firewall and proxy<br>settings for Signatures<br>mode rule updates|See Firewall and Proxy Guidelines<br>for Signatures Updates<br>(/s/article/7215681)|



