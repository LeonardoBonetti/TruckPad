from flask import Flask, jsonify, abort, make_response, request
from flask_mysqldb import MySQL

from app.dao import DriverDao, ItinerarieDao
from app.models import Driver, Itinerarie, ItinerariesGroupedReport
from app.gmaps import Address
from app.schema_validation import (
    DriverSchema, DriversSchema, ItinerarieSchema, FinishItinerarie, GetItinerariesSchema, GetGroupedItinerariesSchema
)
from app.helpers import str_to_bool

app = Flask(__name__)
app.config.from_pyfile('config.py')
db = MySQL(app)

driver_dao = DriverDao(db)
itinerarie_dao = ItinerarieDao(db)

driver_schema = DriverSchema()
get_drivers_schema = DriversSchema()
itinerarie_schema = ItinerarieSchema()
finish_itinerarie_schema = FinishItinerarie()
get_itineraries_schema = GetItinerariesSchema()
get_grouped_itineraries_schema = GetGroupedItinerariesSchema()


# Validado Marshmallow
@app.route('/api/v1.0/drivers', methods=['GET'])
def get_drivers():
    errors = get_drivers_schema.validate(request.args)
    if errors:
        return make_response(
            jsonify({'return_message': 'There is some erros in your request see errors_field', 'errors_field': errors}),
            400)

    has_own_vehicle = str_to_bool(request.args.get('own_vehicle', None))

    drivers_json = []
    for driver in driver_dao.list_drivers(has_own_vehicle):
        drivers_json.append(driver.to_json())
    return jsonify({'meta': {'total_drivers': drivers_json.__len__()}, 'drivers': drivers_json}), 200


# Validado
@app.route('/api/v1.0/drivers/<driver_id>', methods=['GET'])
def get_driver(driver_id):
    if not str.isdigit(driver_id):
        return make_response(jsonify({'return_message': 'driver_id must be a integer number'}), 400)

    driver = driver_dao.get_driver_by_id(driver_id)
    if driver:
        return jsonify({'driver': driver.to_json()}), 200
    else:
        abort(404, {'message': 'Driver do not exist'})


# Validado Marshmallow
@app.route('/api/v1.0/drivers', methods=['POST'])
def register_driver():
    if request.get_json() is None:
        return make_response(jsonify({'return_message': 'JSON Object not found'}), 400)

    errors = driver_schema.validate(request.get_json())
    if errors:
        return make_response(
            jsonify({'return_message': 'There is some erros in your request see errors_field', 'errors_field': errors}),
            400)

    request_json = request.get_json()
    driver = Driver(
        request_json.get('name', None),
        request_json.get('last_name', None),
        request_json.get('date_of_birth', None),
        request_json.get('gender_id', None),
        request_json.get('cnh_type_id', None),
        request_json.get('own_vehicle', None))

    driver = driver_dao.save_driver(driver)
    return jsonify({'driver': driver.to_json(), 'return_message': 'Driver Registered'}), 201


# Validado Marshmallow
@app.route('/api/v1.0/drivers/<int:driver_id>', methods=['PUT'])
def update_driver(driver_id):
    if request.get_json() is None:
        return make_response(jsonify({'return_message': 'JSON Object not found'}), 400)

    json_to_validade = request.get_json()
    json_to_validade['driver_id'] = driver_id
    errors = driver_schema.validate(json_to_validade)
    if errors:
        return make_response(
            jsonify({'return_message': 'There is some erros in your request see errors_field', 'errors_field': errors}),
            400)

    driver = driver_dao.get_driver_by_id(driver_id)
    if driver:
        request_json = request.get_json()
        driver = Driver(
            request_json.get('name', None),
            request_json.get('last_name', None),
            request_json.get('date_of_birth', None),
            request_json.get('gender_id', None),
            request_json.get('cnh_type_id', None),
            request_json.get('own_vehicle', None),
            driver_id)

        driver = driver_dao.save_driver(driver)
        return jsonify({'driver': driver.to_json(), 'return_message': 'Driver Updated'}), 200
    else:
        abort(404, {'message': 'Driver do not exist'})


