# Staff Information

## Adding new staff to the database

To add a new staff member to ADAM, click on the “**Staff**” tab and, under the “**Staff Administration**” heading, click on “**Add a new staff member**”.

There are several sections that will appear in the next screen, and we’ll discuss them individually:

1.  General Information
2.  Contact Information
3.  Qualification Information
4.  Registration Information
5.  Employment Information
6.  Custom Fields (this might not appear – see Custom Data Fields on page  for more information)

### ![](assets/screenshots/staff-information/staff-information-01.png)

### General Information

In this section, you will enter simple information about the teacher of staff member. The following points are worth noting:

**ID Number:** if the teacher is a foreign national, please enter their passport number here. ADAM *will* produce a warning message saying that the number that is entered is not a valid South African ID number. This is not a problem since we know that we are entering a passport number.

The fields for **Population Grouping**, **Home Language**, **Disabilities** and **Marital Status** are used for reporting to the Department of Basic Education through the LURITS system.

### Contact Information

This section includes contact information for the teacher.

![](assets/screenshots/staff-information/staff-information-02.png)

Please take note of the following:

**E-mail address** is the only field that ADAM uses to send emails to staff. The **Personal E-mail Address** field is only for information.

**Dependents’ Names** should be listed one per line.

All phone numbers in ADAM should be entered as simple 10-digit numbers. Do not use any spacing or punctuation. For example, we prefer “0821112222” to “(082) 111 2222”. Whenever ADAM has to display a telephone number, it automatically spaces it out for you.

### Qualification and Registration Information

The next section collects information about the qualification levels of the teachers. Some of this information might seem redundant but this is because of the different reporting mechanisms that the Department of Education requires.

The SACE and PERSAL Numbers should be entered without spaces or punctuation.

![](assets/screenshots/staff-information/staff-information-03.png)

### Employment Information

This is the most important part, as far as ADAM is concerned, of adding a new staff member to the database. The information that is captured here will determine even if they can log in to ADAM or not, so it must be captured carefully!

![](assets/screenshots/staff-information/staff-information-04.png)

All the headings from **Department** to **Teaching Level (Additional)** are for Departmental uses and so should be captured carefully.

ADAM will automatically fill in today’s date as the **Start Date** for a teacher. If you know the start date of a teacher, please capture it accurately. This is so that ADAM can work out the length of time teachers have worked at the school automatically.

The **Prior Teaching Experience** is a field that determines how much teaching experience a teacher has had *before* the started teaching at your school. With this number and the calculation that ADAM works out from the teacher’s start date, ADAM can also determine the total amount of teaching experience that a teacher has.

The **Login name** is an important field. This is the username that the teacher will use to log in to ADAM. If you are using an external authentication mechanism such as an Active Directory Server (see page ), then this username *must* match the username on that service. See also Staff Logins on page .

Finally, the **Authentication Method** tells ADAM how this user should log on. It is possible to have different teachers using different methods, if necessary. However, ADAM should choose, by default, the most common setting on your server when you add a new staff member.

You will also have the chance to add in an initial password for the user. This is only necessary if you are adding in a user that will use the **Internal Password** option. Remember that if the user uses Active Directory LDAP Authentication then their password is never stored in ADAM and ADAM asks that other service each time whether the password supplied by the user is correct.

### Custom Fields

If you have created any custom fields, please note that they will appear below this information in the next section.

### Finishing the process

Once you have entered all the information necessary for a staff member, simply click on the button at the bottom: “**Save information**”.

ADAM then confirms that the staff member was added, and offers you a set of links to carry on with: **Add another staff member**, **Edit another staff member**, a link to the new staff member’s profile, and a link to change their permission groups.

## Employment contracts

ADAM does not keep a simple “employed” or “not employed” marker against a staff member. It keeps a *list* of employment contracts, each one with a commencement date, an optional termination date, and a note. A staff member is treated as **current** when they hold a contract that has already started and has not yet ended.

This matters because being current is what gives someone access:

