# Parent and Pupil Portal

Many schools open the parent and pupil portals to improve the information that is available to parents. There are a number of different steps that need to be taken before parent and pupil access can be successfully given. This particular section in the manual will provide you with links to other parts that will guide you through the tasks in more detail.

## Pupil Permission Groups

It may seem counterintuitive, but parent *and* pupil access to ADAM is controlled through Pupil Permission groups. This is done because it allows parents to see different views for each of their children. For example, a parent with a child in the high school might get to see the mark book for that child but this may not be available for their child in the primary school.

Please read more about [Pupil Login Groups](security-administration-for-families-and-pupils.md#security-administration-for-families-and-pupils) and, once customised, how to [assign them to classes of pupils](security-administration-for-families-and-pupils.md#assigning-pupils-to-groups-by-class) at a time.

## Understanding Pupil Login

Pupils can log in to the portal using one of two different ways.

### Username and Password

The first is using a username or password. Most schools will either have this match their school usernames and use external Active Directory authentication to ensure that their passwords are correct. ADAM can store internal passwords too, if required.

The username and authentication method can be set individually for each pupil. If you require a lot of pupils to be changed, please let us know so that we can update the database for you. In a user’s profile, check that their username and authentication method are set under the **ADAM Access** heading.

![](assets/screenshots/parent-and-pupil-portal/parent-and-pupil-portal-01.png)

If a pupil has an *internal* password and it needs to be changed, this can be done by a staff member by navigating to **Pupils → Security → Change a pupil’s password**.

![](assets/screenshots/parent-and-pupil-portal/parent-and-pupil-portal-02.png)

If the passwords match and are secure, ADAM will allow you to click on the “Change password” button.

ADAM can also set a class’s passwords to a random password by navigating to **Pupils → Security → Change a class’s passwords**. Here, ADAM will prompt you to click on a button:

![](assets/screenshots/parent-and-pupil-portal/parent-and-pupil-portal-03.png)

After this, it will show you a list of randomly generated passwords. You will not see this list again, so make sure to copy it to a spreadsheet if you need it! The passwords generated are case-sensitive.

Pupils will be asked to change these passwords when they next log in.

Pupils and parents who prefer not to type a password each time can also enrol a passkey from the portal at **Pupil Portal → Security → Manage your passkeys** or **Family Portal → Security → Manage your passkeys**. Once a passkey has been enrolled, the pupil or parent can log in with their device’s fingerprint or face instead of a password. Their existing password remains valid as a fallback. See [Passkey Authentication](passkey-authentication.md#passkey-authentication) for more.

### OAuth logins using Google or Microsoft accounts

It is also possible to enable logins using your organisation’s Google or Microsoft accounts. Please see the [Security section](configuring-logins.md#configuring-logins) for more information on enabling this setting.

## Understanding Parent Login

Parents do not use a username to log into ADAM. Instead they type in their ID number (or passport number in the case of foreign parents):

![](assets/screenshots/parent-and-pupil-portal/parent-and-pupil-portal-04.png)

### Logging in for the First Time

If you have never logged into ADAM before, click on the button at the bottom of the screen “**New Account? Forgotten password?**”

![](assets/screenshots/parent-and-pupil-portal/parent-and-pupil-portal-05.png)

Enter your ID number or Passport number and click on the **Send me a reset link**.

Check your inbox for the email to arrive. You may also want to make sure that it does not arrive in your spam folder.

### Forgotten Passwords

If they forget their password, a button is provided at the bottom of the login page for them to click on to get a password reset link sent to their email.

![](assets/screenshots/parent-and-pupil-portal/parent-and-pupil-portal-06.png)

### Guide for Parent Logins

We have drawn up [a guide for parents to follow](logging-on-to-adam-a-guide-for-parents.md#logging-on-to-adam-a-guide-for-parents), guiding them through the login process which you are welcome to point them to, or adjust for your own uses.

## Troubleshooting Parent Logins

The following is a checklist that you can go through when parents are having a problem logging in.

### Duplicate ID Numbers

The most common problem arises when the same ID number is assigned to multiple families on ADAM. When parents login, they provide their ID number and ADAM uses this ID number to identify the family profile that is logging in. If there is more than one profile, ADAM is unable to determine which should be logging in and denies the login.

When parents attempt to log in with an ID number that is duplicated, administrators will receive an email warning them that there is a duplicate ID number on the system. They can then investigate this to find out why. Parents will receive a standard error message saying that their login credentials are invalid.

Similarly, when parents attempt to change their passwords and provide a duplicated ID number, ADAM will not be able to determine which profile should have its password change. In this instance, no email is sent to the parent and they will not be able to change their password. However, as with the login attempts above, the ADAM Administrator will receive an email notification that the duplicated ID number exists on the system.

![](assets/screenshots/parent-and-pupil-portal/parent-and-pupil-portal-07.png)

### Spam Email and Email Delivery Problems

For reasons of privacy and security, ADAM does not put password reset emails into the parent’s messaging log. It is thus difficult to tell if a password reset email has been sent to parents.

It often happens, by the nature of the email, that password reset emails are often filtered to users’ junk mail or spam folders in their email programs, or, occasionally, are rejected outright by their email server which is often managed by a company with strict email policies.

You will need to check your email service’s delivery logs to ensure that ADAM sent the password reset email and that the recipient server accepted delivery thereof. This is normally sufficient, since most recipient email servers will report it when they reject an email, but it can happen that a recipient server will receive and silently delete such emails. This remains out of ADAM’s control and, if this is happening, additional work will need to be done to improve the deliverability of email from your school’s domain, including things like ensuring SPF records, DKIM signing and DMARC policies are in place to improve the reputation of your email.

### Password Changing

ADAM [scans all passwords against a database of passwords](passwords-and-security-information.md#adam-tells-me-there-is-a-problem-with-my-password-why) that have been scraped from database breaches from around the world. This is in an effort to make sure that users are using unique, strong passwords. If a parent chooses a new password that might be already in this database, ADAM may prevent it immediately (depending on how weak the password is) or allow it for a few months. Parents who have existing passwords which are later added to this database from other breaches, may suddenly find that they are being forced to change their passwords.

This is normal and is part of our commitment to keeping the information that is stored within ADAM safe.

## Enabling The Portal, The Final Settings

Once the permissions are set up, you must enable the portal for parents and/or pupils. This is done in Site Settings:

Navigate to **Administration → Site Administration → Edit site settings**. Once the settings are loaded, click on the **Security** tab and scroll down to **Pupil and Family Login**.

![](assets/screenshots/parent-and-pupil-portal/parent-and-pupil-portal-08.png)

**Family Detail - “No ID Number Found” Reports:** If a parent attempts a login to ADAM but their ID number cannot be found on the system, ADAM will offer to send a report to the school alerting them of the parent and their attempt to log in. ADAM will request some identifying information from the parent so that the school can manually follow up with the parent concerned and investigate the matter.

**Default Pupil Login Method:** Your preferred authentication method for pupils is set here. Note that changing this setting alone does not affect any pupils - this is the setting that is applied to any new pupils. Note that this is applied when they are *first* captured into the database.

Once set, this can be changed individually for pupils in the database. This could allow, for example, senior pupils to use Active Directory passwords and junior pupils to use internal ADAM-managed passwords. It is also possible to change a pupil’s authentication mechanism to prevent them from logging in at all.

If your pupils use an Active Directory server, choose this here. ADAM can also manage the passwords internally if you require. Set the method to “internal passwords.” Other authentication mechanisms are also provided.

**Default pupil & family login privileges:** It is an excellent idea to set this [permission group](security-administration-for-families-and-pupils.md#security-administration-for-families-and-pupils) so that it gives new pupils and their families an appropriate level of access to the portal. Normally, this should be set to the same permission group that would normally be applied to the bulk of your student intake.

Again, be aware that this permission group is set when the child is *first* captured onto the system.

ADAM provides some simple permission groups “out the box”, but these can be [customised and new ones added as required](security-administration-for-families-and-pupils.md#security-administration-for-families-and-pupils).

**Allow Family/Pupil Logins:** Change these settings to “Yes” as required.

Finally, save the Site Settings.

## Testing the Logins and Permissions

Many schools have a staff member who has children at the school. Such a staff member makes an excellent test subject when testing parent logins.

Alternatively, an excellent way to test is to create a new family and link some children to the family. Then use this new family to log in.

If you want to verify the information that can be seen by a specific family, system administrators can navigate to **Families → Security → Login as a family**. Then, by searching for the family concerned, ADAM will perform a login as if you were that family. This login is in all senses indistinguishable from a normal family login.

## Parent Login Instructions

The manual has a set of guides written for parents and pupils, listed under **Guides for Parents and Pupils** in the navigation. You are welcome to send them to parents and pupils as they are, or to adjust them for your own uses:

-   [Logging on to ADAM: A Guide for Parents](logging-on-to-adam-a-guide-for-parents.md#logging-on-to-adam-a-guide-for-parents)
-   [Passkeys: A Guide for Parents and Pupils](passkeys-a-guide-for-parents-and-pupils.md#passkeys-a-guide-for-parents-and-pupils)
-   [Goal Setting: A Guide for Pupils and Parents](goal-setting-a-guide-for-pupils-and-parents.md#goal-setting-a-guide-for-pupils-and-parents)
-   [Medical Examinations: A Guide for Parents and Pupils](medical-examinations-a-guide-for-parents-and-pupils.md#medical-examinations-a-guide-for-parents-and-pupils)
-   [Online Agreements: A Guide for Parents and Pupils](online-agreements-a-guide-for-parents-and-pupils.md#online-agreements-a-guide-for-parents-and-pupils)
-   [Online Applications: A Guide for Parents](online-applications-a-guide-for-parents.md#online-applications-a-guide-for-parents)
-   [Sign-ups: A Guide for Parents and Pupils](sign-ups-a-guide-for-parents-and-pupils.md#sign-ups-a-guide-for-parents-and-pupils)
-   [Uploading Documents: A Guide for Parents and Pupils](uploading-documents-a-guide-for-parents-and-pupils.md#uploading-documents-a-guide-for-parents-and-pupils)

## Accessing the QR Code

Any parent or student who has access to the portal will see a **QR Code** menu option listed under the **General** heading. Tap on the link to see the QR Code.

> [!TIP]
> For users with limited data access or who may wish to avoid problems of bad signal, it may be sensible to take a screenshot of the QR code and store that in their phone’s photo gallery for future use.

Note that this QR Code is meant only for scanning by ADAM when searching for a pupil. It is not intended to work in any other website or QR Code scanner.

## Today’s Birthdays

Parents and pupils can be shown a short list of the pupils whose birthday falls on the current day. It appears under the heading **Today’s Birthdays** at the foot of the portal front page, below the children’s information and the family menu. Each pupil is listed with their name and age and, if the school chooses, their photograph. The names are not links, because parents and pupils have no access to another pupil’s profile.

Nothing is shown until the school grants the permission described below, so no birthdays are shared with anybody by default. If none of the pupils in view has a birthday today, the section is left out of the page altogether rather than appearing empty.

### Allowing parents and pupils to see birthdays

The list is controlled by the **View birthdays** permission, which appears under the **Birthdays** heading when you manage a [pupil login group’s permissions](security-administration-for-families-and-pupils.md#managing-permissions).

As with most permissions, there are separate tick boxes for **Pupils** and **Families**, so the list can be shown to parents only, to pupils only, or to both. Only pupils who are currently registered at the school are considered, both as viewers and as names in the list.

![](assets/screenshots/parent-and-pupil-portal/parent-and-pupil-portal-09.png)

### Choosing whose birthdays are shown

Navigate to **Administration → Site Administration → Edit site settings**, click on the **Pupils & Families** tab and scroll down to the **Widgets** heading.

![](assets/screenshots/parent-and-pupil-portal/parent-and-pupil-portal-10.png)

**Birthdays visible in the portal:** this decides how wide the list is.

| Option | Who appears in the list |
| --- | --- |
| **Pupils in the same class** | Only the viewer’s classmates. This is the default. |
| **Pupils in the same grade** | Every pupil in the viewer’s grade. |
| **Pupils in the same class or grade** | Either of the above. |
| **All pupils in the school** | Every currently registered pupil. |

“Class” here means the class in your default class subject — the subject ADAM uses whenever it refers to a pupil’s class without naming one, usually a register or form class. If that subject groups your pupils vertically instead, for example by boarding house, choose **Pupils in the same class or grade** so that pupils still see the others in their year.

A parent with more than one child at the school sees everything that any of their children would see, gathered into a single list.

### Choosing how much is shown about each pupil

Two further settings, in the same place, decide how much the list gives away about each pupil. Both start on the more private option.

**Show photographs in the portal birthday widget:** set this to **Yes** to include each pupil’s photograph. It starts as **No**.

**Names in the portal birthday widget:** choose between **First name and surname initial** — the default, which shows a pupil as *Connor A.* — and **Full name**.

> [!WARNING]
> Switching photographs on publishes pupils’ photographs to other families. ADAM keeps no record of which parents have agreed to their child’s photograph being shared in this way, so please satisfy yourself that your school’s photograph consent covers it before you do.

### What staff members see

Staff members have their own birthday list on the ADAM front page, under the heading **Today’s Birthday List**. It is older than the portal list, it always shows photographs and full names, and none of the three settings above apply to it.

It is governed instead by three staff permissions, on the **Site Admin** tab under the **Birthdays** heading: **See birthdays of pupils**, which is limited to the pupils that the staff member teaches, **See birthdays of all pupils**, and **See birthdays of all staff**. Staff birthdays appear only on this list — they are never shown to parents or pupils.

## Recording How a Name is Said

Parents and pupils can record a short clip of how a pupil’s name is pronounced, straight from the portal, without installing anything. The recording is not audible to anybody at the school until a staff member has listened to it and approved it.

The page appears as **How we say your child’s name** (or **How we say your name** for a pupil login) under the **General** heading of the portal menu. It is governed by the **Record name pronunciation** permission, under the **Pronunciation** heading when you manage a [pupil login group’s permissions](security-administration-for-families-and-pupils.md#managing-permissions), and applies to currently registered pupils only.

A separate site setting adds a prompt to the portal front page for any child with no recording yet. Both the permission and the setting start switched off.

The full feature — recording with a class, approving what parents submit, and what happens to a rejected recording — is described in [Name Pronunciations](name-pronunciations.md#name-pronunciations).
