---
api_prefixes:
  - admin
  - changelog
  - cron
  - export
  - externalauth
  - formfields
  - leaves
  - medical
  - request
  - staff
  - tablefields
---

# Other Endpoints

These endpoints do not belong to a larger module. They cover tasks such as external authentication, field definitions, approved leaves, medical sport restrictions and the changelog.

All endpoints on this page are under one of these paths: `/api/admin/`, `/api/changelog/`, `/api/cron/`, `/api/export/`, `/api/externalauth/`, `/api/formfields/`, `/api/leaves/`, `/api/medical/`, `/api/request/`, `/api/staff/`, `/api/tablefields/`.

See [Authentication](api-access-to-adam.md#authentication) for how to send your API token.

### Admin/test:get

Internal test endpoint for verifying API connectivity.

#### Request {#admintestget-request}

```
GET /api/admin/test
```

#### Parameters {#admintestget-parameters}

None.

#### Response {#admintestget-response}

```json
{
  "data": "Successfully fetched data by asynchronous call from the server at 2026-04-09 14:30:00",
  "message": "",
  "response": {
    "error": "OK",
    "code": 200
  }
}
```

### Changelog/undo:post

Undoes a changelog entry, reverting a field to its previous value.

#### Request {#changelogundopost-request}

```
POST /api/changelog/undo/<changeSet>
```

#### Parameters {#changelogundopost-parameters}

-   `<changeSet>`: The changelog entry identifier (URL path parameter)

#### Response {#changelogundopost-response}

-   Code 200: Undo successful
-   Code 403: Cannot undo the original entry (no previous value to restore)
-   Code 202: Undo operation failed

### Cron/cronlog:get

Returns cron job execution logs. Restricted to super-admin tokens.

#### Request {#croncronlogget-request}

```
GET /api/cron/cronlog/<cronLogID>
```

#### Parameters {#croncronlogget-parameters}

-   `<cronLogID>`: Either a numeric log entry ID (returns that specific record with full log content) or any non-numeric value (returns all records without log content)

#### Response {#croncronlogget-response}

When requesting a specific entry, returns the full cron log record including log output. When requesting all entries, returns an array of records without the log body to reduce payload size.

### Export/families:get

Allows family information to be extracted easily.

#### Request {#exportfamiliesget-request}

```
GET /api/export/families
GET /api/export/families/all
GET /api/export/families/current
GET /api/export/families?updated_since=2024-10-01+08:15:30
GET /api/export/families/all?updated_since=2024-10-01+08:15:30
GET /api/export/families/current?updated_since=2024-10-01+08:15:30
```

#### Parameters {#exportfamiliesget-parameters}

The last parameter (all or current) may be omitted - the default setting is to return current families only. The structure of the data is unchanged.

An optional parameter, updated_since, will only return changes that have been made on or after the time specified. Any valid timestamp, that is URL encoded, can be used.

> [!NOTE]
> Note well that changes to email addresses are **not** reflected in the modified time.

#### Response {#exportfamiliesget-response}

Valid responses will contain an array of family objects in the data property. The family_primary_email and family_secondary_email will be arrays of email addresses:

```json
{
  "data": [
    {
      "family_id": 531,
      "family_admin": "0",
      "family_primary_lastname": "Adamson",
      "family_primary_firstname": "Adam",
      "family_primary_title": "Mr",
      "family_primary_idnum": "1234567890123",
      "family_primary_occupation": "Businessman",
      "family_primary_employer": "ADAM EduTech",
      "family_primary_workphone": "0615096077",
      "family_primary_cell": "0615096077",
      "family_secondary_lastname": "",
      "family_secondary_firstname": "",
      "family_secondary_idnum": "",
      "family_secondary_occupation": "",
      "family_secondary_employer": "",
      "family_secondary_workphone": "",
      "family_secondary_cell": "",
      "family_address_postal_1": "18 Lello Road",
      "family_address_postal_2": "",
      "family_address_postal_suburb": "Assagay",
      "family_address_postal_city": "Outer West Durban",
      "family_address_postal_province": "KwaZulu-Natal",
      "family_address_postal_code": "3600",
      "family_address_postal_country": "South Africa",
      "family_address_residential_1": "18 Lello Road",
      "family_address_residential_2": "",
      "family_address_residential_suburb": "Assagay",
      "family_address_residential_city": "Outer West Durban",
      "family_address_residential_province": "KwaZulu-Natal",
      "family_address_residential_code": "3610",
      "family_address_residential_country": "South Africa",
      "family_notes": "",
      "family_modify": "2024-09-18 08:37:41",
      "family_primary_email": [
        "testing+primary@testing.adam.co.za",
        "testing+primary2@testing.adam.co.za"
      ],
      "family_secondary_email": [
      ]
    }
  ],
  "message": "",
  "response": {
    "error": "OK",
    "code": 200
  }
}
```

### ExternalAuth/auth:post

Allows ADAM to be used as an external authentication source.

> [!WARNING]
> Note well: this API endpoint will divulge user information for a valid login name. As with any API key, it is imperative that it is kept secret and changed if a breach is suspected.

#### Request {#externalauthauthpost-request}

```
POST /api/externalauth/auth/
```

#### Parameters {#externalauthauthpost-parameters}

These parameters are sent via form-data parameters.

- username: The username of the staff member or pupil, or the Identification number or passport number of a family member.
- password: The password associated with the username

#### Response {#externalauthauthpost-response}

Integrating systems should check the HTTP response code rather than the presence of user information in the data object.

If a valid username and password are supplied, the HTTP response code will be 200. The data object contains the user information and the contained response code will be 200:

```json
{
  "data": {
    "username": "admin",
    "firstname": "Patrick",
    "lastname": "Cloete",
    "email": "testing+staff_1@adam.co.za",
    "type": "staff",
    "id": "1"
  },
  "message": "",
  "response": {
    "error": "Login successful",
    "code": 200
  }
}
```

If a valid username is supplied, but the password is incorrect, the HTTP response code will be 401. The data object will contain user information and the contained response code will be 401:

```json
{
  "data": {
    "username": "admin",
    "firstname": "Patrick",
    "lastname": "Cloete",
    "email": "testing+staff_1@adam.co.za",
    "type": "staff",
    "id": "1"
  },
  "message": "",
  "response": {
    "error": "Username or password not recognised",
    "code": 401
  }
}
```

If an invalid username is supplied, the HTTP response code will be 401. The data object will be empty and the contained response code will be 401.

```json
{
  "data": [],
  "message": "",
  "response": {
    "error": "Username or password not recognised",
    "code": 401
  }
}
```

### FormFields/fields:get

Returns field definitions for a specified database table.

#### Request {#formfieldsfieldsget-request}

```
GET /api/formfields/fields/<table>/<action>
```

#### Parameters {#formfieldsfieldsget-parameters}

- `<table>`: Table name (required)
- `<action>`: Action context (optional)

#### Response {#formfieldsfieldsget-response}

Data attribute maps field names to their descriptions.

### Leaves/approved:get

Gets a list of approved leaves with an end date that is either today or in the future.

#### Request {#leavesapprovedget-request}

```
GET /api/leaves/approved[/<pupil>]
```

#### Parameters {#leavesapprovedget-parameters}

- `<pupil>`: Optional: The identifier of the pupil in question.

#### Response {#leavesapprovedget-response}

```
GET /api/leaves/approved/6050
```

```json
{
  "data": [
    {
      "leave_request_id": 4765,
      "leave_request_out": "2024-10-18 14:15:00",
      "leave_request_in": "2024-10-20 18:30:00",
      "leave_request_destination": "Home",
      "leave_request_host": "Parents",
      "leave_request_host_contact": "083",
      "leave_request_notes": "thanks",
      "leave_request_approval_notes": "\\n",
      "leave_request_status": "Approved",
      "leave_request_user_id": 1,
      "leave_request_user_type": "staff",
      "leave_request_submitted_datetime": "2024-10-15 10:37:01",
      "leave_request_reminder_datetime": null,
      "leave_request_choices": "Will he need Saturday Lunch:No\\nWill he need Sunday Supper:No\\nDo you need a gate code:No\\n",
      "leave_type_id": 1,
      "leave_type_description": "Full Weekend Leave",
      "leave_type_overnight": "Yes",
      "leave_type_off_campus": "Yes"
    }
  ],
  "message": "Leaves for Joseph Tshabalala",
  "response": {
    "error": "OK",
    "code": 200
  }
}
```

The **data** attribute contains an array of 0 or more leave records.

### Medical/offsport:get

Returns a list of pupil IDs currently off sport due to medical reasons.

#### Request {#medicaloffsportget-request}

```
GET /api/medical/offsport/<date>
```

#### Parameters {#medicaloffsportget-parameters}

- `<date>`: ISO-formatted date (optional; defaults to current date)

#### Response {#medicaloffsportget-response}

```json
{
  "data": [1234, 1567, 1890],
  "message": "Offsport list for 2026-04-09.",
  "response": { "error": "OK", "code": 200 }
}
```

### Request/test:get

A test method to the API.

#### Request {#requesttestget-request}

```
GET /api/request/test/[Parameter1]/[Parameter2]
```

#### Parameters {#requesttestget-parameters}

[Parameter1]: An arbitrary parameter that is returned.

[Parameter2]: An arbitrary parameter that is returned.

#### Output

The output data will be a JSON object containing attributes parameter1 and parameter2, both of which will contain the values provided in the request.

**Example:**

```
https://demo.adam.co.za/api/request/test/First%20Parameter/Second
```

```json
{
  "data": {
    "parameter1": "First Parameter",
    "parameter2": "Second"
  },
  "message": "Hello, you're speaking to Random High School's ADAM. We are currently on revision 6125 and the local time is 11:26:46.",
  "response": {
    "error": "OK",
    "code": 200
  }
}
```

### Staff/image:get

Returns an image of a staff member.

#### Request {#staffimageget-request}

```
GET /api/staff/image/<staff_id>
```

#### Parameters {#staffimageget-parameters}

- `<staff_id>`: The internal identifier of the pupil.

#### Response {#staffimageget-response}

```
GET /api/reporting/staff/image/123
```

Unlike other API calls, this will return an image file and not a JSON object. The image type will be specified by the response’s Content-Type header, but will almost certainly be a JPG image. A response code of 404 suggests that the image does not exist.

### TableFields/fields:get

Returns field definitions for a specified database table. Similar to FormFields/fields but uses the TableFields system.

#### Request {#tablefieldsfieldsget-request}

```
GET /api/tablefields/fields/<table>/<action>
```

#### Parameters {#tablefieldsfieldsget-parameters}

- `<table>`: Table name (required)
- `<action>`: Action context (optional)

#### Response {#tablefieldsfieldsget-response}

Data attribute maps field names to their descriptions.
