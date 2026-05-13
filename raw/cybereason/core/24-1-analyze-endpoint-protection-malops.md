3. Below the root cause item name, view the service that led to


the creation of this MalOp. For example, you might see **Anti-**


**Malware**, **PowerShell and .NET Protection**, and so forth.


4. Below the MalOp root cause name, read the description to


learn a little more about why the Cybereason platform created


the MalOp.


5. In the main part of the MalOp details, you can see a map of


the associated items for the MalOp.


In the example details above, you can see the platform has

indicated:


The root cause of the MalOp

Detection modules


The malicious file for this MalOp

6. Below the MalOp item summary diagram, view the timeline for


the activities associated with the MalOps.


Understanding the timeline helps you also see the length of


time that these behaviors have occurred in your environment.

## Analyze file information


Since Endpoint Protection MalOps are usually based on a single


event or grouped by similar events, such as the detection of

malware in your environment, the Cybereason platform provides


file details for the file(s) related to the malware for you to analyze.


1. In the MalOp details screen, open the **Files** tab.


2. View the file summary details, including:


The protection mode used


The first and the most recent time the file was run
The number of times the file ran


The machine(s) on which the file was found
The path to the file on the machine


Whether or not the file was detected as part of a scan
The file hash value for the file


3. In the file details grid, for the file name, hover over the file


name and click on the magnifying glass or click **Investigate** .


The Cybereason platform automatically builds the relevant

investigation query and opens the Element Details screen for


this file.


4. In the Element Details screen, view the properties to ensure


that the properties are expected.


For example, in this page, the process details show some


suspicious activity, as the process claims to be a Microsoft

process, it isn't signed by Microsoft. In addition, the process is


running from a temporary folder and has an unknown

reputation.

## Analyze machine information


In addition, you should understand the machines on which the file

was found to help mitigate threats on those machines.


1. In the MalOp details screen, open the **Machines** tab.


2. In the machines grid, view the machine information, including:


Machine name

Whether or not the machine is isolated


The operating system type for the machine

The last time the machine was detected by the


Cybereason platform.
3. In the file details grid, for the machine name, hover over the


machine name and click the magnifying glass or click

**Investigate** .


The Cybereason platform automatically builds the relevant

investigation query and opens the Element Details screen for


this machine.


4. In the **Element details** screen, view the properties to ensure


that the properties are expected.


5. In the **Element Details** screen for the machine, view the


generated suspicion and evidences for the machine to


summarize what is actually happening on the machine.



