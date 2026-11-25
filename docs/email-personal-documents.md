# Email Personal Documents

**Email personal documents** sends each pupil, family or staff member their own document, such as a certificate, a statement or a letter. You upload one file per person, check who each file is for, and then email the whole set from the [Messaging Centre](messaging-centre.md#messaging-centre)’s email form. ADAM attaches each person’s own document to their email.

The uploaded documents are a **set**. A set waits until you email it, and only you can see it. You can email the same set more than once, for example to families first and to pupils afterwards.

Only staff use this feature. Families, pupils and staff members receive the emails.

Navigate to any of these. They all open the same page:

-   **Pupils → Messaging and Communications → Email personal documents**
-   **Staff → Messaging and Communications → Email personal documents**
-   **Families → Messaging and Communications → Email personal documents**

The menu option is shown to staff with the **Allow Bulk Upload of Documents** permission. The page itself also needs the Messaging Centre permissions described in [Who Can Email Personal Documents](#who-can-email-personal-documents).

The page is titled **Email Personal Documents**. It lists your sets, with these columns:

-   **Uploaded**: the date of the upload. Click the date to open the [set’s page](#the-sets-page).
-   **For**: the group the documents are for.
-   **Documents**: the number of documents in the set.
-   **Sent**: each time the set was emailed, with its audience and date, or “Not sent yet”.
-   **Deleted on**: the date ADAM deletes the set. See [How Long ADAM Keeps a Set](#how-long-adam-keeps-a-set).

If you have no sets, the page says “You have no documents waiting to be emailed.”

## Who Can Email Personal Documents

A staff member needs all three of these:

1.  The **Allow Bulk Upload of Documents** permission, on the **Document Repository** tab when [changing the permissions of a group](security-administration-for-staff.md#changing-the-permissions-of-a-group).
2.  The Messaging Centre permission for the group the documents are for. These are described in [Permissions Required for using the Messaging Centre](messaging-centre.md#step-1):
    -   **Current pupils** and **Current staff**: “Can make use of the messaging centre”.
    -   **Applicants**: “SMS and Email Admissions”.
    -   **Alumni and leavers**: “SMS and Email Alumni”.
3.  The right to send emails to the audience, in [Edit messaging permissions](messaging-centre.md#step-2) for the **Email** module:
    -   For current pupils, **All Families** or **Class Families** to email families, and **All Pupils** or **Class Pupils** to email pupils.
    -   For applicants and for alumni and leavers, **All Families** to email families and **All Pupils** to email pupils. The class rights do not count, because nobody teaches these pupils.
    -   For current staff, **Staff**.

A staff member who has only **Class Families** or **Class Pupils** can upload documents for all current pupils. When they email the set, ADAM leaves out the pupils they do not teach. The set’s page and the email form name those pupils before anything is sent.

The feature is offered only while the Email messaging module is enabled. A document larger than the **Maximum size of email attachments** setting (**Communications** category, **Messaging Centre**) cannot be emailed, so ADAM leaves it out of the upload.

## Uploading the Documents

On the **Email Personal Documents** page, click **Upload documents**. The page **Upload Documents to Email** opens.

1.  Choose **Who the documents are for**: **Current pupils**, **Applicants**, **Alumni and leavers** or **Current staff**. The list shows only the groups you may email.
2.  In **Choose documents**, select the files, or a ZIP file of them. Name each file so that ADAM can find its person, as described in [Naming of Documents](document-repository.md#naming-of-documents). The page lists the same rules, and the limits on the number and size of files your server accepts.
3.  Click **Upload Documents**.

ADAM leaves out any file it does not accept, cannot read, or that is larger than the email size limit. A warning names those files. If none of the files can be used, ADAM returns you to the form.

## Checking the Matches

ADAM then shows the review page, headed “Email personal documents”. It matches the files against the group you chose. Check the matches, choose a person for each row that needs one or tick **Ignore**, and click **Confirm**. [Matching Uploads to People](matching-uploads-to-people.md#the-review-page) describes the review page.

Nothing is saved until you click **Confirm**. ADAM then makes the set and opens the set’s page.

## The Set’s Page

The set’s page is also headed **Email Personal Documents**. It starts with a summary, for example “Current pupils: 120 documents, uploaded 12 March 2027. This set is deleted on 11 April 2027.”

Below the summary are two links:

-   **Email these documents** opens the [email form](#emailing-a-set). It appears only when you may email the set to somebody.
-   **Delete this set**. See [Deleting a Set](#deleting-a-set).

The table has one row per document, with the **Person** and the **Document**. Each time the set is emailed, the table gains a column headed with the audience and the date, such as “Families, 12 March 2027”. The column shows what happened for each person:

-   **Queued**, with the number of emails, for example “Queued: 2 emails”.
-   **Not sent**, with the reason. For example:
    -   “No family email address is opted in to bulk mail.”
    -   “The pupil has no email address.”
    -   “The staff member has no email address.”
    -   “You do not teach this pupil.”
    -   “This person is no longer on ADAM.”
    -   “The document has been deleted from the Document Repository.”
-   **Failed**, with the reason, for example “The document could not be filed in the Document Repository.”

When the audience is **Families and pupils**, the reason names the half that was not sent, for example “Queued: 1 email. Pupils: The pupil has no email address.”

A pupil or staff member who is no longer on ADAM is listed as “A pupil no longer on ADAM” or “A staff member no longer on ADAM”.

## Emailing a Set

On the set’s page, click **Email these documents**. The form is the Messaging Centre’s email form, described in [Composing Your Message](messaging-centre.md#composing-your-message), with these differences:

-   **To** says how many people are in the set.
-   **Audience**, for a set of pupils’ documents: **Families**, **Pupils**, or **Families and pupils**. Only the audiences you may email are offered. A set of staff documents always goes to **Staff**.
-   **Left out** names the pupils you do not teach, when your rights cover only your own classes.
-   **Document Repository Category** and **Description** appear on the first email of a set, and both are required. ADAM files each document in this category, linked to its pupil or staff member, when the set is first emailed. The description starts as a copy of the **Message Subject** and follows it until you type your own. On later emails the form shows the category the documents are filed in instead.
-   **Attachments** says that each person’s own document from the set is attached. You may add common attachments as well. They go to everybody.
-   The merge codes are the pupil codes for a set of pupils’ documents, and the staff codes for a set of staff documents.

If the set was emailed before, a warning above the form says so, for example “This set was already emailed to families on 12 March 2027.”

Click **Send emails**. ADAM queues the emails as one Messaging Centre batch and returns you to the set’s page, where the table shows what happened for each person. The batch is an ordinary batch, so you can [delay it or stop it](messaging-centre.md#managing-messaging-centre-batches) as usual.

Each email carries the documents of one pupil or staff member. A family with two children in the set gets two emails, one for each child.

### Who can open the filed documents

Once filed, the documents are ordinary [Document Repository](document-repository.md#document-repository) documents. Staff see them according to their permissions for the category. A family can open the attachment, from the email or on the portal, only if the category allows families to read it. See [Pupil and Family Permissions](document-repository.md#pupil-and-family-permissions). If you want parents to open the documents, choose such a category.

The categories for photographs, name pronunciations, email signatures and the Messaging Centre’s own attachments are not offered.

### Emailing a set again

To email the set again, open it from the **Email Personal Documents** page and click **Email these documents**. Choose another audience, or the same one again. The documents are filed only once, on the first email.

### Sending a test email

**Send a test email** sends you the email that the first person in the set who can be reached would receive, with their document. It goes to you only. A test email files nothing, and does not count as emailing the set.

A [sandbox site](sandbox-sites.md#nothing-is-delivered) does not offer a test email, and cannot email a set.

## Deleting a Set

On the set’s page, click **Delete this set** and confirm.

-   A set that was never emailed is deleted with its uploaded documents. Nothing was filed or emailed.
-   A set that was emailed loses only its record. The documents already filed stay in the Document Repository.

## How Long ADAM Keeps a Set

-   A set that was never emailed is deleted 30 days after it was uploaded, with its documents.
-   A set that was emailed is deleted 90 days after it was first emailed. The filed documents stay in the Document Repository.

An email that reached nobody, because nobody in the set could be emailed, does not count as emailing the set. The **Deleted on** column and the set’s summary give each set’s date.

A set past its date can no longer be emailed.
