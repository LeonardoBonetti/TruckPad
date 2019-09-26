from app import endpoints
from flask import jsonify, request, json
from datetime import datetime

def test_get_drivers_success_without_filter():
    app = endpoints.app
    client = app.test_client()
    url = '/api/v1.0/drivers'
    response = client.get(url)
    assert response.status_code == 200


def test_get_drivers_sucess_with_filter():
    app = endpoints.app
    client = app.test_client()
    url = '/api/v1.0/drivers?own_vehicle=true'
    response = client.get(url)
    assert response.status_code == 200


def test_get_drivers_with_invalid_filter():
    app = endpoints.app
    client = app.test_client()
    url = '/api/v1.0/drivers?own_vehicle=truue'
    response = client.get(url)
    response_json = response.data
    assert response.status_code == 400
    assert response.data == b'{\n  "errors_field": {\n    "own_vehicle": [\n      "Not a valid boolean."\n    ]\n  }, \n  "return_message": "There is some erros in your request see errors_field"\n}\n'


def test_get_driver_who_exist():
    # This test just work if Driver with ID 1 exist, need to fix it
    app = endpoints.app
    client = app.test_client()
    url = '/api/v1.0/drivers/1'
    response = client.get(url)
    assert response.status_code == 200


def test_get_driver_who_does_not_exist():
    app = endpoints.app
    client = app.test_client()
    url = '/api/v1.0/drivers/321554'
    response = client.get(url)
    assert response.status_code == 404
    assert response.data == b'{\n  "return_message": "Driver does not exist"\n}\n'


def test_get_driver_with_not_integer_parameter():
    app = endpoints.app
    client = app.test_client()
    url = '/api/v1.0/drivers/1aaa'
    response = client.get(url)
    response_json = response.data
    assert response.status_code == 400
    assert response.data == b'{\n  "return_message": "driver_id must be a integer number"\n}\n'


def test_register_driver_successful():
    app = endpoints.app
    client = app.test_client()
    url = '/api/v1.0/drivers'
    date = datetime(2018, 11, 28).strftime('%Y-%m-%d %H:%M:%S')
    mock_request_data = {'cnh_type_id': 3, 'date_of_birth': date, 'gender_id': 1, 'last_name': 'pytest', 'name': 'test', 'own_vehicle': False}
    response = client.post(url, json=mock_request_data)
    assert response.status_code == 201


def test_register_driver_json_not_found():
    app = endpoints.app
    client = app.test_client()
    url = '/api/v1.0/drivers'
    response = client.post(url)
    assert response.status_code == 400
    assert response.data == b'{\n  "return_message": "JSON Object not found"\n}\n'


def test_register_driver_invalid_parameters():
    app = endpoints.app
    client = app.test_client()
    url = '/api/v1.0/drivers'
    date = datetime(2018, 11, 28).strftime('%Y-%m-%d %H:%M:%S')
    mock_request_data = {'cnh_type_id': '1aaa', 'date_of_birth': date, 'gender_id': 1, 'last_name': 'pytest', 'name': 'test',
                         'own_vehicle': False}
    response = client.post(url, json=mock_request_data)
    assert response.status_code == 400
    assert response.data == b'{\n  "errors_field": {\n    "cnh_type_id": [\n      "Not a valid integer."\n    ]\n  }, \n  "return_message": "There is some erros in your request see errors_field"\n}\n'


def test_update_driver_invalid_parameters():
    app = endpoints.app
    client = app.test_client()
    url = '/api/v1.0/drivers/1'
    date = datetime(2018, 11, 28).strftime('%Y-%m-%d %H:%M:%S')
    mock_request_data = {'cnh_type_id': 'aa1', 'date_of_birth': date, 'gender_id': 1, 'last_name': 'pytest', 'name': 'test',
                         'own_vehicle': False}
    response = client.put(url, json=mock_request_data)
    assert response.status_code == 400
    assert response.data == b'{\n  "errors_field": {\n    "cnh_type_id": [\n      "Not a valid integer."\n    ]\n  }, \n  "return_message": "There is some erros in your request see errors_field"\n}\n'


def test_update_driver_json_not_found():
    app = endpoints.app
    client = app.test_client()
    url = '/api/v1.0/drivers/1'
    response = client.put(url)
    assert response.status_code == 400
    assert response.data == b'{\n  "return_message": "JSON Object not found"\n}\n'


def test_update_driver_does_not_exist():
    app = endpoints.app
    client = app.test_client()
    url = '/api/v1.0/drivers/0'
    date = datetime(2018, 11, 28).strftime('%Y-%m-%d %H:%M:%S')
    mock_request_data = {'cnh_type_id': 1, 'date_of_birth': date, 'gender_id': 1, 'last_name': 'pytest', 'name': 'test',
                         'own_vehicle': False}
    response = client.put(url, json=mock_request_data)
    assert response.status_code == 404
    assert response.data == b'{\n  "return_message": "Driver does not exist"\n}\n'


