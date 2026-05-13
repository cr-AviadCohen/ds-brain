5. The USB storage device is no longer visible under **This PC >**


**Devices and drives** . The end user receives a "USB device


was blocked" notification and cannot access the device.


Note


When the USB storage device is no longer visible in Windows,

you can view the device details in the **Investigation** screen


under the **Mount Point** element.

## Block FTP access


In this example, the **Personal firewall control** option is enabled,


and a custom rule is applied to block FTP access to a specific IP

address and port.


**To block FTP access, follow these steps:**


1. In the **System > Policies management** screen, create a new


policy or select your policy.

2. In your policy, navigate to the **Endpoint controls** screen.


3. In the **Endpoint controls** screen, set the **Personal firewall**

**control** toggle to **On** and selects all network profiles


( **Domains**, **Private Networks**, **Public Networks** ), and saves

the policy.


4. Creates a CSV file for outbound connections and creates a


rule that includes the following values:


Name: **Ftp denial example**

Group: **Cybereason**


Action: **Block**

Remote address: **66.220.9.50**


Protocol: **TCP**

Remote Port: **21**


Note


This set of fields defines a rule for all endpoints under this


policy. According to the rule, all outgoing FTP connection

attempts that use the TCP protocol to connect to the


66.220.9.50 IP address on port 21 are blocked.


5. Under **Upload custom rule list - outbound connections**,


clicks **Upload CSV** and select the file. The custom rules are

visible in a table, indicating that the rules have been uploaded


to Cybereason.


6. Accesses an endpoint to which you have assigned the policy


and verify that the rule exists in Windows Firewall, indicating


that the rule has been applied.


Note


The rule must also appear under **Monitoring > Firewall** .


Otherwise, the rule is not currently active. The problem
may occur if a mistake exists in the CSV file or if the


endpoint network profile does not match the rule (for

example, if the endpoint is on a public network and the


rule is defined for private and domain network profiles).



