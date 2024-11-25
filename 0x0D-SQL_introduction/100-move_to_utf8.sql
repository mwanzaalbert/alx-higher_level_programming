-- Set the default character set and collation for the database
ALTER DATABASE hbtn_0c_0 
DEFAULT CHARACTER SET 'utf8mb4' 
DEFAULT COLLATE 'utf8mb4_unicode_ci';

-- Ensure the table uses the correct character set and collation
ALTER TABLE first_table 
CONVERT TO CHARACTER SET 'utf8mb4' 
COLLATE 'utf8mb4_unicode_ci';

-- Modify the `name` column to use the correct collation and definition
ALTER TABLE first_table 
MODIFY COLUMN name VARCHAR(256) 
COLLATE 'utf8mb4_unicode_ci' 
DEFAULT NULL;

-- Add the `score` column if it does not exist
ALTER TABLE first_table 
ADD COLUMN score INT DEFAULT NULL;
