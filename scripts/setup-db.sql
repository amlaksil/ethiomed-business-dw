-- Creates a new user
CREATE USER ethiomed WITH PASSWORD 'password';

-- Create a Database
CREATE DATABASE ethiomed_db;

-- Grant privileges to the new user on the database
GRANT ALL PRIVILEGES ON DATABASE ethiomed_db TO ethiomed;
