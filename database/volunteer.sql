CREATE DATABASE IF NOT EXISTS safeme;
USE safeme;

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
    (2, 2, 'Jane', 8888888, '2021-03-15'),
    (3, 3, 'Bob', 8888888, '2021-03-15'),
    (4, 4, 'Alice', 8888888, '2021-04-20'),
    (5, 5, 'Michael', 8888888, '2021-04-20'),
    (1, 6, 'Maria', 8888888, '2021-04-20'),
    (1, 7, 'Juan', 8888888, '2021-05-10'),
    (1, 8, 'Luis', 8888888, '2021-05-10'),
    (1, 9, 'Sophie', 8888888, '2021-06-05'),
    (1, 10, 'Mohd', 8888888, '2021-07-01');