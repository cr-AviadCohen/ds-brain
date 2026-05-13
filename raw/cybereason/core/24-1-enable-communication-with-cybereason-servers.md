|Method|Details|
|---|---|
|One-<br>way<br>TLS|By default, new Cybereason deployments are<br>confgured with one-way TLS with a Cybereason<br>server certifcate that verifes the secure connection<br>from your Cybereason server. As part of the TLS<br>communication, the Cybereason sensor obtains the<br>GeoTrust RSA CA 2018 Intermediate CA directly<br>from the Detection server.<br>For details on the One-way TLS certifcate<br>requirements, see Required Certifcates for<br>Cybereason Sensor Installation (/s/article/3140241).|


|Method|Details|
|---|---|
|Two-<br>way<br>TLS|You can request Two-Way TLS communication<br>between Cybereason sensors and servers. In this<br>case, Cybereason provides a sensor installer<br>packaged with a client certifcate (in addition to the<br>server certifcate), enabling bi-directional secure<br>communication between the server and sensor.<br>Two-way TLS communication can use any of the<br>following settings:<br>**NEED:** If the sensor sends a certifcate, the<br>server checks it. If there's a match, the server<br>accepts the connection, otherwise it refuses<br>the connection. If the sensor doesn't send a<br>certifcate, the server refuses the connection.<br>**WANT:** (default) If the sensor sends a<br>certifcate, the server checks it. If there's a<br>match, the server accepts the connection,<br>otherwise it refuses the connection. If the<br>sensor doesn't send a certifcate, the server<br>accepts the connection.<br>**DISABLED:** The server doesn't check for a<br>certifcate. Even if the sensor sends a<br>certifcate, the server doesn't check it and<br>accepts the connection.<br>To change the default setting, open a Technical<br>Support (/s/support) case.<br>In most cases, Cybereason installs certifcates with<br>the Cybereason CA. If Cybereason installs the<br>Cybereason CA, there are no additional<br>requirements for you to use Two-Way TLS.<br>If your organization uses intermediate hardware,<br>such as a proxy or a web application frewall<br>(WAF), make sure that the hardware does not alter<br>the installed certifcates. If the proxy/WAF<br>communication alters the installed certifcates, you<br>must ensure that the proxy contains the required,<br>original (unaltered) certifcate. In addition, for<br>networks with intermediate hardware, you also<br>need to retrieve a dedicated sensor for two-way<br>TLS. For more information, contact Customer<br>Success.<br>For a list of required certifcates for Two-Way TLS,<br>see Required Certifcates for Cybereason Sensor<br>Installation (/s/article/3140241).<br>Note|


|Method|Details|
|---|---|
||Ensure that Cybereason traffc is allowed if<br>TLS/SSL certifcate breaking technology is<br>used. Any TLS/SSL certifcate breaking<br>technology will interrupt the service, for<br>example, HTTPS inspection or non-transparent<br>proxies.|

## Configure your network settings for

## platform communication

To enable machines on your network to communicate with the


Cybereason platform, you must add a number of configurations.


**To configure your network settings, follow these steps:**


1. On your firewall, allow communication with *.cybereason.net


using the **Web Interface** and **Sensor communication** ports


you requested in the Deployment questionnaire (443 or 8443).

2. If your environment has enabled Endpoint Management


Channel (which enables automated sensor updates and
communication), on your firewall, allow outbound


communication with the relevant URL listed in the following

table to enable sensor package delivery:






|Region|URL|Notes|
|---|---|---|
|USA|https://data-<br>epgw.cybereason.net/<br>(https://data-<br>epgw.cybereason.net/)||
|EMEA|https://data-epgw-eu-west-<br>1.cybereason.net/<br>(https://data-epgw-eu-west-<br>1.cybereason.net/)||
|APAC|https://data-epgw-asia-<br>northeast-<br>1.cybereason.net/<br>(https://data-epgw-asia-<br>northeast-<br>1.cybereason.net/)||


|Region|URL|Notes|
|---|---|---|
|Global|https://probe-dist-<br>dns.cybereason.net/<br>(https://probe-dist-<br>dns.cybereason.net/)|Required if you<br>have the<br>Authenticated<br>URL feature<br>enabled.<br>You must add<br>this URL in<br>addition to the<br>region specifc<br>URL for your<br>region.|







