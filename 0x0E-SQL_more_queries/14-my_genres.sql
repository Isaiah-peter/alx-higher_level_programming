-- list genre of Dexter

SELECT g.`name` AS name
FROM `tv_show_genres` AS c
INNER JOIN `tv_genres` AS g
ON c.`genre_id` = g.`id`
INNER JOIN `tv_shows` AS s
ON c.`show_id` = s.`id`
WHERE s.`title` = "Dexter"
ORDER BY g.`name` ASC;
