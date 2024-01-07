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
application/openapi+json,
and application/openapi+yaml.

--- middle

# Introduction

OpenAPI Specification [OAS] version 3 and above
is a consolidated standard for describing
HTTP APIs using the JSON {{!JSON=RFC8259}} and YAML [YAML] data format.

To increase interoperability when processing API description
and leverage content negotiation mechanisms when exchanging
OpenAPI description resources
this specification register the following media types:
`application/openapi+json`
and `application/openapi+yaml`.

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

## The OpenAPI Media Types

The OpenAPI Specification Media Types convey OpenAPI document (OAS) files
as defined in [OAS] for version 3.0 and above.

Those files can be serialized in {{JSON}} or [YAML].
Since there are multiple OpenAPI Specification versions,
those media types support the `version` parameter.

The following example conveys the desire of a client
to receive an OpenAPI Specification resource preferably in the following
order:

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
: version; unrecognized parameters should be ignored

Encoding considerations:
: Same as "application/json"

Security considerations:
: See {{security-considerations}} of this document, "application/json" and [OAS]

Interoperability considerations:
: See "application/json" and [OAS]

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
: version; unrecognized parameters should be ignored

Encoding considerations:
: Same as "+yaml" Structured Syntax Suffix

Security considerations:
: See {{security-considerations}} of this document, "+yaml" Structured Syntax Suffix and [OAS]

Interoperability considerations:
: See "+yaml" Structured Syntax Suffix and [OAS]

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


# Interoperability Considerations

Interoperability requirements for media type
registrations are discussed in Section 4.6 of {{!MEDIATYPE=RFC6838}}.
and in the Interoperability Considerations of the "+yaml" Structured Syntax Suffix.

# Security Considerations

Security requirements for  media type
registrations are discussed in Section 4.6 of {{!MEDIATYPE=RFC6838}}.
and in the Security Considerations of the "+yaml" Structured Syntax Suffix.

## General Considerations

All REST API Media Types might reference nested or external
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

# Change Log
{: numbered="false" removeinrfc="true"}

RFC EDITOR PLEASE DELETE THIS SECTION.

## Since -00
{:numbered="false" removeinrfc="true"}

- Split YAML registrations in a separate I-D.

## Since -04
{:numbered="false" removeinrfc="true"}

- Split JSONSCHEMA registrations in a separate I-D.
