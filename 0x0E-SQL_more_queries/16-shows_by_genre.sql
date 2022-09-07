-- list show and genre

SELECT s.`title`, g.`name`
FROM `tv_show_genres` AS c
INNER JOIN `tv_genres` AS g
ON c.`genre_id` = g.`id`
INNER JOIN `tv_shows` AS s
ON c.`show_id` = s.`id`
ORDER BY s.`title` ASC, g.`name` ASC;
