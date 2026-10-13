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

One image is still outstanding.

### 1. The start email — `online-applications-07.png` needs recapturing

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

---

## Profile Overview Layouts (`docs/profile-overview-customisation.md`)

The demonstration school now has three pupil layouts — **Default** (the default), **Admin Layout**
and **Medical** — and they appear in the captures already in the manual. Use the same three for
anything below.

### 1. The **Move selected to:** control — still needs a picture

`profile-overview-customisation-15.png` is captured and in place. It shows the **Pupil Overview: who
uses what** heading, the sentence about moving someone, the table, and all three **How** states —
**own choice**, **assigned** and **following the default** — which was the point of it.

What it does not show is the **Move selected to:** control and its **Move selected** button. Those sit
at the foot of the screen, and with 97 staff on the demonstration school and no filter on the list,
they are some 3,900px below the heading. One image spanning both would be an unreadable strip.

**A decision is needed** rather than another capture attempt: either add a second image (say
`profile-overview-customisation-17.png`) framing just the **Move selected to:** control at the bottom,
placed in *Seeing and Changing Who Uses What* after the paragraph that describes it, or accept that
the control is adequately described in prose and drop the requirement.

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

## Messaging Centre — audiences and the admissions filter (`docs/messaging-centre.md`)

Two new sections were written without pictures: *Choosing an audience* and *Messaging applicants and
their parents*. Neither is unreadable as it stands — both are lists and steps rather than screens
that need pointing at — but the manual illustrates every other stage of the messaging flow, so these
two look bare by comparison.

The existing captures on the page run `messaging-centre-02.png` (choosing a module) straight to
`-03.png` (choosing a subject), which is exactly the step the *Choosing an audience* section now
describes. Number the new images from `-20.png` upward rather than renumbering the existing set.

### 1. The audience list — `messaging-centre-20.png`

**Admissions tab → Messaging and Communications → Messaging Centre for Admissions**, or open the
Messaging Centre from any tab and choose the Email module. The screen shows the sentence *"Please
select an audience to send your email to:"* — the wording names the module, so an SMS module reads
*"...your SMS to:"* — followed by the audiences the signed-in user may use.

Capture it as a user holding **all** of the messaging permissions, so that every audience appears —
**Pupils by class**, **Pupils by grade**, **Pupils by filter**, **Staff**, **Admissions**,
**Admissions by filter**, **Alumni** and **Leavers**. A shorter list would be misleading, because the
text explains that the list varies with permissions. Frame the heading and the full list of links.

Place it in *Choosing an audience*, immediately after the sentence quoting the prompt.

### 2. The admissions filter builder — `messaging-centre-21.png`

**Admissions tab → Messaging and Communications → Messaging Centre for Admissions (by filter)**.

Build a filter that matches a believable handful of demonstration applicants — a criterion or two, not
an empty form and not the whole intake — and click **Update the filter** so the capture shows the
result. Frame the criteria table, the **Update the filter** button, the sentence reporting how many
records match, the names listed beneath it, and the **Next** button at the foot with its count.

That single image carries the whole section: the builder, the running count, the name check and the
way out. Place it in *By filter*, after the paragraph that ends "...as many times as you need."

> [!NOTE]
> The demonstration school must have applicants with enough variety to make a meaningful filter —
    check that **Admissions → Lists and Labels → Admissions scratch list using filters** returns rows
    before setting up the shot. If it does not, the demonstration data needs seeding first and that
    is the blocker, not the screenshot.

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

Six of the eight images this page needed are captured and placed; their setup is recorded in
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
audio**, driving the browser by hand if need be. Everything else is already set up: the
demonstration school has recordings in place, and the **Record name pronunciation** permission is
already granted to the **Full Access** pupil login group for both Pupils and Families.

Reach the recorder at **Pupils → Names and Faces → Record Name Pronunciations by Class**, choose
**English Home Language: Grade 8 CC6** (class 7412 — the class the other images use), then
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

## Sign-up Module — family sign-ups (`docs/sign-up-module.md`)

The **Family Sign-ups** section is written but has no pictures. **Capture these only once ADAM PR
#496 has been deployed to the demonstration server**: before that, no family sign-up screens exist
there. Set up one family event first: on **Pupils**, under **Sign Ups**, choose **Manage events**,
pick a category, and add an event named "Parent-Teacher Evening: Mrs Smith" with **Sign up by** set
to **Family (a family signs up, no pupil recorded)**, **Appointment Approval** set to **Approval by
organising teacher required**, and a few ten-minute appointments with bookings open. Give the
**View and allow sign-ups** permission to the family login group the demonstration families use.
Book two families, one of them from the family portal and one with **Book a family**, and leave
one booking unapproved.

### 1. `sign-up-module-17.png` — the event form

The **Create New Event** form, framed from **Event information** to **Limit to classes**, so that
**Sign up by** and **Limit per family** are both in view with **Family** chosen. It goes after the
**Limit per family** bullet in **Creating Events**.

### 2. `sign-up-module-18.png` — the family portal

The **Family Sign-ups** page as a parent of one of the booked families sees it, showing **Your
family's sign-ups** with the booking and **Sign Up for Other Events** with the event open. It goes
at the end of **Booking on the Family Portal**.

### 3. `sign-up-module-19.png` — the attendee list

The attendee list of the booked appointment, showing the **Book a family** link and the **Family**,
**Pupils**, **Details** and **Actions** columns, with **approve** and **reject** on the unapproved
row. It goes after the list of columns in **Seeing Who Has Booked**.

### 4. `sign-up-module-20.png` — approving a family booking

The **Approve signups** page with the unapproved family booking, so that the **Attendee** column
shows the family name and its children. It goes at the end of the first paragraph of **Approving
Family Bookings**.

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

