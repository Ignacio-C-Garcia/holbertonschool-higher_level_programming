-- Write a script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
SELECT tv_genres.name AS genre, count(tv_show_genres.genre_id) AS number_of_shows FROM tv_show_genres 
JOIN tv_genres
ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.name
ORDER BY number_of_shows DESC;

