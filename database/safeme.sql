--
-- Database: safeme
--
DROP DATABASE IF EXISTS safeme;

CREATE DATABASE safeme; -- DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci 
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

-- Table: Location
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

-- Table: Event Log
CREATE TABLE eventLog
(
    logID int not null auto_increment,
    `event` varchar(100) not null, 
    `type` varchar(100) not null,
    userID int not null,
    constraint eventLog_pk primary key (logID)
);

-- Insert 10 rows into the eventLog table, referencing disaster table
INSERT INTO eventLog (logID, `event`, `type`, userID)
VALUES
  (1, 'Hurricane Ida 2021-08-29 12:00:00', 'disasterAlert', 1),
  (2, 'user status: injured', 'userStatus', 1),
  (3, "Created volunteer event ID 1, Hurricane Relief 2021 Red Cross, ", 'createVolunteerEvent', 11),
  (4,  "Sign up for volunteer event ID 1, Hurricane Relief 2021 Red Cross", 'userVolunteerEvent', 2),
  (5, "Sign up for volunteer event ID 1, Hurricane Relief 2021 Red Cross", 'userVolunteerEvent', 3);

-- Table: Disaster
CREATE TABLE disaster
(
    disasterID int not null auto_increment,
    disasterName varchar(60) not null,
    country varchar(60) not null,
    city varchar(60) not null,
    lat decimal(8,3) not null,
    `long` decimal(8,3) not null,
    disasterSeverityLevel varchar(10) not null, -- red, amber, green
    disasterTimestamp timestamp not null,
    constraint disaster_pk primary key (disasterID)
);

-- Insert 10 rows into the disaster tables in 2021
INSERT INTO disaster (disasterID, disasterName, country, city, lat, `long`, disasterSeverityLevel, disasterTimestamp) VALUES
(1, 'Hurricane Ida', 'United States', 'Louisiana', 29.951, -90.072, 'red', '2021-08-29 12:00:00'),
(2, 'Wildfires in California', 'United States', 'California', 36.778, -119.418, 'red', '2021-09-07 15:30:00'),
(3, 'Floods in Europe', 'Germany', 'Cologne', 50.938, 6.960, 'red', '2021-07-12 08:00:00'),
(4, 'Tropical Cyclone Seroja', 'Indonesia', 'East Nusa Tenggara', -8.584, 121.142, 'red', '2021-04-05 18:00:00'),
(5, 'Floods in China', 'China', 'Zhengzhou', 34.747, 113.625, 'red', '2021-07-20 06:00:00'),
(6, 'Typhoon Chanthu', 'China', 'Shanghai', 31.230, 121.474, 'red', '2021-09-12 02:00:00'),
(7, 'Earthquake in Haiti', 'Haiti', 'Les Cayes', 18.200, -73.750, 'red', '2021-08-14 08:30:00'),
(8, 'Tornadoes in Alabama', 'United States', 'Alabama', 32.318, -86.902, 'red', '2021-03-25 12:00:00'),
(9, 'Heatwave in Italy', 'Italy', 'Sicily', 37.600, 14.015, 'red', '2021-08-06 14:00:00'),
(10, 'Flash floods in Arizona', 'United States', 'Arizona', 34.049, -111.094, 'red', '2021-07-14 10:00:00'),
(11, 'Volcanic eruption in Iceland', 'Iceland', 'Reykjavik', 64.147, -21.943, 'red', '2021-03-19 19:00:00'),
(12, 'Landslide in India', 'India', 'Himachal Pradesh', 31.105, 77.173, 'red', '2021-08-02 05:30:00'),
(13, 'Tornadoes in Texas', 'United States', 'Texas', 31.969, -99.902, 'red', '2021-05-03 09:00:00'),
(14, 'Drought in Brazil', 'Brazil', 'Minas Gerais', -18.512, -44.555, 'red', '2021-08-23 16:00:00'),
(15, 'Flooding in Bangladesh', 'Bangladesh', 'Dhaka', 23.810, 90.413, 'red', '2021-08-08 11:00:00');


