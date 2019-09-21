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
    def __init__(self, driver_id, loaded, truck_type_id, origin_lat, origin_long, destination_lat, destination_long, finished, id=None):
        self.id = id
        self.driver_id = driver_id
        self.loaded = loaded
        self.truck_type_id = truck_type_id
        self.origin_lat = origin_lat
        self.origin_long = origin_long
        self.destination_lat = destination_lat
        self.destination_long = destination_long
        self.finished = finished

    def to_json(self):
        return {
            'id': self.id,
            'driver_id': self.driver_id,
            'loaded': self.loaded,
            'truck_type_id': self.truck_type_id,
            'origin_lat': self.origin_lat,
            'origin_long': self.origin_long,
            'destination_lat': self.destination_lat,
            'destination_long': self.destination_long,
            'finished': self.finished
        }
