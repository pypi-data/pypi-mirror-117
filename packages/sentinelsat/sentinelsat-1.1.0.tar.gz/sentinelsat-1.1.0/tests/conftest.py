import re
import threading
from datetime import datetime
from functools import reduce
from os import environ
from os.path import abspath, dirname, exists, isfile, join

import pytest
import yaml
from pytest_socket import disable_socket
from vcr import VCR

import sentinelsat
from sentinelsat import SentinelAPI, geojson_to_wkt, read_geojson
from .custom_serializer import BinaryContentSerializer

TESTS_DIR = dirname(abspath(__file__))
FIXTURES_DIR = join(TESTS_DIR, "fixtures")
CASSETTE_DIR = join(FIXTURES_DIR, "vcr_cassettes")


def pytest_runtest_setup(item):
    markers = {mark.name for mark in item.iter_markers()}
    if "pandas" in markers:
        pytest.importorskip("pandas")
    if "geopandas" in markers:
        pytest.importorskip("geopandas")

    if not markers.intersection({"scihub", "fast", "mock_api"}):
        pytest.fail("The test is missing a 'scihub', 'fast' or 'mock_api' marker")


def scrub_request(request):
    for header in ("Authorization", "Set-Cookie", "Cookie"):
        if header in request.headers:
            del request.headers[header]
    return request


def scrub_response(response):
    ignore = {
        x.lower()
        for x in [
            "Authorization",
            "Set-Cookie",
            "Cookie",
            "Date",
            "Expires",
            "Transfer-Encoding",
            "last-modified",
        ]
    }
    for header in list(response["headers"]):
        if (
            header.lower() in ignore
            or header.lower().startswith("access-control")
            or header.lower().startswith("x-")
        ):
            del response["headers"][header]
    return response


def scrub_string(string, replacement=b""):
    """Scrub a string from a VCR response body string"""

    def before_record_response(response):
        len_before = len(response["body"]["string"])
        response["body"]["string"] = re.sub(string, replacement, response["body"]["string"])
        len_diff = len(response["body"]["string"]) - len_before
        if "content-length" in response["headers"]:
            response["headers"]["content-length"] = [
                str(int(response["headers"]["content-length"][0]) + len_diff)
            ]
        return response

    return before_record_response


def chain(*funcs):
    def chained_call(arg):
        return reduce(lambda x, f: f(x), funcs, arg)

    return chained_call


# Configure pytest-vcr
@pytest.fixture(scope="module")
def vcr(vcr):
    def range_header_matcher(r1, r2):
        return r1.headers.get("Range", "") == r2.headers.get("Range", "")

    vcr.cassette_library_dir = CASSETTE_DIR
    vcr.path_transformer = VCR.ensure_suffix(".yaml")
    vcr.filter_headers = ["Set-Cookie"]
    vcr.before_record_request = scrub_request
    vcr.before_record_response = chain(
        scrub_response,
        scrub_string(rb"Request done in \S+ seconds.", b"Request done in ... seconds."),
        scrub_string(rb'"updated":"[^"]+"', b'"updated":"..."'),
        scrub_string(rb'totalResults":"\d{4,}"', b'totalResults":"10000"'),
        scrub_string(rb"of \d{4,} total results", b"of 10000 total results"),
        scrub_string(rb"&start=\d{4,}&rows=0", b"&start=10000&rows=0"),
    )
    vcr.decode_compressed_response = True
    vcr.register_serializer("custom", BinaryContentSerializer(CASSETTE_DIR))
    vcr.serializer = "custom"
    vcr.register_matcher("range_header", range_header_matcher)
    vcr.match_on = ["method", "range_header", "host", "port", "path", "query", "body"]
    return vcr


@pytest.fixture(scope="session")
def credentials(request):
    # local tests require environment variables `DHUS_USER` and `DHUS_PASSWORD`
    # for Travis CI they are set as encrypted environment variables and stored
    record_mode = request.config.getoption("--vcr-record")
    disable_vcr = request.config.getoption("--disable-vcr")
    if record_mode in ["none", None] and not disable_vcr:
        # Using VCR.py cassettes for pre-recorded query playback
        # Any network traffic will raise an exception
        disable_socket()
    elif "DHUS_USER" not in environ or "DHUS_PASSWORD" not in environ:
        raise ValueError(
            "Credentials must be set when --vcr-record is not none or --disable-vcr is used. "
            "Please set DHUS_USER and DHUS_PASSWORD environment variables."
        )

    return [environ.get("DHUS_USER"), environ.get("DHUS_PASSWORD")]


@pytest.fixture(scope="session")
def api_kwargs(credentials):
    user, password = credentials
    return dict(user=user, password=password, api_url="https://apihub.copernicus.eu/apihub/")


@pytest.fixture
def api(api_kwargs):
    return SentinelAPI(**api_kwargs)


@pytest.fixture(scope="session")
def fixture_path():
    return lambda filename: join(FIXTURES_DIR, filename)


