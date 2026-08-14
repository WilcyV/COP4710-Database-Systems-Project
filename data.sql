-- COP4710 Final Project
-- Sample data file
-- Run this file after Schema.sql.

INSERT INTO Person(first_name, last_name, email, phone)
VALUES
    ('John', 'Doe', 'johndoe@gmail.com', '123-456-7890'),
    ('Lauren', 'Merritt', 'laurenmerritt@gmail.com', '841-308-9831'),
    ('Melody', 'Proctor', 'melodyproctor@gmail.com', '731-834-0922'),
    ('Riley', 'Park', 'rileypark@gmail.com', '912-823-9012'),
    ('Ellen', 'Luna', 'ellenluna@gmail.com', '123-742-9283'),
    ('Tyler', 'Benjamin', 'tylerbenjamin@gmail.com', '939-258-0892'),
    ('Bob', 'Smith', 'bobsmith@gmail.com', NULL);

INSERT INTO Booking_Account(accountUsername, accountPassword, person_id)
VALUES
    ('JDoe', 'ilovecats', 1),
    ('BobSmith', 'secretpassword', 7);

INSERT INTO Staff(StaffYrsOfExp, person_id)
VALUES
    (10, 2),
    (4, 3),
    (0, 5),
    (5, 6),
    (3, 4);

INSERT INTO Service(ServiceName, ServiceDurationInSeconds)
VALUES
    ('Nail care', 900),
    ('Therapy', 1800),
    ('Haircut', 1200),
    ('Massage', 1800);

INSERT INTO Location(address, city, state, postal_code)
VALUES
    ('3782 Tyler Avenue', 'Miami', 'Florida', '33106'),
    ('4798 Ocala Street', 'Orlando', 'Florida', '32801'),
    ('1278 Medical Center Drive', 'Tampa', 'Florida', '33602'),
    ('4932 Alpha Avenue', 'Jacksonville', 'Florida', '32216'),
    ('2575 Woodside Circle', 'Tallahassee', 'Florida', '32301'),
    ('131 Lunetta Street', 'Sarasota', 'Florida', '34240');

-- Sample bookings for proof and query testing.
INSERT INTO Booking(BookingDate, person_id, ServiceID, location_id, StaffID)
VALUES
    ('2026-04-10', 1, 1, 1, 1),
    ('2026-04-11', 1, 3, 2, 2),
    ('2026-04-12', 7, 2, 3, 4),
    ('2026-04-13', 7, 4, 1, 3),
    ('2026-04-14', 1, 2, 2, 5),
    ('2026-04-15', 7, 1, 4, 1);
