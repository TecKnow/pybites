from ast import parse
import os
from pathlib import Path
from ipaddress import IPv4Network
from urllib.request import urlretrieve

from pprint import pprint

import pytest

from ips import (ServiceIPRange, parse_ipv4_service_ranges,
                 get_aws_service_range)

URL = "https://bites-data.s3.us-east-2.amazonaws.com/ip-ranges.json"
TMP = os.getenv("TMP", "/tmp")
PATH = Path(TMP, "ip-ranges.json")
IP = IPv4Network('192.0.2.8/29')


@pytest.fixture(scope='module')
def json_file():
    """Import data into tmp folder"""
    urlretrieve(URL, PATH)
    return PATH


# write your pytest code ...

@pytest.fixture(scope='module')
def range_list(json_file):
    print("foo")
    return parse_ipv4_service_ranges(json_file)

def test_base(range_list):
    assert len(range_list) == 1886

def test_ServiceIPRange_str(range_list):
    assert str(range_list[0]) == '13.248.118.0/24 is allocated to the AMAZON service in the eu-west-1 region'

def test_unrouteable_address(range_list):
    assert get_aws_service_range("192.168.1.1", range_list) == list()

def test_invalid_address(range_list):
     with pytest.raises(ValueError, match="Address must be a valid IPv4 address"):
        get_aws_service_range("8.8.8.266", range_list)
    