# TODO: Outstanding Documentation Work

Most of this file is **screenshots** that the manual needs but does not yet have, or has in a form
that no longer matches ADAM. Each entry says which page the image belongs to, how to get to the
screen, what to frame, and what the data on screen should look like.

The last section, [Missing Written Content](#missing-written-content), is for features that the
manual does not cover at all and that need a page or a section written first.

**Remove an entry from this file as soon as it is done** — a completed task must not be left here.
The whole file can go once it is empty.

Two standing rules from [`CONTRIBUTING.md`](CONTRIBUTING.md) apply to every screenshot below:

- Capture against the **demonstration school**, never a live site. No real pupil, family or staff
  information may appear.
- Save each image at the given path under `docs/assets/screenshots/`, and add the `![](...)`
  reference to the page at the point described.

Most pupil screenshots in the manual use the demo pupil **Brandon Dayne Jarred Clark** (admin number
48619), but the Profile Overview Layouts captures were taken against **Riley Anderson** (admin
number 99726). Reuse Riley Anderson on that page and Brandon Clark elsewhere, so that each page at
least reads as one continuous example.

Neither pupil exists on the demonstration server any more: the school was regenerated before
2026-09-16. Existing images keep them, but new captures need a pupil who is there. The medical
captures use **Edward Clark** (pupil 5083, Grade 9 IM5).

---

## Online Applications (`docs/online-applications.md`)

The way an application begins has changed, and the written page now describes the new screens. Four
images have been captured against the demonstration school and are in place: the opening form
(`online-applications-04.png`), the page shown after it is submitted (`online-applications-05.png`),
the confirmation screen an existing parent sees (`online-applications-17.png`) and the portal card
that starts an application without an emailed link (`online-applications-18.png`).

`online-applications-06.png` showed the old "choose the number of children" screen, which no longer
exists in ADAM, and the file has been deleted.

Two images are outstanding.

### 1. The start email — `online-applications-07.png` needs recapturing

The image now in the file is not a start email at all: it is the old plain-link **New Application**
email (the second email, which says the link stops working after 7 days). The current **New
Application** template uses a **Continue Application** button instead. The image sits under the
paragraph about the two start emails, so the replacement must be a start email.

The email that carries the first link is now one of two templates, and the existing image shows
neither. Capture the **Start an Application (Existing Parent)** message as received, since that is
the one whose wording matters most — it reaches somebody who may not have asked for anything, and it
says so. Frame the greeting, the **Start Application** button and the sentence about ignoring the
email.

This one cannot be captured from ADAM itself: the message only exists once it has been delivered.
The demonstration families' addresses are all `testing+…@adam.co.za`, so whoever can read that
mailbox can capture it. Trigger it by entering the ID number of a demonstration parent on
**/apply** — the link is then emailed to the address on file for that parent, not to the address
typed on the form. Note that ADAM sends at most three such emails per parent in 24 hours.

### 2. The thank-you screen — `online-applications-05.png` needs recapturing

The screen shown after the opening form is submitted has changed since this image was taken. It now
bolds the sentence beginning “If you are already a parent at …”, and adds: “This is for your
security and to protect your personal data… If you no longer have access to that email address,
please contact the school so that we can update your details.”

Capture it by submitting the form on **/apply**. Doing so sends a start email, so use the ID number of
a demonstration parent (the email then goes to their `testing+…@adam.co.za` address on file) and
capture image 1 from the same submission. Frame the whole message. The image is used on
`docs/online-applications.md` (*The Application Process: Procedure for Parents*); the parent guide
`docs/online-applications-a-guide-for-parents.md` leaves it out until it is current, so add it
there too, after the paragraph that begins “After you click **Next**, ADAM thanks you”.

---

## Two-Factor Authentication (`docs/two-factor-authentication.md`,
`docs/two-factor-authentication-for-administrators.md`)

`two-factor-authentication-05.png` (the phone-side authenticator app screenshot) has been checked
against the rebuilt page and still matches. `-07.png` and `-08.png` were the same file — the old
management screen — and have been deleted; the *Removing Two-Factor Authentication* section now uses
`-15.png`.

