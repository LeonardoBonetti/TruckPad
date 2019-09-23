from marshmallow import Schema, fields, validates, ValidationError


class DriversSchema(Schema):
    own_vehicle = fields.Boolean(truthy=set(['true', '1', 'True']), falsy=set(['false', '0', 'False']))


class DriverSchema(Schema):
    driver_id = fields.Int(required=False)
    name = fields.String(required=True)
    last_name = fields.String(required=True)
    date_of_birth = fields.DateTime(required=True)
    gender_id = fields.Int(required=True)
    cnh_type_id = fields.Int(required=True)
    own_vehicle = fields.Boolean(required=True, truthy=set(['true', '1', 'True', True]), falsy=set(['false', '0', 'False', False]))


class ItinerarieSchema(Schema):
    driver_id = fields.Int(required=True)
    loaded = fields.Boolean(required=True, truthy=set(['true', '1', 'True', True]), falsy=set(['false', '0', 'False', False]))
    truck_type_id = fields.Int(required=True)
    finished = fields.Boolean(required=True, truthy=set(['true', '1', 'True', True]), falsy=set(['false', '0', 'False', False]))
    load_date_time = fields.DateTime(required=True)
    unload_date_time = fields.DateTime(required=True)
    origin_address = fields.Str(required=True)
    destination_address = fields.Str(required=True)
    origin_street_number = fields.Str(required=True)
    destination_street_number = fields.Str(required=True)
