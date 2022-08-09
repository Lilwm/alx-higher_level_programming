-- creates a table called first_table in the current database
-- If table exists script shouldn't fail

CREATE TABLE IF NOT EXISTS first_table (
	id INT,
	name VARCHAR(256)
	);
