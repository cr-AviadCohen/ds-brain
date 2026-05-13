[notifications-and-desktop-](https://nest.cybereason.com/s/knowledge-base?article=24-1-endpoint-machine-notifications-and-desktop-settings&language=en_US#configure-end-user-desktop-settings)


[settings&language=en_US#configure-end-user-desktop-](https://nest.cybereason.com/s/knowledge-base?article=24-1-endpoint-machine-notifications-and-desktop-settings&language=en_US#configure-end-user-desktop-settings)

[settings) for more information.](https://nest.cybereason.com/s/knowledge-base?article=24-1-endpoint-machine-notifications-and-desktop-settings&language=en_US#configure-end-user-desktop-settings)


In addition, you can use the Remote Shell utility to perform

remediation actions directly on a selected machine. For more


[information, see Respond to Threats on a Machine with Remote](https://nest.cybereason.com/s/knowledge-base?article=24-1-respond-to-threats-on-a-machine-with-remote-shell&language=en_US#respond-to-threats-on-a-machine-with-remote-shell)

[Shell (/s/knowledge-base?article=24-1-respond-to-threats-on-a-](https://nest.cybereason.com/s/knowledge-base?article=24-1-respond-to-threats-on-a-machine-with-remote-shell&language=en_US#respond-to-threats-on-a-machine-with-remote-shell)


[machine-with-remote-shell&language=en_US#respond-to-threats-](https://nest.cybereason.com/s/knowledge-base?article=24-1-respond-to-threats-on-a-machine-with-remote-shell&language=en_US#respond-to-threats-on-a-machine-with-remote-shell)

[on-a-machine-with-remote-shell).](https://nest.cybereason.com/s/knowledge-base?article=24-1-respond-to-threats-on-a-machine-with-remote-shell&language=en_US#respond-to-threats-on-a-machine-with-remote-shell)


Depending on your operating system and the MalOp you want to

remediate, you have different remediation options. Remediation


options include:






|Remediation<br>Option|Description|
|---|---|
|Kill a process|Use the kill process remediation option to stop<br>a malicious process from running on a<br>machine or a set of machines. When you<br>select this option, the Cybereason platform<br>fnds the necessary process and stops it on<br>the selected machine.|
|Quarantine a<br>fle|Use the quarantine remediation option to<br>move a malicious fle to a different location to<br>prevent it from executing.<br>The Cybereason platform deletes quarantined<br>fles after 30 days. The cleanup is scheduled<br>to run daily (every 24 hours) and on sensor<br>startup.|
|Remove a<br>registry entry|Use the remove registry entry remediation<br>option if you want the Cybereason platform to<br>delete a registry entry associated with a<br>malicious process.<br>**Note:** If detected**ransomware** has been<br>injected into a legitimate process,<br>Cybereason recommends you DO NOT<br>choose to remove the process from the<br>registry. Doing so may affect the integrity of<br>your system.|


|Remediation<br>Option|Description|
|---|---|
|Remediate<br>directly on a<br>machine|If the remediation options presented in the<br>**Malops management** or**MAlop details**<br>screens are not suffcient for your needs, you<br>can perform remediation tasks directly on a<br>machine from the Cybereason UI. Run the<br>Remote Shell utility to remediate and<br>investigate on a specifc machine (this feature<br>must be enabled). For details, see Respond<br>to Threats on a Machine with Remote Shell<br>(/s/knowledge-base?article=24-1-respond-to-<br>threats-on-a-machine-with-remote-<br>shell&language=en_US#respond-to-threats-<br>on-a-machine-with-remote-shell).|
|Prevent fle<br>execution|Use this option to add a fle to the blocklist<br>and prevent it from running on other machines<br>in your environments. This setting applies to<br>all machines with Application Control<br>enabled.<br>After enabling this setting, if the fle hash is<br>detected again, the Cybereason platform will<br>stop it from running on any machine.|
|Isolate a<br>machine|Isolating a machine enables you to stop all<br>communication from a machine or machines.<br>This enables you to later go to the machine<br>and investigate or remediate as needed.|


Note





For a list of supported systems for each option, see the

**Response features** [table in Supported Features by Operating](https://nest.cybereason.com/s/knowledge-base?article=24-1-supported-features-by-operating-system&language=en_US#supported-features-by-operating-system)


[System (/s/knowledge-base?article=24-1-supported-features-](https://nest.cybereason.com/s/knowledge-base?article=24-1-supported-features-by-operating-system&language=en_US#supported-features-by-operating-system)

[by-operating-system&language=en_US#supported-features-](https://nest.cybereason.com/s/knowledge-base?article=24-1-supported-features-by-operating-system&language=en_US#supported-features-by-operating-system)


[by-operating-system).](https://nest.cybereason.com/s/knowledge-base?article=24-1-supported-features-by-operating-system&language=en_US#supported-features-by-operating-system)


[For examples of these remediation options, see MalOp](https://nest.cybereason.com/s/knowledge-base?article=24-1-malop-remediation-examples&language=en_US#malop-remediation-examples)


[Remediation Examples (/s/knowledge-base?article=24-1-malop-](https://nest.cybereason.com/s/knowledge-base?article=24-1-malop-remediation-examples&language=en_US#malop-remediation-examples)

[remediation-examples&language=en_US#malop-remediation-](https://nest.cybereason.com/s/knowledge-base?article=24-1-malop-remediation-examples&language=en_US#malop-remediation-examples)


[examples).](https://nest.cybereason.com/s/knowledge-base?article=24-1-malop-remediation-examples&language=en_US#malop-remediation-examples)


Watch this video to learn about remediation options.


## Remediate using the Malops

After you determine the best response option for one or more


MalOps, you perform remediation actions from the **Malops**

**management** screen.


**To remediate one or more MalOps from the Malops**

**management screen, follow these steps:**


1. Select the checkbox to the left of the MalOps to which you


want to respond. The response option you choose applies to


all the selected MalOps.

2. Click **Respond** above the MalOps list. Available responses for


the MalOp depend on the processes, machines, files, and

users that the MalOp involves.


3. If the MalOp represents a threat to your environment, do the


following:






|Environment Type|Steps|
|---|---|
|Environments not<br>using the Data<br>Platform<br>infrastructure|a. Above the MalOps grid, click<br>**Respond**.<br>b. In the dialog box, select<br>**Malop is malicious -**<br>**Remediate**.<br>c. Select your remediation<br>options and click**Respond**.|


|Environment Type|Steps|
|---|---|
|Environments using<br>the Data Platform<br>infrastructure|a. Above the MalOps grid, click<br>**Respond**.<br>b. Select the necessary response<br>actions and targets.<br>c. Click**Apply response**.|


4. Back on the **Malops management** screen, select the MalOps


you just remediated, and do one of the following


**If your environment does not use the Data Platform**


**infrastructure:** Click **Mark as resolved** to indicate the

MalOp or MalOps have been addressed.


**If your environment does use the Data Platform**


**infrastructure** Click **Set status as** and select **Closed** .


5. If the MalOp is not a threat to your environment and you want


to prevent the specific behaviors from triggering a MalOp in

the future, select **Malop is benign - Exclude** [. See Manage](https://nest.cybereason.com/s/knowledge-base?article=24-1-manage-false-positives&language=en_US#manage-false-positives)


[False Positives (/s/knowledge-base?article=24-1-manage-](https://nest.cybereason.com/s/knowledge-base?article=24-1-manage-false-positives&language=en_US#manage-false-positives)

[false-positives&language=en_US#manage-false-positives) for](https://nest.cybereason.com/s/knowledge-base?article=24-1-manage-false-positives&language=en_US#manage-false-positives)


more information.

## Remediate using the Malop details screen


After you determine the best response option for a MalOp, you


can respond to the MalOp from the MalOp's **Malop details**

screen.


**To remediate a MalOp from the Malop details screen, follow**


**these steps:**


1. Click **Respond** in the upper right-hand corner.


2. Under **Remediate** or **Prevention**, select the checkboxes that


you want. Available responses for the MalOp depend on the


processes, machines, files, and users that the MalOp

involves.


3. From the list of options, select the machines, files, and actions


to apply:


4. Click **Apply** .


5. When you have remediated the MalOp, indicate that you have


addressed the MalOp:


If your environment uses the Data Platform infrastructure,

for all MalOps, select **Closed** from the dropdown menu.


If your environment does not use the Data Platform

infrastructure, for Endpoint Protection MalOps, select the


**Mark as resolved** button.

## Send actions to offline sensors


When performing remediation tasks, If a selected sensor is offline

when the Cybereason platform sends a remediation action, the


action will be queued and applied when the sensor comes online.

Queued actions can wait for up to 72 hours for the sensor to come


online.


Note


If you send the same action multiple times, the Cybereason

platform ignores the new action to avoid duplicates.


Watch a short demo on remediation for offline sensors:


## View MalOp remediation history

You can view MalOp remediation history by MalOp or by machine.


|Remediation<br>view|Details|
|---|---|
|**View response**<br>**history by**<br>**Malop**|From the**Malop details** screen, use the<br>Respond options, and then click**Show**<br>**response history**, as shown below. The<br>response history shows all the response<br>actions performed on the MalOp.|


|Remediation<br>view|Details|
|---|---|
|**View response**<br>**history by**<br>**machine**|From the**Investigation** screen, click the<br>**Response history** button in the**Machine**<br>**details** dialog box. The response history<br>shows all the response actions performed<br>on the machine.<br>Note<br>The**Response history** button only<br>appears for machines with associated<br>remediation actions.|



The response history includes the following columns:












|Column|Description|
|---|---|
|Machine<br>name|Machine from which the action was sent|
|Action|Action sent to the target(s)|
|Target|Element on which the action will execute. For<br>example, the process name associated with a<br>'kill process' action.|
|User|User that sent the action|
|Send time|Time the user sent the action|
|Execution<br>time|Time the action was applied. Note: this may be<br>signifcantly later than the Send time if the target<br>machine was offine when the user sent the<br>action.|
|Action<br>status|Status of the action's execution. Hover over a<br>Failed value to learn more about why the action<br>failed to execute.|





