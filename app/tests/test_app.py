from .common import *


def test_health_check(client):
    """ Test app health """
    response = client.get('/health')
    assert response.status_code == 200


def test_input_completeness_1(client):
    """ Missing lat and lng """
    response = client.get('/predict')
    assert response.status_code == 400


def test_input_completeness_2(client):
    """ Missing lng """
    response = client.get('/predict', query_string={'lat': -65})
    assert response.status_code == 422


def test_input_completeness_3(client):
    """ Missing lat """
    response = client.get('/predict', query_string={'lng': -65})
    assert response.status_code == 422


def test_input_completeness_4(client):
    """ Happy case (every parameter present) """
    response = client.get('/predict', query_string={'lng': -65, 'lat': -77})
    assert response.status_code != 422
    assert response.status_code != 404



def test_input_boundary_1(client):
    """ Lat out of bounds (lower) """
    response = client.get('/predict', query_string={'lng': -65, 'lat': -90.1})
    assert response.status_code == 422


def test_input_boundary_2(client):
    """ Lat out of bounds (upper) """
    response = client.get('/predict', query_string={'lng': -65, 'lat': 90.1})
    assert response.status_code == 422


def test_input_boundary_3(client):
    """ Lon out of bounds (lower) """
    response = client.get('/predict', query_string={'lng': -180.1, 'lat': -77})
    assert response.status_code == 422


def test_input_boundary_4(client):
    """ Lon out of bounds (upper) """
    response = client.get('/predict', query_string={'lng': 180.1, 'lat': -77})
    assert response.status_code == 422


def test_input_boundary_5(client):
    """ Lat in the boundary (upper) """
    response = client.get('/predict', query_string={'lng': -65, 'lat': 90})
    assert response.status_code != 422
    assert response.status_code != 404


def test_input_boundary_6(client):
    """ Lat in the boundary (lower) """
    response = client.get('/predict', query_string={'lng': -65, 'lat': -90})
    assert response.status_code != 422
    assert response.status_code != 404


def test_input_boundary_8(client):
    """ Lon in the boundary (lower) """
    response = client.get('/predict', query_string={'lng': -180, 'lat': -77})
    assert response.status_code != 422
    assert response.status_code != 404


def test_input_boundary_9(client):
    """ Lon in the boundary (upper) """
    response = client.get('/predict', query_string={'lng': 180, 'lat': -77})
    assert response.status_code != 422
    assert response.status_code != 404


def test_output_1(client):
    """ All the expected fields exist in the output """
    response = client.get('/predict', query_string=BaseInputs.campinas)
    expected_fields = ["latitude", "longitude", "n_grandes_concorrentes", "n_pequeno_varejista", "predicao"]
    assert response.status_code != 500
    assert response.status_code != 422
    for k in expected_fields:
        assert k in response.json

def test_output_2(client):
    """ The latitude and longitude fields are the same as passed in input """
    response = client.get('/predict', query_string=BaseInputs.campinas)
    assert response.status_code == 200
    assert response.json['latitude'] == BaseInputs.campinas['lat']
    assert response.json['longitude'] == BaseInputs.campinas['lng']