*The reminder on your dashboard* is deliberately without an illustration. The card could not be made
to appear on the demonstration server, and the section reads perfectly well without a picture, so
nothing is outstanding there.

---

## Medical Module — consultation form width (`docs/medical-module.md`)

All the medical screenshots are captured and in place. One thing is left to come back to, and it
needs development before it needs a picture.

At the manual's 900px capture width, the consultation form's middle column is `overflow: auto` and
scrolls sideways. The right-hand edge of the **Notes** box and the **Actions** column of the
**Medication** table run past it, so `medical-module-15.png` shows the form cut off on the right.
That is how ADAM draws the screen at that width, not a bad crop: the three-column layout (photograph,
form, allergies panel) does not leave the form enough room.

**Take to development:** the layout of **Add a Medical Consultation** at narrower widths — for
example, dropping the allergies panel below the form, or letting the form use the full width.
Once that changes, re-capture `medical-module-15.png` with the setup recorded in
`docs/assets/screenshots/medical-module/captures.yml`.

The off sport list (`-17.png`) has a related but separate problem: its table is 1286px wide, so it
was captured at 1340px, an exception to the house width. If development makes the consultation form
narrower-friendly, it is worth asking about that table at the same time.

---

## Name Pronunciations (`docs/name-pronunciations.md`)

Seven of the nine images this page needs are captured and placed; their setup is recorded in
`docs/assets/screenshots/name-pronunciations/captures.yml`. **Two remain, and both need a machine
this one is not.**

The recorder is built on an AudioWorklet. On the WSL2 machine the captures were run from,
`audioWorklet.addModule()` never settles — it neither resolves nor rejects, headless and headed
alike, on both bundled Chromium builds, with no CSP violation and no network request for the module.
`getUserMedia()` itself succeeds and the fake-device flags work, so this is not a permissions
problem: there is no audio device for Chromium's audio rendering thread to start on, and the worklet
global scope is never created. It is an environment limitation, not a fault in ADAM — the feature
works in an ordinary browser.

**Both images below therefore need capturing from a machine with a real microphone and working
audio**, driving the browser by hand if need be. No other setup is needed: these two images
are taken as staff, and a staff recording needs no portal permission.

Reach the recorder at **Pupils → Names and Faces → Record Name Pronunciations by Class**, choose
**Register Class: Grade 4 CM9** (class 17 — the class images 1 and 9 use), then
**Record the missing**. Frame the recorder card only, 8px padding, 900px viewport, and check the
page is in light mode first.

### 2. `name-pronunciations-02.png` — the recorder mid-recording

Capture the **Recording — say … now** state: the card with the pupil's name, that status line, and
the progress bar beneath it. The countdown state (**Get ready… 3**) is an acceptable alternative if
the five-second window proves too tight to catch — say which one the image shows when placing it.

It goes in the **How the recorder works** section, after the numbered steps.

### 3. `name-pronunciations-03.png` — listening back before saving

The same recorder in its review state: the playback control, the duration line, and the **Try again**
and **Save** buttons together. This is the step readers most need to see, because nothing is sent to
ADAM until **Save** is clicked, and the page says so.

It goes immediately after image 2, before the sentence about the five-second limit.

---

## Guides for Parents and Pupils — pictures still needed

The parent and pupil guides (issue 20) reuse the staff pages' screenshots. These were recaptured on
2026-11-17 against the Bhabha family (SJC Default permission group), and their setup is recorded in
each folder's `captures.yml`: `medical-module-09.png`, `online-agreements-09.png` to `-12.png`, and
`document-repository-08.png` and `-09.png`. The rest are below.

### 1. Goal Setting — `goal-setting-07.png` and `goal-setting-08.png`

