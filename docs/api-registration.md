---
api_prefixes:
  - registration
  - registrations
---

# Registration

Use these endpoints to list registration statuses, list the pupils in a status, and change a pupil's status. They also list the classes a grade of pupils is registered for.

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
