The Cybereason platform does not support NTLM (v1 or v2)


proxy authentication.














|Proxy<br>type|Description|Supported<br>OS|
|---|---|---|
|List<br>(HTTP)|You can confgure a list of proxies,<br>defning IP and Port pairs, and add<br>this list when you install the sensor. If<br>you choose this option, the sensor<br>ignores all other host-based settings<br>for proxies and attempts to connect<br>using the proxies in the list. This<br>option is the least fexible approach<br>for proxy confguration management.<br>Note<br>The Cybereason platform<br>supports both HTTP and HTTPS<br>proxies. TCP forwarding proxies<br>can be supported when the<br>sensor is unaware of the proxy.|Windows,<br>Mac, Linux|
|PAC<br>fle|If the sensor is running on a host that<br>is confgured to use PAC fles to<br>determine proxy confguration, the<br>sensor leverages Windows APIs to<br>discover the address of the given<br>proxy.|Windows,<br>Mac|
|Auto-<br>Detect|In some cases, the sensors<br>automatically detect the proxy. For<br>Linux sensors, you must set up the<br>auto-detect proxy.||



You can define a proxy for the following connections:


Sensors to Registration server using sensor installation


parameters or personalization

Sensors to Detection servers using the Cybereason UI


The table below details each type of connection:


|Connection|Configuration method|How it works|
|---|---|---|
|Sensors to<br>Registration<br>server|Installation<br>parameters/personalization|Your<br>organization/Cybereason<br>can set an HTTP/PAC proxy<br>via installation<br>parameters/personalization<br>If you do not provide an<br>HTTP/PAC proxy, the<br>Cybereason platform uses<br>Auto-Detect or a direct<br>connection. For more<br>details, see Sensor to<br>Registration server.|
|Sensors to<br>Detection<br>server|Cybereason UI|The administrator selects<br>the proxy type. If no option<br>is selected, Auto-Detect is<br>used (default). For more<br>details, see Sensor to<br>Detection server.|
||||


If you want to configure the proxy connection settings at the


endpoint machine level, you can configure the sensor to use the

same proxy for the Registration server and the Detection server


