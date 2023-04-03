CREATE DATABASE IF NOT EXISTS safeme;
USE safeme;

-- Table: Disaster
DROP TABLE IF EXISTS disaster;
CREATE TABLE disaster
(
    disasterID int not null auto_increment,
    disasterName varchar(60) not null,
    country varchar(60) not null,
    city varchar(60) not null,
    lat decimal(8,3) not null,
    `long` decimal(8,3) not null,
    disasterSeverityLevel varchar(10) not null, -- red, amber, green
    disasterTimestamp timestamp not null
    constraint disaster_pk primary key (disasterID)
);

-- Insert 10 rows into the disaster tables in 2021
INSERT INTO disaster (disasterID, disasterName, country, city, lat, `long`, disasterSeverityLevel, disasterTimestamp) VALUES
(1, 'Hurricane Ida 2021-08-29 12:00:00', 'United States', 'Louisiana', 29.951, -90.072, 'red', '2021-08-29 12:00:00'),
(2, 'Wildfires in California 2021-09-07 15:30:00', 'United States', 'California', 36.778, -119.418, 'red', '2021-09-07 15:30:00'),
(3, 'Floods in Europe 2021-07-12 08:00:00', 'Germany', 'Cologne', 50.938, 6.960, 'red', '2021-07-12 08:00:00'),
(4, 'Tropical Cyclone Seroja 2021-04-05 18:00:00', 'Indonesia', 'East Nusa Tenggara', -8.584, 121.142, 'red', '2021-04-05 18:00:00'),
(5, 'Floods in China 2021-07-20 06:00:00', 'China', 'Zhengzhou', 34.747, 113.625, 'red', '2021-07-20 06:00:00'),
(6, 'Typhoon Chanthu 2021-09-12 02:00:00', 'China', 'Shanghai', 31.230, 121.474, 'red', '2021-09-12 02:00:00'),
(7, 'Earthquake in Haiti 2021-08-14 08:30:00', 'Haiti', 'Les Cayes', 18.200, -73.750, 'red', '2021-08-14 08:30:00'),
(8, 'Tornadoes in Alabama 2021-03-25 12:00:00', 'United States', 'Alabama', 32.318, -86.902, 'red', '2021-03-25 12:00:00'),
(9, 'Heatwave in Italy 2021-08-06 14:00:00', 'Italy', 'Sicily', 37.600, 14.015, 'red', '2021-08-06 14:00:00'),
(10, 'Flash floods in Arizona 2021-07-14 10:00:00', 'United States', 'Arizona', 34.049, -111.094, 'red', '2021-07-14 10:00:00'),
(11, 'Volcanic eruption in Iceland 2021-03-19 19:00:00', 'Iceland', 'Reykjavik', 64.147, -21.943, 'red', '2021-03-19 19:00:00'),
(12, 'Landslide in India 2021-08-02 05:30:00', 'India', 'Himachal Pradesh', 31.105, 77.173, 'red', '2021-08-02 05:30:00'),
(13, 'Tornadoes in Texas 2021-05-03 09:00:00', 'United States', 'Texas', 31.969, -99.902, 'red', '2021-05-03 09:00:00'),
(14, 'Drought in Brazil 2021-08-23 16:00:00', 'Brazil', 'Minas Gerais', -18.512, -44.555, 'red', '2021-08-23 16:00:00'),
(15, 'Flooding in Bangladesh 2021-08-08 11:00:00', 'Bangladesh', 'Dhaka', 23.810, 90.413, 'red', '2021-08-08 11:00:00');