Neither image is used any more. Both show goals that ADAM filled in by itself, with an “automatically
set by ADAM” note. ADAM no longer writes that note: it suggests a value beside each subject instead.
It does still pre-fill every goal with 60, which is a fault (see item 6 under *Portal faults found
while writing the parent guides*).
Recapture both, keeping the filenames, and place them in
`docs/goal-setting-a-guide-for-pupils-and-parents.md`:

- `goal-setting-07.png` — the **Academic Goal Setting** page as a pupil sees it while the window is
  open: the “Goals and strategies for …” message, and the **Subject**, **Goal**, **Strategy** and
  **Actions** table with **edit** links. Place it after the paragraph that ends “…an **edit** link
  in the **Actions** column.”
- `goal-setting-08.png` — the form opened by **edit**: two or three subjects, each with a goal box,
  the “Based on your past performance in …” suggestion and the **My strategy to reach this goal:**
  box, and **Save**. Place it after step 3 of *Setting Your Goals*.

**Setup needed, and it cannot all be undone.** On **Reporting → Reporting Period Administration**,
set the pupil’s grade to set goals in **Edit reporting period**, and open a **Capture Goals (for
pupils)** time frame in **Edit reporting period timeframes**. Use a pupil whose permission group
grants **Capture academic goals** to pupils. Opening the page creates a goal row for each of that
pupil’s subjects, each set to 60, and goals cannot be removed from a reporting period once added (see the warning in
*Choosing Which Grades Should Set Goals*), so use one pupil and say which in `captures.yml`. Close
the time frame and reset the grade setting afterwards.

`goal-setting-10.png` (the mark book with the **Goal** row) is still used on both pages. Its
Afrikaans card shows the old automatic-strategy text; recapture it in the same session if the mark
book shows a goal.

### 2. Sign-ups — a picture of the pupil portal

`sign-up-module-18.png`, the family portal, is captured and placed at the end of *What the Family
Sign-ups Page Shows*. One picture is left.

Add `sign-up-module-21.png`: the **Sign ups** page as a pupil sees it from **View sign-ups**, with
**Signed Up Events for** listing one booking and **Sign Up for Other Events** with an event open, so
that the **Appointment**, **Booking** and **Actions** columns and a **sign up** link are in view.
The pupil’s permission group must grant **View and allow sign-ups** to pupils. Place it in *For
Pupils: Signing Yourself Up* of the parent guide, after the description of the page.

### 3. Document Repository — `document-repository-07.png`

The image on `docs/document-repository.md` (*Creating Upload Spaces*, after “…may look like this on
the parent portal:”) shows the old portal styling and the old **Upload documents** button. The
button now reads **Upload '<upload name>' documents**, and each document shows an *Accepted: …* line.
The paragraph above it describes one upload space asking for three documents. The demonstration
school’s spaces ask for one or two, so create a three-document upload space for families first
(through **Manage parent and pupil uploads**), capture the family upload page, then delete the space.

`document-repository-11.png` and `-12.png` are no longer used. They showed the rejected file in red
and the button reading “Documents too large for upload”, neither of which ADAM does now. Delete them
unless a new picture of the too-large state is wanted; the parent guide describes it in words.

### 4. Passkeys — optional

`docs/passkeys-a-guide-for-parents-and-pupils.md` has no pictures and reads well without them. If
pictures are wanted, the two that would help are the “Log in with your fingerprint or face” card on
the portal home page and the **Passkeys** page with one passkey listed. The card is hidden on “Login
as a family” sessions, so it needs a real parent login, not the staff impersonation used above.

---

## Pupil Comments — an AI summary (`docs/pupil-comments.md`)

The *AI Summaries* section has no picture of a summary. Add `pupil-comments-06.png`: the
**Summary** block above a pupil’s comments on the **Comments** tab of the **Pupil’s Info** page,
with the note under it that names who wrote it. Place it after the first paragraph of
*AI Summaries*.

It could not be captured on 2026-11-24. The randomiser blanks every stored summary
(`ai_summary.ai_response`), so no pupil on the screenshot site has one to show, and a new one needs
ADAM’s in-house assistant to answer the screenshot site. Ask the developer how to get a summary
written for a pupil with randomised comments, then capture it as a staff member with the
**View AI Summary** permission.

