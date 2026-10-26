---
api_prefixes:
  - families
  - familylogin
---

# Families

Use these endpoints to find families and their children, read and change family details, email addresses and the communication each address receives, and link a family to a pupil. They also report the privileges of a family login.

All endpoints on this page are under one of these paths: `/api/families/`, `/api/familylogin/`.

See [Authentication](api-access-to-adam.md#authentication) for how to send your API token.

### Families/currentchildren:get

#### Request {#familiescurrentchildrenget-request}

```
GET /api/families/currentchildren/<family_id>
```

#### Parameters {#familiescurrentchildrenget-parameters}

- `<family_id>`: The internal identifier of the family.

#### Response {#familiescurrentchildrenget-response}

This query returns an array of pupils. If no pupils are attached to the family, or if the family identifier does not exist, then the response will be returned with a “404” HTTP status code.

```json
{
  "data": [
    "49",
    "4688"
  ],
  "message": "",
  "response": {
    "error": "OK",
    "code": 200
  }
}
```

### Families/email:get

Get a list of email addresses associated with a family or family member.

#### Request {#familiesemailget-request}

```
GET /api/families/email/<family_id>[/(primary|secondary)]
```

#### Parameters {#familiesemailget-parameters}

- `<family_id>`: The internal identifier of the family.
- (primary|secondary): OPTIONAL - whether to return only email addresses of the primary or secondary parent

#### Response {#familiesemailget-response}

This query returns an array of zero or more email address records.

```json
{
  "data": [
    {
      "email_id": 9372,
      "email_family_id": 123,
      "email_member": "primary",
      "email_address": "testing+245@test.adam.co.za",
      "email_description": "",
      "email_bulkmail": "Yes",
      "email_reports": "Yes",
      "email_alerts": "Yes",
      "email_maillog": "Yes",
      "email_modify": "2025-02-21 12:00:42"
    }
  ],
  "message": "",
  "response": {
    "error": "OK",
    "code": 200
  }
}
```

### Families/email:post

Add an email address to a family member.

#### Request {#familiesemailpost-request}

```
POST /api/families/email/<family_id>/(primary|secondary)
```

#### Parameters {#familiesemailpost-parameters}

- `<family_id>`: The internal identifier of the family.
- (primary|secondary): Which parent the email address should be added to

In the POST body:

- email: a string containing the email address

#### Response {#familiesemailpost-response}

“201 Created” if added successfully, 200 if not added, with an appropriate error message in the response.error property (e.g. the email address may already exist?).

### Families/email:patch

Change the address or description of one of a family's email addresses.

#### Request {#familiesemailpatch-request}

```
PATCH /api/families/email/<email_id>
```

#### Parameters {#familiesemailpatch-parameters}

- `<email_id>`: The identifier of the email address record. This is the `email_id` property returned by [Families/email:get](#familiesemailget).

The body of the request is a JSON object containing one or both of these fields:

- `address`: a string containing the new email address. It must be a valid email address.
- `description`: a string containing the new description for the email address.

```json
{
  "address": "parent@example.com",
  "description": "Work"
}
```

ADAM removes whitespace, such as spaces, tabs and line breaks, from the start and end of each value. A field that is left out, or set to `null`, is not changed. Any other field in the body is rejected.

#### Response {#familiesemailpatch-response}

On success, the **data** attribute contains the updated email address record, with these properties:

- `email_id`: the identifier of the email address record.
- `email_family_id`: the internal identifier of the family.
- `email_member`: `primary` or `secondary`, the parent the address belongs to.
- `email_address`: the email address.
- `email_description`: the description of the email address.
- `email_maillog`: `Yes` or `No`.
- `email_modify`: the date and time the record was last changed.

Response codes:

- Code 200: The email address record was updated.
- Code 400: The body is empty, is not valid JSON, has no value for either field, contains a field other than `address` or `description`, contains a value that is not a string, or contains an address that is not a valid email address.
- Code 404: No email address record has this identifier.
- Code 409: The same parent in the family already has this email address.

### Families/email:delete

Remove an email address to a family member.

#### Request {#familiesemaildelete-request}

```
DELETE /api/families/email/<family_id>/(primary|secondary)
```

#### Parameters {#familiesemaildelete-parameters}

- `<family_id>`: The internal identifier of the family.
- (primary|secondary): Which parent the email address should be added to

In the body which must be x-www-form-urlencoded:

- email: a string containing the email address to delete

#### Response {#familiesemaildelete-response}

200 if deleted successfully, 404 if not found, with an appropriate error message in the response.error property.

### Families/emailpreferences:patch

Change which types of communication an email address receives.

#### Request {#familiesemailpreferencespatch-request}

```
PATCH /api/families/emailpreferences/<email_id>
```

#### Parameters {#familiesemailpreferencespatch-parameters}

- `<email_id>`: The identifier of the email address record. This is the `email_id` property returned by [Families/email:get](#familiesemailget).

The body of the request is a JSON object with a `preferences` object. Each key in `preferences` is a communication type, and each value is `true` to receive that type of communication or `false` to stop receiving it. Values must be JSON `true` or `false`, not strings.

```json
{
  "preferences": {
    "messaging.bulkmail": false,
    "reports.academic": true
  }
}
```

Communication types that are left out are not changed. The communication types include these, listed with the name shown under **Administration → Messaging Administration → Communication preference settings**:

- `messaging.bulkmail`: General Communication
- `reports.academic`: Academic Reports
- `alerts.periodic`: Parent Notifications
- `families.updates`: Family Update Requests
- `leaves.notifications`: Leave Notifications
- `agreements.copies`: Online Agreements
- `transactional.system`: System Notifications

There are also communication types for individual notifications, with keys that start with `notifications.`. A successful response lists every communication type, so use it to find the full set.

If any key is not a known communication type, or any value is not `true` or `false`, the request is rejected and no preferences are changed.

When it saves the preferences, this endpoint does not enforce the school's [communication policies](communication-policies.md). In particular, it does not stop every address in a family from opting out of a **Required** communication type.

#### Response {#familiesemailpreferencespatch-response}

On success, the **data** attribute maps every communication type to `true` or `false`: whether this email address now receives that type of communication. The example below is shortened; a real response lists every communication type.

```json
{
  "data": {
    "messaging.bulkmail": false,
    "reports.academic": true,
    "transactional.system": true
  },
  "message": "",
  "response": {
    "error": "OK",
    "code": 200
  }
}
```

The values take the school's communication policies into account. A communication type whose policy is **Mandatory** is always `true`, and one whose policy is **Disabled** is always `false`, whatever the request set.

Response codes:

- Code 200: The preferences were saved.
- Code 400: The request was rejected. The response.error property gives the reason:
    - `No preferences provided for update.`: the body is empty.
    - `Input was not valid json: ` followed by the parser's message: the body is not valid JSON.
    - `Missing or invalid 'preferences' object.`: the body has no `preferences` object, or the object is empty.
    - `Invalid preferences payload.`: the `preferences` object contains an unknown communication type, or a value that is not `true` or `false`.
- Code 404: No email address record has this identifier.

### Families/searchbyid:get

#### Request {#familiessearchbyidget-request}

```
GET /api/families/searchbyid/<RSA_ID_Number>
```

#### Parameters {#familiessearchbyidget-parameters}

- `<RSA_ID_Number>`: A South African ID number or international passport number for parents without an ID number. The parameter should be trimmed of spaces. This performs a simple text match with the database field and thus relies on reasonable data hygiene.

#### Response {#familiessearchbyidget-response}

This response returns an array of generally one family identifier, but if an ID number is associated with many parents, all will be returned in the array. This is discouraged in the interface, but schools may still do this.

Where the ID number cannot be found, a response will be returned with an HTTP 404 status code.

```json
{
  "data": [
    "1234"
  ],
  "message": "",
  "response": {
    "error": "OK",
    "code": 200
  }
}
```

### Families/children:get

Returns the children linked to a family. Alias: families/get_children_by_family.

#### Request {#familieschildrenget-request}

```
GET /api/families/children/<family>
```

#### Parameters {#familieschildrenget-parameters}

- `<family>`: ADAM internal family identifier (required)

#### Response {#familieschildrenget-response}

Data attribute contains an array of child records with pupil details, grade, and default class status.

```json
{
  "data": [
    {
      "pupil_id": 1234,
      "pupil_lastname": "Smith",
      "pupil_firstname": "John",
      "pupil_grade": "Grade 10",
      "pupil_defaultclass": "10A"
    }
  ]
}
```

Note: Pupils at the "pre" (admissions) stage show "Admission" instead of a class name, and will show their current grade rather than their grade of entry.

### Families/get_children_by_family:get

This endpoint is equivalent to [Families/children:get](#familieschildrenget). It takes the same parameters and returns the same response.

#### Request {#familiesget_children_by_familyget-request}

```
GET /api/families/get_children_by_family/<family>
```

### Families/contactlist:get

Returns contact details for all families.

#### Request {#familiescontactlistget-request}

```
GET /api/families/contactlist
```

#### Parameters {#familiescontactlistget-parameters}

None.

#### Response {#familiescontactlistget-response}

```json
{
  "data": [
    {
      "id": 500,
      "primary": {
        "firstname": "Jane",
        "lastname": "Smith",
        "cell": "0821234567",
        "email": ["jane@example.com"]
      },
      "secondary": {
        "firstname": "John",
        "lastname": "Smith",
        "cell": "0829876543",
        "email": ["john@example.com"]
      }
    }
  ]
}
```

If no secondary contact exists, the secondary field is an empty array.

### Families/familyrelationships:get

Returns all pupil-to-family relationship mappings.

#### Request {#familiesfamilyrelationshipsget-request}

```
GET /api/families/familyrelationships
```

#### Parameters {#familiesfamilyrelationshipsget-parameters}

None.

#### Response {#familiesfamilyrelationshipsget-response}

```json
{
  "data": [
    { "pupil": 1234, "family": 500 },
    { "pupil": 1235, "family": 500 }
  ]
}
```

### Families/fields:get

Returns the list of valid fields for family records.

#### Request {#familiesfieldsget-request}

```
GET /api/families/fields/<action>
```

#### Parameters {#familiesfieldsget-parameters}

- `<action>`: Action context (optional; e.g. "add" or "edit" to filter relevant fields)

#### Response {#familiesfieldsget-response}

Data attribute contains a mapping of field names to their descriptions.

### Families/add:post

Creates a new family record.

#### Request {#familiesaddpost-request}

```
POST /api/families/add
```

#### Parameters {#familiesaddpost-parameters}

JSON request body containing family fields. Use families/fields to retrieve valid field names.

#### Response {#familiesaddpost-response}

- Code 200: Returns the new family ID
- Code 400: Validation error — response includes list of invalid fields

### Families/family:patch

Updates an existing family record.

#### Request {#familiesfamilypatch-request}

```
PATCH /api/families/family/<family>
```

#### Parameters {#familiesfamilypatch-parameters}

- `<family>`: ADAM internal family identifier (URL path parameter)
- JSON request body containing fields to update

#### Response {#familiesfamilypatch-response}

- Code 200: Returns the updated family record
- Code 400: Validation error
- Code 404: Family not found

### Families/link:post

Links a pupil to a family with specified relationship types.

#### Request {#familieslinkpost-request}

```
POST /api/families/link
```

#### Parameters {#familieslinkpost-parameters}

JSON request body:

```json
{
  "family_id": 500,
  "pupil_id": 1234,
  "primary_relationship": "biological",
  "secondary_relationship": "biological"
}
```

Valid relationship types: biological, adoptive parent, step parent, foster parent, guardian, sponsor, relative, other.

#### Response {#familieslinkpost-response}

Code 200 on success.

### Families/detailsupdateform:get

Triggers an email to the family with a details update form.

#### Request {#familiesdetailsupdateformget-request}

```
GET /api/families/detailsupdateform/<family>
```

#### Parameters {#familiesdetailsupdateformget-parameters}

- `<family>`: ADAM internal family identifier (required)

#### Response {#familiesdetailsupdateformget-response}

No data returned.

- Code 200: "Detail update form sent."
- Code 500: Error sending form

### FamilyLogin/privileges:get

Returns the portal permissions available for the currently authenticated family or pupil login.

#### Request {#familyloginprivilegesget-request}

```
GET /api/familylogin/privileges
```

#### Parameters {#familyloginprivilegesget-parameters}

None — uses the current authentication session context.

#### Response {#familyloginprivilegesget-response}

Data attribute maps pupil IDs to their available permission strings.

```json
{
  "data": {
    "1234": ["marks", "reports", "absentee", "stats"],
    "1235": ["marks", "reports"]
  }
}
```
