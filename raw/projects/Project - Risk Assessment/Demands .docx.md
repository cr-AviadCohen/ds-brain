# Demands .docx

Required fields from the schema for calculating the Event score:

metadata.action

metadata.engine

metadata.severity

principal.asset.type

principal.asset.ip\_address.reputation

principal.file.reputation

principal.nat\_ip.reputation

principal.networkInterface.address.reputation

principal.process.integrity

principal.process.file.reputation

principal.process.parent.integrity

principal.process.parent.file.reputation

principal.url.reputation

target.asset.type

target.asset.ip\_address.reputation

target.file.reputation

target.nat\_ip.reputation

target.networkInterface.address.reputation

target.process.integrity

target.process.file.reputation

target.process.parent.integrity

target.process.parent.file.reputation

target.url.reputation

network.dns.resolver.reputation

email.attachment.reputation

email.links.reputation

Permissions: For Day 1, we will use regex to check if these fields include "admin" or "system."

principal.registry.owner.permmisions.name

principal.user.permmisions.name

target.registry.owner.permmisions.name

target.user.permmisions.name

(Chain)Ask the engineering: Is there a field in the schema that indicates whether the process is still running?

Day 2 demands:

Required fields from the schema for Correlation (Incident):

metadata.event\_id

metadata.event\_subtype

metadata.event\_type

metadata.severity

metadata.severity\_details

metadata.timestamp

metadata.type

metadata.uuid

principal.asset.domain

principal.asset.type

principal.asset.ip\_address.address

principal.asset.name

principal.asset.uuid

principal.file.creation\_time

principal.file.sha256

principal.file.tlsh

principal.file.uuid

principal.file.internal\_name

principal.group.name

principal.nat\_ip.address

principal.NetworkInterface.address.address

principal.NetworkInterface.id

principal.NetworkInterface.name

principal.process.creation\_time

principal.process.file.creation\_time

principal.process.file.sha256

principal.process.file.tlsh

principal.process.file.uuid

principal.process.file.internal\_name

principal.process.pid

principal.process.user\_uuid

principal.process.uuid

principal.process.parent.creation\_time

principal.process.parent.file.sha256

principal.process.parent.file.tlsh

principal.process.parent.file.uuid

principal.process.parent.file.internal\_name

principal.process.parent.pid

principal.process.parent.user\_uuid

principal.process.parent.uuid

principal.registry.owner.domain

principal.registry.owner.email\_addresses

principal.registry.owner.username

principal.registry.owner.uuid

principal.url.domain\_name

principal.url.url\_path

principal.url.uuid

principal.url.reputation

principal.user.domain

principal.user.email\_address

principal.usename

principal.user.uuid

target.asset.domain

target.asset.type

target.asset.ip\_address.address

target.asset.name

target.asset.uuid

target.file.creation\_time

target.file.sha256

target.file.tlsh

target.file.uuid

target.file.internal\_name

target.group.name

target.nat\_ip.address

target.NetworkInterface.address.address

target.NetworkInterface.id

target.NetworkInterface.name

target.process.creation\_time

target.process.file.creation\_time

target.process.file.sha256

target.process.file.tlsh

target.process.file.uuid

target.process.file.internal\_name

target.process.pid

target.process.user\_uuid

target.process.uuid

target.process.parent.creation\_time

target.process.parent.file.sha256

target.process.parent.file.tlsh

target.process.parent.file.uuid

target.process.parent.file.internal\_name

target.process.parent.pid

target.process.parent.user\_uuid

target.process.parent.uuid

target.registry.owner.domain

target.registry.owner.email\_addresses

target.registry.owner.username

target.registry.owner.uuid

target.url.domain\_name

target.url.url\_path

target.url.uuid

target.url.reputation

target.user.domain

target.user.email\_address

target.usename

target.user.uuid

network.conn\_end\_time

network.conn\_start\_time

network.conn\_first\_seen

network.dns\_query\_uuid

network.dns.resolver.address

network.dns.resolver.reputation

network.session\_id

email.attachment.creation\_time

email.attachment.sha256

email.attachment.tlsh

email.attachment.uuid

email.attachment..internal\_name

email.attachment.reputation

email.links.domain\_name

email.links.url\_path

email.links.uuid

email.links.reputation

email.message\_id

email.recipients

email.sender

**DAY 2:**

**Machine Score:**

**This information is not currently available in the schema.**

Network Access:

We currently lack information about the machine's connection capability.

For example: If outbound connection capability becomes available, we will add X to the score.

Sensitive ports:

We will need information about all open ports on the endpoint.

Subnet:

The subnet each machine belongs to.

.

OnPrem vs Cloud:

What is the resource? Local or Cloud

Agent policy configuration:

For each machine, the current configuration applied to the agent can be determined.

(detect mode/ prevent mode/ disabled)

Detection unresolved-

Gather information about the detection status: resolved, seen, or not opened, along with the detection time.

**CVE:**
