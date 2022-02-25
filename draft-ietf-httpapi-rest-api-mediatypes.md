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
  oas:
    title: OpenAPI Specification 3.0.0
    date: 2017-07-26
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
application/yaml,
application/schema+json,
application/schema-instance+json,
application/openapi+json,
and application/openapi+yaml.

--- note_Note_to_Readers

*RFC EDITOR: please remove this section before publication*

Discussion of this draft takes place on the HTTP APIs working group
mailing list (httpapi@ietf.org), which is archived at
[https://mailarchive.ietf.org/arch/browse/httpapi/](https://mailarchive.ietf.org/arch/browse/httpapi/).

The source code and issues list for this draft can be found at
[https://github.com/ietf-wg-httpapi/mediatypes](https://github.com/ietf-wg-httpapi/mediatypes).

--- middle

# Introduction

OpenAPI Specification [oas] version 3 and above
is a consolidated standard for describing
HTTP APIs using the JSON {{!JSON=RFC8259}} and YAML [YAML] data format.

To increase interoperability when processing API specifications
and leverage content negotiation mechanisms when exchanging
OpenAPI Specification resources
this specification register the following media-types:
`application/yaml`,
`application/schema+json`,
`application/schema-instance+json`,
`application/openapi+json`
and `application/openapi+yaml`.

Moreover it defines and registers
the `+yaml` structured syntax suffix.

## Notational Conventions

{::boilerplate bcp14+}

This document uses the Augmented BNF defined in {{!RFC5234}} and updated
by {{!RFC7405}}.

# Media Type registrations

This section describes the information required to register
the above media types according to {{!MEDIATYPE=RFC6838}}

## Media Type application/yaml {#application-yaml}

The following information serves as the registration form for the `application/yaml` media type.

Type name:  application

Subtype name:  yaml

Required parameters:  None

Optional parameters:  None; unrecognized parameters should be ignored

Encoding considerations:  Same as {{JSON}}

Security considerations:  see {{security-considerations}} of this document

Interoperability considerations:  see {{int-yaml}} of this document

Published specification: (this document)

Applications that use this media type:  HTTP

Fragment identifier considerations:  Same as for application/json
  {{JSON}}

Additional information:

  Deprecated alias names for this type:  application/x-yaml, text/yaml, text/x-yaml

  Magic number(s):  n/a

  File extension(s):  yaml, yml

  Macintosh file type code(s):  n/a

Person and email address to contact for further information:
  See Authors' Addresses section.

Intended usage:  COMMON

Restrictions on usage:  None.

Author:  See Authors' Addresses section.

Change controller:  n/a


## The +yaml Structured Syntax Suffix {#suffix-yaml}

The suffix
`+yaml` MAY be used with any media type whose representation follows
that established for `application/yaml`.
The media type structured syntax suffix registration form follows.
See {{MEDIATYPE}} for definitions of each of the registration form headings.

   Name:  YAML Ain't Markup LanguageML (YAML)

   +suffix:  +yaml

   References:  [YAML]

   Encoding considerations: see {{application-yaml}}

   Fragment identifier considerations:

      The syntax and semantics of fragment identifiers specified for
      +yaml SHOULD be as specified for {{application-yaml}}

      The syntax and semantics for fragment identifiers for a specific
      `xxx/yyy+json` SHOULD be processed as follows:

      For cases defined in +yaml, where the fragment identifier resolves
      per the +yaml rules, then process as specified in +yaml.

         For cases defined in +yaml, where the fragment identifier does
         not resolve per the +yaml rules, then process as specified in
         `xxx/yyy+yaml`.

         For cases not defined in +yaml, then process as specified in
         `xxx/yyy+yaml`.

   Interoperability considerations:  See {{application-yaml}}

   Security considerations:  See {{application-yaml}}

   Contact:  See Authors' Addresses section.

   Author:  See Authors' Addresses section

   Change controller:  n/a


## The OpenAPI Media Types

The OpenAPI Specification Media Types convey OpenAPI document (OAS) files
as defined in [oas] for version 3.0.0 and above.

Those files can be serialized in {{JSON}} or [YAML].
Since there are multiple OpenAPI Specification versions,
those media-types support the `version` parameter.

The following examples conveys the desire of a client
to receive an OpenAPI Specification resource preferably in the following
order:

1. openapi 3.1 in YAML
2. openapi 3.0 in YAML
3. any openapi version in json

~~~ example

Accept: application/openapi+yaml;version=3.1,
        application/openapi+yaml;version=3.0;q=0.5,
        application/openapi+json;q=0.3
~~~

### Media Type application/openapi+json {#openapi-json}

The following information serves as the registration form for the `application/openapi+json` media type.

Type name:  application

Subtype name:  openapi+json

Required parameters:  None

Optional parameters:  version; unrecognized parameters should be ignored

Encoding considerations:  Same as {{JSON}}

Security considerations:  see {{security-considerations}} of this document

Interoperability considerations:  None

Published specification: (this document)

Applications that use this media type:  HTTP

Fragment identifier considerations:  Same as for application/json
  {{JSON}}

Additional information:

  Deprecated alias names for this type:  n/a

  Magic number(s):  n/a

  File extension(s):  json

  Macintosh file type code(s):  n/a

Person and email address to contact for further information:
  See Authors' Addresses section.

Intended usage:  COMMON

Restrictions on usage:  None.

Author:  See Authors' Addresses section.

Change controller:  n/a

### Media Type application/openapi+yaml {#openapi-yaml}

The following information serves as the registration form for the `application/openapi+yaml` media type.

Type name:  application

Subtype name:  openapi+yaml

Required parameters:  None

Optional parameters:  version; unrecognized parameters should be ignored

Encoding considerations:  Same as {{JSON}}

Security considerations:  see {{security-considerations}} of this document

Interoperability considerations:  see {{application-yaml}}

Published specification: (this document)

Applications that use this media type:  HTTP

Fragment identifier considerations:  Same as for application/json
  {{JSON}}

Additional information:

  Deprecated alias names for this type:  n/a

  Magic number(s):  n/a

  File extension(s):  yaml, yml

  Macintosh file type code(s):  n/a

Person and email address to contact for further information:
  See Authors' Addresses section

Intended usage:  COMMON

Restrictions on usage:  None.

Author:  See Authors' Addresses section

Change controller:  n/a

## JSON Schema Media Types

JSON Schema is a declarative domain-specific language for validating and
annotating JSON documents (see {{jsonschema}}).

This document registers the media types associated with JSON Schema.

There are many dialects of JSON Schema in wide use today. The JSON Schema
maintainers have released several dialects including draft-04, draft-07, and
draft 2020-12. There are also several third-party JSON Schema dialects in wide
use including the ones defined for use in OpenAPI and MongoDB.

This specification defines little more than how to identify the dialect while
leaving most of the semantics of the schema up to the dialect to define. Clients
MUST use the following order of precedence for determining the dialect of a
schema.

* The `$schema` keyword ({{schema-keyword}})
* The "schema" media type parameter ({{schema-parameter}})
* The context of the enclosing document. This applies only when a schema is
  embedded within a document. The enclosing document could be another schema in
  the case of a bundled schema or it could be another type of document that
  includes schemas such as an OpenAPI document.
* If none of the above result in identifying the dialect, client behavior is
  undefined.

### The "$schema" Keyword {#schema-keyword}

The `$schema` keyword is used as a JSON Schema dialect identifier. The value of
this keyword MUST be a URI {{!RFC3986}}. This URI SHOULD identify a meta-schema
that can be used to validate that the schema is syntactically correct according
to the dialect the URI identifies.

The dialect SHOULD define where the `$schema` keyword is allowed and/or
recognized in a schema, but it is RECOMMENDED that dialects do not allow the
schema to change within the same Schema Resource.

### Identifying a Schema via a Media Type Parameter {#schema-parameter}

Media types MAY allow for a `schema` media type parameter, to support content
negotiation based on schema identifier (see Section 12 of {{!SEMANTICS=RFC7231}}).
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
GET /pet/1234 HTTP/1.1
Accept: application/schema-instance+json; schema="/schemas/v2/pet"; q=0.2,
        application/schema-instance+json; schema="/schemas/v1/pet"; q=0.1
~~~

Response:

~~~ http-message
HTTP/1.1 200 Ok
Content-Type: application/schema-instance+json; schema="/schemas/v2/pet"

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
GET /schemas/v2/pet HTTP/1.1
Accept: application/schema+json; schema="https://json-schema.org/draft/2020-12/schema",
        application/schema+json; schema="http://json-schema.org/draft-07/schema#"
~~~

Response:

~~~ http-message
HTTP/1.1 200 OK
Content-Type: application/schema+json; schema="https://json-schema.org/draft/2020-12/schema"

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

In HTTP, such links can be attached to any response using the `Link` header
{{!LINK=RFC8288}}.

~~~
Link: <https://example.com/my-hyper-schema#>; rel="describedby"
~~~

### Fragment Identifiers {#schema-fragment}

Two fragment identifier structures are supported: JSON Pointers and plain-names.

The use of JSON Pointers as URI fragment identifiers is described in RFC 6901
{{!RFC6901}}. Fragment identifiers that are empty or start with a `/`, MUST be
interpreted as JSON Pointer fragment identifiers.

Plain-name fragment identifiers reference locally named locations in the
document. The dialect determines how plain-name identifiers map to locations
within the document. All fragment identifiers that do not match the JSON Pointer
syntax MUST be interpreted as plain name fragment identifiers.

### Media Type application/schema+json {#schema-json}

The `application/schema+json` media type represents JSON Schema. This schema can
be an official dialect or a third-party dialect. The following information
serves as the registration form for the `application/schema+json` media type.

**Type name**: application

**Subtype name**: schema+json

**Required parameters**: N/A

**Optional parameters**:

* **schema**: A URI identifying the JSON Schema dialect the schema was written
  for. If this value conflicts with the value of the `$schema` keyword in the
  schema, the `$schema` keyword takes precedence.

**Encoding considerations**: Same as {{JSON}}

**Security considerations**: See the "Security Considerations" section of
{{jsonschema}}

**Interoperability considerations**: See the "General Considerations" section of
{{jsonschema}}

**Published specification**: (this document)

**Applications that use this media type**: JSON Schema is used in a variety of
applications including API servers and clients that validate JSON requests and
responses, IDEs that valid configuration files, databases that store JSON, and
more.

**Fragment identifier considerations**: See {{schema-fragment}}

**Additional information**:

  * **Deprecated alias names for this type**: N/A

  * **Magic number(s)**: N/A

  * **File extension(s)**: json, schema.json

  * **Macintosh file type code(s)**: N/A

**Person and email address to contact for further information**: See Authors'
Addresses section.

**Intended usage**: COMMON

**Restrictions on usage**: N/A.

**Author**: See Authors' Addresses section.

**Change controller**: N/A

### Media Type application/schema-instance+json {#schema-instance-json}

The `application/schema-instance+json` media type is an extension of the
{{JSON}} media type that just adds the `schema` media type parameter and
fragment identification. The following information serves as the registration
form for the `application/schema-instance+json` media type.

**Type name**: application

**Subtype name**: schema-instance+json

**Required parameters**: N/A

**Optional parameters**:

* **schema**: A URI identifying a JSON Schema that provides semantic information
  about this JSON representation.

**Encoding considerations**: Same as {{JSON}}

**Security considerations**: Same as {{JSON}}

**Interoperability considerations**: Same as {{JSON}}

**Published specification**: (this document)

**Applications that use this media type**: JSON Schema is used in a variety of
applications including API servers and clients that validate JSON requests and
responses, IDEs that valid configuration files, databases that store JSON, and
more.

**Fragment identifier considerations**: See {{schema-fragment}}

**Additional information**:

  * **Deprecated alias names for this type**: N/A
  * **Magic number(s)**: N/A
  * **File extension(s)**: json
  * **Macintosh file type code(s)**: N/A

**Person and email address to contact for further information**: See Authors'
Addresses section.

**Intended usage**: COMMON

**Restrictions on usage**: N/A

**Author**: See Authors' Addresses section.

**Change controller**: N/A

# Interoperability Considerations {#interoperability}

## YAML Media Types {#int-yaml}

### YAML is an Evolving Language {#int-yaml-evolving}

YAML is an evolving language and, in time,
some features have been added, and others removed.

While this document is based on a given YAML version [YAML],
media types registration does not imply a specific version.
This allows content negotiation of version-independent YAML resources.

Implementers concerned about features related to a specific YAML version
can specify it the documents using the `%YAML` directive
(see Section 6.8.1 of [YAML]).

# Security Considerations

Security requirements for both media type and media type suffix
registrations are discussed in Section 4.6 of {{!MEDIATYPE=RFC6838}}.

# IANA Considerations

This specification defines the following new Internet media types {{MEDIATYPE}}.

IANA has updated the "Media Types" registry at <https://www.iana.org/assignments/media-types>
with the registration information provided below.

|--------------------------------------|---------------------------------------|
| Media Type                           | Section                               |
|--------------------------------------|---------------------------------------|
| application/yaml                     | {{application-yaml}} of ThisRFC       |
| application/openapi+yaml             | {{openapi-yaml}} of ThisRFC           |
| application/openapi+json             | {{openapi-json}} of ThisRFC           |
| application/schema+json              | {{schema-json}} of ThisRFC            |
| application/schema-instance+json     | {{schema-instance-json}} of ThisRFC   |
|--------------------------------------|---------------------------------------|

IANA has updated the "Structured Syntax Suffixes" registry at <https://www.iana.org/assignments/media-type-structured-suffix>
with the registration information provided below.

|--------------------------|---------------------------------------|
| Suffix                   |                         Section       |
|--------------------------|---------------------------------------|
| +yaml                    | {{suffix-yaml}} of ThisRFC            |
|--------------------------|---------------------------------------|


--- back

# Acknowledgements

Thanks to Erik Wilde and David Biesack for being the initial contributors of this specification,
and to Darrel Miller and Rich Salz for their support during the adoption phase.

In addition to the people above, this document owes a lot to the extensive discussion inside
and outside the HTTPAPI workgroup.
The following contributors have helped improve this specification by
opening pull requests, reporting bugs, asking smart questions,
drafting or reviewing text, and evaluating open issues:

Eemeli Aro, Tina (tinita) Müller,
Ben Hutton
and Jason Desrosiers.



# FAQ
{: numbered="false"}

Q: Why this document?
:  After all these years, we still lack a proper media-type for YAML.
   This has some security implications too
   (eg. wrt on identifying parsers or treat downloads)

# Change Log
{: numbered="false"}

RFC EDITOR PLEASE DELETE THIS SECTION.