def test_register_itinerarie_successful():
    app = endpoints.app
    client = app.test_client()
    url = '/api/v1.0/itineraries'
    mock_request_data = {'driver_id': 1, 'loaded': False, 'truck_type_id': 2, 'load_date_time': '2020-08-26 00:00:00', 'unload_date_time': '2020-08-30 00:00:00', 'finished': False, 'origin_address': 'Rua Tenente Otavio Gomes 330', 'destination_address': 'Av. Brigadeiro luis antonio 1503 Bela Vista São Paulo SP'}
    response = client.post(url, json=mock_request_data)
    assert response.status_code == 201


def test_register_itinerarie_json_not_found():
    app = endpoints.app
    client = app.test_client()
    url = '/api/v1.0/itineraries'
    response = client.post(url)
    assert response.status_code == 400
    assert response.data == b'{\n  "return_message": "JSON Object not found"\n}\n'


def test_register_itinerarie_invalid_parameters():
    app = endpoints.app
    client = app.test_client()
    url = '/api/v1.0/itineraries'
    mock_request_data = {'driver_id': 'aa1', 'loaded': False, 'truck_type_id': 2, 'load_date_time': '2020-08-26 00:00:00', 'unload_date_time': '2020-08-30 00:00:00', 'finished': False, 'origin_address': 'Rua Tenente Otavio Gomes 330', 'destination_address': 'Av. Brigadeiro luis antonio 1503 Bela Vista São Paulo SP'}
    response = client.post(url, json=mock_request_data)
    assert response.status_code == 400
    assert response.data == b'{\n  "errors_field": {\n    "driver_id": [\n      "Not a valid integer."\n    ]\n  }, \n  "return_message": "There is some erros in your request see errors_field"\n}\n'


def test_register_itinerarie_address_not_found():
    app = endpoints.app
    client = app.test_client()
    url = '/api/v1.0/itineraries'
    mock_request_data = {'driver_id': 1, 'loaded': False, 'truck_type_id': 2,
                         'load_date_time': '2020-08-26 00:00:00', 'unload_date_time': '2020-08-30 00:00:00',
                         'finished': False, 'origin_address': 'Rua NUNCA EXISTIRÁ',
                         'destination_address': 'Av. NÃO EXISTE'}
    response = client.post(url, json=mock_request_data)
    assert response.status_code == 400
    assert response.data == b'{\n  "return_message": "Invalid address data, use: <address> <street_number> <neighborhood> <city> <state>  example: Av. Brigadeiro luis antonio 1503 Bela Vista S\\u00e3o Paulo SP"\n}\n'


def test_finish_itinerarie_does_not_exist():
    app = endpoints.app
    client = app.test_client()
    url = '/api/v1.0/itineraries/finish/0'
    response = client.put(url)
    assert response.status_code == 404
    assert response.data == b'{\n  "return_message": "Itinerarie does not exist"\n}\n'


def test_get_itineraries_sucess_without_filter():
    app = endpoints.app
    client = app.test_client()
    url = '/api/v1.0/itineraries'
    response = client.get(url)
    assert response.status_code == 200

def test_get_itineraries_sucess_with_filter():
    app = endpoints.app
    client = app.test_client()
    url = '/api/v1.0/itineraries?origin_state=SP&destination_state=SP'
    response = client.get(url)
    assert response.status_code == 200


def test_get_itineraries_with_invalid_filter():
    app = endpoints.app
    client = app.test_client()
    url = '/api/v1.0/itineraries?finished=fdsfsadf'
    response = client.get(url)
    assert response.status_code == 400


def test_get_periodical_itineraries_report_sucess():
    app = endpoints.app
    client = app.test_client()
    url = '/api/v1.0/itineraries/periodical?periodical_type=monthly&loaded=false&initial_load_period=2019-01-01 00:00:00&final_load_period=2021-01-01 00:00:00'
    response = client.get(url)
    assert response.status_code == 200


def test_get_periodical_itineraries_report_with_invalid_filter():
    app = endpoints.app
    client = app.test_client()
    url = '/api/v1.0/itineraries/periodical?loaded=false&initial_load_period=2019-01-01 00:00:00&final_load_period=2021-01-01 00:00:00'
    response = client.get(url)
    assert response.status_code == 400
    assert response.data == b'{\n  "errors_field": {\n    "periodical_type": [\n      "Missing data for required field."\n    ]\n  }, \n  "return_message": "There is some erros in your request see errors_field"\n}\n'



