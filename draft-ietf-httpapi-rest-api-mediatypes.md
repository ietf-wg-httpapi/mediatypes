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
    title: YAML Ain’t Markup Language Version 1.2
    date: 2002-10-01
    author:
    - ins: Oren Ben-Kiki
    - ins: Clark Evans
    - ins: Ingy doet Net
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
text/yaml,
application/yaml,
application/openapi+json,
and application/openapi+yaml.

--- note_Note_to_Readers

*RFC EDITOR: please remove this section before publication*

Discussion of this draft takes place on the HTTP APIs working group
mailing list (httpapi@ietf.org), which is archived at
[https://mailarchive.ietf.org/arch/browse/httpapi/](https://mailarchive.ietf.org/arch/browse/httpapi/).

The source code and issues list for this draft can be found at
[https://github.com/ioggstream/draft-polli-rest-api-mediatypes](https://github.com/ioggstream/draft-polli-rest-api-mediatypes).

--- middle

# Introduction

OpenAPI Specification [oas] version 3 and above
is a consolidated standard for describing
HTTP APIs using the JSON {{!JSON=RFC8259}} and yaml [yaml] data format.

To increase interoperability when processing API specifications
and leverage content negotiation mechanisms when exchanging
OpenAPI Specification resources
this specification register the following media-types:
`text/yaml`,
`application/yaml`,
`application/openapi+json`
and `application/openapi+yaml`.

## Notational Conventions

{::boilerplate bcp14+}

This document uses the Augmented BNF defined in {{!RFC5234}} and updated
by {{!RFC7405}}.

## The OpenAPI Media Types

The OpenAPI Specification Media Types convey OpenAPI Specification (OAS) files
as defined in [oas] for version 3.0.0 and above.

Those files can be serialized in {{JSON}} or [yaml].
Since there are multiple OpenAPI Specification Specifications versions,
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

# Security Considerations

Security requirements for both media type and media type suffix
registrations are discussed in Section 4.6 of {{!MEDIATYPE=RFC6838}}.

# IANA Considerations

This specification defines the following new Internet media types {{MEDIATYPE}}.

## application/yaml

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

  Deprecated alias names for this type:  application/x-yaml

  Magic number(s):  n/a

  File extension(s):  yaml, yml

  Macintosh file type code(s):  n/a

Person and email address to contact for further information:
  See Authors' Addresses section.

Intended usage:  COMMON

Restrictions on usage:  None.

Author:  See Authors' Addresses section.

Change controller:  n/a

## text/yaml

Type name:  text

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

  Deprecated alias names for this type:  text/x-yaml

  Magic number(s):  n/a

  File extension(s):  yaml, yml

  Macintosh file type code(s):  n/a

Person and email address to contact for further information:
  See Authors' Addresses section.

Intended usage:  COMMON

Restrictions on usage:  None.

Author:  See Authors' Addresses section.

Change controller:  n/a

## application/openapi+json

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

## application/openapi+yaml

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

--- back

# Acknowledgements

Thanks to Erik Wilde and David Biesack for being the initial contributors of this specification,
and to Darrel Miller and Rich Salz for their support during the adoption phase.


# FAQ
{: numbered="false"}

Q: Why this document?
:  After all these years, we still lack a proper media-type for yaml.
   This has some security implications too
   (eg. wrt on identifying parsers or treat downloads)

Q: Why application/yaml and text/yaml
:  Browsers and libraries implementations treats them differently.
   For example Google Chrome will display pages with
   `Content-Type: text/yaml` and to download pages with
   `Content-Type: application/yaml`.

# Change Log
{: numbered="false"}

RFC EDITOR PLEASE DELETE THIS SECTION.
