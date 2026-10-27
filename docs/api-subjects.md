---
api_prefixes:
  - subjects
---

# Subjects

Use these endpoints to list the subjects available for one grade or for several grades.

All endpoints on this page are under `/api/subjects/`.

See [Authentication](api-access-to-adam.md#authentication) for how to send your API token.

### Subjects/get_by_grades:get

Returns subjects available for one or more grades.

#### Request {#subjectsgetbygradesget-request}

```
GET /api/subjects/get_by_grades/<grades>
```

#### Parameters {#subjectsgetbygradesget-parameters}

- `<grades>`: Comma-separated list of grade identifiers (required)

#### Response {#subjectsgetbygradesget-response}

Data attribute contains an array of subjects valid for the specified grades that have active class registrations.

### Subjects/get_by_grade:get

Returns subjects available for a single grade.

#### Request {#subjectsgetbygradeget-request}

```
GET /api/subjects/get_by_grade/<grade>
```

#### Parameters {#subjectsgetbygradeget-parameters}

- `<grade>`: Grade identifier (required)

#### Response {#subjectsgetbygradeget-response}

Data attribute contains an array of subjects for the specified grade with active class registrations.
