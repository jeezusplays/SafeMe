CREATE DATABASE IF NOT EXISTS safeme;
USE safeme;

-- Table: Location
DROP TABLE IF EXISTS location;
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
  (1, 'United States', 'New York', -75.324, 4.892, '2023-04-07'),
  (2, 'Indonesia', 'Jakarta', -6.215, 106.845, '2021-01-02'),
  (3, 'India', 'Mumbai', 19.076, 72.878, '2021-01-03'),
  (4, 'China', 'Beijing', 39.904, 116.407, '2021-01-04'),
  (5, 'Philippines', 'Manila', 14.600, 120.984, '2021-01-05'),
  (6, 'Colombia', 'Bogota', 4.711, -74.072, '2021-01-06'),
  (7, 'Mexico', 'Mexico City', 19.433, -99.133, '2021-01-07'),
  (8, 'Peru', 'Lima', -12.046, -77.043, '2021-01-08'),
  (9, 'France', 'Paris', 48.857, 2.352, '2021-01-09'),
  (10, 'Malaysia', 'Kuala Lumpur', 3.139, 101.687, '2021-01-10');
