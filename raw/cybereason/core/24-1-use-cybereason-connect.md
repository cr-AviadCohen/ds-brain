forward them to your Cybereason platform.

## Integration classification


In the **Connect** screen, all supported integrations are grouped

into categories that represent the integration's purpose.


Categories include:


Identity and Access Management

Workspace


Email and Workspace Protection

Email Server


Firewall

IDS/IPS


SaaS Application

SIEM


Workflow and Response

Enrichment and Telemetry


Infrastructure

Cyber Posture


Security Analytics


You will see additional categories as the Cybereason platform


adds support for additional integrations.


In addition, each integration has a specific function to describe


how Cybereason XDR uses the data from the integration.

Functions include:














|Detection|Retrieves third-party events and security<br>alerts and utilizes them for Malop detection.|
|---|---|
|**Context data**|Enriches already collected information<br>through the correlation of collected data<br>from XDR integrations with EDR data.|
|**Investigation**|Retrieves third-party events and utilizes<br>them for powerful graph query<br>investigations.|
|**Response**|Automatically executes response actions<br>through third-party vendors APIs.|
|**Analytics**|Analyzes and reports trends in behavior.|
|**Orchestration**|Helps manage and automate your security<br>workfows.|
|**Attack**<br>**Simulation**|Enables you to run simulated attacks safely<br>to test your protection levels.|
|**Management**|Helps you manage all your security assets<br>effciently.|



Likewise, you will see additional functions as the Cybereason


platform adds support for additional integrations.


## Filter the list of integrations

By default, when you open the **Cybereason Connect** screen, you


see all available integrations. To find the integration you need, you

have a number of different options to narrow down the list.


In the **All Integrations** tab, in the search bar at the top of the

screen, enter any of the parts of the product name, such as


Google for the Google Workspace, Google Gmail, or Google

Alerts Center integration:


In addition, next to the search bar, click the **Filter** icon to display
types of filter categories:


You can use this filter list to filter by integration category, product


vendor, or integration function. As you select a specific filter, the

**Cybereason Connect** screen updates the displayed integrations


to match your filter. For example, if you select **Workspace** as a
filter, the screen displays all integrations with the category label of


**Workspace** :

## Add a cloud feed integration to your


[For details, see Add a Cloud Feed Integration (/s/knowledge-](https://nest.cybereason.com/s/knowledge-base?article=24-1-add-a-cloud-feed-integration&language=en_US#add-a-cloud-feed-integration)

[base?article=24-1-add-a-cloud-feed-](https://nest.cybereason.com/s/knowledge-base?article=24-1-add-a-cloud-feed-integration&language=en_US#add-a-cloud-feed-integration)


[integration&language=en_US#add-a-cloud-feed-integration).](https://nest.cybereason.com/s/knowledge-base?article=24-1-add-a-cloud-feed-integration&language=en_US#add-a-cloud-feed-integration)

## Add an on-site integration to your


[For details, see Add an On-Site Integration (/s/knowledge-base?](https://nest.cybereason.com/s/knowledge-base?article=24-1-add-an-on-site-integration&language=en_US#add-an-on-site-integration)


[article=24-1-add-an-on-site-integration&language=en_US#add-](https://nest.cybereason.com/s/knowledge-base?article=24-1-add-an-on-site-integration&language=en_US#add-an-on-site-integration)

[an-on-site-integration).](https://nest.cybereason.com/s/knowledge-base?article=24-1-add-an-on-site-integration&language=en_US#add-an-on-site-integration)

## View your integrations


After you add and configure a specific integration, the

**Cybereason Connect** screen displays the integrations in the **My**


**Integrations** tab, along with the status of each integration:


If your integration displays **ERROR**, you may have a problem with


the incorrect credentials or insufficient permissions. Check the

following to help resolve the error:


1. Verify you entered the correct credentials, such as the


integration host name, tenant ID, application key, secret token,


password, and so forth.


2. Verify that the provided application or user for the integration


has the right permissions. You can find the appropriate
configuration documentation for each integration on the


[Cybereason Integrations (/s/integrations) page.](https://nest.cybereason.com/s/integrations)


If you remove any of your integrations, all log source data


collected and received is retained by your Cybereason platform

according to your data retention package.





