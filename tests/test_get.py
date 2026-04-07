"""Test the module."""
import threading
from unittest.mock import patch

import pytest
import requests

from atcf_data_parser import get_dataframe


@pytest.mark.vcr()
def test_get_dataframe():
    """Test some simple math."""
    url = "https://ftp.nhc.noaa.gov/atcf/aid_public/aep182023.dat.gz"
    df = get_dataframe(url)
    assert len(df) > 100


def test_get_dataframe_timeout():
    """Test that a TimeoutError is raised when read_fwf takes too long."""
    url = "https://ftp.nhc.noaa.gov/atcf/aid_public/aep182023.dat.gz"
    block = threading.Event()

    def fake_head(*args, **kwargs):
        resp = requests.models.Response()
        resp.status_code = 200
        return resp

    def blocking_read_fwf(*args, **kwargs):
        block.wait()
        return None

    with (
        patch("atcf_data_parser.requests.head", side_effect=fake_head),
        patch("atcf_data_parser.requests.get"),
        patch("atcf_data_parser.get_gzipped_url", return_value=""),
        patch("atcf_data_parser.pd.read_fwf", side_effect=blocking_read_fwf),
    ):
        with pytest.raises(TimeoutError, match="timed out after 1 second"):
            get_dataframe(url, timeout=1)
    block.set()


def test_get_dataframe_bad_url():
    """Test that an HTTPError is raised when the URL returns a 404."""
    url = "https://ftp.nhc.noaa.gov/atcf/aid_public/nonexistent.dat.gz"

    def fake_head_404(*args, **kwargs):
        resp = requests.models.Response()
        resp.status_code = 404
        resp.url = url
        return resp

    with patch("atcf_data_parser.requests.head", side_effect=fake_head_404):
        with pytest.raises(requests.HTTPError):
            get_dataframe(url)
