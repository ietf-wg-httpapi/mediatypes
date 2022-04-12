---
title: YAML Media Types
abbrev:
docname: draft-ietf-httpapi-yaml-mediatypes-latest
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
 -
    ins: E. Wilde
    name: Erik Wilde
    org: Axway
    email: erik.wilde@dret.net
    country: Switzerland
 -
    ins: E. Aro
    name: Eemeli Aro
    email: eemeli@gmail.com
    country: Finland

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

informative:

--- abstract

This document registers
the application/yaml media type
and the +yaml structured syntax suffix
on the IANA Media Types registry.

--- note_Note_to_Readers

*RFC EDITOR: please remove this section before publication*

Discussion of this draft takes place on the HTTP APIs working group
mailing list (httpapi@ietf.org), which is archived at
[https://mailarchive.ietf.org/arch/browse/httpapi/](https://mailarchive.ietf.org/arch/browse/httpapi/).

The source code and issues list for this draft can be found at
[https://github.com/ietf-wg-httpapi/mediatypes](https://github.com/ietf-wg-httpapi/mediatypes).

--- middle

# Introduction

YAML [YAML] is a data serialization format that is widely used on the Internet,
including in the API sector (e.g. see [oas])
but the relevant media type and structured syntax suffix are not registered by IANA.

To increase interoperability when exchanging YAML data
and leverage content negotiation mechanisms when exchanging
YAML resources,
this specification
registers the `application/yaml` media type
and the `+yaml` structured syntax suffix.

Moreover, it provides security considerations
and interoperability considerations related to [YAML],
including its relation with {{!JSON=RFC8259}}.

## Notational Conventions

{::boilerplate bcp14+}

This document uses the Augmented BNF defined in {{!RFC5234}} and updated
by {{!RFC7405}}.

The terms  "content", "content negotiation", "resource",
and "user agent"
in this document are to be interpreted as in {{!SEMANTICS=I-D.ietf-httpbis-semantics}}.

The terms "fragment" and "fragment identifier"
in this document are to be interpreted as in {{!URI=RFC3986}}.

The terms "node", "anchor" and "named anchor"
in this document are to be intepreded as in [YAML].

## Fragment identification {#application-yaml-fragment}

This section describes how to use
named anchors (see Section 3.2.2.2 of [YAML])
as fragment identifier to designate a node.

A YAML named anchor can be represented in a URI fragment identifier
by encoding it into octects using UTF-8 {{!UTF-8=RFC3629}},
while percent-encoding those characters not allowed by the fragment rule
in {{Section 3.5 of URI}}. 

If multiple nodes would match a fragment identifier,
the first such match is selected.

Users concerned with interoperability of fragment identifiers:

- SHOULD limit named anchors to a set of characters
  that do not require encoding 
  to be expressed as URI fragment identifiers:
  this is always possible since named anchors are a serialization
  detail;
- SHOULD NOT use a named anchor that matches multiple nodes.

In the example resource below, the URL `file.yaml#foo`
references the anchor `foo` pointing to the node with value `scalar`;
whereas
the URL `file.yaml#bar` references the anchor `bar` pointing to the node
with value `[ some, sequence, items ]`.

~~~ example
 %YAML 1.2
 ---
 one: &foo scalar
 two: &bar
   - some
   - sequence
   - items
~~~


# Media Type registrations

This section describes the information required to register
the above media types according to {{!MEDIATYPE=RFC6838}}

## Media Type application/yaml {#application-yaml}

The following information serves as the registration form for the `application/yaml` media type.

Type name:
: application

Subtype name:
: yaml

Required parameters:
: None

Optional parameters:
: None; unrecognized parameters should be ignored

Encoding considerations:
: binary

Security considerations:
: see {{security-considerations}} of this document

Interoperability considerations:
: see {{interoperability-considerations}} of this document

Published specification:
: this document

Applications that use this media type:
: HTTP

Fragment identifier considerations:
: see {{application-yaml-fragment}}

Additional information:

- Deprecated alias names for this type:  application/x-yaml, text/yaml, text/x-yaml

- Magic number(s)  n/a

- File extension(s):  yaml, yml

- Macintosh file type code(s):  n/a

Person and email address to contact for further information:
: See Authors' Addresses section.

Intended usage:
: COMMON

Restrictions on usage:
: None.

Author:
: See Authors' Addresses section.

Change controller:
: n/a

## The +yaml Structured Syntax Suffix {#suffix-yaml}

The suffix
`+yaml` MAY be used with any media type whose representation follows
that established for `application/yaml`.
The media type structured syntax suffix registration form follows.
See {{MEDIATYPE}} for definitions of each of the registration form headings.

  Name:
  : YAML Ain't Markup LanguageML (YAML)

  +suffix:
  :  +yaml

  References:
  :  [YAML]

  Encoding considerations:
  : see {{application-yaml}}

  Fragment identifier considerations:
  : The syntax and semantics of fragment identifiers specified for
    +yaml SHOULD be as specified for {{application-yaml}}
    The syntax and semantics for fragment identifiers for a specific
    `xxx/yyy+yaml` SHOULD be processed as follows:

    1. For cases defined in +yaml, where the fragment identifier resolves
       per the +yaml rules, then process as specified in +yaml.

    1. For cases defined in +yaml, where the fragment identifier does
       not resolve per the +yaml rules, then process as specified in
      `xxx/yyy+yaml`.

    1. For cases not defined in +yaml, then process as specified in
      `xxx/yyy+yaml`.

  Interoperability considerations:
  : See {{application-yaml}}

  Security considerations:
  : See {{application-yaml}}

  Contact:
  : See Authors' Addresses section.

  Author:
  : See Authors' Addresses section

  Change controller:
  :  n/a

# Interoperability Considerations

## YAML is an Evolving Language {#int-yaml-evolving}

YAML is an evolving language and, in time,
some features have been added, and others removed.

While this document is based on a given YAML version [YAML],
media types registration does not imply a specific version.
This allows content negotiation of version-independent YAML resources.

Implementers concerned about features related to a specific YAML version
can specify it in the documents using the `%YAML` directive
(see Section 6.8.1 of [YAML]).

## YAML and JSON {#int-yaml-and-json}

When using flow collection styles (see Section 7.4 of [YAML])
a YAML document could look like JSON [JSON],
thus similar interoperability considerations apply.

When using YAML as a more efficient format
to serialize information intented to be consumed as JSON,
information can be discarded:
this includes comments (see Section 3.2.3.3 of [YAML])
and alias nodes (see Section 7.1 of [YAML]),
that do not have a JSON counterpart.

~~~ example
# This comment will be lost
# when serializing in JSON.
Title:
  type: string
  maxLength: &text_limit 64

Name:
  type: string
  maxLength: *text_limit  # Replaced by the value 64.
~~~
{: title="JSON replaces alias nodes with static values." #example-json-discards-information}

Implementers need to ensure that relevant
information will not be lost during the processing.
For example, they might consider acceptable
that alias nodes are replaced by static values.

In some cases an implementer may want to
define a list of allowed YAML features,
taking into account that the following ones
might have interoperability
issues with JSON:

- non UTF-8 encoding, since YAML supports UTF-16 and UTF-32 in addition to UTF-8;
- mapping keys that are not strings;
- circular references represented using anchor (see {{sec-yaml-exhaustion}}
  and {{example-yaml-cyclic}});
- `.inf` and `.nan` float values, since JSON does not support them;
- non-JSON types,
  including the ones associated with tags like `!!timestamp`
  that were included in the default schema of older YAML versions;
- tags in general, and specifically the ones that do not map
  to JSON types like
  custom and local tags such as `!!python/object` and
  `!mytag` (see Section 2.4 of [YAML]);

~~~ example
non-json-keys:
  2020-01-01: a timestamp
  [0, 1]: a sequence
  ? {k: v}
  : a map
non-json-value: 2020-01-01
~~~
{: title="Example of mapping keys not supported in JSON" #example-unsupported-keys}

# Security Considerations

Security requirements for both media type and media type suffix
registrations are discussed in Section 4.6 of {{!MEDIATYPE=RFC6838}}.

## Arbitrary Code Execution {#sec-yaml-code-execution}

Care should be used when using YAML tags,
because their resolution might trigger unexpected code execution.

Code execution in deserializers should be disabled by default,
and only be enabled explicitly.
In those cases, the implementation should ensure - for example, via specific functions -
that the code execution results in strictly bounded time/memory limits.

Many implementations provide safe deserializers addressing these issues.

## Resource Exhaustion {#sec-yaml-exhaustion}

YAML documents are rooted, connected, directed graphs
and can contain reference cycles,
so they can't be treated as simple trees (see Section 3.2.1 of [YAML]).
An implementation that attempts to do that
can infinite-loop at some point (e.g. when trying to serialize a YAML document in JSON).

~~~ yaml
x: &x
  y: *x
~~~
{: title="A cyclic document" #example-yaml-cyclic}

Even if a document is not cyclic, treating it as a simple tree could lead to improper behaviors
(such as the "billion laughs" problem).

~~~ yaml
x1: &a1 ["a", "a"]
x2: &a2 [*a1, *a1]
x3: &a3 [*a2, *a2]
~~~
{: title="A billion laughs document" #example-yaml-1e9lol}

This can be addressed using processors limiting the anchor recursion depth
and validating the input before processing it;
even in these cases it is important
to carefully test the implementation you are going to use.
The same considerations apply when serializing a YAML representation graph
in a format that does not support reference cycles (see {{int-yaml-and-json}}).

# IANA Considerations

This specification defines the following new Internet media types {{MEDIATYPE}}.

IANA has updated the "Media Types" registry at <https://www.iana.org/assignments/media-types>
with the registration information provided below.

|--------------------------------------|---------------------------------------------|
| Media Type                           | Section                                     |
|--------------------------------------|---------------------------------------------|
| application/yaml                     | {{application-yaml}} of this document       |
|--------------------------------------|---------------------------------------------|

IANA has updated the "Structured Syntax Suffixes" registry at <https://www.iana.org/assignments/media-type-structured-suffix>
with the registration information provided below.

|--------------------------|------------------------------------------|
| Suffix                   | Section                                  |
|--------------------------|------------------------------------------|
| +yaml                    | {{suffix-yaml}} of this document         |
|--------------------------|------------------------------------------|


--- back

# Acknowledgements

Thanks to Erik Wilde and David Biesack for being the initial contributors of this specification,
and to Darrel Miller and Rich Salz for their support during the adoption phase.

In addition to the people above, this document owes a lot to the extensive discussion inside
and outside the HTTPAPI workgroup.
The following contributors have helped improve this specification by
opening pull requests, reporting bugs, asking smart questions,
drafting or reviewing text, and evaluating open issues:

Tina (tinita) Müller,
Ben Hutton,
Manu Sporny
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
