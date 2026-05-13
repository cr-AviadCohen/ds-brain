**Root Cause Type** : Malicious Code Injection
**Description** : Allow browser injection into flashPlayer


The **Define rule properties** field displays.

## Step 1.2: Add the first expression


1. Click **Select an element** and select **Process** from the drop

down menu. The **Process** element will be the first Element

you select for most behavioral allowlisting rules.


When you select Process, the screen displays:

A filter icon to the right of **Process** .


A plus (+) sign below **Process** .


2. Select the plus ( **+** ) sign to add another Element to the rule.

3. Select the **Original injector process** Element.


4. Select the filter icon for **Original injector process**, type _p_ in

the filter field, and select **Process name** from the list of filters.


5. Complete the filter using the default **contains** operator, and


replace **any string** with a browser name such as **Firefox** or


the process name such as **firefox.exe** .


Click the **OR** button that appears to add more browsers, such


as **Explorer** ( **explorer.exe** ) or **Chrome** ( **chrome.exe** ).


6. Click outside the filters field and click **Add** to add the


expression to the rule.


Now you're ready to add your second expression. The behavior


must match **all** the expressions in the rule to be considered

benign.

## Step 1.3: Add the second expression


1. To add a second expression to the rule, click **Select an**


**element** and select **Process** from the drop-down menu.


2. Select the plus ( **+** ) sign and add the **Host process** Element.
3. Select the filter icon, type _p_ in the filter field, and select


**Process name** from the list of filters.
4. Complete the filter using the default **contains** operator,and


replace **<any string>**with **flashPlayer** .

5. Press **Enter** until the **Add** button activates, and click **Add** to


add the expression to the rule.


You now have a valid behavioral rule that prevents Cybereason


from triggering a Malop when Firefox injects code into Flash

player. You can also add additional expressions, as shown in the


next step.

## Step 1.4: Add the third expression


1. To add a third expression to the rule, click **Select an element**


again and select **Process** .
2. Select the filter icon, type **i** in the filter field, and select


**Injection method** from the list of filters.
3. Complete the filter using the **is** operator, and select


**Anonymous RWX** from the value drop-down menu.
4. Click outside the filters field and click **Add** to add the


expression to the rule.


## Example 2 - Allowlist a connection to a

## malicious IP address

If your users may have legitimate reasons to access an IP address


on the blocklist, you might want to define ths rule.

## Step 2.1: Name and describe the rule


1. In the **Behavioral Allowlisting** screen, click **Create rule** .


2. In the rule creation screen, specify the following:


**Rule name** : Chrome to blocklisted IP


**Root Cause Type** : Connection to blocklisted IP address

**Description** : Allow Chrome connection to a blocklisted IP


address


The **Define rule properties** field displays.

## Step 2.2: Add the first expression


1. To start building the rule, click **Select an element** and select


**Process** from the drop-down menu.


2. Select the filter icon, type _p_, and select **Process name** from


the list of filters.
3. Complete the filter using the **contains** operator, and replace


**<any string>** with **Chrome** or **chrome.exe** .

4. Press **Enter** until the **Add** button activates, and click **Add** to


add the expression to the rule.


The Cybereason platform adds the expression to the rule.

## Step 2.3: Add the second expression


1. To add a second expression to the rule, click **Select an**


**element** again and select **IP address** .


2. Select the filter icon and complete the filter with the IP


address that is usually blocklisted.


3. Press **Enter** until the **Add** button activates, and click **Add** to


add the expression to the rule.


4. Click **Save** to save your completed rule.


## Example 3 Allowlisting for connection to

## a malicious domain

If you want the Cybereason platform to classify the Symantec

management agent as benign when the agent connects to a


malicious domain, you can create an appropriate allowlisting rule.

## Step 3.1: Name and describe the rule


1. In the **Behavioral Allowlisting** screen, click **Create rule** .


2. In the rule creation screen, specify the following:

**Rule name** field: Connection to malicious domain 

Symantec management agent

**Root Cause Type** : Connection to a malicious domain


**Description** : Allow Symantec management agent to

connect to a malicious domain

## Step 3.2: Add first expression


1. To start building the rule, click **Select an element** and select


**Process** from the drop-down menu.


2. Select the filter icon, type **p**, and select **Process name** from

the list of filters.


3. Complete the filter using the **is** operator, and replace **<any**


**string>** with **AeXNSAgent.exe** .


4. Select the plus (+) sign and add the **File** Element to the rule.


5. Select the filter icon, type **s**, and select **Signer** from the list of

filters.


6. Complete the filter using the **contains** operator, and replace


**<any string** with **Symantec** .


7. Press **Enter** until the **Add** button activates, and click **Add** to


add the expression to the rule.

## Step 3.3: Add second expression


1. To add the second expression, click **Select an element** and


select **Domain name** .


2. Select the filter field, type _n_ and select **Name** from the list of


filters.
3. Complete the filter using the **contains** operator, and replace


**<any string>* with **Google** .

4. Press **Enter** until the **Add** button activates, and click **Add** to


add the expression to the rule.


5. Click **Save** to save your completed rule.



