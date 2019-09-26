import googlemaps


class Address:
    def __init__(self):
        self.id = None
        self.address = None
        self.street_number = None
        self.lat = None
        self.lng = None
        self.state = None
        self.city = None

    def __eq__(self, other):
        if not isinstance(other, Address):
            return False
        return self.address == other.address and \
               self.street_number == other.street_number and \
               self.lat == other.lat and \
               self.lng == other.lng and \
               self.state == other.state and \
               self.city == other.city

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


gmaps = googlemaps.Client(key='Add Your Key here')


def coordinates_info(lat, lng):
    geocode_info = gmaps.reverse_geocode((lat, lng))
    return geocode_info_to_location(geocode_info)


def address_info(address):
    geocode_info = gmaps.geocode(address)
    if geocode_info.__len__() == 0:
        return None
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

    if gloc.state is None or gloc.city is None or gloc.street_number is None or gloc.address is None or gloc.lat is None or gloc.lng is None:
        return None

    else:
        return gloc

# coordinates_info(-23.5100646, -46.54488689999999)
# address_info('Rua Parianas 75')
