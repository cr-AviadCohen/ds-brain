Sensor tampering protection provides enhanced protection to the
Cybereason processes running on Windows endpoints. With
sensor tampering protection, Cybereason protects its processes,
files, services, and registries against unauthorized or malicious
modifications or kill attempts. For example, sensor tampering
protection prevents unauthorized access to the processes related
to the sensor.
In addition, sensor tampering protection protects the sensor from
unintentional end user actions that might compromise security. For
example, an end user might kill a resource-intensive sensor
process that is responsible for a number of protection capabilities,
instead of contacting Technical Support to resolve the issue. This
exposes the endpoint machine to potential attacks.
In this topic:
Enable sensor tampering protection
Additional sensor security
Enable sensor tampering protection
In version 23.2.148 and later, sensor tampering protection is
generally available and is enabled by default.
1. In the sensor policy, navigate to the Sensor management &
upgrades screen.
2. For sensors up to version 23.2.148: Switch the Sensor
tampering protection [Legacy] toggle to On.
3. For sensors 23.2.148 and later: Switch the Sensor tampering
protection toggle to On.
To prevent maintenance actions in addition to tampering
protection, you can switch the Extended tampering
protection with passkey toggle to On. If this option is set to
On, maintenance actions such as upgrading the sensor will
require the use of a passkey file. Use of this option requires a
