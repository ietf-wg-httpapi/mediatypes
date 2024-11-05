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

OpenAPI Specification [OAS] version 3 and above
is a consolidated standard for describing
HTTP APIs using the JSON {{JSON}} and YAML [YAML] data format.

To increase interoperability when processing API descriptions
and leverage content negotiation mechanisms when exchanging
OpenAPI description representations
this specification registers the following media types:
`application/openapi+json`
and `application/openapi+yaml`.

## Notational Conventions

{::boilerplate bcp14+}

The terms  "content", "content negotiation", "resource",
and "user agent"
in this document are to be interpreted as in {{HTTP}}.

# Media Type registrations

This section describes the information required to register
the above media types according to {{MEDIATYPE}}.

## The OpenAPI Media Types

The OpenAPI Specification Media Types convey semantics for OpenAPI Document (OAD) resources
as defined in [OAS] for version 3.0 and above.

Those resources can be represented in {{JSON}} or [YAML].

### The version parameter

Since there are multiple OpenAPI Specification versions,
those media types support the `version` parameter.

The following example conveys the desire of a client
to receive an OpenAPI Document resource based on the stated
preferences:

1. openapi 3.1 in YAML
2. openapi 3.0 in YAML
3. any openapi version in JSON

~~~ example

Accept: application/openapi+yaml;version=3.1,
        application/openapi+yaml;version=3.0;q=0.5,
        application/openapi+json;q=0.3
~~~

### The component parameter

The optional `component` parameter indicates that the conveyed content
is not a complete OpenAPI Document.
Instead, it is a referenceable sub-part, (e.g., a single Schema Object,
or a Path Item Object).

Valid values for the `component` parameter
are:

- the star `*` character, indicating that the client
  is willing to accept any component type as well as a complete OpenAPI Document;
- the camelCase names of the associated Object Types,
and depend on the OpenAPI version.
For example, the `component` parameter value for the
Path Item Object defined in OpenAPI 3.1 is `pathItem`,
while the `component` parameter value for the
Schema Object is `schema`.

An example of a request that is willing to accept both
a complete OpenAPI Document and a Schema Object is:

~~~ http-message

GET /person.yaml
Accept: application/openapi+yaml, application/openapi+yaml;component=schema
~~~
{:title "A request that is willing to accept either a complete openapi document or a Schema Object" }

An example response returnning a Schema Object is:

~~~ http-message
HTTP/1.1 200 OK
Content-Type: application/openapi+yaml;component=schema

description: >-
  This schema is enclosed in a separate file,
  that is not a complete OpenAPI Document.
type: object
properties:
  given_name:
    type: string
  family_name:
    type: string

~~~
{:title "OpenAPI response}

### Media Type application/openapi+json {#openapi-json}

The following information serves as the registration form for the `application/openapi+json` media type.

Type name:
: application

Subtype name:
: openapi+json

Required parameters:
: None

Optional parameters:
: version, component; unrecognized parameters should be ignored.

Encoding considerations:
: Same as "application/json"

Security considerations:
: See {{security-considerations}} of this document, "application/json" and [OAS]

Interoperability considerations:
: See "application/json", [OAS] and {{int}}

Published specification:
: this document, [OAS]

Applications that use this media type:
: HTTP

Fragment identifier considerations:
: [OAS] or the specific version
  of the OpenAPI document.

Additional information:

- Deprecated alias names for this type:  N/A

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
: version, component; unrecognized parameters should be ignored

Encoding considerations:
: Same as "+yaml" Structured Syntax Suffix

Security considerations:
: See {{security-considerations}} of this document, "+yaml" Structured Syntax Suffix and [OAS]

Interoperability considerations:
: See "+yaml" Structured Syntax Suffix, [OAS] and {{int}}

Published specification:
: [OAS]

Applications that use this media type:
: HTTP

Fragment identifier considerations:
: [OAS] or the specific version
  of the OpenAPI document.

Additional information:

- Deprecated alias names for this type:  N/A

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
registrations are discussed in Section 4.6 of {{!MEDIATYPE=RFC6838}}.
and in the Interoperability Considerations of the "+yaml" Structured Syntax Suffix.

## Component Parameter {#int-component-parameter}

The `component` parameter allows clients to request specific parts of an OpenAPI Document,
and enables servers to advertise clients that the content does not convey a complete OpenAPI Document.

Current tools tend to process partial documents in the context of a complete document
(e.g., a referenced Schema Object in the context of the sourcing OpenAPI Document).
While the `component` parameter can be a hint for processing tools,
implementors interested in interoperability should be tolerant of the absence of the `component` parameter.

# Security Considerations

Security requirements for media type
registrations are discussed in Section 4.6 of {{!MEDIATYPE=RFC6838}}.
and in the Security Considerations of the "+yaml" Structured Syntax Suffix.

## General Considerations

OpenAPI documents are processed by a wide variety of tooling for numerous different purposes, such as client code generation, documentation generation, server side routing, and API testing. OpenAPI document authors must consider the risks of the scenarios where the OpenAPI document may be used.

An OpenAPI document describes the security schemes used to protect the resources it defines. The security schemes available offer varying degrees of protection. Factors such as the sensitivity of the data and the potential impact of a security breach should guide the selection of security schemes for the API resources. Some security schemes, such as basic auth and OAuth Implicit flow, are supported for compatibility with existing APIs. However, their inclusion in OpenAPI does not constitute an endorsement of their use, particularly for highly sensitive data or operations.

OpenAPI documents may contain references to external resources that may be dereferenced automatically by consuming tools. External resources may be hosted on different domains that may be untrusted. References in an OpenAPI document, or across OpenAPI documents may cause a cycle. Tooling must detect and handle cycles to prevent resource exhaustion.

Certain properties allow the use of Markdown which can contain HTML including script. It is the responsibility of tooling to appropriately sanitize the Markdown.

OpenAPI documents use [jsonschema] therefore share the security consideration of JSON Schema.

# IANA Considerations

This specification defines the following new Internet media types {{MEDIATYPE}}.

IANA is asked to update the "Media Types" registry at <https://www.iana.org/assignments/media-types>
with the registration information provided in the sections below.

|--------------------------------------|---------------------------------------------|
| Media Type                           | Registration information section            |
|--------------------------------------|---------------------------------------------|
| application/openapi+yaml             | {{openapi-yaml}} of this document           |
| application/openapi+json             | {{openapi-json}} of this document           |
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

Q: Do we support OpenAPI 2.0 / Swagger?
:  No, this document is about OpenAPI 3.0 and above.

# Change Log
{: numbered="false" removeinrfc="true"}

RFC EDITOR PLEASE DELETE THIS SECTION.

## Since -00
{:numbered="false" removeinrfc="true"}

- Split YAML registrations in a separate I-D.

## Since -04
{:numbered="false" removeinrfc="true"}

- Split JSONSCHEMA registrations in a separate I-D.
