-- Author: Albert Mwanza
-- License: MIT License
-- Version: 1.1
-- Date: 2024-11-27

-- List only comedy shows
SELECT T.title
FROM tv_shows T
RIGHT JOIN tv_show_genres S ON S.show_id=T.id
RIGHT JOIN tv_genres G ON G.id = S.genre_id
WHERE G.name="Comedy"
ORDER BY T.title;