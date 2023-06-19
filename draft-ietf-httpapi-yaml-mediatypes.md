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
venue:
  group: HTTPAPI
  type: Working Group
  home: https://datatracker.ietf.org/wg/httpapi/about/
  mail: httpapi@ietf.org
  arch: https://mailarchive.ietf.org/arch/browse/httpapi/
  repo: https://github.com/ietf-wg-httpapi/mediatypes/labels/yaml
github-issue-label: yaml

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
on the IANA Media Types registry,
intended to be used to identify document components
serialized according to the YAML specification.

--- middle

# Introduction

YAML [YAML] is a data serialization format
that is capable of conveying one or multiple
documents in a single presentation stream
(e.g., a file or a network resource).
It is widely used on the Internet,
including in the API sector (e.g., see [OAS]),
but a corresponding media type and structured syntax suffix had not previously been registered by IANA.

To increase interoperability when exchanging YAML streams,
and leverage content negotiation mechanisms when exchanging
YAML resources,
this specification
registers the `application/yaml` media type
and the `+yaml` structured syntax suffix {{!MEDIATYPE=RFC6838}}.

Moreover, it provides security considerations
and interoperability considerations related to [YAML],
including its relation with {{!JSON=RFC8259}}.

## Notational Conventions

{::boilerplate bcp14+}

The terms  "content", "content negotiation", "resource",
and "user agent"
in this document are to be interpreted as in {{!HTTP=RFC9110}}.

The terms "fragment" and "fragment identifier"
in this document are to be interpreted as in {{!URI=RFC3986}}.

The terms "presentation", "stream", "YAML document", "representation graph", "tag",
"serialization detail",
"node", "alias node", "anchor" and "anchor name"
in this document are to be interpreted as in [YAML].

Figures containing YAML code always start with
the "%YAML 1.2" directive to improve readability.

## Fragment identification {#application-yaml-fragment}

A fragment identifies a node in a stream.

A fragment identifier starting with "*"
is to be interpreted as a YAML alias node (see {{fragment-alias-node}}).

For single-document YAML streams,
a fragment identifier that is empty
or that starts with "/"
is to be interpreted as a JSON Pointer {{JSON-POINTER}}
and is evaluated on the YAML representation graph,
walking through alias nodes;
in particular, the empty fragment identifier
references the root node.
This syntax can only reference the YAML nodes that are
on a path that is made up of nodes interoperable with
the JSON data model (see {{int-yaml-and-json}}).

A fragment identifier is not guaranteed to reference an existing node.
Therefore, applications SHOULD define how an unresolved alias node
ought to be handled.

### Fragment identification via alias nodes {#fragment-alias-node}

This section describes how to use
alias nodes (see Section 3.2.2.2 and 7.1 of [YAML])
as fragment identifiers to designate nodes.

A YAML alias node can be represented in a URI fragment identifier
by encoding it into bytes using UTF-8 {{!UTF-8=RFC3629}},
but percent-encoding of those characters is not allowed by the fragment rule
in {{Section 3.5 of URI}}.

If multiple nodes would match a fragment identifier,
the first occurrence of such match is selected.

Users concerned with interoperability of fragment identifiers:

- SHOULD limit alias nodes to a set of characters
  that do not require encoding
  to be expressed as URI fragment identifiers:
  this is generally possible since
  anchor names are a serialization detail;
- SHOULD NOT use alias nodes that match multiple nodes.

In the example resource below, the relative reference (see {{Section 4.2 of URI}}) `file.yaml#*foo`
identifies the first alias node `*foo` pointing to the node with value `scalar`
and not the one in the second document;
whereas
the relative reference `file.yaml#*document_2` identifies the root node
of the second document `{ one: [a, sequence]}`.

~~~ example
 %YAML 1.2
 ---
 one: &foo scalar
 two: &bar
   - some
   - sequence
   - items
 ...
 %YAML 1.2
 ---
 &document_2
 one: &foo [a, sequence]
~~~
{: title="A YAML stream containing two YAML documents." }

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
: N/A

