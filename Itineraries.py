class Itineraries:
    def __init__(self, id, driver_id, loaded, truck_type_id, origin_lat, origin_long, destination_lat, destination_long):
        self.id = id
        self.driver_id = driver_id
        self.loaded = loaded
        self.truck_type_id = truck_type_id
        self.origin_lat = origin_lat
        self.origin_long = origin_long
        self.destination_lat = destination_lat
        self.destination_long = destination_long
