# Leave Module

A leave module allows schools, particularly those with boarders, to keep track of pupils and their leaves.

## Initial Setup

Before parents, staff or students can request leaves the following steps must be performed first by a user with the relevant permissions:

1.  **Define Leave Types** \- at least one leave type must be added before users can request leaves. See [Manage Leave Types](#managing-leave-types) below.
2.  **Reset Leave Limits** \- for any leave type that limits the number of leaves, leave limits need to be set or users will not be able to apply for these types of leaves. See [Manage Leave Limits](#managing-leave-limits) below.

## Managing Leave Types

Before any leaves can be issued on ADAM, the leave types need to be defined. This can be done via **Administration → Pastoral Administration → Manage Leave Types**.

A list of existing leave types will be shown.

### Adding a new Leave Type

Click on the button **Add new Leave Type**.

![](assets/screenshots/leave-module/leave-module-01.png)

The fields are defined as follows:

-   **Description** is a description of the leave type that will be used whenever this leave type needs to be shown. Keep the description short, clear and unique from the other Leave Types.
-   **Overnight** indicates to ADAM whether this leave type results in a pupil being away from school overnight.
-   **Limit Leaves** is a setting which will allow ADAM to prevent the issuing of leaves to pupils once their allocations have been depleted. Note that the limits can be set per leave type per pupil and are set [elsewhere](#managing-leave-limits) in ADAM.
-   **Approval Type** indicates to ADAM what approvals are required and in what order the approvals should be requested. Options are:

-   No approval required: ADAM will allow the leave with no other approval.
-   Approval by subject teacher: ADAM will seek approval for this leave from the pupil’s teacher of a specified subject (see below for **Subject for Approval**). In most instances, this would be set to a subject that is linked to pastoral care: an example would be “housemaster” or “boarding house admin”. *If a pupil does not belong to any such class, their leave can only be approved by a person with global approval rights.*
-   Approval by parents: The parents must approve this leave type - this can be done via the parent portal.
-   Approval by parents, then subject teacher: The parents will be asked for approval first, and, if they approve, the subject teacher will be asked for approval.
-   Approval by subject teacher, then parents: The subject teacher will be asked for approval first, and, if they approve, the parents will be asked for their approval.

-   **Send Notification** - this enables ADAM to send out leave approval notifications via email. If this setting is set to “Yes” then ADAM will send an email notification to any staff or parent that needs to approve a leave of this type. The days and times when these notifications are to be sent can be configured in the [Site Settings](changing-site-settings.md#changing-site-settings).
-   **Subject for Approval** defines which subject ADAM should look at to find which teachers are allowed to approve leaves for a pupil. The teachers and Teaching Assistants of a class in this subject, will be able to approve leaves for all pupils in those classes. They will not be able to approve leaves for pupils in other classes that they are not teachers of. If notification emails are turned on then the teachers of pupils in the subject here specified will be notified of their required approval.
-   **Submission Permissions** tells ADAM who may submit these leave requests. Options including all combinations of Pupils, Staff and Families.
-   **Off Campus** tells ADAM whether this leave counts as the pupil being away from school. For example, a pupil who has signed out of the boarding house for the evening might be in the school library - out of their boarding house, but still on campus. This impacts catering and roll-call lists.
-   **Use Scheduler** — if set to “Yes”, users can only select dates and times from the leave scheduler for this leave type.
-   **Leave Options** are the questions asked when someone requests this leave, such as whether the pupil needs Saturday lunch. They are described [below](#questions-asked-with-a-leave-request).

### Questions asked with a leave request

The **Leave Options** field holds the questions that appear on the leave request form once this leave type is chosen. Leave it empty if the leave type needs no questions.

![](assets/screenshots/leave-module/leave-module-07.png)

To add a question:

1.  Click **+ Add question**.
2.  Type the question in the **Question** box.
3.  Choose the kind of answer:
    -   **Choices** gives a list of answers to pick one from, shown as radio buttons. Type each answer in the **+ Add choice** box and press Enter after each one. To remove an answer, click the **×** next to it. An example is *Saturday Lunch*, with the choices *Yes* and *No*.
    -   **Text answer** gives a box to type a short answer in, of up to 255 characters. An example is *Driver’s name*, for the person collecting the pupil.
4.  Tick **Must be answered** if a request should not be submitted without an answer to this question.

To remove a question, click the bin icon next to it. Click **Save this Leave Type** to keep the changes.

ADAM removes any colon from a question and any comma from a choice, because it uses these characters to store the answers.

#### Answering the questions

The questions appear on every leave request form for this leave type: **Submit a Leave Request for a Pupil** and **Submit Leave Requests by Class** for staff, and **Leave Requests** on the parent and pupil portals. A question that must be answered is marked with an asterisk (\*). A request cannot be submitted until every such question has an answer. If one is missing, ADAM names the questions that still need an answer and does not save the request.

#### Seeing the answers

The answers are shown to the people who approve the leave:

-   The lists of leave requests on **Pupils → Leave Management → View Leave Requests For Your Approval** and **View Leave Requests by Class** have a **Choices** column with each request’s answers. The column is shown only when at least one request in the list has answers.
-   On the parent portal, **Approve Leave Requests** shows the **Choices** column in the list of past leaves that the parent approved or denied. The cards for upcoming leaves do not show the answers.
-   When a member of staff clicks **update** in the **School Approval** column, the **Update leave status** page lists each answer below the request’s details, together with the **Host Contact**.

To count or list the answers across many requests, use the [Leave Reports](#leave-reports).

> [!NOTE]
> Leave types set up before this editor was introduced keep their questions. ADAM converted them to the new editor, and none of them is marked **Must be answered**.

### Editing a Leave Type

From the list of Leave Types, click on the **edit** option next to the leave type that you’d like to change. The editing screen will be displayed. A description of each of the fields can be [found above](#adding-a-new-leave-type).

## Managing Leave Limits

Some leaves can be configured to be taken only a limited number of times. These limits must be set per leave type, per pupil.

> [!WARNING]
> Note that if leave limits are not set for each pupil and for each leave type this will result in parents, staff and pupils being unable to apply for leaves of types where no limit has been set. In the same way pupils who have a balance of zero leaves for a particular type will not be allowed to request leaves of that type.

Leave limits can be changed in one of two ways:

1.  **Reset** - A hard reset of the number of leaves for a particular leave type. This can be used, for example, at the beginning of a term/semester/year to allocate an initial number of leaves to each pupil. Resetting leave limits in this way will overwrite the current leave balance for each pupil with a new predetermined value.
2.  **Change** - This is a change in  the number of leaves relative to their total allowed leaves for a particular type. For example if pupils were allocated 3 overnight leaves at the beginning of a term/semester/year and each pupil has used a different number of leaves this method can be used to increase (or decrease) the number of available leaves for all pupils by a certain amount relative to their own balance.

### Reset Leave Limits By Class

Navigate to **Pupils → Leave Management → Reset Leave Limits by Class**.

Choose the class and the leave type.

> [!NOTE]
> The classes shown are those from the subject specified in the Site Settings as the **General / Default Class subject for Leaves**. This might need to be set correctly the first time if you do not see any classes listed here. This setting should be set to align to your boarding houses.

![](assets/screenshots/leave-module/leave-module-03.png)

This screen shows the pupils’ current leave counts for the selected Leave Type.

To change a pupil’s limit, make sure the **Select** box is checked, and enter a new amount in the **New Balance** column on the right and, optionally, enter a **Note**.

> [!WARNING]
> Note carefully that only rows that have the **Select** box checked will be saved. This allows you to update only a single pupil in a whole class if required. The **Select** column will check automatically when the **New Balance** column or **Notes** column is typed in.

Once done, click on the **Save Limits** button at the bottom of the screen.

ADAM will confirm how many leave limits were saved:

![](assets/screenshots/leave-module/leave-module-04.png)

When setting limits, please note that any *future-dated* leaves will be deducted from the new balance.

On 1 April, a pupil has 2 leaves available and books two leaves for 21 April and 28 April. On 14 April, the pupil’s limit is reset to 3. At the end of April, the pupil will have 1 leave available. This is because the limit reset of the 14th happened prior to the two leaves being taken and thus those leaves will be deducted from that total. This has potential issues if, for example, a pupil has two leaves, books them, and has a limit then reduced to 1. Both leaves were requested and will not be revoked. Any pupil who has leaves deducted because of disciplinary or other reasons, may need this checked manually. ADAM will certainly prevent a user from having a negative leave balance where it can, but if a leave total is reset to a lower amount than the leaves already booked, the pupil will have a negative leave total and will be allowed to proceed with the leaves. This is because the negative amount was essentially created by a human rather than ADAM.

## Leave Requests

Submitting leave requests is slightly different for staff vs parents and pupils.

### Submitting a Leave Request by Staff for/on behalf of a Pupil

Navigate to **Pupils → Leave Management → Submit a Leave Request for a Pupil**.

## Leave Reports

ADAM offers reports for reviewing the leaves that pupils have requested. They are found under the **Leave Management** heading on the **Pupils** tab, and require the **View Leave Reports Globally** permission.

- **Leave Option Responses** shows, for a chosen leave type and date range, *how many* pupils selected each option — for example, how many requested Saturday lunch.
- **Leave Option Lists** lists the *named pupils* who selected particular options. This is described below.

Both reports filter and count only **Choices** questions. A **Text answer** question has no fixed answers to count or tick, so it does not appear in **Leave Option Responses** or in the filter of **Leave Option Lists**. See [Questions asked with a leave request](#questions-asked-with-a-leave-request).

### Leave Option Lists

Where the **Leave Option Responses** report gives you totals, the **Leave Option Lists** report gives you the actual names. It is ideal for building a working list — for example, the pupils who requested transport back to school for a given weekend, or who signed up for Saturday lunch.

To open it, navigate to **Pupils → Leave Management → Leave Option Lists** and complete the filter form:

- **Leave Type** — required. Choose the leave type to report on. The options to tick appear only once a leave type has been chosen, because each leave type defines its own options.
- **Options** — once a leave type is chosen, its **Choices** questions (such as *Saturday Lunch* or *Transport Back*) appear as tick boxes. **Text answer** questions are not listed here. Tick the values you want to list. You can:
    - leave everything unticked to list **all** pupils on this leave type within the date range;
    - tick more than one value of the *same* option to match pupils who chose **any** of those values;
    - tick values across *different* options to match only pupils who chose **all** of them — for example, *Saturday Lunch = yes* **and** *Transport Back = yes*.
- **From Date** and **To Date** — the period to cover. **From Date** defaults to a week ago and **To Date** to now.

![](assets/screenshots/leave-module/leave-module-05.png)

Click **Generate Report**. The report opens in a new window.

Only **approved** leave requests are included. The report lists each matching pupil with their **Name**, **Grade** and **Class**, a column for each of the leave type’s questions showing that pupil’s answer (typed answers included), and the **Leaving** and **Returning** dates and times. The headings confirm the leave type, the date range and the options you filtered on.

![](assets/screenshots/leave-module/leave-module-06.png)

To save or print the list, click the **Download as Excel** button at the top of the report to download it as a spreadsheet.
