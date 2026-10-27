---
api_prefixes:
  - documents
---

# Documents

Use these endpoints to list, view, download, upload, update and delete documents stored in ADAM. A token can only reach the document categories it has permission for.

All endpoints on this page are under `/api/documents/`.

See [Authentication](api-access-to-adam.md#authentication) for how to send your API token.

### Documents/categories:get

Returns a list of document categories that the current API token has any permissions for, along with the permission flags for each.

#### Request {#documentscategoriesget-request}

```
GET /api/documents/categories
```

#### Parameters {#documentscategoriesget-parameters}

None.

#### Response {#documentscategoriesget-response}

The data attribute will be an array of zero or more JSON objects representing categories.

Example:

```
GET /api/documents/categories
```

```json
{
    "data": [
        {
            "category_id": 7,
            "category_name": "Photographs",
            "description": "Pupil photographs",
            "parent_id": 1,
            "permissions": {
                "read": true,
                "add": true,
                "delete": false
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

-   `category_id` is ADAM's internal identifier for the category.
-   `category_name` is the display name of the category.
-   `description` is the category's description text.
-   `parent_id` is the identifier of the parent category (top-level categories have a parent of 0).
-   `permissions` indicates which operations the token is allowed to perform on this category.

### Documents/list:get

Returns a list of documents for a given entity within a specific category.

#### Request {#documentslistget-request}

```
GET /api/documents/list/<categoryId>/<entityId>
```

#### Parameters {#documentslistget-parameters}

-   `categoryId`: The ADAM identifier of the document category.
-   `entityId`: The ADAM identifier of the entity (pupil, staff member, family, or site record).

#### Response {#documentslistget-response}

The data attribute will be an array of zero or more JSON objects representing documents. Requires **read** permission on the category.

Example:

```
GET /api/documents/list/108/4561
```

```json
{
    "data": [
        {
            "document_id": 12345,
            "name": "Birth Certificate",
            "filename": "birth_cert.pdf",
            "filetype": "application/pdf",
            "upload_date": "2025-03-15 10:30:00",
            "category_id": 108,
            "link": "a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6"
        }
    ],
    "message": "",
    "response": {
        "error": "OK",
        "code": 200
    }
}
```

-   `document_id` is ADAM's internal identifier for the document.
-   `name` is the descriptive name given to the document.
-   `filename` is the original filename of the uploaded file.
-   `filetype` is the MIME type of the document.
-   `upload_date` is the date and time the document was uploaded.
-   `category_id` is the category the document belongs to.
-   `link` is a unique random string identifier for the document.

### Documents/document:get

Returns detailed metadata for a single document, including its entity links.

#### Request {#documentsdocumentget-request}

```
GET /api/documents/document/<documentId>
```

#### Parameters {#documentsdocumentget-parameters}

-   `documentId`: The ADAM identifier of the document.

#### Response {#documentsdocumentget-response}

The data attribute will be a JSON object with document metadata and linked entities. Requires **read** permission on the document's category.

Example:

```
GET /api/documents/document/12345
```

```json
{
    "data": {
        "document_id": 12345,
        "name": "Birth Certificate",
        "notes": "",
        "filename": "birth_cert.pdf",
        "filetype": "application/pdf",
        "upload_date": "2025-03-15 10:30:00",
        "category_id": 108,
        "category_name": "Admin Documents",
        "link": "a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6",
        "links": [
            {
                "table": "pupils",
                "entity_id": 4561,
                "link_date": "2025-03-15 10:30:00"
            }
        ]
    },
    "message": "",
    "response": {
        "error": "OK",
        "code": 200
    }
}
```

- `notes` is any additional notes attached to the document.
- `category_name` is the display name of the document's category.
- `links` is an array of entity associations. Each link contains the entity `table` (pupils, staff, families, or site), the `entity_id`, and the `link_date`.

### Documents/download:get

Downloads the binary file content of a document.

#### Request {#documentsdownloadget-request}

```
GET /api/documents/download/<documentId>
```

#### Parameters {#documentsdownloadget-parameters}

- `documentId`: The ADAM identifier of the document.

#### Response {#documentsdownloadget-response}

Returns the raw binary file content with the appropriate Content-type header. Requires **read** permission on the document's category.

If the document is not found, a standard JSON error response is returned with code 404.

### Documents/upload:post

Uploads a new document and links it to an entity.

#### Request {#documentsuploadpost-request}

```
POST /api/documents/upload
```

The request body must be JSON with the following fields:

#### Parameters {#documentsuploadpost-parameters}

- `category` (required): The ADAM identifier of the target category.
- `entity_type` (required): The type of entity to link the document to. Must be one of: pupils, staff, families, site.
- `entity_id` (required): The ADAM identifier of the entity.
- `name` (required): A descriptive name for the document.
- `filename` (required): The filename (e.g. report.pdf).
- `file_data` (required): The file content encoded as a base64 string.
- `mimetype` (optional): The MIME type. If omitted, ADAM will attempt to detect it automatically.

#### Response {#documentsuploadpost-response}

Returns the new document's identifier. Requires **add** permission on the target category.

Example request body:

```json
{
  "category": 108,
  "entity_type": "pupils",
  "entity_id": 4561,
  "name": "Medical Certificate",
  "filename": "medical.pdf",
  "file_data": "JVBERi0xLjQK..."
}
```

Example response:

```json
{
  "data": {
    "document_id": 12346,
    "message": "Document uploaded successfully"
  },
  "message": "",
  "response": {
    "error": "OK",
    "code": 200
  }
}
```

### Documents/document:patch

Updates the metadata of an existing document. Can change the name, notes, or move the document to a different category.

#### Request {#documentsdocumentpatch-request}

```
PATCH /api/documents/document/<documentId>
```

The request body must be JSON with one or more of the following fields:

#### Parameters {#documentsdocumentpatch-parameters}

- `documentId` (URL): The ADAM identifier of the document.
- `name` (optional): New descriptive name for the document.
- `notes` (optional): New notes text for the document.
- `category` (optional): ADAM identifier of a category to move the document to. The token must also have **add** permission on the destination category.

#### Response {#documentsdocumentpatch-response}

Returns a success message. Requires **add** permission on the document's current category (and on the destination category if moving).

Example request body:

```json
{
  "name": "Updated Certificate",
  "notes": "Verified by admin"
}
```

Example response:

```json
{
  "data": {
    "message": "Document updated successfully"
  },
  "message": "",
  "response": {
    "error": "OK",
    "code": 200
  }
}
```

### Documents/document:delete

Permanently deletes a document and its file from the repository.

#### Request {#documentsdocumentdelete-request}

```
DELETE /api/documents/document/<documentId>
```

#### Parameters {#documentsdocumentdelete-parameters}

- `documentId`: The ADAM identifier of the document.

#### Response {#documentsdocumentdelete-response}

Returns a success message. Requires **delete** permission on the document's category.

Example:

```
DELETE /api/documents/document/12345
```

```json
{
  "data": {
    "message": "Document deleted successfully"
  },
  "message": "",
  "response": {
    "error": "OK",
    "code": 200
  }
}
```