-   Only current staff members can log in. Somebody with no current contract is turned away at the login screen, even though their login name and password are still stored.
-   Only current staff members count as staff elsewhere in ADAM. They are the ones offered when a class is given a teacher, and the ones who appear in staff lists and in security group listings.

Because it is a list and not a switch, a staff member can leave and return, work a series of fixed-term contracts, or be signed up now for a post that only starts next term.

### Viewing a staff member’s employment history

Click on the “**Staff**” tab and, under the “**Staff Administration**” heading, click on “**Staff Info**”. Choose the staff member from the list, and then click on **Employment History**.

![The employment contract history of a staff member who has left, showing two concluded contracts and the link to add a new one](assets/screenshots/staff-information/staff-information-16.png)

The employment history of a staff member who has left the school.

Reading this screen:

-   The line just below the heading tells you whether ADAM treats this person as a current member of staff right now.
-   Each row is one contract. An **End Date** of *currently employed* marks the contract the staff member is working under now; where that contract has a known end, ADAM adds “set to end on” and the date. A contract that has not started yet reads *to be indefinitely employed*, or gives the date it is set to end.
-   Where there is more than one contract, the record that ADAM is currently using is emphasised in bold.
-   **Total Length of Service** adds together every period the staff member has worked, so a person who has left and returned keeps credit for their earlier service. Contracts that have not started yet are not counted.
-   The **Actions** column offers **edit**, **delete** and **terminate** for each contract. These are discussed below.

> [!NOTE]
> You need the permission “View staff sensitive information (staff\_info\_sensitive)” to see this page at all, and “Edit staff member (staff\_edit)” for the **Add new employment contract** link and the actions in the last column. Without the second permission the page is read-only.

### Staff who leave the school

If a staff member leaves the school, it is usually desirable that they should not be able to log in to ADAM anymore.

The way to stop this is simply to terminate their employment contract. Visit the staff member’s information page and click on **Employment History**:

![](assets/screenshots/staff-information/staff-information-05.png)

If there are multiple employment records, as appear in the screenshot above, one will be highlighted in bold. Click on the **terminate** option.

![](assets/screenshots/staff-information/staff-information-06.png)

Ensure that the termination date is accurate, and click on the button **Terminate employment** at the bottom of the screen. The date must be a real date on or after the contract’s commencement date; anything else is refused and you are returned to this screen.

