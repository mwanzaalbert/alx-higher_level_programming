-- Author: Albert Mwanza
-- License: MIT License
-- Version: 1.1
-- Date: 2024-11-26
-- lists all the cities of California that can be found in the database hbtn_0d_usa using subquery
SELECT id, name FROM 
cities
WHERE state_id=(SELECT id FROM states WHERE name="California");