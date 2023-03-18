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

