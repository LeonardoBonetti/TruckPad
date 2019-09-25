CREATE DEFINER=`admin`@`%` PROCEDURE `GetDrivers`(

	IN ID INT(11),
    IN OwnVehicle bool

)
BEGIN
	SELECT * FROM Drivers WHERE
    (ID IS NULL OR ID = Drivers.ID) AND
    (OwnVehicle IS NULL OR OwnVehicle = Drivers.OwnVehicle);
END;

CREATE DEFINER=`admin`@`%` PROCEDURE `GetItineraries`(
	IN InitialLoadPeriod DATETIME,
    IN FinalLoadPeriod DATETIME,
    IN FK_TruckType INT(11),
    IN Loaded bool,
    IN Finished bool,
    IN OAState VARCHAR(256),
    IN OACity VARCHAR(256),
	IN DAState VARCHAR(256),
    IN DACity VARCHAR(256),
    IN ID int(11)
)
BEGIN
SELECT I.ID IDItinerarie, D.ID IDDriver, CONCAT(D.Name, ' ', D.Lastname) DriverName,TT.ID TruckTypeID, I.Loaded,
    TT.Description TruckTypeDescription, I.Finished, I.LoadDateTime, I.UnLoadDateTime,
    OA.ID as OrigAdressID,OA.Lng OrigLongitude, OA.Lat OrigLatitude, OA.Address OrigAddress, OA.StreetNumber OrigStreetNumber, OA.City OrigCity, OA.State OrigState,
    DA.ID as DestAdressID,DA.Lng DestLongitude, DA.Lat DestLatitude, DA.Address DestAddress, DA.StreetNumber DestStreetNumber , DA.City DestCity, DA.State DestState

    FROM DRIVERS D
    inner join ITINERARIES I on I.FK_DRIVERS = D.ID
    inner join Addresses OA on OA.ID = I.FK_Dest_Addresses
    inner join Addresses DA on DA.ID = I.FK_Origin_Addresses
    inner join trucktypes TT on TT.ID = I.FK_TruckType
    WHERE
		(Finished IS NULL OR I.Finished = Finished) AND
		(Loaded IS NULL OR I.Loaded = Loaded) AND
        (InitialLoadPeriod IS NULL OR I.LoadDateTime >= InitialLoadPeriod ) AND
        (FinalLoadPeriod IS NULL OR I.LoadDateTime <= FinalLoadPeriod) AND
        (FK_TruckType IS NULL OR I.FK_TruckType = FK_TruckType) AND
        (OAState IS NULL OR OA.State = OAState) AND
        (OACity IS NULL OR OA.City = OACity) AND
        (DAState IS NULL OR DA.State = DAState) AND
        (DACity IS NULL OR DA.City = DACity) AND
        (ID IS NULL OR I.ID = ID);
END;

CREATE DEFINER=`admin`@`%` PROCEDURE `GetItinerariesGroupedByDay`(
	IN InitialLoadPeriod DATETIME,
    IN FinalLoadPeriod DATETIME,
    IN Loaded BOOL
)
BEGIN
	IF(InitialLoadPeriod IS NULL  OR FinalLoadPeriod IS NULL)
    THEN
		SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'NULL is not allowed.';
	END IF;

SELECT DATE(I.LoadDateTime) AS Period,
       COUNT(*) AS Itineraries
  FROM Itineraries I
  WHERE
	(InitialLoadPeriod IS NULL OR I.LoadDateTime >= InitialLoadPeriod ) AND
	(FinalLoadPeriod IS NULL OR I.LoadDateTime <= FinalLoadPeriod) AND
    (Loaded IS NULL OR I.Loaded = Loaded)
 GROUP BY DATE(I.LoadDateTime)
 ORDER BY DATE(I.LoadDateTime);
END;

CREATE DEFINER=`admin`@`%` PROCEDURE `GetItinerariesGroupedByMonth`(
	IN InitialLoadPeriod DATETIME,
    IN FinalLoadPeriod DATETIME,
    IN Loaded BOOL
)
BEGIN
	IF(InitialLoadPeriod IS NULL  OR FinalLoadPeriod IS NULL)
    THEN
		SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'NULL is not allowed.';
	END IF;

SELECT DATE_FORMAT(I.LoadDateTime, '%Y-%m') AS Period,
       COUNT(*) AS Itineraries
  FROM Itineraries I
  WHERE
	(InitialLoadPeriod IS NULL OR I.LoadDateTime >= InitialLoadPeriod ) AND
	(FinalLoadPeriod IS NULL OR I.LoadDateTime <= FinalLoadPeriod) AND
    (Loaded IS NULL OR I.Loaded = Loaded)
 GROUP BY MONTH(DATE(LoadDateTime)),YEAR(DATE(LoadDateTime))
 ORDER BY YEAR(DATE(LoadDateTime)),MONTH(DATE(LoadDateTime));
END;

CREATE DEFINER=`admin`@`%` PROCEDURE `GetItinerariesGroupedByYear`(
	IN InitialLoadPeriod DATETIME,
    IN FinalLoadPeriod DATETIME,
    IN Loaded BOOL
)
BEGIN
	IF(InitialLoadPeriod IS NULL  OR FinalLoadPeriod IS NULL)
    THEN
		SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'NULL is not allowed.';
	END IF;

SELECT DATE_FORMAT(I.LoadDateTime, '%Y') AS Period,
       COUNT(*) AS Itineraries
  FROM Itineraries I

  WHERE
	(InitialLoadPeriod IS NULL OR I.LoadDateTime >= InitialLoadPeriod) AND
	(FinalLoadPeriod IS NULL OR I.LoadDateTime <= FinalLoadPeriod) AND
    (Loaded IS NULL OR I.Loaded = Loaded)
 GROUP BY YEAR(DATE(LoadDateTime))
 ORDER BY YEAR(DATE(LoadDateTime));
END
