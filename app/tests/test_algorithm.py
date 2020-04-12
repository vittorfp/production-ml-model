import numpy as np
import pandas as pd
from .common import *

test_cases = pd.read_csv('./app/tests/test_resources/test_samples_1.0.csv')


def test_municipal_boundary_1(client):
    """ Point out of municipal boundary """
    response = client.get('/predict', query_string=BaseInputs.valid_outside)
    assert response.status_code != 500
    assert response.status_code == 400


def test_municipal_boundary_2(client):
    """ Point inside municipal boundary """
    response = client.get('/predict', query_string=BaseInputs.campinas)
    assert response.status_code != 400
    assert response.status_code != 500
    assert response.status_code == 200


@pytest.mark.parametrize("index,case", test_cases.iterrows())
def test_model_outputs_1(client, mocker, index, case):

    count = pd.DataFrame(case).T.drop(columns=['Unnamed: 0', 'latitude', 'longitude', 'tipo_POI', 'response'])
    count = count[sorted(count.columns)]
    mocker.patch('app.repository.data_repository.DataRepository.get_points_count', return_value=count)

    response = client.get('/predict', query_string={'lat': case.latitude, 'lng': case.longitude})

    assert response.status_code != 500
    assert response.status_code == 200
    assert response.json['latitude'] == case.latitude
    assert response.json['longitude'] == case.longitude
    assert response.json['n_grandes_concorrentes'] == case.concorrentes__grandes_redes
    assert response.json['n_pequeno_varejista'] == case.concorrentes__pequeno_varejista
    assert np.isclose(response.json['predicao'], case.response, atol=1e-8)
