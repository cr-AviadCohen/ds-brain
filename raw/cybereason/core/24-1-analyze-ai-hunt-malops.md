3. Below the MalOp root cause name, read the description to


learn a little more about why the Cybereason platform created

the MalOp.


4. In the main part of the MalOp details, you can see a map of


the associated items for the MalOp.


In the example details above, you can see the platform has


indicated:


The main process for the MalOp


The attack stage ( **Infection** ) exhibited by this MalOp

The host process ( **svchost.exe** ) for the process that led


to the creation of this MalOp

Affected machines and affected users associated with


this MalOp

In addition, if there were modules, connections, or other


Elements associated with the MalOp, you would find them in

this area.


5. Below the MalOp item summary diagram tree, view the


timeline for the activities associated with the MalOp.


Because AI Hunting MalOps do not reflect a single event, but


rather a pattern of behavior, the MalOp details provide you a

view of the chain of events that led to or contributed to this


particular MalOp.


Understanding the timeline helps you also see the length of


time that these behaviors have occurred in your environment.


6. Lastly, below the timeline, view the suspicions that led to the


MalOp creation. You should view these to understand what

other behaviors are occurring in your environment which led to


the larger attack pattern represented in the MalOp.


If a suspicion in the MalOp is of particular interest to you, you


can note the suspicion name and use this as a filter to run

queries in the **Investigation** screen later.

## Analyze process information


In the **Malop details**, the Cybereason platform reports a variety of
process-related information about the process identified as the


root cause of the MalOp. Use these details to understand exactly

what the process has done in your environment.


1. In the **Malop details**, navigate or scroll down to the **Process**


tab.


2. In the main part of the Process details section, view the


associated Elements for the root cause process.


In this example, you see the following:


The name of the machine on which the process ran

The name of the parent process of this process


Although this example does not display data for the process,

you may also see information on modules related to the


process, connections opened by the processes, and child

processes of this process.


3. Below the associated Elements diagram for the process, find


the collected process details.


In these details, you can view the following:


The file associated with the process

Total time the process ran


The start and end times for the process

File reputation and signature details (not pictured)


File hash for the process image file (not pictured)

Company name and product name for the process image


file (not pictured)

4. In the process details, also view the command line. The


command line for a process can often be a good indicator of

malicious activity since attackers may use processes, such as


legitimate OS processes, to run malicious commands.

Analyzing the command line will help you spot the use of


malicious commands.


5. If possible, look at the process type and product type for the


process. Finding that the process is an OS process or a third
party process may help you understand the process's


behavior better.

6. Below the process properties, view the behaviors the


Cybereason platform has highlighted for this process as well

as any suspicions and evidence the Cybereason platform


generated for this process.


For example, you may want to look to see if the process is


using persistence mechanisms such as registry entries,

scheduled tasks, services, and child processes. Likewise, you


may want to see if the process has a suspicious parent

process or it is an injected process.


In addition, the suspicions and evidence may be a powerful

indicator of the true nature of the process, even if the other


properties you viewed already seem to indicate that the

process is benign.


7. To the right of the process details, in the **Process profiles**,


select the process and click **Investigate** . The Cybereason


platform automatically builds the relevant investigation query

and runs the query.


8. In the **Investigation** screen, open the query result and view


the properties to view the properties and evaluate that they


seem legitimate to you.


For example, in the details above, the process details show

some suspicious activity, as the process claims to be a


Microsoft process, but it is not signed by Microsoft. In

addition, the process in the example above is running from a


temporary folder and has an unknown reputation.


In addition, for processes of interest, you should view the Attack


Tree to see parent and child process and to understand the chain

of activity happening in this MalOp. For each process, you could


also view many of the same properties and details from the Attack

Tree that you view in the Malop Details analysis.

## Analyze file information


In the **Malop details** screen, the Cybereason platform includes


some details on files. However, you can quickly find additional

details from the MalOp details screen.


1. In the **Malop Details** screen, navigate to the **Process** tab.


2. In the **Process** tab, to the left of the process details, locate


the **Process profile** section and expand the list of processes.
3. Select the process about which you want investigate file


details, and click the **Investigate** button.


The Cybereason platform builds and runs the relevant query

in the **Investigation** screen for the process


4. Open the results for the query.


5. In the Element Details screen, find the **File** section.


6. Click on the name of the image file.


7. In the expanded list of files, select the file about which to view


properties, and select **View Element** .


8. In the Element Details view that opens, view the file properties.


9. View the file properties, including:


Process names and IDs running from this file
Creation and end times for the file


Command line information used by the process from the
file


File extension type
Path to the file


Signature details for the file

Product names and types, and company names for the


file.
10. Investigate whether the file is signed and by whom.


Unexpected details from the signature information is often a

sign of malicious behavior.


In the example above, you can see the file is not signed, nor
is the signature verified.


11. View the file reputation to see the classification.


For those MalOps in which the process or logon session identified


as the root cause included connections to other networks, the

MalOp Ddtails include connection and communication information.


1. In the MalOp Details, navigate to the **Communication** tab.


Note


If there are no connections made by the process or logon

session, the **Communication** tab is not included in the


MalOp details.


2. In the main part of the **Communications** tab, view the


associated items for the main communications, including:


Machines and users involved in the communication


Processes which opened connection

Ports used in the connection


3. In the associated items diagram, look to see if there are any


connections, and whether those connections are internal or


external connections, as well as outgoing or incoming

connections


4. Also in the associated items diagram, in particular, note if


there is a listening connection as well as DNS requests


associated with the connection.


You can expand the list of these items if they exist and


investigate further if needed.

5. Below the associated items diagram for the MalOp


communications, view the communication details.


6. In the connection details, look for how long the connections


happened in the **Total time** field (not pictured in the example).
7. Next to the **Total time** field, look at the transmitted data


information.


8. Analyze the port being used by the connections.


9. Next to the connection details, locate the **Communication**


**profile** section.


10. Expand the list of connections and select the connection to


investigate.


11. Below the list of connections, click **Investigate** . The


Cybereason platform automatically creates a relevant query


and runs the query, and then opens the results.


12. In the Element Details screen, view the connection details and


analyze whether there are expected.


In this example, you can see potentially suspicious activity for


the connection since the connection uses port 4444, which is

the default port for the Meterpreter agent. In addition, you can


see the machines in the connection are definitely transferring

data.

## Analyze module information


In addition, the Cybereason platform enables you to see module
related information for processes in a MalOp. This module


information is not displayed in the MalOp details but is quick to
find.


1. In the MalOp details, open the **Process** tab.


2. In the associated items diagram, view the details on


associated modules.


3. Click on the module name or count of modules to display a list


of all modules.


4. Below the list of modules, select **View all elements** .


The Cybereason platform creates a relevant query and runs


the query.


5. From the list of results, open a result.


6. In the Element Details screen, view details on the module,


including:


Names and addresses


Characteristics of the module

File details for the module file


Header and allocated properties values

Whether a header is a malformed executable header


7. View what processes are running the module and consider


whether that process should run the module.


8. Note if the module is a floating module. If it is a floating


module, check the protection details for mismatches.



