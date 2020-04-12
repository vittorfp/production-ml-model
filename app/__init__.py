from flask import Flask
from .util import JSONEncoder
from flask import jsonify, request
from app.schema import location_schema
from app.util import validate_input
from app.model.invoice_model import InvoiceModel
from app.repository.data_repository import DataRepository
from app.repository.geoprocessing_helper import GeoHelper
from app.model.city_checker import CityChecker


app = Flask(__name__)
app.json_encoder = JSONEncoder

geo = GeoHelper(radius=1000)
city = CityChecker(file='./app/resources/campinas.wkt')
model = InvoiceModel(file='./app/model/model_campifarma.pickle')


@app.route('/predict', methods=['GET'])
def predict():
    input_data = validate_input(location_schema, dict(request.args))
    if isinstance(input_data, tuple):
        return input_data

    if not city.is_inside(**input_data):
        message = "Ponto enviado não se encontra no municipio de campinas."
        app.logger.error(message)
        return jsonify({'error': message}), 400

    isocota = geo.get_isocota(**input_data)

    db = DataRepository()
    data = db.get_points_count(isocota)

    try:
        response = dict(
            latitude=input_data['lat'],
            longitude=input_data['lng'],
            predicao=model.predict(data)[0],
            n_pequeno_varejista=int(data['concorrentes__pequeno_varejista'].values[0]),
            n_grandes_concorrentes=int(data['concorrentes__grandes_redes'].values[0])
        )
    except Exception as e:
        app.logger.error(e)
        return jsonify({'error': e}), 500

    return jsonify(response), 200


@app.route('/health')
def health_check():
    """
        Route to be used as health-check endpoint for the ECS target group.
    """
    return jsonify({"status": "OK"})
