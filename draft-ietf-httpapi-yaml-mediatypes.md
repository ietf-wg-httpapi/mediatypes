---
title: YAML Media Type
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
    org: Mozilla
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
    - ins: Tina Müller
    - ins: Pantelis Antoniou
    - ins: Eemeli Aro
    - ins: Thomas Smith
    target: https://yaml.org/spec/1.2.2/
  OAS:
    title: OpenAPI Specification 3.0.0
    date: 2017-07-26
    author:
    - ins: Darrel Miller
    - ins: Jeremy Whitlock
    - ins: Marsh Gardiner
    - ins: Mike Ralphson
    - ins: Ron Ratovsky
    - ins: Uri Sarid
  JSON-POINTER: RFC6901

informative:
  I-D.ietf-jsonpath-base:

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
including in the API sector (e.g. see [OAS]),
but the relevant media type and structured syntax suffix previously had not been registered by IANA.

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

The terms "node", "alias node", "anchor" and "named anchor"
in this document are to be intepreded as in [YAML].

## Fragment identification {#application-yaml-fragment}

This section describes how to use
alias nodes (see Section 3.2.2.2 and 7.1 of [YAML])
as fragment identifiers to designate nodes.

A YAML alias node can be represented in a URI fragment identifier
by encoding it into octects using UTF-8 {{!UTF-8=RFC3629}},
while percent-encoding those characters not allowed by the fragment rule
in {{Section 3.5 of URI}}.

If multiple nodes would match a fragment identifier,
the first such match is selected.

A fragment identifier is not guaranteed to reference an existing node.
Therefore, applications SHOULD define how an unresolved alias node
ought to be handled.

Users concerned with interoperability of fragment identifiers:

- SHOULD limit alias nodes to a set of characters
  that do not require encoding
  to be expressed as URI fragment identifiers:
  this is generally possible since
  named anchors are a serialization
  detail;
- SHOULD NOT use alias nodes that match multiple nodes.

In the example resource below, the URL `file.yaml#*foo`
references the alias node `*foo` pointing to the node with value `scalar`;
whereas
the URL `file.yaml#*bar` references the alias node `*bar` pointing to the node
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


# Media Type and Structured Syntax Suffix registrations

This section describes the information required to register
the above media type according to {{!MEDIATYPE=RFC6838}}

## Media Type application/yaml {#application-yaml}

The media type for YAML text is `application/yaml`;
the following information serves as the registration form for this media type.

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
: [YAML]

Applications that use this media type:
: HTTP

Fragment identifier considerations:
: An empty fragment identifier references
  the root node.

  A fragment identifier starting with "*"
  is to be interpreted as a YAML alias node {{application-yaml-fragment}}.

  A fragment identifier starting with "/"
  is to be interpreted as a JSON Pointer {{JSON-POINTER}}
  and is evaluated on the YAML representation graph,
  walking through alias nodes;
  this syntax can only reference YAML nodes that are
  on a path that is made up of nodes interoperable with
  the JSON data model (see {{int-yaml-and-json}}).

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
  : YAML Ain't Markup Language (YAML)

  +suffix:
  :  +yaml

  References:
  :  [YAML]

  Encoding considerations:
  : see {{application-yaml}}

  Fragment identifier considerations:
  : Differently from `application/yaml`,
    there is no fragment identification syntax defined
    for +yaml.

    A specific `xxx/yyy+yaml` media type
    needs to define the syntax and semantics for fragment identifiers
    because the ones in {{application-yaml}}
    do not apply unless explicitly expressed.

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

YAML is an evolving language and, over time,
some features have been added and others removed.

While this document is based on a given YAML version [YAML],
the media type registration does not imply a specific version.
This allows content negotiation of version-independent YAML resources.

Implementers concerned about features related to a specific YAML version
can specify it in documents using the `%YAML` directive
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
 %YAML 1.2
 ---
 non-json-keys:
   0: a number
   2020-01-01: a timestamp
   [0, 1]: a sequence
   ? {k: v}
   : a map
 non-json-value: 2020-01-01
