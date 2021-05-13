import pytest


@pytest.fixture()
def base_url():
    base = 'https://api.openbrewerydb.org/new_mocked_api'

    def url_by(code):
        return f'{base}/{code}'

    return url_by
