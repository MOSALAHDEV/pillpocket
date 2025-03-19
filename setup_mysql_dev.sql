-- Create the PillPocket database if not exists
CREATE DATABASE IF NOT EXISTS pillpocket_dev_db;
-- Create the PillPocket user if not exists
CREATE USER IF NOT EXISTS 'pillpocket_dev'@'localhost' IDENTIFIED BY 'pillpocket_dev_pwd';
-- Grant all privileges to the PillPocket user
GRANT ALL PRIVILEGES ON PillPocket_dev_db.* TO 'pillpocket_dev'@'localhost';
-- Grant SELECT privilages to the user
GRANT SELECT ON performance_schema.* TO 'pillpocket_dev'@'localhost';
-- Flush privileges to apply changes
FLUSH PRIVILEGES;
