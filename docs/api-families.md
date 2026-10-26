---
api_prefixes:
  - families
  - familylogin
---

# Families

Use these endpoints to find families and their children, read and change family details and email addresses, and link a family to a pupil. They also report the privileges of a family login.

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
