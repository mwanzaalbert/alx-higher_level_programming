-- Author: Albert Mwanza
-- License: MIT License
-- Version: 1.0
-- Date: 2024-11-27

-- List all genres and their ratings
SELECT G.name, sum(R.rate) AS rating
FROM tv_genres G
JOIN tv_show_genres SG ON SG.genre_id=G.id
JOIN tv_shows T ON T.id=SG.show_id
JOIN tv_show_ratings R ON R.show_id=T.id
GROUP BY G.name
ORDER BY rating DESC;

