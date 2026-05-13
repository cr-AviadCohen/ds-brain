You may choose to distribute sensors across your organization by
creating a template, or golden image, of a virtual or physical
machine with a sensor already installed. You can then distribute
the golden image to all endpoints in your organization.
Cybereason sensors include mechanisms to generate unique IDs
for a machine based on a variety of parameters. The sensor
process regenerates this ID automatically on the sensor machine
start to ensure that the sensor has its own uniquely identifier.
To deploy the golden image, do the following:
1. Install the Cybereason sensor on the machine that will
become the golden image.
2. Verify that the sensor is connected to the server and is
configured correctly (in the System > Sensors screen).
3. Create the golden image of the machine.
4. Deploy the golden image to other machines.
5. Verify that the sensors on all deployed golden image
machines are connected to the server and are configured
correctly (in the System > Sensors screen).
See Virtualization Support (/s/knowledge-base?article=24-1-
virtualization-support&language=en_US#virtualization-support) for
more information on deployment on VMs.
Note
After you deploy sensors in a virtual machine (VM) or virtual
desktop infrastructure (VDI) environment by using a golden
image, on the System > Sensors screen you may notice
duplicate entries or duplicate sensor entries override each
other's data and the connection to the server. For
troubleshooting steps on how to resolve this issue, see
Duplicate Sensors or Data Overrides After VM or VDI Sensor
Deployment with Golden Image (/s/article/2863372).