# Validado Marshmallow
@app.route('/api/v1.0/itineraries', methods=['POST'])
def register_itinerarie():
    if request.get_json() is None:
        return make_response(jsonify({'return_message': 'JSON Object not found'}), 400)
    request_json = request.get_json()
    errors = itinerarie_schema.validate(request_json)
    if errors:
        return make_response(
            jsonify({'return_message': 'There is some erros in your request see errors_field', 'errors_field': errors}),
            400)
    itinerarie = Itinerarie(
        request_json.get("driver_id", None),
        request_json.get("loaded", None),
        request_json.get("truck_type_id", None),
        request_json.get("finished", None),
        request_json.get("load_date_time", None),
        request_json.get("unload_date_time", None),
        Address(request_json.get("origin_address", None), request_json.get("origin_street_number", None)),
        Address(request_json.get("destination_address", None), request_json.get("destination_street_number", None))
    )
    itinerarie.load_addresses_info()
    itinerarie.origin_address = itinerarie_dao.save_address(itinerarie.origin_address)
    itinerarie.destination_address = itinerarie_dao.save_address(itinerarie.destination_address)
    itinerarie = itinerarie_dao.save_itinerarie(itinerarie)
    return jsonify({'itinerarie': itinerarie.to_json(), 'return_message': 'Itinerarie Registered'}), 201


# validado marshmallow
@app.route('/api/v1.0/itineraries/finish/<itinerarie_id>', methods=['PUT'])
def finish_itinerarie(itinerarie_id):
    errors = finish_itinerarie_schema.validate({'itinerarie_id': itinerarie_id})
    if errors:
        return make_response(
            jsonify({'return_message': 'There is some erros in your request see errors_field', 'errors_field': errors}),
            400)

    itinerarie = itinerarie_dao.get_itinerarie_by_id(itinerarie_id)
    if itinerarie:
        itinerarie_dao.finish_itinerarie(itinerarie)
        itinerarie.finished = True
        return jsonify({'itinerarie': itinerarie.to_json(), 'return_message': 'Itinerarie Finished'}), 200
    else:
        abort(404)


# validado marshmallow
@app.route('/api/v1.0/itineraries', methods=['GET'])
def get_itineraries():
    errors = get_itineraries_schema.validate(request.args)
    if errors:
        return make_response(
            jsonify({'return_message': 'There is some erros in your request see errors_field', 'errors_field': errors}),
            400)

    initial_load_period = request.args.get('initial_load_period', None)
    final_load_period = request.args.get('final_load_period', None)
    truck_type = request.args.get('truck_type', None)
    loaded = request.args.get('loaded', None)
    finished = request.args.get('finished', None)
    state = request.args.get('state', None)
    city = request.args.get('city', None)

    itineraries = itinerarie_dao.get_itineraries(initial_load_period, final_load_period, truck_type, loaded, finished,
                                                 state, city)
    itineraries_json = []
    for itinerarie in itineraries:
        itineraries_json.append(itinerarie.to_json())
    return jsonify({'meta': {'total_itineraries': itineraries_json.__len__()}, 'itineraries': itineraries_json}), 200


@app.route('/api/v1.0/itineraries/grouped', methods=['GET'])
def get_grouped_itineraries():
    errors = get_grouped_itineraries_schema.validate(request.args)
    if errors:
        return make_response(
            jsonify({'return_message': 'There is some erros in your request see errors_field', 'errors_field': errors}),
            400)

    periodical_type = request.args.get('periodical_type', None)
    loaded = request.args.get('loaded', None)
    initial_load_period = request.args.get('initial_load_period', None)
    final_load_period = request.args.get('final_load_period', None)

    grouped_itineraries_reports = itinerarie_dao.get_grouped_itineraries_report(periodical_type, loaded, initial_load_period, final_load_period)

    itineraries_report = ItinerariesGroupedReport(periodical_type,initial_load_period,final_load_period,loaded,[])

    for report in grouped_itineraries_reports:
        itineraries_report.periodic_reports.append(report.to_json())

    return jsonify(itineraries_report.to_json()), 200


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'return_message': error.description['message']}), 404)