~~~
{: title="Example of mapping keys not supported in JSON" #example-unsupported-keys}

## Fragment identifiers {#int-fragment}

To allow fragment identifiers to traverse alias nodes,
the YAML representation graph needs to be generated before the fragment identifier evaluation.
It is important that this evaluation will not cause the issues mentioned in {{int-yaml-and-json}}
and in [Security considerations](#security-considerations) such as infinite loops and unexpected code execution.

Implementers need to consider that the YAML version and supported features (e.g. merge keys)
can impact on the generation of the representation graph (see {{example-merge-keys}}).

In {{application-yaml}}, this document extends the use of specifications based on
the JSON data model with support for YAML fragment identifiers.
This is to improve the interoperability of already consolidated practices,
such as the one of writing [OpenAPI documents](#OAS) in YAML.

{{ex-fragid}} provides a non exhaustive list of examples that could help
understanding interoperability issues related to fragment identifiers.

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
can infinite-loop traversing the YAML representation graph at some point,
for example:

- when trying to serialize it JSON;
- or when searching/identifying nodes using specifications based on the JSON data model (e.g. {{JSON-POINTER}}).

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

This specification defines the following new Internet media type {{MEDIATYPE}}.

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

# Examples related to fragment identifier interoperability {#ex-fragid}

## Unreferenceable nodes

In this example, a couple of YAML nodes that cannot be referenced
based on the JSON data model
since their mapping keys are not strings.

~~~ example
 %YAML 1.2
 ---
 a-map-cannot:
   ? {be: expressed}
   : with a JSON Pointer

 0: no numeric mapping keys in JSON
~~~
{: title="Example of YAML nodes that are not referenceable based on JSON data model." #example-unsupported-paths}

## Referencing a missing node

In this example the fragment `#/0` does not reference an existing node

~~~ example
0: "JSON Pointer `#/0` references a string mapping key."
~~~
{: title="Example of a JSON Pointer that does not reference an existing node." #example-missing-node}

## Representation graph with anchors and cyclic references

In this YAML document, the `#/foo/bar/baz` fragment identifier
traverses the representation graph and references the string `you`.
Moreover, the presence of a cyclic reference implies that
there are infinite fragment identifiers `#/foo/bat/../bat/bar`
referencing the `&anchor` node.

~~~ example
 anchor: &anchor
   baz: you
 foo: &foo
   bar: *anchor
   bat: *foo
~~~
{: title="Example of a cyclic references and alias nodes." #example-cyclic-graph}

Many YAML implementations will resolve
[the merge key "<<:"](https://yaml.org/type/merge.html) defined in YAML 1.1
in the representation graph.
This means that the fragment `#/book/author/given_name` references the string `Federico`
and that the fragment `#/book/<<` will not reference any existing node.

~~~ example
 %YAML 1.1
 ---
 # Many implementations use merge keys.
 the-viceroys: &the-viceroys
   title: The Viceroys
   author:
     given_name: Federico
     family_name: De Roberto
 book:
   <<: *the-viceroys
   title: The Illusion
~~~
{: title="Example of YAML merge keys." #example-merge-keys}


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
{: numbered="false" removeinrfc="true"}

Q: Why this document?
:  After all these years, we still lack a proper media-type for YAML.
   This has some security implications too
   (eg. wrt on identifying parsers or treat downloads)

Q: Why using alias nodes as fragment identifiers?
:  Alias nodes starts with `*`. This allow to distinguish
   a fragment identifier expressed as an alias node from
   one expressed in JSON Pointer {{JSON-POINTER}}
   which is expected to start with `/`.
   Moreover, since json-path {{I-D.ietf-jsonpath-base}} expressions
   start with `$`, this mechanism is even extensible that specification.

# Change Log
{: numbered="false" removeinrfc="true"}

RFC EDITOR PLEASE DELETE THIS SECTION.
