## (B2C and SAML 2.0)

Follow these steps to configure Azure Active Directory for use with


Cybereason SSO. As you configure, note the following values that

you will need to provide to Technical Support to enable SSO:


For B2C:


Application (client) ID


Client secret

Microsoft Azure AD Domain


Application ID URI


For SAML 2.0:


IdP Domain: The user email domain used to log into the

system


Sign In URL (available from the Okta Admin Dashboard)
x.509 Signing certificate (available from the Okta Admin


Dashboard)

## Register an app


1. Log in to your Azure portal.


2. Search for one of the following services:


For SAML 2.0: **Azure Active Directory**


For B2C: **Azure AD B2C**

3. Select the service to open the **Overview** page.


4. From the left navigation pane, under **Manage**, select **App**


**registrations** .


5. Select **New Registration** .


6. In the **Register an application window**, configure the


following:


**Name** : A user-facing display name for the application


**Supported account types** : Accounts in this

organizational directory only (Cybereason only - Single


tenant)

**Platform configuration** : Web API


7. Select **Register** .

## Set API permissions for your registered


After you register an app in your Azure platform for the

Cybereason SSO service, you need to provide the appropriate API


permissions for the app.


The following instructions apply to the API that connects your


Azure instance and the Cybereason SSO service.


**To add API permissions, follow these steps:**


1. After you register the app, if needed select the app in the **App**


**registrations** page.


2. In the app registration details, in the left navigation pane,


under **Manage**, select **API permissions** .


3. Select **Add a permission** .

4. From the **Request API permissions** pane, select **Microsoft**


**Graph** and then **Delegated Permissions** .

5. In the **Select permissions** section, select the following:


email

offline_access (optional)


openid
profile


6. Select **Add permissions** .

7. From the **API permissions** page, select **Grant admin**


**consent to <tenant name>** .

8. When prompted, answer **Yes** .

## Configure SSO-based authentication

## between Azure and Cybereason SSO


After you add the API permissions, you must configure the

authentication mechanisms between your Azure AD instance and


Cybereason SSO.


**To configure authentication, follow these steps:**


1. After you register the app, if needed select the app in the **App**


**registrations** page.


2. In the app registration details, in the left navigation pane,


under **Manage**, select **Authentication** .


3. Select **Add a platform** .
4. From the **Configure platforms** pane, select **Web** .


5. In the **Configure Web** window, configure the following:


**Redirect URLs** : Contact Technical Support for this value


**Implicit grant** : Select **Access tokens** and **ID tokens**


6. Select **Configure** .

## Add client secrets


To ensure the secure communication between your Azure instance

and Cybereason SSO, you need to set up client secrets as


needed.


**To add secrets, follow these steps:**


1. After you register the app, if needed select the app in the **App**


**registrations** page.


2. In the app registration details, in the left navigation pane,

under **Manage**, select **Certificates & Secrets** .


3. Select **New client secret** .


4. From the **Add a client secret** window, enter a description and


expiration time. Note this value and provide it to Technical

Support.


Ensure you note this value, as you will need the value later in
the configuration process.


5. Select **Add** .

## Add application ID URI for Cybereason SSO


The final step in the process is to add an application ID URI for


Cybereason SSO to use for SSO requests.


**To add an application ID URI, follow these steps:**


1. After you register the app, if needed select the app in the **App**


**registrations** page.


2. In the app registration details, in the left navigation pane,


select **Overview** .

3. Note the **Application (client) ID** as you will need this value


later in the SSO configuration process.

4. Select **Add an Application ID URI** .


5. Select **Set** to use the default URI.

## Configure SAML settings in Okta


Follow these steps to configure the SAML settings in Okta for


Cybereason SSO. To learn how to create a SAML integration, see
**Task 1: Launch the Wizard**, and **Task 2: Configure general**


**settings** [in the Okta documentation](https://help.okta.com/en/prod/Content/Topics/Apps/Apps_App_Integration_Wizard_SAML.htm)

[(https://help.okta.com/en/prod/Content/Topics/Apps/Apps_App_In](https://help.okta.com/en/prod/Content/Topics/Apps/Apps_App_Integration_Wizard_SAML.htm)


[tegration_Wizard_SAML.htm).](https://help.okta.com/en/prod/Content/Topics/Apps/Apps_App_Integration_Wizard_SAML.htm)


As you configure, note the following values that you will need to


provide to Technical Support to enable SSO. The values are

available from the Okta Admin Dashboard:


Login URL/SignOn URL

Logout URL/SignOut URL (this value may be the same as the


login value)
x.509 certificate format


To configure SAML settings in Okta:


When Okta is enabled in your environment, the Cybereason


Support team will provide you with the **ACS URL** and **Audience**

**URI** values.


1. In Okta, select the **Sign On** tab for the Cybereason SAML


app, and then click **Edit** .


2. Enter the **ACS URL** and **Audience URI** into the


corresponding fields.


3. Select **Email** for the **Application username format**


4. Click **Save** .

5. You can now assign users to the application.


The following SAML attributes are supported:


**Name** : email


**Name format** : Basic

**Value** : user.email


## Configure Other SAML 2.0 Vendors

Note


The Cybereason platform SSO authentication can be

integrated with any vendor using SAML 2.0 authentication.


However, Cybereason only provides vendor-specific
configuration instructions for the vendors above.


To configure SSO with other SAML 2.0 vendors, provide the

information listed below to the Technical Support team. You can


then use the SSO URL and Audience URI to configure integration

with your SAML 2.0 vendor.

## Provide SSO details to Cybereason

## Technical Support


To complete the configuration of SSO, provide the following

[information to Technical Support (/s/support):](https://nest.cybereason.com/s/support)


**IdP Domain**  - This is typically the email domain for your users

using SSO.


**Sign In URL** 1- Also known as the Identity Provider Single

Sign-On URL or just the SSO URL. This is the URL where the


Cybereason platform sends your vendor SAML authentication

requests.


**X509 Signing Certificate** 1- This validates the signature of the

authentication assertions that have been digitally signed by


your SSO vendor.


1Many SSO vendors allow you to export a metadata XML file,


which contains this information.

## Configure integration with your SAML


Use the information provided below to complete your SSO


integration.

## SSO URL


The SSO URL is also known as the Assertion Consumer Service


URL (ACS). This is the Cybereason URL where your SSO vendor

sends SAML assertions.


To configure your SSO, use the URL appropriate for your region:


|Location|Domain|
|---|---|
|USA|https://cybereason-us-<br>prod.auth0.com/login/callback<br>(https://cybereason-us-<br>prod.auth0.com/login/callback)?connection=<br><DNS name for your Cybereason platform>-okta-<br>ad|
|EMEA<br>and<br>APAC|https://cybereason-eu-<br>prod.eu.auth0.com/login/callback<br>(https://cybereason-eu-<br>prod.eu.auth0.com/login/callback)?connection=<br><DNS name for your Cybereason platform>-okta-<br>ad|








|Location|Tenant name|
|---|---|
|USA|urn:auth0:cybereason-us-prod:<DNS name for<br>your Cybereason platform>-okta-ad|
|EMEA and<br>APAC|urn:auth0:cybereason-eu-prod:<DNS name for<br>your Cybereason platform>-okta-ad|





