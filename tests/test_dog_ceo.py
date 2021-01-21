import requests
from jsonschema import validate
import pytest

'''
1. Тестирование REST сервиса 1
Написать минимум 5 тестов для REST API сервиса: https://dog.ceo/dog-api/.
Как минимум 2 из 5 должны использовать параметризацию.
Документация к API есть на сайте.
Тесты должны успешно проходить.
'''


def breeds_lists():
    url = f"https://dog.ceo/api/breeds/list/all"

    resp = requests.get(url)
    assert resp.ok
    res = resp.json()
    return res["message"].keys()


def test_list_breeds(base_url):
    resp = requests.get(f"{base_url}/breeds/list/all")
    assert resp.ok

    schema = {
        "type": "object",
        "properties": {
            "message": {"type": "object"},
            "status": {"type": "string"}
        },
        "required": ["message", "status"]
    }

    validate(instance=resp.json(), schema=schema)


@pytest.mark.parametrize("subbreed, cnt", [("afghan", 4), ("blood", 2), ("english", 5)])
def test_random_subbreed(subbreed, cnt, base_url):
    url = f"{base_url}/breed/hound/{subbreed}/images/random/{cnt}"
    resp = requests.get(url)
    assert resp.ok

    res = resp.json()

    schema = {
        "type": "object",
        "properties": {
            "message": {"type": "array"},
            "status": {"type": "string"}
        },
        "required": ["message", "status"]
    }
    validate(instance=res, schema=schema)

    assert res["status"] == "success"
    assert len(res["message"]) == cnt
    for item in res["message"]:
        assert item.endswith((".jpg", ".jpeg"))


def test_schema_images_by_breed(base_url):
    resp = requests.get(f"{base_url}/breed/hound/images")
    assert resp.ok
    res = resp.json()

    schema = {
        "type": "object",
        "properties": {
            "message": {"type": "array"},
            "status": {"type": "string"}
        },
        "required": ["message", "status"]
    }

    validate(instance=res, schema=schema)


@pytest.mark.parametrize("breed", ["beagle", "akita", "borzoi"])
def test_unique_name_image_by_random_collection(breed, base_url):
    url = f"{base_url}/breed/{breed}/images/random"
    resp_1 = requests.get(url)
    resp_2 = requests.get(url)
    res_1 = resp_1.json()
    res_2 = resp_2.json()

    assert resp_1.ok
    assert resp_2.ok
    assert res_1["status"] == res_2["status"] == "success"
    assert res_1["message"] != res_2["message"]


@pytest.mark.parametrize("breed", breeds_lists())
def test_random_image_by_online_breed(breed, base_url):
    url = f"{base_url}/breed/{breed}/images/random"
    resp = requests.get(url)
    assert resp.ok
    res = resp.json()
    assert breed in res["message"]
    assert res["message"].endswith((".jpg", ".jpeg"))
    assert res["status"] == "success"
