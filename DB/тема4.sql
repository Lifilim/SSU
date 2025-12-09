SELECT rooms.number, roomclasses.size, roomclasses.cost AS result 
FROM rooms 
INNER JOIN roomclasses ON rooms.fk_roomclass_id = roomclasses.id;

SELECT rs.number, h.startdate, h.enddate
FROM rooms rs
LEFT JOIN history h ON rs.id = h.fk_room_id;

SELECT rs.number, rcs.size 
FROM rooms rs 
RIGHT JOIN roomclasses rcs ON rs.fk_roomclass_id = rcs.id AND rs.fk_hotel_id = 65;

SELECT *
FROM rooms 
FULL JOIN roomclasses ON rooms.fk_roomclass_id = roomclasses.id;

SELECT *
FROM hotels 
CROSS JOIN roomclasses;

SELECT *
FROM roomclasses rc
CROSS JOIN LATERAL (
    SELECT *
    FROM rooms 
    WHERE rc.id = rooms.fk_roomclass_id
    LIMIT 3
);

--SELECT r1.id, r1.fk_roomclass_id, r1.fk_hotel_id, r1.number AS result
--FROM rooms r1 
--INNER JOIN rooms r2 ON r1.fk_hotel_id = r2.fk_hotel_id AND r1.fk_roomclass_id = r2.fk_roomclass_id
--WHERE r1.fk_roomclass_id <> r2.fk_roomclass_id AND DISTINCT r1.fk_hotel_id, r1.fk_roomclass_id;

SELECT *
FROM roomclasses rc1 
INNER JOIN roomclasses rc2 
ON rc1.active = rc2.active AND rc1.active = true;
--WHERE r1.fk_roomclass_id <> r2.fk_roomclass_id AND DISTINCT r1.fk_hotel_id, r1.fk_roomclass_id;


--------------------------------------------------------------------------------------------------------------------------


SELECT fk_hotel_id, fk_roomclass_id
FROM rooms r
UNION
SELECT fk_hotel_id, fk_roomclass_id
FROM rooms;

(SELECT r.fk_roomclass_id, h.city
FROM rooms r
INNER JOIN hotels h 
ON r.fk_hotel_id = h.id AND r.fk_roomclass_id < 77)
UNION 
(SELECT r.fk_roomclass_id, h.city
FROM rooms r
INNER JOIN hotels h 
ON r.fk_hotel_id = h.id AND r.fk_roomclass_id > 75)
ORDER BY city, fk_roomclass_id;



SELECT fk_hotel_id, fk_roomclass_id
FROM rooms r
UNION ALL
SELECT fk_hotel_id, fk_roomclass_id
FROM rooms;

(SELECT r.fk_roomclass_id, h.city
FROM rooms r
INNER JOIN hotels h 
ON r.fk_hotel_id = h.id AND r.fk_roomclass_id < 77)
UNION ALL
(SELECT r.fk_roomclass_id, h.city
FROM rooms r
INNER JOIN hotels h 
ON r.fk_hotel_id = h.id AND r.fk_roomclass_id > 75)
ORDER BY city, fk_roomclass_id;


(SELECT r.fk_roomclass_id, h.city
FROM rooms r
INNER JOIN hotels h 
ON r.fk_hotel_id = h.id AND r.fk_roomclass_id < 78)
INTERSECT
(SELECT r.fk_roomclass_id, h.city
FROM rooms r
INNER JOIN hotels h 
ON r.fk_hotel_id = h.id AND r.fk_roomclass_id > 74)
ORDER BY city, fk_roomclass_id;

(SELECT r.fk_roomclass_id, h.city
FROM rooms r
INNER JOIN hotels h 
ON r.fk_hotel_id = h.id AND r.fk_roomclass_id < 77)
INTERSECT ALL
(SELECT r.fk_roomclass_id, h.city
FROM rooms r
INNER JOIN hotels h 
ON r.fk_hotel_id = h.id AND r.fk_roomclass_id > 75)
ORDER BY city, fk_roomclass_id;


(SELECT r.fk_roomclass_id, h.city
FROM rooms r
INNER JOIN hotels h 
ON r.fk_hotel_id = h.id AND r.fk_roomclass_id < 77)
EXCEPT
(SELECT r.fk_roomclass_id, h.city
FROM rooms r
INNER JOIN hotels h 
ON r.fk_hotel_id = h.id AND r.fk_roomclass_id > 75)
ORDER BY city, fk_roomclass_id;

(SELECT r.fk_roomclass_id, h.city
FROM rooms r
INNER JOIN hotels h 
ON r.fk_hotel_id = h.id AND r.fk_roomclass_id < 77)
EXCEPT ALL
(SELECT r.fk_roomclass_id, h.city
FROM rooms r
INNER JOIN hotels h 
ON r.fk_hotel_id = h.id AND r.fk_roomclass_id > 75)
ORDER BY city, fk_roomclass_id;


--------------------------------------------------------------------------------------------------------------------------

SELECT * 
FROM roomclasses 
WHERE NOT EXISTS (SELECT 1 FROM rooms WHERE rooms.fk_roomclass_id = roomclasses.id);

SELECT * 
FROM rooms
WHERE fk_roomclass_id IN (SELECT id FROM roomclasses WHERE roomclasses.cost < 5000)
ORDER BY fk_roomclass_id;

