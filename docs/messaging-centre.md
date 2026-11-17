# Messaging Centre

## Sending Messages from the Messaging Centre

There are a number of entry points into the messaging centre.

### Messaging current pupils or parents

All of the following menu options can be used: they are all the same.

-   **Pupils → Messaging and Communications → Messaging Centre**
-   **Classes → Messaging and Communications → Messaging Centre**
-   **Families → Messaging and Communications → Messaging Centre**

The first step in any of these will be to select the module that you wish to use to send the message with. The “Email” module is available on most servers, and many schools have also enabled SMS sending. If SMS sending is available, you will see one of the SMS modules also available for you to use.

> [!WARNING]
> Note that sending SMSs does incur costs!

![](assets/screenshots/messaging-centre/messaging-centre-02.png)

### Choosing an audience

Having chosen a module, ADAM asks you to select an audience — *“Please select an audience to send your email to:”*, or *“...your SMS to:”* if you picked an SMS module — and offers a list of the groups of people you are allowed to write to. You will only see the audiences that your permissions allow, so your list may be shorter than the one below.

-   **Pupils by class** — choose a subject, then the classes within it. This is the option described in the rest of this section, and is the one most people use.
-   **Pupils by grade** — choose one or more grades.
-   **Pupils by filter** — build a filter, in the same way you would for a [scratch list](scratch-lists.md#scratch-lists), and message everybody it matches.
-   **Staff** — choose from the staff of the school.
-   **Admissions** — applicants and their parents, chosen by the year and the grades they are entering and by their registration statuses.
-   **Admissions by filter** — applicants and their parents, chosen with a filter. See [Messaging applicants and their parents](#messaging-applicants-and-their-parents) below.
-   **Alumni** — pupils who have graduated.
-   **Leavers** — pupils who have left the school.

Each audience also has a menu option of its own, which takes you straight to that audience without going past this list. The three **Messaging Centre** options listed at the start of this section all lead to **Pupils by class**; the rest are:

-   **Pupils by grade:** **Grades → Messaging and Communications → Messaging Centre (by grade)**
-   **Pupils by filter:** **Pupils → Messaging and Communications → Messaging Centre (by filter)**
-   **Staff:** **Staff → Messaging and Communications → Messaging Centre**
-   **Admissions:** **Admissions → Messaging and Communications → Messaging Centre for Admissions**
-   **Admissions by filter:** **Admissions → Messaging and Communications → Messaging Centre for Admissions (by filter)**
-   **Alumni:** **Alumni → Messaging and Communications → Messaging Centre for Alumni**
-   **Leavers:** **Alumni → Messaging and Communications → Messaging Centre for Leavers**

If your school has only one messaging module enabled, these menu options take you directly to the audience’s own screen. If more than one is enabled, ADAM asks you to choose the module first.

You will then need to select a subject. By selecting a subject, ADAM will show you a list of classes in that subject and allow you to select which of those classes you would like to send your message to. Many schools will set up some classes specifically for communication so that it is easy to select a whole grade, or other specific groups of pupils/parents that you may need to communicate with on a regular basis.

![](assets/screenshots/messaging-centre/messaging-centre-03.png)

You can now choose the classes that you would like to message by ticking the boxes that appears next to each. If you wish to send to all classes, you can click on the “Select” box in the header column to select all classes.

![](assets/screenshots/messaging-centre/messaging-centre-04.png)

Once selected, click on the **Next** button that appears at the bottom of the page.

ADAM will now show you a list of pupils in the classes you selected and any staff that may be associated with those classes (either as teachers or teaching assistants):

![](assets/screenshots/messaging-centre/messaging-centre-05.png)

> [!WARNING]
> Note that the list of staff might also include other senior teachers and management staff members who have a specific permission to receive all copies of mail sent via the messaging centre.

There are three tick-boxes in the table header. You can click on these to send to ALL pupils, ALL parents or ALL staff. You’ll see that as you click on these, all the ticks in the column are selected.

> [!WARNING]
> While sometimes necessary, if you plan on extensive personalisation of the emails with mail merge fields, you are strongly encouraged to limit your email to either only parents or only pupils. Mixing the audience types will be confusing for mail-merge scenarios.

Individual pupils, parents or staff members can either be added or removed from the recipient list by ticking or unticking the boxes next to their names.

At the top of the table is a **Next** button to click on when you are happy with your list of recipients.

ADAM now shows you the messaging centre composer. This works in a very similar way to your web-based email systems.

The image below shows all options that are available on the Messaging Centre and you may not see all of them depending on your permissions and will depend on the message type (e.g. SMSs do not have subjects or attachments).

![](assets/screenshots/messaging-centre/messaging-centre-08.png)

-   **Send email on behalf of:** ADAM will normally show your own name and email address as the sender of any messages from the messaging centre. However, where schools delegate the sending of messages to a central person, it is often useful for responses to be directed to the person who asked for the message to be sent rather than the person who actually sends it.
-   **Message Subject:** Enter the subject of your message here. This field is not visible for SMS messages.
-   **Message:** You can type in your message here. Please see the section below on [Composing your Message](#composing-your-message).
-   **Disable rich-text editor:** This will almost never be required, but some schools make use of specific design tools to format their emails in specific ways can use this to paste in a generated HTML email body that ADAM won’t attempt to fiddle with.
-   **Mark as confidential:** When notifications are sent out to administrators that a message has been sent from the messaging centre, ADAM normally includes the message body. However, when sending sensitive information via email or SMS, it can be useful to have the contents of the message not included. Such messages will also be restricted for viewing in the messaging centre logs.
-   **Delay sending until at least:** ADAM will accept your message and add it to the queue, but will not start processing that batch until the specified time has passed. Note that this will not be an exact time, and not all messages will be processed at once - and depending on the size and volume of messages, may take some time to process after that. But when sending embargoed information to your school community, this can be a useful tool.
-   **Attachments:** You can attach a number of files to your email for adam to send. Along side each is a drop-down list of options. If you are attaching an image file (e.g. JPG, PNG, GIF), ADAM will allow that to be embedded directly into the message body either at the top, bottom, or where it finds the code {embed} written in your email. Where you have multiple embedded images, they are placed in the order that you add them here. Note that for embedded images, ADAM does not attempt any resizing and so your original images that you use should take this into account. If you are unsure, use a 600px width as the maximum.

Once you have composed your message, click on the **Send** button to have ADAM queue the message for you.

> [!WARNING]
> Note that regardless of your selected delivery time, all messages are queued with a minimum of 5 minutes lead time before they are processed.

> [!NOTE]
> Messages sent from a [sandbox](sandbox-sites.md#nothing-is-delivered) are never delivered. They stay in their batch, waiting to be sent, and the **Send a test email** and **Send a test SMS** buttons are not shown.

### Messaging applicants and their parents

Applicants — pupils who have applied to the school but have not yet enrolled — are not part of the ordinary pupil audiences, and they have two audiences of their own. Both require the **SMS and Email Admissions** permission, described under [Permissions Required for using the Messaging Centre](#permissions-required-for-using-the-messaging-centre) below.

#### By entering year and grade

Choose the **Admissions** audience, or navigate to **Admissions → Messaging and Communications → Messaging Centre for Admissions**. ADAM asks for three things:

-   **Entering in Year:** the year the applicants are due to start.
-   **Entering in Grades:** the grades they are entering. To message every applicant for that year, either select all the grades or deselect all of them.
-   **Registration Statuses:** which registration statuses to include. Your school’s default status for applicants is ticked for you.

Click on the **Next** button to see the list of recipients.

This is the quickest way to reach a whole intake, but it can only ask those three questions.

#### By filter

Choose the **Admissions by filter** audience, or navigate to **Admissions → Messaging and Communications → Messaging Centre for Admissions (by filter)**.

Instead of the three fields above, you build a filter — exactly the same filter builder you would use for a [scratch list](scratch-lists.md#scratch-lists), and with the same fields available. That means you can select applicants on anything ADAM records about them, including **Date of Application**, **Months Since Application**, **Previous School**, **Siblings At School**, and any custom fields your school has added.

Add your criteria and click on **Update the filter** to see how many applicants match. As long as the filter matches 200 applicants or fewer, ADAM lists their names underneath so that you can check you have caught the right people. Adjust the criteria and update the filter as many times as you need.

When you are satisfied, click on the button at the bottom of the page — it reads **Next – with 12 pupils selected**, or however many your filter has matched — and ADAM shows you the list of recipients in the usual way, from which you continue to the composer.

> [!NOTE]
> This audience only ever sees applicants. Pupils already enrolled at the school are reached with the **Pupils by filter** audience instead, which offers the same filter builder over current pupils. Neither audience can see the other’s pupils, and the two are controlled by different permissions.

## Composing Your Message

ADAM allows for the message you write to be customised for each recipient to allow them to receive a personalised message. This increases engagement with your communication.

### Formatting

The formatting options that are permitted are specifically kept to a minimum so that the school’s branding can be preserved. Note that formatting and school branding are applied to the message after it is sent and so you won’t get to appreciate the colours and fonts until ADAM sends the message. For more information on customising the branding of your emails, please see the section on [Editing the Default Template](email-message-templates.md#editing-the-default-template).

### Personalised Greeting

By default, ADAM includes the greeting “Dear ^n” as part of its template. This will ensure that regardless of who receives the message, it will be addressed to them. ADAM will substitute the “^n” out with the recipient’s name.

### Merge Codes

Below the email window is a list of merge codes that can be used in your message. These are the same fields that you can call on when you draw up a [scratch list](scratch-lists.md#scratch-lists) of pupils.

![](assets/screenshots/messaging-centre/messaging-centre-10.png)

To have ADAM include the information in your messages, you can include the code where you would like it to appear. For example, the following message:

Please remember to send your reply slip with {3} to school tomorrow.

Will be substituted as sent as:

Please remember to send your reply slip with Johnny to school tomorrow.

#### A warning about context

Note that if you mix more than one type of recipient (parents, pupils, or staff) in the same email, ADAM won’t be able to substitute information reliably. Staff, for example, don’t have children linked to their profiles and so ADAM won’t be able to substitute anything when it finds a pupil code in the email.

Our advice: Send to one audience at a time, especially if you are using merge codes.

Note that this limitation does not apply to the “^n” greeting which will be substituted regardless.

### Duplicated Messages within Batches

If parents have multiple children at the school, one concern is that they will receive a copy of every message sent multiple times - once for each child.

ADAM handles this scenario quite cleverly in that, within a batch, it will check the contents of every message and if it sees that a parent is getting the exact same message more than once, it removes the duplicates.

This applies to all types of message, including SMS.

There are two caveats that you should be aware of:

1.  The messages must be sent in the same batch. ADAM will not detect duplicate messages that have been sent across multiple batches, regardless of how soon after each other they were sent. Some schools, for example, will send a message to the primary school separately to the high school and parents will children in both phases will receive the same message from each.
2.  If you personalise a message using merge codes, assuming that parents would give their children different names, using the first name merge code would mean that they would then get a copy for each child - even if these were sent in the same batch - because the content of the message, now including the different children’s names - is no longer identical.

## Permissions Required for using the Messaging Centre

Before a user can send messages from the messaging centre, they need a few permissions to be set first.

### Step 1:

The first permission is a general one that is applied to the whole permission group. They require, at a minimum, “Can make use of the messaging centre (*messaging\_centre*)”. This is found on the **Messaging** tab, and under the heading **E-mail**. For more information on changing staff permissions, please see [Security Administration for Staff](security-administration-for-staff.md#security-administration-for-staff) elsewhere in this documentation.

That permission covers the pupil and staff audiences. The remaining audiences are held separately, on the same **Messaging** tab but under the heading **Admissions and Alumni**:

-   “SMS and Email Admissions (*messaging\_centre\_admissions*)” allows both the **Admissions** and the **Admissions by filter** audiences.
-   “SMS and Email Alumni (*messaging\_centre\_alumni*)” allows the **Alumni** and **Leavers** audiences.

These are deliberately separate from the general permission. A user who can message the school’s current pupils does not thereby gain the ability to message applicants, and a user given only one of these permissions will see only that audience in the list.

### Step 2:

Once they can use the Messaging Centre, ADAM will need to know which messaging modules they may use and which people they may send to. Visit **Administration → Messaging Administration → Edit messaging permissions**.

Here you will see a list of permission groups along the side and a list of enabled messaging modules along the top:

![](assets/screenshots/messaging-centre/messaging-centre-11.png)

If you wish to set permissions for other messaging modules, you will need to enable these modules in the [Site Settings](logging-on-to-adam.md#site-settings). A link to the correct place in the site settings is provided at the top of the page. Note that while it is possible to set permissions for enabled modules, the module must have the correct configuration details supplied in the Site Settings in order for it to be capable of delivering your messages.

Here you can specify which groups can use which modules to send to which audiences.

-   **Staff:** This allows the user to send messages to any staff members.
-   **Class Pupils:** This allows the user to send messages to any pupils who belong to any of their classes (i.e. they can send messages only if they “teach” the pupil).
-   **All Pupils:** This allows the user to send messages to all pupils in the school. This permission is also needed to send messages to alumni and the pupil applicants.
-   **Class Families:** This allows the user to send messages to the parents of any pupils that they teach.
-   **All Families:** This allows the user to send messages to all parents of the school. This permission is also required to send messages to the parents of applicants.

Once you’ve set up the permissions, please click on the **Save** button at the bottom of the page.

## Managing Messaging Centre Batches

Once you’ve sent a message, you have a number of options regarding the batch, including seeing delivery reports and more. To access a list of batches, navigate to **Administration → Messaging Administration → View Messaging Centre batches**. A list of batches will be shown.

To access the details of a specific batch, click on the **view** action.

![](assets/screenshots/messaging-centre/messaging-centre-12.png)

The medium of the message, the sender of the message, the time that the message was loaded and the number of recipients is shown. ADAM also indicates the batch’s current status, such as “waiting”, “processing”, “paused”, or “finished”. A batch that contains messages ADAM can no longer complete on its own is flagged as **⚠️ needs attention (stuck)** — see [Recovering stuck messages](#recovering-stuck-messages) below.

### Delaying a Batch

It is possible to delay a batch in ADAM for a customised delivery time. One can either access the batch details as shown above, or immediately after sending a message:

![](assets/screenshots/messaging-centre/messaging-centre-13.png)

Batches will show different options based on their statuses. For example, one can abort and pause a batch that has started processing, but one cannot delay such a batch. ADAM will show the available options to you at the top of the batch. If the batch has finished processing, ADAM will not show any options.

If the batch can be delayed, an option will appear at the top of the list. This option will allow you to delay the sending of any messages that have not yet been processed. If a message has already been sent, ADAM cannot delay it, nor will it attempt to send it again.

![](assets/screenshots/messaging-centre/messaging-centre-14.png)

Clicking on this option brings up a screen where you can choose when you want the message delivered:

![](assets/screenshots/messaging-centre/messaging-centre-15.png)

Simply enter the date and time that you would like delivery to begin on. Note that ADAM will only allow you to choose a time in the future. If you choose a time in the past, ADAM will leave the delivery time unchanged. The same goes if you enter an invalid time.

Click on the **Delay batch** button to delay any unsent messages to the time you’ve specified.

![](assets/screenshots/messaging-centre/messaging-centre-16.png)

ADAM confirms that it has changed the delivery time.

### Recovering stuck messages

Occasionally an SMS batch can leave one or more messages in a state that no delivery worker will ever complete — for example, if a delivery run was interrupted before ADAM could record the outcome. Such a batch is flagged on the batch list as **⚠️ needs attention (stuck)**, and the affected messages show a status of **⁉️ Stuck (never sent)** when you open the batch.

Open the batch to deal with these messages. Depending on what happened to each one, ADAM offers one or both of the following options at the top of the batch:

-   **Re-queue … that never reached the SMS provider** – these messages were never handed to the SMS provider, so ADAM can safely send them again. Choosing this returns them to the queue for another delivery attempt.
-   **Abandon … stuck … (they will not be resent)** – these messages may already have been sent, but ADAM was unable to confirm it. Because resending them could deliver a duplicate, ADAM will not send them again. Choosing this simply clears the stuck state; if the messages still need to go out, compose a new message.

These options only appear when there are stuck messages to act on, and only for staff who are permitted to manage the batch (its owner, or a user with the permission to re-queue error messages or to abort batches).

> [!NOTE]
> Only SMS batches can become stuck in this way. Email messages are claimed and sent in a single step, so they never enter this state.

## Sending SMSs from the Messaging Centre

Please see [SMS Service](sms-services.md#sms-services) elsewhere in this manual.

## Messaging a Pupil’s Teachers

It is very useful to be able to message the teachers of a single pupil. To do this, navigate to **Pupils → Messaging and Communications → Send email to a pupil’s teachers**.

Type in the name of a pupil and click on the **Next** button:

![](assets/screenshots/messaging-centre/messaging-centre-17.png)

The following screen appears:

![](assets/screenshots/messaging-centre/messaging-centre-18.png)

The buttons at the top allow you to select different types of teachers. For example, clicking on **Select Academic** will select only the teachers who are recorded against classes in the **Academic** subject category. Your server will show customised buttons depending on which categories are available on your server.

In the **Additional Staff** at the bottom, you can click and choose other staff members, not listed, to be included in the email. You can search for staff here by typing a part of their name. You can have many staff here if you require. If staff are duplicated by accident, they will *not* be sent the email twice.

Click on the **Next** button to begin composing your message.

The screen shown is the standard messaging centre screen, which may have different options to those shown below, depending on your permissions:

![](assets/screenshots/messaging-centre/messaging-centre-19.png)

Click on **Send emails** to queue your email.
