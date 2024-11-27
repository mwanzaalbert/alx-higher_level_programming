-- Author: Albert Mwanza
-- License: MIT License
-- Version: 1.1
-- Date: 2024-11-26
-- creates the table id_not_null on MySQL server.
CREATE TABLE if NOT EXISTS id_not_null(
id INT NOT NULL DEFAULT '1',
name VARCHAR(256));