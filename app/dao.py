from app.models import Itinerarie, Driver, ItinerariesPeriodicalReport, PeriodicReport
from app.gmaps import Address

SQL_INSERT_DRIVER = "INSERT INTO Drivers(Name,LastName,DateOfBirth,FK_Gender,FK_CNHTypes,OwnVehicle,InsertDate) " \
                    "VALUES(%s,%s,%s,%s,%s,%s,UTC_TIMESTAMP())"

SQL_UPDATE_DRIVER = "UPDATE Drivers " \
                    "set Name=%s, LastName=%s ,DateOfBirth=%s ,FK_Gender=%s ,FK_CNHTypes=%s,OwnVehicle=%s WHERE ID = %s;"

# SQL_LIST_DRIVERS = "SELECT ID,Name,LastName,DateOfBirth,FK_Gender,FK_CNHTypes,OwnVehicle from Drivers"

# SQL_GET_DRIVER_BY_ID = "SELECT ID,Name,LastName,DateOfBirth,FK_Gender,FK_CNHTypes,OwnVehicle from Drivers WHERE ID = %s;"

SQL_INSERT_ITINERARIE = "INSERT INTO Itineraries(FK_Drivers,Loaded,FK_TruckType,Finished,LoadDateTime,UnLoadDateTime," \
                        "InsertDate,FK_Dest_Addresses,FK_Origin_Addresses) " \
                        "VALUES(%s,%s,%s,%s,%s,%s,UTC_TIMESTAMP(),%s,%s)"

SQL_INSERT_ADDRESS = "INSERT INTO Addresses(Lng,Lat,Address,StreetNumber,City,State)" \
                     "VALUES(%s,%s,%s,%s,%s,%s)"

SQL_FINISH_ITINERARIE = "UPDATE Itineraries set Finished = 1 WHERE ID = %s;"

SQL_GET_ITINERARIE_BY_ID = "SELECT ID,FK_Drivers,Loaded,FK_TruckType,OriginLat,OriginLong,DestinationLat,DestinationLong," \
                           "Finished,LoadDateTime,UnLoadDateTime from Itineraries WHERE ID = %s;"


class DriverDao:
    def __init__(self, db):
        self.__db = db

    def list_drivers(self, own_vehicle):
        cursor = self.__db.connection.cursor()
        # cursor.execute(SQL_LIST_DRIVERS)
        cursor.callproc('GetDrivers', [None, own_vehicle])
        dict_list = recordset_to_dict(cursor)
        drivers = []
        for i in range(0, dict_list.__len__()):
            drivers.append(sql_driver_to_obj(dict_list[i]))
        return drivers

    def get_driver_by_id(self, id):
        cursor = self.__db.connection.cursor()
        cursor.callproc('GetDrivers', [id, None])
        # cursor.execute(SQL_GET_DRIVER_BY_ID, (id,))
        dict_list = recordset_to_dict(cursor)
        if len(dict_list) == 0:
            return None
        else:
            driver = sql_driver_to_obj(dict_list[0])
            return driver

    def save_driver(self, driver):
        cursor = self.__db.connection.cursor()
        if driver.id:
            cursor.execute(SQL_UPDATE_DRIVER,
                           (driver.name, driver.last_name, driver.date_of_birth, driver.gender_id, driver.cnh_type_id,
                            driver.own_vehicle, driver.id))
        else:
            cursor.execute(SQL_INSERT_DRIVER,
                           (driver.name, driver.last_name, driver.date_of_birth, driver.gender_id, driver.cnh_type_id,
                            driver.own_vehicle))
            driver.id = cursor.lastrowid
        self.__db.connection.commit()
        return driver


