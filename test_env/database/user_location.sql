CREATE DATABASE IF NOT EXISTS safeme;
USE safeme;

-- Table: User
DROP TABLE IF EXISTS user;
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

-- Table: Location
DROP TABLE IF EXISTS location;
CREATE TABLE location
(
    locationID int not null auto_increment,
    userID int not null,
    country varchar(60) not null,
    city varchar(60) not null,
    lat decimal(8,3) not null,
    `long` decimal(8,3) not null,
    `timestamp` timestamp not null,
    constraint location_pk primary key (locationID),
    constraint location_fk foreign key (userID) references user(userID)
);

-- Insert 10 rows into the location table, referencing user table
INSERT INTO location (userID, country, city, lat, `long`, `timestamp`)
VALUES
  (1, 'United States', 'New York', 40.713, -74.006, '2021-01-01'),
  (2, 'Indonesia', 'Jakarta', -6.215, 106.845, '2021-01-02'),
  (3, 'India', 'Mumbai', 19.076, 72.878, '2021-01-03'),
  (4, 'China', 'Beijing', 39.904, 116.407, '2021-01-04'),
  (5, 'Philippines', 'Manila', 14.600, 120.984, '2021-01-05'),
  (6, 'Colombia', 'Bogota', 4.711, -74.072, '2021-01-06'),
  (7, 'Mexico', 'Mexico City', 19.433, -99.133, '2021-01-07'),
  (8, 'Peru', 'Lima', -12.046, -77.043, '2021-01-08'),
  (9, 'France', 'Paris', 48.857, 2.352, '2021-01-09'),
  (10, 'Malaysia', 'Kuala Lumpur', 3.139, 101.687, '2021-01-10');
