-- Write a script that creates the database hbtn_0d_2 and the user user_0d_2.
CREATE DATABASE hbtn_0d_2;
CREATE USER IF NOT EXISTS 'USER_0D_2' IDENTIFIED BY 'user_0d_2_pwd';
GRANT select ON hbtn_0d_2.* TO 'USER_0d_2'@'localhost';
