CREATE TABLE Checks (
	id SERIAL PRIMARY KEY,
	payment NUMERIC(10,3) NOT NULL
);

CREATE TABLE RoomClasses (
	id SERIAL PRIMARY KEY,
	active BOOLEAN NOT NULL,
	size SMALLINT,
	cost NUMERIC(10,3) NOT NULL
);

CREATE TABLE Coefficients (
	FK_roomClass_id INTEGER PRIMARY KEY,
	mondayCoef NUMERIC(6,3),
	tuesdayCoef NUMERIC(6,3),
	wednesdayCoef NUMERIC(6,3),
	thursdayCoef NUMERIC(6,3),
	fridayCoef NUMERIC(6,3),
	saturdayCoef NUMERIC(6,3),
	sundayCoef NUMERIC(6,3),
	holidayCoef NUMERIC(6,3)
);

CREATE TABLE Hotels (
	id SERIAL PRIMARY KEY,
	city TEXT NOT NULL
);

CREATE TABLE Clients (
	id SERIAL PRIMARY KEY,
	name VARCHAR(100) NOT NULL,
	country CHAR(3) NOT NULL
);

CREATE TABLE Services (
	id SERIAL PRIMARY KEY,
	name TEXT NOT NULL, 
	cost NUMERIC(10,3) NOT NULL
);

CREATE TABLE Rooms (
	id SERIAL PRIMARY KEY,
	FK_roomClass_id INTEGER NOT NULL,
	FK_hotel_id INTEGER NOT NULL,
	number TEXT NOT NULL
);

CREATE TABLE StayInfo (
	--id SERIAL PRIMARY KEY,
	FK_reservation_id INTEGER PRIMARY KEY,
	FK_room_id INTEGER NOT NULL,
	startDate TIMESTAMP,
	endDate TIMESTAMP,
	cost NUMERIC(10,3)
);

CREATE TABLE Reservations (
	id SERIAL PRIMARY KEY,
	FK_client_id INTEGER NOT NULL,
	FK_hotel_id INTEGER NOT NULL,
	--FK_stayInfo_id INTEGER UNIQUE,
	FK_roomClass_id INTEGER NOT NULL,
	startDate TIMESTAMP NOT NULL,
	endDate TIMESTAMP NOT NULL
);

CREATE TABLE Reviews (
	id SERIAL PRIMARY KEY,
	FK_client_id INTEGER NOT NULL,
	createdAt TIMESTAMP NOT NULL,
	message TEXT
);

CREATE TABLE History (
	id SERIAL PRIMARY KEY,
	FK_room_id INTEGER NOT NULL,
	startDate TIMESTAMP NOT NULL,
	endDate TIMESTAMP NOT NULL
);

CREATE TABLE ProvidedServices (
	id SERIAL PRIMARY KEY,
	FK_service_id INTEGER NOT NULL,
	FK_stayInfo_id INTEGER NOT NULL,
	startDate TIMESTAMP NOT NULL,
	endDate TIMESTAMP NOT NULL
);



ALTER TABLE Coefficients 
ADD CONSTRAINT FK_Coefficients_roomClass_id 
	FOREIGN KEY (FK_roomClass_id) 
	REFERENCES RoomClasses(id);


ALTER TABLE Rooms 
ADD CONSTRAINT FK_Rooms_hotel_id 
	FOREIGN KEY (FK_hotel_id) 
	REFERENCES Hotels(id),
--ALTER TABLE Rooms 
ADD CONSTRAINT FK_Rooms_roomClass_id 
	FOREIGN KEY (FK_roomClass_id) 
	REFERENCES RoomClasses(id); 


ALTER TABLE Reservations 
--ADD CONSTRAINT FK_Reservations_stayInfo_id 
--	FOREIGN KEY (FK_stayInfo_id) 
--	REFERENCES StayInfo(id)
--ALTER TABLE Reservations 
ADD CONSTRAINT FK_Reservations_client_id 
	FOREIGN KEY (FK_client_id) 
	REFERENCES Clients(id),
--ALTER TABLE Reservations 
ADD CONSTRAINT FK_Reservations_hotel_id 
	FOREIGN KEY (FK_hotel_id) 
	REFERENCES Hotels(id),
--ALTER TABLE Reservation 
ADD CONSTRAINT FK_Reservations_roomClass_id 
	FOREIGN KEY (FK_roomClass_id) 
	REFERENCES RoomClasses(id); 


ALTER TABLE StayInfo 
ADD CONSTRAINT FK_StayInfo_reservation_id 
	FOREIGN KEY (FK_reservation_id) 
	REFERENCES Reservations(id),
--ALTER TABLE StayInfo 
ADD CONSTRAINT FK_StayInfo_room_id 
	FOREIGN KEY (FK_room_id) 
	REFERENCES Rooms(id);
	

ALTER TABLE Reviews 
ADD CONSTRAINT FK_Reviews_client_id 
	FOREIGN KEY (FK_client_id) 
	REFERENCES Clients(id);
	

ALTER TABLE History 
ADD CONSTRAINT FK_History_room_id 
	FOREIGN KEY (FK_room_id) 
	REFERENCES Rooms(id);
	

ALTER TABLE ProvidedServices 
ADD CONSTRAINT FK_ProvidedServices_stayInfo_id 
	FOREIGN KEY (FK_stayInfo_id) 
	REFERENCES StayInfo(FK_reservation_id),
--ALTER TABLE ProvidedServices
ADD CONSTRAINT FK_ProvidedServices_service_id 
	FOREIGN KEY (FK_service_id) 
	REFERENCES Services(id);