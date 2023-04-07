CREATE DATABASE IF NOT EXISTS safeme_volunteer;
USE safeme_volunteer;

-- Table: Volunteer Event
DROP TABLE IF EXISTS volunteerevent;
CREATE TABLE volunteerevent
(
    volunteerEventID int not null auto_increment,
    volunteerEventName varchar(60) not null,
    institute varchar(60) not null,
    disasterID int not null,
    -- userID int not null,
    constraint volunteerEvent_pk primary key (volunteerEventID)
);

-- Insert 10 rows into the volunteerEvent table
INSERT INTO volunteerevent (volunteerEventID, volunteerEventName, institute, disasterID)
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
DROP TABLE IF EXISTS volunteer;
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