**To create the sensor groups, follow these steps:**


1. In your Cybereason platform, navigate to the **System >**


**Groups** screen.


2. In the **Groups** screen, click **Create new group** .
3. In the **Create new group** dialog box, give the the first sensor


group a name and description:


**Name:** USA


**Description:** Sensors in the USA region


Leave the **Assignment logic** and **Policy assignment** options
blank for now. You will fill these in later.


4. Click **Create group** .

5. In the main **Groups** screen, repeat steps 2-4 to create two


additional groups:






|Group<br>1|Name: EMEA<br>Description: Sensors in the EMEA region|
|---|---|
|**Group**<br>**2**|**Name:** AUS-NZ<br>**Description:** Sensors in the Australia and New<br>Zealand region|


## Step 2: Assign sensors to a group

When you have created sensor groups, you can assign or remove

sensors in these groups. Sensors that are not assigned to any


sensor group are located in the **Unassigned** group.


**To assign the sensors in a group, follow these steps:**


1. In your. Cybereason platform, navigate to the **System >**


**Sensors** screen.


2. In the top right corner of the **Sensors** screen, in the dropdown


list, select the **Unassigned** group.


3. In the Sensors screen, select the sensor that you want to add.

4. Above the sensors list, click **Actions** and select **Add to**


**Group** .


5. In the **Add sensors to group** dialog box, from the group list,


select **USA** .


6. Click **Confirm** to assign the sensor.


Later, if you need to remove the sensor from the group, use the


**Remove From Group** option.

## Step 3: Assign sensors automatically


To help scale and automate parts of the sensor group assignment


process, you can instruct the Cybereason platform to assign a
sensor to a specific group according to one of the following


criteria:


Organization unit (OU)


Machine name

Internal IP address


External IP address


In this tutorial, the USA part of your organization uses IP


addresses in a certain range. You will create criteria that assigns

sensors that have IP addresses in this range to the USA group.


**To set automatic assignment criteria, follow these steps:**


1. In your Cybereason platform, navigate to the **System >**


**Groups** screen.

2. In the **Groups** screen, for the **USA** group, click the **Edit**


button.

3. In the **Edit group** screen, in the **Assignment logic** field, from


the **Select** dropdown list, select **Internal IP address** .

4. Next to the **Internal IP address** option, select **is in range**


5. Replace **any ip address with mask** with the IP address and


mask (for example, 192.168.5.0/24).



