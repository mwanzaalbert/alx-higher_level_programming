-- Author: Albert Mwanza
-- License: MIT License
-- Version: 1.1
-- Date: 2024-11-26
-- list Genre ID by show
SELECT S.title, G.genre_id
FROM tv_shows S
RIGHT JOIN tv_show_genres G ON G.show_id=S.id
ORDER BY S.title, G.genre_id ASC;
