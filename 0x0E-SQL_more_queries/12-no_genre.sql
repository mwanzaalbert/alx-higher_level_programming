-- Author: Albert Mwanza
-- License: MIT License
-- Version: 1.1
-- Date: 2024-11-26
-- Genre ID for all shows
SELECT S.title, G.genre_id
FROM tv_shows S
LEFT JOIN tv_show_genres G ON G.show_id=S.id
WHERE G.genre_id IS NULL;
