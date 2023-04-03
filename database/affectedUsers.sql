CREATE DATABASE IF NOT EXISTS safeme;
USE safeme;

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
