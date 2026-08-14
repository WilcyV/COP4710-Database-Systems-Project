-- COP4710 Final Project
-- queries.sql
-- These queries are written to satisfy the project rubric.

-- Query 1: Multi-table JOIN
SELECT
    b.BookingID,
    b.BookingDate,
    CONCAT(c.first_name, ' ', c.last_name) AS CustomerName,
    s.ServiceName,
    CONCAT(stp.first_name, ' ', stp.last_name) AS StaffName,
    l.city AS LocationCity
FROM Booking b
JOIN Person c ON b.person_id = c.person_id
JOIN Service s ON b.ServiceID = s.ServiceID
JOIN Staff st ON b.StaffID = st.StaffID
JOIN Person stp ON st.person_id = stp.person_id
JOIN Location l ON b.location_id = l.location_id
ORDER BY b.BookingDate;

-- Query 2: GROUP BY with aggregation
SELECT
    s.ServiceName,
    COUNT(*) AS TotalBookings
FROM Booking b
JOIN Service s ON b.ServiceID = s.ServiceID
GROUP BY s.ServiceName
ORDER BY TotalBookings DESC, s.ServiceName;

-- Query 3: Subquery
SELECT
    CONCAT(p.first_name, ' ', p.last_name) AS StaffName,
    st.StaffYrsOfExp
FROM Staff st
JOIN Person p ON st.person_id = p.person_id
WHERE st.StaffYrsOfExp > (
      SELECT AVG(StaffYrsOfExp)
      FROM Staff
  );

-- Query 4: CASE statement
SELECT
    CONCAT(p.first_name, ' ', p.last_name) AS StaffName,
    st.StaffYrsOfExp,
    CASE
        WHEN st.StaffYrsOfExp >= 8 THEN 'Senior'
        WHEN st.StaffYrsOfExp >= 4 THEN 'Mid-level'
        ELSE 'Junior'
    END AS ExperienceLevel
FROM Staff st
JOIN Person p ON st.person_id = p.person_id
ORDER BY st.StaffYrsOfExp DESC;

-- Query 5: Query using the VIEW
SELECT *
FROM listUpcomingAppointments
WHERE person_id = 1
ORDER BY BookingDate;

-- Query 6: Filtering query with multiple conditions
SELECT
    b.BookingID,
    b.BookingDate,
    s.ServiceName,
    l.city
FROM Booking b
JOIN Service s ON b.ServiceID = s.ServiceID
JOIN Location l ON b.location_id = l.location_id
WHERE b.BookingDate >= '2026-04-11'
  AND l.city IN ('Miami', 'Orlando')
ORDER BY b.BookingDate;

-- Query 7: INSERT query
INSERT INTO Booking(BookingDate, person_id, ServiceID, location_id, StaffID)
VALUES ('2026-04-20', 1, 4, 6, 2);

SELECT *
FROM Booking
WHERE BookingDate = '2026-04-20';

-- Query 8: UPDATE query
UPDATE Booking
SET location_id = 5
WHERE BookingID = 1;

SELECT *
FROM Booking
WHERE BookingID = 1;

-- Query 9: Non-trivial logic query
SELECT
    CONCAT(p.first_name, ' ', p.last_name) AS CustomerName,
    COUNT(b.BookingID) AS NumberOfBookings,
    GROUP_CONCAT(DISTINCT s.ServiceName ORDER BY s.ServiceName SEPARATOR ', ') AS ServicesBooked
FROM Person p
JOIN Booking b ON p.person_id = b.person_id
JOIN Service s ON b.ServiceID = s.ServiceID
GROUP BY p.person_id, p.first_name, p.last_name
HAVING COUNT(b.BookingID) >= 2
ORDER BY NumberOfBookings DESC, CustomerName;

-- Optional extra query: DELETE query
-- Delete the most recently inserted practice booking if needed.
DELETE FROM Booking
WHERE BookingDate = '2026-04-20'
  AND person_id = 1
  AND ServiceID = 4
  AND location_id = 6
  AND StaffID = 2;
