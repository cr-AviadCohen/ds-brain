For larger deployments, you can optionally install an NGAV Local
Update server to deliver the Anti-Malware Signatures DB updates.
In this topic:
Install the NGAV Local Update server
Use multiple NGAV Local Update servers
Capacity and related configuration
If your organization has a large number of endpoints, you can
optionally choose to install an NGAV Local Update server (or
servers) in your network to deliver Anti-Malware signature updates
to endpoints more quickly. This option also helps to minimize
potential traffic issues on the external network, and is especially
useful during the initial installation of Anti-Malware on sensors due
to the size of the full signature database (~1.2 GB) that requires
deployment to each endpoint.
Sensors download their first-time signatures update and
subsequent updates from the NGAV Local Update server. This
conserves network usage for your organization by avoiding direct
communication from your machines with an external server.
You can also control how frequently the Local Update server
receives signature updates from the Global update server. We
recommend setting the update frequency to between a few hours
to up to two days, for optimal security value. Ask Technical
Support for assistance to configure this setting.
If the sensor cannot connect to the NGAV Local Update server, it
connects to the NGAV Global Update server at https://cr-
protect.cybereason.net/ (https://cr-protect.cybereason.net/).
Cybereason provides (on request) a VM-based Local update
server running on a Linux operating system. This server Uses a
mirroring technology, which allows separation between the Anti-
Malware signature update request and retrieval process to reduce
sensor latency during updates and reduces load for the sensor. In
addition, your organization can now use a proxy to access the
Global Update server, which allows you to restrict access to
external domains, or to reduce the traffic and consumed