---

## Sandbox Sites — the banner (`docs/sandbox-sites.md`)

The page has no pictures. Add `sandbox-sites-01.png`: the **Sandbox** banner at the top of a staff
page, with enough of the page below it to show that it sits above ordinary content. Place it in
*Recognising a sandbox*, after the quoted banner text.

**The screenshot site is not a sandbox.** The banner shows only when the site's configuration sets
`env = sandbox` and `sandbox_source`. Do not set these on the screenshot site's own configuration
without the developer: `sandbox:prepare` deletes the contents of folders the configuration names,
and the banner prints the `sandbox_source` host, which must not be a real school's address. Ask for
a sandbox of the demonstration school, then capture it.

---

## Logging on as a Parent — the reset email (`docs/logging-on-to-adam-a-guide-for-parents.md`)

Issue 24 recaptured every other image on the page. `logging-on-to-adam-a-guide-for-parents-06.png`
still shows the old email from “Random High School”, in an old mail client.

The screenshot site cannot produce the email yet. The randomiser replaced the body of the
password reset email template with placeholder Latin, so the email that reaches Mailtrap has no
greeting, no text and no link. Restore the template first: open it in ADAM's email message editor
(the `family_passwordreset` message, and `family_password_new` for a parent without a password)
and click **Restore default**. Then request a link through **Parent Login → New
account? Forgotten password?** with ID number `123456789` (Dr Alec van der Merwe, family 2304), and
capture the email as it appears in Mailtrap. It must show the school name and a
`testing+…@adam.co.za` address only. The capture browser cannot reach Mailtrap, so this capture
needs a person.

---

## Email Personal Documents — pictures (`docs/email-personal-documents.md`)

The page was written from ADAM PR #643 (`feature/document-emailer`) before it reached the branch the
screenshot site serves, so it has no pictures. Capture these once the feature is on that branch.
Emailing a set from the screenshot site queues real mail batches, so ask the user before any send.

1. `email-personal-documents-01.png`: **Pupils → Messaging and Communications → Email personal
   documents → Upload documents**. Frame from the **Upload Documents to Email** heading to the
   **Upload Documents** button, with **Who the documents are for** on **Current pupils**. Place it
   after the numbered steps under "Uploading the Documents".
2. `email-personal-documents-02.png`: the email form of a set of about five current pupils' documents,
   before its first send. Frame from **To** down to **Description**, so that **Audience**,
   **Document Repository Category** and **Description** show. Place it after the list of
   differences under "Emailing a Set".
3. `email-personal-documents-03.png`: the set's page of the same set after one send to
   **Families**, showing at least one **Queued** row and one **Not sent** row with its reason. Place
   it after the list of outcomes under "The Set's Page". This needs a real send, so it waits until
   the user agrees to one on the screenshot site.

## Pictures made out of date by the text corrections of 2026-11-18

The text of these pages was corrected against ADAM on 2026-11-18. The images below still show the
old screens. Recapture each on the screenshot site under the same file name.

- `medical-module-03.png` (*Adding and Editing Medical Examination Types*): the example is a
  “Covid-19: Self-declaration Form”, which the rewritten section no longer uses. The help text under
  **Allow Completion via Parent and Pupil Portal** now says “permissions … pupil permissions groups”,
  not “privileges … pupil privilege groups”. Capture the **Add** form for an ordinary examination
  type, such as a height and weight check.
- `online-agreements-01.png` (*Creating Online Agreements*): has no **Agreement is Rescindable** row.
  Choose an audience with “by” in its name, such as **Families (by Pupil Grade)**, so that its
  selection field shows as well.
- `online-applications-13.png` (*Application Process: Procedure for Staff*): dates from 2018. The
  current **Manage Online Applications** page has an **Unconfirmed Applications** table, **Email**
  and **Phone** columns, and **resend link**, **edit** and **expire** on incomplete applications. The
  old image also shows a staff member's own name as a family name.
