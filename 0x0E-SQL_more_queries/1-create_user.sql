--  creates the MySQL server user user_0d_1
CREATE OR REPLACE USER user_0d_1 IDENTIFIED BY PASSWORD 'user_0d_1_pwd' ;
GRANT ALL ON *.* TO 'user_0d_1'@'localhost';