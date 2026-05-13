You can also manage forensic data ingestion tools with the


Cybereason platform's main console. For details on how to

use **IR Tools** [screen to manage these tools, see Manage](https://nest.cybereason.com/s/knowledge-base?article=24-1-manage-incident-response-and-forensic-data-ingestion-tools-with-the-platform&language=en_US#manage-incident-response-and-forensic-data-ingestion-tools-with-the-platform)


[Incident Response and Forensic Data Ingestion Tools with the](https://nest.cybereason.com/s/knowledge-base?article=24-1-manage-incident-response-and-forensic-data-ingestion-tools-with-the-platform&language=en_US#manage-incident-response-and-forensic-data-ingestion-tools-with-the-platform)

[Platform (/s/knowledge-base?article=24-1-manage-incident-](https://nest.cybereason.com/s/knowledge-base?article=24-1-manage-incident-response-and-forensic-data-ingestion-tools-with-the-platform&language=en_US#manage-incident-response-and-forensic-data-ingestion-tools-with-the-platform)


[response-and-forensic-data-ingestion-tools-with-the-](https://nest.cybereason.com/s/knowledge-base?article=24-1-manage-incident-response-and-forensic-data-ingestion-tools-with-the-platform&language=en_US#manage-incident-response-and-forensic-data-ingestion-tools-with-the-platform)

[platform&language=en_US#manage-incident-response-and-](https://nest.cybereason.com/s/knowledge-base?article=24-1-manage-incident-response-and-forensic-data-ingestion-tools-with-the-platform&language=en_US#manage-incident-response-and-forensic-data-ingestion-tools-with-the-platform)


[forensic-data-ingestion-tools-with-the-platform).](https://nest.cybereason.com/s/knowledge-base?article=24-1-manage-incident-response-and-forensic-data-ingestion-tools-with-the-platform&language=en_US#manage-incident-response-and-forensic-data-ingestion-tools-with-the-platform)


In this topic:


Enable the DFIR package

Before you begin


Deploy a forensic data ingestion tool

Run a forensic data ingestion tool


Evaluate collected forensic data

Remove a forensic data ingestion tool

## Enable the DFIR package


If you do not use an Express IR environment as a Cybereason IR

partner, you can purchase and enable the DFIR package in your


environment.


Note


To enable the DFIR package, you must upgrade your

environment. You cannot enable the DFIR package on an


existing version without a version upgrade.


[Open a Technical Support (/s/support) to upgrade your](https://nest.cybereason.com/s/support)


environment and add the DFIR package to your environment. As

part of the DFIR package enablement, incident response tool


management features are also enabled for your environment.


Because the ability to collect forensics data through the


Cybereason platform uses the platform's incident response

management infrastructure, many of the initial steps required are


the same as the incident response tool management process,

including:


Deploy Cybereason sensors

Create a Responder L2 user


Log in to the platform


[For details on these steps, see Manage Incident Response Tools](https://nest.cybereason.com/s/knowledge-base?article=24-1-manage-incident-response-tools-with-the-api&language=en_US#manage-incident-response-tools-with-the-api)


[with the API (/s/knowledge-base?article=24-1-manage-incident-](https://nest.cybereason.com/s/knowledge-base?article=24-1-manage-incident-response-tools-with-the-api&language=en_US#manage-incident-response-tools-with-the-api)

[response-tools-with-the-api&language=en_US#manage-incident-](https://nest.cybereason.com/s/knowledge-base?article=24-1-manage-incident-response-tools-with-the-api&language=en_US#manage-incident-response-tools-with-the-api)


[response-tools-with-the-api).](https://nest.cybereason.com/s/knowledge-base?article=24-1-manage-incident-response-tools-with-the-api&language=en_US#manage-incident-response-tools-with-the-api)


## Deploy a forensic data ingestion tool

When you enable forensic data ingestion, the supported forensics


data ingestion packages files are added to your environment. You

only need to deploy these tools to the necessary machines.


**To deploy a forensic data ingestion tool, follow these steps:**


1. In your REST API client or script, create a request to get the


list of supported forensic data ingestion packages files. For

[details on the API endpoint to retrieve this list, see the Retrieve](https://nest.cybereason.com/s/knowledge-base?article=incident-response-api-token-retrieve-a-list-of-supported-forensics-ingestion-tools)


[the List of Supported Forensic Data Ingestion Tools](https://nest.cybereason.com/s/knowledge-base?article=incident-response-api-token-retrieve-a-list-of-supported-forensics-ingestion-tools)

[(/s/knowledge-base?article=incident-response-api-token-](https://nest.cybereason.com/s/knowledge-base?article=incident-response-api-token-retrieve-a-list-of-supported-forensics-ingestion-tools)


[retrieve-a-list-of-supported-forensics-ingestion-tools) topic in](https://nest.cybereason.com/s/knowledge-base?article=incident-response-api-token-retrieve-a-list-of-supported-forensics-ingestion-tools)

the API documentation.


2. In your REST API client or script, create and run the request to


deploy the tool. The name of the package should be one of


the names returned in the list of supported packages files.


For details on the API endpoint to deploy a forensics data


[ingestion tool, see the Deploy a Forensic Data Ingestion Tool](https://nest.cybereason.com/s/knowledge-base?article=incident-response-api-token-deploy-a-forensics-data-ingestion-tool)

[(/s/knowledge-base?article=incident-response-api-token-](https://nest.cybereason.com/s/knowledge-base?article=incident-response-api-token-deploy-a-forensics-data-ingestion-tool)


[deploy-a-forensics-data-ingestion-tool) topic.](https://nest.cybereason.com/s/knowledge-base?article=incident-response-api-token-deploy-a-forensics-data-ingestion-tool)


During the deployment, you can track the progress using the


[Monitor Deployment of Forensic Data Ingestion Tools](https://nest.cybereason.com/s/knowledge-base?article=incident-response-api-token-monitor-deployment-of-forensic-data-ingestion-tools)

[Deployment (/s/knowledge-base?article=incident-response-](https://nest.cybereason.com/s/knowledge-base?article=incident-response-api-token-monitor-deployment-of-forensic-data-ingestion-tools)


[api-token-monitor-deployment-of-forensic-data-ingestion-](https://nest.cybereason.com/s/knowledge-base?article=incident-response-api-token-monitor-deployment-of-forensic-data-ingestion-tools)

[tools) API endpoint.](https://nest.cybereason.com/s/knowledge-base?article=incident-response-api-token-monitor-deployment-of-forensic-data-ingestion-tools)

## Run a forensic data ingestion tool


Once you deploy the tool to the appropriate machines, you can

run the tool on selected machines.


**To run a forensic data ingestion tool on a machine, follow**

**these steps:**


1. In your REST API client or script, create the request to run the


forensic data ingestion tools. For details on using the API


[endpoint to run the tools, see the Run a Forensic Data](https://nest.cybereason.com/s/knowledge-base?article=incident-response-api-token-run-a-forensic-data-ingestion-tool)

[Ingestion Tool (/s/knowledge-base?article=incident-response-](https://nest.cybereason.com/s/knowledge-base?article=incident-response-api-token-run-a-forensic-data-ingestion-tool)


[api-token-run-a-forensic-data-ingestion-tool) topic in the API](https://nest.cybereason.com/s/knowledge-base?article=incident-response-api-token-run-a-forensic-data-ingestion-tool)

documentation.


In your API request body, ensure that you run the tool on a
specific sensor or a filtered group of sensors, but not both.


Specifying a specific sensor and a filtered group of sensors

will cause the request to fail.


You do not need to specify any run commands, queries, or

output locations for the forensic tools. The tools you receive


with your environment contain the required queries and

settings to perform forensic ingestion from machines and then


send this data directly to the Cybereason platform.


2. Run the request or script using your REST API client or


automation framework.


You may only need to run the standard forensic data ingestion tool


request one time. This initial request collects data on operations

on the machine prior to the installation of the Cybereason sensor.


However, after the Cybereason sensor is installed (which is

required for forensic tool deployment and execution), the same


information collected by the forensic ingestion tool is also

collected by the Cybereason sensor.


If you run the forensic data ingestion tool again, you may end up

with duplicate data that displays differently in the **Investigation**


screen. For example, the same information may appear as part of

the **Process** Element if the sensor collects the information and as


part of the **Forensic Artifacts** Element if the forensic data

ingestion tool collects the data. However, any data collected by


the forensic data ingestion tool is not duplicated in the **Forensic**

**Artifacts** Element if you run the forensic data ingestion tool more


than one time.


The response for the request to run a forensic data ingestion tool


contains a batch number which indicates the successful initiation

of the tool on selected endpoints. In order to monitor the execution


[status on endpoints, see the Monitor Forensic Data Ingestion Tool](https://nest.cybereason.com/s/knowledge-base?article=incident-response-api-token-monitor-forensic-data-ingestion-tool-execution)

[Execution (/s/knowledge-base?article=incident-response-api-](https://nest.cybereason.com/s/knowledge-base?article=incident-response-api-token-monitor-forensic-data-ingestion-tool-execution)


[token-monitor-forensic-data-ingestion-tool-execution) reference](https://nest.cybereason.com/s/knowledge-base?article=incident-response-api-token-monitor-forensic-data-ingestion-tool-execution)

topic in the API documentation.

## Evaluate collected forensic data


Upon the completion of a forensic tool execution run, the collected

data is sent to your Cybereason platform's detection servers,


where it is integrated with existing data from other sources. The

platform's CMC engine evaluates and correlates the forensic data


with all other data.


You can view data from forensic sources in a number of places:


The **Forensic Artifacts** Element enables you to build queries
to find specific forensic information:


For details on the **Forensic Artifacts** [Element, see the Query](https://nest.cybereason.com/s/knowledge-base?article=query-api-token-query-elements-and-features-version-232148-and-later)


[Elements and Features (/s/knowledge-base?article=query-](https://nest.cybereason.com/s/knowledge-base?article=query-api-token-query-elements-and-features-version-232148-and-later)

[api-token-query-elements-and-features-version-232148-and-](https://nest.cybereason.com/s/knowledge-base?article=query-api-token-query-elements-and-features-version-232148-and-later)


[later) topic.](https://nest.cybereason.com/s/knowledge-base?article=query-api-token-query-elements-and-features-version-232148-and-later)