- `roll-calls-13.png` (*Configuring Roll Calls*): the **Roll Call** heading on the **Attendance**
  tab now starts with **Cron interval (minutes)** and ends with **Reason to show for Leaves** and
  **Reason to show for Off Sport**. The image has none of the three.
- `goal-setting-01.png` (*Permissions required for Goal Setting*): says “privilege” where ADAM now
  says “permission”. Wait until the **View academic goals** help-text fault below is settled, or the
  new image will show the misleading description.
- `sign-up-module.md`: the images date from 2015 and use the old styling.
  - `sign-up-module-04.png` (the **Create New Event** form) has no **Appointment Type**, **Sign up
    by**, **Limit per family**, **Send confirmation reminders to** or notify fields, and shows
    **Category** as a drop-down. On the create form it is now read-only text.
  - `sign-up-module-06.png` and `-07.png` (team or group appointments) have no **Finish Date** or
    **Finish Time** columns.
  - `-06`, `-07`, `-08`, `-09` and `-11` show a “del” link instead of the bin icon, and a “No limit”
    option where the form now offers “Unlimited”. `-10`, `-12` and `-13` were not checked and are
    probably the same.
  - `sign-up-module-15.png` (the appointment list) has no **Add new appointments**, **Copy
    appointments from another event** or **attendees** link.
  - `sign-up-module-05.png` (the old type-choice screen) and `sign-up-module-14.png` (the old
    confirmation screen) are no longer used by the page. Delete the files.

---

# Missing Written Content

## Parent and Pupil Portal — Today's Birthdays (`docs/parent-and-pupil-portal.md`)

The new **Today's Birthdays** section is written but has no images. It needed three: the permission,
the settings, and the result as a parent actually sees it. The permission is captured; the settings
and the parent's-eye view remain. The feature is off by default on the demonstration school, so each
capture needs setting up first.

Image 1 was captured against the **Full Access** pupil login group, chosen because it was the only
login group with any pupils assigned. Use the same group for images 2 and 3 — item 3 needs a parent
login, so keeping the group consistent across all three matters.

Grant **View birthdays** to the login group that the demonstration families use, and set
**Birthdays visible in the portal** to **All pupils in the school** before capturing — at the
default class scope, a demonstration login will usually see nobody and the section will not render
at all.

### 2. `parent-and-pupil-portal-11.png` — the list as a parent sees it

**Families → Security → Login as a family** for a demonstration family with more than one child, so
that the birthday card can be seen sitting *below* the children's cards — that placement is the
point of the image and is easy to lose by cropping too tightly. Frame the foot of the portal front
page: the last child's card, the **Family** and **Security** menu, and the **Today's Birthdays**
card. Photographs off and names abbreviated, matching the defaults in image 2.

**Blocked on demonstration data, and this is the setup it needs first.** No family on the
demonstration school currently satisfies the brief. `pupil_login_privileges` puts only three pupils in
the **Full Access** group, and just one of them, **Riley Anderson** (pupil 4753, family 1902), is a
current pupil — an only child. Every other family, including the two-child families, gets *"your
profile has not been granted access to any pupil information"* on logging in, so there are no
children's cards for the birthday card to sit below.

Pick a family with two current children — **de Villiers** (family 3090: Owen and Sheryl) is one — and
put **both** children into the **Full Access** pupil login group, so the portal renders two cards.
Keep to Full Access, so all three birthday images stay on one group.

The settings side is already done and needs no repeating: **Birthdays visible in the portal** is
**All pupils in the school**, photographs are **No**, names are **First name and surname initial**.
Two pupils genuinely have a birthday today, so no date of birth needs moving — but note that the two
with birthdays are **Yasmin Butcher** and **Coral Till**, in other families, which is exactly why the
school-wide scope matters for this image.

## Staff pages — wording still to correct

The corrections found while writing the parent guides (issue 20) were made on 2026-11-18, except
these:

- `docs/goal-setting.md`, *Capturing Goals: Instructions for Pupils* (line ~105): “Goals start
  empty” is wrong today: every goal opens at 60 (see item 6 under *Portal faults*). Say what the
  pupil sees once that fault is settled.
