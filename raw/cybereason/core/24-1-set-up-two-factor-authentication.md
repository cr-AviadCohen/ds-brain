2. In the Authentication section, in the **Enable TFA**


**authentication** option, move the toggle to **On** to enable, or

**Off** to disable.


When two-factor authentication is enabled, the Cybereason

platform also displays the number of users that have the two

factor authentication enabled for their user:


Note


Turning off two-factor authentication for the platform disables

two-factor authentication for all users, regardless of the user's


individual TFA status.

## Enable or disable two-factor

## authentication for users


Once a system admin enables two-factor authentication for the


platform, the user admin can manage user-level TFA settings from

the **Users** screen.


The checkbox in the far right of the user's row shows the current
state of TFA for that specific user:


If the user has TFA disabled, the checkbox is

empty/unchecked.


If the user has TFA enabled, the checkbox shows a

checkmark.


To enable or disable TFA for a single user, select or clear the

checkbox in the far right of the user's row. To enable or disable


TFA for all users, select or clear the checkbox in the header row.


In both cases, the platform prompts you to confirm your choice:


If you enable TFA, the Cybereason platform sends the user or

users an email with instructions on how to set up two-factor


authentication.


When you log in with two-factor authentication, in the login screen,


after you enter your password, the Cybereason platform prompts

you to enter a personal key into the TOTP application. An


authenticator code is then sent to you, and you can then complete

the login process.

## Reset the two-factor authentication key

## for a user


The personal key powers the connection between the TOTP


application and the Cybereason platform two-factor authentication

mechanism. A system admin can reset this key to resolve issues


with the TOTP application for a specific user or if required by

internal security policies.


**To reset the personal key for a user, follow these steps:**

1. Hover your mouse over the row for a specific user account


that has two-factor authentication enabled.



