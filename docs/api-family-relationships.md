---
api_prefixes:
  - familyrelationships
---

# Family Relationships

Use these endpoints to find the families linked to a pupil, or the current pupils linked to a family, with the relationship of each parent.

All endpoints on this page are under `/api/familyrelationships/`.

See [Authentication](api-access-to-adam.md#authentication) for how to send your API token.

### FamilyRelationships/family:get

Gets a list of *current* pupils linked to a family with their relationships descriptors for primary and secondary parents.

#### Request {#familyrelationshipsfamilyget-request}

```
GET /api/familyrelationships/family[/<family_id>]
```

#### Parameters {#familyrelationshipsfamilyget-parameters}

- `<family_id>`: The internal identifier for the family. If omitted, all families are returned.

#### Response {#familyrelationshipsfamilyget-response}

The **data** attribute contains an array of 0 or more objects.

- The **index** of each array object is the identifier of the pupil.
- A **primary** and **secondary** key contain the relationship between the primary or secondary family member and the pupil. Note that a relationship will be returned even in instances where there may not be a secondary family member. Other logic must determine whether to discard this value or not.

Possible values include:

- biological
- adoptive parent
- stepparent
- foster parent
- guardian
- sponsor
- relative
- Other

```
GET /api/familyrelationships/family/123
```

```json
{
  "data": [
    {
      "111": {
        "primary": "biological",
        "secondary": "step parent"
      },
      "321": {
        "primary": "step parent",
        "secondary": "biological"
      }
    }
  ],
  "message": "",
  "response": {
    "error": "OK",
    "code": 200
  }
}
```

### FamilyRelationships/pupil:get

Gets a list of families linked to a pupil with their relationships descriptors for primary and secondary parents.

#### Request {#familyrelationshipspupilget-request}

```
GET /api/familyrelationships/pupil[/<pupil_id>]
```

#### Parameters {#familyrelationshipspupilget-parameters}

- `<pupil_id>`: The internal identifier for the pupil. If omitted, all pupils are returned

#### Response {#familyrelationshipspupilget-response}

```
GET /api/familyrelationships/pupil/123
```

```json
{
  "data": {
    "111": {
      "primary": "biological",
      "secondary": "step parent"
    },
    "321": {
      "primary": "step parent",
      "secondary": "biological"
    }
  },
  "message": "",
  "response": {
    "error": "OK",
    "code": 200
  }
}
```

The **data** attribute contains an array of 0 or more objects.

- The **index** of each array object is the identifier of the family.
- A **primary** and **secondary** key contain the relationship between the primary or secondary family member and the pupil. Note that a relationship will be returned even in instances where there may not be a secondary family member. Other logic must determine whether to discard this value or not.

Possible values include:

- biological
- adoptive parent
- step parent
- foster parent
- guardian
- sponsor
- relative
- Other

```
GET /api/familyrelationships/pupil
```

```json
{
  "data": {
    "123": {
      "111": {
        "primary": "biological",
        "secondary": "step parent"
      },
      "321": {
        "primary": "step parent",
        "secondary": "biological"
      }
    },
    "456": {
      "111": {
        "primary": "step parent",
        "secondary": "biological"
      }
    }
  },
  "message": "",
  "response": {
    "error": "OK",
    "code": 200
  }
}
```
