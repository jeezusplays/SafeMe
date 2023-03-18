--
-- Database: safeme
--
DROP DATABASE IF EXISTS safeme;

CREATE DATABASE safeme; -- DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci 
USE safeme;
DROP TABLE IF EXISTS user;

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

-- Table: Location
CREATE TABLE location
(
    locationID int not null auto_increment,
    userID int not null,
    country varchar(60) not null,
    city varchar(60) not null,
    lat decimal(8,6) not null,
    `long` decimal(8,6) not null,
    `timestamp` date not null,
    constraint location_pk primary key (locationID),
    constraint location_fk foreign key (userID) references user(userID)
);

-- Table: Event Log
CREATE TABLE eventLog
(
    logID int not null auto_increment,
    `event` varchar(100) not null, 
    `type` varchar(100) not null,
    userID int not null,
    constraint eventLog_pk primary key (logID)
);

-- Table: Disaster
CREATE TABLE disaster
(
    disasterID int not null auto_increment,
    disasterName varchar(60) not null,
    country varchar(60) not null,
    city varchar(60) not null,
    lat decimal(8,6) not null,
    `long` decimal(8,6) not null,
    `level` varchar(10) not null, -- red, amber, green
    constraint disaster_pk primary key (disasterID)
);

-- Table: Affected Users
CREATE TABLE affectedUsers
(
    affectedUsersID int not null auto_increment,
    disasterID int not null,
    userID int not null,
    userName varchar(60) not null,
    `status` varchar(60) not null,
    contact int not null, -- assume not country code
    constraint affectedUsers_pk primary key (affectedUsersID)
);

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

-- Table: Volunteer
CREATE TABLE volunteer
(
    -- volunteerID int not null,
    volunteerEventID int not null,
    userID int not null,
    userName varchar(30) not null,
    contact int not null,
    `timestamp` date not null,
    constraint volunteer_pk primary key (volunteerEventID, userID),
    -- constraint volunteer_pk primary key (volunteerID),
    constraint volunteer_fk1 foreign key (volunteerEventID) references volunteerEvent(volunteerEventID),
    constraint volunteer_fk2 foreign key (userID) references user(userID)
);
