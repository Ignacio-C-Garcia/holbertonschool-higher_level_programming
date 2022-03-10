-- Write a script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
SELECT tv_shows.title AS title FROM tv_shows 
JOIN tv_show_genres
ON tv_show_genres.show_id = tv_shows.id
JOIN tv_genres
ON tv_genres.id = tv_show_genres.genre_id WHERE tv_genres.name="COMEDY"
ORDER BY title ASC;

