-- Author: Albert Mwanza
-- License: MIT License
-- Version: 1.0
-- Date: 2024-11-27

-- List all shows and their ratings
SELECT T.title, sum(R.rate) AS rating
FROM tv_shows T
JOIN tv_show_ratings R ON R.show_id=T.id
GROUP BY T.title
ORDER BY rating DESC;