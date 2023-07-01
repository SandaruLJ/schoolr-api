"""Test module for health checking endpoints"""

from http import HTTPStatus

from schoolr_api.common.constants import PREFIX


def test_health(client):
    """Test health endpoint."""
    response = client.get(f'{PREFIX}/health')

    assert response.status_code == HTTPStatus.OK
    assert response.json == {'message': 'Healthy'}
