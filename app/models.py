from app import gmaps


class Driver:
    def __init__(self, name, last_name, date_of_birth, gender_id, cnh_type_id, own_vehicle, id=None):
        self.id = id
        self.name = name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.gender_id = gender_id
        self.cnh_type_id = cnh_type_id
        self.own_vehicle = own_vehicle

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'last_name': self.last_name,
            'date_of_birth': self.date_of_birth,
            'gender_id': self.gender_id,
            'cnh_type_id': self.cnh_type_id,
            'own_vehicle': self.own_vehicle
        }


class Itinerarie:
    def __init__(self, driver_id, loaded, truck_type_id, finished,
                 load_date_time, unload_date_time, origin_address, destination_address, id=None,
                 truck_type_description=None):
        self.id = id
        self.driver_id = driver_id
        self.loaded = loaded
        self.truck_type_id = truck_type_id
        self.truck_type_description = truck_type_description
        self.finished = finished
        self.load_date_time = load_date_time
        self.unload_date_time = unload_date_time
        self.origin_address = origin_address
        self.destination_address = destination_address

    def load_addresses_info(self):
        self.origin_address = gmaps.address_info(self.origin_address.simples_address())
        self.destination_address = gmaps.address_info(self.destination_address.simples_address())

    def to_json(self):
        return {
            'id': self.id,
            'driver_id': self.driver_id,
            'loaded': self.loaded,
            'truck_type_id': self.truck_type_id,
            'truck_type_description': self.truck_type_description,
            'finished': self.finished,
            'load_date_time': self.load_date_time,
            'unload_date_time': self.unload_date_time,
            'origin_address': self.origin_address.to_json(),
            'destination_address': self.destination_address.to_json()
        }


class ItinerariesPeriodicalReport:
    def __init__(self, periodical_type, initial_period, final_period, loaded, periodic_reports):
        self.periodical_type = periodical_type
        self.initial_period = initial_period
        self.final_period = final_period
        self.loaded = loaded
        self.periodic_reports = periodic_reports

    def to_json(self):
        return {
            'periodical_type': self.periodical_type,
            'initial_period': self.initial_period,
            'final_period': self.final_period,
            'loaded': self.loaded,
            'periodic_reports': self.periodic_reports,
        }


class PeriodicReport:
    def __init__(self, period, count):
        self.period = period
        self.count = count

    def to_json(self):
        return {
            'period': self.period,
            'count': self.count
        }
