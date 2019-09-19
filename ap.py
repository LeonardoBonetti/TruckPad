from flask import Flask,jsonify
import Driver

app = Flask(__name__)


driver1 = Driver.Driver(1, 'Leonardo', 'Bonetti', '2019-09-18 00:00:00', 1, 2)
driver2 = Driver.Driver(2, 'Nicolas', 'Matos', '2019-07-18 00:00:00', 1, 1)
driver3 = Driver.Driver(3, 'Natalia', 'Garcia', '2019-01-18 00:00:00', 2, 1)
drivers = [driver1.to_json(), driver2.to_json(), driver3.to_json()]

@app.route("/api/v1.0/driver", methods=['GET'])
def index():
    return jsonify({'tasks': drivers}), 200


if __name__ == '__main__':
    app.run(debug=True)