SELECT * 
FROM roomclasses 
WHERE roomclasses.cost BETWEEN 3300 AND 5000;

SELECT * 
FROM rooms 
WHERE fk_roomclass_id = ANY (SELECT id 
                             FROM roomclasses 
                             WHERE size < 5);

SELECT * 
FROM roomclasses 
WHERE (SELECT COUNT(*) FROM rooms WHERE rooms.fk_roomclass_id = roomclasses.id) 
      >= ALL ((SELECT COUNT(*) FROM rooms WHERE rooms.fk_roomclass_id = 78)
              UNION 
              (SELECT COUNT(*) FROM rooms WHERE rooms.fk_roomclass_id = 76));

SELECT * 
FROM rooms 
WHERE number LIKE '___' OR number LIKE '%b';

SELECT * 
FROM rooms 
WHERE number ILIKE '%a' OR number ILIKE '%b';

--------------------------------------------------------------------------------------------------------------------------

SELECT id, fk_hotel_id, number,
       CASE WHEN fk_hotel_id = 65 THEN 'столичный' 
            WHEN fk_hotel_id = 66 THEN 'второстоличный' 
            ELSE 'йэта хде ваабсе..?'
       END
FROM rooms;

--------------------------------------------------------------------------------------------------------------------------

SELECT * 
FROM roomclasses 
WHERE cost::text LIKE '_5__.%';

SELECT * 
FROM roomclasses 
WHERE CAST(cost AS text) LIKE '_5__.%';

SELECT fk_roomclass_id, COALESCE(holidaycoef, saturdaycoef, sundaycoef, mondayCoef, 1)
FROM coefficients;

SELECT *
FROM rooms r1 
WHERE NULLIF ((r1.fk_hotel_id, r1.fk_roomclass_id), (65, 74)) IS NOT NULL
ORDER BY r1.fk_hotel_id, r1.fk_roomclass_id;

SELECT r1.id, NULLIF ((r1.fk_hotel_id, r1.fk_roomclass_id), (65, 74))
FROM rooms r1;

SELECT fk_roomclass_id, GREATEST(mondaycoef, tuesdaycoef, wednesdaycoef, thursdaycoef, fridaycoef, saturdaycoef, sundaycoef, holidaycoef)
FROM coefficients;

SELECT fk_roomclass_id, LEAST(mondaycoef, tuesdaycoef, wednesdaycoef, thursdaycoef, fridaycoef, saturdaycoef, sundaycoef, holidaycoef)
FROM coefficients;

--------------------------------------------------------------------------------------------------------------------------

SELECT id, number, LENGTH(number)
FROM rooms;

SELECT number, STRPOS(number, 'A') AS pos_a
FROM rooms
LIMIT 11;

SELECT number, POSITION('B' IN number) AS pos_b
FROM rooms
LIMIT 11;

WITH r AS (SELECT id, number, POSITION('A' IN number) AS pos FROM rooms)
SELECT id, number, OVERLAY (number PLACING 'a' FROM pos FOR LEAST(1, pos))
FROM r
WHERE pos > 0
LIMIT 11;

SELECT id, number, REPLACE (number, 'A', 'a')
FROM rooms
--WHERE number LIKE '%A%'
LIMIT 11;

SELECT id, number
FROM rooms 
WHERE LOWER (SUBSTRING (number FROM LENGTH(number) FOR 1)) BETWEEN 'a' AND 'z'
LIMIT 11;

SELECT id, number, SUBSTRING (number FROM 1 FOR LENGTH(number)) || CHR(65)
FROM rooms 
WHERE NOT (UPPER (SUBSTRING (number FROM LENGTH(number) FOR 1)) BETWEEN 'A' AND 'Z')
LIMIT 11;

SELECT id, number, BTRIM(number, '0123456789')
FROM rooms 
LIMIT 11;

SELECT id, number, LTRIM(number, '0')
FROM rooms;

SELECT id, number, RTRIM(number, 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm')
FROM rooms;

--------------------------------------------------------------------------------------------------------------------------

SELECT NOW();
SELECT CURRENT_DATE;
SELECT CURRENT_TIME; 
SELECT CURRENT_TIMESTAMP;
SELECT LOCALTIMESTAMP;

SELECT * 
FROM history
WHERE enddate < NOW() AND enddate IN (SELECT MAX(enddate) FROM history GROUP BY fk_room_id)
ORDER BY enddate DESC;

SELECT * 
FROM history
WHERE DATE_PART('year', enddate) < EXTRACT(YEAR FROM CURRENT_DATE) 
      AND AGE(startdate, enddate) IN (SELECT MAX(AGE(startdate, enddate))  
                                      FROM history 
                                      WHERE enddate::time <= CURRENT_TIME
                                      GROUP BY fk_room_id
                                      HAVING COUNT(*) > 1)
ORDER BY enddate DESC;



WITH tb AS (
    SELECT rooms.fk_hotel_id, roomclasses.cost 
    FROM roomclasses
    RIGHT JOIN rooms ON rooms.fk_roomclass_id = roomclasses.id
)
SELECT fk_hotel_id, AVG(cost), SUM(cost)
FROM tb
GROUP BY fk_hotel_id
HAVING COUNT(*) > 1;
--------------------------------------------------------------------------------------------------------------------------
