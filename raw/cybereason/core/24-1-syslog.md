As you perform various actions in your Cybereason platform, the
platform's updates the syslog to provide an audit trail of the users
that took various actions, as well as details about the action. As a
result, you can send the information in the syslog to other
platforms to use in your various other security workflows and
management systems, or use the information for auditing and
compliance.
You can use the logging feature for a variety of purposes:
Workflow management: Track the process from MalOp
creation to remediation.
Team member monitoring: If an employee is no longer with
the company, review their action history and make sure you
removed their access abilities.
Investigation: If a MalOp status is incorrectly changed to Not
Relevant, investigate the user action log to see who made the
change.
Alerts: Set up alerts in your SIEM to track MalOps or
suspicious user behavior, such as machine isolation from a
user who should not be isolating machines, or to ensure you
set up permissions correctly.
Compliance checking: If certain actions require supervision,
send logs of certain actions to the appropriate reviewer.
Review what information you can use in the syslog. There is no
automatic integration for consumption of the syslog messages.
However, once you understand what details the syslog contains,
you can build your own custom system to consume the data from
the syslog.
In addition, you can customize the syslog stream (for example, if
you would like to forward the syslog messages to your own syslog
server) with the help of Technical Support.
For more details on the syslog, see:
Available syslog files: Syslog Files (/s/knowledge-base?
article=24-1-syslog-files&language=en_US#syslog-files)
