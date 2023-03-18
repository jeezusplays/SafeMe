--
-- Database: `safeme`
--
DROP DATABASE IF EXISTS safeme;

CREATE DATABASE safeme; -- DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci 
USE safeme;
DROP TABLE IF EXISTS user;

-- Table: User
CREATE TABLE user
(
  -- column_name data_type() [not null] ,
  userID int not null auto_increment,
  name varchar(60) not null,
  familyID int not null,
  age int not null,
  country varchar(60) not null,
  email varchar(60) not null,
  contact int not null,
  constraint user_pk primary key (userID)
);

