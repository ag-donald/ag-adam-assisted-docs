---
api_prefixes:
  - calendar
---

# Calendar

Use these endpoints to get the calendar subscription links for current pupils and current staff.

All endpoints on this page are under `/api/calendar/`.

See [Authentication](api-access-to-adam.md#authentication) for how to send your API token.

### Calendar/pupillinks:get

This provides calendar subscription links for all current pupils. API keys are generated automatically for pupils who
don't have one yet.

#### Request {#calendarpupillinksget-request}

```
GET /api/calendar/pupillinks/
```

#### Parameters {#calendarpupillinksget-parameters}

None required.

#### Response {#calendarpupillinksget-response}

```
GET /api/calendar/pupillinks/
```

```json
{
    "data": [
        {
            "pupil_id": 142,
            "calendar_link": "webcal://adam.example.com/api/calendar/xK9mNp2qRs5tUv8wXy1zA4bCdEfGhIjKlMnOpQrStUvWxYz012"
        }
    ],
    "message": "",
    "response": {
        "error": false,
        "code": 200
    }
}
```

### Calendar/stafflinks:get

This provides calendar subscription links for all current staff. API keys are generated automatically for staff who don't have one yet.

#### Request {#calendarstafflinksget-request}

```
GET /api/calendar/stafflinks/
```

#### Parameters {#calendarstafflinksget-parameters}

None required.

#### Response {#calendarstafflinksget-response}

```
GET /api/calendar/stafflinks/
```

```json
{
    "data": [
        {
            "staff_id": 3,
            "calendar_link": "webcal://adam.example.com/api/calendar/gMSrVY4iGLAdk3RDks7AK3a2BTFW9PAGgpt9MgPDvVd6vBS7im"
        }
    ],
    "message": "",
    "response": {
        "error": false,
        "code": 200
    }
}
```
