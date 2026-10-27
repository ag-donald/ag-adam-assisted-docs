---
api_prefixes:
  - recordsandpoints
---

# Records and Points

Use these endpoints to read a pupil's Records and Points entries, either the most recent ones or all of them.

All endpoints on this page are under `/api/recordsandpoints/`.

See [Authentication](api-access-to-adam.md#authentication) for how to send your API token.

### RecordsAndPoints/recentpupilrecords:get

Returns the most recent Records and Points entries for a pupil.

#### Request {#recordsandpointsrecentpupilrecordsget-request}

```
GET /api/recordsandpoints/recentpupilrecords/<pupil>[/<number>]
```

#### Parameters {#recordsandpointsrecentpupilrecordsget-parameters}

- `<pupil>`: ADAM internal pupil identifier (required)
- `<number>`: Maximum number of records to return (optional; defaults to 10)

#### Response {#recordsandpointsrecentpupilrecordsget-response}

```json
{
  "data": [
    {
      "group_name": "Bad",
      "category_description": "Demerit",
      "discipline_date": "2026-04-01 08:30:00",
      "discipline_effective_date": "2026-04-01",
      "discipline_amount": 1,
      "discipline_notes": "Late to class",
      "option_description": null
    }
  ]
}
```

### RecordsAndPoints/pupilrecords:get

Returns all Records and Points entries for a pupil, grouped by category group and category.

#### Request {#recordsandpointspupilrecordsget-request}

```
GET /api/recordsandpoints/pupilrecords/<pupil>
```

#### Parameters {#recordsandpointspupilrecordsget-parameters}

- `<pupil>`: ADAM internal pupil identifier (required)

#### Response {#recordsandpointspupilrecordsget-response}

Data attribute is a nested structure grouped by discipline group, then by category, with all records within each category.

```json
{
  "data": {
    "1": {
      "group_name": "Bad",
      "discipline_categories": [
        {
          "category_description": "Demerit",
          "discipline_records": [
            {
              "discipline_date": "2026-04-01",
              "discipline_amount": 1,
              "discipline_notes": "Late to class"
            }
          ]
        }
      ]
    }
  }
}
```
