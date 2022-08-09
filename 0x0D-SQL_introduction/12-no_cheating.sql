-- updates Bob's score to 10 in second table
-- not allowed to use Bob's id

UPDATE second_table
SET score = 10
WHERE name = "Bob";
