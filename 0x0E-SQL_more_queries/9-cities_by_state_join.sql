-- lists all the cities of California that can be found in the database hbtn_0d_usa using subquery
SELECT C.id, C.name,  S.name 
FROM cities C
JOIN states S ON C.state_id=S.id;