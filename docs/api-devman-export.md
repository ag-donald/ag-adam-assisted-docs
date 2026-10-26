---
api_prefixes:
  - xdevman
---

# DevMan Export

Use these endpoints to export lists of current pupils, leavers and alumni, with their last-modified dates, and the details of a single alumnus.

All endpoints on this page are under `/api/xdevman/`.

See [Authentication](api-access-to-adam.md#authentication) for how to send your API token.

### XDevMan/alumni:get

Returns a list of Alumni and their last-modified dates

#### Request {#xdevmanalumniget-request}

```
GET /api/xdevman/alumni/<year>
```

#### Parameters {#xdevmanalumniget-parameters}

- `<year>`: The year of matriculation of the pupils

#### Response {#xdevmanalumniget-response}

```
GET /api/xdevman/alumni/2019
```

```json
{
  "data": [
    {
      "pupil_id": "2240",
      "pupil_admin": "7623",
      "pupil_modify": "2019-11-11 16:25:54",
      "alumni_modify": "2020-01-02 16:04:04"
    },
    {
      "pupil_id": "1319",
      "pupil_admin": "7289",
      "pupil_modify": "2019-11-11 16:25:54",
      "alumni_modify": "2020-01-02 16:04:04"
    }
  ],
  "message": "",
  "response": {
    "error": "OK",
    "code": 200
  }
}
```

In each record, the internal ID and school-provided administration number are returned. There are two modification times because data for alumni is stored in two separate places (one from the historical pupil information, and another from the alumni-specific information).

### XDevMan/currentpupils:get

Returns a list of current pupils and their list of modification dates.

#### Request {#xdevmancurrentpupilsget-request}

```
GET /api/xdevman/currentpupils
```

#### Parameters {#xdevmancurrentpupilsget-parameters}

- none

#### Response {#xdevmancurrentpupilsget-response}

```
GET /api/xdevman/currentpupils
```

```json
{
  "data": [
    {
      "pupil_id": "2240",
      "pupil_admin": "7623",
      "pupil_modify": "2019-11-11 16:25:54"
    },
    {
      "pupil_id": "1319",
      "pupil_admin": "7289",
      "pupil_modify": "2019-11-11 16:25:54"
    }
  ],
  "message": "",
  "response": {
    "error": "OK",
    "code": 200
  }
}
```

In each record, the internal ID and school-provided administration number are returned. There are two modification times because data for alumni is stored in two separate places (one from the historical pupil information, and another from the alumni-specific information).

### XDevMan/leavers:get

Returns a list of Leavers and their last-modified dates. A leaver for a year is a person who was deregistered during the course of that year. It includes people from all grades.

#### Request {#xdevmanleaversget-request}

```
GET /api/xdevman/leavers/<year>
```

#### Parameters {#xdevmanleaversget-parameters}

- `<year>`: The year of matriculation of the pupils

#### Response {#xdevmanleaversget-response}

```
GET /api/xdevman/leavers/2019
```

```json
{
  "data": [
    {
      "pupil_id": "2240",
      "pupil_admin": "7623",
      "pupil_modify": "2019-11-11 16:25:54",
      "alumni_modify": "2020-01-02 16:04:04"
    },
    {
      "pupil_id": "1319",
      "pupil_admin": "7289",
      "pupil_modify": "2019-11-11 16:25:54",
      "alumni_modify": "2020-01-02 16:04:04"
    }
  ],
  "message": "",
  "response": {
    "error": "OK",
    "code": 200
  }
}
```

In each record, the internal ID and school-provided administration number are returned. There are two modification times because data for alumni is stored in two separate places (one from the historical pupil information, and another from the alumni-specific information).

### XDevMan/alumnus:get

Returns the details of a single alumnus.

#### Request {#xdevmanalumnusget-request}

```
GET /api/xdevman/alumnus/<pupil_id>
```

#### Parameters {#xdevmanalumnusget-parameters}

- `<year>`: The year of matriculation of the pupils

#### Response {#xdevmanalumnusget-response}

```
GET /api/xdevman/alumnus/999
```

```json
{
  "data": {
    "pupil_id": "999",
    "pupil_admin": "6727",
    "pupil_lastname": "xxx",
    "pupil_firstname": "xxx",
    "pupil_fullfirst": "xxx",
    "pupil_birth": "1994-08-xx",
    "pupil_final": "2012",
    "pupil_gender": "Female",
    "pupil_entry": "2010-07-12",
    "pupil_exit": "2012-12-31",
    "pupil_idnumber": "9408xxx",
    "pupil_population_id": "4",
    "pupil_language_id": "2",
    "pupil_language_other": "",
    "pupil_email": "",
    "pupil_email_personal": "",
    "pupil_prepschool": "xxx",
    "pupil_nationality": "South Africa",
    "pupil_boarder": "3",
    "alumni_title": "Miss",
    "alumni_marital_status": "",
    "alumni_maiden_name": "",
    "alumni_spouse_title": "",
    "alumni_spouse_firstname": "",
    "alumni_spouse_gender": null,
    "alumni_spouse_occupation": "",
    "alumni_date_married": "0000-00-00",
    "alumni_region": "",
    "alumni_district": "",
    "alumni_branch_id": null,
    "alumni_type_id": "1",
    "alumni_deceased": "No",
    "alumni_deceased_date": null,
    "alumni_workphone": "",
    "alumni_homephone": "(031) xxx 6xxx",
    "alumni_other": "",
    "alumni_reason_left": "",
    "alumni_exit_grade": "12",
    "alumni_previous_school": null,
    "alumni_qualification": "Senior Certificate",
    "family": {
      "families": [
        {
          "family_id": "873",
          "family_admin": "0",
          "family_primary_lastname": "xxx",
          "family_primary_firstname": "xxx",
          "family_primary_fullfirst": "xxx",
          "family_primary_initials": "X",
          "family_primary_title": "Mr",
          "family_primary_idnum": "651xxxx",
          "family_primary_gender": "Male",
          "family_primary_occupation": "xxx",
          "family_primary_employer": "xxx",
          "family_primary_workphone": "0315xxx",
          "family_primary_cell": "083xxx",
          "family_primary_birth": "1965-10-xx",
          "family_secondary_lastname": "xxx",
          "family_secondary_firstname": "xxx",
          "family_secondary_fullfirst": "xxx",
          "family_secondary_initials": "X",
          "family_secondary_title": "Mrs",
          "family_secondary_idnum": "6607xxx",
          "family_secondary_gender": "Female",
          "family_secondary_occupation": "xxx",
          "family_secondary_employer": "xxx",
          "family_secondary_workphone": "0315xxx",
          "family_secondary_cell": "083xxx",
          "family_secondary_birth": "1966-07-xx",
          "family_address_postal_1": "xxx",
          "family_address_postal_2": "xxx",
          "family_address_postal_suburb": "xxx",
          "family_address_postal_city": "",
          "family_address_postal_province": "",
          "family_address_postal_code": "xxx",
          "family_address_postal_country": "South Africa",
          "family_address_residential_1": "xxx",
          "family_address_residential_2": "xxx",
          "family_address_residential_suburb": "xxx",
          "family_address_residential_city": "",
          "family_address_residential_province": "",
          "family_address_residential_code": "",
          "family_address_residential_country": "xxx",
          "family_home_phone": "03150xxx",
          "family_home_fax": "03150xxx"
        }
      ],
      "email": [
        {
          "email_family_id": "873",
          "email_member": "primary",
          "email_address": "xxx@example.com"
        },
        {
          "email_family_id": "873",
          "email_member": "secondary",
          "email_address": "yyy@example.com"
        }
      ]
    }
  },
  "message": "",
  "response": {
    "error": "OK",
    "code": 200
  }
}
```

A record of a single alumnus is returned.