@pytest.fixture(scope="session")
def read_fixture_file(fixture_path):
    def read_func(filename, mode="r"):
        with open(fixture_path(filename), mode) as f:
            return f.read()

    return read_func


@pytest.fixture(scope="session")
def read_yaml(fixture_path, read_fixture_file):
    def read_or_store(filename, result):
        path = fixture_path(filename)
        if not exists(path):
            # Store the expected result for future if the fixture file is missing
            with open(path, "w") as f:
                yaml.safe_dump(result, f)
        return yaml.safe_load(read_fixture_file(filename))

    return read_or_store


@pytest.fixture(scope="session")
def geojson_path():
    path = join(FIXTURES_DIR, "map.geojson")
    assert isfile(path)
    return path


@pytest.fixture(scope="session")
def geojson_string():
    string = """{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "properties": {},
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [
              -66.26953125,
              -8.05922962720018
            ],
            [
              -66.26953125,
              0.7031073524364909
            ],
            [
              -57.30468749999999,
              0.7031073524364909
            ],
            [
              -57.30468749999999,
              -8.05922962720018
            ],
            [
              -66.26953125,
              -8.05922962720018
            ]
          ]
        ]
      }
    }
  ]
}"""
    return string


@pytest.fixture(scope="session")
def wkt_string():
    string = (
        "POLYGON((-78.046875 46.377254205100286,-75.76171874999999 43.32517767999295,-71.279296875 "
        "46.55886030311717,-78.046875 46.377254205100286))"
    )
    return string


@pytest.fixture(scope="session")
def test_wkt(geojson_path):
    return geojson_to_wkt(read_geojson(geojson_path))


@pytest.fixture(scope="module")
def products(api_kwargs, vcr, test_wkt):
    """A fixture for tests that need some non-specific set of products as input."""
    with vcr.use_cassette("products_fixture", decode_compressed_response=False):
        api = SentinelAPI(**api_kwargs)
        products = api.query(test_wkt, ("20151219", "20151228"))
    assert len(products) > 20
    return products


@pytest.fixture(scope="module")
def raw_products(api_kwargs, vcr, test_wkt):
    """A fixture for tests that need some non-specific set of products in the form of a raw response as input."""
    with vcr.use_cassette("products_fixture", decode_compressed_response=False):
        api = SentinelAPI(**api_kwargs)
        raw_products = api._load_query(api.format_query(test_wkt, ("20151219", "20151228")))[0]
    return raw_products


def _get_smallest(api_kwargs, cassette, online, n=3):
    time_range = ("NOW-1MONTH", None) if online else (None, "20170101")
    odatas = []
    with cassette:
        api = SentinelAPI(**api_kwargs)
        products = api.query(date=time_range, size="/.+KB/", limit=15)
        for uuid in products:
            odata = api.get_product_odata(uuid)
            if odata["Online"] == online:
                odatas.append(odata)
                if len(odatas) == n:
                    break
    assert len(odatas) == n
    return odatas


@pytest.fixture(scope="module")
def smallest_online_products(api_kwargs, vcr):
    return _get_smallest(api_kwargs, vcr.use_cassette("smallest_online_products"), online=True)


@pytest.fixture(scope="module")
def smallest_archived_products(api_kwargs, vcr):
    return _get_smallest(api_kwargs, vcr.use_cassette("smallest_archived_products"), online=False)


@pytest.fixture(scope="module")
def quicklook_products(api_kwargs, vcr):
    ids = [
        "6b126ea4-fe27-440c-9a5c-686f386b7291",
        "1a9401bc-6986-4707-b38d-f6c29ca58c00",
        "54e6c4ad-6f4e-4fbf-b163-1719f60bfaeb",
    ]
    with vcr.use_cassette("quicklook_products"):
        api = SentinelAPI(**api_kwargs)
        odata = [api.get_product_odata(x) for x in ids]
    return odata


@pytest.fixture(scope="module")
def node_test_products(api_kwargs, vcr):
    with vcr.use_cassette("node_test_products"):
        api = SentinelAPI(**api_kwargs)
        products = api.query(date=("NOW-1MONTH", None), identifier="*IW_GRDH*", limit=3)
        odatas = [api.get_product_odata(x) for x in products]
        assert all(info["Online"] for info in odatas)
    return odatas


@pytest.fixture(scope="session")
def small_query():
    return dict(
        area="POLYGON((0 0,1 1,0 1,0 0))", date=(datetime(2015, 1, 1), datetime(2015, 1, 2))
    )


@pytest.fixture(scope="session")
def large_query():
    return dict(
        area="POLYGON((0 0,0 10,10 10,10 0,0 0))",
        date=(datetime(2015, 12, 1), datetime(2015, 12, 31)),
    )


@pytest.fixture(autouse=True)
def disable_waiting(monkeypatch):
    monkeypatch.setattr(sentinelsat.download, "_wait", lambda event, timeout: event.wait(0.001))
