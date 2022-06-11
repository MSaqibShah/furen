-- MySQL dump 10.13  Distrib 8.0.26, for Win64 (x86_64)
--
-- Host: localhost    Database: frms
-- ------------------------------------------------------
-- Server version	8.0.26

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `booking`
--

DROP TABLE IF EXISTS `booking`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `booking` (
  `bid` int NOT NULL AUTO_INCREMENT,
  `uid` int NOT NULL,
  `pid` int NOT NULL,
  `bstatus` varchar(10) DEFAULT NULL,
  `bdate` datetime DEFAULT NULL,
  `deliverydate` datetime DEFAULT NULL,
  `quantity` int DEFAULT NULL,
  PRIMARY KEY (`bid`,`uid`,`pid`),
  KEY `uid` (`uid`),
  KEY `pid` (`pid`),
  CONSTRAINT `booking_ibfk_1` FOREIGN KEY (`uid`) REFERENCES `user` (`uid`) ON DELETE CASCADE,
  CONSTRAINT `booking_ibfk_2` FOREIGN KEY (`pid`) REFERENCES `product` (`pid`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `booking`
--

LOCK TABLES `booking` WRITE;
/*!40000 ALTER TABLE `booking` DISABLE KEYS */;
INSERT INTO `booking` VALUES (1,2,50,'PD','2022-01-02 07:13:45',NULL,6),(1,2,52,'PD','2022-01-02 07:13:46',NULL,1),(2,2,50,'PD','2022-01-02 07:18:35',NULL,1),(2,2,52,'PD','2022-01-02 07:20:17',NULL,10);
/*!40000 ALTER TABLE `booking` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cart`
--

DROP TABLE IF EXISTS `cart`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cart` (
  `uid` int NOT NULL,
  `pid` int NOT NULL,
  `quantity` int DEFAULT NULL,
  PRIMARY KEY (`uid`,`pid`),
  KEY `pid` (`pid`),
  CONSTRAINT `cart_ibfk_1` FOREIGN KEY (`uid`) REFERENCES `user` (`uid`) ON DELETE CASCADE,
  CONSTRAINT `cart_ibfk_2` FOREIGN KEY (`pid`) REFERENCES `product` (`pid`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cart`
--

LOCK TABLES `cart` WRITE;
/*!40000 ALTER TABLE `cart` DISABLE KEYS */;
INSERT INTO `cart` VALUES (2,50,1),(3,50,11),(7,50,11),(7,52,6),(8,50,2),(8,52,1),(9,50,109),(9,52,12);
/*!40000 ALTER TABLE `cart` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employee`
--

DROP TABLE IF EXISTS `employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employee` (
  `eid` int NOT NULL AUTO_INCREMENT,
  `ename` varchar(30) DEFAULT NULL,
  `enumber` varchar(15) DEFAULT NULL,
  `eemail` varchar(240) DEFAULT NULL,
  `etype` varchar(20) DEFAULT NULL,
  `esalary` int DEFAULT NULL,
  `esup` int DEFAULT NULL,
  PRIMARY KEY (`eid`),
  KEY `esup` (`esup`),
  CONSTRAINT `employee_ibfk_1` FOREIGN KEY (`esup`) REFERENCES `employee` (`eid`) ON DELETE SET NULL
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee`
--

LOCK TABLES `employee` WRITE;
/*!40000 ALTER TABLE `employee` DISABLE KEYS */;
INSERT INTO `employee` VALUES (1,'saif','11123','mdsaif@abc.com','sales',12000,NULL),(5,'saif','11123','mdsaif@abc.com','sales',12000,1),(6,'sanskaar','21452','abc@gmail.com','type',4512,NULL),(9,'gauruv','21452','abc@gmail.com','type',4512,NULL),(10,'kush','124521','aaaa','A',5000,NULL);
/*!40000 ALTER TABLE `employee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `payment`
--

DROP TABLE IF EXISTS `payment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `payment` (
  `paymentid` int NOT NULL AUTO_INCREMENT,
  `paymentdate` datetime DEFAULT NULL,
  `paymentamount` int DEFAULT NULL,
  `uid` int DEFAULT NULL,
  `eid` int DEFAULT NULL,
  `rid` int DEFAULT NULL,
  PRIMARY KEY (`paymentid`),
  KEY `uid` (`uid`),
  KEY `eid` (`eid`),
  KEY `rid` (`rid`),
  CONSTRAINT `payment_ibfk_1` FOREIGN KEY (`uid`) REFERENCES `user` (`uid`) ON DELETE CASCADE,
  CONSTRAINT `payment_ibfk_2` FOREIGN KEY (`eid`) REFERENCES `employee` (`eid`) ON DELETE SET NULL,
  CONSTRAINT `payment_ibfk_3` FOREIGN KEY (`rid`) REFERENCES `rent` (`rid`) ON DELETE SET NULL
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `payment`
--

LOCK TABLES `payment` WRITE;
/*!40000 ALTER TABLE `payment` DISABLE KEYS */;
INSERT INTO `payment` VALUES (1,'2022-01-01 00:00:00',334,2,1,1);
/*!40000 ALTER TABLE `payment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product`
--

DROP TABLE IF EXISTS `product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `product` (
  `pid` int NOT NULL AUTO_INCREMENT,
  `pname` varchar(50) DEFAULT NULL,
  `pdesc` varchar(500) DEFAULT NULL,
  `ptype` varchar(20) DEFAULT NULL,
  `price` int DEFAULT NULL,
  PRIMARY KEY (`pid`)
) ENGINE=InnoDB AUTO_INCREMENT=53 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product`
--

LOCK TABLES `product` WRITE;
/*!40000 ALTER TABLE `product` DISABLE KEYS */;
INSERT INTO `product` VALUES (50,'p2','dddddddd','b',125),(52,'un2','updated desc','a',51);
/*!40000 ALTER TABLE `product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rent`
--

DROP TABLE IF EXISTS `rent`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `rent` (
  `rid` int NOT NULL AUTO_INCREMENT,
  `rstart` datetime DEFAULT NULL,
  `rend` datetime DEFAULT NULL,
  `pid` int DEFAULT NULL,
  `eid` int DEFAULT NULL,
  `uid` int DEFAULT NULL,
  PRIMARY KEY (`rid`),
  KEY `pid` (`pid`),
  KEY `eid` (`eid`),
  KEY `uid` (`uid`),
  CONSTRAINT `rent_ibfk_1` FOREIGN KEY (`pid`) REFERENCES `product` (`pid`) ON DELETE SET NULL,
  CONSTRAINT `rent_ibfk_2` FOREIGN KEY (`eid`) REFERENCES `employee` (`eid`) ON DELETE SET NULL,
  CONSTRAINT `rent_ibfk_3` FOREIGN KEY (`uid`) REFERENCES `user` (`uid`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rent`
--

LOCK TABLES `rent` WRITE;
/*!40000 ALTER TABLE `rent` DISABLE KEYS */;
INSERT INTO `rent` VALUES (1,'2022-01-01 00:00:00','2022-02-01 00:00:00',50,1,2);
/*!40000 ALTER TABLE `rent` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `uid` int NOT NULL AUTO_INCREMENT,
  `uname` varchar(30) DEFAULT NULL,
  `uemail` varchar(240) DEFAULT NULL,
  `unumber` varchar(15) DEFAULT NULL,
  `uaddress` varchar(250) DEFAULT NULL,
  `ucity` varchar(250) DEFAULT NULL,
  `ustates` varchar(250) DEFAULT NULL,
  `upin` int DEFAULT NULL,
  `_password` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`uid`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (2,'Saqib','saqib@gmail.com','','','','',10520,'$2b$12$w3c.lRsqWF5ZN3ivUxfYHul51JPCa1Gf/0tvdXhvmsofs6paIdteG'),(3,'Gaurav','gaurav@gmail.com','','','','',10520,'$2b$12$I0EeYiRRC5G9i/YJPj.nVOpiYmxMDOm2ZgMTxK9rtbdMwf8aKgptG'),(4,'Kush ','kush@abc.com','123456789','Pg ','bangalore','karnataka',560078,'$2b$12$3z0L/692G2llRgs2akKQb.mc3zCv2PGgcep3yPgWRS0P7rC/vZEre'),(5,'sanskaar','sd@gmail.com','123456789','flat','bangalore','karnataka',560078,'$2b$12$XVFB7HFaokd5Qf2423qNZOZpYE058FcH1hHlnmxXjhCjWMp12eTae'),(6,'asdh','ASDA@FsaM.COM','7006437998','14 R G Baruah Road guwhati','Srinagar','karnataka',560078,'$2b$12$KvuQFNhOm2/CejTTuqaTquiyjCacZEhX74CJFFNVUxEyJIsquVVKe'),(7,'askb','aaa@aaa.com','79787865','aasda','bangalore','ka',560078,'$2b$12$BSlwEgmlAI.E2FvYu9ENX.h3wQyjtcijhF8HgHja6slh7Y5MF71nW'),(8,'aaa','bbb@bbb.com','123','11212ass','54asd','asdasd',454545,'$2b$12$uvdcmQVAEegjn5RiYe8paOB4nRg8gDYR.Ed7dl9aG2GhDifAzzkXG'),(9,'aran','aran@a.com','789','asda','asda','asda',560078,'$2b$12$BUfscikuAyy3Ki.V5kSa2O3s9mPC1Wc0MoPdu85VXyCWO5ck.lrOO'),(10,'moza','moza@a.com','788979','8sdasd','asdas','asdas',560078,'$2b$12$roghYXuhWcyuQm6UM5ih9O6Uq8AnTL84A1SZItS.RbUCT0kBo2ImW');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-01-22  0:10:14
