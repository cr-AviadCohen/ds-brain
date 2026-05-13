Likewise, the Logon Session Element is correlated with multiple


**Processes** that are executed in the context of the session:


The Process Element is a core Element in the Cybereason data

model as this is the object that is using the processing power of


the system to perform activities.


The Process Element has numerous connections to other


Elements:


The **Process** Element is directly correlated to the **Machine**


Element on which it was executed and with the **User** Element

that executed the process.


The **Process** Element is also correlated with the executable

**File** Element that was used to execute the process.


The **Module** Element is also correlated with the **File** Element,

which connects to the file that holds the code that the module


loaded.


From the **Process** Element, the data model adds connections for

network activity:


The **Process** Element displays the process **connections** with

a link to the **Connection** Element, which are correlated to the


**IP Address** Element.

The **Process** element also connects to the **DNS** request


Elements which correlate to the source **Domain** Element and

the target **IP Address** Element.


The CMC Engine adds links and correlations to automatic

executions of processes, correlating the **Service** Element with the


**Process** Element that executed the service, **Scheduled Task**

Elements with the **Process** Element that executed the task, and


**Registry Entry** Elements with **File** Elements.


Other activities related to the **Process** Element include the


creation, modification, and deletion of files, which are represented
by the **File Event** Element. If the file activity is performed on a file


on which the CMC Engine has information, the Engine correlates

the activity to the relevant **File** Element:


It is important to note that while an activity is happening on a


single machine, the CMC Engine correlates activities between

different machines using cross organization elements such as


Users, IP Addresses, and Domains.


The following graphic shows a model of the central Elements of


the platform related to endpoint data:


This model reflects the reality of what happens on your endpoint


machines. For example, a User logs onto a Machine via a Logon

Session, opens a program (Process) from an .exe File which then


loads a .dll Module to open the application.

## View correlations of endpoint data


By correlating these Elements, you receive a more complete


snapshot of what is or has happened on your endpoints. This

enables you to:


View context on any given component. For example, when

you view details on a Process, you receive information not


only about the process, but about Files associated with the

process, the Service that runs the process, the Module that


loaded the process, Connections that the process makes, and

so forth.


When you hunt or investigate, you can drill down into

additional information. For example, your investigation or hunt


results may be grouped by the name of the process. However,
if your goal was to find malicious connections associated with


the process, the results enable you to see this information

without having to cross-reference different sets of data.


Because the platform CMC Engine does the analysis, you can


spend your time analyzing the pattern of behavior or planning

queries to hunt for previously undiscovered malicious behavior.

## Use the data model to create queries


Once you understand how Elements are related, you can create

queries that utilize these connections.


For example, with an understanding of the data model and the

correlations between Elements, you can answer a question like


this: **What are the processes that are connecting to addresses**

**used by malicious processes, but that are not malicious**


**themselves?**


Using a couple of queries and analyzing the results, you can find


processes such as this. From a security point of view, you can

assume that a certain amount of malicious processes are making


connections to malicious addresses. The queries you create help

you have visibility into all the processes that access the same


address to ensure that these other processes are legitimate or not.


To start, you use the links from the **Process** Element. To find the


process's connections, you have to look for the connections of a
process. As a result, the first step in the query is to add the


**Process** and **Connection** Elements:


In addition, you need to view the addresses of these connections


in the results. Therefore, you need to link the **Connection** Element

to the **Remote Address** Element (which is an **IP Address** Element


in the data model).


Using this query until this point, you have found the remote

addresses of connections from all processes. However, the


fundamental question of this query is looking at the connections of

malicious processes. Therefore, before you go further, you want to


add a filter on the **Process** Element to filter for processes
classified as malicious:


Your query will now return results for any process detected as


malicious, showing the remote IP address of connections this

process makes.


However - to answer the question - which focuses on what _other_

processes are accessing these addresses, you have to build the


query further.


To do so, you can connect the **Remote address** Element to the


**Connection (Local address)** Element. This enables you to see

the connections to this remote address.


Then, you want to see what processes are accessing this

Connection to the Remote address. Therefore, you can connect


the final **Connection (Local address)** Element to the **Owner**

**process** Element:


As a final step, you need to filter the final Element (the **Owner**

**process** ) to see processes that are not malicious.


This query will return results that contain a list of processes that

are not malicious, but that connect to a remote address that is


accessed by processes that are malicious.


Using traditional tools and databases, combining and analyzing


the results would take you more than two days. However, using

the Cybereason data model and the strength of the correlations


used by the CMC Engine, you have results within minutes.

Understanding this structure can be very useful to create


sophisticated queries to hunt and analyze the query results in you

organization's environment.



