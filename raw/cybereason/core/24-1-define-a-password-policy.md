When you deploy the Cybereason platform for the first time, the


password complexity is set to Strict and the default admin

password will meet the Strict requirements. If you upgrade from a


version that supports password complexity, the Cybereason

platform preserves the existing complexity setting, as well as the


user lockout policy and 2FA configurations.


If you change the password complexity from Strict to Basic, no


changes are required for existing users, since all Strict passwords
already fulfill the criteria for Basic password complexity.


If you change the password complexity from Basic to Strict,the

Cybereason platform alerts each user the next time they log in that


their password is non-compliant with the organizational policy. The

Cybereason platform redirects the user to a screen to change the


password.

## Define password expiration policy


By default, passwords expire after 6 months.


When a user password expires, the Cybereason platform prompts

the user to enter a new password at next log in. The new


password must comply with the complexity policy. In addition, the

new password cannot be the same as the previous 10 passwords.


**To change the password expiration policy setting:**


1. In the **Settings** screen, navigate to the **Password policy**


section.

2. In the **Password expiration** option, from the drop-down list,


select the number of months after which passwords will

expire. You can select any value from 1 to 12 months.

## Define the user lockout policy


The user lockout policy specifies when to lock out a user based
on incorrect password attempts within a configured time frame.


When a user is locked out, they cannot attempt to log in. Once the

platform locks out a user, only the User admin can manually


unlock the user account. The Cybereason platform also

automatically unlocks the locked user's account after a


configurable time period.


**To configure the user lockout policy:**


1. In the **Settings** screen, navigate to the **Password policy**


section.


2. If the **User lockout option** is not enabled, move the toggle to


**On** to enable lockout settings.


3. Set values for:


The number of failed attempts. Select a value between 3


and 99.

The timeframe. Select a value between 1 and 999


minutes.


The unlock timeout. Select a value between 1 and 999


minutes.


**To unlock a locked out user:**


1. Navigate to the **Users** view.

2. Hover over the row for the locked user.


3. Click the lock icon that appears towards the right of the row.


The user is unlocked. They can now attempt to log in again.





