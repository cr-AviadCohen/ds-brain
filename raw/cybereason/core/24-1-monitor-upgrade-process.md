|Status|Description|How to Resolve|Col4|
|---|---|---|---|
|A <1>-<br>installation<br>cannot be<br>installed on<br>a <2>-bit<br>Windows|The version of<br>the installer<br>package was not<br>appropriate for<br>the architecture<br>(32-bit vs. 64-bit)<br>of the machine<br>on which you<br>tried to upgrade<br>the sensor.|Ensure you have the correct<br>installation package for your<br>architecture. Contact your<br>Cybereason system admin to get the<br>correct version.||
|Failed to<br>verify<br>bundle's<br>certifcation|The machine on<br>which the sensor<br>is installed does<br>not have the<br>correct<br>certifcates.|Install the correct certifcates on the<br>machine. For details on the required<br>certifcates, see Required Certifcate<br>for Cybereason Sensor Installation<br>(/s/article/3140241).||
|Failed|General failure<br>(for example, the<br>upgrade failed)|No specifc action. Contact Support.||
|Failed<br>sending|May be a server<br>or connectivity<br>failure.|Resending the upgrade action may<br>solve the issue.||
|Failed<br>sending<br>installation<br>package|The system was<br>not able to send<br>the installation<br>package.|Try again, and contact Support if the<br>issue reoccurs.||
|In progress|The installation is<br>in progress|N/A||
|Failed to<br>verify the<br>required KB<br>updates are<br>installed on<br>this<br>machine|Indicates there<br>are missing KB<br>versions from<br>Windows<br>updates that are<br>not installed.|Install the required updates in<br>Windows Support for Trusted Signing<br>(https://support.microsoft.com/en-<br>us/topic/kb5022661-windows-<br>support-for-the-trusted-signing-<br>formerly-azure-code-signing-<br>program-4b505a31-fa1e-4ea6-85dd<br>6630229e8ef4).||
|||||


|Status|Description|How to Resolve|Col4|
|---|---|---|---|
|Insuffcient<br>build<br>number -<br>required:<br><1>, found<br><2>.|The version or<br>build for the<br>machine<br>operating system<br>is not a<br>supported<br>version.|Upgrade the operating system to a<br>supported version. For the full list of<br>supported operating systems, see<br>Supported OS Versions for the Sens<br>(/s/knowledge-base?article=24-1-<br>supported-os-versions-for-the-<br>sensor&language=en_US#supporte<br>os-versions-for-the-sensor).||
|Missing<br>package<br>from fle<br>system|This can occur<br>due to one of<br>these causes:<br>In<br>environments<br>using the<br>Scaled<br>Sensor<br>upgrade<br>feature, no<br>sensor<br>package is<br>detected on<br>the local fle<br>system.<br>The sensor<br>package is<br>incompatible.|Verify with Technical Support that the<br>Endpoint Management Channel<br>feature is enabled for your<br>Cybereason environment.||
|Already up<br>to date|Indicates that the<br>sensor is up-to-<br>date and does<br>not require<br>upgrade.|Verify that your frewall is<br>confgured to receive certifcate<br>updates.<br>Check if your sensor package<br>fles are signed with the Sectigo<br>Root certifcates to meet the<br>Microsoft Virus Initiative MVI<br>requirements. To learn more<br>about Sectigo certifcate<br>signatures, see Sensor Binaries<br>are Now Signed with Sectigo<br>Certifcates<br>(/announcements/sensor-<br>binaries-are-now-signed-sectigo<br>root-certifcates).||
|||||


|Status|Description|How to Resolve|Col4|
|---|---|---|---|
|New<br>package<br>downloaded|A new package<br>was downloaded<br>to the endpoint<br>and is waiting for<br>the upgrade<br>action.|Perform the upgrade action.||
|Package<br>signing<br>verifcation<br>failure|A certifcate is<br>missing on the<br>endpoint.|Ensure the required certifcates are<br>installed on the endpoint or contact<br>Support.||
|Succeeded|The sensor<br>upgrade process<br>succeeded.|No action required.||
|This<br>Windows<br>OS is<br>unidentifed.|The version or<br>build for the<br>machine<br>operating system<br>is not a<br>supported<br>version.|Upgrade the operating system to a<br>supported version. For the full list of<br>supported operating systems for the<br>sensor, see Supported OS Versions<br>for the Sensor (/s/knowledge-base?<br>article=24-1-supported-os-versions-<br>for-the-<br>sensor&language=en_US#supporte<br>os-versions-for-the-sensor).||
|Windows<br><version> is<br>not<br>supported.|The version or<br>build for the<br>machine<br>operating system<br>is not a<br>supported<br>version.|Upgrade the operating system to a<br>supported version. For the full list of<br>supported operating systems for the<br>sensor, see Supported OS Versions<br>for the Sensor (/s/knowledge-base?<br>article=24-1-supported-os-versions-<br>for-the-<br>sensor&language=en_US#supporte<br>os-versions-for-the-sensor).||
|Windows<br><1> is not<br>supported.|The version or<br>build for the<br>machine<br>operating system<br>is not a<br>supported<br>version.|Upgrade the operating system to a<br>supported version. For the full list of<br>supported operating systems for the<br>sensor, see Supported OS Versions<br>for the Sensor (/s/knowledge-base?<br>article=24-1-supported-os-versions-<br>for-the-<br>sensor&language=en_US#supporte<br>os-versions-for-the-sensor).||
|Uninstalled|The sensor was<br>uninstalled|N/A||
|||||


In addition, if you see error code 14 on the endpoint machine


where you are trying to upgrade the sensor, please check that you

[have implemented this procedure: Enable Communication with](https://nest.cybereason.com/s/knowledge-base?article=24-1-enable-communication-with-cybereason-servers&language=en_US#enable-communication-with-cybereason-servers)


[Cybereason Servers (/s/knowledge-base?article=24-1-enable-](https://nest.cybereason.com/s/knowledge-base?article=24-1-enable-communication-with-cybereason-servers&language=en_US#enable-communication-with-cybereason-servers)

[communication-with-cybereason-](https://nest.cybereason.com/s/knowledge-base?article=24-1-enable-communication-with-cybereason-servers&language=en_US#enable-communication-with-cybereason-servers)


[servers&language=en_US#enable-communication-with-](https://nest.cybereason.com/s/knowledge-base?article=24-1-enable-communication-with-cybereason-servers&language=en_US#enable-communication-with-cybereason-servers)

[cybereason-servers). If this procedure does not resolve the issue,](https://nest.cybereason.com/s/knowledge-base?article=24-1-enable-communication-with-cybereason-servers&language=en_US#enable-communication-with-cybereason-servers)


contact Cybereason Support. For details on GPRC error codes,

[see GRPC error codes](https://grpc.github.io/grpc/core/md_doc_statuscodes.html)


[(https://grpc.github.io/grpc/core/md_doc_statuscodes.html).](https://grpc.github.io/grpc/core/md_doc_statuscodes.html)





