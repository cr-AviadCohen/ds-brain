|Setting|Description|
|---|---|
|Email address|The user's email address. Cybereason<br>uses this email address to send<br>notifcations.<br>The email address's TLD (top-level<br>domain) must be a valid public TLD.<br>Note: For On Prem environments where<br>SSO is enabled, it is possible to add a<br>user with a local domain email. Such<br>users can login via SSO. Note that it is<br>not possible to enable email notifcations<br>for such users, and other email workfows<br>(e.g. reset password) are not supported<br>for such users.|
|Password|A password for the user. The password<br>must conform to your organization's<br>password policy set in the**Settings >**<br>**Password Policy** screen.<br>For details, see Defne a Password Policy<br>(/s/knowledge-base?article=24-1-defne-<br>a-password-<br>policy&language=en_US#defne-a-<br>password-policy).|
|Change<br>password on<br>next login|Select this option to require the user to<br>change the password on their next login.<br>The new password cannot be the same<br>as the previous 10 passwords.|
|Enable<br>notifcations|Select this option to enable notifcations<br>for the user.<br>Non-admin users can only change this<br>value for themselves.|
|Enable Two<br>Factor<br>Authentication|Select this option to enable Two-Factor<br>Authentication (TFA) for the user. TFA<br>must also be enabled for the<br>environment. For details on enabling TFA,<br>see Set Up Two-Factor Authentication<br>(/s/knowledge-base?article=24-1-set-up-<br>two-factor-<br>authentication&language=en_US#set-up-<br>two-factor-authentication).|


|Setting|Description|
|---|---|
|Custom and<br>Predefned<br>Roles|The role to assign to the user. For details<br>on available roles, see Manage User<br>Roles and Permissions (/s/knowledge-<br>base?article=24-1-manage-user-roles-<br>and-<br>permissions&language=en_US#manage-<br>user-roles-and-permissions).|



After you create a user, the **Date** column in the **Users** screen

shows the time when you created the user.


Note


The User Classification feature is in the beta stage. Contact


your Customer Success representative to enable this feature.


The User classification feature allows user administrators to add a


label to a specific user for auditing purposes. User administrators
can add a string value to the **User classification** field in the


**Users** screen when creating or editing a user.


The User classification string must meet the following parameters:


Include only alphanumeric, hyphen, and underscore

characters


Be no longer than 12 characters


For each user action, the **userclassification** field appears in the


[user audit syslog message. See Syslog Messages - Extension](https://nest.cybereason.com/s/knowledge-base?article=24-1-syslog-messages-extension-fields&language=en_US#syslog-messages-extension-fields)

[Fields (/s/knowledge-base?article=24-1-syslog-messages-](https://nest.cybereason.com/s/knowledge-base?article=24-1-syslog-messages-extension-fields&language=en_US#syslog-messages-extension-fields)


[extension-fields&language=en_US#syslog-messages-extension-](https://nest.cybereason.com/s/knowledge-base?article=24-1-syslog-messages-extension-fields&language=en_US#syslog-messages-extension-fields)
[fields) for more information about the user audit syslog.](https://nest.cybereason.com/s/knowledge-base?article=24-1-syslog-messages-extension-fields&language=en_US#syslog-messages-extension-fields)


For example:


cybereason|cybereason||useraction|general/login|0|cs1label=user


[name cs1=/temp@cybereason.com](mailto:cs1=/temp%40cybereason.com)

[(mailto:cs1=/temp%40cybereason.com) ...](mailto:cs1=/temp%40cybereason.com)