<!-- RFC 6838:
   "N/A", written exactly that way, can be used in any field if desired
   to emphasize the fact that it does not apply or that the question was
   not omitted by accident.  Do not use 'none' or other words that could
   be mistaken for a response.
  -->

Optional parameters:
: N/A; unrecognized parameters should be ignored

Encoding considerations:
: binary

Security considerations:
: see {{security-considerations}} of this document

Interoperability considerations:
: see {{interoperability-considerations}} of this document

Published specification:
: [YAML], this document

Applications that use this media type:
: Applications that need a human-friendly, cross language, Unicode
  based data serialization language designed around the common native
  data types of dynamic programming languages.

Fragment identifier considerations:
: See {{application-yaml-fragment}} of this document

Additional information:

- Deprecated alias names for this type:  application/x-yaml, text/yaml, text/x-yaml.
  These names are used, but not registered.

- Magic number(s)  N/A

- File extension(s): "yaml" (preferred), "yml". See {{int-yaml-filename-extension}} of this document.

- Macintosh file type code(s):  N/A

- Windows Clipboard Name: YAML

Person and email address to contact for further information:
: See the Authors' Addresses section of this document.

Intended usage:
: COMMON

Restrictions on usage:
: None.

Author:
: See the Authors' Addresses section of this document.


Change controller:
: IETF


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
  :  [YAML], this document

  Encoding considerations:
  : Same as "application/yaml"

  Fragment identifier considerations:
  : Differently from `application/yaml`,
    there is no fragment identification syntax defined
    for +yaml.

    A specific `xxx/yyy+yaml` media type
    needs to define the syntax and semantics for fragment identifiers
    because the ones defined for "application/yaml"
    do not apply unless explicitly expressed.

  Interoperability considerations:
  : Same as "application/yaml"

  Security considerations:
  : Same as "application/yaml"

  Contact:
  : httpapi@ietf.org or art@ietf.org

  Author:
  : See the Authors' Addresses section of this document


  Change controller:
  :  IETF

# Interoperability Considerations

## YAML is an Evolving Language {#int-yaml-evolving}

YAML is an evolving language and, over time,
some features have been added and others removed.

This [YAML] media type registration is independent of YAML version.
This allows content negotiation of version-independent YAML resources.

Implementers concerned about features related to a specific YAML version
can specify it in YAML documents using the `%YAML` directive
(see Section 6.8.1 of [YAML]).

## YAML streams {#int-yaml-streams}

A YAML stream can contain zero or more YAML documents.

When receiving a multi-document stream,
an application that only expects one-document streams,
ought to signal an error instead of ignoring the extra documents.

Current implementations consider different documents in a stream independent,
similarly to JSON Text Sequences (see {{?RFC7464}});
elements such as anchors are not guaranteed to be referenceable
across different documents.

## Filename extension {#int-yaml-filename-extension}

The "yaml" filename extension is the preferred one;
it is the most popular and widely used on the web.
The "yml" filename extension is still used.
The simultaneous usage of two filename extensions in the same context
might cause interoperability issues
(e.g., when both a "config.yaml" and a "config.yml" are present).

## YAML and JSON {#int-yaml-and-json}

When using flow collection styles (see Section 7.4 of [YAML])
a YAML document could look like JSON [JSON],
thus similar interoperability considerations apply.

When using YAML as a more efficient format
to serialize information intended to be consumed as JSON,
information not reflected in the representation graph
and classified as presentation or serialization detail
(see Section 3.2 of [YAML]) can be discarded.
This includes comments (see Section 3.2.3.3 of [YAML]),
directives, and alias nodes (see Section 7.1 of [YAML])
that do not have a JSON counterpart.

~~~ example
 %YAML 1.2
 ---
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
issues with {{JSON}}:

- multi-document YAML streams;
- non UTF-8 encoding. Before encoding YAML streams in UTF-16 or UTF-32,
  it is important to note that {{Section 8.1 of JSON}} mandates the use of UTF-8
  when exchanging JSON texts between systems that are not part of a closed ecosystem,
  and that Section 5.2 of [YAML] recommends the use of UTF-8;
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
   [0, 1]: a sequence
   ? {k: v}
   : a map
 ---
 non-json-keys:
   !date 2020-01-01: a timestamp
 non-json-value: !date 2020-01-01
 ...
