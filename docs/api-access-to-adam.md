# API Access to ADAM

## Introduction the ADAM API

An API allows for another computer program to connect to ADAM to either access data stored in its database or to make
changes to that data. ADAM makes use of a “RESTful” API and returns data mostly in JSON format.

### What is a RESTful system?

REST is a technique of communicating with an API which is very common amongst web-based applications - such as ADAM.
Other programs will make one of four types of web request depending on what they are hoping to do in the database, and
include the necessary information for ADAM. ADAM then responds to that request with the appropriate data or success
code.

### How does access control work?

Access to the ADAM database is controlled using a token system. These are essentially random passwords that are created
which are shared only with the other program that wishes to access the API. Because these tokens are really only meant
to be used by a computer, it is not important that they are memorable or easy to type. In fact, ADAM will generate a
random set of characters to be used as the API key and you are strongly encouraged to make use of the suggested token.

> [!WARNING]
> It is vitally important that the token is kept confidential between the person issuing it and the person using it.
> Anyone who knows the token will be able to access the API. Please read
> the [Best Practices](#best-practice-security-principals) section below for further information.

Each API token can be given access to one or more [API resources](#api-resources). Anyone who knows the API token can
access all the resources that have been allocated to that token.

API tokens can be revoked at any point and can have their resources changed and added to over time. A token can also be
**suspended** — temporarily blocked without deleting it — and later **reactivated**. Any changes you make to the token
and its API resource assignments will take place immediately.

## Managing API Tokens in ADAM

In ADAM: Navigate to **Administration → Security Administration → Manage API Tokens**.

A list of existing API tokens will be shown. Click on **Add new API Token** to begin the process of creating a new
Token.

![](assets/screenshots/api-access-to-adam/api-access-to-adam-01.png)

1. A random 30-character **token** will be generated. This should be left unmodified unless you have a very specific
   reason to do so. Once set, token values cannot be changed. If you need to change the token, you must delete the
   existing endpoint and create a new one.
2. Select the appropriate **resources** to allow the token to access. Hold down the “Ctrl” key on your keyboard to allow
   you to select multiple resources by then clicking on those resources while holding down that button.
3. Add **notes** if required. It is a good idea to make note of what service is making use of the API token.
4. Click on **Save Token**.

> [!WARNING]
> The random 30 character token must be kept secret since it will allow anyone who knows it access to the data stored in
> the ADAM database. It will need to be shared with the integration provider and great care should be taken with how they
> are provided the API key. We strongly recommend against sending this information via email or other unsecured means.

### Managing Existing Tokens

In the table of existing API tokens, each row has a **Status** column and an **Actions** column. The **Status** column
shows whether the token is currently **Active** or **Suspended**. In the **Actions** column you have the option to
**edit**, **delete**, **regenerate**, and — depending on the current status — **suspend** or **reactivate** the API
token.

**Edit** allows you to change the **Resources** and **Notes** associated with an endpoint, but does not allow you to
edit the Token.

**Regenerating** a token will create a new random value for the token but will keep your resources and notes the same.
If you do regenerate a token, please remember to update your external systems with the new token.

**Deleting** the token will remove it from the list and it will no longer be available for use. Systems that rely on the
resources will no longer have access to the data supplied by ADAM.

### Suspending and Reactivating Tokens

Suspending a token is a reversible alternative to deleting it. A suspended token is kept in the list, together with all
its resources and notes, but is rejected by the API until it is reactivated. This is useful when you need to stop a
service from accessing ADAM temporarily — for example while you investigate unexpected activity — without losing the
token and having to reconfigure the external system with a new one later.

![](assets/screenshots/api-access-to-adam/api-access-to-adam-05.png)

To suspend an active token, click **suspend** in the **Actions** column of that token’s row. You will be asked to
confirm with the message “Suspend API token? This immediately blocks all requests using this token.” Once confirmed,
the token’s **Status** changes to **Suspended** and ADAM shows the message “The API token has been suspended.”

A suspended token is clearly marked in the list, and its **Actions** column offers **reactivate** in place of
**suspend**.

![](assets/screenshots/api-access-to-adam/api-access-to-adam-06.png)

To bring a suspended token back into use, click **reactivate** in the **Actions** column of that token’s row. Its
**Status** returns to **Active** and ADAM shows the message “The API token has been reactivated.”

> [!NOTE]
> Suspending and reactivating a token both take effect immediately. Because the token value itself is unchanged, you
> do not need to update your external systems when you reactivate a token — it simply starts working again.

> [!WARNING]
> While a token is suspended, any request that uses it is refused as though the token had no access to the resource,
> and the calling system receives a “403 Forbidden” response. Make sure the service that relies on the token is
> prepared to handle being blocked before you suspend it.

The difference between the two ways of stopping a token is important:

- **Suspend** is temporary and fully reversible. The token, its resources and its notes are all kept, and access can be
  restored at any time by reactivating it.
- **Delete** is permanent and cannot be undone. The token is removed from the list entirely and cannot be recovered; a
  new token would have to be created and shared with the external system.

## Best Practice Security Principals

The following are provided as best practice guidelines for managing API tokens.

1. Treat API Tokens as **top secret**. Do not send them via email and do not publish them in a place where they could be
   accessed by unauthorised personnel. API access can expose sensitive data. Allowing an API token to fall into the
   wrong hands could expose personal information about the users of your system and this would be considered an offence
   under the “Protection of Personal Information Act” (POPIA). Access to such personal information could become a
   security and safety issue.
2. Each entity (e.g. a program that is accessing data from ADAM) should have its **own** token or tokens. Tokens should
   never be shared between entities. If another entity requires access to the same data, give it a new token. This
   allows you to revoke each token individually and stop one program from accessing the data without affecting any other
   programs.
3. Programmers integrating with the ADAM API should not, under any circumstances, include API tokens in their source
   code and should always fetch them from some form of access controlled data storage.

## API Interactions

### Authentication

All API requests should be authenticated using a Bearer Token.

**Example:**

Authenticating with the token value svyzBvkuuXLdJwV7YcdYsQFVX5ha54 would yield the following header:

```
Authorize: Bearer svyzBvkuuXLdJwV7YcdYsQFVX5ha54
```

ADAM also will accept a Basic Authorization header with an arbitrary username. Authenticating with the username apitoken
token value `svyzBvkuuXLdJwV7YcdYsQFVX5ha54` would yield the following header:

```
Authorize: Basic YXBpdG9rZW46c3Z5ekJ2a3V1WExkSndWN1ljZFlzUUZWWDVoYTU0
```

### API Requests

All API requests, as listed below, should be prefixed with the “api” folder to make the URL end-point:

```
https://*adam.example.com*/api/
```

The remainder of the URL generally consists of a module name, a data set and zero or more parameters. These should all
be in lower-case. For example:

```
https://demo.adam.co.za/api/request/test/parameter
```

Parameters should
be “[percent encoded](https://www.w3schools.com/tags/ref_urlencode.asp)”.
Spaces should be encoded as %20 and not as a “+”.

A `GET` request to this API end-point would require token access to the resource: request/test:get. Note that without
specifically assigned access, access to the resource - even this test resource - will be denied.

### API Responses

All responses will be returned within JSON objects. The basic structure of these objects is:

```json
{
  "data": null,
  "message": "",
  "response": {
    "error": "",
    "code": 200
  }
}
```

Any response which does not have these properties as listed above, MUST be treated as invalid.

The contents of the **data** attribute will depend on the API endpoint being interrogated.

The **message** attribute contains a human-readable message which, in most cases, describes the data set that has been
returned. This is intended for debugging and may change unpredictably with future versions of ADAM.

The **response code** should mirror the HTTP response code which will be descriptive of the success or failure of the
call. The **error** attribute will provide a human-readable description of the error. The error message is not intended
to be interpreted by machines.

## API Resources

The ADAM API is organised by module. Each page below documents the endpoints for one area of ADAM.

- [Absentees](api-absentees.md)
- [Assessment](api-assessment.md)
- [Calendar](api-calendar.md)
- [Classes](api-classes.md)
- [Data Query](api-data-query.md)
- [DevMan Export](api-devman-export.md)
- [Documents](api-documents.md)
- [Families](api-families.md)
- [Family Relationships](api-family-relationships.md)
- [Messaging Logs](api-messaging-logs.md)
- [Online Applications](api-applications.md)
- [Psychometric](api-psychometric.md)
- [Pupils](api-pupils.md)
- [Records and Points](api-records-and-points.md)
- [Registration](api-registration.md)
- [Reporting](api-reporting.md)
- [Subjects](api-subjects.md)
- [Other Endpoints](api-other-endpoints.md)

## Specific Integration Requirements

Please see the [Third Party Integration](third-party-integration.md#third-party-integration) section in this documentation.
