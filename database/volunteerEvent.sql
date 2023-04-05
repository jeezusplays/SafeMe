CREATE DATABASE IF NOT EXISTS volunteerEvent;
USE volunteerEvent;

-- Table: Volunteer Event
DROP TABLE IF EXISTS volunteerEvent;
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