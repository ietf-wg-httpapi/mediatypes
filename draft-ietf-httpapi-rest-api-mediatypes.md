---
title: REST API Media Types
abbrev:
docname: draft-ietf-httpapi-rest-api-mediatypes-latest
category: info

ipr: trust200902
area: Applications and Real-Time
workgroup: HTTPAPI
keyword: Internet-Draft

stand_alone: yes
pi: [toc, tocindent, sortrefs, symrefs, strict, compact, comments, inline, docmapping]

venue:
  group: HTTPAPI
  type: Working Group
  home: https://datatracker.ietf.org/wg/httpapi/about/
  mail: httpapi@ietf.org
  arch: https://mailarchive.ietf.org/arch/browse/httpapi/
  repo: https://github.com/ietf-wg-httpapi/mediatypes/labels/rest-api
github-issue-label: rest-api

author:
 -
    ins: R. Polli
    name: Roberto Polli
    org: Par-Tec
    email: robipolli@gmail.com
    country: Italy

normative:
  HTTP: RFC9110
  JSON: RFC8259
  MEDIATYPE: RFC6838
  YAML:
    title: YAML Ain't Markup Language Version 1.2
    date: 2021-10-01
    author:
    - ins: Oren Ben-Kiki
    - ins: Clark Evans
    - ins: Ingy dot Net
    target: https://yaml.org/spec/1.2/spec.html
  OAS:
    title: OpenAPI Specification 3.1.0
    date: 2021-02-15
    target: https://spec.openapis.org/oas/latest
    author:
    - ins: Darrel Miller
    - ins: Jeremy Whitlock
    - ins: Marsh Gardiner
    - ins: Mike Ralphson
    - ins: Ron Ratovsky
    - ins: Uri Sarid
  jsonschema:
    title: JSON Schema
    date: 2020-01-28
    target: "https://json-schema.org/specification.html"
    author:
    - ins: A. Wright
    - ins: H. Andrews
    - ins: B. Hutton
    - ins: G. Dennis

informative:

--- abstract

This document registers
the following media types used in APIs
on the IANA Media Types registry:
application/openapi+json,
and application/openapi+yaml.

--- middle

# Introduction

OpenAPI Specification [OAS]
is a consolidated standard for describing
HTTP APIs using the JSON {{JSON}} and YAML [YAML] data format.

To increase interoperability
and leverage content negotiation mechanisms when exchanging
API descriptions
this specification registers the following media types:
`application/openapi+json`
and `application/openapi+yaml`.

## Notational Conventions

{::boilerplate bcp14+}

The terms  "content", "content negotiation", "resource",
and "user agent"
in this document are to be interpreted as in {{HTTP}}.

# Media Type registrations

This section describes the information required for IANA to register
the above media types per {{MEDIATYPE}}.

## The OpenAPI Media Types

The OpenAPI Specification Media Types convey semantics for OpenAPI resources
as defined in [OAS].

Those resources can be represented in {{JSON}} or [YAML].
Since there are multiple OpenAPI Specification versions,
those media types support the `version` parameter.

The following example conveys the desire of a client
to receive an OpenAPI Specification resource based on the stated
preferences:

1. openapi 3.1 in YAML
2. openapi 3.0 in YAML
3. any openapi version in JSON

~~~ example

Accept: application/openapi+yaml;version=3.1,
        application/openapi+yaml;version=3.0;q=0.5,
        application/openapi+json;q=0.3
~~~

### Media Type application/openapi+json {#openapi-json}

The following information serves as the registration form for the `application/openapi+json` media type.

Type name:
: application

Subtype name:
: openapi+json

Required parameters:
: None

Optional parameters:
: version: its value is a string representing
  the OpenAPI Specification version.
  ;  unrecognized parameters should be ignored

Encoding considerations:
: Same as "application/json"

Security considerations:
: See {{sec}} of this document, "application/json" and [OAS]

Interoperability considerations:
: See {{int}} of this document, "application/json" and [OAS]

Published specification:
: this document, [OAS]

Applications that use this media type:
: HTTP

Fragment identifier considerations:
: [OAS] or the specific version
  of the OpenAPI document.

Additional information:

- Deprecated alias names for this type:  "application/vnd.oai.openapi+json". This name is used, but not registered.

- Magic number(s):  N/A

- File extension(s):  json

- Macintosh file type code(s):  N/A

Person and email address to contact for further information:
: See Authors' Addresses section.

Intended usage:
: COMMON

Restrictions on usage:
: None.

Author:
: See Authors' Addresses section.

Change controller:
: IETF

### Media Type application/openapi+yaml {#openapi-yaml}

The following information serves as the registration form for the `application/openapi+yaml` media type.

Type name:
: application

Subtype name:
: openapi+yaml

Required parameters:
: N/A

Optional parameters:
: version: its value is a string representing
  the OpenAPI Specification version.
  ; unrecognized parameters should be ignored

Encoding considerations:
: Same as "+yaml" Structured Syntax Suffix

Security considerations:
: See {{sec}} of this document, "+yaml" Structured Syntax Suffix and [OAS]

Interoperability considerations:
: See {{int}} of this document, "+yaml" Structured Syntax Suffix and [OAS]

Published specification:
: [OAS]

Applications that use this media type:
: HTTP

Fragment identifier considerations:
: [OAS] or the specific version
  of the OpenAPI document.

Additional information:

- Deprecated alias names for this type: "application/vnd.oai.openapi". This name is used, but not registered.

- Magic number(s):  N/A

- File extension(s): Same as "application/yaml"

- Macintosh file type code(s):  N/A

Person and email address to contact for further information:
: See Authors' Addresses section

Intended usage:
:  COMMON

Restrictions on usage:
:  None.

Author:
:  See Authors' Addresses section

Change controller:
:  IETF


# Interoperability Considerations {#int}

Interoperability requirements for media type
registrations are discussed in Section 4.6 of {{!MEDIATYPE=RFC6838}}
and in the Interoperability Considerations of the "+yaml" Structured Syntax Suffix.

## Using the version parameter

The `version` parameter ought to be processed
according with the associated OpenAPI Specification.

For example, when an OpenAPI 3.1 resource
uses the patch version `version=3.1.1`,
its value is expected to be ignored
by tooling
(see https://spec.openapis.org/oas/v3.1.0.html#versions).

While it is possible to use the version parameter
to identify OpenAPI resources prior to version 3.0,
the terminology used in this document
was formally introduced in OAS 3.0.4 and OAS 3.1.1.

# Security Considerations {#sec}

Security requirements for media type
registrations are discussed in Section 4.6 of {{!MEDIATYPE=RFC6838}}.
and in the Security Considerations of the "+yaml" Structured Syntax Suffix.

## General Considerations

OpenAPI documents are processed by a wide variety of tooling for numerous different purposes,
such as client code generation, documentation generation, server side routing, and API testing.
OpenAPI document authors must consider the risks of the scenarios where the OpenAPI document may be used.

An OpenAPI document describes the security schemes used to protect the resources it defines.
The security schemes available offer varying degrees of protection.
Factors such as the sensitivity of the data and the potential impact of a security breach should guide the selection of security schemes for the API resources.
Some security schemes, such as basic auth and OAuth Implicit flow, are supported for compatibility with existing APIs.
However, their inclusion in OpenAPI does not constitute an endorsement of their use,
particularly for highly sensitive data or operations.

OpenAPI documents may contain references to external resources that may be dereferenced automatically by consuming tools.
External resources may be hosted on different domains that may be untrusted.
References in an OpenAPI document, or across OpenAPI documents may cause a cycle.
Tooling must detect and handle cycles to prevent resource exhaustion.

Certain properties allow the use of Markdown which can contain HTML including script.
It is the responsibility of tooling to appropriately sanitize the Markdown.

OpenAPI documents use [jsonschema] therefore share the security consideration of JSON Schema.

# IANA Considerations

This specification defines the following new Internet media types {{MEDIATYPE}}.

IANA is asked to update the "Media Types" registry at <https://www.iana.org/assignments/media-types>
with the registration information provided in the sections below.

|--------------------------------------|---------------------------------------------|
| Media Type                           | Registration information section            |
|--------------------------------------|---------------------------------------------|
| application/openapi+json             | {{openapi-json}} of this document           |
| application/openapi+yaml             | {{openapi-yaml}} of this document           |
|--------------------------------------|---------------------------------------------|

--- back

# Acknowledgements
{: numbered="false"}

Thanks to Erik Wilde and David Biesack for being the initial contributors of this specification,
and to Darrel Miller and Rich Salz for their support during the adoption phase.

In addition to the people above, this document owes a lot to the extensive discussion inside
and outside the HTTPAPI workgroup.
The following contributors have helped improve this specification by
opening pull requests, reporting bugs, asking smart questions,
drafting or reviewing text, and evaluating open issues:

Austin Wright,
Ben Hutton
and Jason Desrosiers.

# FAQ
{: numbered="false" removeinrfc="true"}

Q: Why this document?
:  After all these years, we still lack a proper media type for REST related document types.
   This has some security implications too
   (eg. wrt on identifying parsers or treat downloads)

# Examples of content negotiation
{: numbered="false" removeinrfc="true"}

This section explores the possibilities for User Agents
to retrieve information about API specifications
using their preferred version of OpenAPI.

Note:

- for readability, we use only YAML serialization;
- we use the fictiotius media type `application/whatever+yaml`
  to represent definitions
  that are not associated with any specific registered media type;
- this does not specify nor mandate a specific server behavior;
  the various ecosystems are free to implement a more specific
  behavior. See {{?RFC9205}}.

An API catalog exposes API specifications using OAS 3.0,
and it wants to provide migration/upgrade capabilities
to future versions of OAS and of the referenced resources.

Github publishes OpenAPI specification files.

Resource: https://example.org/openapi.yaml
: is an OpenAPI Specification document
  that references the Foo schema located at /foo.yaml.

The following representation is used
both when the User Agent requests OAS 3.0
and as a default representation
(see {{Section 15.5.7 of HTTP}}).
For example, this is the response
returned when the User Agent requests
OAS 3.1.

~~~ http
HTTP/1.1 200 OK
Content-Location: openapi.yaml
Content-Type: application/openapi+yaml; version=3.0

openapi: 3.0.4
…
components:
  schemas:
    Foo:
      "$ref": "/foo.yaml"
~~~

The following representation is used
when the User Agent requests OAS 3.2.

~~~ http
HTTP/1.1 200 OK
Content-Location: openapi.yaml
Content-Type: application/openapi+yaml; version=3.2

openapi: 3.2.1
"$self": https://example.com/openapi.yaml
…
components:
  schemas:
    Foo:
      "$ref": /foo.yaml
~~~

Resource: https://example.org/foo.yaml
: is the schema definition for Foo,
  represented in two different ways
  depending on the OpenAPI version requested.

~~~ http
HTTP/1.1 200 OK
Content-Location: foo.yaml
Content-Type: application/whatever+yaml

type: string
enum: [ it, en]
~~~

Since OAS 3.2 supports JSON Schema,
the same syntax can be described
adding a `title` to each enum value.

~~~ http
HTTP/1.1 200 OK
Content-Location: foo.yaml
Content-Type: application/whatever+yaml; version=https://json-schema.org/draft/2020-12/schema

"$schema": "https://json-schema.org/draft/2020-12/schema"
"$id": "https://example.com/foo.yaml"
oneOf:
- const: it
  title: Italian
- const: en
  title: English
~~~

## User Agent wants only OAS3.1, gets 406
{: numbered="false" removeinrfc="true"}

The User Agent wants OAS3.1,
and is not willing to accept other versions
(see {{Section 12.4.3 of HTTP}}.

~~~ http
GET /openapi.yaml HTTP/1.1
Host: example.com
Accept: \
  application/openapi+yaml; version=3.1,
  */*; q=0
~~~

The server does not have
the selected representation
and responds with a 406 Not Acceptable.

~~~ http
HTTP/1.1 406 Not Acceptable
Accept: \
  application/openapi+yaml; version=3.0, \
  application/openapi+yaml; version=3.2
~~~

## User Agent prefers OAS3.1, gets OAS3.0
{: numbered="false" removeinrfc="true"}

The User Agent prefers OAS3.1,
and does not impose further constraints.

~~~ http
GET /openapi.yaml HTTP/1.1
Host: example.com
Accept: application/openapi+yaml; version=3.1
~~~

The server responds with the default representation.

~~~ http
HTTP/1.1 200 OK
Content-Type: application/openapi+yaml; version=3.0

openapi: 3.0.4
…
components:
  schemas:
    Foo:
      "$ref": /foo.yaml
~~~

## User Agent requires OAS3.0 for entry document and compatible referenced resources
{: numbered="false" removeinrfc="true"}

The User Agent only supports OAS3.0 entry documents.

~~~ http
GET /openapi.yaml HTTP/1.1
Host: example.com
Accept: \
  application/openapi+yaml; version=3.0;q=1, \
  */*; q=0
~~~

The server responds with the desired resource.

~~~ http
HTTP/1.1 200 OK
Content-Type: application/openapi+yaml; version=3.0

openapi: 3.0.4
…
components:
  schemas:
    Foo:
      "$ref": /foo.yaml
~~~

The User Agent processes the content
and to resolve the `$ref`, requests /foo.yaml.
Since it is not an entry document,
the User Agent is willing to accept
any content compatible with OAS3.0.

~~~ http
GET /foo.yaml HTTP/1.1
Host: example.com
Accept: \
  application/openapi+yaml; version=3.0; q=1, \
  application/yaml; q=0.5
~~~

The server responds with a YAML serialized content
that is compatible with OAS3.0.
Since the content only contains a Schema Object,
that is not associated with any media type,
the server uses the `application/yaml` media type.

~~~ http
HTTP/1.1 200 OK
Content-Type: application/yaml

type: string
enum: [it, en]
~~~

Q: Could the server respond with the same content
    using the `application/whatever+yaml` media type?

## User Agent prefers OAS3.2, gets JSON Schema
{: numbered="false" removeinrfc="true"}

The User Agent prefers OAS3.2.

~~~ http
GET /openapi.yaml HTTP/1.1
Host: example.com
Accept: application/openapi+yaml; version=3.2
~~~

The server responds with the OAS3.2 document.

~~~ http
HTTP/1.1 200 OK
Content-Type: application/openapi+yaml; version=3.2

openapi: 3.0.4
…
components:
  schemas:
    Foo:
      "$ref": /foo.yaml
~~~

The User Agent then requests the /foo.yaml,
but it wants to retrieve a content with the most recent OAS version.

~~~ http
GET /foo.yaml HTTP/1.1
Host: example.com
Accept: application/openapi+yaml; version=3.2
~~~

The server processes the Accept header,
and it realizes that the User Agent
prefers an OAS3.2 compatible content.
It then choses the JSON Schema representation
and responds accordingly.

Since JSON Schema has no associated media type,
the server uses the `application/yaml` media type.

~~~ http
HTTP/1.1 200 OK
Content-Type: application/yaml

"$schema": "https://json-schema.org/draft/2020-12/schema"
"$id": "https://example.com/foo.yaml"
oneOf:
- const: it
  title: Italian
- const: en
  title: English
~~~

## User Agent prefers OAS3.2, Github responds with default representation
{: numbered="false" removeinrfc="true"}

In this scenario:

1. the User Agent express preference
   for referenced resources compatible with OAS3.2.
1. The server does not support strict content negotiation,
   and responds with the default representation;
1. the User Agent processes the content
   and retrieves the referenced resources.

See {{Section 12.1 of HTTP}}

> A user agent cannot rely on proactive negotiation preferences being consistently honored,
> since the origin server might not implement proactive negotiation for the requested resource
> or might decide that sending a response that doesn't conform to the user agent's preferences
> is better than sending a 406 (Not Acceptable) response.

~~~ http:

GET /OpenAPITools/openapi-generator-cli/refs/heads/master/examples/v3.0/petstore.yaml HTTP/1.1
Host: raw.githubusercontent.com
Accept: application/openapi+yaml; version=3.2
~~~

The server responds with the default representation.

~~~ http
HTTP/1.1 200 OK
Content-Type: text/plain; charset=utf-8

openapi: 3.0.0
info:
  title: Hotel Booker API
…
~~~


## User Agent negotiates for a non-OAS media type
{: numbered="false" removeinrfc="true"}

In this scenario:

1. the User Agent express preference
   for referenced resources compatible with OAS3.2.
1. The server enforces a strict content negotiation,
   and responds with a 406 Not Acceptable;
1. the User Agent will have to retry
   using one of the acceptable media types.

The User Agent prefers OAS3.2;
moreover uses the `q` parameter
to decline OAS3.0 documents.
If it weren't so, the server
could have responded with the older version
if the OAS3.2 document were not available.

~~~ http
GET /openapi.yaml HTTP/1.1
Host: example.com
Accept: application/openapi+yaml; version=3.2, application/openapi+yaml; version=3.0;q=0
~~~

The server responds with the OAS3.2 document.

~~~ http
HTTP/1.1 200 OK
Content-Type: application/openapi+yaml; version=3.2

openapi: 3.0.0
…
components:
  schemas:
    Foo:
      "$ref": /foo.yaml
~~~

The User Agent then requests the /foo.yaml,
but it wants to retrieve a content with the most recent OAS version.

~~~ http
GET /foo.yaml HTTP/1.1
Host: example.com
Accept: application/openapi+yaml; version=3.2
~~~

The server processes the Accept header,
and it realizes that foo.yaml is
a JSON Schema document and not an OpenAPI document.

It then replies with the acceptable content.

~~~ http
HTTP/1.1 406 Not Acceptable
Accept: \
  application/whatever+yaml; version=https://json-schema.org/draft/2020-12/schema, \
  application/whatever+yaml; version=https://spec.openapis.org/oas/v3.0.4#schema-object
~~~

The User Agent decides to retry the request
using one of the acceptable media types.
It could have also decided to give up.

~~~ http
GET /foo.yaml HTTP/1.1
Host: example.com
Accept: \
  application/whatever+yaml; version=https://json-schema.org/draft/2020-12/schema
~~~

Now the server can respond with the JSON Schema representation.

~~~ http
HTTP/1.1 200 OK
Content-Type: application/whatever+yaml; version=https://json-schema.org/draft/2020-12/schema

"$schema": "https://json-schema.org/draft/2020-12/schema"
"$id": "https://example.com/foo.yaml"
oneOf:
- const: it
  title: Italian
- const: en
  title: English
~~~

Pros:

- The returned content is exactly what the User Agent requested.

Cons:

- Two requests were needed to retrieve the resource.
- Some User Agents may not be able to handle
  the 406 Not Acceptable response and give up.
- Requires a specific Accept value for each possible referenced resource,
  which may be difficult to manage.


# Change Log
{: numbered="false" removeinrfc="true"}

RFC EDITOR PLEASE DELETE THIS SECTION.

## Since -00
{:numbered="false" removeinrfc="true"}

- Split YAML registrations in a separate I-D.

## Since -04
{:numbered="false" removeinrfc="true"}

- Split JSONSCHEMA registrations in a separate I-D.

## Since -07
{:numbered="false" removeinrfc="true"}

- Support OAS 2.0
