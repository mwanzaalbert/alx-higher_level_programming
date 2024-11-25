-- alter character set and collocation for database, table and column
ALTER DATABASE hbtn_0c_0 DEFAULT CHARACTER SET 'utf8mb4' DEFAULT COLLATE 'utf8mb4_unicode_ci';
ALTER TABLE IF EXISTS  first_table CONVERT TO CHARACTER SET 'utf8mb4' COLLATE 'utf8mb4_unicode_ci';
ALTER TABLE IF EXISTS  first_table MODIFY IF EXISTS name VARCHAR(256) NULL DEFAULT NULL COLLATE 'utf8mb4_unicode_ci';