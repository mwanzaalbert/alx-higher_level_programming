-- lists all the cities of California that can be found in the database hbtn_0d_usa using subquery
SELECT id, name FROM 
cities
WHERE state_id=(SELECT id FROM states WHERE name="California");