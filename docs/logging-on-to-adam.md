# Logging on to ADAM

## Passkeys

A passkey is a credential stored on the user’s device (phone, tablet or computer) that signs the user in to ADAM using a fingerprint, face recognition or device PIN, instead of a password. Passkeys are resistant to phishing, are not reusable across sites, and never travel across the internet, so they are considerably safer than passwords. ADAM supports passkeys for staff, parents and pupils.

Each user may enrol more than one passkey — for example, one on their phone and one on their work laptop — and each passkey can be named so that it is easy to identify later. Passkeys never replace a user’s password and Two-Factor Authentication settings: they are an additional, optional way to log in, and the password and one-time PIN remain available as a fallback.

For a more detailed walkthrough, see the dedicated [Passkey Authentication](passkey-authentication.md#passkey-authentication) page.

### Signing in with a Passkey

On the staff, parent and pupil log-in pages, ADAM offers a Log in with a passkey button (marked with a fingerprint icon) above the username and password form. The button is only shown if the browser supports passkeys; older browsers will continue to see the password form on its own.

To sign in:

1.  Open the appropriate ADAM log-in page.
2.  Click Log in with a passkey.
3.  The browser will prompt for the device’s biometric (fingerprint or face) or PIN.
4.  Once the gesture is recognised, ADAM signs the user in and takes them to their dashboard or portal home.

Signing in with a passkey does not also ask for a one-time PIN — the passkey is itself a second factor. It does not, however, excuse the user from setting two-factor authentication up; see [Passkeys and Two-Factor Authentication](#passkeys-and-two-factor-authentication) below.

### Setting Up a Passkey for Staff

Whenever a staff member signs in without using a passkey — for example with their username and password — their dashboard displays a card titled “Log in with your fingerprint or face”, with a Set up a passkey button. Clicking the button takes the staff member to the Passkeys management page.

The card is hidden whenever the staff member signs in with a passkey (and on administrator “log in as” sessions), so it stays out of the way once a passkey is in use on that device. It will reappear on any later password login — for example on a shared computer where no passkey has been set up — as a reminder that a passkey can be added there too. To return to the Passkeys management page at any time, see [Managing Your Passkeys](#managing-your-passkeys) below.

To register a new passkey:

1.  On the Passkeys page, click Register a new passkey.
2.  Enter a name for the passkey when prompted (for example, “My iPhone” or “Office laptop”). The name is only used to identify the passkey on this management page.
3.  The browser will ask the operating system to create a passkey. On a phone or tablet this typically requires a fingerprint or face scan; on a desktop it may use Windows Hello, Touch ID, a security key, or a paired phone.
4.  Once the device confirms the gesture, the passkey is saved and listed on the management page.

### Setting Up a Passkey for Parents and Pupils

Parents and pupils manage their passkeys through the portal:

-   Family Portal → Security → Manage your passkeys
-   Pupil Portal → Security → Manage your passkeys

The Pupil Portal menu item is only shown to pupils whose accounts have logins enabled (see [Enabling and Disabling Pupil Logins](#enabling-and-disabling-pupil-logins)).

Whenever a parent or pupil signs in without using a passkey, the top of the portal page will also show a “Log in with your fingerprint or face” card with a Set up a passkey button, which is a shortcut to the same page. As with staff, the card is hidden only on sessions where the user signed in with a passkey, so it will reappear on any later password login. The registration steps are the same as those described under [Setting Up a Passkey for Staff](#setting-up-a-passkey-for-staff).

### Managing Your Passkeys

The Passkeys management page lists every passkey enrolled on the current account, showing the name, the date it was enrolled, and the date it was last used. Each passkey has two actions:

-   rename — change the name shown for the passkey (up to 100 characters). This does not affect the credential itself.
-   remove — permanently delete the passkey from ADAM. The user will no longer be able to sign in with that passkey, although the credential will still take up space in the device’s passkey manager (and can be removed there separately).

Users should remove a passkey if the device it lives on has been lost, sold, or is no longer in their possession. As long as the user can still log in another way (using their password and Two-Factor Authentication, or another passkey on a different device), they can remove a stale passkey themselves. Should a user lose their only passkey and be unable to log in to delete it, an administrator can remove it on their behalf — see [Revoking a Staff Member’s Passkey](#revoking-a-staff-members-passkey).

### Revoking a Staff Member’s Passkey

If a staff member loses a device, has it stolen, or leaves the school, an ADAM Super-Administrator can revoke any of their passkeys without needing the staff member’s cooperation. This is reached through the Manage Staff Passkeys page, where a Super-Administrator can:

1.  Select the staff member from a drop-down list of staff who have at least one passkey enrolled.
2.  Review the passkeys on that staff member’s account, with the name, date enrolled, and date last used for each.
3.  Click remove against any passkey that should be revoked.

The Super-Administrator cannot rename a staff member’s passkey or register a new passkey on their behalf — only the staff member, signed in as themselves, can do that. The same is true of parent and pupil passkeys: there is no administrator override for these, because they are tied to a specific device that only the parent or pupil has access to. If a parent or pupil cannot remove their own passkey, they should reset their password and use that to sign back in, then delete the passkey from their management page.

### Passkeys and Two-Factor Authentication

A passkey is itself a strong second factor — the device holding it, plus the biometric or PIN that unlocks it — so a user who signs in with a passkey is not asked for a one-time PIN as well. That remains true when **Two Factor Authentication Forced For Staff** is set to “Yes”.

What a passkey does **not** do is excuse a staff member from setting two-factor authentication up. Their password still works, and anyone who obtains it can still try to use it; the one-time PIN is what stops them. A staff member who signs in with a passkey but has not set up two-factor authentication will be asked to do so, exactly like anyone else.

Users signing in with a username and password continue to be asked for a one-time PIN as before.

### Browser and Device Requirements

Passkeys require a modern browser (recent versions of Chrome, Edge, Firefox or Safari) and a device with a fingerprint reader, face camera, passcode or device PIN. ADAM must be reached over an HTTPS connection — passkeys will not work on plain HTTP. Users on older browsers, or on devices without an authenticator, will not see the Log in with a passkey button and should continue to use their password.

### Audit Trail for Passkeys

Every passkey enrolment, rename, removal and login is recorded in the ADAM logs alongside other authentication events. Each passkey’s “Last used” date on the management page is also updated on every successful login, so users and administrators can see at a glance which credentials are still in active use.

## General Login Settings

A number of common login settings can be found in the [Site Settings](changing-site-settings.md#changing-site-settings). Navigate to the “Security” tab.

### Active Directory Authentication

If your school has an Active Directory server, you can capture its details here. The LDAP module may need to be installed before this will work.

If ADAM will communicate via the public internet with your AD server, you must use a Secure LDAP Connection to prevent your users’ login credentials from being visible.

### OAuth Authentication Settings

This can allow your users to authenticate to ADAM if they are signed in with their school-issued Google or Microsoft account. **Please contact [help@adam.co.za](mailto:help@adam.co.za) before you enable any of these settings.**

### Internal Password Administration

Here you can set the minimum password length required. Note that passwords shorter than 8 characters are not permitted.

The “Allow External Authentication Failover” feature allows users who would normally log into ADAM by authenticating against their Active Directory Server to still log in, even if their Active Directory Server is not available. Note the following:

The failover service works by storing an AD-validated encrypted hash of the user’s password as if it were an internally managed password. On future login attempts if the AD server is not available, ADAM will check the supplied password against the stored hash.

This is no less safe than having ADAM manage user passwords itself. On a successful login, ADAM will verify the user’s password against the hash stored in the database and, if necessary, update the password with a new hash.

-   This is not password *synchronisation*, rather password *caching*. ADAM can only remember passwords it has seen itself and which the AD server has verified as being correct. ADAM cannot “fetch” passwords from AD.

-   Users who have never logged into ADAM before will not be able to log in during an AD outage for the first time.
-   Users who logged into ADAM a log time ago and who have subsequently changed their password will still have their old passwords cached on ADAM and thus may need to use an old password to get into ADAM if logging in during an AD outage.
-   Take note here of “remember me” type logins which do not require a user to enter their password. Should a user need to log in with a password, they may find that they have to enter their previous password which might have changed some time ago.

-   If Active Directory blocks a user’s login attempt for any reason (e.g. account disabled, incorrect password used), ADAM erases the password hash stored.

-   This prevents the user from being able to log in later when the AD server is unreachable and is therefore unable to deny the login.
-   Such a user will not be able to log in until the connection to AD is restored.

-   While ADAM is not able to communication with the AD server, user accounts that may be disabled on AD but which have not attempted a login on ADAM since they were disabled, will still be allowed to log into ADAM during an outage.

-   It is important that user accounts in ADAM are also suspended and that AD is not relied upon.

### LDAP Authentication

In Linux based networks it is possible to have ADAM use a pure LDAP server for authentication. Note that while the Active Directory logins are conducted over LDAP, many of the settings for the AD LDAP implementation have been preconfigured.

### Login Settings

The **Login time out** is the amount of time in minutes that must elapse between any two page loads on ADAM before the user account is considered logged out. Note that typing a message (especially in the [Messaging Centre](messaging-centre.md#messaging-centre)) is not considered activity because there is no information going between the server and the client computer.

The **Remember logged-in machines for** setting stores a long-term cookie on a computer so that ADAM can recognise it on a later visit. It works together with the two-factor authentication settings, and both are described in [Two-Factor Authentication for Administrators](two-factor-authentication-for-administrators.md#the-settings).

Some schools may chose to **Allow “Remember Me” Logins**. This will prevent the login time-out from affecting the user. Schools should be cautioned against allowing this if the computers that staff use are often left unsupervised and unlocked (consider a desktop computer in a classroom which may have pupils in unsupervised, as opposed to a laptop which is more likely to be turned off and locked). The number of days that ADAM can remember a user for can be set with the **Remember Me Duration** setting.

## Staff Logins

Staff logins are governed by a number of different settings in ADAM.

### Site Settings

Within the [Site Settings](changing-site-settings.md#changing-site-settings), navigate to the “Security” tab. Here, a number of settings will affect staff logins.

## Pupil Logins

ADAM Administrators may also want to see [Understanding Pupil Login](parent-and-pupil-portal.md#understanding-pupil-login).

### Enabling and Disabling Pupil Logins

Pupil logins can be disabled from within the [Site Settings](changing-site-settings.md#changing-site-settings). On the Security tab under the heading “Pupil and Family Login”, change the setting “Allow pupil logins” to “No”.

### Default Settings

Within the [Site Settings](changing-site-settings.md#changing-site-settings), navigate to the “Security” tab. Under the heading “Pupil and Family Login”, ADAM has two settings which dictate the default login options for pupils.

The “Default Login Method” and “Default pupil & family login privileges” settings are automatically applied to any pupils when they are first added to the database. Note that changing these settings will not change any pupils’ login details: they are only used at the moment that the pupil is added to the database for the first time.

## Parent Logins

Parents may wish to refer to the section on [Logging on to ADAM: A Guide for Parents](logging-on-to-adam-a-guide-for-parents.md#logging-on-to-adam-a-guide-for-parents).

ADAM Administrators may also want to see [Understanding Parent Logins](parent-and-pupil-portal.md#understanding-parent-login).

Parent logins can be disabled from within the [Site Settings](changing-site-settings.md#changing-site-settings). On the Security tab under the heading “Pupil and Family Login”, change the setting “Allow family logins” to “No”.

## Troubleshooting Logins

### Parent requests a password reset, but does not receive an email

There are several possibilities as to why this might happen. If a parent doesn’t receive the password reset email, check each of these possibilities in the following order:

1.  **Check that their email address is captured accurately.** If the incorrect email address is captured, any password reset requests will be sent to the wrong address. In the worst case, this could mean that someone else will get access to their ADAM profile. In some instances, where ADAM can see obvious issues with the email address which makes it invalid (e.g. spaces in the domain), then ADAM won’t even attempt to send the email.
2.  **Check that their ID number is captured accurately.** It may be that ADAM simply isn’t able to match the ID number against any family member. This happens often with passport numbers which change from time to time when a new passport is issued.
3.  **Check that the ID number is linked to only one family profile.** Sometimes divorced or separated parents end up with multiple profiles on ADAM. In these instances, ADAM is unable to determine which family profile is logging in or, by extension, which children it should be showing. You can check if the ID number is associated with the family by searching for it: **Families → Messaging and Communications → Search for ID numbers**. Make sure that only one family profile is shown. If you are searching for a staff member who is also a parent, you should expect to see one family profile and one staff profile appear in the search results. It is only a problem if they have more than one family profile.
4.  **Ask the parent to check that the email hasn’t been delivered to a spam or junk mail folder.** In many instances, emails requesting password changes are treated suspiciously by many email providers and have a higher chance of being flagged as spam.
5.  **Ask your IT department to trace the email’s delivery in your email service’s logs.** It will be helpful to report the time when the parent requested the login. The more accurate the time is, the easier it will be to trace. They should see a record of the message being received from ADAM and it then being delivered onward on to the family member’s email service. If the email server had problems with onward delivery, they should be able to report these to you. The resolution of any problems here will, of course, depend on the issue that your IT department discovers. If, however, there is no record of any email being sent, and assuming that ADAM can send other email without issue, the problem is almost definitely going to be linked to one of the first three points above.

> [!WARNING]
> Parents tell us that they find the error messages about logging into ADAM to be unhelpful and vague. They ask us to change these messages to show more detail about what is wrong. We agree this would help solve problems faster.
>
> However, if we do this, it would also help hackers and criminals find real ID numbers in our system. Not only is it against the law to share information with people who shouldn’t have it, but it’s even more serious because it could put children in danger if someone finds out they go to a certain school.

### The login is very slow

The most likely reason is that ADAM is implementing a login delay which is based on a sudden influx of failed logins.

If ADAM detects a large number of failed login attempts, it begins to implement a delay before it validates the login. This is done to delay anyone who may be trying to try lots of different passwords in very quick succession using automated tools. This technique, credential stuffing, commonly employed by hackers.

This login delay will resolve over time, assuming that the failed login attempts stop.

ADAM administrators should check the logs for information related to these possible login failures.

A second reason, specifically for schools who use remote authentication mechanisms is that the communication between the ADAM server and the authentication server is being delayed. This could be because of network congestion or a performance issue with the authentication server.
