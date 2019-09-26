from marshmallow import Schema, fields, validates, ValidationError

truthy_values = ['true', '1', 'True', True, 1]
falsy_values = ['false', '0', 'False', False, 0]


class DriversSchema(Schema):
    own_vehicle = fields.Boolean(truthy=truthy_values, falsy=falsy_values)


class DriverSchema(Schema):
    driver_id = fields.Int(required=False)
    name = fields.String(required=True)
    last_name = fields.String(required=True)
    date_of_birth = fields.DateTime(required=True)
    gender_id = fields.Int(required=True)
    cnh_type_id = fields.Int(required=True)
    own_vehicle = fields.Boolean(required=True, truthy=truthy_values, falsy=falsy_values)


class ItinerarieSchema(Schema):
    driver_id = fields.Int(required=True)
    loaded = fields.Boolean(required=True, truthy=truthy_values, falsy=falsy_values)
    truck_type_id = fields.Int(required=True)
    finished = fields.Boolean(required=True, truthy=truthy_values, falsy=falsy_values)
    load_date_time = fields.DateTime(required=True)
    unload_date_time = fields.DateTime(required=True)
    origin_address = fields.Str(required=True)
    destination_address = fields.Str(required=True)


class FinishItinerarie(Schema):
    itinerarie_id = fields.Int(required=True)


class GetItinerariesSchema(Schema):
    initial_load_period = fields.DateTime()
    final_load_period = fields.DateTime()
    truck_type = fields.Int()
    loaded = fields.Boolean(truthy=set(truthy_values), falsy=set(falsy_values))
    finished = fields.Boolean(truthy=set(truthy_values), falsy=set(falsy_values))
    origin_state = fields.Str()
    origin_city = fields.Str()
    destination_state = fields.Str()
    destination_city = fields.Str()


class PeriodicalItinerariesReportSchema(Schema):
    loaded = fields.Boolean(truthy=truthy_values, falsy=falsy_values)
    periodical_type = fields.Str(required=True, validate=[lambda x: x in ['monthly', 'daily', 'yearly']],
                              error_messages={
                                    'validator_failed': 'Use a periodical type \'monthly, daily or yearly\' value on periodical_type parameter',
                                })
    initial_load_period = fields.DateTime(required=True)
    final_load_period = fields.DateTime(required=True)

