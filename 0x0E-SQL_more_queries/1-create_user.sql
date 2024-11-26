-- Check if the user already exists
SELECT EXISTS(SELECT 1 FROM mysql.user WHERE user = 'user_0d_1') INTO @user_exists;

-- If the user does not exist, create the user and grant privileges
IF @user_exists = 0 THEN
    CREATE USER 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
    GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;
    FLUSH PRIVILEGES;
END IF;
