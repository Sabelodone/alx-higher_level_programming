-- Create the database hbtn_0d_2 if it doesn't exist; if it exists, this won't fail.
-- Create the user user_0d_2 with 'user_0d_2_pwd' as the password if the user doesn't exist; won't fail if the user exists.
-- Grant SELECT privilege on all tables within the hbtn_0d_2 database to the user user_0d_2.
-- Refresh the user privileges to ensure the changes take effect.

CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON `hbtn_0d_2`.* TO 'user_0d_2'@'localhost';
FLUSH PRIVILEGES;
