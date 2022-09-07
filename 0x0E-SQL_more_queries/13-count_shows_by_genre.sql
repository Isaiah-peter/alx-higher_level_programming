-- more

SELECT g.`name` AS genre,  COUNT(s.`title`) AS number_of_shows
FROM `tv_show_genres` AS c
INNER JOIN `tv_genres` AS g
ON c.`genre_id` = g.`id`
INNER JOIN `tv_shows` AS s
ON c.`show_id` = s.`id`
GROUP BY g.`name`
ORDER BY number_of_shows DESC;
