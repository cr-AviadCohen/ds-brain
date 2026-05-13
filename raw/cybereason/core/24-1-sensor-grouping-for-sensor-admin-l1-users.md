## Sensor admin L1 role permissions

As shown in the image above, from the **System** screen, Sensor


admin L1 users can:


1. Access the **Sensors** tab.


2. View and search for sensors in the groups specified in their


user settings.


3. Download sensor packages specific to the groups specified


in their user settings.


4. Perform limited actions on sensors in their groups (see the


Available Sensor admin L1 actions section below).


As shown in the image above, from the **Security profile** screen,

Sensor admin L1 users can:


Access the **Reputations** tab to search for reputations or

download a CSV of the reputations in the environment.


Access the **Machine isolation** tab to view machine isolation

exception rules.


Sensor admin L1 users _cannot_ :


Access **System** screens other than the **Sensors** page.


View or search for sensors outside the groups specified in

their user settings.


Perform actions on sensors outside the groups specified in

their user settings.


Add or update reputations or machine isolation exception

rules.

## Available Sensor admin L1 sensor actions


Users with the Sensor admin L1 role can perform the following
actions on sensors in the groups specified in their user settings:


Update

Restart


Fetch sensor log

Start system scan


Stop system scan

Export to CSV


Import sensor tags CSV

Archive sensors


Add sensor to group from the **Unassigned** group (in versions

earlier than 23.1.125)


Add sensors to a group (in version 23.1.125 and later)

Remove sensor from group from the **Unassigned** group (in


versions earlier than 23.1.125)

Remove sensors from a group (in version 23.1.125 and later)


## Add a sensor to a group

Sensor admin L1 users can add sensors to another group for


which they have permissions.


To add a sensor to a group:


1. From the **System**  - **Sensors** screen top right dropdown


menu, select the Unassigned group.
2. If necessary, use the filter bar or quick filter checkboxes to


identify the sensors you want to add to a group.

3. Select the checkbox next to the sensor(s) and click **Actions**,


and then select **Add to group** .

4. From the **Add sensors to group** dialog box, select a group to


add the sensors to, and then click **Confirm** .

## Remove a sensor from a group


Sensor admin L1 users can remove sensors from groups for which


they have permissions. Removed sensors will automatically join

the Unassigned group.


To remove a sensor from a group:


1. From the **System**                    - **Sensors** screen top right dropdown


menu, select the sensor group from which you want to remove

sensors.


2. If necessary, use the filter bar or quick filter checkboxes to


identify the sensors you want to remove from the group.


3. Select the checkbox next to the sensor(s) and click **Actions**,


and then select **Remove from group** .


To move a sensor from one group to another, first remove the

sensor from its current group, and then add it to a new group. This


means the sensor will appear in the Unassigned group for a short

period of time.





