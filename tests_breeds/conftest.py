import pytest
import requests

BASE_URL = "https://dog.ceo/api"

@pytest.fixture()
def base_url():
    return f"{BASE_URL}"


def pytest_generate_tests(metafunc):
    if "id" in metafunc.fixturenames:
        url = f"{BASE_URL}/breeds/list/all"
        resp = requests.get(url)

        assert resp.ok
        res = resp.json()
        breeds_lists =  res["message"].keys()
        return metafunc.parametrize("id", breeds_lists)
