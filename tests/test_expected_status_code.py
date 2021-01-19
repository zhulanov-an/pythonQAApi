import requests


def test_url_status(base_url, expected_status):
    response = requests.get(base_url)
    assert response.status_code == expected_status
