# Roundtrip yaml/json.
from graphql import ValidationRule
from path import Path
import yaml, json
import pytest


testcases = yaml.safe_load(Path("yaml-json-interoperability.yaml").read_text())

import logging

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
