import pytest
import requests
from jsonschema import validate


def test_schema_list_of_breweries(base_url):
    url = f"{base_url}/breweries"
    resp = requests.get(url)
    assert resp.ok

    jresp = resp.json()

    schema = {
        "type": "array",
        "items": {
            "type": "object",
        }
    }

    validate(jresp, schema)


@pytest.mark.parametrize("id", [5494, 5495, 530])
def test_get_id_of_a_single_brewery(base_url, id):
    url = f"{base_url}/breweries/{id}"
    resp = requests.get(url)
    assert resp.ok

    jresp = resp.json()
    assert jresp["id"] == id


@pytest.mark.parametrize("term", ["Mash monkeys brewing Company", "6th and La Brea"])
def test_search_for_breweries_based_on_a_search_term(base_url, term):
    url = f"{base_url}/breweries/search?query={term}"
    resp = requests.get(url)
    assert resp.ok

    jresp = resp.json()
    for item in jresp:
        assert term.lower() in item["name"].lower()


@pytest.mark.parametrize("term", ["dog", "cat"])
def test_autocomplete(base_url, term):
    url = f"{base_url}/breweries/autocomplete?query = {term}"
    resp = requests.get(url)
    assert resp.ok

    jresp = resp.json()
    for item in jresp:
        assert term.lower() in item["name"].lower()


@pytest.mark.parametrize("post", ["44107-4840", "44107 - 4020", "44107 - 4020"])
def test_filter_by_postal(base_url, post):
    url = f"{base_url}/breweries?by_postal={post}"
    resp = requests.get(url)
    assert resp.ok

    jresp = resp.json()
    for item in jresp:
        assert item["postal_code"] == post
