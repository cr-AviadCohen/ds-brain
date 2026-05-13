|Method|Details|
|---|---|
|**From the**<br>**Malop details**<br>**screen**|1. From the**Malop details** screen for the<br>MalOp whose associated machine(s)<br>you want to isolate, click**Isolate** in the<br>upper right corner.<br>2. If the MalOp is associated with more<br>than one machine, Cybereason<br>prompts you to confrm that you want to<br>isolate all associated machines.|


|Method|Details|
|---|---|
|**From the**<br>**Investigation**<br>**screen**|1. Use the query builder to search for the<br>machine you want to isolate. If you want<br>to isolate a machine associated with a<br>specifc MalOp, you can fnd<br>information about the machine in the<br>**Malop details** screen of the associated<br>MalOp.<br>2. From the**Investigation** screen results<br>grid, double-click the machine that you<br>want to isolate.<br>3. Click**Isolate**.<br>Note<br>The**Isolate** button only appears if the<br>machine is currently online and<br>connected to the Cybereason platform.|


## Stop isolation on a machine

When you no longer need a machine isolated, you can stop

isolation from the **Malop details** screen (for all associated


machines) or **Investigation** screen (for individual machines).






|Method|Details|
|---|---|
|**From the**<br>**Malop details**<br>**screen**|From the**Malop details** screen for the<br>MalOp whose associated machine(s) you<br>want to isolate, click**Stop isolating** in the<br>upper right corner.|
|**From the**<br>**Investigation**<br>**screen**|1. Use the query builder to search for the<br>machine on which you want to stop<br>isolate. If you want to stop isolating a<br>machine associated with a specifc<br>MalOp, you can fnd information about<br>the machine in the**Malop details**<br>screen of the associated MalOp.<br>2. From the**Investigation** screen results<br>grid, double-click the machine that you<br>want to stop isolating.<br>3. Click**Stop isolating**.|


## Machine isolation exception rules

Machine isolation exception rules allow you to define IP addresses


and/or ports through which you can communicate with isolated

machines. Machine isolation exception rules are useful when you


want to allow IT staff from outside your environment to access

isolated machines to conduct deeper investigations and perform


remediation actions.


Note


Since isolated machines are completely cut off from

communication with all systems except for the Cybereason


platform, isolation can hamper investigation of the machine if

not used correctly.


Using machine isolation exception rules, you can allow machine

communication according to the following:


Specific IP address

IP range


One or more ports


When you create an exception rule, you must select the direction


of communication affected by the exception. If you select

**Incoming**, the selected port refers to the port on the isolated


machine. If you select **Outgoing**, the selected port refers to the

destination port on the remote machine (for example, a server that


the isolated machine is connecting to). For example, you could
define that incoming communication is allowed to isolated


machines from IP address 31.166.153.170 on port 8443 of the

isolated machines.


If your environment has sensor grouping enabled, you can also

specify the groups to which the isolation exception applies.


Assigning the rule to a specific group limits access to the

machines in the group to admins or analysts who have permission


to access the sensors included in the specified group. Other

analysts and admins without permission to access the group will


not be able to access the machine, even with the isolation

exception rule defined in the Cybereason platform.

## Define isolation exception rules


You define machine isolation exception rules in the **Machine**
**isolation exceptions** tab in the **Security profile** screen.


**To define a machine isolation exception rule, follow these**


**steps:**


1. In the **Machine isolation exceptions** tab, click **Create**


**exception** .

2. Select one of the following communication options:


**Incoming** : communication is allowed for data arriving to
the port and/or address or range specified.


**Outgoing** : communication is allowed for data sent to the
port and/or address or range specified.


3. Define one or more of the following:

**IP Address/Range** : Users can define a specific IP


address or an IP range, which will include all the IPs
within the defined range. You specify the ranges in 3rd


and 4th bytes (for example, 1.2.3-5.5-6).
**Port(s)** : To define multiple ports, separate each port with


a comma ","


Note


You must choose at least one port or IP address.


4. If your environment has sensor grouping enabled, assign the


group assignment permissions. You set the isolation

exception rule to **Assign globally** (for all groups) or **Assign**


**to a specific/multiple groups** .



