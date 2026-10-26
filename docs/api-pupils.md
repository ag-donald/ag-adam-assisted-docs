---
api_prefixes:
  - pupils
---

# Pupils

Use these endpoints to search for pupils, read and change pupil records, add a pupil, and retrieve a pupil's image.

All endpoints on this page are under `/api/pupils/`.

See [Authentication](api-access-to-adam.md#authentication) for how to send your API token.

### Pupils/image:get

Returns a pupil's photograph, resized to a given width.

#### Request {#pupilsimageget-request}

```
GET /api/pupils/image/<pupil_id>[/<width>]
```

#### Parameters {#pupilsimageget-parameters}

- `<pupil_id>`: The internal identifier of the pupil (required).
- `<width>`: OPTIONAL. The maximum width of the image in pixels. If omitted, a width of 200 pixels is used. The height is scaled to keep the image's proportions. If the width is larger than the photograph's own width, the photograph is returned at its own size and is not enlarged.

#### Response {#pupilsimageget-response}

```
GET /api/pupils/image/123/400
```

Unlike other API calls, this returns an image file and not a JSON object.

The image data is always in PNG format. The response's `Content-Type` header gives the file type of the photograph as it was uploaded to ADAM (for example `image/jpeg`), which may not be PNG. Read the image data as PNG, or detect the format from the data itself, rather than relying on the `Content-Type` header.

A 404 response, with no body, means that there is no photograph for that pupil identifier, or that the photograph could not be read as an image.

### Pupils/add:post

#### Request {#pupilsaddpost-request}

```
POST /api/pupils/add
```

#### Parameters {#pupilsaddpost-parameters}

The body of the request is a JSON object of field names and values.

```json
{
  "pupil_id": 123,
  "pupil_lastname": "Adams",
  "pupil_firstname": "Adam",
  ...
}
```

#### Response {#pupilsaddpost-response}

The response code will determine whether the pupil was added or not, with invalid requests returning a 400 error. Acceptable field names can be inspected by using the [pupils/pupil:get](#pupilspupilget) endpoint. The following fields are mandatory:

- pupil_lastname - the pupil’s last name
- pupil_firstname - the pupil’s preferred legal name
- pupil_fullfirst - the pupil’s full names, excluding last name
- pupil_final - the pupil’s estimated Grade 12 year (NB - this must be the year of their Grade 12 year, even at a primary school level. ADAM uses this year to calculate the current grade a pupil is in)
- pupil_entry - the date when a pupil will enter the school. For pupils starting school at the start of an academic year, it is suggested to use is ‘year-01-01’ rather than the first day of term.

Note that while pupils may be added to the database even if these fields are omitted, doing so will make the pupils nearly impossible to manage on the receiving end.

For fields ending in an “_id” suffix, some values can be determined from [Appendix A](appendix-a-import-and-export-codes.md#appendix-a-import-and-export-codes). Note that pupil_registration_id field refers to a many-to-many relationship and thus cannot be completed by this end-point. If it exists in the submitted data, it is silently discarded.

If any other invalid fields are passed in, the response message will contain details of those invalid fields.

### Pupils/pupil:get

#### Request {#pupilspupilget-request}

```
GET /api/pupils/pupil/<ADAM_Identifier>
```

#### Parameters {#pupilspupilget-parameters}

- `<ADAM_Identifier>`: An integer referring to the pupil’s internal ADAM identifier.

#### Response {#pupilspupilget-response}

This response returns a JSON object of data for a single pupil.

Where the identifier cannot be found, a response will be returned with an HTTP 404 status code.

```json
{
  "data": {
    "pupil_id": 123,
    "pupil_lastname": "Adams",
    "pupil_firstname": "Adam",
    ...
  },
  "message": "",
  "response": {
    "error": "OK",
    "code": 200
  }
}
```

### Pupils/search-admin:get

#### Request {#pupilssearch-adminget-request}

```
GET /api/pupils/search-admin/<AdminNumber>
```

#### Parameters {#pupilssearch-adminget-parameters}

- `<AdminNumber>`: The school-assigned administration number for a pupil. The parameter should be trimmed of spaces. This performs a simple text match with the database field and thus relies on reasonable data hygiene.

#### Response {#pupilssearch-adminget-response}

This response returns an array of generally one pupil identifier, but if an Admin number is associated with many pupils, all will be returned in the array. This is discouraged in the interface, but schools may still do this.

Where the Admin number cannot be found, a response will be returned with an HTTP 404 status code.

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

### Pupils/searchbyid:get

#### Request {#pupilssearchbyidget-request}

```
GET /api/pupils/search-id/<RSA_ID_Number>
GET /api/pupils/searchbyid/<RSA_ID_Number>
```

#### Parameters {#pupilssearchbyidget-parameters}

- `<RSA_ID_Number>`: A South African ID number or international passport number for pupils without an ID number. The parameter should be trimmed of spaces. This performs a simple text match with the database field and thus relies on reasonable data hygiene.

#### Response {#pupilssearchbyidget-response}

This response returns an array of generally one pupil identifier, but if an ID number is associated with many pupils, all will be returned in the array. This is discouraged in the interface, but schools may still do this.

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

### Pupils/fields:get

Returns the list of valid fields for pupil records.

#### Request {#pupilsfieldsget-request}

```
GET /api/pupils/fields/<action>
```

#### Parameters {#pupilsfieldsget-parameters}

- `<action>`: Action context (optional; e.g. "add" or "edit")

#### Response {#pupilsfieldsget-response}

Data attribute maps field names to their descriptions.

### Pupils/pupil:patch

Updates an existing pupil record.

#### Request {#pupilspupilpatch-request}

```
PATCH /api/pupils/pupil/<pupil>
```

#### Parameters {#pupilspupilpatch-parameters}

- `<pupil>`: ADAM internal pupil identifier (URL path parameter)
- JSON request body containing fields to update

#### Response {#pupilspupilpatch-response}

- Code 200: Returns the updated pupil record (includes pupil_gender as name and pupil_grade)
- Code 400: Validation error
- Code 404: Pupil not found

### Pupils/contactlist:get

Returns contact details for all pupils.

#### Request {#pupilscontactlistget-request}

```
GET /api/pupils/contactlist
```

#### Parameters {#pupilscontactlistget-parameters}

None.

#### Response {#pupilscontactlistget-response}

```json
{
  "data": [
    {
      "id": 1234,
      "firstname": "John",
      "lastname": "Smith",
      "cell": "0821234567",
      "email": "john@example.com",
      "grade": "Grade 10"
    }
  ]
}
```

### Pupils/search-id:get

Searches for pupils by ID number. Alias: pupils/searchbyid (note: this is a different endpoint from the documented Pupils/searchbyid which searches by admin number — verify the documented version is correct).

#### Request {#pupilssearch-idget-request}

```
GET /api/pupils/search-id/<idNumber>
```

#### Parameters {#pupilssearch-idget-parameters}

- `<idNumber>`: ID number to search for (required)

#### Response {#pupilssearch-idget-response}

- Code 200: Array of matching pupil IDs
- Code 400: Empty idNumber parameter
- Code 404: No pupils found
