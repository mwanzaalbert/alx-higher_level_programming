-- Author: Albert Mwanza
-- License: MIT License
-- Version: 1.1
-- Date: 2024-11-26

-- Number of shows by genre
SELECT G.name, COUNT(S.genre_id) AS  number_of_shows
FROM tv_genres G
LEFT JOIN tv_show_genres S ON S.genre_id=G.id
-- WHERE S.genre_id IS NOT NULL
GROUP BY G.name
ORDER BY number_of_shows DESC;