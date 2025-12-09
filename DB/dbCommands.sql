INSERT INTO Hotels 
VALUES (0, 'Detroit:BH');
--INSERT INTO Hotels 
--VALUES (0, 'Detroit:BH');
INSERT INTO Hotels 
VALUES (1, 'Саратов');

INSERT INTO RoomClasses  (active, size, cost) 
VALUES (false, 6, 9999999.999);
INSERT INTO RoomClasses
VALUES (2, true, 2, 1000);

SELECT * FROM RoomClasses;

INSERT INTO Coefficients
VALUES (2, 0.9, 1.0, 1.0, 1.0, 1.5, 2.5, 2.0, 2.5);

SELECT * FROM Coefficients;

INSERT INTO Clients
VALUES (0, 'Clain', 'RUS');

SELECT * FROM Clients;

INSERT INTO Reservations
VALUES (0, 0, 0, 2, '2018-05-18 14:00:00', '2019-12-12 11:59:59');
INSERT INTO Reservations
VALUES (-2, 0, 1, 2, '2005-10-18 14:00:00', '2012-12-19 11:59:59');

SELECT * FROM Reservations;

DELETE FROM RoomClasses
WHERE active = false;

SELECT * FROM RoomClasses;

TRUNCATE Coefficients;
DELETE FROM Reservations;

DELETE FROM RoomClasses
WHERE cost < 10000;

--TRUNCATE Hotels;
--TRUNCATE Clients;

DELETE FROM Hotels;
DELETE FROM Clients;
DELETE FROM RoomClasses;


SELECT * FROM Coefficients;
SELECT * FROM Clients;
SELECT * FROM Hotels;
SELECT * FROM RoomClasses;