import pytest
from jsonschema import validate
import requests


def resp_to_dict(url):
    resp = requests.get(url)
    return resp.json()


@pytest.mark.parametrize("id, userid", [(1, 1), (2, 1), (3, 1), (4, 1)])
def test_get_posts_by_id(base_url, id, userid):
    url = f"{base_url}/posts/{id}"
    resp = resp_to_dict(url)
    assert resp["id"] == id
    assert resp["userId"] == userid


@pytest.mark.parametrize("id", [1, 2, 3, 4, 5])
def test_get_users_by_id(base_url, id):
    url = f"{base_url}/users/{id}"
    resp = resp_to_dict(url)
    assert resp["id"] == id


@pytest.mark.parametrize("id", [1, 2, 3, 4, 5])
def test_get_todos_by_id(base_url, id):
    url = f"{base_url}/todos/{id}"
    resp = resp_to_dict(url)
    assert resp["id"] == id


def test_posts_schema(base_url):
    url = f"{base_url}/posts"
    resp = resp_to_dict(url)

    schema = {
        "type": "array",
        "items": {
            "type": "object",
        }
    }

    validate(resp, schema)


def test_todos_schema(base_url):
    url = f"{base_url}/todos"
    resp = resp_to_dict(url)

    schema = {
        "type": "array",
        "items": {
            "type": "object",
        }
    }

    validate(resp, schema)
