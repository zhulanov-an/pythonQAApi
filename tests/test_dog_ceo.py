import requests
from jsonschema import validate
'''
1. Тестирование REST сервиса 1
Написать минимум 5 тестов для REST API сервиса: https://dog.ceo/dog-api/.
Как минимум 2 из 5 должны использовать параметризацию.
Документация к API есть на сайте.
Тесты должны успешно проходить.
'''


def test_list_breeds():
    resp = requests.get("https://dog.ceo/api/breeds/list/all")
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
