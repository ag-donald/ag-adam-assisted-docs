---
api_prefixes:
  - classes
---

# Classes

Use these endpoints to list the school's current classes, find the classes a pupil attends, and list the pupils in a class today or on a past date.

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
            "description": "Maths 8A",
            "fulldescription": "Mathematics 8A (J Smith)",
            "grade": 8,
            "gradetext": "Grade 8",
            "grade_id": 4,
            "gradelevel": "Senior Phase",
            "teacher_id": 19,
            "teacher_name": "Mr J Smith",
            "teaching_assistants": [
                {
                    "id": 23,
                    "name": "Mrs A Bell"
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

The `data` attribute contains one object per pupil, ordered by surname and then first name, with the same properties as [Classes/pupils:get](#classespupilsget). `grade` is the grade the pupil was in during the calendar year of `<date>`, not their grade today.

A pupil appears if their registration in the class had begun on or before `<date>` and had not ended on or before it. Unlike Classes/pupils:get, the pupil's enrolment at the school is not checked: a pupil who has since left the school is still listed for a date on which they were in the class. For this reason, asking for today's date can return more pupils than Classes/pupils:get.

A class with nobody enrolled in it on that date returns an empty `data` list with a 200 response code.

-   Code 200: The class exists; `data` contains the (possibly empty) list of pupils
-   Code 400: The date is not a real calendar date in `YYYY-MM-DD` format
-   Code 404: No such class, or the class has been deleted
