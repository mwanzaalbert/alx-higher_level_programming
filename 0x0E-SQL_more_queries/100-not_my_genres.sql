-- Author: Albert Mwanza
-- License: MIT License
-- Version: 1.0
-- Date: 2024-11-27

-- List all genres not linked to show "Dexter"
SELECT G.name
FROM tv_genres G
WHERE G.name NOT IN (
SELECT G.name
FROM tv_shows T
JOIN tv_show_genres S ON S.show_id=T.id
JOIN tv_genres G ON G.id = S.genre_id
WHERE T.title="Dexter")
ORDER BY G.name;