from app.gmaps import Address, address_info
from app import endpoints
from flask import jsonify, request
import pytest

@pytest.fixture
def google_address_example():
    target_address = Address()
    target_address.street_number = '75'
    target_address.address = 'Rua Parianas'
    target_address.state = 'SP'
    target_address.city = 'São Paulo'
    target_address.lat = -23.5100646
    target_address.lng = -46.54488689999999
    return target_address


def test_google_api_correctly_response(google_address_example):

    test_address = address_info('Rua Parianas 75 Jd Jaú São Paulo SP')
    assert test_address == google_address_example