class ItinerarieDao:
    def __init__(self, db):
        self.__db = db

    def save_itinerarie(self, itinerarie):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_INSERT_ITINERARIE,
                       (itinerarie.driver_id, itinerarie.loaded, itinerarie.truck_type_id, itinerarie.finished,
                        itinerarie.load_date_time, itinerarie.unload_date_time, itinerarie.origin_address.id,
                        itinerarie.destination_address.id))
        itinerarie.id = cursor.lastrowid
        self.__db.connection.commit()
        return itinerarie

    def get_itinerarie_by_id(self, id):
        cursor = self.__db.connection.cursor()
        cursor.callproc('GetItineraries', [None, None, None, None, None, None, None, None, None, id])
        dict_list = recordset_to_dict(cursor)
        if len(dict_list) == 0:
            return None
        else:
            itinerarie = sql_itinerarie_to_obj(dict_list[0])
            return itinerarie

    def finish_itinerarie(self, itinerarie):
        self.__db.connection.cursor().execute(SQL_FINISH_ITINERARIE, (itinerarie.id,))
        self.__db.connection.commit()

    def get_itineraries(self, initial_load_period, final_load_period, truck_type, loaded, finished, origin_state,
                        origin_city, destination_state, destination_city):
        cursor = self.__db.connection.cursor()
        cursor.callproc('GetItineraries',
                        [initial_load_period, final_load_period, truck_type, loaded, finished, origin_state,
                         origin_city, destination_state, destination_city, None])
        dict_list = recordset_to_dict(cursor)
        itineraries = []
        for i in range(0, dict_list.__len__()):
            itineraries.append(sql_itinerarie_to_obj(dict_list[i]))
        return itineraries

    def save_address(self, address):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_INSERT_ADDRESS,
                       (address.lng, address.lat, address.address, address.street_number, address.city, address.state))
        address.id = cursor.lastrowid
        self.__db.connection.commit()
        return address

    def get_itineraries_periodic_reports(self, periodical_type, loaded, initial_load_period, final_load_period):
        cursor = self.__db.connection.cursor()
        if periodical_type == 'daily':
            cursor.callproc('GetItinerariesGroupedByDay',
                            [initial_load_period, final_load_period, loaded])
        elif periodical_type == 'monthly':
            cursor.callproc('GetItinerariesGroupedByMonth',
                            [initial_load_period, final_load_period, loaded])
        elif periodical_type == 'yearly':
            cursor.callproc('GetItinerariesGroupedByYear',
                            [initial_load_period, final_load_period, loaded])

        dict_list = recordset_to_dict(cursor)
        reports = []
        for i in range(0, dict_list.__len__()):
            reports.append(sql_periodic_reports_to_sql(dict_list[i]))
        return reports


def recordset_to_dict(cursor):
    row_headers = [x[0] for x in cursor.description]  # this will extract row headers
    rv = cursor.fetchall()
    json_data = []
    for result in rv:
        json_data.append(dict(zip(row_headers, result)))
    return json_data


def sql_driver_to_obj(sql_obj):
    driver = Driver(
        sql_obj.get('Name', None),
        sql_obj.get('LastName', None),
        sql_obj.get('DateOfBirth', None),
        sql_obj.get('FK_Gender', None),
        sql_obj.get('FK_CNHTypes', None),
        sql_obj.get('OwnVehicle', None),
        sql_obj.get('ID', None))
    return driver


def sql_itinerarie_to_obj(sql_obj):
    itinerarie = Itinerarie(
        sql_obj.get('IDDriver', None),
        sql_obj.get('Loaded', None),
        sql_obj.get('TruckTypeID', None),
        sql_obj.get('Finished', None),
        sql_obj.get('LoadDateTime', None),
        sql_obj.get('UnLoadDateTime', None))

    origin_address = Address()
    origin_address.address = sql_obj.get('OrigAddress', None)
    origin_address.street_number = sql_obj.get('OrigStreetNumber', None)
    origin_address.lat = sql_obj.get('OrigLatitude', None)
    origin_address.lng = sql_obj.get('OrigLongitude', None)
    origin_address.state = sql_obj.get('OrigState', None)
    origin_address.city = sql_obj.get('OrigCity', None)
    origin_address.id = sql_obj.get('OrigAdressID', None)

    destination_address = Address()
    destination_address.address = sql_obj.get('DestAddress', None)
    destination_address.street_number = sql_obj.get('DestStreetNumber', None)
    destination_address.lat = sql_obj.get('DestLatitude', None)
    destination_address.lng = sql_obj.get('DestLongitude', None)
    destination_address.state = sql_obj.get('DestState', None)
    destination_address.city = sql_obj.get('DestCity', None)
    destination_address.id = sql_obj.get('DestAdressID', None)

    itinerarie.id = sql_obj.get('IDItinerarie', None)
    itinerarie.truck_type_description = sql_obj.get('TruckTypeDescription', None)
    itinerarie.origin_address = origin_address
    itinerarie.destination_address = destination_address

    return itinerarie


def sql_periodic_reports_to_sql(sql_obj):
    periodic = PeriodicReport(sql_obj.get('Period', None), sql_obj.get('Itineraries', None))
    return periodic
