-- Genre ID for all shows
SELECT S.title, G.genre_id
FROM tv_shows S
LEFT JOIN tv_show_genres G ON G.show_id=S.id
ORDER BY S.title, G.genre_id ASC;
