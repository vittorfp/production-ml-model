from .common import *


def test_municipal_boundary_1(client):
    """ Point out of municipal boundary """
    response = client.get('/health', query_string={'lon': -65, 'lat': -77})
    assert response.status_code == 400


def test_municipal_boundary_2(client):
    """ Point inside municipal boundary """
    response = client.get('/health', query_string={'lon': -65, 'lat': -77})
    assert response.status_code != 400
