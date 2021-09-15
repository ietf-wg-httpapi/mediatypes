---
title: The "id-" prefix for Digest Algorithms
abbrev:
docname: draft-polli-id-digest-algorithms-latest
category: std

ipr: trust200902
area: General
workgroup:
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

informative:

--- abstract

This document defines
the "id-" prefix for digest-algorithms
used in the Digest HTTP field.
This prefix explicits that the value of the digest-algorithm
is independent from Content-Encoding.

--- note_Note_to_Readers

*RFC EDITOR: please remove this section before publication*

Discussion of this draft takes place on the HTTP working group mailing list
(ietf-http-wg@w3.org), which is archived at
<https://lists.w3.org/Archives/Public/ietf-http-wg/>.

The source code and issues list for this draft can be found at
<https://github.com/ioggstream/draft-polli-id-digest-algorithms>.


--- middle

# Introduction

The {{!DIGEST=I-D.ietf-httpbis-digest-headers}} defines a way to convey a checksum of a representation-data
as specified in {{!SEMANTICS=RFC7231}}.

As the representation data depends on the value of `Content-Encoding`, it is useful
to convey the checksum value of a representation without any content-coding applied.

This proposal introduces the "id-" prefix
to specify that the provided digest-algorithm value is computed on the representation-data
without any content-coding applied.

## Notational Conventions
{::boilerplate bcp14+}

This document uses the Augmented BNF defined in {{!RFC5234}} and updated
by {{!RFC7405}}.

The definitions "representation", "selected representation", "representation
data", "representation metadata", and "payload body" in this document are to be
interpreted as described in {{SEMANTICS}}.

The definitions "digest-algorithm" and "representation-data-digest" in this document
are to be interpreted as described in {{DIGEST}}.


# The "id-" prefix for digest-algorithms

A digest-algorithm to be registered within the
[HTTP Digest Algorithm Values](https://www.iana.org/assignments/http-dig-alg/http-dig-alg.xhtml)
MUST NOT start with the string "id-".

The following two examples show two digest-algorithm names that cannot be registered

~~~ example

   id-crc32c
   id-adler32
~~~


For every digest-algorithm registered in the 
[HTTP Digest Algorithm Values](https://www.iana.org/assignments/http-dig-alg/http-dig-alg.xhtml)
the associate "id-" digest-algorithm has the following properties:

  * the checksum is computed on the representation-data of the resource
    when no content coding is applied;
  * the checksum is computed according to the original digest-algorithm
    Description field, and uses the same encoding of the original digest-algorithm.

This definition is compatible, and thus extends, the definition
of the "id-sha-256" and "id-sha-512" digest-algorithms
contained in Section X of {{DIGEST}}.


# Security Considerations

## Disclosure of encrypted content

Like the "id-sha-256" digest-algoritm defined in {{DIGEST}}
if the content-coding provides encryption features,
sending the checksum of unencoded representation can
disclose information.

# IANA Considerations

## TBD how to reserve "id-" prefix?

# Examples

## The id-crc32c digest-algorithm

The following request conveys a brotli encoded
json object

~~~ example
{"hello": "world"}
~~~

The `Digest` computed using the "crc32c" digest-algorithm present in 
[HTTP Digest Algorithm Values](https://www.iana.org/assignments/http-dig-alg/http-dig-alg.xhtml)
is content-coding aware,
while its associated "id-" digest-algorithm is not "id-crc32c" 

~~~ example

POST /data HTTP/1.1
Content-Type: application/json
Content-Encoding: br
Digest: id-crc32c=43794720, crc32c=DB329237

CwGAZG9nAw==
~~~



--- back

# Acknowledgements

This specification was born from a thread created by James Manger
and the subsequent discussion here https://github.com/httpwg/http-extensions/issues/885.

# FAQ
{: numbered="false"}

Q: Question 1
:  Answer 1

# Code Samples
{:numbered="false"}

_RFC Editor: Please remove this section before publication._

How can I generate and validate the `Digest` values shown in the examples
throughout this document?

The following python3 code can be used to generate digests for json objects
using crc32c algorithm. Note that these are formatted as
base64. This function could be adapted to other algorithms and should take into
account their specific formatting rules.

~~~
import base64, json, brotli, crc32c

identity = lambda x: x

def digest(item, content_coding=identity, algorithm=crc32c.crc32c):
    json_bytes = json.dumps(item).encode()
    content_encoded = content_coding(json_bytes)
    checksum = algorithm(content_encoded)
    # encode result has uppercase hex
    return hex(checksum)[2:].upper()


item = {"hello": "world"}

print("crc32c digest value for a br-coded representation: ",
    digest(item, content_coding=brotli.compress)
)

print("id-crc32c digest value for a br-coded representation: ",
    digest(item, content_coding=identity)
)

~~~

# Change Log
{: numbered="false"}

RFC EDITOR PLEASE DELETE THIS SECTION.
