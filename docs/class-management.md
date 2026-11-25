# Class Management

You will need to make sure that you have created subjects in ADAM first. To read up about subjects, please [click here](subjects.md#subjects).

A class can be considered a container. Its primary purpose is to link a teacher to pupils and link pupils to an activity, whether academic or otherwise.

## Creating a new class

To create a new class, click on the “**Add a new class**” option on the “**Classes**” tab, found under the “**Class Administration**” heading.

To create many classes at once and put pupils into them from one file, use the [Classes import](importing-and-exporting-data.md#importing-classes-and-class-registrations).

https://www.youtube.com/watch?v=pfIaJu2TFzA

The following screen is shown:

![](assets/screenshots/class-management/class-management-02.png)

The different headings are explained below:

-   **Subject**

-   Choose the subject or activity that this class or group belongs to.

-   **Grade Level**

-   If this is an academic subject, please make sure that you choose “NSC/GET: Ordinary Grade (100)”. If it is some other form of class, you can leave this as “Non-academic”.

-   **Teacher**

-   This is the primary teacher that is responsible for the class. One teacher must be chosen, although other teachers can be added later on in the “Teaching Assistants” section below.

-   **Grade**

-   Some classes, certainly all academic classes, will have a grade associated with them, however, not all groups and activities do. An example of one that does not is a Sports House which has membership from all grades. If you choose a grade here, you will not be able to add pupils from a different grade.

-   **Class Description**

-   This is a short code that allows you to distinguish different classes within the subject. Often this is the teacher’s initials, for example “A” would result in this class being displayed as “Form 2 A”. For non-academic subjects, a qualifier such as “Seniors” might result in a group being displayed as “Rugby: Seniors”.

-   **Teaching Time**

-   This is submitted to LURITS if it is entered. It is not compulsory and LURITS don’t seem to mind too much if it is omitted.

-   **Teaching Venue**

-   This is used by the [timetable module](timetable-module.md#timetable-module) for informational purposes only. It is an optional field to fill in.

-   **Reporting Teacher**

-   Because a class has been assigned a principal teacher already, this block can be left, most of the time, empty. However, when you wish to have multiple teachers, for example, displayed, you might enter those names here. Note that ADAM will only look at the principal teacher and this block when deciding what name to show next to a class. It does *not* consider the Teaching Assistants.

-   **Teaching Assistants**

-   Teaching Assistants, in spite of the actual meaning of the phrase, allow other teachers to be linked to the class. These teachers are able to, for academics, add marks in the mark book, enter and edit report comments and produce class lists for these classes easily.

-   **Language of Teaching and Learning**

-   This field is only important if your school is a parallel medium school with different classes being taught in different languages. Select the language that this class is taught in so that ADAM uses the appropriate [subject translation](subjects.md#translating-subject-names) when displaying the details of this class.

Once you are happy with the options, click on the “**Add class**” button at the bottom of the page.

ADAM then shows you this confirmation screen:

![](assets/screenshots/class-management/class-management-03.png)

This allows you to [enrol pupils in this class or group](class-registration.md#class-registration), to edit and change the settings of the class (see “[Edit an existing class](#editing-an-existing-class)” below, bearing in mind that you will skip the first few steps of selecting a class) or to take you back to add a new class, as you’ve just done.

## Editing an existing class

To edit an existing class, click on the “**Edit a class’s details**” option on the “**Classes**” tab under the “**Class Administration**” heading.

Select the class to edit by first selecting its subject category, then the subject and finally, the class you wish to edit.

When changing the details of the class, please take note of [the details given above about the different fields](#creating-a-new-class).

Note that a class’s **Subject** and **Grade Level** cannot be changed once the class exists — choosing a different subject or grade really means creating a different class. These two fields are therefore shown for reference only on the editing screen.

### Setting the effective date of a change

When you edit a class, ADAM records what changed and when, so that the class keeps a full history (see “[Viewing a class’s history](#viewing-a-classs-history)” below). At the bottom of the editing screen there is an “**Effective from**” date, which sets the date your changes take effect. It defaults to today.

![](assets/screenshots/class-management/class-management-06.png)

-   Leave it as today, or choose a future date, when the change reflects something happening now or going forward — for example, a new teacher taking over next term. Reports for earlier periods keep the previous details.

-   Choose a date in the past when you are correcting the record — for example, noting that a teacher actually changed earlier in the year.

Back-dating a change into a reporting period whose reports have already been published requires an additional permission, “**Edit class details within closed reporting periods**”. Without it, ADAM will refuse the change and tell you why. With it, ADAM will warn you that already-published reports will reflect the change the next time they are regenerated and the archive refreshed.

## Viewing a class’s history

Every change you make to a class — the teacher, class description, teaching venue, teaching time, reporting teacher or language — is recorded over time. To see this history, open the class’s profile page: click the “**Class Info**” option on the “**Classes**” tab, found under the “**Class Administration**” heading, then choose the subject category, the subject and the class. On the class profile, click the “**History**” tab.

The History tab shows a timeline chart showing the class versions and the reporting period dates.

![](assets/screenshots/class-management/class-management-04.png)

This is followed by a table. Each row is the state of the class from a particular effective date, with the most recent at the top. Cells that changed from the previous version are highlighted, and a change of teacher is shown in bold, so you can see at a glance who the teacher was during any part of the year and exactly when something changed. The “**Changed by**” column shows who recorded each change — the earliest entry is marked “cut-over”, meaning it pre-dates history tracking. The chart above the table shows which version each reporting period’s end date falls into, which helps you understand the details a particular report would have used.

The History tab is shown to staff who can administer the class: those with class administration permission, the class’s own teacher or teaching assistants, and the head of the class’s subject.

### Editing or removing a history entry

If a change was recorded with the wrong details or the wrong date, you can put it right. In the “**Actions**” column of the History table, click the pencil icon next to a version to open the “**Edit class version**” screen. Here you can adjust the teacher, class description, teaching venue, teaching time, reporting teacher, language and the “**Effective from**” date, then click “**Save version**”.

![](assets/screenshots/class-management/class-management-05.png)

A version can also be removed when it is safe to do so. A trash icon appears in the “**Actions**” column — and a “**Delete version**” button on the edit screen — only for versions that may be deleted. When you delete a version, the previous version extends to cover the gap it leaves behind. To protect your records, ADAM will not let you:

-   delete the only remaining version, because a class must always keep at least one, or

-   edit or delete a version when marks, comments or other reporting data already exist for the period it covers.

As when editing a class, moving a change into a reporting period whose reports have already been published requires the “**Edit class details within closed reporting periods**” permission.

## Deleting a class

Please follow the same instructions for “Editing an existing class”. On the editing screen, at the bottom, there will be a button to “DELETE CLASS”. Clicking on this will confirm that you are sure you want to continue. Clicking on “Yes, delete this class” will result in the class being deleted and all pupils will be un-enrolled from it.
