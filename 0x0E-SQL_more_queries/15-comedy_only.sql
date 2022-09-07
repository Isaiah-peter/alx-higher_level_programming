-- list all comedy show

SELECT s.`title` AS title
FROM `tv_show_genres` AS c
INNER JOIN `tv_genres` AS g
ON c.`genre_id` = g.`id`
INNER JOIN `tv_shows` AS s
ON c.`show_id` = s.`id`
WHERE g.`name` = "Comedy"
ORDER BY s.`title` ASC;