- `docs/sign-up-module.md`, *Seeing Who Has Booked* and *Booking for a Family*: the **attendees**
  link appears only once an appointment has at least one booking, and the attendee list is the only
  way to reach **Book a family**. So staff cannot make the first booking for a family appointment,
  and the page now says a parent must make it in the portal. Decide with development whether the
  link should always show for family events. If it changes, update both sections.

---

## Portal faults found while writing the parent guides (for development)

None of these is documented as a feature. The guides are written so that they stay true after each
is fixed; check the wording named against each when it is.

1. **Online Applications — the form link ignores the expiry setting.** The emailed application-form link is
   fixed at 7 days and 20 opens (`ApplicationStartConfirmation.php:30-31,144-145`, the staff
   **resend link** at `OnlineApplications.php:405-407`, and an application started through the API
   at `Applications.php:567-572`), whatever **Expire applications (days)** is
   set to. The default **New Application** email promises `{expiredays}` days, so a school that
   sets 14 days promises 14 and the link dies at 7. Reminder emails already set the link to last
   until the application expires (`ApplicationReminders.php:206-215`).
2. **Online Applications — a misleading message.** An expired, rejected or approved application
   opened through a working link says “Sorry - this application has already been submitted.”
   (`OnlineApplicationFlowController.php:294,404,503,661,918`). The parent guide tells parents who see it without having submitted to
   contact the school.
3. **Document uploads — no size warning on the family page.** The family upload page does not load
   `filesize.js` (`DocRepExternalUpload.php:479-482`); only the pupil page does (line 295). A
   too-large family document gets no pop-up and is refused after it is sent.
4. **Sign-ups — pupil bookings.** A pupil-path booking that fails because the appointment is full
   shows no message (`AppointmentActionController::signUp`). The per-event limit for pupils is only
   enforced by hiding the link; `signUpForAppointment` does not check it. A family booking that
   needs approval still says “Your family is booked for this appointment.”
5. **Medical — graphs.** `Metrics::fetchMetricsWithGraphs` ignores **Graph Type**, so the portal
   graphs every metric with readings; text and choice readings plot as 0. A pupil with no
   examinations of a published type can get graphs from other types under its heading.
6. **Goal setting.** `Goals::getRecommendedGoal` passes the period as the subject to
   `Reporting::getRecentTermResults`, so the term-results fallback looks up the wrong subject. The
   deadline line joins `diffForHumans()` with “ to go”, giving “… from now to go.”

   Found on 2026-11-17 while capturing: goals do not start empty. `Goals::ensureDefaultGoals`
   (`Goals.php:789`) inserts each goal row without `goal_result`, and the column defaults to 60
   (`database/datainstall.sql:141`). So every subject opens at 60, both on the **Academic Goal
   Setting** list and in the form. `Goals::setDefaultGoals` sets the result to `null` explicitly,
   which suggests empty was the intent. The form’s opening paragraph (`Goals.php:451`) also shows a
   stray backslash, “if you don\'t agree”, because the apostrophe is escaped inside a double-quoted
   string.
8. **Sign-ups — family events offer “add to classes”.** On **View appointments**, a family
   appointment with a booking shows an **add to classes** link (`Appointments.php:1273-1278`). It
   checks only that there are attendees and that the user holds `signup_classregistration`, not
   whether the event is a family event. The manual says family events cannot be used to add
   attendees to a class. The link leads nowhere: every step of the enrolment flow refuses a family
   event and returns to **View appointments** with “Family sign-up events cannot be used for class
   sign-up or class lists.” (`AppointmentAdminController.php:202-207`). The design spec
   (`docs/superpowers/specs/2026-06-23-family-signup-staff-side-design.md:79-83`) says to hide the
   link for family events, and the plan has a `!$isFamily` guard that did not ship. This one is on a
   staff screen, not the portal.
