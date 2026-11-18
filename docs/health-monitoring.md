# Health Monitoring

Health Monitoring lets staff examine many pupils, one after another, and record at the same time whether each pupil stays at school. It brings together the Medical and Absentee modules. Each check saves a [medical examination](medical-module.md#medical-examinations) against the pupil and sets the pupil’s attendance for the day: present, or absent with a reason.

A school might use it for a temperature check at the gate, a screening before a sports event, or any other check that is done for a large group of pupils at once.

## Using the Health Monitoring feature

Navigate to **Pupils → Medical Records → Health Monitoring**.

Under **Medical Exam**, choose the [Medical Examination](medical-module.md#medical-examinations) that will be conducted. Any examination type can be used, and each one asks for its own readings. Every server has a **Covid-19** examination type and a **Temperature** reading, both added during the pandemic. You can rename that type, or [add your own](medical-module.md#managing-the-medical-examinations) with the readings your check needs.

![](assets/screenshots/health-monitoring/health-monitoring-01.png)

Under **Show recent results from**, you can choose one or more other examination types. For each pupil, ADAM then shows when that pupil last had each of those examinations. This lets the person doing the check see whether an earlier examination has been done, and when. Click **Perform Health Monitoring** to begin.

You will be given the opportunity to search for a pupil. You can either type in a few characters of their name or click on the option to scan a QR code. [Student cards](student-cards.md#student-cards) with QR codes can be printed and laminated for each student. Alternatively, any pupil with access to ADAM’s pupil portal will be able to get an electronic version of their QR code for their phone.

> [!TIP]
> It might be worth students taking a screenshot of their QR Code to have it easily available without them having to log in to ADAM each time.

The QR Code scanning can be done on any device with a web camera and a modern web browser.

> [!NOTE]
> A specific note on iPhones and iPads: At the time of writing, there is a limitation on iPhones which only allows the Safari web browser to scan barcodes. Other browsers, such as Chrome and Opera, are not given access to the iOS devices’ cameras.

Once a pupil has been identified, complete the necessary health information and determine whether the pupil is permitted to stay at school or not.

![](assets/screenshots/health-monitoring/health-monitoring-02.png)

If you chose examination types under **Show recent results from**, ADAM lists them under **Previous Medical Examinations** and says when each was last conducted for this pupil. If the pupil has never had one, ADAM says “No recent medical examinations were found.” Staff with the **View Medical Examination Report** permission also see a **show details...** link, which shows the readings from that examination. Other staff see only the date.

For example, a school can ask families to complete a health declaration [on the portal](medical-module.md#parents-and-pupils-completing-medical-examinations), and then check at the gate that each pupil’s declaration has been done before taking the pupil’s temperature.

The medical examination then begins asking its necessary questions. In the example above, these are “Temperature” and “Fatigue”.

You may wish to add in a separate **[absentee reason](absentee-administration.md#absentee-reasons)** to indicate that the pupil was sent home because of a failed health check. The user will select an appropriate absentee record.

The **Notes** field is copied in to the [Medical Examination](medical-module.md#medical-examinations) record *and* the absentee record. These might indicate mitigating circumstances regarding the medical examination.

For more information on following-up on pupils who have not been recorded as present, please see the [absentee reports](absentee-administration.md#daily-absentees).

## Medical Examinations Report

A medical examinations report can be printed off for each grade by navigating to **Pupils → Medical Records → Medical Examinations Report**.

![](assets/screenshots/health-monitoring/health-monitoring-03.png)

Click on **Generate Report** to be able to see this report.

## Permissions Required for Health Monitoring

For users who are recording the results of Health Monitoring, there is only one permission that needs to be [assigned to staff](security-administration-for-staff.md#changing-the-permissions-of-a-group): **Wellbeing → Medical Records → Perform Health Monitoring** (medical\_healthcheck).

For staff that are viewing the medical examination report, they should be given the permission **Wellbeing → Medical Administration → View Medical Examination Report** (medical\_exam\_report).

> [!WARNING]
> Kindly note that this permission allows the staff member to see *all* medical exam information, not only the examinations recorded through Health Monitoring. Thus this permission should be given to appropriately authorised staff members only.
