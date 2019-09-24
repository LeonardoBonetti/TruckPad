import googlemaps

class Address:
    def __init__(self, address=None, street_number=None, lat=None, lng=None, state=None, city=None, id=None):
        self.id = id
        self.address = address
        self.street_number = street_number
        self.lat = lat
        self.lng = lng
        self.state = state
        self.city = city

    def simples_address(self):
        return "{} {}".format(self.address, self.street_number)

    def to_json(self):
        return {
            'address': self.address,
            'street_number': self.street_number,
            'lat': self.lat,
            'lng': self.lng,
            'state': self.state,
            'city': self.city,
            'id': self.id
        }


gmaps = googlemaps.Client(key='AIzaSyA5j12KynK_TmVxz4K0zOiX3cWCQAxhYMA')


def coordinates_info(lat, lng):
    geocode_info = gmaps.reverse_geocode((lat, lng))
    return geocode_info_to_location(geocode_info)


def address_info(address):
    geocode_info = gmaps.geocode(address)
    return geocode_info_to_location(geocode_info)


def geocode_info_to_location(geocode_info):
    gloc = Address()

    address_components = geocode_info[0]['address_components']
    types = ['route', 'street_number', 'administrative_area_level_1', 'administrative_area_level_2']
    geonames = filter(lambda x: len(set(x['types']).intersection(types)), address_components)

    for geoname in geonames:
        common_types = set(geoname['types']).intersection(set(types))
        type = str(', '.join(common_types))
        if type == 'administrative_area_level_1':
            gloc.state = geoname['short_name']
        elif type == 'administrative_area_level_2':
            gloc.city = geoname['long_name']
        elif type == 'route':
            gloc.address = geoname['long_name']
        elif type == 'street_number':
            gloc.street_number = geoname['long_name']

    geometry_info = geocode_info[0]['geometry']
    gloc.lat = geometry_info['location']['lat']
    gloc.lng = geometry_info['location']['lng']
    return gloc


# coordinates_info(-23.5100646, -46.54488689999999)
# address_info('Rua Parianas 75')
