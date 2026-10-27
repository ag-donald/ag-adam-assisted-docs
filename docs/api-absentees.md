---
api_prefixes:
  - absentees
  - absenteekiosk
---

# Absentees

Use these endpoints to list the pupils who are absent, count each pupil's days absent, and view a pupil's absentee log. They also register a pupil as present or late, as the absentee kiosk does.

All endpoints on this page are under one of these paths: `/api/absentees/`, `/api/absenteekiosk/`.

See [Authentication](api-access-to-adam.md#authentication) for how to send your API token.

### AbsenteeKiosk/register:post

This registers a pupil as either present or late. It is intended to be used either by automated access control systems
or ADAM’s own absentee kiosk.

#### Request

- `POST` to `/api/absenteekiosk/register/<pupil>`
- `POST` to `/api/absenteekiosk/register` with `pupil=<pupil>` as a form variable in the POST body

#### Parameters

- `<pupil>`: The ADAM identifier of the pupil.

#### Response

If the pupil identifier can be matched against an existing pupil, the endpoint will return two items in the data object.
These are used internally by ADAM’s “Absentee Kiosk” feature.

- `message`: an HTML message which will contain the name of the pupil and confirmation that they have been registered.
- `colour`: an HTML hex code either red, green or amber depending on the status.

The times and windows are configured in ADAM’s site settings. Depending on these settings, ADAM will report one of the
following HTTP status codes:

- The pupil identifier is not recognised: `404 (Not found)`
- The pupil is too early and registers before the earliest time allowed: `406 (Not acceptable)`
- The pupil registers during the first window and is recorded as present: `200 (OK)`
- The pupil registers during the second window and is recorded as late: `202 (Accepted)`
- The pupil is too late and registers after the second window closes: `406 (Not acceptable)`

In each case, the status code will be corroborated by a more descriptive message.

**Example:**

```json
{
  "data": {
    "message": "<strong>Joe Smith</strong> has been recorded as <strong>present</strong>",
    "colour": "green"
  },
  "message": "",
  "response": {
    "error": "Present",
    "code": 200
  }
}
```

### Absentees/summarycount:get

Returns a list of pupils and the number of days they’ve been absent. This counts all the absentees with a reason that is
set to count as “absent”. Only pupils with absentee records are returned. All pupils, including those that might have
left the school, are returned.

#### Request {#absenteessummarycountget-request}

```
GET /api/absentees/summarycount/<from>[/<to>]
```

#### Parameters {#absenteessummarycountget-parameters}

- `<from>`: An ISO formatted date to begin the summary. This date is included in the summary.
- `<to>`: OPTIONAL. An ISO formatted date to mark the end of the range of the summary. This date is included in the
  summary. If omitted, the current date is used instead.

#### Response {#absenteessummarycountget-response}

The data attribute will be an array of zero or more JSON objects.

**Example:**

```
GET /api/absentees/summarycount/2018-01-01/2018-01-31
```

```json
{
  "data": [
    {
      "pupil_id": 875,
      "pupil_admin": "19634",
      "absent_count": 1
    },
    {
      "pupil_id": 879,
      "pupil_admin": "52351",
      "absent_count": 2
    }
  ],
  "message": "Absentee counts for all pupils from 2018-01-01 to 2018-01-31.",
  "response": {
    "error": "OK",
    "code": 200
  }
}
```

- `pupil_id` is ADAM’s internal database identifier and will always refer to a unique pupil.
- `pupil_admin` is the user-defined administration number. While this should not change, it may do so at the school’s
  discretion.
- `absentee_count` is the number of days that the pupil has been recorded as absent. This does not include absentee
  records which do not prejudice a pupil (such as “away on sports tour”). These reasons are customisable by the school.

### Absentees/list:get

Gets a list of pupils absent with the reasons.

#### Request {#absenteeslistget-request}

```
GET /api/absentees/list/[<date>[/<to>]]
```

#### Parameters {#absenteeslistget-parameters}

- `<date>`: OPTIONAL. An ISO formatted date to query the absentees. If omitted, today’s date is used.
- `<to>`: OPTIONAL. An ISO formatted date. If provided, all absentees on or between the `<date>` and `<to>` dates will be
  provided. If omitted, `<to>` effectively takes the same value as `<date>` and only absentees for that date are provided.

#### Response {#absenteeslistget-response}

```
GET /api/absentees/list/2018-01-30
```

```json
{
  "data": [
    {
      "pupil_id": 1720,
      "pupil_admin": "47547",
      "absent_date": "2018-01-31",
      "absent_reason_id": 1,
      "absent_reason_description": "Absent",
      "absent_notes": "App Test"
    }
  ],
  "message": "Absentee list for all pupils from 2018-01-31 to 2018-01-31.",
  "response": {
    "error": "OK",
    "code": 200
  }
}
```

The data attribute contains an array of zero or more absentee records. Each record is a JSON object with the following
properties:

- `pupil_id` is ADAM’s internal identifier for the pupil.
- `pupil_admin` is a school-provided identifier for the pupil. While this should not change, it may do so at the
  school’s discretion.
- `absent_date` gives the date that the absentee occurred on in case a range of dates was requested. A pupil can only
  have a single absentee record per day.
- `absent_reason` is an internal identifier corresponding to the absentee reason that was chosen.
- `absent_reason_description` is the descriptor for the absentee reason. It will be consistent per `absent_reason` in
  any one API call, but may change between calls at the school’s discretion.
- `absent_notes` contain the end-user provided notes related to the pupil’s absence. This may contain personal
  information.

### Absentees/daysabsentforpupil:get

Returns the absentee log for a specific pupil.

#### Request {#absenteesdaysabsentforpupilget-request}

```
GET /api/absentees/daysabsentforpupil/<pupil>/<year>
```

#### Parameters {#absenteesdaysabsentforpupilget-parameters}

- `<pupil>`: ADAM internal pupil identifier (required)
- `<year>`: Calendar year to filter by (optional; returns all records if omitted)

#### Response {#absenteesdaysabsentforpupilget-response}

Data attribute contains the pupil's absentee log entries.
