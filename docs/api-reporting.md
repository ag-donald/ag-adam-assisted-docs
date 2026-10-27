---
api_prefixes:
  - reporting
---

# Reporting

Use these endpoints to read reporting periods, results, markbooks and reports, and the comments, outcomes, standards and indicators that go with them.

All endpoints on this page are under `/api/reporting/`.

See [Authentication](api-access-to-adam.md#authentication) for how to send your API token.

### Reporting/periods:get

Gets a list of reporting periods for a year.

#### Request {#reportingperiodsget-request}

```
GET /api/reporting/periods[/<year>]
```

#### Parameters {#reportingperiodsget-parameters}

- `<year>`: OPTIONAL. The calendar year in question. If omitted, the current calendar year is used.

#### Response {#reportingperiodsget-response}

```
GET /api/reporting/periods/2018
```

```json
{
  "data": [
    {
      "period_id": "31",
      "period_name": "Term 1",
      "period_start": "2018-01-01",
      "period_end": "2018-12-02",
      "period_publish": "2018-12-02 12:00:00"
    }
  ],
  "message": "Reporting periods from year 2018",
  "response": {
    "error": "OK",
    "code": 200
  }
}
```

The **data** attribute contains an array of 0 or more reporting period objects.

- `period_id` is the internal identifier for the reporting period in question.
- `period_name` is the user-provided descriptor for that reporting period.
- `period_start` is the starting date of the reporting period. This is often set as the start of term, but some schools, who run concurrent or additional reporting periods may not align reporting periods with terms.
- `period_end` is the date on which the reporting period is deemed to have finished.
- `period_publish` is the date and time when the reports are made available on the parent portal. This date may change at the user discretion and so this value should always be double checked on or after this time if important actions are to occur.

### Reporting/results:get

Gets all academic results for a reporting period.

#### Request {#reportingresultsget-request}

```
GET /api/reporting/results/<reportingperiod>
```

#### Parameters {#reportingresultsget-parameters}

- `<reportingperiod>` is the value of the reporting period identifier. See the `period_id` property returned in the Reporting/periods/get request above.

#### Response {#reportingresultsget-response}

```
GET /api/reporting/results/31
```

```json
{
  "data": [
    {
      "pupil_id": 1754,
      "pupil_admin": "55012",
      "pupil_grade": 9,
      "results": [
        {
          "subject_id": 1,
          "subject_name": "English",
          "dbe_subject_code": "",
          "result_term": 50,
          "result_ytd": 50
        },
        {
          "subject_id": 40,
          "subject_name": "Technology",
          "dbe_subject_code": "15351142",
          "result_term": null,
          "result_ytd": null
        }
      ],
      "report_aggregate": 72.5,
      "report_aggregate_ytd": 72.5,
      "report_modified": "2016-02-11 11:36:17"
    }
  ],
  "message": "",
  "response": {
    "error": "OK",
    "code": 200
  }
}
```

The **data** attribute contains an array of 0 or more pupil objects. The pupil object has the following attributes:

- `pupil_id` the internal identifier of the pupil.
- `pupil_admin` is a user-provided identifier. These should be consistent but can change at the school’s discretion.
- `pupil_grade` gives the grade that the pupil was in for this reporting period. Values are integers between -3 (Grade 0000) and 13 (Post Matric).
- **results** is an array of 0 or more subject result objects. These objects have the following properties:

- `subject_id` is the internal identifier for the subject in ADAM. Note that these may not be consistent as some schools have multiple versions of the same subject (e.g. English for Junior School vs English for High School). These values are not consistent across schools.
- `subject_name` is the user-provided name for that subject.
- `dbe_subject_code` is the Department of Basic Education’s subject code. Typically, this is specific to the grade and subject. Because some schools offer their curriculum in different configurations, some codes may be duplicated, and yet other subjects may not have a code assigned (which is represented by an empty string).
- `result_term` is the pupil’s result for this reporting period (normally akin to a term). A **null** value represents an absent result. This result is otherwise returned as a **float** and decimal places should be anticipated
- `result_ytd` is the pupil’s year-to-date result, a result that is often an aggregated result across a number of reporting periods. A **null** value represents an absent result.This result is otherwise returned as a **float** and decimal places should be anticipated.

- `report_aggregate` is a summary result (often, but not always, an average of all the subject results) for the pupil for that term.
- `report_aggregate_ytd` is a summary year-to-date result. Again, this is often, but not always an average of the subject results.
- `report_modified` is a timestamp of the last modification time of that report.

### Reporting/pupilreportingperiods:get

Returns the reporting periods in which a pupil has a report, with the pupil's aggregates and the archived report document for each period.

#### Request {#reportingpupilreportingperiodsget-request}

```
GET /api/reporting/pupilreportingperiods/<pupil>
```

#### Parameters {#reportingpupilreportingperiodsget-parameters}

- `<pupil>`: ADAM internal pupil identifier (required)

#### Response {#reportingpupilreportingperiodsget-response}

```
GET /api/reporting/pupilreportingperiods/123
```

```json
{
  "data": [
    {
      "period_id": 3,
      "period_name": "Term 1 2026",
      "period_start": "2026-01-15",
      "period_end": "2026-03-31",
      "period_publish": "2026-04-01 12:00:00",
      "report_aggregate": "72.5000000",
      "report_aggregate_ytd": "-1.0000000",
      "document_id": 456,
      "document_upload_date": "2026-04-01 09:15:00",
      "pupil_gradetext": "Grade 10"
    }
  ],
  "message": "",
  "response": {
    "error": "OK",
    "code": 200
  }
}
```

The **data** attribute contains an array of 0 or more reporting period objects, with the most recent period (by end date) first. A period is included only if the pupil has a report in it and the period's **Show on Parent/Pupil Portals** setting is **Yes**. The period's publish date is not checked, so the list can include periods whose reports are not yet published.

- `period_id`, `period_name`, `period_start`, `period_end` and `period_publish` are as described under [Reporting/periods:get](#reportingperiodsget-response).
- `report_aggregate` and `report_aggregate_ytd` are the pupil's summary result for the period and for the year to date, as stored on the pupil's report. Each is a string holding a decimal number with seven decimal places, for example `"72.5000000"`. A value of `"-1.0000000"` means that no aggregate is stored, not a mark of -1. These are not always the same values that [Reporting/results:get](#reportingresultsget-response) returns: that endpoint calculates an aggregate when none is stored, and this endpoint does not.
- `document_id` is the identifier of the archived report document for this period, and `document_upload_date` is the date and time it was stored. Both are `null` when no report document has been archived for the period.
- `pupil_gradetext` is the name of the grade the pupil was in during the year in which the period ended, using the grade names set up in ADAM, for example "Grade 10".

### Reporting/subjectmarksbypupil:get

Returns subject marks for a pupil across all reporting periods.

#### Request {#reportingsubjectmarksbypupilget-request}

```
GET /api/reporting/subjectmarksbypupil/<pupil>
```

#### Parameters {#reportingsubjectmarksbypupilget-parameters}

- `<pupil>`: ADAM internal pupil identifier (required)

#### Response {#reportingsubjectmarksbypupilget-response}

Data attribute contains an array of reporting periods, each with a nested subjects array:

```json
{
  "data": [
    {
      "period_id": 3,
      "period_name": "Term 1 2026",
      "subjects": [
        {
          "subject_id": 5,
          "grade": 10,
          "subject_name": "Mathematics",
          "subject_short": "Maths",
          "teacher_email": "smith@school.co.za",
          "teacher_name": "Mr Smith",
          "result": 78,
          "class_friendly": "10A Maths"
        }
      ]
    }
  ]
}
```

### Reporting/markbook:get

Returns the markbook (assessment results by category) for a pupil in a specific reporting period.

#### Request {#reportingmarkbookget-request}

```
GET /api/reporting/markbook/<period>/<pupil>
```

#### Parameters {#reportingmarkbookget-parameters}

- `<period>`: Reporting period identifier (required)
- `<pupil>`: ADAM internal pupil identifier (required)

#### Response {#reportingmarkbookget-response}

Data attribute contains an array of subjects with assessment categories and individual assessments.

```json
{
  "data": [
    {
      "subject_name": "Mathematics",
      "subject_short": "Maths",
      "class_teacher": "Mr Smith",
      "class_gradeyear": 10,
      "class_description": "10A",
      "class_friendly": "10A Maths",
      "assessment_categories": [
        {
          "category_name": "Tests",
          "assessments": []
        }
      ]
    }
  ]
}
```

### Reporting/report:get

Returns a pupil's report as a PDF document.

#### Request {#reportingreportget-request}

```
GET /api/reporting/report/<period>/<pupil>
```

#### Parameters {#reportingreportget-parameters}

- `<period>`: Reporting period identifier (required)
- `<pupil>`: ADAM internal pupil identifier (required)

#### Response {#reportingreportget-response}

Binary PDF response with content type application/pdf.

### Reporting/previousreports:get

Returns historical report information for a pupil.

#### Request {#reportingpreviousreportsget-request}

```
GET /api/reporting/previousreports/<pupil>
```

#### Parameters {#reportingpreviousreportsget-parameters}

- `<pupil>`: ADAM internal pupil identifier (required)

#### Response {#reportingpreviousreportsget-response}

Data attribute contains previous report table data.

> [!NOTE]
> **Report detail endpoints and publication**
>
> The four `reporting/…` endpoints that follow (and their `reporting/grade/…` counterparts) expose the
> detail that appears on a pupil's printed report — subject comments, learning outcomes, assessment
> standards and behavioural indicators — as JSON. Every value is read through the same report engine
> that renders the PDF, so the figures match the printed report exactly.
>
> **Only published reporting periods are exposed.** A period is published once its publish date and time
> has passed (see `period_publish` under [Reporting/periods](#reportingperiodsget-response)). Behaviour
> for the period identifier supplied in the request:
>
> - Period not yet published → `403 (Forbidden)`, with no data.
> - Period identifier not recognised → `400 (Bad Request)`.
> - Published period with no captured detail → `200 (OK)` with an empty `data` array.
>
> Wherever a value has not been captured it is returned as `null`. This covers absent marks and any text
> field left blank on the report.

### Reporting/comments:get

Returns the subject comments and result summary for a pupil's report in a published reporting period.

#### Request {#reportingcommentsget-request}

```
GET /api/reporting/comments/<pupil>/<period>
```

#### Parameters {#reportingcommentsget-parameters}

- `<pupil>`: ADAM internal pupil identifier (required).
- `<period>`: Reporting period identifier (required). The period must be published (see the note above).

#### Response {#reportingcommentsget-response}

The **data** attribute contains an array with one object per reporting subject on the pupil's report.

```json
{
  "data": [
    {
      "subject_id": 5,
      "subject_name": "Mathematics",
      "subject_short": "Maths",
      "subject_category_id": 2,
      "class_id": 812,
      "class_friendly": "10A Maths",
      "teacher_name": "Mr Smith",
      "comment": "A pleasing term's work.",
      "comment_generic": null,
      "result_term": 78,
      "result_ytd": 74.5,
      "symbol_term": "B",
      "symbol_ytd": "B",
      "level": null
    }
  ],
  "message": "",
  "response": {
    "error": "OK",
    "code": 200
  }
}
```

- `subject_id` is the internal identifier for the subject in ADAM (see [Reporting/results](#reportingresultsget-response)).
- `subject_name` is the subject's full name.
- `subject_short` is the subject's short name.
- `subject_category_id` is the identifier of the subject category the subject belongs to.
- `class_id` is the identifier of the class the pupil is registered in for this subject.
- `class_friendly` is a human-readable class name, or `null` if none is configured.
- `teacher_name` is the class teacher's name, or `null`.
- `comment` is the pupil's subject comment for this period, or `null` if none was captured.
- `comment_generic` is the generic (shared) subject comment, or `null`.
- `result_term` is the term result as a **float**, or `null` if absent.
- `result_ytd` is the year-to-date result as a **float**, or `null` if absent.
- `symbol_term` is the term result symbol, or `null`.
- `symbol_ytd` is the year-to-date result symbol, or `null`.
- `level` is the subject level descriptor, or `null`.

### Reporting/outcomes:get

Returns the learning outcomes captured on a pupil's report in a published reporting period.

#### Request {#reportingoutcomesget-request}

```
GET /api/reporting/outcomes/<pupil>/<period>
```

#### Parameters {#reportingoutcomesget-parameters}

- `<pupil>`: ADAM internal pupil identifier (required).
- `<period>`: Reporting period identifier (required). The period must be published (see the note above).

#### Response {#reportingoutcomesget-response}

The **data** attribute contains an array with one object per populated learning outcome, across all of the
pupil's subjects. Outcomes with no captured value are omitted, matching the printed report.

```json
{
  "data": [
    {
      "subject_id": 5,
      "outcome_id": 41,
      "outcome_number": "1",
      "outcome_name": "Numbers, Operations and Relationships",
      "outcome_description": "Recognises, describes and represents numbers.",
      "symbol": "4",
      "symbol_name": "Adequate",
      "symbol_description": "Adequate achievement (50 – 59%)",
      "mark": null,
      "weighting": 25,
      "comment": null
    }
  ],
  "message": "",
  "response": {
    "error": "OK",
    "code": 200
  }
}
```

- `subject_id` is the subject the learning outcome belongs to.
- `outcome_id` is the internal identifier of the learning outcome.
- `outcome_number` is the outcome's display number.
- `outcome_name` is the outcome's name.
- `outcome_description` is the outcome's longer description.
- `symbol` is the captured symbol/level for the outcome, or `null`.
- `symbol_name` is the name associated with that symbol, or `null`.
- `symbol_description` is the description associated with that symbol, or `null`.
- `mark` is the numeric mark for the outcome as a **float**, or `null` when the outcome is assessed by symbol rather than a mark.
- `weighting` is the outcome's weighting as a **float**, or `null`.
- `comment` is the outcome comment, or `null`.

### Reporting/standards:get

Returns the assessment standards captured on a pupil's report in a published reporting period.

#### Request {#reportingstandardsget-request}

```
GET /api/reporting/standards/<pupil>/<period>
```

#### Parameters {#reportingstandardsget-parameters}

- `<pupil>`: ADAM internal pupil identifier (required).
- `<period>`: Reporting period identifier (required). The period must be published (see the note above).

#### Response {#reportingstandardsget-response}

The **data** attribute contains an array with one object per assessment standard that has a captured symbol,
across all of the pupil's learning outcomes. Standards with no captured symbol are omitted, matching the
printed report.

```json
{
  "data": [
    {
      "subject_id": 5,
      "outcome_id": 41,
      "criterion_id": 233,
      "criterion_number": "1.1",
      "criterion_name": "Counts objects",
      "criterion_description": "Counts to at least 100 everyday objects reliably.",
      "symbol": "3"
    }
  ],
  "message": "",
  "response": {
    "error": "OK",
    "code": 200
  }
}
```

- `subject_id` is the subject the assessment standard belongs to.
- `outcome_id` is the learning outcome the standard falls under.
- `criterion_id` is the internal identifier of the assessment standard (criterion).
- `criterion_number` is the standard's display number, or `null`.
- `criterion_name` is the standard's name, or `null`.
- `criterion_description` is the standard's longer description, or `null`.
- `symbol` is the captured symbol for the standard, or `null`.

### Reporting/indicators:get

Returns the behavioural indicators captured on a pupil's report in a published reporting period.

#### Request {#reportingindicatorsget-request}

```
GET /api/reporting/indicators/<pupil>/<period>
```

#### Parameters {#reportingindicatorsget-parameters}

- `<pupil>`: ADAM internal pupil identifier (required).
- `<period>`: Reporting period identifier (required). The period must be published (see the note above).

#### Response {#reportingindicatorsget-response}

The **data** attribute contains an array with one object per behavioural indicator captured against a
subject. Behavioural indicators are configured per grade and period, so a period/grade without a
behavioural-indicator configuration returns an empty array.

```json
{
  "data": [
    {
      "subject_id": 5,
      "descriptor": "Participates in class",
      "value": "Often"
    }
  ],
  "message": "",
  "response": {
    "error": "OK",
    "code": 200
  }
}
```

- `subject_id` is the subject the behavioural indicator was captured against.
- `descriptor` is the behavioural indicator descriptor.
- `value` is the captured value for the indicator, or `null`.

### Reporting/grade/comments:get

Returns the same detail as [Reporting/comments](#reportingcommentsget-response), but for **every pupil**
registered for a given subject in a given grade during a published reporting period, rather than a single
pupil.

Each row carries two extra leading keys — `pupil_id` and `pupil_admin` — identifying the pupil the row
belongs to. The remaining keys are exactly those of the pupil-scoped endpoint. The publication rules and
`null` handling described in the note above apply identically.

#### Request {#reportinggradecommentsget-request}

```
GET /api/reporting/grade/comments/<grade>/<subject>/<period>
```

#### Parameters {#reportinggradecommentsget-parameters}

- `<grade>`: The grade identifier (required). Values are integers between -3 (Grade 0000) and 13 (Post Matric); negative values denote pre-primary grades.
- `<subject>`: The internal subject identifier (required).
- `<period>`: Reporting period identifier (required). The period must be published (see the note above).

#### Response {#reportinggradecommentsget-response}

The **data** attribute contains an array with one object per subject **per pupil** in the cohort.

```json
{
  "data": [
    {
      "pupil_id": 1754,
      "pupil_admin": "55012",
      "subject_id": 5,
      "subject_name": "Mathematics",
      "subject_short": "Maths",
      "subject_category_id": 2,
      "class_id": 812,
      "class_friendly": "10A Maths",
      "teacher_name": "Mr Smith",
      "comment": "A pleasing term's work.",
      "comment_generic": null,
      "result_term": 78,
      "result_ytd": 74.5,
      "symbol_term": "B",
      "symbol_ytd": "B",
      "level": null
    }
  ],
  "message": "",
  "response": {
    "error": "OK",
    "code": 200
  }
}
```

- `pupil_id` is the internal identifier of the pupil the row belongs to.
- `pupil_admin` is that pupil's user-provided identifier.
- All remaining fields are as described under [Reporting/comments](#reportingcommentsget-response).

### Reporting/grade/outcomes:get

Returns the same detail as [Reporting/outcomes](#reportingoutcomesget-response), for every pupil registered
for a given subject in a given grade during a published reporting period. Each row is prefixed with
`pupil_id` and `pupil_admin`; the remaining fields match the pupil-scoped endpoint.

#### Request {#reportinggradeoutcomesget-request}

```
GET /api/reporting/grade/outcomes/<grade>/<subject>/<period>
```

#### Parameters {#reportinggradeoutcomesget-parameters}

- `<grade>`: The grade identifier (required). Values are integers between -3 (Grade 0000) and 13 (Post Matric); negative values denote pre-primary grades.
- `<subject>`: The internal subject identifier (required).
- `<period>`: Reporting period identifier (required). The period must be published (see the note above).

#### Response {#reportinggradeoutcomesget-response}

As [Reporting/outcomes](#reportingoutcomesget-response), with each row prefixed by `pupil_id` and
`pupil_admin`.

### Reporting/grade/standards:get

Returns the same detail as [Reporting/standards](#reportingstandardsget-response), for every pupil
registered for a given subject in a given grade during a published reporting period. Each row is prefixed
with `pupil_id` and `pupil_admin`; the remaining fields match the pupil-scoped endpoint.

#### Request {#reportinggradestandardsget-request}

```
GET /api/reporting/grade/standards/<grade>/<subject>/<period>
```

#### Parameters {#reportinggradestandardsget-parameters}

- `<grade>`: The grade identifier (required). Values are integers between -3 (Grade 0000) and 13 (Post Matric); negative values denote pre-primary grades.
- `<subject>`: The internal subject identifier (required).
- `<period>`: Reporting period identifier (required). The period must be published (see the note above).

#### Response {#reportinggradestandardsget-response}

As [Reporting/standards](#reportingstandardsget-response), with each row prefixed by `pupil_id` and
`pupil_admin`.

### Reporting/grade/indicators:get

Returns the same detail as [Reporting/indicators](#reportingindicatorsget-response), for every pupil
registered for a given subject in a given grade during a published reporting period. Each row is prefixed
with `pupil_id` and `pupil_admin`; the remaining fields match the pupil-scoped endpoint.

#### Request {#reportinggradeindicatorsget-request}

```
GET /api/reporting/grade/indicators/<grade>/<subject>/<period>
```

#### Parameters {#reportinggradeindicatorsget-parameters}

- `<grade>`: The grade identifier (required). Values are integers between -3 (Grade 0000) and 13 (Post Matric); negative values denote pre-primary grades.
- `<subject>`: The internal subject identifier (required).
- `<period>`: Reporting period identifier (required). The period must be published (see the note above).

#### Response {#reportinggradeindicatorsget-response}

As [Reporting/indicators](#reportingindicatorsget-response), with each row prefixed by `pupil_id` and
`pupil_admin`.
