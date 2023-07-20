-- a script that creates the MySQL server user user_0d_1.
-- Check if the user 'user_0d_1' already exists
SELECT 1 INTO @user_exists
FROM mysql.user
WHERE user = 'user_0d_1' AND host = 'localhost';

-- If the user does not exist, create the user and grant all privileges
SET @sql = IF(@user_exists IS NULL, 'CREATE USER \'user_0d_1\'@\'localhost\' IDENTIFIED BY \'user_0d_1_pwd\';', '');
SET @sql = CONCAT(@sql, 'GRANT ALL PRIVILEGES ON *.* TO \'user_0d_1\'@\'localhost\'; FLUSH PRIVILEGES;');

-- Execute the SQL statements
PREPARE stmt FROM @sql;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;
