-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS pillpocket_test_db;

-- Create the user if it doesn't exist
CREATE USER IF NOT EXISTS 'pillpocket_test'@'localhost' IDENTIFIED BY 'Pillpocket_Test@2024!';

-- Grant all privileges on pillpocket_test_db to the user pillpocket_test
GRANT ALL PRIVILEGES ON pillpocket_test_db.* TO 'pillpocket_test'@'localhost';

-- Grant SELECT privilege on performance_schema to the user pillpocket_test
GRANT SELECT ON performance_schema.* TO 'pillpocket_test'@'localhost';

-- Flush privileges to apply the changes
FLUSH PRIVILEGES;