7. **Passkeys — wording.** The **Passkeys** page tells users to use the “Sign in with a passkey”
   button (`PasskeyManagementView.php:79`); the button on the log-in pages reads **Log in with a
   passkey**. The manual uses the button's label.

---

## Faults found while correcting the staff pages on 2026-11-18 (for development)

1. **Medical — staff instructions are never shown.** The examination type form saves **Instructions
   shown to staff** (`ExamTypesController.php:52`), and its help text says they appear at the top of
   the staff form. Nothing reads `type_instructions_staff`: the staff examination form and Health
   Monitoring show no instructions. `docs/medical-module.md` carries a warning. Remove it once fixed.
2. **Online Agreements — applicants never see Acceptable Responses.** The application flow always
   shows the two standard buttons (`OnlineApplicationFlowController.php:213-219`); the portal uses
   the school's own responses (`OnlineAgreements.php:368-397`). `docs/online-agreements.md`
   describes **Acceptable Responses** with no exception. Decide whether this is intended, then
   document it or fix it.
3. **Goal setting — the View academic goals help text.** It says the permission lets pupils and
   parents see goals against their results (`Goals.php:329`). In the portal it only affects the API
   (`PortalResultsController.php:182`). The help text should say so.
4. **Sign-ups — a typo.** The **cancel** confirmation says “has bee cancelled”
   (`Appointments.php:1255`).
5. **API — Families/email.** `Families/email:get` returns `email_modify` in ISO 8601 through the
   DTO; `Families/email:patch` returns the raw row, presumably `Y-m-d H:i:s`. Neither format was
   tested against a real response. `Families/email:get` with a member other than primary or
   secondary reaches an unhandled `match` (`FamilyEmail.php:579`) and probably returns 500.
6. **Sign-ups — the add to classes form.** The help text for **Remove all current enrolments for
   the class** says that pupils “who are not in the list below” are removed. The code removes every
   pupil in the class who is not *ticked* (`AppointmentAdminController.php:333-342`), so an attendee
   who is unticked and already in the class is removed too. After **Enrol pupils**, ADAM always
   says “The enrolments have been made.”, even when it skipped pupils who are not current or who
   are in another class of the subject. **Subject registrations for a class** reports the real
   count instead. `docs/sign-up-module.md` (*Adding Attendees to a Class*) describes what the code
   does.

---

## Staff detail updates — the undo is still missing

The two faults found while capturing `staff-information-23.png` on 2026-08-26 are fixed in the
application, and this page is written against the fixed behaviour:

- staff who lack `staff_edit_own` are no longer offered on **Request staff detail updates**, and a
  note above the list accounts for them; and
- the ADAM home page no longer redirects a staff member to a prompt that would refuse them, so a
  request made before the permission existed simply waits instead of breaking the page.

---

## Sign-up categories — the default limit is a Yes/No (for development)

