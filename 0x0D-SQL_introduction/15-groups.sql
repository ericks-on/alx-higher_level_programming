-- with the same score
SELECT DISTINCT score,
(SELECT COUNT(*)
	FROM second_table st2
	WHERE st2.score = st1.score) AS 'number'
FROM second_table AS st1
ORDER BY number DESC;
