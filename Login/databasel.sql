/* include a SQL script to create the database and table.*/

CREATE DATABASE IF NOT EXISTS login_system;
USE login_system;

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
);
