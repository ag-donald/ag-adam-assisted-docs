---
api_prefixes:
  - messaginglogs
---

# Messaging Logs

Use these endpoints to read the messages ADAM has delivered to a family or pupil, including attachments.

All endpoints on this page are under `/api/messaginglogs/`.

See [Authentication](api-access-to-adam.md#authentication) for how to send your API token.

### MessagingLogs/messages:get

Returns 20 delivered messages for a family or pupil, paginated.

#### Request {#messaginglogsmessagesget-request}

```
GET /api/messaginglogs/messages/<type>/<id>[/<start>]
```

#### Parameters {#messaginglogsmessagesget-parameters}

- `<type>`: family or pupil (required)
- `<id>`: Family or pupil identifier (required)
- `<start>`: Pagination offset (optional; defaults to 0). Returns 20 messages per page.

#### Response {#messaginglogsmessagesget-response}

Data attribute contains an array of delivered message summaries.

### MessagingLogs/message:get

Returns a single message's details.

#### Request {#messaginglogsmessageget-request}

```
GET /api/messaginglogs/message/<type>/<id>/<messageId>
```

#### Parameters {#messaginglogsmessageget-parameters}

- `<type>`: family, pupil, or staff (required)
- `<id>`: Identifier for the family, pupil, or staff member (required)
- `<messageId>`: Message identifier (required)

#### Response {#messaginglogsmessageget-response}

Data attribute contains the full message details.

### MessagingLogs/messagebyid:get

Returns a message by its ID, including attachments.

#### Request {#messaginglogsmessagebyidget-request}

```
GET /api/messaginglogs/messagebyid/<messageId>
```

#### Parameters {#messaginglogsmessagebyidget-parameters}

- `<messageId>`: Message identifier (required)

#### Response {#messaginglogsmessagebyidget-response}

Data attribute contains the message with an attachments array:

```json
{
  "data": {
    "message_id": 42,
    "subject": "Newsletter",
    "body": "...",
    "attachments": [
      { "link": "/path/to/file", "location": "docrep", "name": "Newsletter.pdf" }
    ]
  }
}
```

#### Permissions

Requires one of: messagelog_staff_view, messagelog_family_view, messagelog_pupil_view (staff tokens); or viewmessagelog_family, viewmessagelog_pupil (family/pupil tokens).
