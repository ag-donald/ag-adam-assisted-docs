# Trying the API on the Demo Site

The ADAM demonstration site, `https://demo.adam.co.za`, is where developers build and test an integration before a
school gives them a token for its own site. On the demo site you can create your own API token with one request, and
then create [Data Query](api-data-query.md#dataquerygetget) definitions for it. You do not need to log in.

The three addresses on this page work only on the demo site. On a school's site they answer `404 (Not Found)`. On a
school's site, the school creates the token for you (see [Managing API Tokens in ADAM](api-access-to-adam.md#managing-api-tokens-in-adam)).

## How the Demo Site Treats Your Token

You choose the token and the secrets yourself, so the values in your own configuration never have to change.

- **The demo site is reset every night.** The reset removes every token and every Data Query definition. Run your
  set-up requests again after the reset, or at the start of each test run. You can use the same token and secrets
  again.
- **A token is exactly 30 letters or digits** (`A`–`Z`, `a`–`z`, `0`–`9`). Tokens are case-sensitive:
  `abc…` and `ABC…` are different tokens.
- **A Data Query secret is exactly 10 letters or digits.** Secrets are case-sensitive too.
- **Sending the same token again updates it.** Its resources and notes are replaced, and the token is reactivated if
  someone suspended it.
- **Sending the same secret again with the same token and data source updates the definition.** Its fields and
  comment are replaced.
- **A secret belongs to the token that created it.** No other token can change it.
- **Other visitors share the demo's admin screens.** On the demo site, the API token and Data Query screens show only
  the first characters of each token and secret, so other visitors cannot copy yours. They can still delete your
  token. Deleting a token also deletes its Data Query definitions. If this happens, run your set-up requests again.
- **Each address allows 30 requests in 5 minutes** from each visitor. A setup takes only a few requests.

## The Three Requests

Every answer uses the usual JSON envelope (see [API Responses](api-access-to-adam.md#api-responses)). The HTTP status
is the same as `response.code`, and the reason for a refusal is in `response.error`.

### Create or Update a Token

```
PUT /api/demo/token
```

This request needs no `Authorization` header. The body is a JSON object:

```json
{
    "token": "Abcdefghijklmnopqrstuvwxyz0123",
    "resources": ["dataquery/get:get"],
    "notes": "Acme SIS nightly pupil sync"
}
```

| Property | Required | Notes |
|---|---|---|
| `token` | Yes | Exactly 30 letters or digits. |
| `resources` | Yes | A list of at least one API resource, such as `dataquery/get:get`. The names are the ones on the [API resource pages](api-access-to-adam.md#api-resources). Letter case does not matter. |
| `notes` | No | What the token is for. ADAM removes HTML tags and keeps the first 255 characters. |

ADAM answers `201` with the message `Token created.` when the token is new, and `200` with the message
`Token updated.` when the token already existed. `data` holds the token's `token_id` and the `resources` saved:

```json
{
    "data": {
        "token_id": 4,
        "resources": ["dataquery/get:get"]
    },
    "message": "Token created.",
    "response": {
        "error": "OK",
        "code": 201
    }
}
```

The token can now use every resource you listed, on the demo site, in the same way as a token a school creates.

### List the Fields of a Data Source

```
GET /api/demo/dataquery/fields?source=<source>
```

Send your token in the header `Authorization: Bearer <token>`. `<source>` is one of `staff`, `pupils`, `families`,
`applicants`, `applicant-families` or `past-pupils`. The `past-staff` data source is not supported.

`data` lists the fields that a definition for this source can include. Each field has an `id`, a `label` and a
`group`. Custom fields have identifiers such as `custom_4`, and their group is `Custom Fields`. This is an excerpt:

```json
{
    "data": [
        {
            "id": 1,
            "label": "Admin Number",
            "group": "Pupil Information"
        },
        {
            "id": 3,
            "label": "Preferred Name",
            "group": "Pupil Information"
        }
    ],
    "message": "",
    "response": {
        "error": "OK",
        "code": 200
    }
}
```

### Create or Update a Data Query Definition

```
PUT /api/demo/dataquery/<secret>
```

`<secret>` is the secret you choose: exactly 10 letters or digits. Send your token in the header
`Authorization: Bearer <token>`. The body is a JSON object:

```json
{
    "source": "pupils",
    "fields": [1, 3],
    "comment": "Acme SIS nightly pupil sync"
}
```

| Property | Required | Notes |
|---|---|---|
| `source` | Yes | The data source, as for the field list above. A secret keeps the source it was created with. |
| `fields` | Yes | A list of at least one field `id` from the field list for this source. |
| `comment` | No | What the definition is for. ADAM removes HTML tags and keeps the first 250 characters. |

ADAM answers `201` with the message `Definition created.` when the definition is new, and `200` with the message
`Definition updated.` when it already existed. `data` holds the `secret`, the `source` and the `fields` saved.

Read the data with [DataQuery/get:get](api-data-query.md#dataquerygetget), using the same secret and token. The token
needs the `dataquery/get:get` resource for this.

## Errors

| Status | Error | When |
|---|---|---|
| 400 | `The request body must be a JSON object.` | The body is missing, empty, not valid JSON, or a list. |
| 400 | `The token must be exactly 30 letters or digits.` | The `token` is missing, the wrong length, or has other characters. A newline at the end counts as a character. |
| 400 | `List at least one resource.` | `resources` is missing, empty or not a list. |
| 400 | `Unknown resources: … The data lists every valid resource.` | A resource name is not valid. `data.valid` lists every valid name. |
| 400 | `The notes must be text.` | `notes` is not a string. |
| 401 | `A valid API token is required.` | The `Authorization` header is missing, or the token is not 30 letters or digits, is unknown, or is suspended. |
| 400 | `The secret must be exactly 10 letters or digits.` | The secret in the address is not valid. A newline at the end counts as a character. |
| 400 | `Unknown data source. Use one of: staff, pupils, families, applicants, applicant-families, past-pupils.` | `source` is missing or not one of these. |
| 400 | `The past-staff data source is not yet supported.` | `source` is `past-staff`. |
| 400 | `List at least one field.` | `fields` is missing, empty or not a list. |
| 400 | `These fields are not available for pupils: …` | A field is not offered for the source. The error names the source. |
| 400 | `The comment must be text.` | `comment` is not a string. |
| 409 | `This secret is already in use.` | Another token holds the secret. |
| 409 | `This secret was created for the pupils data source. Choose a new secret to use a different one.` | Your token already has a definition with this secret, for a different source. The error names that source. |
| 404 | | The site is not the demo site. |
| 429 | | More than 30 requests to the address in 5 minutes. Wait a few minutes before you try again. |

A `409 This secret is already in use.` on a secret you know is yours means another token now holds it. This happens
when someone deletes your token and another visitor then uses your secret. The secret stays taken until the nightly
reset, so choose another secret.

## Example Script

This script sets up a token and a definition, and then reads the data. Run it after each nightly reset.

```bash
HOST=https://demo.adam.co.za
TOKEN=Abcdefghijklmnopqrstuvwxyz0123   # exactly 30 letters or digits
SECRET=Secret0001                      # exactly 10 letters or digits

# 1. Create the token (201 the first time, 200 after that)
curl -sX PUT "$HOST/api/demo/token" \
  -d '{"token":"'$TOKEN'","resources":["dataquery/get:get"],"notes":"curl check"}'

# 2. List the fields for pupils (200)
curl -sH "Authorization: Bearer $TOKEN" "$HOST/api/demo/dataquery/fields?source=pupils"

# 3. Create the definition with fields 1 and 3 (201 the first time, 200 after that)
curl -sX PUT -H "Authorization: Bearer $TOKEN" "$HOST/api/demo/dataquery/$SECRET" \
  -d '{"source":"pupils","fields":[1,3],"comment":"curl check"}'

# 4. Read the data (200)
curl -sH "Authorization: Bearer $TOKEN" "$HOST/api/dataquery/get/$SECRET"
```
