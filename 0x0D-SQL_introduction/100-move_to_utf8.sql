-- Set the default character set and collation for the database
ALTER DATABASE hbtn_0c_0 
CHARACTER SET 'utf8mb4' 
COLLATE 'utf8mb4_unicode_ci';

-- Use the correct database
USE hbtn_0c_0;

-- Convert the table character set and collation
ALTER TABLE first_table 
CONVERT TO CHARACTER SET 'utf8mb4' 
COLLATE 'utf8mb4_unicode_ci';

-- Explicitly modify the `name` column's collation
ALTER TABLE first_table 
MODIFY COLUMN name VARCHAR(256) 
CHARACTER SET 'utf8mb4' 
COLLATE 'utf8mb4_unicode_ci' 
DEFAULT NULL;