~~~
{: title="Example of mapping keys and values not supported in JSON in a multi-document YAML stream" #example-unsupported-keys}

## Fragment identifiers {#int-fragment}

To allow fragment identifiers to traverse alias nodes,
the YAML representation graph needs to be generated before the fragment identifier evaluation.
It is important that this evaluation will not cause the issues mentioned in {{int-yaml-and-json}}
and in [Security considerations](#security-considerations) such as infinite loops and unexpected code execution.

Implementers need to consider that the YAML version and supported features (e.g., merge keys)
can affect the generation of the representation graph (see {{example-merge-keys}}).

In {{application-yaml}}, this document extends the use of specifications based on
the JSON data model with support for YAML fragment identifiers.
This is to improve the interoperability of already consolidated practices,
such as the one of writing [OpenAPI documents](#OAS) in YAML.

{{ex-fragid}} provides a non-exhaustive list of examples that could help
understand interoperability issues related to fragment identifiers.

# Security Considerations

Security requirements for both media type and media type suffix
registrations are discussed in Section 4.6 of {{MEDIATYPE}}.

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
An implementation that treats them as simple trees
risks going into an infinite loop while traversing the YAML representation graph.
This can happen:

- when trying to serialize it as JSON;
- or when searching/identifying nodes using specifications based on the JSON data model (e.g., {{JSON-POINTER}}).

~~~ yaml
 %YAML 1.2
 ---
 x: &x
   y: *x
~~~
{: title="A cyclic document" #example-yaml-cyclic}

Even if a representation graph is not cyclic, treating it as a simple tree could lead to improper behaviors
(such as the "billion laughs"
or "Exponential Entity Expansion" problem).

~~~ yaml
 %YAML 1.2
 ---
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


## YAML streams

Incremental parsing and processing of a YAML stream can produce partial results
and later indicate failure to parse the remainder of the stream;
to prevent partial processing, implementers might prefer validating and processing all the documents in a stream at the same time.

Repeated parsing and re-encoding of a YAML stream can result
in the addition or removal of document delimiters (e.g., `---` or `...`)
as well as the modification of anchor names and other serialization details,
which can break signature validation.

## Expressing booleans

Section 10.3.2 of [YAML] specifies that only the scalars matching the
regular expression `true|True|TRUE|false|False|FALSE` are interpreted as booleans.
Older YAML versions were more tolerant (e.g., intepreting `no` and `n` as `false`,
and `yes` and `y` as `true`).
When the older syntax is used, a YAML implementation could then interpret
`insecure: n` as `insecure: "n"` instead of `insecure: false`.
To avoid these issues, express booleans only using the syntax defined
in Section 10.3.2 of [YAML].

# IANA Considerations

This specification defines the following new Internet media type {{MEDIATYPE}}.

IANA is asked to update the "Media Types" registry at <https://www.iana.org/assignments/media-types>
with the registration information provided in the section below.

|--------------------------------------|---------------------------------------------|
| Media Type                           | Registration information section            |
|--------------------------------------|---------------------------------------------|
| application/yaml                     | {{application-yaml}} of this document       |
|--------------------------------------|---------------------------------------------|

IANA is asked to update the "Structured Syntax Suffixes" registry at <https://www.iana.org/assignments/media-type-structured-suffix>
with the registration information provided in the section below.

|--------------------------|------------------------------------------|
| Suffix                   | Registration information section         |
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
 %YAML 1.2
 ---
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
 %YAML 1.2
 ---
 anchor: &anchor
   baz: you
 foo: &foo
   bar: *anchor
   bat: *foo
~~~
{: title="Example of a cyclic reference and alias nodes." #example-cyclic-graph}

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
{: numbered="false"}

Thanks to Erik Wilde and David Biesack for being the initial contributors of this specification,
and to Darrel Miller and Rich Salz for their support during the adoption phase.

In addition to the people above, this document owes a lot to the extensive discussion inside
and outside the HTTPAPI workgroup.
The following contributors have helped improve this specification by
opening pull requests, reporting bugs, asking smart questions,
drafting or reviewing text, and evaluating open issues:

Tina (tinita) Müller,
Ben Hutton,
Carsten Bormann,
Manu Sporny
and Jason Desrosiers.

# FAQ
{: numbered="false" removeinrfc="true"}

Q: Why this document?
:  After all these years, we still lack a proper media-type for YAML.
   This has some security implications too
   (eg. wrt on identifying parsers or treat downloads)

Q: Why using alias nodes as fragment identifiers?
:  Alias nodes are a native YAML feature that allows
   addressing any node in a YAML document.
   Since YAML is not limited to string keywords,
   not all nodes are addressable using JSON Pointers.
   Alias nodes are thus the natural choice for fragment identifiers
   {{application-yaml-fragment}}.

Q: Why not use plain names for alias nodes? Why not define plain names?
:  Using plain name fragments could have
   limited the ability of future xxx+yaml
   media types to define their plain name fragments.
   Moreover, alias nodes starts with `*` so we found no reason
   to strip it when using them in fragments.

   Preserving `*` had another positive result:
   it allows distinguishing
   a fragment identifier expressed as an alias node from
   one expressed in other formats.
   In this document we included JSON Pointer {{JSON-POINTER}}
   which is expected to start with `/`.
   Moreover, since JSON Path {{I-D.ietf-jsonpath-base}} expressions
   start with `$`, this mechanism can be extended to JSON Path too.

Q: Why not just use JSON Pointer as the primary fragment identifier?
:  Fragment identifiers in YAML always reference
   YAML representation graph nodes.
   JSON Pointer can only rely on string keywords so
   it is not able to reference a generic node in the
   representation graph.

   Since JSON Pointer is a specification unrelated to YAML,
   we decided to isolate the impacts of changes in JSON Pointer
   on YAML fragments:
   only fragments starting with "/" are "delegated" to an external spec,
   and if {{JSON-POINTER}} changes, it will only affect fragments starting with "/".

   The current behaviour for empty fragments is the same
   for both JSON Pointer and alias nodes.
   Incidentally, it's the only sensible behaviour independently of {{JSON-POINTER}}.

Q: Why describe the YAML/JSON so closely?
:  In the context of Web APIs, YAML is widely used as a more compact way to serialize
   content inteded to be consumed according to the JSON data model.
   Typical examples are OpenAPI specifications and Kubernetes manifest files,
   that can be serialized in both formats.
   The YAML media type registration I-D is a spin-off and a building block
   for the OpenAPI specification media type registration.
   The YAML/JSON section aims at clarifying what developers should expect when using YAML
   instead of JSON, and its content arose from common mistakes and FAQs.

   Please note that we are not imposing any normative restriction on YAML streams;
   this is because YAML is defined outside this document.
   Instead, we only provide Interoperability and Security considerations that,
   by their nature, are not normative.

Q: Do we forbid using non-UTF-8 YAML serialization?
:  No. Since {{JSON}} recommends UTF-8 in interoperability context
   we suggest that using UTF-8 is an interoperable behavior.
   This is aligned with Section 5.2 of [YAML] that explicitly
   recommends UTF-8.

Q: Why media type registration information is outside the IANA Considerations?
:  We decided to follow the style adopted in {{HTTP}} where
   the IANA Considerations in {{Section 18.8 of HTTP}}
   references the `multipart/byteranges` media type registration form
   contained in the specification body {{Section 14.6 of HTTP}}.

# Change Log
{: numbered="false" removeinrfc="true"}

## Since draft-ietf-httpapi-yaml-mediatypes-02
{: numbered="false"}

* clarification on fragment identifiers #50.


## Since draft-ietf-httpapi-yaml-mediatypes-01
{: numbered="false"}

* application/yaml fragment identifiers compatible with JSON Pointer #41 (#47).