If the termination date you enter is today or in the future, the contract stays current until that date has passed. ADAM re-checks employment records every hour, so access ends on the correct day without anybody having to remember to come back and do it. See [Cron Service](cron-service.md#cron-service) for more about these background checks.

At the moment a contract stops being current, three things happen:

-   Any sessions that the staff member has open are closed immediately. They do not keep working until they happen to expire.
-   Any browser they had marked as trusted for two-factor authentication is forgotten, so that a remembered device cannot be used to get back in.
-   Their security group memberships are left exactly as they were.

That last point is deliberate, and it is worth understanding. ADAM relies on the concluded contract to keep a past staff member out, rather than on stripping their permissions away. It is what makes re-engaging somebody straightforward — but it also means that adding a new contract restores every permission they used to have, at the moment the new contract starts. If somebody returns to a different post, check their group memberships as well. See [Security Administration](security-administration-for-staff.md#security-administration-for-staff).

### Re-engaging a staff member who returns

When a former staff member comes back, **do not add them again as a new staff member**. Doing so creates a second, unconnected record, and splits their service history, their documents, their change log and their past marks and comments across two people. Instead, add a new employment contract to the record they already have.

#### Step 1: Find the staff member

Former staff members are still in ADAM, but they are kept out of the way. In the drop-down lists used to choose a staff member — including the one on “**Staff Info**” — they appear at the bottom of the list, under a heading that reads **Previous Staff Members**:

![A staff drop-down list scrolled to the boundary between current staff and the section headed Previous Staff Members](assets/screenshots/staff-information/staff-information-19.png)

Past staff members appear under their own heading at the end of the list.

#### Step 2: Add the new contract

Open their **Employment History** page and click on **Add new employment contract**.

![The Add Employment Record screen, with fields for the commencement date, whether the appointment is indefinite, a termination date and notes](assets/screenshots/staff-information/staff-information-17.png)

-   **Commencement Date** is the day the staff member starts again. If you put a date in the future here, the staff member is only treated as current — and can only log in — from that date onwards. This is the safe way to prepare a return in advance.
-   **Indefinite Appointment** should be set to **Yes** for an open-ended appointment. When it is **Yes**, the **Termination Date** is ignored entirely.
-   **Termination Date** is only used when **Indefinite Appointment** is set to **No**, for a contract with a known end.
-   **Notes** are shown in the Notes column of the employment history, and are a good place to record the post or the reason.

Click on **Save Employment Record** to finish.

> [!NOTE]
> A contract cannot end before it begins. If you set **Indefinite Appointment** to **No** and give a **Termination Date** earlier than the **Commencement Date**, ADAM refuses to save the record and returns you to this screen with a message explaining why.

#### Step 3: Check the result

![The employment contract history of a returning staff member, showing a concluded contract, a current one, and a combined total length of service](assets/screenshots/staff-information/staff-information-18.png)

The same staff member’s history after a new contract has been added.

Both periods are now listed, the new contract is emphasised as the active one, and **Total Length of Service** covers both spells.

There is nothing else to switch back on. A staff member’s login name, authentication method and password are stored against the person and not against the contract, so they are all unchanged. They will be able to log in exactly as before, using the same login name, from the commencement date of the new contract. Because their trusted browsers were forgotten when they left, they will be asked for a two-factor code again the first time they log in.

Two things are worth checking on a return:

-   **Their personal details.** Contact numbers, addresses and qualifications may have changed while they were away. See [Online Staff Update Forms](#online-staff-update-forms) below for a tidy way to have them confirm their own details.
-   **Whether their information has been erased.** ADAM can be set to remove the personal information of past staff members after a period, using the setting **Delete personal information from past staff members**, found in “Site Settings” under “Data Management” in the “Data Retention” section. If a staff member returns after that period has passed, their personal details will have to be captured again. Their work in ADAM — marks, comments and assessments — is not affected.

### Overlapping contracts

Two contracts for the same staff member cannot cover the same dates, and ADAM will quietly adjust the records to prevent it. Most often this happens when somebody on an open-ended contract is given a new one: because the old contract has no termination date, ADAM closes it on the day before the new contract begins.

This is usually exactly what you want, but it does mean the dates you see afterwards may not be quite the dates you typed. Look over the employment history once you have finished making changes.

ADAM also removes a contract that ends before it begins, because such a period cannot be counted. New ones can no longer be created, but older databases may still hold some. To find them, click on the “**Staff**” tab and, under the “**Staff Administration**” heading, click on “**Staff data verification**”. Any staff member with such a contract is listed there, with a link to their employment history so that the dates can be corrected before the record is removed.

### Fixed-term contracts and renewals

When a fixed-term contract comes to an end and the staff member is staying on, you have a choice:

-   **Extend the existing contract.** Click on **edit** next to the contract and move the **Termination Date** out, or set **Indefinite Employment** to **Yes** to make the appointment permanent. Use this when it is really the same appointment continuing.
-   **Add a new contract.** Use **Add new employment contract**, starting the day after the current one ends. Use this when the terms have changed, or when there is a genuine break in service. The history then shows both periods separately.

![The Edit Staff Employment Record screen, with the commencement date, an indefinite employment option, a termination date and notes](assets/screenshots/staff-information/staff-information-21.png)

Editing an existing contract.

Take care to leave no gap when you intend none: a staff member with no current contract, even for a single day, cannot log in on that day.

### Deleting an employment record

The **delete** action is for records that were captured in error — a contract entered against the wrong staff member, or entered twice. It is **not** the way to record that somebody has left; use **terminate** for that, so that the history of their service is kept.

Deleting a record cannot be undone. Two further points are worth knowing:

-   Every staff member must have at least one employment record. If you delete the only one, ADAM immediately creates a replacement to take its place.
-   If you delete the record that is currently active, ADAM chooses one of the remaining records to become active instead.

### Finding current, past and future staff

Two lists on the “**Staff**” tab, under the “**Lists and Labels**” heading, are useful when you are working with employment contracts.

“**Staff scratch list by contract**” lists staff by the state of their contracts. Tick any combination of the three options:

![The staff scratch list by contract screen, offering past, current and future contract options](assets/screenshots/staff-information/staff-information-20.png)

-   **Past contracts (concluded)** finds everybody who has a contract that has already ended — the list to use when you are looking for a former staff member.
-   **Current contracts** finds the staff employed today.
-   **Future contracts (not yet started)** finds staff whose contracts begin at some point in the future, which is a useful check after preparing returns or new appointments in advance.

“**Historical staff scratch list**” asks you for a date and then lists the staff who were employed on that day.

See [Scratch Lists](scratch-lists.md#scratch-lists) for what you can do with a list once you have made one.

## Staff security permissions

Please see [Security Administration](security-administration-for-staff.md#security-administration-for-staff)

## Online Staff Update Forms

In order to keep staff information up to date, many schools resort to giving staff the permissions to edit staff information. This is not advised since all staff then have the permissions to edit, and see, any other staff member’s personal details.

ADAM offers an online update form for staff, very similar in function to the [parent detail update forms](family-detail-updates.md#online-detail-updates). The staff member does the typing, and nothing they type reaches the database until somebody has approved it.

> [!WARNING]
> Staff must have the necessary permission to update their information. In the staff permissions, the permission can be found in the “Staff Admin” section, called “Edit personal information (staff\_edit\_own)”.
>
> ADAM checks this for you. Staff without the permission are left off the request list, and a note above the list says how many were left out. If you need to include somebody, give them the permission first and they will appear.
>
> Staff who are already carrying a request when the permission is taken away are simply not prompted until it is given back. Nothing is lost, and their request is still waiting.

A request to update is called a **trigger**. Once a staff member has been asked, ADAM interrupts them the next time they open the ADAM home page and puts the update form in front of them, and it keeps doing so until they submit it. They also receive a reminder email, so a member of staff who rarely logs in is not left out.

There are four steps in the process:

1.  Ask the selected staff members to update their information.
2.  ADAM prompts each of them at their next sign-in, and emails them a reminder.
3.  They check their details, change what has changed, and save the form.
4.  An email goes to an administrative contact, who approves the changes before they reach the database.

### Setting up ADAM:

Before you begin, please make sure that ADAM has been configured with the email address of the person who will be responsible for verifying and approving this information. This is configured in “[Site Settings](changing-site-settings.md#changing-site-settings)” under “**Data Management**”, in the “**Detail Updates**” section.

Add in one or more email addresses (separate them with commas if you have more than one) into the block for “Staff Detail Update Mail Recipients”:

![](assets/screenshots/staff-information/staff-information-08.png)

Save the site settings!

The site administrator’s address is always included as well, so this setting adds to that list rather than replacing it. Notifications to reviewers are only sent if **Enable internal email** — in “Site Settings” under “**Communications**” — is set to **Yes**.

### Choosing which form staff are asked to complete

If you do nothing here, ADAM uses its standard staff update form and everything below works as described. Read this section only if you want staff to be asked for a particular set of fields, or if you want ADAM to re-ask them at regular intervals without anybody remembering to.

Which fields appear on the form is decided by an **update profile**. Profiles are managed at **Administration → Database Administration → Manage Detail Update profiles**, and the screen is described in full under [Configuring an update profile](family-detail-updates.md#configuring-an-update-profile). Three of its settings matter for staff:

-   **Entity** must be set to **Staff**. A profile created for **Families** is never offered to staff. The entity is chosen when the profile is created and cannot be changed afterwards.
-   **Primary Form** is the form staff will see.
-   **Update cadence** decides whether ADAM re-asks on its own. Choose anything from *Every 2 months* to *Every 24 months* and an overnight job re-flags every current staff member who has never completed that profile, or whose last completed update for it is older than the cadence. Choose *No forced updates* and staff are only ever asked when somebody asks them.

> [!NOTE]
> The **Audience** and **Default for Audience** settings on that screen belong to the family flows. Nothing on the staff side reads them, so leave them as you find them.

The overnight job skips anybody who already has an open request, and anybody whose last submission is still sitting in the review queue, so a staff member is never asked twice for the same thing. It sends no reminder email — the assumption is that a member of staff logs in often enough to be prompted.

### Asking staff to update their details

Click on the “**Staff**” tab and, under the “**Staff Administration**” heading, click on “**Request staff detail updates**”. A list of current staff is shown, with everybody ticked. Untick anybody who should not be asked.

Only staff who are able to update their own details are listed — see the permission note above. If any have been left out, ADAM says so above the list.

![](assets/screenshots/staff-information/staff-information-22.png)

If your school has more than one active staff update profile, an **Update Profile** drop-down appears above the button so that you can choose which form the selected staff will be given. With one profile, or none, there is nothing to choose and no drop-down is shown.

Click on **Request updates from selected staff**. ADAM confirms the request — naming the profile, where one was used — and each selected staff member receives a personalised copy of the following email:

![](assets/screenshots/staff-information/staff-information-10.png)

> [!WARNING]
> Two permissions are needed to use this screen. “Produce Staff Information Forms (staff\_infosheet)” in the “Staff Admin” section opens the page, and “Email details update forms (detailupdate\_email)” in the “Family Admin” section puts the button on it. A user with only the first sees the list of staff and no way to submit it.

### Updating the Information:

The next time the staff member opens the ADAM home page, ADAM does not show it. It shows the update form instead, headed **Update Staff Details**, with their name card above it and their current information already filled in. The menu tabs are deliberately hidden: the page has two ways out and no others, and both sit together at the foot of the form.

![](assets/screenshots/staff-information/staff-information-23.png)

-   **Save information**, at the foot of the form, submits the changes. They are not written to the database — they are held for approval, and an email goes to the addresses configured above. A message thanks the staff member and returns them to the ADAM home page.
-   **Skip for now**, beside the Save button, puts the prompt off. Nothing is recorded and the request stays open: ADAM stops asking until the staff member closes their browser, and prompts them again in their next browser session.

A staff member who has been asked more than once — two profiles, say — works through the requests one at a time, oldest first. Each save clears one request and the next sign-in raises the next.

> [!NOTE]
> A staff member has only one submission waiting for approval at a time. If they submit the form again before anybody has reviewed the first one, the newer submission replaces the older one.

#### Updating without being asked

Staff do not have to wait to be asked. At any time they can click on the “**Staff**” tab and, under the “**Staff Administration**” heading, click on “**Update your personal information**”. The form is the same, and the changes are held for approval in exactly the same way:

![](assets/screenshots/staff-information/staff-information-11.png)

> [!NOTE]
> Updating this way does **not** clear an outstanding request. A staff member who has been flagged, and who then updates from the menu, will still be prompted at their next sign-in. Only the prompted form clears the request.

#### Confirming your identity before editing

The update form shows a staff member their own personal details — contact numbers, addresses, and banking information where the school’s form includes it — and then lets them be changed. A browser left open at a desk is enough to reach it, so ADAM will not open the form on a session that has been signed in for a while. It asks for the password again first.

ADAM counts a session as recent for **ten minutes** after signing in, or after any other point at which the password was confirmed. This matters more than it sounds, because requests are usually raised overnight and so reach most staff in the middle of the working day rather than at sign-in.

-   **Reaching the form.** A staff member whose session is older than that sees a short page in place of the form, headed **Update Staff Details**, offering **Confirm your identity** and **Skip for now**. Skipping stays free: putting the prompt off records nothing, so it never needs a password. Choosing to confirm asks for the password, and the one-time PIN as well for anybody enrolled in [two-factor authentication](two-factor-authentication.md#two-factor-authentication), and then opens the form.
-   **Saving the form.** The ten minutes can also run out while the form is on screen, which is easily done on a long form. ADAM then shows a page headed **Confirm your identity**. Fill in the **Password** — and the **One Time PIN**, where enrolled — and click on **Confirm and save**. Everything typed into the form is carried across and saved with it.

![](assets/screenshots/staff-information/staff-information-24.png)

The **One Time PIN** field is only shown to staff enrolled in two-factor authentication; the picture above is of a staff member who is not.

A wrong password returns the same page, with the changes still intact, and the message *“That password was not correct.”* Too many wrong passwords in a row are refused for a few minutes. Passwords entered here are counted separately from the ones entered at the login screen, so fumbling a password at this prompt can never lock a staff member out of ADAM itself. A wrong **One Time PIN** is treated differently — it counts against the same allowance as the one-time PIN at sign-in, because it is a guess at the same secret.

> [!WARNING]
> Staff who sign in only with a [passkey](passkey-authentication.md#passkey-authentication), or through Google or Microsoft, may never have needed a password and may not know one. They can still use **Skip for now** to put the prompt off, but they will not be able to save the form. If this affects somebody at your school, make sure they have a working password for the authentication method their record uses — see [Staff Passwords](staff-passwords.md#staff-passwords) — before asking them to update their details.

### Approving the Information:

ADAM will send the following email to the specified email addresses when a staff member updates their information:

![](assets/screenshots/staff-information/staff-information-12.png)

If they click on the link, or - from the ADAM menu on the “**Staff**” tab under the heading “**Staff Administration**”, click on the option “**Review submitted changes**”

A list of unapproved changes will be displayed:

![](assets/screenshots/staff-information/staff-information-13.png)

Clicking on the option to “review changes” will show the information that was changed and allow the reviewer to make further changes to that information:

![](assets/screenshots/staff-information/staff-information-14.png)

Changes can also be ignored completely by setting “Approve Change” to “No”.

Click on “Save changes” when done. The changes are now recorded in the system.

Note that in the change log, the reviewer will be recorded as the person making those changes.

## Staff Medical Records

Staff have medical records in the same way that pupils do, although only consultations are kept for them. A staff member with the right permission sees a **Medical Records** section on a colleague’s profile, holding a **Consultations** tab where sick bay visits are recorded and viewed. See [Medical Records for Staff](medical-module.md#medical-records-for-staff) for how this works and which permissions it needs.

This is separate from sick leave, which is recorded in the [Leave Module](leave-module.md#leave-module).

## Staff Signatures for Reports

Many report templates allow for the automatic placement of electronic signatures. Each teacher will need a signature scanned and uploaded onto the ADAM. Please see the section in [Report Publishing](report-publishing.md#staff-signatures) for more information.

## Staff Name Pronunciation

ADAM can hold a short recording of how a staff member’s name is said. Once one exists, a media control appears on the name card in their profile and users can click it to listen to the name.

![](assets/screenshots/staff-information/staff-information-15.png)

The simplest way to provide one is to **record it in the browser**. Every staff member has a **Name Pronunciations** tab on their own profile, which plays the current recording and offers a recorder; a name recorded there is audible straight away. See [Name Pronunciations](name-pronunciations.md#name-pronunciations) for the whole feature.

Alternatively, upload an audio file into the “Name Pronunciation” category of the staff member’s Document Repository.

If multiple files are uploaded, only the most recent file is played when the button is clicked.

If the button is greyed out, it may be because an invalid audio file has been uploaded or the specific browser does not support the playback of that type of file. You are encouraged to upload files in MP3 format for the widest possible support.

> [!NOTE]
> Note that different web browsers may display the media control buttons differently. This is a function of the web browser rather than of ADAM.

Have a look at the Document Repository documentation for more information on uploading many files at once using the [Bulk Upload feature](document-repository.md#uploading-documents-in-bulk).
