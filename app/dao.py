from app.models import Itinerarie, Driver
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
        cursor.execute(SQL_GET_ITINERARIE_BY_ID, (id,))
        dict_list = recordset_to_dict(cursor)
        if len(dict_list) == 0:
            return None
        else:
            itinerarie = sql_itinerarie_to_obj(dict_list[0])
            return itinerarie

    def finish_itinerarie(self, itinerarie):
        self.__db.connection.cursor().execute(SQL_FINISH_ITINERARIE, (itinerarie.id,))
        self.__db.connection.commit()

    def get_itineraries(self, initial_load_period, final_load_period, truck_type, loaded, finished):
        cursor = self.__db.connection.cursor()
        cursor.callproc('GetItineraries', [initial_load_period, final_load_period, truck_type, loaded, finished])
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
        sql_obj.get('FK_TruckType', None),
        sql_obj.get('Finished', None),
        sql_obj.get('LoadDateTime', None),
        sql_obj.get('UnLoadDateTime', None),
        Address(
            sql_obj.get('OrigAddress', None),
            sql_obj.get('OrigStreetNumber', None),
            sql_obj.get('OrigLatitude', None),
            sql_obj.get('OrigLongitude', None),
            sql_obj.get('OrigState', None),
            sql_obj.get('OrigCity', None)
        ),
        Address(
            sql_obj.get('DestAddress', None),
            sql_obj.get('DestStreetNumber', None),
            sql_obj.get('DestLatitude', None),
            sql_obj.get('DestLongitude', None),
            sql_obj.get('DestState', None),
            sql_obj.get('DestCity', None)
        ),
        sql_obj.get('IDItinerarie', None),
        sql_obj.get('TruckTypeDescription', None))
    return itinerarie
