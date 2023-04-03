CREATE DATABASE IF NOT EXISTS safeme;
USE safeme;

-- Table: Volunteer
CREATE TABLE volunteer
(
    -- volunteerID int not null,
    volunteerEventID int not null,
    userID int not null,
    userName varchar(60) not null,
    contact int not null,
    `timestamp` date not null,
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