(which overrides the settings in the **Detection servers** screen. For

Windows endpoints, this is done using the


**AP_DETECTION_PROXY_AS_SIGNON** parameter, see

[Supported sensor installation parameters (/s/knowledge-base?](https://nest.cybereason.com/s/knowledge-base?article=24-1-sensor-installation-parameters&language=en_US#supported-sensor-installation-parameters)


[article=24-1-sensor-installation-](https://nest.cybereason.com/s/knowledge-base?article=24-1-sensor-installation-parameters&language=en_US#supported-sensor-installation-parameters)

[parameters&language=en_US#supported-sensor-installation-](https://nest.cybereason.com/s/knowledge-base?article=24-1-sensor-installation-parameters&language=en_US#supported-sensor-installation-parameters)


[parameters). For macOS and Linux endpoints, contact Technical](https://nest.cybereason.com/s/knowledge-base?article=24-1-sensor-installation-parameters&language=en_US#supported-sensor-installation-parameters)

Support to use this option.

## configuration and precedence


This section describes how to configure the proxy connection and

the order of precedence for the different proxy communication


methods.

## Sensor to Registration server


[Your administrator can set an HTTP/PAC proxy via Supported](https://nest.cybereason.com/s/knowledge-base?article=24-1-sensor-installation-parameters&language=en_US#supported-sensor-installation-parameters)


[sensor installation parameters (/s/knowledge-base?article=24-1-](https://nest.cybereason.com/s/knowledge-base?article=24-1-sensor-installation-parameters&language=en_US#supported-sensor-installation-parameters)

[sensor-installation-parameters&language=en_US#supported-](https://nest.cybereason.com/s/knowledge-base?article=24-1-sensor-installation-parameters&language=en_US#supported-sensor-installation-parameters)


[sensor-installation-parameters) for each endpoint, or Cybereason](https://nest.cybereason.com/s/knowledge-base?article=24-1-sensor-installation-parameters&language=en_US#supported-sensor-installation-parameters)

Technical Support can assist you to set these parameters as part


of your sensor installation package (personalization).


1. If you provide a manual proxy or proxy list, the Cybereason


platform applies the manual proxy list. You can provide a

single PAC proxy or an HTTP proxy list. The PAC proxy


configuration script takes precedence over an HTTP proxy list.


Note


The Cybereason platform supports HTTP proxy lists on

Linux endpoints, but does not support PAC proxy


configuration scripts.


2. If your administrator does not provide a manual proxy list, the


Cybereason platform uses Auto-Detect for proxies. This is the

default option.


If Auto-Detect is used, sensors automatically detect proxy
configurations in a predefined order:


The sensor automatically detects settings
Use automatic configuration script (PAC) (not supported


on Linux machines)

Use a proxy server for your LAN


3. If the sensor does not detect a proxy, the sensor connects


directly to the server without a proxy.


## Sensor to Detection server

You configure proxy connections from the sensor to the Detection


server via the **System > Detection servers** screen.


Note


On Windows endpoints, if a system user defines a PAC proxy

on the endpoint machine as part of a group policy setting, the


sensor automatically detects the PAC proxy, even if you did
not define a proxy or did not select Auto-Detect mode in the


**Detection servers** screen. If an individual user defines a PAC

proxy on the endpoint machine, the sensor does not detect


the PAC proxy.


The Cybereason platform uses the method that the user selects


(there is no order of precedence):


**Auto Detect**


**PAC proxy configuration script**


Note


PAC proxy configuration scripts are not supported on

Linux endpoints. If an administrator selects the **PAC**


**server** option, Linux sensors connect directly to the

server.


**Proxy list** (HTTP proxies)


If you want to set proxy configuration details on the endpoint


machine level, you can configure the sensor to use the same

proxy for the Registration server and the Detection server (which


overrides the settings in the **Detection servers** screen. For

Windows endpoints, this is done using the


**AP_DETECTION_PROXY_AS_SIGNON** parameter, see

[Supported sensor installation parameters (/s/knowledge-base?](https://nest.cybereason.com/s/knowledge-base?article=24-1-sensor-installation-parameters&language=en_US#supported-sensor-installation-parameters)


[article=24-1-sensor-installation-](https://nest.cybereason.com/s/knowledge-base?article=24-1-sensor-installation-parameters&language=en_US#supported-sensor-installation-parameters)

[parameters&language=en_US#supported-sensor-installation-](https://nest.cybereason.com/s/knowledge-base?article=24-1-sensor-installation-parameters&language=en_US#supported-sensor-installation-parameters)


[parameters). For Mac and Linux endpoints, contact Technical](https://nest.cybereason.com/s/knowledge-base?article=24-1-sensor-installation-parameters&language=en_US#supported-sensor-installation-parameters)

Support to use this option.

## Add a proxy connection on Linux

## machines using automatic detection


Sensors on Linux machines detect if there is a proxy defined on
the machine. If you do not provide a manual proxy list or define a


proxy list via the **Detection servers** screen, the sensor uses the

Auto-Detect proxy to automatically detect if a proxy environment


variable (https_proxy) is defined, and connects to the

Registration/Detection servers via the proxy.


To ensure that the Auto-Detect proxy is used, you need to set up


the proxy for Linux machines before the sensor installation.


Note


Proxy creation is not done as part of the command line

installation for the sensor installation.


You can set up an Auto-Detect proxy in one of the following ways:


Set up a Linux proxy at the operating system level: This proxy


will apply to the entire OS and may be affected by other

applications or services running on the machine.


Set up a Linux proxy at the sensor level: This proxy will apply

to the sensor only and will not be affected by general


operating system settings. This method is useful when you are

managing multiple application requirements and you do not


want network settings and other general settings to override
the sensor proxy configuration.


Set up a Linux proxy at the sensor level for Linux AV support:

This proxy will enable Linux AV to communicate with the


necessary components for signature updates.

## Set up a Linux proxy at the operating

## system level


To define a proxy at the operating system level, follow these steps:


1. On the Linux machine add the following command to

/etc/profile file:

```
   export https_proxy=<proxy URL>

```

Here are some examples of valid commands:

```
   export

   https_proxy=http://company_proxy:8080

   (http://company_proxy:8080)

   export https_proxy=company_proxy:8080

   export https_proxy=1.2.3.4:8080

   export

   https_proxy=http://company_proxy:1234

   (http://company_proxy:1234) #Some

   comment

```

The command must appear in the **/etc/profile** file or in a file
that is loaded by the /etc/profile file.


2. Under the **/etc/profile.d/**, create a **.sh** file (for example,


**[proxy.sh (https://proxy.sh)](https://proxy.sh/)** ) with the relevant export

command.


3. To load your new proxy configuration, run this command:

```
   sudo source /etc/profile // load the

   updated profile with the export proxy

   command

```

4. If you added the proxy export command after the sensor was


installed, run this command:

```
   sudo service cybereason-sensor

   restart // restart the sensor

```

Cybereason recommends you also restart the machine to ensure
the configuration updates.


Note


If the sensor has been configured using a personalized


installer file to connect directly to the Registration/Detection
servers or to connect to a different proxy, this configuration


overrides a proxy detected using the method described
above. To change the configuration, consult Technical


Support.

## Set up a Linux proxy at the sensor level


When you configure a proxy at the sensor level, the machine uses


the settings in the **cybereason-sensor** configuration file relevant

to the service running the sensor.


Note


[For CentOS 6 machines, follow this procedure](https://nest.cybereason.com/s/article/7910446)


[(/s/article/7910446) instead of the steps below.](https://nest.cybereason.com/s/article/7910446)


**To set up the proxy, follow these steps:**


1. On the Linux machine running the sensor, to edit the

**cybereason-sensor** configuration file, run the following


command:

```
   sudo systemctl edit cybereason-sensor

```


