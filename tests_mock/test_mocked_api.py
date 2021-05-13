import json
from unittest.mock import patch
from requests.models import Response
import requests


def mocked_request(*args, **kwargs):
    response_content_200 = json.dumps({'api_mock': 'success'})
    response_content_400 = json.dumps({'api_mock': 'client_error'})
    response_content_500 = json.dumps({'api_mock': 'server_error'})
    response_content_other = json.dumps({'api_mock': 'other'})
    request_url: str = kwargs.get('url', None)
    response = Response()
    response.headers['Content-Type'] = 'application/json; charset=utf-8'

    codes = tuple(str(i) for i in range(100, 550))
    if request_url.endswith(codes):
        code = int(request_url[-3:])
        response.status_code = code
        if 200 <= code < 300:
            response._content = str.encode(response_content_200)
        elif 400 <= code < 500:
            response._content = str.encode(response_content_400)
        elif code >= 500:
            response._content = str.encode(response_content_500)
        else:
            response._content = str.encode(response_content_other)
    return response


@patch('requests.get', side_effect=mocked_request)
def test_new_api_get_200(mock_requests, base_url):
    response = requests.get(url=base_url(200))
    assert response.status_code == 200
    assert response.headers.get('Content-Type')
    assert response.headers['Content-Type'] == 'application/json; charset=utf-8'
    assert response.json() == {'api_mock': 'success'}


@patch('requests.put', side_effect=mocked_request)
def test_new_api_put_400(mock_requests, base_url):
    response = requests.put(url=base_url(400))
    assert response.status_code == 400
    assert response.headers.get('Content-Type')
    assert response.headers['Content-Type'] == 'application/json; charset=utf-8'
    assert response.json() == {'api_mock': 'client_error'}


@patch('requests.post', side_effect=mocked_request)
def test_new_api_post_500(mock_requests, base_url):
    response = requests.post(url=base_url(500))
    assert response.status_code == 500
    assert response.headers.get('Content-Type')
    assert response.headers['Content-Type'] == 'application/json; charset=utf-8'
    assert response.json() == {'api_mock': 'server_error'}


@patch('requests.patch', side_effect=mocked_request)
def test_new_api_patch_other(mock_requests, base_url):
    response = requests.patch(url=base_url(302))
    assert response.status_code == 302
    assert response.headers.get('Content-Type')
    assert response.headers['Content-Type'] == 'application/json; charset=utf-8'
    assert response.json() == {'api_mock': 'other'}
