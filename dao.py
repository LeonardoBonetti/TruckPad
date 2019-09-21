from models import Itinerarie, Driver
import json

SQL_INSERT_DRIVER = "INSERT INTO Drivers(Name,LastName,DateOfBirth,FK_Gender,FK_CNHTypes,OwnVehicle) " \
                    "VALUES(%s,%s,%s,%s,%s,%s)"

SQL_UPDATE_DRIVER = "UPDATE Drivers " \
                    "set Name=%s, LastName=%s ,DateOfBirth=%s ,FK_Gender=%s ,FK_CNHTypes=%s,OwnVehicle=%s ) WHERE ID = %s;"

SQL_LIST_DRIVERS = "SELECT ID,Name,LastName,DateOfBirth,FK_Gender,FK_CNHTypes,OwnVehicle from Drivers"

SQL_GET_DRIVERS_BY_ID = "SELECT ID,Name,LastName,DateOfBirth,FK_Gender,FK_CNHTypes,OwnVehicle from Drivers WHERE ID = %s;"

SQL_INSERT_ITINERARIE = "INSERT INTO Itineraries(FK_Drivers,Loaded,FK_TruckType,OriginLat,OriginLong,DestinationLat,DestinationLong,Finished) " \
                    "VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"

SQL_UPDATE_ITINERARIE = "UPDATE Itineraries " \
                    "set FK_Drivers=%s, Loaded=%s ,FK_TruckType=%s ,OriginLat=%s ,OriginLong=%s, DestinationLat=%s, DestinationLong=%s, Finished=%s" \
                    " WHERE ID = %s;"


class DriverDao:
    def __init__(self, db):
        self.__db = db

    def list_drivers(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_LIST_DRIVERS)
        dict_list = recordset_to_dict(cursor)
        drivers = []
        for i in range(0, dict_list.__len__()):
            drivers.append(sql_driver_to_obj(dict_list[i]))
        return drivers

    def get_drivers_by_id(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_GET_DRIVERS_BY_ID, (id,))
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
                           (driver.name, driver.last_name, driver.date_of_birth, driver.gender_id, driver.cnh_type_id, driver.own_vehicle))
            driver.id = cursor.lastrowid
        self.__db.connection.commit()
        return driver

    def save_itinerarie(self, itinerarie):
        cursor = self.__db.connection.cursor()
        if itinerarie.id:
            cursor.execute(SQL_UPDATE_ITINERARIE,
                           (itinerarie.driver_id, itinerarie.loaded, itinerarie.truck_type_id, itinerarie.origin_lat,
                            itinerarie.origin_long,itinerarie.destination_lat,itinerarie.destination_long, itinerarie.finished, itinerarie.id))
        else:
            cursor.execute(SQL_INSERT_ITINERARIE,
                           (itinerarie.driver_id, itinerarie.loaded, itinerarie.truck_type_id, itinerarie.origin_lat,
                            itinerarie.origin_long, itinerarie.destination_lat, itinerarie.destination_long, itinerarie.finished))
            itinerarie.id = cursor.lastrowid
        self.__db.connection.commit()
        return itinerarie


def recordset_to_dict(cursor):
    row_headers = [x[0] for x in cursor.description]  # this will extract row headers
    rv = cursor.fetchall()
    json_data = []
    for result in rv:
        json_data.append(dict(zip(row_headers, result)))
    return json_data


def sql_driver_to_obj(sql_driver):
    driver = Driver(
        sql_driver['Name'],
        sql_driver['LastName'],
        sql_driver['DateOfBirth'],
        sql_driver['FK_Gender'],
        sql_driver['FK_CNHTypes'],
        sql_driver['OwnVehicle'],
        sql_driver['ID'])
    return driver
