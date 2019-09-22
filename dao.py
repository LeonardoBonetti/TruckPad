from models import Itinerarie, Driver
import json

SQL_INSERT_DRIVER = "INSERT INTO Drivers(Name,LastName,DateOfBirth,FK_Gender,FK_CNHTypes,OwnVehicle) " \
                    "VALUES(%s,%s,%s,%s,%s,%s)"

SQL_UPDATE_DRIVER = "UPDATE Drivers " \
                    "set Name=%s, LastName=%s ,DateOfBirth=%s ,FK_Gender=%s ,FK_CNHTypes=%s,OwnVehicle=%s WHERE ID = %s;"

SQL_LIST_DRIVERS = "SELECT ID,Name,LastName,DateOfBirth,FK_Gender,FK_CNHTypes,OwnVehicle from Drivers"

SQL_GET_DRIVER_BY_ID = "SELECT ID,Name,LastName,DateOfBirth,FK_Gender,FK_CNHTypes,OwnVehicle from Drivers WHERE ID = %s;"

SQL_INSERT_ITINERARIE = "INSERT INTO Itineraries(FK_Drivers,Loaded,FK_TruckType,OriginLat,OriginLong,DestinationLat,DestinationLong,Finished) " \
                    "VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"

SQL_FINISH_ITINERARIE = "UPDATE Itineraries set Finished = 1 WHERE ID = %s;"

SQL_GET_ITINERARIE_BY_ID = "SELECT ID,FK_Drivers,Loaded,FK_TruckType,OriginLat,OriginLong,DestinationLat,DestinationLong,Finished" \
                           " from Itineraries WHERE ID = %s;"

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

    def get_driver_by_id(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_GET_DRIVER_BY_ID, (id,))
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


class ItinerarieDao:
    def __init__(self, db):
        self.__db = db

    def save_itinerarie(self, itinerarie):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_INSERT_ITINERARIE,
                       (itinerarie.driver_id, itinerarie.loaded, itinerarie.truck_type_id, itinerarie.origin_lat,
                        itinerarie.origin_long, itinerarie.destination_lat, itinerarie.destination_long,
                        itinerarie.finished))
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
            driver = sql_itinerarie_to_obj(dict_list[0])
            return driver

    def finish_itinerarie(self, itinerarie):
        self.__db.connection.cursor().execute(SQL_FINISH_ITINERARIE, (itinerarie.id,))
        self.__db.connection.commit()


def recordset_to_dict(cursor):
    row_headers = [x[0] for x in cursor.description]  # this will extract row headers
    rv = cursor.fetchall()
    json_data = []
    for result in rv:
        json_data.append(dict(zip(row_headers, result)))
    return json_data


def sql_driver_to_obj(sql_obj):
    driver = Driver(
        sql_obj['Name'],
        sql_obj['LastName'],
        sql_obj['DateOfBirth'],
        sql_obj['FK_Gender'],
        sql_obj['FK_CNHTypes'],
        sql_obj['OwnVehicle'],
        sql_obj['ID'])
    return driver


def sql_itinerarie_to_obj(sql_obj):
    itinerarie = Itinerarie(
        sql_obj['FK_Drivers'],
        sql_obj['Loaded'],
        sql_obj['FK_TruckType'],
        sql_obj['OriginLat'],
        sql_obj['OriginLong'],
        sql_obj['DestinationLat'],
        sql_obj['DestinationLong'],
        sql_obj['Finished'],
        sql_obj['ID'])
    return itinerarie