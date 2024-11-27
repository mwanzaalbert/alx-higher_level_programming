-- Author: Albert Mwanza
-- License: MIT License
-- Version: 1.0
-- Date: 2024-11-27

-- List all shows without the genre "Comedy"
SELECT T.title
FROM tv_shows T
WHERE T.title NOT IN (
SELECT T.title
FROM tv_shows T
JOIN tv_show_genres S ON S.show_id=T.id
JOIN tv_genres G ON G.id = S.genre_id
WHERE G.name="Comedy")
ORDER BY T.title;