-- Table: Affected Users
CREATE TABLE affectedUsers
(
    affectedUsersID int not null auto_increment,
    disasterID int not null,
    userID int not null,
    userName varchar(60) not null,
    `status` varchar(60) not null,
    contact int not null, -- assume no country code
    constraint affectedUsers_pk primary key (affectedUsersID)
);

-- Insert 10 rows into the affectedUsers table, referencing disaster and user table
INSERT INTO affectedUsers (affectedUsersID, disasterID, userID, userName, status, contact)
VALUES
(1, 1, 1, 'John', 'safe', 8888888),
(2, 1, 2, 'Jane', 'injured', 8888888),
(3, 1, 3, 'Bob', 'safe', 8888888),
(4, 1, 4, 'Alice', 'injured', 8888888),
(5, 2, 5, 'Michael', 'safe', 8888888),
(6, 2, 6, 'Maria', 'injured', 8888888),
(7, 2, 7, 'Juan', 'safe', 8888888),
(8, 3, 8, 'Luis', 'injured', 8888888),
(9, 3, 9, 'Sophie', 'safe', 8888888),
(10, 3, 10, 'Mohd', 'injured', 8888888);

-- Table: Volunteer Event
CREATE TABLE volunteerEvent
(
    volunteerEventID int not null auto_increment,
    volunteerEventName varchar(60) not null,
    institute varchar(60) not null,
    disasterID int not null,
    -- userID int not null,
    constraint volunteerEvent_pk primary key (volunteerEventID)
);

-- Insert 10 rows into the volunteerEvent table
INSERT INTO volunteerEvent (volunteerEventID, volunteerEventName, institute, disasterID)
VALUES
  (1, 'Hurricane Relief 2021', 'Red Cross', 1),
  (2, 'Earthquake Relief 2021', 'UNICEF', 2),
  (3, 'Tropical Cyclone Relief 2021', 'Save the Children', 3),
  (4, 'Wildfire Relief 2021', 'World Wildlife Fund', 4),
  (5, 'Flood Relief 2021', 'Oxfam', 5),
  (6, 'Tsunami Relief 2021', 'Doctors Without Borders', 6),
  (7, 'Drought Relief 2021', 'CARE', 7),
  (8, 'Pandemic Relief 2021', 'WHO', 8),
  (9, 'Typhoon Relief 2021', 'Mercy Corps', 9),
  (10, 'Volcano Relief 2021', 'Greenpeace', 10);

-- Table: Volunteer
CREATE TABLE volunteer
(
    -- volunteerID int not null,
    volunteerEventID int not null,
    userID int not null,
    userName varchar(60) not null,
    contact int not null,
    `timestamp` timestamp not null,
    constraint volunteer_pk primary key (volunteerEventID, userID)
    -- constraint volunteer_pk primary key (volunteerID),
    -- constraint volunteer_fk1 foreign key (volunteerEventID) references volunteerEvent(volunteerEventID),
    -- constraint volunteer_fk2 foreign key (userID) references user(userID)
);

-- Insert 10 rows into the volunteer table, referencing the volunteerEvent table
INSERT INTO volunteer (volunteerEventID, userID, userName, contact, `timestamp`)
VALUES
    (1, 1, 'John', 8888888, '2021-03-15'),
    (1, 2, 'Jane', 8888888, '2021-03-15'),
    (1, 3, 'Bob', 8888888, '2021-03-15'),
    (2, 4, 'Alice', 8888888, '2021-04-20'),
    (2, 5, 'Michael', 8888888, '2021-04-20'),
    (2, 6, 'Maria', 8888888, '2021-04-20'),
    (3, 7, 'Juan', 8888888, '2021-05-10'),
    (3, 8, 'Luis', 8888888, '2021-05-10'),
    (4, 9, 'Sophie', 8888888, '2021-06-05'),
    (5, 10, 'Mohd', 8888888, '2021-07-01');