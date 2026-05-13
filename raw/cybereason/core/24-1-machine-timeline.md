7. Open the **Details** pane for an item by clicking on the event


The **Machine Timeline** screen displays machine activities that


involve the following Cybereason Elements:


Connection


Detection Events

Driver


File


FileAccessEvent

LogonSession


MalopProcess

Msrpc


Process

QuatantineFile


RegistryEvent

Scheduled Task


For example, the timeline will display an entry for a file that was
modified, or a connection that was established.


The **Machine Timeline** includes the following columns:






|Column name|Description|
|---|---|
|Date|Timestamp for the activity.|
|Name|Name of the activity, for example the<br>name of the fle or process.|
|Suspicions/MalOps|Icon and number indicating whether the<br>activity is associated with one or more<br>suspicions or MalOps.|
|Operation|Operation performed by the item. Values<br>include:<br>Creation Time<br>Termination Time<br>Modifcation Time|
|Description|Details about the item, such as the fle<br>path, whether a connection is ingoing or<br>outgoing, or the type of detection.|
|Element Type|The activity Element type. Values<br>include:<br>Connect<br>Detection Events<br>File<br>Logon Session<br>Process<br>Scheduled Task|


## Access the Machine Timeline

You access the **Machine Timeline** screen when inspecting a

process on a single machine. You can open the **Machine**


**Timeline** screen for a specific event from the **Investigation** and


**Attack Tree** screens:

## From results in the Investigation screen


Click the arrow to the left of a result to expand the individual item.

Then, do one of the following:


Click the **Machine Timeline** icon next to the item:


Select the item to open the **Details** pane, and then click the


**View Machine Timeline** link.

## From the Attack Tree screen


Select a process bubble in the **Attack Tree** view to open the


**Details** pane. Click the **View Machine Timeline** link in the top

section of the pane, under the process name, as shown in the


following image:

## Example usage


As an analyst, when reviewing the results of an investigation


query, you come across a process on a specific machine and

want to understand the events that surround the process.


Specifically, you are interested in files that were modified within the

ten minutes surrounding the event. To do so, perform the


following:


1. From the **Investigation** screen, expand the item in the results


table to view the individual processes.


2. Click the **Machine Timeline** icon .


The **Machine Timeline** screen opens in a new browser tab


and displays activity that occurred on the machine five

minutes before and after the selected event.


3. Filter activity to include file modification events:

a. Select the filter icon to reveal the **Filters** pane


b. Select the **File** checkbox under **Element Type** .

c. Select the **Modification Time** checkbox under


**Operation** .

4. Expand the timeframe by selecting **+-10 min from event**


**creation time** in the timeframe selector dropdown.


The timeline now lists file modification activity on the machine in


the ten minutes surrounding the original process.



