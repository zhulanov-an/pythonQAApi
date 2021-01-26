import requests
import pytest


@pytest.fixture
def base_url(request):
    return request.config.getoption("--url")


@pytest.fixture
def expected_status(request):
    return request.config.getoption("--status_code")


def test_url_status(base_url, expected_status):
    response = requests.get(base_url)
    assert response.status_code == expected_status
