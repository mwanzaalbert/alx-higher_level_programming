-- Author: Albert Mwanza
-- License: MIT License
-- Version: 1.1
-- Date: 2024-11-26

-- List all genres with the number of shows linked to each
SELECT 
    G.name AS genre, 
    COUNT(S.genre_id) AS number_of_shows
FROM 
    tv_genres G
JOIN 
    tv_show_genres S ON G.id = S.genre_id
GROUP BY 
    G.name
HAVING 
    number_of_shows > 0
ORDER BY 
    number_of_shows DESC;
