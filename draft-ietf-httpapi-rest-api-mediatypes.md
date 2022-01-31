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
  yaml:
    title: YAML Ain't Markup Language Version 1.2
    date: 2002-10-01
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

informative:

--- abstract

This document registers
the following media types used in APIs
on the IANA Media Types registry:
application/yaml,
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
HTTP APIs using the JSON {{!JSON=RFC8259}} and yaml [yaml] data format.

To increase interoperability when processing API specifications
and leverage content negotiation mechanisms when exchanging
OpenAPI Specification resources
this specification register the following media-types:
`application/yaml`,
`application/openapi+json`
and `application/openapi+yaml`.

## Notational Conventions

{::boilerplate bcp14+}

This document uses the Augmented BNF defined in {{!RFC5234}} and updated
by {{!RFC7405}}.

# Media Type registrations

This section describes the information required to register
the above media types.

## Media Type application/yaml {#application-yaml}

The following information serves as the registration form for the `application/yaml` media type.

Type name:  application

Subtype name:  yaml

Required parameters:  None

Optional parameters:  None; unrecognized parameters should be ignored

Encoding considerations:  Same as {{JSON}}

Security considerations:  see {{security-considerations}} of this document

Interoperability considerations:  None

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

## The OpenAPI Media Types

The OpenAPI Specification Media Types convey OpenAPI document (OAS) files
as defined in [oas] for version 3.0.0 and above.

Those files can be serialized in {{JSON}} or [yaml].
Since there are multiple OpenAPI Specification versions,
those media-types support the `version` parameter.

The following examples conveys the desire of a client
to receive an OpenAPI Specification resource preferably in the following
order:

1. openapi 3.1 in yaml
2. openapi 3.0 in yaml
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

Interoperability considerations:  None

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


# Security Considerations

Security requirements for both media type and media type suffix
registrations are discussed in Section 4.6 of {{!MEDIATYPE=RFC6838}}.

# IANA Considerations

This specification defines the following new Internet media types {{MEDIATYPE}}.

IANA has updated the "Media Types" registry at <https://www.iana.org/assignments/media-types>
with the registration information provided below.

|--------------------------|---------------------------------------|
| Media Type               |                         Section       |
|--------------------------|---------------------------------------|
| application/yaml         | {{application-yaml}} of ThisRFC       |
| application/openapi+yaml | {{openapi-yaml}} of ThisRFC           |
| application/openapi+json | {{openapi-json}} of ThisRFC           |
|--------------------------|---------------------------------------|

--- back

# Acknowledgements

Thanks to Erik Wilde and David Biesack for being the initial contributors of this specification,
and to Darrel Miller and Rich Salz for their support during the adoption phase.

In addition to the people above, this document owes a lot to the extensive discussion inside
and outside the HTTPAPI workgroup,
including Eemeli Aro and Ingy dot Net.


# FAQ
{: numbered="false"}

Q: Why this document?
:  After all these years, we still lack a proper media-type for yaml.
   This has some security implications too
   (eg. wrt on identifying parsers or treat downloads)

# Change Log
{: numbered="false"}

RFC EDITOR PLEASE DELETE THIS SECTION.
