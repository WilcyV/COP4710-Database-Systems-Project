-- COP4710 Final Project
-- Schema file
-- Run this file first.

DROP TRIGGER IF EXISTS avoidDoubleBooking;
DROP VIEW IF EXISTS listUpcomingAppointments;

DROP TABLE IF EXISTS Booking_Account;
DROP TABLE IF EXISTS Booking;
DROP TABLE IF EXISTS Service;
DROP TABLE IF EXISTS Staff;
DROP TABLE IF EXISTS Location;
DROP TABLE IF EXISTS Person;

CREATE TABLE IF NOT EXISTS Person (
      person_id INT AUTO_INCREMENT PRIMARY KEY,
      first_name VARCHAR(50),
      last_name VARCHAR(50),
      email VARCHAR(100) UNIQUE NOT NULL,
      phone VARCHAR(12)
  );

CREATE TABLE IF NOT EXISTS Location (
      location_id INT AUTO_INCREMENT PRIMARY KEY,
      address VARCHAR(80),
      city VARCHAR(40),
      state VARCHAR(80),
      postal_code VARCHAR(10)
  );

CREATE TABLE IF NOT EXISTS Staff (
      StaffID INT AUTO_INCREMENT PRIMARY KEY,
      StaffYrsOfExp INT NOT NULL,
      person_id INT UNIQUE NOT NULL,
      FOREIGN KEY (person_id) REFERENCES Person(person_id)
  );

CREATE TABLE IF NOT EXISTS Service (
      ServiceID INT AUTO_INCREMENT PRIMARY KEY,
      ServiceName VARCHAR(50),
      ServiceDurationInSeconds INT NOT NULL
  );

CREATE TABLE IF NOT EXISTS Booking (
      BookingID INT AUTO_INCREMENT PRIMARY KEY,
      BookingDate DATE DEFAULT (CURRENT_DATE),
      person_id INT NOT NULL,
      ServiceID INT NOT NULL,
      location_id INT NOT NULL,
      StaffID INT NOT NULL,
      FOREIGN KEY (person_id) REFERENCES Person(person_id),
      FOREIGN KEY (ServiceID) REFERENCES Service(ServiceID),
      FOREIGN KEY (location_id) REFERENCES Location(location_id),
      FOREIGN KEY (StaffID) REFERENCES Staff(StaffID)
  );

CREATE TABLE IF NOT EXISTS Booking_Account (
      accountID INT AUTO_INCREMENT PRIMARY KEY,
      accountUsername VARCHAR(50) UNIQUE NOT NULL,
      accountPassword VARCHAR(20) NOT NULL,
      person_id INT UNIQUE NOT NULL,
      FOREIGN KEY (person_id) REFERENCES Person(person_id)
  );

CREATE VIEW listUpcomingAppointments AS
SELECT
    Booking.BookingID,
    Booking.BookingDate,
    Booking.person_id,
    CONCAT(Person.first_name, ' ', Person.last_name) AS StaffName,
    Location.location_id,
    Location.address,
    Location.city,
    Service.ServiceName
FROM Booking
JOIN Staff ON Booking.StaffID = Staff.StaffID
JOIN Person ON Staff.person_id = Person.person_id
JOIN Location ON Booking.location_id = Location.location_id
JOIN Service ON Booking.ServiceID = Service.ServiceID;

DROP TRIGGER IF EXISTS avoidDoubleBooking;

CREATE TRIGGER avoidDoubleBooking
BEFORE INSERT ON Booking
FOR EACH ROW
BEGIN
    IF EXISTS (
          SELECT 1
          FROM Booking
          WHERE BookingDate = NEW.BookingDate
            AND StaffID = NEW.StaffID
      ) THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Staff already booked for this day.';
    END IF;
END;
