-- COP4710 Final Project
-- constraints_test.sql
-- These queries are expected to FAIL to demonstrate constraint enforcement.

-- Test 1: Violating UNIQUE constraint (duplicate email in Person)
INSERT INTO Person(first_name, last_name, email, phone)
VALUES ('Test', 'User', 'johndoe@gmail.com', '000-000-0000');

-- Expected result:
-- ERROR: Duplicate entry 'johndoe@gmail.com' for key 'email'


-- Test 2: Violating FOREIGN KEY constraint (invalid person_id in Booking)
INSERT INTO Booking(BookingDate, person_id, ServiceID, location_id, StaffID)
VALUES ('2026-05-01', 999, 1, 1, 1);

-- Expected result:
-- ERROR: Cannot add or update a child row: a foreign key constraint fails


-- Test 3: Violating TRIGGER constraint (double booking same staff/date)
INSERT INTO Booking(BookingDate, person_id, ServiceID, location_id, StaffID)
VALUES ('2026-04-10', 2, 1, 1, 1);

-- Expected result:
-- ERROR: Staff already booked for this day.
