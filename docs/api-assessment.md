---
api_prefixes:
  - assessment
  - questions
---

# Assessment

Use these endpoints to retrieve a pupil's recent assessment results and a breakdown of those results by question.

All endpoints on this page are under one of these paths: `/api/assessment/`, `/api/questions/`.

See [Authentication](api-access-to-adam.md#authentication) for how to send your API token.

### Assessment/recentresults:get

Returns recent assessment results for a pupil.

#### Request {#assessmentrecentresultsget-request}

```
GET /api/assessment/recentresults/<pupil>
```

#### Parameters {#assessmentrecentresultsget-parameters}

- `<pupil>`: ADAM internal pupil identifier (required)

#### Response {#assessmentrecentresultsget-response}

Data attribute contains an array of assessment result objects:

```json
{
  "data": [
    {
      "assessment_id": 42,
      "assessment_period_id": 3,
      "assessment_description": "Term 1 Test",
      "assessment_date": "2026-03-15",
      "assessment_releasedate": "2026-03-20",
      "assessment_total": 100,
      "assessment_weighting": 1.0,
      "assessment_weighting_display": "10%",
      "result_total": 78,
      "result_comment": "",
      "class_grade_id": 10,
      "class_description": "10A",
      "subject_name": "Mathematics",
      "subject_short": "Maths"
    }
  ]
}
```

### Questions/questionbreakdown:get

Returns a per-question breakdown of a pupil's assessment results.

#### Request {#questionsquestionbreakdownget-request}

```
GET /api/questions/questionbreakdown/<pupil>/<assessment>
```

#### Parameters {#questionsquestionbreakdownget-parameters}

- `<pupil>`: ADAM internal pupil identifier (required)
- `<assessment>`: Assessment identifier (required)

#### Response {#questionsquestionbreakdownget-response}

Data attribute contains an array of question result objects:

```json
{
  "data": [
    {
      "question_description": "Algebra",
      "outcome_name": "Patterns and Algebra",
      "answer_total": 8.5,
      "answer_level": "B",
      "question_total": 10
    }
  ]
}
```
