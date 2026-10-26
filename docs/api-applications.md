---
api_prefixes:
  - applications
---

# Online Applications

Use these endpoints to find the fields on the online application form, submit an application, and start an application for a parent to finish. They also check whether an ID number belongs to an existing family login.

All endpoints on this page are under `/api/applications/`.

See [Authentication](api-access-to-adam.md#authentication) for how to send your API token.

### Applications/applicationformfields:get

The ability to see which fields are accepted as part of the application form. These fields can be customised by updating
the core and custom fields to change their availability in the application form.

#### Request {#applicationsapplicationformfieldsget-request}

```
GET /api/applications/applicationformfields
```

#### Parameters {#applicationsapplicationformfieldsget-parameters}

None

#### Response {#applicationsapplicationformfieldsget-response}

The output data will be a JSON object containing the fields that are accepted. Within the data property are two sub
arrays for families and pupils. These list the field names that are accepted.

**Example:**

```
GET https://demo.adam.co.za/api/applications/applicationformfields
```

```json
{
  "data": {
    "families": [
      "family_primary_idnum",
      "family_primary_lastname",
      "family_primary_firstname",
      "family_primary_fullfirst",
      "family_primary_title",
      "family_primary_initials",
      "family_primary_gender",
      "family_primary_birth",
      "family_primary_occupation",
      "family_primary_employer",
      "family_primary_workphone",
      "family_primary_cell",
      "family_primary_cell_sms",
      "family_primary_email",
      "family_secondary_idnum",
      "family_secondary_lastname",
      "family_secondary_firstname",
      "family_secondary_fullfirst",
      "family_secondary_title",
      "family_secondary_initials",
      "family_secondary_gender",
      "family_secondary_birth",
      "family_secondary_occupation",
      "family_secondary_employer",
      "family_secondary_workphone",
      "family_secondary_cell",
      "family_secondary_cell_sms",
      "family_secondary_email",
      "family_address_residential_1",
      "family_address_residential_2",
      "family_address_residential_suburb",
      "family_address_residential_city",
      "family_address_residential_province",
      "family_address_residential_code",
      "family_address_residential_country",
      "family_address_postal_1",
      "family_address_postal_2",
      "family_address_postal_suburb",
      "family_address_postal_city",
      "family_address_postal_province",
      "family_address_postal_code",
      "family_address_postal_country",
      "family_home_phone",
      "family_home_fax",
      "family_ice",
      "family_ice_number",
      "family_report_required"
    ],
    "pupils": [
      "pupil_lastname",
      "pupil_fullfirst",
      "pupil_firstname",
      "pupil_gender",
      "pupil_idnumber",
      "pupil_birth",
      "pupil_religion",
      "pupil_population_id",
      "pupil_language_id",
      "pupil_language_other",
      "pupil_teaching_language_id",
      "pupil_entry",
      "pupil_final",
      "pupil_email",
      "pupil_cell",
      "pupil_cell_sms",
      "pupil_allergies",
      "pupil_medaid_name",
      "pupil_medaid_number",
      "pupil_medaid_principal",
      "pupil_medaid_principal_id",
      "pupil_doctor",
      "pupil_doctor_phone",
      "pupil_orphan_status",
      "pupil_relationships",
      "pupil_atschool",
      "pupil_prevschool_firstprovince",
      "pupil_prepschool",
      "pupil_prevschool_country",
      "pupil_prevschool_formalgrr",
      "pupil_nationality",
      "pupil_studypermit_required",
      "pupil_studypermit",
      "custom_38",
      "custom_36"
    ]
  },
  "message": "",
  "response": {
    "error": "OK",
    "code": 200
  }
}
```

### Applications/apply:post

Submit an application to the site. Note that if the ID number submitted matches an existing parent, the child will
automatically be linked to that parent. Note that when applications are submitted through ADAM’s web interface, ADAM
automatically authenticates the parent to ensure that strange children are not linked to their profiles. Implicit in the
web application is the validation of the email address which is done as part of the application process. Applications
received via the API are not given such scrutiny and special care should be taken on the sending system to mitigate
against spam and fraudulent attempts at applications.

#### Request {#applicationsapplypost-request}

```
POST /api/applications/apply
```

#### Parameters {#applicationsapplypost-parameters}

None - data sent by message body.

#### Body

The body of the request should contain the data required for the application. The data should either be in JSON format,
or as an encoded query string (as is typical with normal form-submitted data).

Fields: The three fields, `idnumber`, `email`, and `phone`, may be duplicated within the parent information. It is not
necessary that they complete them twice, but it is necessary for the information to be submitted both with the family
and as separate information.

Note carefully the point about existing parents: *if their ID or passport numbers already exist in ADAM’s database, the
family information provided in the application will be silently discarded in favour of information already in the
database.* Thus having updated contact information provided in the email and phone fields is important. The silent
discarding is to ensure that malicious actors cannot update family information without their authorisation.

- `idnumber`: The South African ID or passport number of the parent making the submission. This is used to match against
  other families. If omitted, no linking will take place. If this value matched the value of an existing family, the
  pupil will automatically be linked to that family and the information provided in the family info will be lost.
- `email`: The email address to get in tough with the parents regarding the application.
- `phone`: The phone number to get in touch with the parents regarding the application.
- `application`: The body of the application. This contains:

    - `pupil`: An array of child information to be included on the application. Each element of the array is a sub-array
      of information for each child. A valid application must have at least one child and no more than 5 children.
    - `family`: An array of family fields to be included.
    - `email`: further details of the parents’ email addresses.

A minimum set of required fields is:

- Families:
    - Primary last name (`family_primary_lastname`)
    - Primary first name (`family_primary_firstname`)
    - Primary full first names, can duplicate `family_primary_firstname` if required  (`family_primary_fullfirst`)

- Pupils:
    - Last name (`pupil_lastname`)
    - Preferred name (`pupil_firstname`)
    - Full first name, can duplicate pupil_firstname if required (`pupil_fullfirst`)
    - Gender (`pupil_gender`)
    - Year of entry (`entry_year`) - note non-standard field naming
    - Month of entry (`entry_month`) - note non-standard field naming
    - Grade of entry (`entry_grade`) - note non-standard field naming. Note, integers accepted only. For grades prior to
      Grade 1, zero or negative grades: Grade R = 0, Grade RR = -1, Grade RRR = -2, etc.

##### Example (JSON):

```json
{
  "idnumber": "1234567890123",
  "email": "morticia@adam.co.za",
  "phone": "0834699569",
  "application": {
    "pupil": [
      {
        "pupil_lastname": "Addams",
        "pupil_firstname": "Wednesday",
        "pupil_fullfirst": "Wednesday Jane",
        "pupil_gender": "Female",
        "entry_year": "2019",
        "entry_month": "1",
        "entry_grade": "10",
        "relationship": [
          {
            "primary": "biological",
            "secondary": "step parent"
          }
        ]
      },
      {
        "pupil_lastname": "Addams",
        "pupil_firstname": "Pugsley",
        "pupil_fullfirst": "Pugsley Georgie",
        "pupil_gender": "Male",
        "entry_year": "2019",
        "entry_month": "1",
        "entry_grade": "8",
        "relationship": [
          {
            "primary": "step parent",
            "secondary": "biological"
          }
        ]
      }
    ],
    "family": {
      "family_primary_idnum": "1234567890123",
      "family_primary_lastname": "Addams",
      "family_primary_firstname": "Gomez",
      "family_primary_fullfirst": "Gomez",
      "family_secondary_idnum": "1234567890123",
      "family_secondary_lastname": "Addams",
      "family_secondary_firstname": "Morticia",
      "family_secondary_fullfirst": "Morticia May"
    },
    "email": [
      {
        "member": "primary",
        "address": "gomes@adam.co.za",
        "bulk": "Yes",
        "reports": "Yes"
      },
      {
        "member": "secondary",
        "address": "morticia@adam.co.za",
        "bulk": "Yes",
        "reports": "Yes"
      }
    ]
  }
}
```

#### Response {#applicationsapplypost-response}

A simple object providing notification of success or failure. The application field gives a code unique to this
application which will, in a future development, allow for editing of the application.

```json
{
  "data": {
    "application": "6ESKmQYMWH3KbJUdAESsZUi3BysaLx"
  },
  "message": "",
  "response": {
    "error": "OK",
    "code": 200
  }
}
```

### Applications/create:post

Creates a **partially completed application** and invites the parent to finish it themselves. This is intended for
authoritative external systems — for example an application-fee payment provider — that already hold verified
information about the parent and their children, and want that information to be carried into ADAM without the parent
being able to contradict it.

The difference between this resource and `Applications/apply:post` is important:

- `Applications/apply:post` submits a **finished** application. The application is completed immediately and appears in
  the list of applications awaiting approval.
- `Applications/create:post` creates an application that is **left open**. The supplied information is stored as
  *locked* data, an email containing a continuation link is sent to the parent, and the parent then completes the rest
  of the application form in ADAM in the normal way. Only once the parent submits it does it appear for approval.

Locked information survives everything the parent does to the form, and is written authoritatively onto the family and
pupil records when a member of staff approves the application.

#### Request {#applicationscreatepost-request}

```
POST /api/applications/create
```

#### Parameters {#applicationscreatepost-parameters}

None - data sent by message body.

#### Body

The body should either be in JSON format, or as an encoded query string (as is typical with normal form-submitted
data).

- `email`: The email address of the parent. The continuation link is sent to this address, so it must be a valid email
  address.
- `idnumber`: The South African ID or passport number of the parent making the application. Any non-empty identifier is
  accepted, since parents may apply with a passport number. If this matches an existing family in ADAM, the application
  is linked to that family.
- `phone`: The contact number for the parent.
- `children`: The number of children on the application. A valid application must have at least one child and no more
  than 5 children. This determines how many sets of pupil details the parent is asked to complete.
- `locked`: The information which the sending system is asserting. This contains:

    - `family`: An object of family field names and their values.
    - `pupil`: An array of objects of pupil field names and their values, one entry per child, numbered from zero. The
      array may be sparse: a child with nothing locked can be omitted or sent as `{}`.
    - `readonly`: The manifest of which of the locked fields the parent may not change.

        - `family`: A list of family field names.
        - `pupil`: An array, per child, of lists of pupil field names.

The field names accepted in the `family` and `pupil` objects are exactly those reported by
`Applications/applicationformfields:get`.

##### Read-only and editable locked fields

A locked field listed in `readonly` is presented to the parent as a field they can see but cannot change. A locked
field which is *not* listed in `readonly` is presented as an ordinary, editable field pre-filled with the supplied
value — but the value supplied by the sending system is still the one written to ADAM when the application is
approved. Use `readonly` where it would confuse a parent to be able to edit something (a payment reference, for
example) and leave a field editable where the parent’s own correction is helpful to see but should not overrule the
authoritative source.

##### Example (JSON):

```json
{
  "email": "morticia@adam.co.za",
  "idnumber": "1234567890123",
  "phone": "0834699569",
  "children": 2,
  "locked": {
    "family": {
      "family_primary_idnum": "1234567890123",
      "family_primary_lastname": "Addams"
    },
    "pupil": [
      {
        "pupil_lastname": "Addams",
        "custom_38": "INV-00417"
      },
      {
        "custom_38": "INV-00418"
      }
    ],
    "readonly": {
      "family": [
        "family_primary_idnum"
      ],
      "pupil": [
        [
          "custom_38"
        ],
        [
          "custom_38"
        ]
      ]
    }
  }
}
```

#### Response {#applicationscreatepost-response}

On success the data object contains two items:

- `application`: A code unique to this application, for the sending system’s own record keeping. It is not a
  credential and cannot be used to open the application form.
- `continue_url`: The same continuation link that has been emailed to the parent. A sending system can present this
  directly — as a “Continue your application” button after a payment, for instance — so that the parent does not have
  to wait for the email. The link expires after 7 days and may be used at most 20 times.

```json
{
  "data": {
    "application": "6ESKmQYMWH3KbJUdAESsZUi3BysaLx",
    "continue_url": "https://demo.adam.co.za/api/click/dHrLPUuoSHi0tbAkNsX2NwYtoxlLPqIYr8ozfQxWCcIS7uzUEq"
  },
  "message": "",
  "response": {
    "error": "OK",
    "code": 200
  }
}
```

The continuation link is the only credential that opens the application, and it is exactly the secret contained in the
parent’s email. It must be transmitted over HTTPS and must not be written to logs.

The email is sent whether or not the sending system uses `continue_url`.

#### Errors {#applicationscreatepost-errors}

Every failure is reported as `400 (Bad request)` and nothing is created — there are no half-made applications to clean
up. Where more than one thing is wrong, all of the messages are returned together in `response.error`.

- `Body of request not understood.` — the body was empty or could not be read.
- `A valid email address is required.`
- `A primary ID number is required.`
- `Invalid number of children; cannot continue.` — fewer than one, or more than five.
- `Unknown family fields: <list>` / `Unknown pupil fields (child <n>): <list>` — a field name that is not accepted on
  the application form.
- `Locked pupil index out of range: <n>` — locked information sent for a child beyond the number given in `children`.
- `Read-only family field has no value: <field>` / `Read-only pupil field has no value (child <n>): <field>` — a field
  was named as read-only but no value was supplied for it.
- `Primary id number mismatch between idnumber and locked family_primary_idnum.` — where `family_primary_idnum` is
  locked it must be identical to `idnumber`.

If the application cannot be written to the database, `500 (Internal server error)` is returned with the error
`Unable to create application.`

#### Existing families {#applicationscreatepost-existingfamilies}

If the ID number matches a family already in ADAM, the application is linked to that family and the parent is not asked
to complete the family section again. In that case locked **family** fields are stored but are not written to the
existing family record when the application is approved; this is the same protection that stops an application
overwriting an existing family’s details. Locked **pupil** fields are applied as normal. Sending systems whose locked
information is about the children — payment references and the like — are unaffected by this.

### Applications/verifyid:get

Checks whether an ID number is associated with an existing family login account.

#### Request {#applicationsverifyidget-request}

```
GET /api/applications/verifyid/<idNumber>
```

#### Parameters {#applicationsverifyidget-parameters}

- `<idNumber>`: South African ID number to look up (required)

#### Response {#applicationsverifyidget-response}

No data attribute. The `response.message` field indicates the result:

- "authorization required" — ID number found and a password exists (family can log in)
- "authorization not possible" — ID number found but no password set
- "id number not found" (code 404) — no matching record
