-- MySQL dump 10.16  Distrib 10.1.23-MariaDB, for debian-linux-gnueabihf (armv7l)
--
-- Host: localhost    Database: GarageDoor
-- ------------------------------------------------------
-- Server version       10.1.23-MariaDB-9+deb9u1


--
-- Table structure for table `DoorStatus`
--

DROP TABLE IF EXISTS `DoorStatus`;
CREATE TABLE `DoorStatus` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `Status` varchar(100) COLLATE utf8_bin DEFAULT NULL,
  `TS` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
