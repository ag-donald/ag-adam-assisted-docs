---
api_prefixes:
  - dataquery
---

# Data Query

Use these endpoints to read the whole-school scratch list, which is the list you configure under **Administration → Security → Manage Data Query API Fields**.

All endpoints on this page are under `/api/dataquery/`.

See [Authentication](api-access-to-adam.md#authentication) for how to send your API token.

### DataQuery/get:get

Provides automated access to a whole-school scratch list. The contents of the scratch list fields can be customised as per the settings in ADAM found at **Administration → Security → Manage Data Query API Fields**.

Please treat this feature with the utmost care. By its very definition, it gives wide access to a range of personal data.

#### Create a Data Query Secret

To use this API endpoint, an additional data query token must be defined.

![](assets/screenshots/api-access-to-adam/api-access-to-adam-03.png)

Note that field access definitions can only be linked to a single API Token. If multiple API tokens require access to the same fields, this process must be duplicated for each API token and a unique list created for each.

-   Select the **API Token** that you want to associate with this query. *Note that only API Tokens who have access to the* *DataQuery/get/get* *resource may be selected here.*
-   Make a note of the **Secret** and do not share this with unauthorised personnel.
-   Choose a **data source** for the query. Once set here, this cannot be changed later.
-   Add a **comment** to provide insight into the function and reason for this query.

Click on **Add record** when done.

A second screen will show, allowing you to select the fields required for this query:

![](assets/screenshots/api-access-to-adam/api-access-to-adam-04.png)

Check the fields that you require and **save** your selections using the button at the bottom.

#### Request {#dataquerygetget-request}

```
GET /api/dataquery/get/<secret>
```

OR, for a modified data structure to provide more consistency for automated systems, (see example response below), add the version parameter “2” to the end of the request.

```
GET /api/dataquery/get/<secret>/2
```

#### Parameters {#dataquerygetget-parameters}

-   `<secret>` is a series of random characters as [created above](#create-a-data-query-secret).

#### Response {#dataquerygetget-response}

```
GET /api/dataquery/get/GXiE4V5qYB
```

```json
{
    "data": {
        "49": {
            "admin_number_1": "3316",
            "lurits_number_177": "",
            "age_6": "15 years, 200 days",
            "gender_10": "Male"
        },
        "4688": {
            "admin_number_1": "6333",
            "lurits_number_177": "",
            "age_6": "17 years, 10 days",
            "gender_10": "Male"
        }
    },
    "message": "",
    "response": {
        "error": "OK",
        "code": 200
    }
}
```

The `data` attribute is a JSON object with zero or more attributes, each being the ID of the relevant data object as specified in the Data Query setup. Each of these objects will have a number of attributes depending on the fields chosen. 

> [!WARNING]
> Note that the names of these attributes **can** be overridden by the school. However, there is a unique numeric identifier that is appended to each which will remain constant. Logic should be based around that identifier. 

Note that custom fields will contain the word “custom” before the unique identifier and so that should also be checked for.

```
GET /api/dataquery/get/GXiE4V5qYB/2
```

Where the optional parameter “2” is included at the end, the structure of the returned data will change. An additional “fields” property is included with clearer textual descriptions of the fields. The fields in each of the data objects is identified by the immutable identifier. This allows automated systems to ignore parts of the field name that might change.

```json
{
    "fields": [
        {
           "id": 1,
           "name": "Admin Number"
        },
        {
           "id": 177,
           "name": "LURITS Number"
        },
        {
           "id": 6,
           "name": "Age"
        },
        {
           "id": 10,
           "name": "Gender"
        }  
    ],
    "data": {
        "49": {
            "1": "3316",
            "177": "",
            "6": "15 years, 200 days",
            "10": "Male"
        },
        "4688": {
            "1": "6333",
            "177": "",
            "6": "17 years, 10 days",
            "10": "Male"
        }
    },
    "message": "",
    "response": {
        "error": "OK",
        "code": 200
    }
}
```

### DataQuery/getsince:get

See above.

#### Request {#dataquerygetsinceget-request}

```
GET /api/dataquery/getsince/<secret>/<timestamp>[/<version>]
```

#### Parameters {#dataquerygetsinceget-parameters}

-   `<secret>` is the secret defined for a list. This also determines what type of data and which fields are returned.
-   `<timestamp>` is a [Unix integer timestamp](https://en.wikipedia.org/wiki/Unix_time) - the number of non-leap seconds since 1 January 1970, 00:00:00 UTC. See also [Unix Timestamp - Epoch Converter](https://www.unixtimestamp.com/).
-   `<version>` , if supplied, is the version of the data structure to be returned. See above.

#### Response {#dataquerygetsinceget-response}

See above.

### DataQuery/getone:get

See above.

#### Request {#dataquerygetoneget-request}

```
GET /api/dataquery/getone/<secret>/<identifier>[/<version>]
```

#### Parameters {#dataquerygetoneget-parameters}

-   `<secret>` is the secret defined for a list. This also determines what type of data and which fields are returned.
-   `<identifier>` is the identifier of the dataobject to be returned.
-   `<version>`, if supplied, is the version of the data structure to be returned. See above.

#### Response {#dataquerygetoneget-response}

See above.
