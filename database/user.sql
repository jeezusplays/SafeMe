CREATE DATABASE IF NOT EXISTS safeme;
USE safeme;

-- Table: User
CREATE TABLE user
(
  userID int not null auto_increment,
  userName varchar(60) not null,
  familyID int not null, -- assume always 1 (missing Family table)
  age int not null,
  country varchar(60) not null,
  email varchar(60) not null,
  contact int not null, -- assume no country code etc
  constraint user_pk primary key (userID)
);

-- Insert 10 rows into the user table from top 10 natural disaster countries in 2021
INSERT INTO user (userID, userName, familyID, age, country, email, contact)
VALUES
  (1, 'John', 1, 30, 'United States', 'joeytanbiz@gmail.com', 8888888),
  (2, 'Jane', 1, 25, 'Indonesia', 'hongxiangliow@gmail.com', 8888888),
  (3, 'Bob', 1, 35, 'India', 'hx24000@gmail.com', 8888888),
  (4, 'Alice', 1, 28, 'China', 'alice@aol.com', 8888888),
  (5, 'Michael', 1, 42, 'Philippines', 'michael@outlook.com', 8888888),
  (6, 'Maria', 1, 31, 'Colombia', 'maria@gmail.com', 8888888),
  (7, 'Juan', 1, 37, 'Mexico', 'juan@yahoo.com', 8888888),
  (8, 'Luis', 1, 26, 'Peru', 'luis@hotmail.com', 8888888),
  (9, 'Sophie', 1, 29, 'France', 'sophie@outlook.com', 8888888),
  (10, 'Mohd', 1, 33, 'Malaysia', 'mohd@aol.com', 8888888),
  (11, 'US Government', 999, 99, 'United States', 'joey.tan.2021@scis.smu.edu.sg', 911);
