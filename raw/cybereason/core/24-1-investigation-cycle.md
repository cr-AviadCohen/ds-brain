## Phase 1: Choose your approach

You have many different approaches available to use:






|Approach|Description|
|---|---|
|**Lead-based**|Using this approach you start your<br>investigation with a specifc item or behavior<br>of interest.<br>For example, when you view MalOp details,<br>you may fnd a process that you did not<br>expect or that behaved in an unexpected<br>way. This process could be the start point of<br>an investigation as you search for more<br>information about it.<br>Leads can come from MalOp details, threat<br>intelligence you received, items of interest<br>found in previous hunts, and so forth.|
|**Attack**<br>**lifecycle**|In this approach, you search for behaviors<br>associated with different parts of the attack<br>cycle. For example, you can:<br>Search for processes transmitting large<br>amounts of data, a behavior used in the<br>Data Theft stage<br>Search for connections to a malicious<br>address, a possible sign of<br>communication with a Command and<br>Control server<br>Search for processes that elevated their<br>privilege to SYSTEM, which is<br>symptomatic of the privilege escalation<br>stage|
|**Internal**<br>**investigation**|This approach focuses on specifc points of<br>interest within your organization. You<br>investigate specifc departments, users,<br>machines and so forth and look at the<br>activity for the machines.<br>For example, you could look at the machines<br>of all the upper management to fnd<br>evidence of data theft and so forth.<br>Conversely, you could focus on all the<br>machines in a department that has suffered<br>attacks in the past.|


|Approach|Description|
|---|---|
|**Freestyle**|This approach involves random surveys<br>across your organization. You look for a<br>specifc item - such as a fle hash or certain<br>behavior - and sample randomly across your<br>organization.|
|**Emerging**<br>**threats**|This approach focuses more on behavioral<br>characteristics.<br>For example, for a new type of malware, you<br>can search for behaviors that the malware<br>uses, such as using WMI to open new<br>processes.|



Once you select an appropriate approach, you are ready to begin.

## Phase 2: Pick a starting point


Based on your investigation method, choose an item from which to


launch your investigation. This can be something you do not

understand or suspect might be malicious.


For example, for the **lead-based** approach, start with MalOps in

your **Malops management** screen and put together a list of leads.


You could also start with an item from threat intel that is a known

indicator of compromise. For an attack lifecycle approach, pick


behaviors used in different parts of the attack cycle.

## Phase 3: What is it?


From the reported data, try to determine what the suspicious item


or activity is. You can:


Look through your system to compare and contrast the


suspicion with known activities

View the item's properties


Search the Internet and threat intelligence sources

Use the **File Search** feature to search for and view malicious


files on your organization's machines.


Use the information you collect from this to make a more informed


guess.

## Phase 4: What is it doing now?


Use the data collected from the Cybereason platform to figure out


what is happening at this moment.


If you chose your lead from a MalOp, look at the timeline in the


**Malop details** screen.


If you are using the **Investigation** screen, look in the **Element**


**details** screen.


From these details, determine the characteristics of the item,


including related processes, which can help you determine what

the item is trying to accomplish.


For some items, the Attack Tree provides a useful visualization of

[the item over time. For details on the Attack Tree, see Hunt with](https://nest.cybereason.com/s/knowledge-base?article=24-1-hunt-with-the-attack-tree&language=en_US#hunt-with-the-attack-tree)


[the Attack Tree (/s/knowledge-base?article=24-1-hunt-with-the-](https://nest.cybereason.com/s/knowledge-base?article=24-1-hunt-with-the-attack-tree&language=en_US#hunt-with-the-attack-tree)

[attack-tree&language=en_US#hunt-with-the-attack-tree).](https://nest.cybereason.com/s/knowledge-base?article=24-1-hunt-with-the-attack-tree&language=en_US#hunt-with-the-attack-tree)


Note


Some details reflect the state at the time of collection, not at


the present moment. These include items you can delete,
such as files, registry entries, scheduled tasks and so forth.

## Phase 5: Is it supposed to be here?


By now you have a better idea of what the item is doing and how it

interacts with your environment, so you can determine whether it is


legitimate.


**If the item you are investigating is legitimate** : If this item is


part of a MalOp, you can respond to the MalOp by using the

'Malop is benign - Exclude' option from the **Malops**


**management** screen's response dialog box.

**If the item you are investigating is NOT legitimate** :


Continue your investigation with Phase 6.

**If you are unsure whether the item you are investigating is**


**legitimate or not:** Continue your investigation with Phase 6.

## Phase 6: To whom is it talking?


Determine who the malicious item is communicating with. From the


MalOp details and Element details screens in the Cybereason

interface, investigate parent and child processes, connections,


and affected users and machines to determine who the item is

communicating with.


Also in this case, the Attack Tree visualization provides a useful

context.

## Phase 7: Why is it running?


What process or action caused the item to run on your machine?

The answer to this may also help you determine if the item is


legitimate or malicious.

## Phase 8: Where else can I find it?


Conduct wide searches to see where else this item might be.