## Staff detail updates — the undo is still missing

The two faults found while capturing `staff-information-23.png` on 2026-08-26 are fixed in the
application, and this page is written against the fixed behaviour:

- staff who lack `staff_edit_own` are no longer offered on **Request staff detail updates**, and a
  note above the list accounts for them; and
- the ADAM home page no longer redirects a staff member to a prompt that would refuse them, so a
  request made before the permission existed simply waits instead of breaking the page.

---

## Heads of Subject — one question for development

The **Heads of Subject** section is now written, on `docs/subjects.md` between *Editing a Subject* and
*Changing the Order of Subjects*. The cross-links from `docs/mark-book-administration.md` and
`docs/reporting-period-administration.md` now point at it instead of restating the two-halves rule,
and both screenshots are captured and placed. One thing is left.

### Answered: `rep_aggregated_subject` follows teaching

Development confirmed that **Manage aggregated result calculations from subjects taught** is meant to
follow the subjects a staff member **teaches**. The section as written is correct, and its note
stays.

The permission has been taken out of `SubjectHeadController::SUBJECT_SCOPED_PRIVILEGES` on the ADAM
branch `fix/aggregated-subject-not-head-scoped`, which is not merged yet. Once it ships, saving a
head who holds only this permission shows the "no head-of-subject privileges" warning. If
*Heads of Subject* lists the permissions that stop that warning, make sure this one is not among
them. The original intention was a separate head-of-subject version of this permission. That has
not been built, so do not document it. Remove this entry once the page has been checked.

---

## Medical Module — answers from development

Development has answered all eleven questions. The fixes are on the ADAM branch
`fix/medical-module-permissions`, which is **not merged or deployed yet**. Until it reaches the
demonstration server, the screens still behave the old way, so change the pages when the branch
ships and not before. Each answer says what the page needs once it has shipped. Remove this section
once the pages match.

### Permission checks on the wrong permission — none of the four was intended

In every case the page itself checked the right permission and the menu or link did not. The menus
and links now match their pages.

1. **Consultation Report** now appears to anyone with `medical_view`
   (**View medical information**). That is what the report page has always required.
   `medical_exams_add` has nothing to do with it.
2. **Add a new off-sport entry** on the pupil's **Off Sport** tab now needs
   `medical_offsport_manage`, like every other off sport control.
3. The three **stock transaction report** menu options now need `medical_transaction_view`
   (**View Medical Transactions Report**). The fault also ran the other way: staff with
   **Manage Medications** saw the three options and were refused on clicking them. *Change needed:*
   remove the caveat from `docs/medical-stock.md`. The reports need **View Medical Transactions
   Report** alone, and **Manage Medications** no longer shows them.
4. A staff member's **Medical Records** section now needs `medical_view_staff` throughout, for the
   photograph as well as the **Consultations** tab. `medical_view` is the pupil permission and no
   longer affects staff records. *Change needed:* remove the caveat and the advice to grant both.

A fifth menu option had the same fault: **View All Consultations for Chargeable Entities** checked
`medical_consultations_add` while its page checks `medical_view`. It now checks `medical_view`. If
the manual says who can see that option, check the wording.

### The portal refuses report viewers — fixed

Each portal action now checks its own permission. **View Medical Examination Reports** needs
**View medical reports** only, and completing an examination needs **Complete medical exams** only.
Before the fix, **Complete medical exams** on its own also let a login read the reports by typing the
address. *Change needed:* remove the warning under *Parents and Pupils Viewing Their Results*.

### Two fields labelled "Transaction Type" — fixed

The second field now reads **Stock Group** on both reports. *Change needed:* remove the note and use
**Stock Group** as the field name.

The by-item report leaving out the stock group filter is deliberate. You choose one stock item, and
an item belongs to exactly one group, so the filter would add nothing.

### The Group radio on the stock item form — works, no caveat needed

Editing a stock item's group saves correctly. The form code renames every field to its own column
before the page is drawn, so the wrong name in the constructor never reached the browser. The only
effect was a duplicated HTML id, which is now fixed. Nothing on `docs/medical-stock.md` changes.

### `consultation_follow_up` — unused, stays out of the manual

The field has not been on the consultation form since 2017, and nothing in ADAM reads it. The
stray default has been removed. The field stays off the form unless a school asks for it. Do not
document it.

### The portal report's five-exam limit — fixed

The limit now applies to each examination type separately: up to five of each. *Change needed:*
remove the note under *Parents and Pupils Viewing Their Results*. If the page mentions how many
examinations are shown, make it five per type.

### `medical_exam_report`'s description — fixed

It now reads "This allows a staff member to view a report of medical examinations." If the manual
quotes permission descriptions, update this one.

### The off sport alert form's thresholds — fixed

The help text now reads "Staff members selected here will always receive a full list of the pupils
on the off sport list for this reason." and "If a subject is selected, then a teacher of that
subject will be notified if anyone in their class is on the off sport list for this reason." Nothing
needs to change, unless the manual quotes either sentence.

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

## Roll Calls — a stale settings path

Not medical, but found from the medical side. In `docs/roll-calls.md`, the *Leave Module* subsection
sends the reader to "**Cron Settings → Roll Call → Reason to show for Leaves**". That category no
longer exists: `rollcall-leave-reason` sits on the **Attendance** tab under the **Roll Call** heading,
next to `rollcall-offsport-reason`. The neighbouring *Medical Module* subsection, added at the same
time, uses the correct path, so the two now disagree on the same screen.

Worth a sweep of the whole manual for "Cron Settings" and for "**Cron** tab" while somebody is in
there — the settings screen was reorganised into the categories in
`ADAM\Support\Settings\SettingCategory` and other pages are likely to be stale in the same way.
