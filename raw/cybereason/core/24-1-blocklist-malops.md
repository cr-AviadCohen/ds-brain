Examples of behavior that can trigger this MalOp:


File or process image file is on the blocklist
Process is executing a file on the blocklist

## Next steps: Blocklist file Hash


Investigate the image file hash value of the process.
Depending on the result of the investigation, mark the file for


prevention.

If prevention fails, escalate further and take appropriate steps


for your organization.

## Blocklisted module


The MalOp for Blocklisted module is triggered when a process


loads a module that is on the blocklist.


**Supported OS for this MalOp:** Windows, Mac OSX, and Linux


Examples of behavior that can trigger this MalOp:


Presence of modules on the blocklist


Presence of modules with a known malicious reputation

according to threat intelligence

## Next steps: Blocklisted module


Investigate the process that loaded the module by hash value.

Investigate the list of modules. In particular look at the


modules that are on the blocklist.

Verify if the detection is raised for the actual prevention of a


module on the machine. In some cases, the MalOp is raised

because you previously added the module to the blocklist. In


this case, you would no longer need to investigate the module

and would instead focus on the other items.


Ensure that the module in question is removed from the

machine.

## Connection to blocklist IP address


The MalOp for Connection to blocklist IP address is triggered

when a process accesses an IP address (either though a


connection or a DNS request) that is on your organization's

blocklist. Note that an IP address is not as strong of an indicator of


malicious activity since a single IP address may host a large

number of sites.


**Supported OS for this MalOp:** Windows, Mac OSX, and Linux


Examples of behavior that can trigger this MalOp:


Connection to an IP address on the blocklist for your

organization


Use of an IP address on the blocklist



