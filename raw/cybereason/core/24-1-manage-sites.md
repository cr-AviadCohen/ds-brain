The **Manage sites** wizard's **Define sites** screen appears.


2. Click **Add Site** . Enter a Site name (e.g. USA). To add


additional sites, click **Add Site** again and enter more site
names, until you are finished adding sites.


3. Click **Next** to go to the **Assign detection servers** screen.

## Assign Detection servers to sites


From the **Assign detection servers** screen, you can assign


Detection servers to the sites you created.


1. Click a site to select it, and mark the checkbox beside a


Detection server to assign it to the selected site. Repeat this

for each Detection server. You can opt to leave some


Detection servers unassigned. Unassigned servers are

placed in a Default site.


2. Click **Next** to go to the **Define OS support to sites** screen.

## Assign sensors to sites


You can specify how you want Cybereason to assign sensors to


sites. Cybereason can assign sensors in the following ways:


By operating system


Following rules defined by regular expression


Mapping based on an uploaded CSV file


In the **Manage sites** wizard, you define operating systems rules
first. You specify other rules for assigning sensors to sites in the


subsequent screen.

## Assign sensors by operating system


1. In the **Define OS support to sites** screen, select operating


system types for each site. Your selection tells the
Cybereason platform to assign sensors to a specific site


based on the endpoint's operating system.


If you select Linux this includes all supported versions of


Linux.

2. Click **Next** to go to the **Assign sensors to sites** screen.

## Assign sensors by regular expression


From the **Assign sensors to sites** screen, you can specify rules

using regular expressions.


To add a rule, enter a regular expression that matches the

sensor's FQDN (or its machine names, if the FQDN does not


exist).


The Cybereason platform checks rules in the order in this list


(rules higher in the list that match an FQDN take priority over rules

that appear further down in the list).


Note


The Cybereason platform evaluates regular expressions


according to exact matches and are case insensitive.

## Assign sensors with mappings in a CSV


From the **Assign sensors to sites** screen, you can specify


assignments by uploading a CSV file that maps a list of sensors

and the sites to which they should be assigned.


The CSV file should include the following columns:

Fully qualified domain name (FQDN) of the machine with the


sensor

Site name


(Optional Field) Specific Detection server name inside the

respective site


Download an example CSV file to assist you in creating this file.


1. Click **Test configuration** to test your new sites and rules

configuration. A summary screen appears, summarizing your


changes and noting how many sensors will be reassigned to a

different site based on your changes.


2. Click **Apply** to apply your changes. The Detection servers


screen now displays the Detection servers organized into the
sites you defined.

## Sensor assignment priority


By default, the Registration server uses the following priority order


when assigning sensors to sites:

1. Mapping set in the CSV file


2. OS configuration settings in the **OS support** screen
3. Rules defined by regular expressions


To change the priority in which the Cybereason platform assigns

sensors to sites, click the up and down arrows next to the site


number in the **Priority** column:


As a best practice, Cybereason recommends you create a default


site with a regular expression of ".*" and set it last in the priority list.

Sensors will be assigned to the default site if they are not mapped


in the CSV file and do not satisfy any existing rules.


If sensors remain unassigned, the Cybereason platform sends an


alert and the server provides you with an Assignment CSV to help

with the sensor assignment. Cybereason recommends assigning


unassigned sensors quickly to ensure full security coverage.

## - Known limitations Managing sites


The following are known limitations for managing sites.


If two machines have the same FQDN address, if you assign
sensors to a site using a CSV file, both machines will be


redirected to the same site according to the FQDN specified
in the file. This is true even if the machine names for both


machines are different.



