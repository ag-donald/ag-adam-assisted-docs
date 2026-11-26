---
api_prefixes:
  - registration
  - registrations
---

# Registration

Use these endpoints to list registration statuses, list the pupils in a status, and change a pupil's status. They also list the classes a grade of pupils or a single pupil is registered for, and enrol, move and remove a pupil in a class. To create or change the classes themselves, see [Classes](api-classes.md#classesclasspost).

All endpoints on this page are under one of these paths: `/api/registration/`, `/api/registrations/`.

See [Authentication](api-access-to-adam.md#authentication) for how to send your API token.

### Registration/status:post

Updates the registration status of a pupil by adding a record to their registration status log.

#### Request {#registrationstatuspost-request}

```
POST /api/registration/status/<pupil>
```

#### Parameters {#registrationstatuspost-parameters}

URL parameters:

- `<pupil>`: The identifier of the pupil whose registration status is to be changed.

These parameters are sent via form-data parameters.

- status: The identifier of the new registration status
- notes: Notes to add to the registration status

#### Response {#registrationstatuspost-response}

If the request was successful, a 200 OK code is returned. If an invalid status was chosen, a 400 Bad Request code is returned.

This endpoint is restricted in that updating the registration status of a pupil cannot change the “stage” of a pupil’s registration (a “stage” being one of “admissions”, “current enrolment” or “alumni”). Changing to a new stage requires additional processing to be done within ADAM and so attempts to change between statuses that are from different stages will be responded to with a 400 code.

### Registration/statuses:get

Gets a list of registration statuses that are active on the system.

#### Request {#registrationstatusesget-request}

```
GET /api/registration/statuses
```

#### Parameters {#registrationstatusesget-parameters}

None

#### Response {#registrationstatusesget-response}

```
GET /api/registration/statuses
```

```json
{
  "data": [
    {
      "status_id": 1,
      "status_description": "Applicant",
      "status_stage": "pre",
      "status_active": "Yes",
      "status_default": "Yes",
      "status_official": "Yes",
      "status_familyshow": "Yes",
      "status_sortorder": 1
    }
  ],
  "message": "",
  "response": {
    "error": "OK",
    "code": 200
  }
}
```

- status_stage is an enum with values pre (pre-admission), current (pupils enrolled in the school) or post (alumni and graduated pupils).

The following boolean values are also given:

- status_active: Whether the pupil record is active or inactive. Inactive pupils might include those who have withdrawn from the registration process, withdrawn from the school, died, and so on. When combined with status_stage, this provides [six broad categories of registration status](enrolment-process.md#enrolment-process).
- status_default: Each of the three status_stage values has one default status. This is automatically applied to pupils entering this stage for the first time.
- status_official: Whether this status refers to an official enrolment or not. Unofficial enrolments may include exchange or visiting pupils.
- status_familyshow: Whether or not pupils with this status should be shown on the family portal. For example, it can be distressing for parents of a deceased child to see that child appear on their family portal landing page. Similarly, withdrawn pupils might not show, but graduated pupils should.

### Registration/statuslist:get

Gets a list of pupils who belong to a specific registration status

#### Request {#registrationstatuslistget-request}

```
GET /api/registration/statuslist/<status>
```

#### Parameters {#registrationstatuslistget-parameters}

- `<status>`: The identifier of the registration status.

#### Response {#registrationstatuslistget-response}

```
GET /api/registration/statuslist/2
```

```json
{
  "data": [
    1,
    123,
    4321
  ],
  "message": "",
  "response": {
    "error": "OK",
    "code": 200
  }
}
```

The data attribute contains an array of 0 or more integers representing the identifiers of pupils who belong to this registration status.

### Registrations/grade:get

Returns a list of classes that a grade of pupils is registered for.

#### Request {#registrationsgradeget-request}

```
GET /api/registrations/grade/<grade>
```

#### Parameters {#registrationsgradeget-parameters}

- `<grade>` is an integer representing the grade of pupils to retrieve from the database. Note that 0 represents Grade R and negative grades represent the pre-school grades.

#### Response {#registrationsgradeget-response}

The response is an array of pupil registration objects, each following the structure below:

```json
{
  "data": [
    {
      "registration_id": 162555,
      "pupil_id": 1234,
      "pupil_lastname": "Last-Name",
      "pupil_firstname": "First",
      "class_id": 4231,
      "class_description": "Z",
      "class_gradeyear": "11",
      "subject_id": 101,
      "subject_name": "English Home Language",
      "subject_short": "Eng",
      "category_id": 1,
      "category_description": "Academic",
      "registration_datestart": "2024-01-20",
      "registration_dateend": null,
      "staff_id": 123,
      "staff_firstname": "Educator",
      "staff_lastname": "Mary"
    }
  ],
  "message": "",
  "response": {
    "error": "OK",
    "code": 200
  }
}
```

### Registrations/pupil:get

Returns the classes a pupil is in today, in every subject.

#### Request {#registrationspupilget-request}

```
GET /api/registrations/pupil/<pupil>
```

#### Parameters {#registrationspupilget-parameters}

- `<pupil>`: The identifier of the pupil.

#### Response {#registrationspupilget-response}

```
GET /api/registrations/pupil/1183
```

```json
{
  "data": [
    {
      "registration_id": 90211,
      "pupil_id": 1183,
      "class_id": 42,
      "class": "Mathematics: Grade 8 A (Mr John Smith)",
      "subject_id": 7,
      "subject": "Mathematics",
      "datestart": "2026-01-14",
      "dateend": null
    }
  ],
  "message": "",
  "response": {
    "error": "OK",
    "code": 200
  }
}
```

The data attribute contains one registration object for each class the pupil is in today, ordered by subject. `datestart` and `dateend` are in `YYYY-MM-DD` format. `dateend` is `null` for a registration with no end date. A pupil who is in no class returns an empty list.

The endpoints below return a registration in the same form.

- Code 200: The pupil exists; `data` contains the (possibly empty) list of registrations
- Code 404: No such pupil

### Changing a Pupil’s Classes

The four `Registrations/class` endpoints below enrol a pupil in a class, move a pupil to another class of the same subject, and remove a pupil from a class. They make the same changes as the class registration pages in ADAM (see [Class Registration](class-registration.md#class-registration)), and follow the same rule: a pupil can be in only one class of each subject at a time. So a pupil who is already in a class of the subject is **moved**, not enrolled.

These rules apply to all four endpoints:

- The pupil must be currently enrolled at the school. Otherwise the request is refused with `422 (Unprocessable entity)`.
- The class must exist and must not have been deleted. Otherwise the request is refused with `404 (Not found)`.
- Every change takes effect today. A change cannot be back-dated. Once the year-end process has been run, “today” is 1 January of the new year, as it is in ADAM itself: a pupil enrolled in December after the year-end starts in the class on 1 January.
- Moving or removing a pupil deletes their report comment for the subject, with its learning-outcome comments and assessment-standard results, in every current and future reporting period. This is what the class registration pages in ADAM do too. The pupil’s assessment marks are kept.
- If a pupil is enrolled and then removed on the same day, they do not appear in the class list at all. ADAM’s change history still records both changes.

ADAM records each change against the API token that made it. See [Changes Made Through a Token](api-access-to-adam.md#changes-made-through-a-token).

### Registrations/class:post

Enrols a pupil in a class from today.

#### Request {#registrationsclasspost-request}

```
POST /api/registrations/class/<class>/<pupil>
```

#### Parameters {#registrationsclasspost-parameters}

- `<class>`: The identifier of the class.
- `<pupil>`: The identifier of the pupil.

No body is needed.

#### Response {#registrationsclasspost-response}

```
POST /api/registrations/class/42/1183
```

```json
{
  "data": {
    "registration_id": 90211,
    "pupil_id": 1183,
    "class_id": 42,
    "class": "Mathematics: Grade 8 A (Mr John Smith)",
    "subject_id": 7,
    "subject": "Mathematics",
    "datestart": "2026-11-25",
    "dateend": null
  },
  "message": "Pupil enrolled.",
  "response": {
    "error": "OK",
    "code": 200
  }
}
```

On success, `data` holds the new registration and the message is `Pupil enrolled.` If the pupil is already in this class, and in no other class of the subject, nothing changes: `data` holds the pupil’s registration and the message is `No change: the pupil is already in this class.`

#### Errors {#registrationsclasspost-errors}

- `404 (Not found)`: no such class, or the class has been deleted.
- `409 (Conflict)`: the pupil is already in another class of the same subject. The error names that class, and `data` holds the pupil’s registration in it. Use [Registrations/class:patch](#registrationsclasspatch) to move the pupil instead.
- `422 (Unprocessable entity)`: the pupil is not currently enrolled at the school.

### Registrations/class:patch

Moves a pupil into a class. ADAM ends, today, every other class the pupil is in for the same subject, and enrols the pupil in this class. The pupil’s marks for current and future reporting periods move with them to the new class.

#### Request {#registrationsclasspatch-request}

```
PATCH /api/registrations/class/<class>/<pupil>
```

#### Parameters {#registrationsclasspatch-parameters}

- `<class>`: The identifier of the class to move the pupil into.
- `<pupil>`: The identifier of the pupil.

No body is needed.

#### Response {#registrationsclasspatch-response}

```
PATCH /api/registrations/class/43/1183
```

```json
{
  "data": {
    "registration_id": 90388,
    "pupil_id": 1183,
    "class_id": 43,
    "class": "Mathematics: Grade 8 B (Mrs Priya Naidoo)",
    "subject_id": 7,
    "subject": "Mathematics",
    "datestart": "2026-11-25",
    "dateend": null,
    "ended": [42]
  },
  "message": "Pupil moved.",
  "response": {
    "error": "OK",
    "code": 200
  }
}
```

On success, `data` holds the pupil’s registration in the class, and `ended` lists the identifiers of the classes the pupil has left. The message is `Pupil moved.`

If the pupil is already in this class, that registration is kept and only the other classes of the subject are ended. If the pupil is already in this class and in no other class of the subject, nothing changes and the message is `No change: the pupil is already in this class.`

#### Errors {#registrationsclasspatch-errors}

- `404 (Not found)`: no such class, or the class has been deleted.
- `409 (Conflict)`: the pupil is in no class of the subject. Use [Registrations/class:post](#registrationsclasspost) to enrol the pupil instead.
- `422 (Unprocessable entity)`: the pupil is not currently enrolled at the school.

### Registrations/class:put

Behaves exactly as [Registrations/class:patch](#registrationsclasspatch).

#### Request {#registrationsclassput-request}

```
PUT /api/registrations/class/<class>/<pupil>
```

The parameters, response and errors are the same as for [Registrations/class:patch](#registrationsclasspatch).

### Registrations/class:delete

Removes a pupil from a class today. This is the same as removing the pupil from the class list in ADAM.

#### Request {#registrationsclassdelete-request}

```
DELETE /api/registrations/class/<class>/<pupil>
```

#### Parameters {#registrationsclassdelete-parameters}

- `<class>`: The identifier of the class.
- `<pupil>`: The identifier of the pupil.

#### Response {#registrationsclassdelete-response}

On success, `data` holds the pupil’s registration in the class, with today’s date as `dateend`, and the message is `Pupil removed from the class.`

The pupil’s assessment marks in the class are kept. To take them to another class, move the pupil with [Registrations/class:patch](#registrationsclasspatch) instead of removing them.

#### Errors {#registrationsclassdelete-errors}

- `404 (Not found)`: no such class, the class has been deleted, or the pupil is not in the class.
- `422 (Unprocessable entity)`: the pupil is not currently enrolled at the school.
