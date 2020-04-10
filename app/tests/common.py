import pytest


@pytest.fixture
def app():
    from app import app
    return app


class BaseInputs:
    campinas = {'lng': -47.0626, 'lat': -22.9099}
    valid_outside = {'lng': -65, 'lat': -77}

