# Roundtrip yaml/json.
from pathlib import Path
import yaml, json
import pytest
import logging
import abnf

testcases = yaml.safe_load(Path("yaml-json-interoperability.yaml").read_text())
fragment_identifier_testcases = yaml.safe_load(Path("yaml-fragment-identifiers.yaml").read_text())

log = logging.getLogger(__name__)


def json_safe_dump(d):
    return json.dumps(d, allow_nan=False)


@pytest.mark.parametrize(
    "testname,testcase,yaml_load",
    [
        (k, v, yaml_load)
        for (k, v) in testcases.items()
        if v.get("expected") == False
        for yaml_load in (yaml.safe_load, yaml.unsafe_load)
    ],
)
def test_unsupported_safe(testname, testcase, yaml_load):
    log.info(f"Running {testname}")
    data = testcase["data"]
    with pytest.raises((yaml.constructor.ConstructorError, TypeError, ValueError)) as e:
        ret = yaml_load(data)
        json_safe_dump(ret)
        ret_yaml = yaml.safe_dump(ret)
        if "!!python/" in ret_yaml:
            raise ValueError("Local tags in serialization")
        for tag in ("!!omap", "!!pairs"):
            if tag in data and tag not in ret_yaml:
                raise ValueError(f"Non-JSON type not preserved in round-trip: {tag}")
    if error_message := testcase.get("error"):
        assert e.match(error_message)


@pytest.mark.parametrize(
    "testname,testcase",
    [(k, v) for (k, v) in testcases.items() if v.get("expected") != False],
)
def test_supported(testname, testcase):
    log.info(f"Running {testname}")
    data = testcase["data"]
    ret = yaml.safe_load(data)
    assert testcase["expected"] == json_safe_dump(ret)


from urllib.parse import urlparse, urlsplit, urlunsplit
from urllib.parse import quote, unquote


def iri_to_uri(iri, encoding="utf-8"):
    "Takes a Unicode string that can contain an IRI and emits a URI."
    scheme, authority, path, query, frag = urlsplit(iri)
    scheme = scheme.encode(encoding)
    if ":" in authority:
        host, port = authority.split(":", 1)
        authority = host.encode("idna") + f":{port}".encode()
    else:
        authority = authority.encode(encoding)
    path = quote(path.encode(encoding), safe="/;%[]=:$&()+,!?*@'~")
    query = quote(query.encode(encoding), safe="/;%[]=:$&()+,!?*@'~")
    frag = quote(frag.encode(encoding), safe="/;%[]=:$&()+,!?*@'~")
    return urlunsplit(
        x.encode() if hasattr(x, "encode") else x
        for x in (scheme, authority, path, query, frag)
    )


@pytest.mark.parametrize(
    "alias_node",
    [
        "*foo",
        "*foo-bar-baz",
        "*però",
        "*però/fara",
        "*però/fara/perì",
        "/components/schemas/Person",
        "$.o.*",
    ],
)
def test_uri_alias_nodes(alias_node):
    """
    fragment syntax:
    fragment    = *( pchar / "/" / "?" )
    pchar         = unreserved / pct-encoded / sub-delims / ":" / "@"
    sub-delims    = "!" / "$" / "&" / "'" / "(" / ")"
                    / "*" / "+" / "," / ";" / "="
    pct-encoded   = "%" HEXDIG HEXDIG
    unreserved  = ALPHA / DIGIT / "-" / "." / "_" / "~"

    """
    s = "https://host.example:443/path.yaml#" + alias_node
    url2 = iri_to_uri(s)
    url = urlparse(url2)
    print(
        f'\n{{ "{alias_node}": {{ "iri": "{s}","url": "{url2.decode("""ascii""")}" }} }},'
    )
    fragment = unquote(url.fragment)
    print(fragment)


@pytest.mark.parametrize("testcase", [
    testcase for testcase in fragment_identifier_testcases["yaml-fragment-identifiers"]["data"]
    ])
def test_iri_full(testcase):
    ((alias_node, testcase),) = testcase.items()
    url = urlparse(testcase["url"])
    iri = urlparse(testcase["iri"])
    parsed_fragment = unquote(url.fragment)
    validate_uri_fragment(url.fragment)
    iri_fragment = iri.fragment
    assert parsed_fragment == iri_fragment


def validate_uri_fragment(uri_fragment):
    rules = """
    sub-delims    = "!" / "$" / "&" / "'" / "(" / ")" / "*" / "+" / "," / ";" / "="
    pct-encoded   = "%" HEXDIG HEXDIG
    unreserved  = ALPHA / DIGIT / "-" / "." / "_" / "~"
    pchar         = unreserved / pct-encoded / sub-delims / ":" / "@"
    fragment    = *( pchar / "/" / "?" )
    """
    for rule in rules.strip().splitlines():
        abnf.Rule.create(rule.strip())
    return abnf.Rule('fragment').parse_all(uri_fragment)