On **Manage event categories → Add new Sign-up Category**, **Default Appointment Limit** is drawn as
**Yes**/**No** radio buttons (`CategoryController.php:46`, `RadioOptions::getYesNoElement`). The
column it saves, `category_default_appointment_limit`, is a number, and the appointment forms read
it as the default limit (`AppointmentController.php:297`). A school cannot enter a number, so the
field cannot do what its help text says. Found on 2026-11-18 while setting up the family sign-up
captures. `docs/sign-up-module.md` still describes the field as a default limit; check that
sentence once the control is fixed.

---

## Off Sport — a new question for development

Found while capturing `medical-module-18.png`, after the answers above came back, so it is not on
`fix/medical-module-permissions`.

`OffSportController::index` adds a script that copies an off sport type's `offsport_type_absent`
default into **Counts as Absent for Roll Call** when a **Type** is chosen. The script selects
`input[name='offsport_type_id']` and `input[name='offsport_absent']`, but the DataEditor form names
those controls `edit[offsport_type_id]` and `edit[offsport_absent]`. The selectors match nothing, so
choosing a type never changes the absent setting. Confirmed in the browser on the dev instance: the
page has no `offsport_type_id` inputs, only `edit[offsport_type_id]` ones.

`docs/medical-module.md` now says the default is not copied across and tells staff to set the field
by hand. `docs/roll-calls.md` no longer mentions the default at all. Once the selectors are fixed,
put the sentence back: choosing a **Type** sets **Counts as Absent for Roll Call** to that type's
default, which can still be overridden.

(Every type on the demonstration school defaults to **No**, so a picture could not show the fault or
the fix without changing a type first.)

---

## Off Sport Alerts — an alert with no staff shows "Unknown"

Found while creating demonstration data on 2026-09-16; not on `fix/medical-module-permissions`.

On **Manage Off Sport Alerts**, an alert that emails subject teachers but no named staff lists its
recipients as "Unknown, Grade Tutor, Register Class", with **Unknown** linked to an empty
`mailto:`. `Alerts::displayAlerts` runs `Validation::safeInt (explode (":", $alert ['alert_email']))`:
an empty string becomes `[0]`, and the following `if ($staff != '')` is true for `0` under PHP 8's
comparison rules, so it prints `StaffMember::getName (0)`. The same pattern guards the subjects loop.

Worth checking whether `AlertData` has the same fault when it builds the emails, since an alert with
no named staff is an ordinary way to set one up. The manual does not mention it; the screenshot was
taken after giving the alert a named staff member.

---

## Operations and Vaccinations — the "or new:" category is discarded

Found while creating demonstration data on 2026-09-16; not on `fix/medical-module-permissions`.

On **Manage Medical Operations and Vaccinations**, a category typed into the **or new:** box is lost:
the entry saves under **Unknown**. `MedicalAdminController::interventions` reads
`$data [0] ['intervention_category_new']` in its `setProcessData` callback, but
`DataEditor::saveNew` first runs the posted fields through `filterInputFields`, which keeps only the
editor's own entry fields. `intervention_category_new` is not one — it is a sub-control inside the
**Category** `CombinedFields` — so it is gone before the callback sees it, and the callback's fallback
sets **Unknown**. A school starting with an empty list has no way to create a category.

`docs/medical-module.md` now carries a warning to this effect. Remove it once fixed, and restore the
sentence saying a category can be typed into **or new:** to start a new one.

---

## API pages — the portal and profile endpoints are undocumented

`scripts/audit_api_endpoints.py`, run on 2026-11-18, reports 48 undocumented endpoints: every
`portal/*` endpoint and `profile/me:get`. No page declares the `portal` or `profile` prefix. Decide
where they belong (see the `auditing-api-docs` skill) and write the entries.

---

## Pupils/image:get — the `Content-Type` header is wrong (for development)

This is an ADAM code issue, not a documentation one. `DocRep::getApiImage` sets the response's
file type from the uploaded document's `document_filetype` (`DocRep.php`, lines 1504 to 1506),
but the bytes it sends come from `ThumbnailStore`, which always renders a PNG (`imagepng`). A
photograph uploaded as a JPEG is therefore sent as PNG data with `Content-Type: image/jpeg`.

`docs/api-pupils.md` already warns readers to treat the data as PNG and not to trust the header.
Once ADAM sends `image/png`, remove that warning.

## Result and Aggregate Audit — faults found while capturing (for development)

These are ADAM issues found on the screenshot site while writing
`docs/result-and-aggregate-audit.md`. They were seen on pupil 5250, College Trinity Term 2026
(period 48), on the `development` branch at commit 1c33fc7896.

1. **Question: should the overview's Academic Progress Menu still need the subject progress
   permission?** `PupilScreenRenderer` shows the **Academic Progress Menu** widget only to staff
   with **View a Subject Progress Graph for a pupil**. The menu now leads to the audit and the two
   history pages, which need no such permission, so a staff member who can see the academic
   records but not the graphs does not get the menu on the overview. The issue (#21) said the
   entry appears "in the academic progress block on the pupil overview" without that condition.
   The manual describes the current behaviour. If the condition is dropped, remove the sentence
   about it from the "Opening the Audit" section.
