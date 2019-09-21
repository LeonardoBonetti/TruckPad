from flask import Flask, jsonify, abort, make_response, request
from models import Driver, Itinerarie
from flask_mysqldb import MySQL
from dao import DriverDao

app = Flask(__name__)
app.config.from_pyfile('config.py')

db = MySQL(app)

driver_dao = DriverDao(db)

@app.route('/api/v1.0/drivers', methods=['GET'])
def get_drivers():
    drivers_json = []
    for driver in driver_dao.list_drivers():
        drivers_json.append(driver.to_json())
    return jsonify({'drivers': drivers_json}), 200


@app.route('/api/v1.0/drivers/<int:driver_id>', methods=['GET'])
def get_driver(driver_id):
    driver = driver_dao.get_drivers_by_id(driver_id)
    if driver:
        return jsonify({'driver': driver.to_json()}), 200
    else:
        abort(404)


@app.route('/api/v1.0/drivers', methods=['POST'])
def register_driver():
    if request.get_json() is None:
        return make_response(jsonify({'error': 'JSON Object not found'}), 400)
    request_json = request.get_json()
    driver = Driver(
        request_json['name'],
        request_json['last_name'],
        request_json['date_of_birth'],
        request_json['gender_id'],
        request_json['cnh_type_id'],
        request_json['own_vehicle'])

    driver = driver_dao.save_driver(driver)
    return jsonify({'driver': driver.to_json(), 'return_message': 'Driver Registered'}), 201


@app.route('/api/v1.0/itineraries', methods=['POST'])
def register_itinerarie():
    if request.get_json() is None:
        return make_response(jsonify({'error': 'JSON Object not found'}), 400)
    request_json = request.get_json()
    itinerarie = Itinerarie(
        request_json['driver_id'],
        request_json['loaded'],
        request_json['truck_type_id'],
        request_json['origin_lat'],
        request_json['origin_long'],
        request_json['destination_lat'],
        request_json['destination_long'],
        request_json['finished']
    )

    itinerarie = driver_dao.save_itinerarie(itinerarie)
    return jsonify({'itinerarie': itinerarie.to_json(), 'return_message': 'Itinerarie Registered'}), 201


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run(debug=True)
