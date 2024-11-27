-- Author: Albert Mwanza
-- License: MIT License
-- Version: 1.1
-- Date: 2024-11-27

-- List all shows and their genres
SELECT T.title, G.name
FROM tv_shows T
LEFT JOIN tv_show_genres S ON S.show_id=T.id
LEFT JOIN tv_genres G ON G.id = S.genre_id
ORDER BY T.title, G.name;