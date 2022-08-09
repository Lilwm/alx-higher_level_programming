-- lists all records with score >= 10 in second_table
-- results should display both score and name in order
-- ordered by score

SELECT score, name FROM second_table
WHERE score >= 10
ORDER BY score DESC;
