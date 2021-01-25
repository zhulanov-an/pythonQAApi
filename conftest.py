import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        default="https://ya.ru",
        help="This is request url"
    )

    parser.addoption(
        "--status_code",
        default="200",
        help="expected status code",
        type=int
    )


@pytest.fixture
def base_url(request):
    return request.config.getoption("--url")

@pytest.fixture
def expected_status(request):
    return request.config.getoption("--status_code")