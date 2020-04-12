import pytest


@pytest.fixture
def app(mocker):
    mocker.patch('psycopg2.connect', return_value=True)
    mocker.patch('app.repository.data_repository.DataRepository.get_nearby_points', return_value=[])

    from app import app
    app.config['DEBUG'] = True
    return app


class BaseInputs:
    campinas = {'lng': -47.0626, 'lat': -22.9099}
    valid_outside = {'lng': -65, 'lat': -77}

