---
api_prefixes:
  - classes
---

# Classes

Use these endpoints to list the school's current classes, find the classes a pupil attends, and list the pupils in a class today or on a past date. An external system, such as a timetabling program, can also use them to read, create, change and delete a class. To enrol, move or remove pupils, use the class registration endpoints on the [Registration](api-registration.md#registrationsclasspost) page.

All endpoints on this page are under `/api/classes/`.

See [Authentication](api-access-to-adam.md#authentication) for how to send your API token.

### Classes/pupilteachers:get

This provides a list of classes that an individual pupil is registered for.

#### Request {#classespupilteachersget-request}

```
GET /api/classes/pupilteachers/<pupil>
```

#### Parameters {#classespupilteachersget-parameters}

-   `<pupil>` is the pupil identifier

#### Response {#classespupilteachersget-response}

```
GET /api/classes/pupilteachers/123
```

```json
{
    "data": [
        {
            "class_id": 1111,
            "class_description": "AB",
            "class_gradeyear": 10,
            "subject_name": "Geography",
            "subject_short": "Geo",
            "staff": {
                "staff_id": 321,
                "staff_lastname": "Van Der Walt",
                "staff_firstname": "Drikus",
                "staff_title": "Mr",
                "staff_email": "dvdwalt@school.example.com"
            },
            "teaching_assistants": [
                {
                    "staff_id": 1234,
                    "staff_lastname": "Smith",
                    "staff_firstname": "James",
                    "staff_title": "Mr",
                    "staff_email": "jsmith@school.example.com"
                }
            ],
            "class_friendly": "Geography Grade 10 AB"
        }
    ],
    "message": "",
    "response": {
        "error": "OK",
        "code": 200
    }
}
```

The `data` attribute contains one or more class objects. This contains the details of the subject, and the class.

Note that the `class_gradeyear` property can be negative to represent pre-school grades. (e.g. Grade 0 = Grade R, Grade -1 = Grade RR, and so on).

One `staff` member (the teacher of the class) will be provided, and the `teaching_assistants` may contain 0 or more staff objects.

### Classes/bygradeperiodsubject:get

Returns classes matching a specific grade, reporting period, and subject combination.

#### Request {#classesbygradeperiodsubjectget-request}

```
GET /api/classes/bygradeperiodsubject/<grade>/<period>/<subject>
```

#### Parameters {#classesbygradeperiodsubjectget-parameters}

-   `<grade>`: Grade identifier (required)
-   `<period>`: Reporting period identifier (required)
-   `<subject>`: Subject identifier (required)

#### Response {#classesbygradeperiodsubjectget-response}

```json
{
    "data": [
        {
            "id": 150,
            "grade": 10,
            "gradetext": "Grade 10",
            "description": "10A",
            "subject": 5,
            "fulldescription": "Grade 10 Mathematics 10A",
            "teacher_id": 42,
            "teacher_name": "Mr Smith"
        }
    ]
}
```

### Classes/list:get

Returns every current class in the school, with its subject, grade, teacher, teaching assistants, venue, category, and the number of pupils currently enrolled in it. This is the same set of classes shown by the **List of All Classes** report in ADAM.

Classes that have been deleted are not included.

#### Request {#classeslistget-request}

```
GET /api/classes/list
```

#### Parameters {#classeslistget-parameters}

This endpoint takes no parameters.

#### Response {#classeslistget-response}

```json
{
    "data": [
        {
            "id": 42,
            "subject_id": 7,
            "subject": "Mathematics",
            "subject_short": "MAT",
            "description": "A",
            "fulldescription": "Mathematics: Grade 8 A (Mr John Smith)",
            "grade": 8,
            "gradetext": "Grade 8",
            "grade_id": 1,
            "gradelevel": "NSC / GET (100)",
            "teacher_id": 19,
            "teacher_name": "Mr John Smith",
            "teaching_assistants": [
                {
                    "id": 23,
                    "name": "Mrs Anne Bell"
                }
            ],
            "venue": "Room 12",
            "category_id": 1,
            "category": "Academic",
            "pupils": 27
        }
    ],
    "message": "",
    "response": {
        "error": "OK",
        "code": 200
    }
}
```

The `data` attribute contains one object per class, ordered as the List of All Classes report orders them — by category, then subject, then grade and class description.

`teaching_assistants` contains zero or more staff objects. `pupils` is the number of pupils currently enrolled, and matches the number of records returned by [Classes/pupils:get](#classespupilsget) for the same class.

Note that the `grade` property can be negative to represent pre-school grades (e.g. Grade 0 = Grade R, Grade -1 = Grade RR, and so on). It is `null` for a class that is not tied to a particular grade.

### Classes/pupils:get

Returns the pupils who are currently enrolled in a particular class, together with the date on which each pupil's registration in that class began.

#### Request {#classespupilsget-request}

```
GET /api/classes/pupils/<class>
```

#### Parameters {#classespupilsget-parameters}

-   `<class>`: The class identifier (URL path parameter, required). Class identifiers are returned by [Classes/list:get](#classeslistget).

#### Response {#classespupilsget-response}

```json
{
    "data": [
        {
            "id": 1183,
            "admin": "A2021-044",
            "firstname": "Thandi",
            "lastname": "Mokoena",
            "grade": 8,
            "datestart": "2026-01-12"
        }
    ],
    "message": "",
    "response": {
        "error": "OK",
        "code": 200
    }
}
```

The `data` attribute contains one object per pupil, ordered by surname and then first name. `datestart` is the date the pupil's registration in this class began, in `YYYY-MM-DD` format.

The list reflects who is in the class **today**. A pupil appears only if their registration in the class covers today *and* they are still enrolled at the school — pupils who have left are not included, even if their class registration was never formally ended. For this reason the number of records returned always matches the `pupils` count given by [Classes/list:get](#classeslistget).

A class with nobody currently enrolled in it returns an empty `data` list with a 200 response code.

-   Code 200: The class exists; `data` contains the (possibly empty) list of pupils
-   Code 404: No such class, or the class has been deleted

### Classes/enrolment:get

Returns the pupils who were enrolled in a particular class on a given date, together with the date on which each pupil's registration in that class began. Use this to see who was in a class on a past date; use [Classes/pupils:get](#classespupilsget) to see who is in it today.

#### Request {#classesenrolmentget-request}

```
GET /api/classes/enrolment/<class>/<date>
```

#### Parameters {#classesenrolmentget-parameters}

-   `<class>`: The class identifier (URL path parameter, required). Class identifiers are returned by [Classes/list:get](#classeslistget).
-   `<date>`: The date to report on, in `YYYY-MM-DD` format (URL path parameter, required). It must be a real calendar date.

#### Response {#classesenrolmentget-response}

```
GET /api/classes/enrolment/150/2025-06-30
```

```json
{
    "data": [
        {
            "id": 1183,
            "admin": "A2021-044",
            "firstname": "Thandi",
            "lastname": "Mokoena",
            "grade": 7,
            "datestart": "2025-01-15"
        }
    ],
    "message": "",
    "response": {
        "error": "OK",
        "code": 200
    }
}
```

The `data` attribute contains one object per pupil, ordered by surname and then first name, with the same properties as [Classes/pupils:get](#classespupilsget). `grade` is the grade the pupil was in during the calendar year of `<date>`, not their grade today. It is `null` if no Grade 12 year (the `pupil_final` field) is recorded for the pupil.

A pupil appears if their registration in the class had begun on or before `<date>` and had not ended on or before it. Unlike Classes/pupils:get, the pupil's enrolment at the school is not checked: a pupil who has since left the school is still listed for a date on which they were in the class. For this reason, asking for today's date can return more pupils than Classes/pupils:get.

A class with nobody enrolled in it on that date returns an empty `data` list with a 200 response code.

-   Code 200: The class exists; `data` contains the (possibly empty) list of pupils
-   Code 400: The date is not a real calendar date in `YYYY-MM-DD` format
-   Code 404: No such class, or the class has been deleted

### Classes/class:get

Returns one class. It has the same properties as an item from [Classes/list:get](#classeslistget), and three more: `teachingtime`, `reporttext` and `language_id`. These are the properties [Classes/class:post](#classesclasspost) and [Classes/class:patch](#classesclasspatch) accept, so a program can read a class, change a property and send the class back.

#### Request {#classesclassget-request}

```
GET /api/classes/class/<class>
```

#### Parameters {#classesclassget-parameters}

-   `<class>`: The class identifier (URL path parameter, required). Class identifiers are returned by [Classes/list:get](#classeslistget).

#### Response {#classesclassget-response}

```
GET /api/classes/class/42
```

```json
{
    "data": {
        "id": 42,
        "subject_id": 7,
        "subject": "Mathematics",
        "subject_short": "MAT",
        "description": "A",
        "fulldescription": "Mathematics: Grade 8 A (Mr John Smith)",
        "grade": 8,
        "gradetext": "Grade 8",
        "grade_id": 1,
        "gradelevel": "NSC / GET (100)",
        "teacher_id": 19,
        "teacher_name": "Mr John Smith",
        "teaching_assistants": [
            {
                "id": 23,
                "name": "Mrs Anne Bell"
            }
        ],
        "venue": "Room 12",
        "category_id": 1,
        "category": "Academic",
        "pupils": 27,
        "teachingtime": 240,
        "reporttext": "",
        "language_id": 1
    },
    "message": "",
    "response": {
        "error": "OK",
        "code": 200
    }
}
```

`teachingtime` is the number of minutes a week that the class is taught. `reporttext` is the **Reporting Teacher** of the class: the name printed on reports when it should differ from the teacher's own name. It is usually empty. `language_id` is the class's language of teaching and learning, or 0 for none.

-   Code 200: `data` contains the class
-   Code 404: No such class, or the class has been deleted. The error is `There is no class with id <class>.`

### Classes/class:post

Creates a class and returns it, with its new `id`.

#### Request {#classesclasspost-request}

```
POST /api/classes/class
```

#### Parameters {#classesclasspost-parameters}

None. The class is sent in the message body. Do not add a class identifier to the URL: a `POST` only ever creates a class. To change a class, use [Classes/class:patch](#classesclasspatch).

#### Body {#classesclasspost-body}

The body must be a JSON object. The property names are the ones [Classes/class:get](#classesclassget) returns.

| Property | Type | Required | Notes |
|---|---|---|---|
| `subject_id` | number | Yes | A current subject. It cannot be changed later. |
| `teacher_id` | number | Yes | A current staff member. |
| `grade_id` | number | Yes | The grade level, which decides whether the class carries marks. It is not the grade. Use a `grade_id` that [Classes/list:get](#classeslistget) returns. In most schools, 1 is the academic grade level and 2 is the non-academic grade level. |
| `description` | text, up to 30 characters | Yes | The class description, for example `B`. ADAM shows it after the subject and grade, so it does not need to repeat them. |
| `grade` | number or `null` | No | The grade the class belongs to. Leave it out, or send `null`, for a class that is not tied to a grade. It cannot be changed later. |
| `venue` | text, up to 50 characters | No | The teaching venue. |
| `teachingtime` | whole number, not negative | No | Minutes a week. |
| `reporttext` | text, up to 250 characters | No | The **Reporting Teacher**. Leave it out unless it should differ from the teacher's name. When it is set, it replaces the teacher's name in `fulldescription`. |
| `language_id` | number | No | The language of teaching and learning, or 0 for none. |
| `teaching_assistants` | list | No | The staff identifiers of the teaching assistants, each a current staff member. The `{"id": …, "name": …}` objects that a read returns are also accepted. |

Identifiers can be sent as JSON numbers or as strings of digits.

The properties that only a read returns (`id`, `subject`, `subject_short`, `fulldescription`, `gradetext`, `gradelevel`, `teacher_name`, `category_id`, `category` and `pupils`) are ignored. Any other property name is refused.

##### Example (JSON):

```json
{
    "subject_id": 7,
    "teacher_id": 19,
    "grade_id": 1,
    "description": "B",
    "grade": 8,
    "venue": "Room 14",
    "teaching_assistants": [23]
}
```

#### Response {#classesclasspost-response}

On success, `data` holds the new class in the form [Classes/class:get](#classesclassget) returns, and the message is `Class created.`

#### Errors {#classesclasspost-errors}

-   `400 (Bad request)`: the body is not a JSON object (`Body of request not understood: send a JSON object.`); the body has a property this endpoint does not know; or the URL has a class identifier (`POST classes/class takes no id; use PATCH to change a class.`).
-   `409 (Conflict)`: a class that has not been deleted already has the same subject, grade, teacher and description. `data` holds the `id` of that class. Because of this check, a request that is sent twice does not create two classes.
-   `422 (Unprocessable entity)`: a required property is missing, or a value is not valid. The error names the property, for example ``` `subject_id` is required.``` or ``` `teacher_id` 9 is not a current staff member.```

> [!TIP]
> If a create fails with a `500 (Internal server error)`, the class may have been created before the fault. Send the same request again. If it is refused with `409`, `data` holds the identifier of the class that was created.

### Classes/class:patch

Changes a class. Only the properties that are sent change. A property that is left out keeps its value.

#### Request {#classesclasspatch-request}

```
PATCH /api/classes/class/<class>
```

#### Parameters {#classesclasspatch-parameters}

-   `<class>`: The class identifier (URL path parameter, required).

#### Body {#classesclasspatch-body}

A JSON object with the properties to change, as described for [Classes/class:post](#classesclasspost-body). None is required. A class read with [Classes/class:get](#classesclassget) can be sent back whole: the properties that have not changed are left alone.

`subject_id` and `grade` cannot change. A class of a different subject or grade is a new class, so create one with [Classes/class:post](#classesclasspost) instead.

`teaching_assistants`, when it is sent, replaces the whole list. Send an empty list to remove every teaching assistant.

##### Example (JSON):

```json
{
    "venue": "Room 7",
    "teaching_assistants": []
}
```

#### Response {#classesclasspatch-response}

On success, `data` holds the class as it now is, in the form [Classes/class:get](#classesclassget) returns. The message is `Class updated.`, or `No change.` when nothing sent differs from the class.

The change takes effect today. ADAM records it as a new version of the class, so it shows on the class's **History** tab. See [Viewing a class’s history](class-management.md#viewing-a-classs-history).

#### Errors {#classesclasspatch-errors}

-   `400 (Bad request)`: the body is not a JSON object; the body is empty (`The request names no fields to change.`); or the body has a property this endpoint does not know.
-   `404 (Not found)`: no such class, or the class has been deleted.
-   `422 (Unprocessable entity)`: a value is not valid, or the request tries to change `subject_id` or `grade`. The error names the property.

### Classes/class:put

Behaves exactly as [Classes/class:patch](#classesclasspatch). A property that is left out keeps its value; it is not cleared.

#### Request {#classesclassput-request}

```
PUT /api/classes/class/<class>
```

The parameters, body, response and errors are the same as for [Classes/class:patch](#classesclasspatch).

### Classes/class:delete

Deletes a class and returns it as it was before the delete.

#### Request {#classesclassdelete-request}

```
DELETE /api/classes/class/<class>
```

#### Parameters {#classesclassdelete-parameters}

-   `<class>`: The class identifier (URL path parameter, required).

#### Response {#classesclassdelete-response}

On success, `data` holds the class in the form [Classes/class:get](#classesclassget) returns, and the message is `Class deleted.`

ADAM refuses to delete a class that is still in use:

-   While any pupil who is currently at the school is in the class. Remove or move the pupils first, with [Registrations/class:delete](api-registration.md#registrationsclassdelete) or [Registrations/class:patch](api-registration.md#registrationsclasspatch).
-   While any pupil has a mark or comment on the class's assessments in a current or future reporting period. Removing a pupil from the class does not clear their marks, so the marks still prevent the delete. A pupil who is moved to another class of the subject takes their marks with them.

#### Errors {#classesclassdelete-errors}

-   `404 (Not found)`: no such class, or the class has already been deleted.
-   `409 (Conflict)`: the class still has pupils (`data` holds the number, as `pupils`), or still has marks in a current or future reporting period (`data` holds the number, as `results`).
