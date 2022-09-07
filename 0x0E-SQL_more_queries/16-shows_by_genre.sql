-- list show and genre

SELECT s.`title`, g.`name`
FROM `tv_shows` AS s
INNER JOIN `tv_show_genres` AS c
ON s.`id` = c.`show_id`

INNER JOIN `tv_genres` AS g
ON c.`genre_id` = g.`id`
ORDER BY s.`title` ASC, g.`name` ASC;
