-- lists all records of the table second_table of the database.
-- Don’t list rows without a name value
-- Results should display the score and the name (in this order)

SELECT score, name FROM second_table
WHERE name IS NOT NULL AND name != '' 
ORDER BY score DESC;
