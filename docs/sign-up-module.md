# Sign-up Module

The Sign-up module is designed to allow staff, pupils and parents the ability to sign up for lists, events and appointments. Most events are booked by or for a pupil. An event can instead be set up so that a family books it as itself — see [Family Sign-ups](#family-sign-ups). The sign-up module has the following data structure:

-   Event Category

-   Events

-   Appointments

Here is an example of how this might translate into real-life - using the same colour coding as above:

-   Support Lessons

-   Maths

-   Monday 5 Apr
-   Tuesday 6 Apr

-   Afrikaans

-   Monday 5 Apr, 14h00
-   Tuesday 6 Apr, 14h00

-   Catering Lists

-   Hot Lunches

-   Monday 5 Apr
-   Tuesday 6 Apr

-   Clubs and Societies

-   Term 1, 2015

-   Agricultural
-   Bridge
-   Computers

-   Sports

-   Term 1, 2015

-   Tennis: Social
-   Tennis: Team
-   Waterpolo

-   Teacher Meetings

-   Mr Smith

-   Monday 21 April, 14h00
-   Monday 21 April, 14h10

As can be seen in these examples, it is possible to have a wide variety of appointment types – some are time-dependent and others are not.

## Terminology: Event Categories vs Events vs Appointments

These three terms are easily confused. ADAM and this documentation makes very specific use of them. We have used them to represent a hierarchical structure. The top level being “Event Category” and the bottom level being “Appointment”.

Every event must have an element of all three. It might seem odd that an “Event” should have “Appointments”, particularly if the event is a once-off occasion. However, in order to be consistent in our handling of the many different possibilities, this is a strange anomaly that exists. However, don’t worry: if you understand that a once-off event must have an appointment, then you are most of the way to understanding how it all fits together. ADAM will guide you through the process of adding events and appointments, with some guidance about which options to choose.

Here are some examples to illustrate the differences to you.

-   In the scenario where we are creating a signup sheet for parents to book meetings with teachers at a parent-teacher evening, the “Event Category” would be “Parent-Teacher Meetings”, each teacher would then have an “Event” within this category. The “Event” is then broken down into the 5-minute “Appointments” that are available. I.e. Parent-Teacher Meetings → Mrs Smith → 18h45 to 18h50. Because the parents book these meetings, each event would be a [family sign-up](#family-sign-ups).
-   When signing up pupils for sports teams, the “Event Category” would be “Sports Teams Signups”. Each sport would be an “Event” and each “Appointment” could be a term or season. I.e. Sports Teams → Cricket → 1st Term
-   When signing up pupils who wish to attend a voluntary presentation by a visiting speaker, the “Event Category” might be “Visiting Speakers”, the “Event” might be the name of the speaker and the appointment would be the date of the presentation (this also allows there to be multiple presentations, for example). I.e. Visiting Speakers → Nelson Mandela Foundation → Tuesday 5th, 7pm.
-   In boarding schools, pupils often need to request permission to visit venues such as the library. Here, the “Event Category” might be “Evening Prep”, the “Event” might be “Library” or “Computer Lab” and the appointment would be the date of the visit. I.e. Evening Prep → Library → Thursday 14th.

## Managing Event Categories

On the “**Pupils”** tab, under the “**Sign Ups”** heading, click on the option to “**Manage event categories**”.

![](assets/screenshots/sign-up-module/sign-up-module-01.png)

### Adding a new Signup Category

At the top of the page, click on the “**Add new Sign-up Category**” link.

![](assets/screenshots/sign-up-module/sign-up-module-02.png)

The fields have the following meanings:

-   **Category Description:** This is the name of the category and is used in the displaying and sorting of events and appointments.
-   **About this category:** This field is a note field and is not used for display purposes.
-   **Notify teacher for each sign-up:** If this option is set to “Yes”, the organising teacher will receive an email after each pupil signs up for the event. Please choose this setting carefully as a wildly popular event could cause a lot of mail to be delivered.
-   **Notify teacher of final sign-up list:** If this option is set to “Yes”, then the organising teacher will receive a list of signed-up participants when the booking time closes.
-   **Limit number of signups:** This option sets a default limit for each appointment (it is easily overridden later). This serves to prevent an activity being oversubscribed.

Click on “**Save this Sign-up Category**” to save it.

Once saved, you should be taken back to the “Sign-up Categories” list shown above. Click on the “events” option in the table next to the new category.

![](assets/screenshots/sign-up-module/sign-up-module-03.png)

### Creating Events

This will display any events that have been created for this category. Because ours is still new, it shows nothing. Click on the link “**Add a new event**”.

![](assets/screenshots/sign-up-module/sign-up-module-04.png)

The fields on this page are explained as follows:

-   **Event name:** Type in the name of the event. See the [examples above](#terminology-event-categories-vs-events-vs-appointments) for ideas.
-   **Category:** This should already reflect the category of the event, but you can change it if you need to.
-   **Organising Teacher:** Please select the organising teacher from the list. This teacher will receive attendance lists and more from the appointments that will be scheduled later. If you may only manage your own events, this is always you.
-   **Event information:** The information for this event will be shown to pupils (or, for a family sign-up, to families) and should explain what the event is about.
-   **Limit pupil signups:** This will prevent pupils from signing up for too many appointments. If these are schedules for one-on-one appointments, for example, you may wish that a pupil only signs up for only one of them. This setting is ignored for family sign-ups.

Please note that only future appointments count towards a pupil’s limit. If an appointment passes, it will no longer count towards the pupil’s limit and they may be able to sign up for further appointments. If you wish to avoid this, then all bookings should be set to close before the first appointment takes place.

-   **Sign up by:** Choose **Pupil (each pupil signs up)** for an ordinary event. Choose **Family (a family signs up, no pupil recorded)** when parents book as a family, such as parent-teacher meetings. See [Family Sign-ups](#family-sign-ups) for how these differ.
-   **Limit per family:** For a family sign-up, this is how many appointments one family may book for this event. It is ignored for pupil sign-ups.
-   **Limit to classes:** The event and its appointments will only be shown to pupils who are members of the selected classes. If no classes are selected, it will be available to all pupils. It may be useful, for example, when setting up appointments for pupils to see teachers to limit those appointments to appear for pupils taught by the organising teacher. For a family sign-up, the event is shown to families who have a child in one of the selected classes.
-   **Confirmation reminders:** Choose when ADAM should send a reminder to the people who signed up, or **No reminders**.
-   **Send confirmation reminders to:** Choose whether reminders go to the **Pupils**, their **Families**, or both. For a family sign-up, this setting is ignored: the reminder always goes to the family that made the booking, and to no one else.
-   **Appointment Approval:** It may be possible that your appointment or sign-up requires teacher approval. If this is the case, it is possible to set either the organising teacher or another teacher that teaches the pupil, to approve the appointment. A family sign-up can only use **No approval required** or **Approval by organising teacher required**. ADAM will not save a family event that asks for another subject teacher’s approval.

For example, it may be necessary for the pupil’s Home Room Teacher to approve sign up to an extension activity. In this case, one would choose “Approval by another subject teacher required” and in the “**Approving Subject Teacher**” dropdown, choose the “Home Room” subject. When a pupil signed up for this event, an email would be sent to their Home Room teacher requesting their approval. The subject that is in this list is otherwise ignored.

Click on the “**Save this event**” button.

### Creating Appointment Slots

After saving a new event, you are automatically taken to this screen:

![](assets/screenshots/sign-up-module/sign-up-module-05.png)

This screen allows you to choose the type of appointment you require. There are four options. Each displays slightly different information and is displayed slightly differently to the user. Use the descriptions to guide you to which appointment type would best suit your needs.

We will work through each example:

#### Team sign-up

![](assets/screenshots/sign-up-module/sign-up-module-06.png)

-   In this instance, the **Description** is the most important option since it will differentiate it from the other appointments.
-   The **Limit** will default to what you set in the event category. You can override it here on an appointment-by-appointment basis.
-   Please ensure to choose the signup **start** and **end** dates and times carefully. ADAM currently does not check for poorly chosen entries (such as things that close before they open). When the signup end date is reached, ADAM will automatically send the organising teacher a list of attendees.

Below the table is an option to “**Add a new appointment**”. Clicking on this will duplicate the row, including the signup start and end dates. Before you add new appointments, set the sign-up start and end times to appropriately before you add new appointments!

Use the “**del**” option on any row to remove the appointment, except that ADAM won’t let you remove the last row in the appointment table. Every event must have at least one appointment in order to be useful!

Here is an example of what a “Team sign-up” set of appointments may look like:

![](assets/screenshots/sign-up-module/sign-up-module-07.png)

Notice that the limits on each appointment are entirely independent of each other. In this example, each activity has approximately one week to sign up for the activities, with each providing a limit to the number of spaces available for that. Only 10 people, for example, can sign up for “Sky Diving”.

#### Once-off Event

This is a single event which generally has a time and date associated with it, but which happens only once. This might be attending a specific presentation or activity.

![](assets/screenshots/sign-up-module/sign-up-module-08.png)

With this particular appointment type, there is no option to add a second appointment.

#### Daily Signup

This option allows you to create similar appointments on successive days.

For this particular type of appointment, a description is not necessary since it will be possible to distinguish between the appointments based on their date. Notice that here there is only a date for the appointment and no time, since it is assumed that the time is either constant or irrelevant to the sign-up.

![](assets/screenshots/sign-up-module/sign-up-module-09.png)

Clicking on the “Add next day” option will add a new appointment for the next *weekday* date. It will also advance the sign-up *end date* by a day also, but keep the signup start date the same. In the example below, on the second entry, ADAM kept the sign-up start date for the event the same (2 Feb), but changed the end date to a day later (9 Feb).

![](assets/screenshots/sign-up-module/sign-up-module-10.png)

Clicking on the option for “**Add for rest of reporting period**” will again add in options for all *weekday* appointments from the last date in the form until the end of the reporting period.

If you wish to add in weekend appointments, these can be done manually at the bottom of the form. It does not matter that these might be out of order. Simply click on “Add next day” (which will add a “week day”) and then change the date of that appointment to be a weekend.

Additionally, if you wish to delete certain appointments (e.g. no Fridays), then this must also be done manually by clicking on the “**del**” option next to the rows that you don’t want. Each event must have at least one appointment, so you won’t be able to delete the last entry.

#### Multiple Daily Appointments

This option allows you to set starting and finishing times for your appointment and to add in consecutive appointments based on the previously entered appointment. Here is an example of an appointment slot for pupil meetings:

![](assets/screenshots/sign-up-module/sign-up-module-11.png)

By clicking on the “**add a new consecutive appointment**” option, ADAM will create a new appointment that starts where the previous one ends and for the same duration as the previous appointment. Note that it does not affect the signup start or end time:

![](assets/screenshots/sign-up-module/sign-up-module-12.png)

If, however, you click on the option “**Add next day**”, ADAM will add in a new appointment for the next day, but at the same time as the last appointment. The signup ending time is also changed:

![](assets/screenshots/sign-up-module/sign-up-module-13.png)

Therefore you may have to adjust the appointment time before adding in new consecutive appointments.

Once you’re happy with your appointments, click on “**Save appointments**”. Importantly, nothing is saved until you click on that button.

![](assets/screenshots/sign-up-module/sign-up-module-14.png)

Clicking on the option “see the list of appointments for this event” will show you the list of appointments we created:

![](assets/screenshots/sign-up-module/sign-up-module-15.png)

Next to each option, the number of people that are signed up for the event are shown, and the options to edit or cancel the event.

To see a list of people who are attending the event, click on the **number of attendees**.

To edit the appointment, click on the “**edit**” link. *CURRENTLY THIS DOES NOT WORK*.

To cancel the appointment, click on the “**cancel**” link. Any pupils who might already have signed up for this appointment will receive an email notifying them that the appointment has been cancelled.

## Navigating through without creating a new event

We navigated through all the screens above by creating a new event. If you need to get back to any of them, use the menu items on the **“Pupils”** tab under the “**Sign Ups**” heading.

-   To see a list of events, click on “**Manage events**”. From there, you will be able to view and edit events. You can also see the event appointments from that screen. The **Signs up** column shows whether each event is booked by a **Pupil** or a **Family**.
-   Alternatively, the option “**View appointment slots for an event**” will also allow you to view the appointments, attendance lists and to cancel specific appointments.

## Signing Pupils Up for an Event

Staff members can sign up pupils for events, and pupils can sign themselves up for events. Note that both staff and pupils will require permissions to access these sections. Information on [how to set up staff permissions](security-administration-for-staff.md#security-administration-for-staff) is available, as is information on [how to assign pupil permissions](security-administration-for-families-and-pupils.md#security-administration-for-families-and-pupils).

### Individual Pupils

Navigate to the pupil’s profile and click on the “**Sign-Up**” link:

![](assets/screenshots/sign-up-module/sign-up-module-16.png)

The top of the page shows any recent and upcoming events that the pupil has signed up for. Notice that for the last one, the pupil has signed up for it, but approval for the event is still pending.

Below this is a list of all sign-up events that the pupil can sign up for. Click on the “**sign up**” link next to any even to sign up.

Note that future appointments, for which bookings are not yet open, are shown, indicating when bookings will open and for how long. No sign up link is available for these.

If a pupil is already signed up for an event, they will see “**cancel**” next to the event. This will remove their names from the list.

Appointments that are full, and have no more space left, also have no option to sign up. Also note that if an event has a limit for the number of appointments that a pupil can sign up for, once they reach that limit all other appointments in that event are closed to them. If they cancel one appointment, however, they will then be able to sign up for another.

### By Class

Navigate to the **Classes** tab and under the **Sign Ups** heading, click on the option **Sign up for an event by class**.

Choose an event category, then the event and finally the appointment. The choose the class for which you want to sign up pupils. Note that if an event has specifically had classes specified for it, then only those classes will be available in the dropdown list.

Finally, click on the **sign up** link next to a pupil’s name to sign them up for the appointment.

If there is a limit to the number of pupils that can sign up to the appointment, the **sign up** links will disappear when the limit is reached.

Also be aware that in spite of a page reporting that an event has a number of spaces available, this does not take into account other staff members who might be signing up pupils concurrently.

Family sign-up events cannot be used here, because nobody signs up a pupil for them.

### On the Pupil Portal

Pupils sign themselves up on the pupil portal. On their card, under the **General** heading, they click **View sign-ups**, open an event and click **sign up** next to an appointment. They can **cancel** or **withdraw** a sign-up until bookings close. Parents see the same **View sign-ups** option on each child’s card, so a parent can also sign a child up for a pupil event.

The option appears only if the pupil’s login group has the **View and allow sign-ups** permission ticked for pupils, or for families in the parents’ case. See [Managing Permissions](security-administration-for-families-and-pupils.md#managing-permissions).

The steps that pupils and parents follow are described in [Sign-ups: A Guide for Parents and Pupils](sign-ups-a-guide-for-parents-and-pupils.md#for-pupils-signing-yourself-up). You can send that page to pupils and parents.

## Family Sign-ups

Some bookings are made by parents rather than by pupils. The clearest example is a parent-teacher evening: the family books a meeting with a teacher, and the meeting is about their children rather than something a pupil attends. For these, set **Sign up by** to **Family (a family signs up, no pupil recorded)** when you [create the event](#creating-events).

A family sign-up differs from a pupil sign-up in these ways:

-   **The family books as itself.** No pupil is recorded against the booking. Wherever ADAM shows a family booking to staff, it lists the family’s children that the booking concerns, with their grades. If the event is limited to classes, these are the family’s children who are currently in those classes. Otherwise, they are all the family’s children.
-   **Only families with a child in the selected classes can book.** If **Limit to classes** is left empty, every family can book.
-   **The limit is per family.** **Limit per family** sets how many appointments one family may book for the event. **Limit pupil signups** does not apply.
-   **Only the organiser can approve.** A family event can require **Approval by organising teacher required**, but not the approval of another subject teacher.
-   **Only the booking family is told.** Reminders, approvals and cancellation notices go to the family that made the booking and to no other family. Where a pupil’s parents are separated and each has their own family login, one parent cannot see, cancel or be reminded of the other parent’s booking.
-   **Pupils never see family bookings.** Family bookings do not appear on the pupil portal.
-   **Family events cannot be used to sign up a class** or to add attendees to a class.

Once an event has bookings, you cannot change **Sign up by**. The edit form shows the current setting and the message “Cancel the existing bookings before changing who signs up.”

### Giving families access

Families book on the family portal. Their login group needs the **View and allow sign-ups** permission, the same one that lets pupils sign up. See [Managing Permissions](security-administration-for-families-and-pupils.md#managing-permissions).

### Booking on the Family Portal

Parents book family events on the family portal, under the **Family** heading, by clicking **Family sign-ups**. The page lists the family’s bookings under **Your family’s sign-ups** and the events open to the family under **Sign Up for Other Events**. Parents click **sign up** to book, and **cancel** or **withdraw** to cancel. Once bookings close, a family can no longer cancel online and must contact the school. You can then [remove the booking](#seeing-who-has-booked) for them.

The steps that parents follow are described in [Sign-ups: A Guide for Parents and Pupils](sign-ups-a-guide-for-parents-and-pupils.md#for-parents-booking-for-your-family). You can send that page to parents. For the permission that families need, see [Giving families access](#giving-families-access).

### Seeing Who Has Booked

On the list of appointments for a family event, click on the **number of attendees** as usual. This needs the **View Appointment Attendance** permission. For a family event the list has these columns:

-   **Family:** the family that booked.
-   **Pupils:** the family’s children that the booking concerns, with their grades.
-   **Details:** when the family booked and, if the event needs approval, who approved it and when.
-   **Actions:** **remove** cancels the booking and tells the family it was removed. If the booking is waiting for approval and you may approve it, **approve** and **reject** also appear.

The link **Scratch list of the pupils** opens a scratch list of every child the bookings concern.

### Booking for a Family

Staff can book an appointment on a family’s behalf, for example when a parent phones the school. On the attendee list of a family event, click on **Book a family**, search for the family by either parent’s first or last name, and choose the family from the results.

This link is shown to staff with the **Manage Events** permission, and to the event’s organiser if they have the **Manage Own Events** permission. When staff book for a family, ADAM ignores the booking dates and the family’s limit. Only staff with **Manage Events** can book a family into an appointment that is already full.

### Approving Family Bookings

If a family event needs the organiser’s approval, the organiser receives an email when a family books, with a link to the approvals page. On the **Pupils** tab, under the **Sign Ups** heading, click on **Approve signups**. Family requests appear next to pupil requests. The **Attendee** column shows the family name followed by the children the booking concerns. Click **approve** or **reject**. The family receives an email either way.

The organiser needs the **Approve designated signups** permission. Staff with **Approve any signups** can approve any family booking.

### Family Bookings on a Pupil’s Profile

On a pupil’s **Sign-Up** page, the heading **Family bookings about this pupil** lists the family events booked by any of the pupil’s families that concern this pupil. It shows the event, the appointment, and which family booked it. The heading appears only when there is at least one such booking.

### Family Bookings in Reports

The sign-up reports list family bookings against each child they concern, followed by the family’s name in brackets, for example “(Smith family)”. A family with two children in the report therefore appears on two rows. Do not add up the rows to count family bookings.

### Emails for Family Sign-ups

Family sign-ups use their own [email message templates](email-message-templates.md#email-message-templates), in the **Signup Module** section:

-   **Family Signup Approval Request (to Staff)** — sent to the organiser when a family books an event that needs approval.
-   **Family Signup Notification (to Staff)** — sent to the organiser each time a family books or cancels, if **Notify teacher on each sign-up** is set to “Yes”.
-   **Family Signup Approved (to Families)** and **Family Signup Not Approved (to Families)** — sent to the family when the organiser approves or rejects its booking.
-   **Family Signup Removed (to Families)** — sent to the family when staff remove its booking.
-   **Family Signup Appointment Cancelled (to Families)** — sent to each booked family when an appointment or the whole event is cancelled.

The reminder before the appointment uses the existing **Signup Notification (to Families)** template.
