---
api_prefixes:
  - psychometric
---

# Psychometric

Use these endpoints to list the active psychometric assessments in a category. The two endpoints on this page are equivalent: the second is another name for the first.

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

### Psychometric/assessments_by_category:get

This endpoint is equivalent to [Psychometric/assessmentsbycategory:get](#psychometricassessmentsbycategoryget). It takes the same parameters and returns the same response.

#### Request {#psychometricassessments_by_categoryget-request}

```
GET /api/psychometric/assessments_by_category/<category>
```
