While all the items in the matrix may be involved in malicious


activity, not every item in the MITRE framework may be malicious

by itself. For example, the matrix includes a technique for user


account creation ( **Create Account** ). Marking every user account

creation as malicious wastes an analyst's time as they would


investigate every user creation event, most of which are benign.

However, the MITRE ATT&CK matrix helps you identify when a


specific technique that by itself is often benign is used in

conjunction with other techniques.

## ATT&CK details in the Cybereason


The Cybereason platform provides coverage and visibility to many

parts of the ATT&CK matrix through detected MalOps, suspicions,


and evidence, and through collected telemetry data.


To help you understand when MalOps, suspicions, or evidence


correspond to a specific technique, the Cybereason platform

adds tags with the corresponding tactic, technique, or sub

technique:


Hover over the tag to see the technique numbers:


For each of the tags, you can then click the tag name to open the

relevant page in the MITRE ATT&CK site to learn more.


Watch the following video for an overview on how Cybereason

displays MITRE ATT&CK tactics and techniques in Malops.


For a full listing of the tactics and techniques included in the


[MITRE ATT&CK matrix, see the MITRE ATT&CK Knowledge Base](https://attack.mitre.org/wiki/Main_Page)

[(https://attack.mitre.org/wiki/Main_Page).](https://attack.mitre.org/wiki/Main_Page)


You can search for instances of techniques using the Cybereason

platform **Investigation** screen.


For evidence and suspicions that correspond to a tactic or

technique, you can build a query based on the tactic or technique


number assigned by MITRE. These numbers are represented by a

string that begins with **T** followed by the technique number:


In addition, the reference page for every MITRE ATT&CK


technique or sub-technique contains a wide variety of information

to help search further:


An extensive description on how the technique or behavior

works on the machine, including examples of what processes,


files, and so forth that are used.

Real world malicious frameworks that use the technique.


A section on Mitigation that includes steps to respond to the

technique.


A section on Detection that discusses different ways to find

the technique in your organization's environments.


You can use this information in a number of ways:


Use the keywords included in the technique's reference page

to search in the Search bar of the Investigation screen. For


example, for the **Account discovery** technique (Discovery >

Account Discovery), you can search in the Investigation


screen for this keyword and find an appropriate filter:


You can analyze the Detection section and find the relevant


indicators or behaviors you should detect. From these

suggestions, you can write an investigation goal/statement


and then build a query.


Watch the following video for an overview on creating queries to


identify MITRE ATT&CK tactics and techniques.


[For details on building a query and statement, see Plan a Hunt](https://nest.cybereason.com/s/knowledge-base?article=24-1-plan-a-hunt&language=en_US#plan-a-hunt)


[(/s/knowledge-base?article=24-1-plan-a-](https://nest.cybereason.com/s/knowledge-base?article=24-1-plan-a-hunt&language=en_US#plan-a-hunt)

[hunt&language=en_US#plan-a-hunt) and Hunting Use-Case](https://nest.cybereason.com/s/knowledge-base?article=24-1-plan-a-hunt&language=en_US#plan-a-hunt)


[Example (/s/knowledge-base?article=24-1-hunting-use-case-](https://nest.cybereason.com/s/knowledge-base?article=24-1-hunting-use-case-example&language=en_US#hunting-use-case-example)


[example&language=en_US#hunting-use-case-example).](https://nest.cybereason.com/s/knowledge-base?article=24-1-hunting-use-case-example&language=en_US#hunting-use-case-example)

## 

To illustrate how to discover instances of behavior corresponding


to ATT&CK techniques using the Cybereason platform, let's look at

an example of how this is done. For this example, you can use the


[Process Injection technique](https://attack.mitre.org/techniques/T1055/)

[(https://attack.mitre.org/techniques/T1055/).](https://attack.mitre.org/techniques/T1055/)


In the Process Injection specification, you can see that Process

Injection is done in a number of ways:


Injecting DLL files to another process and then running a

remote thread


Using malicious code inside a process through portable

executable injection


Injecting malicious code or a DLL through a process thread

Adding malicious code through an asynchronous call to a


process thread

Updating pointers inside a process to run malicious code


instead of the process's legitimate code
Using specific libraries or commands in Linux and Mac


machines


You can also see there are numerous examples of malicious tools


and frameworks that use process injection, including well-known

ones such as Cobalt Strike, PowerSploit, and so forth.


Then in the **Detection** section, you see many suggestions for

detection, including:


Monitor Windows API calls that are commonly used for code

injection


Monitor Linux-specific commands

Monitor for named pipe creation and connection events


Analyze command line arguments of processes for actions

that sync with code injection


Search for malicious tools like PowerSploit and PowerShell

performing injection


Given this information, there are a number of ways to search for

code injection using the Cybereason platform:


|Method|Description|
|---|---|
|Use the<br>**Injection**<br>keyword|The Cybereason platform contains a large<br>number of detection rules around code<br>injection:|


|Method|Description|
|---|---|
|Search by<br>command<br>line|For Process Elements, there is a flter<br>(Feature) to search for a specifc command<br>line. If you know of specifc command line<br>arguments used for code injection you can<br>search for those:<br>In addition, if you do not have a specifc<br>command line argument, you can return a list<br>of all processes, and add the command line<br>column to the results list in the**Investigation**<br>screen. This enables you to see and analyze<br>all command line arguments for all running<br>processes:<br>This method may be much more time-<br>consuming so it is recommended that you<br>research specifc command line arguments<br>relevant to your organization.<br>Furthermore, the Element Details for each<br>process report the command line details as<br>part of the collected details.|


|Method|Description|
|---|---|
|Search for<br>instances of<br>malicious<br>tools|The Cybereason platform contains detection<br>rules about some malicious frameworks.|



