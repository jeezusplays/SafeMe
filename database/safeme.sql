--
-- Database: `safeme`
--
DROP DATABASE if exists `safeme`;

CREATE DATABASE IF NOT EXISTS `safeme`; -- DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci 
USE `safeme`;
DROP TABLE IF EXISTS `user`;

-- Table: User
CREATE TABLE user
(
  -- column_name data_type() [not null] ,
  `userID` int not null auto_increment,
  `name` varchar(60) not null,
  `familyID` int not null,
  `age` int not null,
  `country` varchar(60) not null
  `email` varchar(60) not null,
  `contact` int not null
  constraint user_pk primary key (`userID`)
  -- constraint table_name_pk primary key (column_name(s)) ,
  -- constraint table_name_fk1 foreign key (column_name) references table_name(column_name)
);

