from flask import Flask,jsonify,abort,make_response,request
import Driver

app = Flask(__name__)


driver1 = Driver.Driver(1, 'Leonardo', 'Bonetti', '2019-09-18 00:00:00', 1, 2)
driver2 = Driver.Driver(2, 'Nicolas', 'Matos', '2019-07-18 00:00:00', 1, 1)
driver3 = Driver.Driver(3, 'Natalia', 'Garcia', '2019-01-18 00:00:00', 2, 1)
drivers = [driver1.to_json(), driver2.to_json(), driver3.to_json()]


@app.route('/api/v1.0/driver', methods=['GET'])
def get_drivers():
    return jsonify({'tasks': drivers}), 200


@app.route('/api/v1.0/driver/<int:driver_id>', methods=['GET'])
def get_driver(driver_id):
    driver = [driver for driver in drivers if driver['id'] == driver_id]
    if len(driver) == 0:
        abort(404)
    return jsonify({'driver': driver[0]}), 200


@app.route('/api/v1.0/driver', methods=['POST'])
def register_driver():
    if request.get_json() is None:
        return make_response(jsonify({'error': 'JSON Object not found'}), 400)
    request_json = request.get_json()
    driver = Driver.Driver(request_json['id'],
                           request_json['name'],
                           request_json['last_name'],
                           request_json['date_of_birth'],
                           request_json['gender_id'],
                           request_json['cnh_type_id'])

    drivers.append(driver.to_json())
    return jsonify({'driver': driver.to_json(), 'return_message': 'Driver Registered'}), 201


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run(debug=True)