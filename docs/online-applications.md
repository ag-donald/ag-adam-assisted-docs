# Online Applications

## How Does It Work?

ADAM has an online application facility which allows parents to complete their enrolment information forms online and have those directly included in the ADAM database without any manual data capture.

ADAM provides a similar data capture form that staff would normally use to add a new pupil. However, this [can be customised](database-field-management.md) to have custom fields included if necessary. Applicants can submit their and their children’s details onto ADAM.

All online applicants are manually screened first to ensure data quality and eligibility (e.g. girls into a boys school) and to fix minor errors.

If the school chooses to collect supporting documents (such as birth certificates or past school reports), parents can upload these as a step *within* the application itself, before it is submitted. When the application is approved, any documents that were uploaded are filed automatically into the document repository against the new pupil and family. Parents can still also upload further documents after approval through the [Parent and Pupil Portal](parent-and-pupil-portal.md#parent-and-pupil-portal).

### High-level Overview

The following steps provide an overview of the process for both parents and staff. Included below are links to more specific information that might be required to set up or manage the step or process described.

#### Step 0:

The school sets up the online application process. This includes:

1.  Customising the [application form](#customising-the-application-form)
2.  Customising the [application notification emails](#communication-from-the-online-application-module)
3.  Setting up any [supporting documents to collect during the application](#collecting-supporting-documents-during-the-application) and marking which are required
4.  Enabling the [application form and notifications](#setting-up-online-applications) in site settings

#### Step 1:

Parents visit the online application form and submit their ID or passport number, email address, contact telephone number and the number of children they are applying for. Everybody sees the same form and the same reply, so the screen never reveals whether an ID number already belongs to a parent at the school. ADAM emails a link that starts the application. If the ID number belongs to an existing parent, that link goes to the email address the school already holds for them, rather than to the address just typed in — so no third party can use somebody else’s ID number to reach their family’s details.

#### Step 2:

After submitting their details, the parent receives an email containing a link that is valid for 24 hours. Clicking it shows them their details to check, and nothing is created until they click **Start Application**. ADAM then creates the application, emails them a second link to the application form itself, and takes them straight to it. If the school has set up [online agreements](online-agreements.md#online-agreements) for the **Admissions Parents** audience, applicants are first asked to read and respond to each outstanding agreement before the application form is shown. The parent will be asked to complete the application form with both their and the applicant child’s information.

Some parents never click the link. The school can still see these parents in the [**Unconfirmed Applications**](#unconfirmed-applications) table, and the [status email](#online-application-status-email) lists those who have waited more than a day.

If the family already exists in ADAM, only the child’s information is requested. No password is asked for at any point during an application. Parents who already use the portal can log in first instead and start the application from there, without waiting for an email.

Parents complete the form one page at a time — their own details first, then a page for each child — and can save any page and come back to it later, even if some of it is still empty. Required information is only insisted on when they submit the application.

#### Step 3:

Once completed, parents finalise and submit their application. No further changes are possible to that application form from this point.

Internally, the school’s designated contacts are notified that a new application has been received.

#### Step 4:

The application form is reviewed. The school has the option to “Accept” or “Reject” the application form. This does not *enrol* the pupil to the school. If accepted, the pupil and the family - if they don’t already exist - are added to the database as *applicants* and ADAM can then manage them further.

If the application is rejected, the information is not added to the database and will remain in a list of rejected applicants for a period of 30 days before all information related to that application is deleted.

Any applicant is only searchable from the “Pupil Info” page and will only appear in the list of applicants once the application form has been accepted.

A real world analogy to this process is having a parent fill out a paper form. The form is handed to you. If the form is filled in correctly, you add the form to your list of applicants (i.e. you “accept” the application). If the form is filled out incorrectly, or perhaps they’ve applied for a boy to attend a girls-only school, then you throw the application form in the bin (i.e. you “reject” the application form). Nothing about accepting or rejecting the application form implies anything about whether a future place will be offered to the applicant or not.

#### Step 5:

At the point that the application is accepted or rejected, ADAM can send out an optional email to notify parents thereof. This email would include further information such as the need to pay a deposit, perhaps.

We strongly recommend enabling and customising the acceptance email, but we strongly recommend not using the rejection email at all.

> [!WARNING]
> An application can be rejected for hundreds of reasons, and it seems improper to send a generic rejection mail out when there are either material or minor issues with the application. One example is a duplicated application where the parents applied twice: one might accept one and reject another. They would receive confusing messaging and perhaps be unaware that they had a valid application that was being considered. In these cases, we strongly suggest that schools respond directly to the applying parents directly to address any issues that might have arisen.

#### Step 6:

Once the application is accepted, the pupil is added to the database in the default application status of “Applicant”. This is a generic status that every new pupil added to the database is added to. Based on the progress of the application, the pupil can be moved to different statuses to indicate this progress.

The pupils would typically end up in one of two broad categories of applicant: “confirmed enrolment” or “not to be enrolled”. The latter is general and schools might prefer different subcategorisations such as “application withdrawn,” “position not offered,” or even “application deferred” (i.e. a waitlist).

## Setting up Online Applications

### Checking your site settings

There are a few things that need to be checked first. In the [Site Settings](changing-site-settings.md#changing-site-settings), check the following settings:

-   **Admissions / Online Applications:**

    -   **Online Applications Recipients:** Enter an email address or a comma-separated list of email addresses of people who will be notified when an online application has been received by the school. The same people receive the [status email](#online-application-status-email) each weekday morning.
    -   **Enable online applications:** Ensure that this is set to “Yes” to allow parents access to the application form.
    -   **Expire applications (days):** This setting will automatically expire and eventually remove incomplete applications. These are applications that were started, but never submitted to the school for consideration. The default setting is 7 days, but some schools have it as low as 2 or 3. Ask yourself how long it should take a person to complete this information. ADAM also keeps the details of parents who never clicked the emailed link for this many days, so that they appear in the [**Unconfirmed Applications**](#unconfirmed-applications) table.

-   **General / Site Settings:**

    -   **URL for external access:** Ensure that this matches the address that you normally type in to get to ADAM. Note that this setting might not be configurable on some servers and a message will appear saying “Set in the configuration file.” If this is the case, you can carry on!

Don’t forget to save the settings when you’ve updated them!

The wording parents see at each stage is also yours to change. In the same settings screen, under the **Admissions** category and the **Online Applications** heading, **Collect ID Number** and **Collect Email Address** are the two messages shown above the opening form, **Confirmation of Email** is the message shown once the form has been submitted, **Confirm Submitting** is shown above the submit button on the review screen, and **Receipt of Application** is shown after the application has been submitted to the school. The default wording of **Collect ID Number** no longer promises existing parents a login step, because there is no longer one; if your school has customised that message, ADAM has left your version alone, so it is worth re-reading it for any promise it still makes about logging in.

### Customising the Application Form

ADAM has four different data capture screens for each of families and pupils. These are:

-   Adding a new family/pupil: this is done internally by staff when a new pupil is added.
-   Editing a family/pupil: this is done internally by staff when information changes.
-   Applying: this is done *externally* by a parent applying for a position at your school.
-   Updating: this is done *externally* by a parent updating their contact details.

Each of these screens can be customised, within reason, to show only the fields that are required.

On the application forms you can also ask a question only when it applies — for example only for the grades a question is about, or only when the parent says the child needs a study permit. Give the field a [**Show when** rule](database-field-management.md#show-when-rules). A field that a rule hides is not required, and any answer typed into it is discarded when the parent saves the page.

Spend a moment deciding which fields are necessary for an application form. Our advice is to be conservative in what you ask for. Remember that with the introduction of the Protection of Personal Information Act, it will be an offence to store information unnecessarily.

The most important fields are, from ADAM’s point of view:

-   Families:
    -   Primary parent’s names
    -   Primary parent’s ID number
    -   Primary parent’s email address
    -   Primary parent’s cell number

-   Pupils:
    -   Pupil’s names
    -   Pupil’s ID number
    -   Pupil’s grade and year of entry (these fields appear differently after the pupil has been added, as “date of entry” and “grade 12 year”.

Anything more than this is, strictly speaking, not required for ADAM’s functionality. Other information is certainly required, as mentioned, later in the process once the child has been admitted to the school.

If you would like to add in fields which are not part of ADAM’s default setup, then please read up about adding [custom fields](database-field-management.md#managing-custom-database-fields).

### Collecting Supporting Documents During the Application

You can ask parents to upload supporting documents — such as a birth certificate, proof of residence, or past school reports — as part of completing their online application, rather than waiting until after the application has been approved. Any documents uploaded this way are held against the application and filed automatically into the document repository when the application is approved.

These document requests are configured in the same place as all other parent and pupil uploads. Navigate to **Administration → Document Repository → Manage parent and pupil uploads**, and create an upload whose **Audience** is set to **Applicant**. Each file you add to that upload becomes a slot that applicants will see during their application.

When configuring the slots, the **Requirement** column controls how strongly each document is enforced for applicants: **Optional** (no badge, never enforced), **Requested** (shown with a “Requested” badge; the parent is warned if it is still missing but can still submit), or **Mandatory** (shown with a red “Required” badge; the application cannot be submitted until it is uploaded). See [Creating Upload Spaces](document-repository.md#creating-upload-spaces) for the full explanation of the three levels, including what changed if your school has upgraded from an earlier version of ADAM.

Each slot also has an **Accepted Types** column, where you tick which kinds of file may be uploaded — such as **PDF document** or **JPEG image**. Applicants can only upload a file whose type you have allowed, and the accepted types are shown to them next to each slot. Every slot must have at least one type ticked before the upload can be saved.

The full set of options for creating these uploads — audience, document scope (per family or per child), descriptions, maximum file size, the file types each slot accepts and the document repository category each document is filed into — is described under [Parent Uploads into the Document Repository](document-repository.md#parent-uploads-into-the-document-repository).

If the school has not configured any **Applicant** uploads, the document step is skipped entirely and parents move straight from their details to the review screen.

### Finding the address of your Application Form

There are a number of steps that need to be considered before opening up your online application portal. The application portal is easy to find. You can link to it either from your website or by sending parents and email link. The application form can be found by simply adding “apply” to the end of your ADAM address. For example:

https://demo.adam.co.za**/apply**

### Communication from the Online Application Module

During the application process, ADAM always sends two emails: the link that starts the application, and, once the parent has confirmed their details, the link to the application form itself. There are three other emails that can be sent out, but each of these must be enabled before they will be sent:

1.  **Confirmation of receipt of application form:** This email is sent at the end of the application process once they have clicked on the “Submit Application” button at the end of their application procedure.
2.  **Application approval:** When the school accepts the application by “approving” it, an email can be sent to parents with further steps. This may include instructions for paying a deposit and for [uploading documents into ADAM](document-repository.md#parent-uploads-into-the-document-repository).
3.  **Application rejection:** When the school rejects an application, an email can be sent to parents with further information. Note that we do not recommend that this feature be used since the email, apart from general customisation below, cannot be tailored to provide reasons why the application was rejected. Given that there are so many reasons that one might decide to reject an application, we strongly recommend personalised communication to parents in this regard.

The contents of the emails that ADAM sends [can be customised](email-message-templates.md#email-message-templates).

![](assets/screenshots/online-applications/online-applications-01.png)

In the “**Applications**” section, you will find the emails that are relevant here. Three of them carry a link, and it is crucial that each one keeps its “{link}” or “{button:…}” code, or parents will have no way to continue.

-   **Start an Application** is sent to the address a parent types on the application form when that ID or passport number is not one ADAM recognises. It carries the link that starts the application.
-   **Start an Application (Existing Parent)** is sent instead when the ID or passport number belongs to a parent ADAM already knows, and it goes only to the email addresses the school holds for that parent. It tells them that somebody asked to start an application using their ID number and that they can ignore the email if it was not them. Keep that reassurance in the wording if you customise it, because the person receiving it may not be the person who filled the form in.
-   **New Application** is sent once the parent has confirmed their details, and it carries the link to the application form. Parents use this email to return to a part-completed form, so it is the one they need to keep.
-   **Notify Parent of Application Approval** is used when the application is approved. Edit this template to give the parent information for appropriate next steps.
-   **Notify Parent of Application Rejection** is used when the application is rejected. We strongly discourage the use of this email template and suggest that schools make direct contact with parents.
-   **Notify Parent of Application Submission** is sent to parents when they click on the final button to submit their application.
-   **Notify School of Completed Application** is used to notify a member of staff at the school that a new application form is waiting for acceptance of rejection.
-   **Online Application Status (to Staff)** is the [status email](#online-application-status-email) that the school’s recipients receive each weekday morning.

Because you are customising the template for your school, you do not have to make use of the other codes that are provided.

The three additional emails are enabled via the site settings. Under the **Admissions** tab, look for the section on **Online Applications**. The three settings that control the three emails are shown below:

![](assets/screenshots/online-applications/online-applications-02.png)

Change the relevant settings to “Yes” where you’d like ADAM to send the emails.

Note, again, that we **do not recommend that the Rejection email is sent automatically** and rather suggest that schools engage directly with the applicants in this regard.

### Testing the Application Form

Once you have completed the steps outlined above, you are encouraged to complete the application form to ensure that you are happy with its content. To do this, follow the [instructions for parents](#the-application-process-procedure-for-parents) below.

Once the application process has been completed, you will need to put on your “staff member” hat in order to finalise the admission. More of this is provided in the [instructions for staff](#application-process-procedure-for-staff) below.

## Online Application Reminder Emails

### Overview

The Online Application Reminder Emails feature automatically sends reminder emails to parents who have incomplete online applications. This helps improve application completion rates by gently prompting parents to finish the admissions process.

The system sends reminders for two types of incomplete applications:

1.  Not Started - Parents who confirmed their email address but never began filling out the application form
2.  Incomplete - Parents who started the application but haven't submitted it yet

Reminders are sent on a configurable schedule and stop automatically when the maximum number of reminders has been reached or when the application link is about to expire.

### Enabling the Feature

To enable automatic reminder emails:

1.  Go to **Administration → Site Administration → Edit site settings**
2.  Navigate to the **Admissions** category
3.  Set **Enable Reminder Emails** to Yes

When disabled, no reminder emails will be sent regardless of other settings.

![](assets/screenshots/online-applications/online-applications-03.png)

### Configuration Settings

There are four settings that control how reminders work:

#### Enable Reminder Emails

-   Setting name: Enable Reminder Emails
-   Options: Yes / No
-   Default: No

This is the master switch for the feature. Set to "Yes" to enable automatic reminders.

#### Days for Not Started Reminders

-   Setting name: Days for Not Started Reminders
-   Default: 3,7,14

This controls when reminders are sent to parents who requested an application but never started filling it out. The days are counted from when the parent first requested the application.

Example: With the default setting of 3,7,14, a parent will receive reminders:

-   3 days after requesting the application
-   7 days after requesting the application
-   14 days after requesting the application

#### Days for Incomplete Reminders

-   Setting name: Days for Incomplete Reminders
-   Default: 5,10,15

This controls when reminders are sent to parents who started an application but haven't submitted it. The days are counted from when the parent last saved their progress.

Example: With the default setting of 5,10,15, a parent will receive a reminder:

-   5 days after they last saved the application
-   10 days after they last saved the application
-   15 days after they last saved the application

#### Maximum Reminders per Application

-   Setting name: Maximum Reminders per Application
-   Default: 3

This limits the total number of reminder emails sent for a single application. Once this limit is reached, no more reminders will be sent, even if additional reminder days are configured.

Example: If set to 3, each application will receive at most 3 reminder emails total, regardless of whether they are "not started" or "incomplete" reminders.

### Understanding the Day Sequence

The day settings accept a comma-separated list of numbers. Each number represents how many days after the relevant date a reminder should be sent.

#### Format

-   Use whole numbers only (e.g., 3, 7, 14)
-   Separate multiple days with commas (e.g., 3,7,14)
-   Spaces around commas are optional (e.g., 3, 7, 14 works the same as 3,7,14)
-   Days do not need to be in order, but listing them in ascending order is recommended for clarity

#### Examples

|**Setting**|**Meaning**|
|-----------|-----------|
|3|Send one reminder on day 3|
|3,7|Send reminders on days 3 and 7|
|3,7,14,21|Send reminders on days 3, 7, 14, and 21|
|1,2,3,5,7|Send reminders on days 1, 2, 3, 5, and 7 (more frequent early reminders)|

#### How the Base Date Works

-   Not Started reminders: Days are counted from the date the application was first requested
-   Incomplete reminders: Days are counted from the date the application was last saved

If a parent saves their application, the incomplete reminder countdown resets. For example, if reminders are set for days 5, 10, and 15, and a parent saves on day 4, the next reminder would be 5 days from that save date.

### Email Templates

Two email templates are used for reminder messages. To customise them, click on the **Administration** tab, then under the **Site Administration** heading, click on **Manage email messages**. The templates are in the **Applications** section.

#### Reminder: Application Not Started

This template is used for parents who haven't begun their application form.

**Available merge codes:**

| Merge Code | Description |
|------------|-------------|
| `{school}` | The name of your school |
| `{requestdate}` | The date the application was requested |
| `{daysremaining}` | Number of days until the application link expires |
| `{childcount}` | Number of children on the application |
| `{link}` | The URL to the application form |
| `{button:Text}` | A clickable button linking to the application (e.g., `{button:Start Application}`) |

#### Reminder: Application Incomplete

This template is used for parents who started but haven't submitted their application.

**Available merge codes:**

|Merge Code|Description|
|----------|-----------|
|`{school}`|The name of your school|
|`{greeting}`|Parent/guardian name if available, or a default greeting|
|`{children}`|Names of children on the application|
|`{daysremaining}`|Number of days until the application link expires|
|`{link}`|The URL to the application form|
|`{schoolphone}`|The school's phone number|
|`{button:Text}`|A clickable button linking to the application (e.g., {button:Complete Application})|

### Expiry Protection

The system automatically protects against sending reminders for applications that are about to expire or have already expired.

#### How It Works

-   Reminders are only sent for applications where the link has not yet expired
-   The {daysremaining} merge code shows parents how many days they have left
-   Once an application expires, no further reminders are sent

#### Application Expiry Setting

The application expiry period is controlled by a separate setting, **Expire applications (days)**. It is in the site settings on the **Admissions** tab, under the **Online Applications** heading. The default is 7 days.

When planning your reminder schedule, ensure your last reminder day is well before the expiry period. For example, if applications expire after 30 days, setting reminders for days 3, 7, and 14 gives parents at least 16 days to complete their application after the final reminder.

### Best Practices

#### Recommended Settings

For most schools, the default settings work well:

-   Not Started reminders: 3, 7, 14 days
-   Incomplete reminders: 5, 10, 15 days
-   Maximum reminders: 3

#### Tips for Effective Reminders

1.  Don't send too many reminders - Excessive emails may annoy parents. Three reminders is usually sufficient.
2.  Space reminders appropriately - Allow enough time between reminders for parents to respond. Sending reminders on consecutive days may seem pushy.
3.  Start reminders early - The first reminder should come before parents might forget about their application. Day 3 is a good starting point.
4.  Leave room before expiry - Ensure your final reminder gives parents adequate time to complete the application before it expires.
5.  Customise your templates - Personalise the email templates to match your school's tone and include any specific instructions parents might need.
6.  Include clear calls to action - Use the {button:Text} merge code to create prominent, clickable buttons that make it easy for parents to access their application.

### Frequently Asked Questions

#### When are reminders sent?

The reminder system runs automatically every 6 hours. When a reminder is due (based on the configured days), it will be sent during the next run.

#### Will parents receive reminders after they submit their application?

No. Once an application is submitted, it is no longer considered "incomplete" and no further reminders are sent.

#### Can I see which applications have received reminders?

Yes. In the online applications list, you can see the reminder count for each application. The database tracks both the number of reminders sent and the date of the last reminder.

#### What if a parent saves their application - does that reset the reminders?

Yes. For "incomplete" applications, the reminder countdown is based on the last save date. If a parent saves their application, the days are counted from that new date. Saving any single page of the application counts as a save.

#### Can I manually send a reminder to a specific applicant?

The automatic system does not support manual triggering. However, you can contact individual applicants directly through the online applications interface.

#### Will reminders be sent during school holidays?

Yes, the automatic reminder system runs continuously regardless of term dates or holidays. If you wish to pause reminders during certain periods, you can temporarily set Enable Reminder Emails to "No".

## Online Application Status Email

### Overview

Each weekday morning, ADAM sends a summary of online applications to the people listed in **Online Applications Recipients**. The email says how many applications have arrived, and it lists the parents who may need a phone call: parents who never clicked the link ADAM emailed them, and parents whose application will soon expire. The email does not change anything in ADAM.

ADAM sends the email only when all of these are true:

-   **Enable online applications** is set to “Yes”;
-   **Send Daily Status Email** is set to “Yes”, which is the default;
-   **Online Applications Recipients** holds at least one email address.

To stop the email, see [Stopping the Email](#stopping-the-email). Every recipient receives the same email. If there is nothing to report — no new applications, no parents who have not clicked their link, and no applications close to expiry — ADAM does not send an email that day.

### What the Email Contains

The email opens with three numbers:

-   **new:** the applications that parents started since the previous email was due, together with parents who gave their details in that time but have not yet clicked the link. Monday’s email therefore covers the weekend. An application counts as new even if the parent has already submitted it. If more than four days have passed since the previous email was due, the count covers only the last 72 hours.
-   **not confirmed:** parents who gave their details on the application form, but who had still not clicked the emailed link after 24 hours.
-   **expiring:** applications that have not been submitted and that will expire within 3 days.

![A status email with the subject “Online applications — Friday 30 October”, the counts 4 new, 3 not confirmed and 4 expiring, a list of three parents whose link was not clicked, a list of four applications expiring within 3 days, and the Manage online applications button](assets/screenshots/online-applications/online-applications-21.png)

Below the numbers are two lists. A list that has nobody in it is left out of the email.

**Link not clicked after 24 hours** lists the parents counted as not confirmed, newest first. It shows each parent’s **Email**, **Phone**, the number of **Children** and how long ago their details were **Submitted**. These are the same parents shown in the [**Unconfirmed Applications**](#unconfirmed-applications) table. Their link has expired, so a parent who still wants to apply must start again on the application form.

**Expiring within 3 days** lists the applications counted as expiring, with the soonest expiry first. It shows:

-   **Family / children:** the family name and the children’s names, or the parent’s email address if the parent has not yet entered any names;
-   **Phone:** the contact telephone number;
-   **State:** “nothing captured” if the parent has not saved any page of the form, or “captured, not submitted” if they have;
-   **Expires:** how long is left before the application expires;
-   **Reminders:** “none”, or how many [reminder emails](#online-application-reminder-emails) ADAM has sent the parent, with the date of the last one — for example “2 (27 Oct)”.

Each list shows at most 15 parents. When there are more, the last line of the list says how many more there are, for example “… and 4 more”. A parent appears in only one of the two lists: a parent who already has an application that is not yet submitted is not listed as not confirmed, even if they also asked for a new link.

Every telephone number in the lists is a link, and so is every email address in the **Link not clicked** list, so you can call or write from the email. The **Manage online applications** button at the bottom opens the [list of applications](#application-process-procedure-for-staff) in ADAM.

### When the Email Is Sent

By default, the email is sent on Monday to Friday at 07:00.

ADAM sends the email from its scheduled tasks, which run every few minutes (see [Cron Service](cron-service.md#cron-service)). The email therefore arrives a few minutes after the time you set. If the scheduled tasks are not running at that time, the email goes when they next run. If they miss several send times, ADAM sends one email when they start again, and its **new** count covers the time since the previous send time, as described above.

After ADAM is updated to include this email, the first run of the scheduled tasks only notes the time; it sends nothing. The first email goes at the next send time after that, and it covers the time since the update.

To change the days or the time, click on the **Administration** tab, then under the **Site Administration** heading, click on **Edit site settings**. On the **Notifications & Scheduling** tab, under the **Online Application Status** heading, change:

-   **Days on which to send the status email**
-   **Time at which to send the status email**

Then click on **Save settings**.

### Stopping the Email

In the site settings, on the **Admissions** tab under the **Online Applications** heading, set **Send Daily Status Email** to “No” and click on **Save settings**. ADAM stops sending the status email. The **Notify School of Completed Application** email, which ADAM sends to the same recipients each time a parent submits an application, is not affected.

Do not use these other settings to stop the status email:

-   **Clearing Online Applications Recipients** also stops the status email. However, ADAM then sends the **Notify School of Completed Application** email to the address in **System Admin's Email** instead (on the **General** tab of the site settings, under **System Administration**). If that is empty too, nobody at the school is told when an application is submitted.
-   **Unticking every day** in **Days on which to send the status email** does **not** stop it. ADAM saves the empty choice, but then sends the email once every eight days instead, on whatever day of the week that falls.

### Changing Who Is Listed

The 24 hours and the 3 days in the lists above are both settings. In the site settings, on the **Admissions** tab under the **Online Applications** heading:

-   **Status email: hours before "not confirmed"** is how many hours after giving their details a parent who has not clicked the link is listed as not confirmed. The default is 24.
-   **Status email: days before expiry** is how many days before it expires an application that has not been submitted is listed as expiring. The default is 3. If you make this the same as **Expire applications (days)**, every application that has not been submitted will be listed every day.

### Changing the Wording

The wording of the email can be [customised](email-message-templates.md#email-message-templates) like the other application emails. Click on the **Administration** tab, then under the **Site Administration** heading, click on **Manage email messages**. The template is called **Online Application Status (to Staff)**, in the **Applications** section. Its default subject is “Online applications — {date}”.

ADAM builds the two lists itself and places them where the `{notconfirmedlist}` and `{expiringlist}` codes appear. Keep both codes in the template, or the lists will not appear in the email.

**Available merge codes:**

|Merge Code|Description|
|----------|-----------|
|`{school}`|The name of your school|
|`{date}`|Today’s date, for example “Friday 30 October”|
|`{newcount}`|The number of new applications since the previous email|
|`{notconfirmedcount}`|The number of parents who have not clicked the emailed link|
|`{expiringcount}`|The number of applications that will soon expire|
|`{notconfirmedhours}`|The value of **Status email: hours before "not confirmed"**|
|`{expirydays}`|The value of **Status email: days before expiry**|
|`{notconfirmedlist}`|The list of parents who have not clicked the emailed link|
|`{expiringlist}`|The list of applications that will soon expire|
|`{link}`|The address of the **Manage Online Applications** page|
|`{button:Text}`|A button linking to the **Manage Online Applications** page (e.g., `{button:Manage online applications}`)|

### Frequently Asked Questions

#### Why was there no email today?

One of these is the reason:

-   Today is not one of the days in **Days on which to send the status email**, or the time has not yet come.
-   There was nothing to report: all three numbers would have been zero.
-   **Enable online applications** or **Send Daily Status Email** is set to “No”, or **Online Applications Recipients** is empty.
-   ADAM’s scheduled tasks are not running. See [Cron Service](cron-service.md#cron-service).
-   ADAM was updated to include this email since the last send time. The first email goes at the next send time.

#### Why is a parent not in the email?

-   A parent who has not clicked the link is listed only once more than 24 hours have passed. Before that, they are only counted among the new applications.
-   A parent whose ID or passport number ADAM already knows is never listed as not confirmed. Their link went to the address the school already holds.
-   A parent who has started an application is not listed as not confirmed. Their application is listed only when it will expire within 3 days, and not after it has been submitted or has expired.
-   A parent who gave their details longer ago than **Expire applications (days)** has been removed.
-   Each list shows at most 15 parents; the rest are counted in the “… and 4 more” line.

The [**Unconfirmed Applications**](#unconfirmed-applications) table explains who it leaves out, and the email follows the same rules.

## The Application Process: Procedure for Parents

Generally, schools will link through to the application form in ADAM from their website, or perhaps and email. Simply add on “apply” to the end of your ADAM URL for the correct address to visit:

E.g. https://demo.adam.co.za**/apply**

Everybody starts on the same short form, whether or not the school already knows them. Parents fill in **Your ID or Passport Number**, their **Email Address**, **Confirm Email Address**, a **Contact Telephone Number** and the **Number of Children Applying**, then click **Next**:

![](assets/screenshots/online-applications/online-applications-04.png)

Parents who already use the parent portal can click **Already use the parent portal? Log in first.** beneath the form and begin from there instead — see [Starting from the parent portal](#starting-from-the-parent-portal) below.

ADAM then thanks them and tells them that a link is on its way, that the application must be completed within the number of days set in **Expire applications (days)**, and that the link is valid for 24 hours. This screen is the same for everyone.

![](assets/screenshots/online-applications/online-applications-05.png)

Where that email goes, however, depends on the ID or passport number:

-   If it does not belong to a parent the school already knows, the link goes to the address just typed in, using the **Start an Application** template.
-   If it does belong to an existing parent, the link goes only to the email addresses ADAM already holds for that parent, using the **Start an Application (Existing Parent)** template. The address typed into the form is not used and is not kept. This means an existing parent should look for the email in the account the school has on file for them.

ADAM sends at most three of these start emails to the same parent in any 24 hours.

![](assets/screenshots/online-applications/online-applications-07.png)

The contents of both emails [are customisable](email-message-templates.md#email-message-templates).

### Confirming the Details

Clicking the link in the email opens a screen showing what will be used to create the application. Nothing is created until the parent clicks **Start Application**, so a link opened by accident changes nothing.

Parents the school does not yet know simply check the details they typed. If something is wrong, **These details are wrong: start again** takes them back to the beginning.

Parents the school does know are asked where to send the rest of the correspondence. **Email Address** offers each address ADAM holds for them, plus **(use an alternate address)**, which reveals an **Alternate Email Address** box. They also give a **Contact Telephone Number** and the **Number of Children Applying**.

![](assets/screenshots/online-applications/online-applications-17.png)

If anything is typed incorrectly here, ADAM says so and shows the screen again without using up the link.

The link works once. Following it again, or after 24 hours have passed, gives the message *This link has expired or has already been used.* with a **Start a new application** button. This is the same message whatever the reason, so the page never confirms whether an ID number is known to the school.

### Starting from the Parent Portal

A parent who is already logged into the [Parent and Pupil Portal](parent-and-pupil-portal.md#parent-and-pupil-portal) does not need the emailed link at all. Under the **New Pupil Application** heading, they click **Submit an online application for a new pupil**, which takes them straight to the same confirmation screen described above, with the email addresses ADAM holds for them already offered. Clicking **Start Application** creates the application at once.

![](assets/screenshots/online-applications/online-applications-18.png)

### Continuing to the Application Form

Once **Start Application** has been clicked, ADAM creates the application, emails the parent the link to the application form itself — the **New Application** template — and takes them straight on to it. That second email is the one they need in order to come back to a part-completed form later.

### Responding to Online Agreements

When parents click on the link provided, ADAM first checks whether the school has set up any [online agreements](online-agreements.md#online-agreements) for the **Admissions Parents** audience. If there are any, parents must read and respond to each outstanding agreement before they can continue. Where an agreement has **Acceptance Required** set to Yes, parents are given a single button to accept it; where it is set to No, they may also decline. Once every outstanding agreement has been answered, ADAM moves the parent on to the application form automatically.

If the school has not set up any agreements for applicants, this step is skipped and parents go straight to the application form.

### Completing the Application Form

ADAM now presents the application form one page at a time. Parents complete their own details on the **Parents** page first, then a page for each child. Families the school already knows skip the **Parents** page. Each page ends with a **Save and continue** button, which saves the page and opens the next one. A page can be saved at any time, even with required fields still empty; ADAM lists anything still missing below the form.

![](assets/screenshots/online-applications/online-applications-08.png)

The contents of this application form can be customised by controlling which fields appear in the application form within the [core database field management screen](database-field-management.md). Some questions may appear only once the parent has given a particular earlier answer, such as a grade of entry, because the school has given them a [**Show when** rule](database-field-management.md#show-when-rules).

Where an application was started for the parent by another system — an application-fee payment provider, for example, using the [API](api-applications.md#applicationscreatepost) — some of the form may already be filled in. Fields that the other system has supplied are pre-filled, and those it has marked as fixed are shown but cannot be changed by the parent. Values supplied that way are also the ones written to the family and pupil records when a member of staff approves the application, even where the parent was allowed to edit them.

Parents can return at any time within the 7 day window they are given to continue completing the form. To return to the screen, they simply need to use the email link that was sent to them.

From this point on, a progress bar is shown across the top of each screen so that parents can see where they are in the process. It shows **Parents**, one step per child, **Documents** and **Review & Submit**. A child’s step shows **Child 1**, **Child 2** and so on until the child’s first name has been saved, and then shows the name. A tick next to a step means that page is complete; a warning sign means something on it is still needed. Parents can click the **Parents** step or any child’s step at any time, and can click **Documents** or **Review & Submit** once they have reached it; the page they are leaving is saved first. On a phone the progress bar wraps onto a second line. The **Documents** step only appears if the school has [asked for supporting documents](#collecting-supporting-documents-during-the-application).

### Uploading Supporting Documents

If the school has set up [supporting documents to collect during the application](#collecting-supporting-documents-during-the-application), parents are taken to a **Supporting Documents** screen after saving the last child’s page. A counter at the top shows how many documents have been uploaded so far, out of every document on the screen. The total includes optional documents as well as Requested and Mandatory ones. The **Documents** step in the progress bar shows a tick once every mandatory document is uploaded, and a warning sign until then.

Each document is shown with its name, a short description, and the file types it accepts (shown as *Accepted: …*). Depending on how the school configured the slot, it may also carry a badge: a **Requested** badge means the school would like the document but will still accept the application without it, and a red **Required** badge means the application cannot be submitted until it is uploaded. A document with neither badge is entirely optional. Documents that apply to a particular child are repeated for each child and labelled with the child’s first name, or “Child 1”, “Child 2” and so on if the child’s first name has not been saved yet.

![](assets/screenshots/online-applications/online-applications-16.png)

To upload a document, the parent clicks **Choose file** next to the slot and selects the file. The file is uploaded immediately and the slot shows a tick alongside the file name. If a parent uploads the wrong file, they can click the **remove** option next to it and choose another. If a file is larger than the maximum size set for that slot, it will be rejected and the parent asked to choose a smaller file. Likewise, if the parent selects a file whose type is not accepted for that slot, ADAM rejects it with a message listing the accepted types — for example *'birth-certificate.key' must be one of: PDF document, JPEG image.*

Uploading documents here is not the same as having them approved — the documents are held against the application and only filed into the document repository once a staff member approves the application.

When all the Requested and Mandatory documents have been uploaded, the parent clicks **Continue to review** to move to the final step. If any are still missing, clicking **Continue to review** first shows a pop-up listing them. If a Mandatory document is missing, the pop-up is titled *Some required documents are missing* and warns that the application cannot be submitted without it. If only Requested documents are missing, it is titled *Some requested documents are missing*. Either way, **Continue anyway** moves on to the review step and **Go back** stays on the documents screen.

### Reviewing and Submitting the Application

The **Review & Submit** step shows the proposed date and grade of entry for each child. For a new family, it also lists each parent’s cell number and email address under **Parent Contact Information** and asks the parent to check them. Families the school already knows do not see the contact details.

Below the details is the message set in **Confirm Submitting**, followed by the **Confirm and Submit Application** button. If any Requested documents have not been uploaded, a warning above the message lists them. This is a reminder only.

![](assets/screenshots/online-applications/online-applications-10.png)

If anything required is still missing, the review screen shows a **Still needed** list instead of the **Confirm and Submit Application** button. The list is grouped by page — **Parents**, each child, and **Documents** — and each group heading links straight back to that page. It includes required fields, the proposed date and grade of entry, the ID number used to start the application if it no longer belongs to either parent, and any **Mandatory** documents. Once the list is empty the button appears. **Requested** documents that are missing are shown as a reminder only, and do not stop the application being submitted.

![](assets/screenshots/online-applications/online-applications-19.png)

Finally, they click on the **Confirm and Submit Application** button. ADAM shows the **Receipt of Application** message, with a tick against every step in the progress bar. The application is now with the school, and the parent can no longer change it. Following the email link again gives the message *Sorry - this application has already been submitted. No more changes are possible.*

![](assets/screenshots/online-applications/online-applications-11.png)

## Application Process: Procedure for Staff

At this point a notification is sent to the system administrator, or the configured contact in site settings if one has been set.

![](assets/screenshots/online-applications/online-applications-12.png)

The content of this email can be [changed in the email templates](email-message-templates.md#email-message-templates). This template is called “Notify School of Completed Application”.

The staff member can now visit **Admissions → Online Applications → Manage Online Applications** within ADAM. Here they will see a list of all the applications and their statuses. This list will include any applications that might be incomplete, might have expired (not completed within the 7 days) or which were rejected. Parents who have not yet clicked the link ADAM emailed them have no application yet. They are shown separately, in the [**Unconfirmed Applications**](#unconfirmed-applications) table near the top of the page.

![](assets/screenshots/online-applications/online-applications-13.png)

Note that applications can be revived from any status here by clicking on the “view” button. However, if an expired application is not viewed and approved within 3 weeks of it being requested by the parents, it will be deleted. Note that this expiry and deletion only happens if the application was never submitted to the school in the final step. However, it is possible for you to pick up an application that has expired (before it is deleted) and perform the enrolment from there.

Click on **view** next to the application you’d like to see. ADAM brings up the parents’ answers as a single form, with the family and every child on one page. Required fields must be filled in before the application can be approved.

![](assets/screenshots/online-applications/online-applications-14.png)

The admissions officer can make changes to this form, correcting spelling, or making sure that the data conforms to the required standards. There is no separate save: changes made here are kept only when the application is approved, and are lost if the application is rejected or the page is left.

If the school collects [supporting documents during the application](#collecting-supporting-documents-during-the-application), a **Submitted Documents** panel appears on this screen. It lists each document the parent uploaded, who it relates to (the family, or a child shown as **Child 1**, **Child 2** and so on in the order the children appear on the form), and the file name. Click on a file name to view or download it. If any Requested or Mandatory documents were not uploaded — note that a missing Mandatory document should already have stopped the parent from submitting — an **Outstanding required documents** warning lists what is missing, so the admissions officer can decide whether to follow these up before approving.

At the bottom of this form are two options:

![](assets/screenshots/online-applications/online-applications-15.png)

-   **Approving the Application** will add the pupil and family (if it is new) to the database. The pupil is added as an applicant in the [default admissions status](enrolment-process.md#managing-the-registration-statuses). This does *not* guarantee them a place or add them as a current pupil. *Remember that no communication is sent by ADAM.* Any documents the parent uploaded during the application are filed automatically into the document repository against the new pupil and family at this point — there is no separate document approval step for them.
-   **Reject Application** will remove the application from the pile. Typically, applicants are rejected here for technical reasons (incomplete form, incorrect grades, incorrect gender for monastic schooling, and so on). Rejection here essentially means tossing the application form into the bin. The pupil and the family will *not* be added to the database.

To leave an application on the list without approving or rejecting it, simply leave the page. Applications in the **Incomplete Applications** list also have an **edit** option. It opens **Edit Application Request**, where the ID number, contact number, email address and number of applicants given when the application was started can be corrected and saved. It does not change the parents’ answers on the form.

> [!WARNING]
> “Accepting” and “Rejecting” applications refers specifically to the **application form**. This will add these details into your database as an Applicant profile. **No decisions about enrolment into the school have been made** at this point. Enrolment (or not!) will only happen at the very end of the application process.

### Unconfirmed Applications

The **Unconfirmed Applications** table is on the **Manage Online Applications** page, between **Currently Waiting Approval** and **Incomplete Applications**. It lists the parents who gave their details on the application form but have not clicked the link that ADAM emailed to them. The newest are shown first. The table shows:

-   **Email:** the address the parent typed. Click on it to write to them.
-   **Phone:** the contact telephone number the parent typed.
-   **Children:** the number of children the parent said they are applying for.
-   **Submitted:** the date and time the parent gave their details.
-   **Link:** “valid until” and a time while the emailed link can still be used, or “expired” once it cannot. The link stops working 24 hours after the time in **Submitted**, so the time shown is usually tomorrow’s.

![The Unconfirmed Applications table with five parents: two whose link is still valid and three whose link has expired](assets/screenshots/online-applications/online-applications-20.png)

These parents do not have an application yet, so there is nothing to view or edit, and the table has no actions. You can email or phone them. The emailed link is valid for 24 hours. After that, a parent who still wants to apply must start again on the [application form](#finding-the-address-of-your-application-form); ADAM cannot send them a new link from this page.

A parent leaves this table when they click the link and then **Start Application**. Their application then appears under **Incomplete Applications**. Otherwise, ADAM removes the parent from the table once the number of days in **Expire applications (days)** has passed since they gave their details. The ID or passport number that the parent typed is deleted after 24 hours, when the link expires; ADAM keeps only the email address, telephone number and number of children until then.

A few parents are not listed here:

-   A parent who asked for a link more than once is listed once, with their most recent request.
-   A parent who already has an application that has not been submitted is not listed. That application is shown under **Incomplete Applications** instead.
-   A parent whose ID or passport number ADAM already knows is never listed. Their link went to the email address the school already holds for them, and ADAM does not keep the details typed on the form.

The parents in this table who have waited longer than the hours set in **Status email: hours before "not confirmed"** (24 by default) also appear in the [status email](#online-application-status-email).

## Uploading of Supporting Documents

Part of the admissions process is normally to collect documentation for your applicants, including past school reports and a copy of a birth certificate, for example. ADAM can collect these documents from parents in two ways.

**During the application.** If you set up [supporting documents to collect during the application](#collecting-supporting-documents-during-the-application), parents upload them as a step within the application itself, before it is submitted. The documents are held against the application and filed automatically into the document repository when the application is approved. This is usually the simplest experience for parents, because they complete everything in one sitting.

**After approval, through the portal.** Parents can also upload documents once their application has been approved, through the [Parent and Pupil Portal](parent-and-pupil-portal.md#parent-and-pupil-portal). Documents uploaded this way must be [approved by a staff member](document-repository.md#approving-documents) before they appear in the document repository. This route is also used for documents that are requested from existing pupils and families rather than at application time.

Read more about [setting up the document repository](document-repository.md#document-repository) and [allowing parents to upload documents](document-repository.md#parent-uploads-into-the-document-repository).
