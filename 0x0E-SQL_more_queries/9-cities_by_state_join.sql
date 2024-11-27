-- Author: Albert Mwanza
-- License: MIT License
-- Version: 1.1
-- Date: 2024-11-26
-- lists all cities  and state names contained in the database hbtn_0d_usa
SELECT C.id, C.name,  S.name 
FROM cities C
JOIN states S ON C.state_id=S.id;