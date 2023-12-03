-- Create another database
CREATE DATABASE etl_pipeline;

-- Create a user for the new database
CREATE USER another_user WITH PASSWORD 'another_password';

-- Grant privileges to the new user on the new database
ALTER USER another_user CREATEDB;
GRANT ALL PRIVILEGES ON DATABASE etl_pipeline TO another_user;

--  connect to the etl_pipeline database
\c etl_pipeline;
-- Create table
create table if not exists users
(id int,first_name varchar,last_name varchar,email varchar,hashed_email varchar)