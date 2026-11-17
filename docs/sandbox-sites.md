# Sandbox Sites

A **sandbox** is a practice copy of your school’s ADAM site. It has its own web address, and it holds a copy of all of your school’s real information. Staff can use it to try things that they would not risk on the live site, for example:

-   a new report layout;
-   a rehearsal of the [year-end functions](year-end-functions.md#year-end-functions);
-   a large import of information;
-   training a new administrator.

Nothing that you do in a sandbox changes your live site, and nothing that you send from a sandbox reaches parents, pupils, staff or any other system.

> [!WARNING]
> A sandbox holds your school’s real pupil, family and staff information. Treat it with the same care as the live site, and give its web address only to staff who need it.

## Getting a sandbox

There are no settings for a sandbox, and there is no menu option to create one. To have a sandbox created, or refreshed, contact ADAM support at [help@adam.co.za](mailto:help@adam.co.za). ADAM support will give you the sandbox’s web address.

> [!NOTE]
> A sandbox site is essentially another copy of ADAM. As such, there are costs involved for having a sandbox because you are essentially running another copy of ADAM. This takes up additional server resources. Please contact [help@adam.co.za](mailto:help@adam.co.za) for more information about the costs involved. These include setup fees and hosting costs.

## Refreshing a sandbox

When ADAM support refreshes a sandbox, everything in it is replaced with a new copy of the live site. Every change made in the sandbox since the last refresh is lost. This includes changes to information, settings, report layouts, passwords, passkeys and documents.

Do not keep work in a sandbox that you need to keep. When a change that you tried in the sandbox works, make the same change on the live site.

## Recognising a sandbox

Every page of a sandbox shows a banner headed **Sandbox**, which reads:

> This is a sandbox copy of *your live site’s address*. Nothing sent from here is delivered, and every change is discarded at the next refresh.

If you do not see this banner, you are on the live site.

Search engines are asked not to list a sandbox.

## Signing in to a sandbox

Only staff can sign in to a sandbox.

-   **Staff** sign in with their ADAM password or, at schools that use it, their [Active Directory or LDAP account](configuring-logins.md#configuring-active-directory-authentication). Their ADAM password is the one they had on the live site when the sandbox was last refreshed.
-   **Sign in with Google** and **Sign in with Microsoft** are not offered, even when your school has turned them on.
-   **Passkeys** made on the live site do not work in a sandbox, because a passkey belongs to one web address. A staff member can sign in with their password and then add a new passkey in the sandbox. See [Passkey Authentication](passkey-authentication.md#passkey-authentication).
-   **Parents and pupils** cannot sign in, by any method, including the ADAM App. The Parent Login and Pupil Login pages show “Family and pupil sign-in is not available in a sandbox.”
-   **Login as a family** and **Login as a pupil** do not work in a sandbox. They show the same message.
-   The reCAPTCHA check is not shown on the login page.

> [!NOTE]
> A staff member who has no ADAM password, because they sign in only with Google, Microsoft or a passkey, cannot sign in to a sandbox until they have one. An administrator can set a password for them in the sandbox itself, but it is lost at the next refresh. A password set on the live site is copied into the sandbox at the next refresh. See [Resetting a staff member’s password](staff-passwords.md#resetting-a-staff-members-password).

## What a sandbox does not do

### Nothing is delivered

No email or SMS sent from a sandbox reaches anyone.

-   Features that send messages behave as if the message was sent, but it goes nowhere.
-   Messages sent from the [Messaging Centre](messaging-centre.md#messaging-centre) stay in their batch, waiting to be sent. You can view them under **Administration → Messaging Administration → View Messaging Centre batches**.
-   The **Send a test email** and **Send a test SMS** buttons are not shown in the Messaging Centre, because a test message could not arrive.
-   Messages that ADAM sends on a schedule, such as absentee alerts and reminders, are not sent.

### Nothing reaches other systems

A sandbox does not connect to other systems. For example, it does not send information to SA-SAMS, transfer files by FTP or send notifications to the ADAM App. Integrations with other systems do not run.

The only outside connection a sandbox makes is to your school’s Active Directory or LDAP server, when a staff member signs in with their directory account.

### AI summaries are not made

A sandbox does not make new AI summaries. Where ADAM would show a new summary, the sandbox shows “Summaries are not available in a sandbox.” Summaries that were copied from the live site can still be read.

### No backups are made

ADAM makes no backups of a sandbox, because everything in it is replaced at the next refresh.

## Documents and photographs

Documents and photographs from the live site can be viewed in a sandbox. Documents that you add, replace or delete in the sandbox affect only the sandbox. The live site’s documents are never changed.
