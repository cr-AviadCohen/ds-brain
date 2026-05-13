1. Add the **Children** Element to the rule. To do this, click the plus


sign next to the Process Element, and then select **Children** .
2. Add the following filter to the Children Element:


**Product type is Shell**


The **Build a rule** canvas should look like the following:


1. Click **Save rule** to save and enable the rule.


The next time the Cybereason platform encounters a shell process


with a Microsoft Office parent process, the platform will trigger a

Malop.

## Example 2: Trigger a MalOp for

## PowerShell attacks that are not running

## through PowerShell


**Scenario** : You want to trigger a MalOp when the platform

encounters PowerShell processes that are not running through


PowerShell. This behavior may indicate that an attacker is trying to

evade security tools. To detects this behavior, you'll want to create


a rule that detects when the term 'PowerShell' appears in the

command line, but the process that runs is not actually a


PowerShell process. We can determine if the process is a
PowerShell process by looking at the process's **Image file**, which


is the file from the disk that executes the process. To build the

rule:


1. On the **Security profile** screen, click **Create new rule** in the


**Custom detection rules** section.


2. In the **Configure rule type** section, specify the following:


a. **Rule name** : Suspicious PS Process


b. **Detection type** : Custom rule


c. **Detected activity** : Infection


d. **Root cause element** : Self


e. **Description** : PowerShell in the command line but image


file is not PowerShell.



