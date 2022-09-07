-- select title from tv_show

SELECT s.`title`, c.`genre_id`
FROM `tv_shows` AS s
INNER JOIN `tv_show_genres` AS c
ON s.`id` = c.`show_id`
WHERE c.`genre_id` IS NULL
ORDER BY s.`title` ASC,  c.`genre_id` ASC;
