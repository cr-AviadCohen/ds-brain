You can then analyze these threat detections just like any other


MalOp or investigation.


The Cybereason platform marks MalOps from mobile devices with


a special **Mitigated** label to show that the alert has been

addressed on the mobile device with relevant protection actions:


Depending on your threat policy configuration, the **Mitigated** label

works differently on a device for each threat:


If you selected **Block** as the response action, if a MalOp is

mitigated, Cybereason Mobile blocks the device's connection


to the malicious site.

If you selected **Secure** as the response action, if the MalOp is


mitigated, Cybereason Mobile creates a secure network for

the device that prevents malicious communication.


When you run an investigation query in the **Investigation** screen,

the query results return information from both Mobile and non

Mobile endpoints:


Mobile-specific detections contain mobile-relevant information,

such as the device information and device properties:


You can also use mobile-specific information in the **Investigation**


screen in a number of different Elements and Features, including:


In addition, Cybereason Mobile threats generate numerous


Evidences and Suspicions that you can use in your queries. Use

the search bar in the **Investigation** screen to locate mobile

related Evidences or Suspicions.

## View details on connected mobile devices


When a device has the Cybereason Mobile sensor installed, the


**System > Sensors** screen includes details on these mobile

devices.


Add the column for **Device Type** or **OS** to the **Sensors** screen

and you can view the details of the mobile devices:


When you view the device information, the FQDN for the device is


shown in the **FQDN** column. Cybereason recommends that you

update device information in your UEM/MDM platform as the


Cybereason platform takes the device information from your

UEM/MDM platform.


To integrate the information received from Cybereason Mobile

connected devices, the Cybereason platform includes a number


of MalOps related to mobile devices, including:
