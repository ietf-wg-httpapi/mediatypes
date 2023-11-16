---
title: JSON Schema Media Types
abbrev:
docname: draft-ietf-httpapi-jsonschema-mediatypes-latest
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
    org: Digital Transformation Department, Italian Government
    email: robipolli@gmail.com
    country: Italy

normative:
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
    title: JSON Schema Core
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
application/schema+json,
and application/schema-instance+json,

--- middle

# Introduction

OpenAPI Specification [OAS] version 3 and above
is a consolidated standard for describing
HTTP APIs using the JSON {{!JSON=RFC8259}} and YAML [YAML] data format.

YAML media type registration is addressed in {{!YAML-MEDIATYPES=I-D.ietf-httpapi-yaml-mediatypes}},
which provides interoperability and security considerations.

OpenAPI media type registration is addressed in {{!OAS-MEDIATYPES=I-D.ietf-httpapi-rest-api-mediatypes}},
which provides interoperability and security considerations.

To increase interoperability when processing API specifications
and leverage content negotiation mechanisms when exchanging
OpenAPI Specification resources
this specification register the following media types:
`application/schema+json`,
and `application/schema-instance+json`,

## Notational Conventions

{::boilerplate bcp14+}

This document uses the Augmented BNF defined in {{!RFC5234}} and updated
by {{!RFC7405}}.

The terms  "content", "content negotiation", "resource",
and "user agent"
in this document are to be interpreted as in {{!HTTP=RFC9110}}.

# Media Type registrations

This section describes the information required to register
the above media types according to {{!MEDIATYPE=RFC6838}}.

## JSON Schema Media Types

JSON Schema is a declarative domain-specific language for validating and
annotating JSON documents (see {{jsonschema}}).

This document registers the media types associated with JSON Schema.

There are many dialects of JSON Schema in wide use today.
The JSON Schema maintainers have released several dialects
including draft-04, draft-07, and draft 2020-12.
There are also several third-party JSON Schema dialects in wide
use including the ones defined for use in [OAS] and MongoDB.

This specification defines little more than
how to identify the dialect
while leaving most of the semantics of the schema
up to the dialect to define.

Clients MUST use the following order of precedence for determining the dialect of a schema:

- the `$schema` keyword ({{schema-keyword}})
- the "schema" media type parameter ({{schema-parameter}})
- the context of the enclosing document. This applies only when a schema is
  embedded within a document. The enclosing document could be another schema in
  the case of a bundled schema or it could be another type of document that
  includes schemas such as an OpenAPI document.

If none of the above result in identifying the dialect,
client behavior is undefined.

### The "$schema" Keyword {#schema-keyword}

The `$schema` keyword is used as a JSON Schema dialect identifier.
The value of this keyword MUST be a URI {{!RFC3986}}.
This URI SHOULD identify a meta-schema
that can be used to validate that the schema is syntactically correct according
to the dialect the URI identifies.

The dialect SHOULD define where the `$schema` keyword is allowed and/or
recognized in a schema,
but it is RECOMMENDED that dialects do not allow the schema to change within the same Schema Resource.

### Identifying a Schema via a Media Type Parameter {#schema-parameter}

Media types MAY allow for a `schema` media type parameter, to support content
negotiation based on schema identifier (see  {{Section 12 of HTTP}}).
The `schema` media type parameter MUST be a URI-reference {{!RFC3986}}.

The `schema` parameter identifies a schema that provides semantic information
about the resource the media type represents. When using the
`application/schema+json` media type, the `schema` parameter identifies the
dialect of the schema the media type represents.

The `schema` URI is opaque and SHOULD NOT automatically be dereferenced. Since
`schema` doesn't necessarily point to a network location, the "describedby"
relation is used for linking to a downloadable schema.

The following is an example of content negotiation where a user agent can accept
two different versions of a "pet" resource. Each resource version is identified
by a unique JSON Schema.

Request:

~~~ http-message
NOTE: '\' line wrapping per RFC 8792

GET /pet/1234 HTTP/1.1
Host: foo.example
Accept: \
  application/schema-instance+json; schema="/schemas/v2/pet"; q=0.2, \
  application/schema-instance+json; schema="/schemas/v1/pet"; q=0.1
~~~

Response:

~~~ http-message
NOTE: '\' line wrapping per RFC 8792

HTTP/1.1 200 Ok
Content-Type: \
  application/schema-instance+json; schema="/schemas/v2/pet"

{
  "petId": "1234",
  "name": "Pluto",
  ...
}
~~~

In the following example, the user agent is able to accept two possible dialects
of JSON Schema and the server replies with the latest one.

Request:

~~~ http-message
NOTE: '\' line wrapping per RFC 8792

GET /schemas/v2/pet HTTP/1.1
Host: foo.example
Accept: application/schema+json; \
            schema="https://json-schema.org/draft/2020-12/schema", \
        application/schema+json; \
            schema="http://json-schema.org/draft-07/schema#"
~~~

Response:

~~~ http-message
NOTE: '\' line wrapping per RFC 8792

HTTP/1.1 200 OK
Content-Type: \
  application/schema+json; \
      schema="https://json-schema.org/draft/2020-12/schema"

{
  "$id": "https://json-schema.org/draft/2020-12/schema",
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  ...
}
~~~

### Linking to a Schema {#schema-linking}

It is RECOMMENDED that instances described by a schema provide a link to a
downloadable JSON Schema using the link relation `describedby`, as defined by
Linked Data Protocol 1.0, section 8.1 {{!W3C.REC-ldp-20150226}}.

In HTTP, such links can be attached to any response using the `Link` header field
{{!LINK=RFC8288}}.

~~~ http-message
Link: <https://example.com/my-hyper-schema#>; rel="describedby"
~~~

### Fragment Identifiers {#schema-fragment}

Two fragment identifier structures are supported: JSON Pointers and plain-names.

The use of JSON Pointers as URI fragment identifiers is described in
{{!JSON-POINTER=RFC6901}}.
Fragment identifiers that are empty or start with a `/`, MUST be
interpreted as JSON Pointer fragment identifiers.

Plain-name fragment identifiers reference locally named locations in the
document.
The dialect determines how plain-name identifiers map to locations
within the document.
All fragment identifiers that do not match the JSON Pointer
syntax MUST be interpreted as plain name fragment identifiers.

### Media Type application/schema+json {#schema-json}

The media type for JSON Schema documents is `application/schema+json`.
This schema can be an official dialect or a third-party dialect.

The following information serves as the registration form for the `application/schema+json` media type.

Type name:
: application

Subtype name:
: schema+json

Required parameters:
: N/A

Optional parameters:

- schema: A URI identifying the JSON Schema dialect the schema was written
  for. If this value conflicts with the value of the `$schema` keyword in the
  schema, the `$schema` keyword takes precedence.

Encoding considerations:
: Same as "application/json"

Security considerations:
: See the "Security Considerations" section of {{jsonschema}}

Interoperability considerations:
: See the "General Considerations" section of {{jsonschema}}

Published specification:
: this document

Applications that use this media type:
: JSON Schema is used in a variety of
  applications including API servers and clients that validate JSON requests and
  responses, IDEs that valid configuration files, databases that store JSON.

Fragment identifier considerations:
: See {{schema-fragment}}

Additional information:

- Deprecated alias names for this type: N/A

- Magic number(s): N/A

- File extension(s): json, schema.json

- Macintosh file type code(s): N/A

Person and email address to contact for further information:
: See Authors' Addresses section.

Intended usage:
: COMMON

Restrictions on usage:
: N/A.

Author:
: See Authors' Addresses section.

Change controller:
: N/A

### Media Type application/schema-instance+json {#schema-instance-json}

The `application/schema-instance+json` media type is an extension of the
{{JSON}} media type that just adds the `schema` media type parameter and
fragment identification.

The following information serves as the registration
form for the `application/schema-instance+json` media type.

Type name:
: application

Subtype name:
: schema-instance+json

Required parameters:
: N/A

Optional parameters:

- schema:
  : A URI identifying a JSON Schema that provides semantic information
    about this JSON representation.

Encoding considerations:
: Same as {{JSON}}

Security considerations:
: Same as {{JSON}}

Interoperability considerations:
: Same as {{JSON}}

Published specification:
: this document

Applications that use this media type:
: JSON Schema is used in a variety of
  applications including API servers and clients that validate JSON requests and
  responses, IDEs that valid configuration files, databases that store JSON, and
  more.

Fragment identifier considerations:
: See {{schema-fragment}}

Additional information:

- Deprecated alias names for this type: N/A
- Magic number(s): N/A
- File extension(s): json
- Macintosh file type code(s): N/A

Person and email address to contact for further information:
: See Authors' Addresses section.

Intended usage:
: COMMON

Restrictions on usage:
: N/A

Author:
: See Authors' Addresses section.

Change controller:
: N/A

# Interoperability Considerations

Interoperability requirements for media type
registrations are discussed in Section 4.6 of {{!MEDIATYPE=RFC6838}}.

# Security Considerations

Security requirements for media type
registrations are discussed in Section 4.6 of {{!MEDIATYPE=RFC6838}}.

## General Considerations

All JSON Schema Media Types might reference nested or external
resources,
as well as processable information like HTML.

Implementations that try to dereference or process those
resource automatically
might be subject to various security risks,
from resource exhaustion (e.g., caused by cyclic references)
to retrieval and processing of malicious code
(e.g., embedded as markup language).

# IANA Considerations

This specification defines the following new Internet media types {{MEDIATYPE}}.

IANA is asked to update the "Media Types" registry at <https://www.iana.org/assignments/media-types>
with the registration information provided in the sections below.

|--------------------------------------|---------------------------------------------|
| Media Type                           | Registration Information Section            |
|--------------------------------------|---------------------------------------------|
| application/schema+json              | {{schema-json}} of this document            |
| application/schema-instance+json     | {{schema-instance-json}} of this document   |
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

# Change Log
{: numbered="false" removeinrfc="true"}

RFC EDITOR PLEASE DELETE THIS SECTION.

## Since -00
{:numbered="false" removeinrfc="true"}

- Split YAML registrations in a separate I-D.
