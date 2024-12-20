-- Author: Albert Mwanza
-- License: MIT License
-- Version: 1.1
-- Date: 2024-11-26
-- create the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa) on your MySQL server.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states(
id INT NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY,
name VARCHAR(256) NOT NULL);