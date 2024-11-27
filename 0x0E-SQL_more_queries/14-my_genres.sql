-- Author: Albert Mwanza
-- License: MIT License
-- Version: 1.1
-- Date: 2024-11-27

-- List genres of a given show title
SELECT G.name
FROM tv_genres G
RIGHT JOIN tv_show_genres S ON S.genre_id=G.id
RIGHT JOIN tv_shows T ON S.show_id=T.id
WHERE T.title="Dexter"
ORDER BY G.name;