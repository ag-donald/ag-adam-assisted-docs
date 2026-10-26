---
api_prefixes:
  - psychometric
---

# Psychometric

Use this endpoint to list the active psychometric assessments in a category.

All endpoints on this page are under `/api/psychometric/`.

See [Authentication](api-access-to-adam.md#authentication) for how to send your API token.

### Psychometric/assessmentsbycategory:get

Returns active psychometric assessments for a category. Alias: psychometric/assessments_by_category.

#### Request {#psychometricassessmentsbycategoryget-request}

```
GET /api/psychometric/assessmentsbycategory/<category>
```

#### Parameters {#psychometricassessmentsbycategoryget-parameters}

- `<category>`: Psychometric category identifier (required)

#### Response {#psychometricassessmentsbycategoryget-response}

Data attribute contains an array of active assessment records (where assessment_disabled = 'No').
