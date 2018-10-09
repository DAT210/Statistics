-- MySQL dump 10.13  Distrib 5.7.23, for Linux (x86_64)
--
-- Host: localhost    Database: statistics
-- ------------------------------------------------------
-- Server version	5.7.23-0ubuntu0.18.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `customer` (
  `customer_id` int(9) NOT NULL AUTO_INCREMENT,
  `f_name` varchar(20) DEFAULT NULL,
  `s_name` varchar(30) DEFAULT NULL,
  `phone` int(11) DEFAULT NULL,
  `birthdate` date DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `c_address` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`customer_id`)
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
INSERT INTO `customer` VALUES (1,'Zachary','Ortiz',14848750,'2006-01-04','samanthajacobs@yahoo.com','092 Holly Passage Apt. 875\nJefferystad, MS 27197'),(2,'Jennifer','Warren',57058801,'1972-12-02','allisonclements@dudley.org','619 Holmes Loop Apt. 073\nPort Dawn, MD 62682'),(3,'Juan','Combs',72681650,'1999-01-20','thomaswalter@delacruz.biz','4057 Carolyn Unions\nWest Scott, ME 81558'),(4,'Cristina','Carr',89434867,'2008-01-28','paul57@drake-doyle.org','9314 Mark Pines\nValerietown, MN 22524'),(5,'William','Clark',2429891,'2003-08-15','mmartin@morris.com','709 Perkins Burgs\nEast Rebecca, OK 17498'),(6,'Judith','Phillips',83271047,'2005-03-25','edward59@yahoo.com','703 Carey Inlet Suite 304\nWatkinsville, PA 64105'),(7,'Kimberly','Forbes',11652679,'2008-09-02','rogersscott@smith.com','4723 Lori Locks\nRebekahtown, CO 50131'),(8,'Aaron','Coleman',85908354,'1980-08-03','stephen15@garcia-smith.info','01504 Cindy Way\nEast Brandy, NE 52362'),(9,'James','Mcpherson',12016890,'2007-12-26','bennettrodney@gmail.com','6463 Brown River\nNew Melissa, ID 18705'),(10,'Lisa','Miller',51917978,'1987-05-28','troberts@meyer.info','980 Byrd Bridge Apt. 151\nAndersonfurt, ME 76313'),(11,'Jennifer','Sanders',89572704,'1996-06-13','melanie63@farley-munoz.com','175 Campbell Union\nSouth Amanda, IL 30533'),(12,'Larry','Johnson',16360433,'1979-10-31','rachel29@gmail.com','20790 Travis Ramp Apt. 489\nEast Michael, AZ 51532'),(13,'Adam','Hamilton',36021291,'2014-01-20','acruz@gmail.com','931 Vincent Circle\nJameshaven, OK 77707'),(14,'Justin','Duncan',27541784,'1997-11-19','apham@yahoo.com','34152 Leon Branch\nSouth Michael, NE 98527'),(15,'Bradley','Green',97956818,'1989-03-09','rachel37@phillips.org','6979 Wright Plaza\nWest Kari, WY 18522'),(16,'Jeffery','Johnson',4904490,'2007-12-22','jeanne35@bean-hughes.com','02762 Amy Burg\nLake Michaelton, IL 28372'),(17,'Kelly','Gonzalez',96363238,'2016-04-18','jerry33@gmail.com','92845 Mendoza Groves\nWest Jim, IA 57601'),(18,'Sarah','Wang',36825974,'1985-02-22','amandaford@yahoo.com','3368 Aaron Alley\nAdambury, LA 66200'),(19,'Timothy','Morgan',53978843,'1991-05-29','douglasjohnston@allen.info','123 Brianna Parkway\nWest Miguelview, DE 90812'),(20,'Wayne','Harper',94255197,'2014-07-21','tanyarichards@yahoo.com','798 Jackson Lakes Apt. 081\nSamanthamouth, MS 73716'),(21,'Jeanette','Martin',72250063,'2013-12-16','andrew46@yahoo.com','0955 Jenna Trail Suite 897\nSimonborough, OH 81945'),(22,'Jason','Hunter',14818593,'1997-10-22','nflores@pearson.net','79191 Wesley Bridge Apt. 070\nWest Catherine, RI 34383'),(23,'Gregory','Stewart',61086360,'2001-06-14','bridgesjames@gmail.com','074 Farmer Mountain Apt. 472\nLake Juan, NE 20147'),(24,'Julie','Velez',51501356,'1989-04-16','joshuajohnson@thompson.info','77149 Jennifer Common\nPort Jacobton, TN 73988'),(25,'David','Davis',82920406,'1979-12-03','pgilbert@yahoo.com','82920 Michael Row Apt. 878\nLake Johnfort, DC 73392'),(26,'Daniel','Ruiz',45437052,'1994-10-28','jonathan94@chang-schaefer.com','2816 Thompson Circle\nWest Anthony, MT 27395'),(27,'Ronnie','Lambert',91033367,'1993-07-02','kjenkins@hall.org','39481 Deborah Center Suite 739\nLake Alicia, MN 81001'),(28,'Rebecca','Escobar',95477766,'2002-05-16','glenda74@yahoo.com','058 Gloria Trail\nSouth Josephstad, VT 80507'),(29,'Robert','Perez',47427397,'1993-01-14','matthewmann@gmail.com','177 Wilson Highway Suite 128\nLake Janiceburgh, MA 14798'),(30,'Brittany','Smith',4615759,'2009-03-15','cooperjames@wilson.com','PSC 7934, Box 4623\nAPO AP 58979'),(31,'Jessica','Turner',67289577,'1993-10-29','kclay@gibson.com','681 Rowe Path\nCameronview, ID 40095'),(32,'Jacqueline','Mccormick',22495144,'1980-10-22','sharonmoss@brown.biz','733 Laura Harbors Suite 756\nEast Kathrynstad, VA 88758'),(33,'Katrina','Bernard',47018976,'1982-07-23','icortez@hansen-thompson.com','89853 Denise Via\nKeithview, NE 08785'),(34,'William','Miller',11849965,'1978-02-18','jrivera@gmail.com','6309 Lauren Underpass Suite 094\nYoungport, KY 26203'),(35,'Daniel','Knapp',68954448,'1987-09-15','smithjose@yahoo.com','15172 Laura Glen Apt. 238\nWest Alicia, ME 88071'),(36,'Sandra','Fuentes',79856175,'2012-11-09','tiffany92@yahoo.com','376 Kim Spring Suite 031\nNorth Michaelstad, NH 44536'),(37,'Ashley','Ewing',88477125,'1988-06-12','stacystone@yahoo.com','9425 Brown Heights\nSeanberg, AK 76544'),(38,'Chelsea','Barnes',48319107,'1992-01-28','rgibson@hotmail.com','7544 Cooley Ferry\nGraystad, FL 47113'),(39,'Kaitlyn','Gamble',98517931,'1972-07-19','jmeyer@gmail.com','8371 Kimberly Court Suite 830\nVargasmouth, KS 54549'),(40,'Mary','Dennis',83231702,'1993-07-24','swright@vazquez.com','1296 Martinez Bypass\nWest Andrew, WI 84291'),(41,'Jason','Carter',11341231,'1986-07-16','hollygreen@evans.com','3139 Dylan Trail\nJacksonborough, MD 80330'),(42,'Crystal','Shaffer',22528321,'2002-05-26','kperez@yahoo.com','10234 Sandra Extensions\nNorth John, ND 43376'),(43,'Bridget','Brooks',42761998,'1999-01-05','leachamy@yahoo.com','26735 Hall Track\nDanielmouth, MO 23773'),(44,'Jason','Brewer',51189747,'1974-01-05','grantsusan@thompson-henson.com','PSC 5809, Box 6949\nAPO AP 75289'),(45,'John','Rodriguez',16651007,'1998-07-16','ginawolf@whitney.biz','9029 Thomas Estate Suite 864\nNorth Meghan, VA 31008'),(46,'Alyssa','Jefferson',48502156,'1980-09-17','jamiewebster@ramos.net','7965 Bryce Well Apt. 696\nNorth Jason, ID 33690'),(47,'Shannon','Webb',24890112,'2002-10-11','jsantiago@gmail.com','9286 Cook Passage Apt. 378\nLake Robertfort, WI 69100'),(48,'Jeremiah','Clark',63155948,'1970-10-07','david19@gmail.com','8008 Skinner Flat Apt. 805\nSullivantown, VT 93508'),(49,'Diana','Howell',837273,'1975-12-03','zfranco@tapia-strickland.biz','69476 Hartman Glen\nEast Samanthaton, TX 78466'),(50,'Christopher','Mullins',54734774,'1978-11-01','foxderrick@hill.com','17518 Brown Fields Suite 868\nWest Brianhaven, DE 06581');
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dish`
--

DROP TABLE IF EXISTS `dish`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dish` (
  `dish_id` int(9) NOT NULL AUTO_INCREMENT,
  `dish_name` varchar(50) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `price` int(9) DEFAULT NULL,
  PRIMARY KEY (`dish_id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dish`
--

LOCK TABLES `dish` WRITE;
/*!40000 ALTER TABLE `dish` DISABLE KEYS */;
INSERT INTO `dish` VALUES (1,'Pepperoni Pizza',816),(2,'Pasta Bolognese',460),(3,'Ribeye',287),(4,'French Onion Soup',605),(5,'Cesar Salad',440),(6,'Fish and Chips',105),(7,'Sushi',840),(8,'Bibimbap',14),(9,'Cheeseburger',33),(10,'Yemista',568),(11,'Roasted Lamb',60);
/*!40000 ALTER TABLE `dish` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orders`
--

DROP TABLE IF EXISTS `orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `orders` (
  `order_id` int(9) NOT NULL AUTO_INCREMENT,
  `time_stamp` time DEFAULT NULL,
  `order_type` varchar(20) DEFAULT NULL,
  `customer_id` int(9) DEFAULT NULL,
  `dish_id` int(9) DEFAULT NULL,
  `delivery` varchar(32) DEFAULT NULL,
  `price` int(9) DEFAULT NULL,
  PRIMARY KEY (`order_id`),
  KEY `dish_id_ibfk1` (`dish_id`),
  KEY `customer_id_ibfk2` (`customer_id`),
  CONSTRAINT `customer_id_ibfk2` FOREIGN KEY (`customer_id`) REFERENCES `customer` (`customer_id`),
  CONSTRAINT `dish_id_ibfk1` FOREIGN KEY (`dish_id`) REFERENCES `dish` (`dish_id`)
) ENGINE=InnoDB AUTO_INCREMENT=251 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders`
--

LOCK TABLES `orders` WRITE;
/*!40000 ALTER TABLE `orders` DISABLE KEYS */;
INSERT INTO `orders` VALUES (1,'18:59:24','inhouse',21,9,'Car',59),(2,'00:14:35','inhouse',38,10,'Car',53),(3,'07:41:01','take-away',31,2,'Car',810),(4,'07:38:55','take-away',11,8,'Customer',63),(5,'16:42:49','inhouse',19,7,'Cycle',854),(6,'08:29:19','inhouse',7,8,'Drone',668),(7,'19:12:13','take-away',38,2,'Car',605),(8,'06:32:13','take-away',19,5,'Cycle',869),(9,'13:51:18','take-away',26,8,'Pickup',642),(10,'05:27:10','inhouse',6,10,'Drone',349),(11,'03:09:33','take-away',9,5,'Car',488),(12,'05:57:15','take-away',29,3,'Cycle',260),(13,'20:32:58','inhouse',37,10,'Cycle',134),(14,'01:47:39','take-away',18,11,'Car',620),(15,'17:16:47','inhouse',46,3,'Cycle',954),(16,'22:12:34','take-away',40,6,'Drone',201),(17,'13:43:12','take-away',32,7,'Customer',81),(18,'13:40:10','take-away',45,6,'Customer',662),(19,'06:36:10','inhouse',29,4,'Cycle',78),(20,'12:05:25','take-away',37,7,'Drone',341),(21,'08:10:49','inhouse',45,11,'Drone',263),(22,'09:17:53','inhouse',48,10,'Customer',540),(23,'10:56:13','take-away',21,1,'Drone',422),(24,'10:36:47','take-away',1,6,'Pickup',432),(25,'22:25:49','take-away',38,7,'Customer',761),(26,'07:25:39','take-away',16,5,'Pickup',619),(27,'23:26:18','inhouse',33,1,'Car',779),(28,'21:25:21','inhouse',24,8,'Pickup',371),(29,'14:01:51','take-away',34,1,'Pickup',648),(30,'13:50:59','take-away',12,1,'Customer',910),(31,'02:26:21','take-away',42,1,'Cycle',923),(32,'00:05:40','inhouse',1,4,'Cycle',680),(33,'00:46:43','inhouse',36,5,'Cycle',305),(34,'09:52:16','inhouse',26,11,'Customer',99),(35,'15:25:24','inhouse',39,9,'Pickup',699),(36,'13:34:03','take-away',33,5,'Customer',910),(37,'06:11:43','take-away',24,5,'Drone',700),(38,'06:07:45','inhouse',37,9,'Customer',320),(39,'02:11:13','take-away',4,9,'Car',605),(40,'04:19:05','take-away',38,2,'Car',588),(41,'14:58:10','take-away',28,5,'Car',802),(42,'08:19:48','take-away',5,5,'Car',794),(43,'19:52:21','inhouse',39,1,'Drone',446),(44,'13:38:03','take-away',22,1,'Car',641),(45,'14:03:48','inhouse',15,9,'Cycle',774),(46,'21:52:41','take-away',37,8,'Pickup',661),(47,'23:49:44','take-away',7,2,'Cycle',698),(48,'22:16:37','take-away',49,1,'Car',354),(49,'09:58:36','take-away',27,5,'Pickup',644),(50,'21:22:37','inhouse',36,6,'Customer',736),(51,'16:32:59','take-away',22,8,'Customer',329),(52,'03:58:41','inhouse',33,6,'Customer',756),(53,'19:55:26','inhouse',22,2,'Pickup',465),(54,'18:03:37','take-away',14,8,'Cycle',582),(55,'16:15:32','take-away',33,8,'Car',682),(56,'16:09:02','inhouse',38,9,'Cycle',103),(57,'20:22:25','inhouse',48,3,'Cycle',252),(58,'21:24:53','inhouse',21,5,'Drone',546),(59,'13:10:03','inhouse',22,10,'Car',356),(60,'00:06:12','inhouse',39,1,'Drone',211),(61,'17:21:31','take-away',20,8,'Customer',196),(62,'08:32:44','take-away',31,1,'Drone',193),(63,'15:20:50','inhouse',41,11,'Drone',274),(64,'03:05:40','take-away',38,2,'Drone',345),(65,'16:16:27','inhouse',37,5,'Cycle',296),(66,'21:22:55','take-away',27,4,'Car',868),(67,'10:37:21','take-away',38,5,'Drone',452),(68,'21:31:58','inhouse',18,6,'Cycle',331),(69,'07:52:39','take-away',5,2,'Cycle',872),(70,'12:07:03','take-away',48,5,'Customer',794),(71,'09:01:32','take-away',23,3,'Cycle',365),(72,'19:54:05','take-away',49,6,'Customer',314),(73,'04:02:20','inhouse',4,2,'Drone',564),(74,'23:47:11','take-away',14,11,'Customer',617),(75,'06:33:59','inhouse',45,9,'Customer',999),(76,'11:21:51','take-away',7,10,'Car',789),(77,'06:24:49','take-away',25,9,'Cycle',685),(78,'19:51:12','inhouse',47,9,'Customer',799),(79,'18:40:33','inhouse',3,7,'Pickup',164),(80,'18:12:33','take-away',23,10,'Drone',291),(81,'17:54:26','inhouse',48,3,'Pickup',616),(82,'17:53:25','take-away',23,8,'Drone',267),(83,'00:34:57','inhouse',1,6,'Customer',656),(84,'14:14:01','take-away',13,3,'Pickup',939),(85,'16:21:31','take-away',4,2,'Drone',668),(86,'14:16:28','take-away',3,3,'Cycle',769),(87,'16:48:58','inhouse',7,11,'Pickup',993),(88,'03:08:38','inhouse',47,7,'Customer',581),(89,'13:40:05','inhouse',44,2,'Car',137),(90,'08:56:42','inhouse',6,5,'Pickup',882),(91,'08:13:50','inhouse',44,4,'Pickup',597),(92,'10:38:04','inhouse',5,1,'Pickup',391),(93,'05:31:15','take-away',24,4,'Pickup',923),(94,'09:35:56','take-away',12,2,'Customer',591),(95,'17:45:10','inhouse',20,1,'Drone',806),(96,'09:55:34','inhouse',41,5,'Drone',857),(97,'10:00:38','take-away',8,5,'Car',91),(98,'10:57:17','inhouse',29,10,'Drone',442),(99,'07:27:01','inhouse',8,6,'Cycle',553),(100,'04:26:30','inhouse',33,9,'Car',617),(101,'19:03:29','take-away',18,7,'Pickup',987),(102,'00:43:29','inhouse',35,7,'Cycle',315),(103,'14:12:32','inhouse',50,8,'Customer',559),(104,'18:55:35','inhouse',26,11,'Cycle',434),(105,'01:18:13','take-away',24,1,'Car',703),(106,'05:54:10','take-away',5,5,'Cycle',90),(107,'18:48:13','inhouse',4,8,'Cycle',322),(108,'07:44:36','take-away',22,8,'Pickup',155),(109,'16:03:48','take-away',24,3,'Car',250),(110,'09:01:56','inhouse',22,2,'Customer',119),(111,'23:23:24','take-away',7,5,'Customer',613),(112,'01:28:50','inhouse',24,4,'Cycle',454),(113,'15:18:11','take-away',25,11,'Car',333),(114,'03:34:44','inhouse',8,2,'Car',424),(115,'22:52:34','inhouse',7,7,'Drone',248),(116,'19:59:28','take-away',26,10,'Customer',419),(117,'16:45:54','take-away',46,1,'Customer',844),(118,'15:06:08','take-away',43,5,'Drone',329),(119,'08:13:32','take-away',27,4,'Drone',402),(120,'21:04:59','take-away',30,6,'Pickup',410),(121,'16:30:20','take-away',26,8,'Customer',180),(122,'11:10:25','take-away',45,4,'Drone',422),(123,'17:49:15','take-away',9,3,'Cycle',449),(124,'04:44:34','take-away',47,10,'Car',999),(125,'12:48:35','inhouse',29,7,'Car',988),(126,'13:03:44','inhouse',11,7,'Drone',158),(127,'18:49:26','take-away',31,10,'Customer',688),(128,'07:34:04','take-away',16,11,'Drone',527),(129,'18:36:44','take-away',17,9,'Customer',769),(130,'22:41:28','inhouse',2,4,'Car',118),(131,'13:18:04','take-away',5,8,'Cycle',459),(132,'07:49:38','take-away',40,9,'Car',764),(133,'06:38:28','inhouse',32,9,'Customer',961),(134,'21:50:10','take-away',41,7,'Pickup',99),(135,'09:44:14','take-away',30,8,'Pickup',910),(136,'16:31:12','inhouse',22,6,'Drone',753),(137,'10:00:57','inhouse',24,3,'Cycle',515),(138,'22:07:33','inhouse',4,5,'Car',272),(139,'17:36:50','inhouse',23,4,'Pickup',819),(140,'20:23:53','inhouse',33,2,'Car',250),(141,'04:54:46','take-away',5,10,'Cycle',450),(142,'12:15:00','take-away',30,8,'Pickup',894),(143,'21:39:13','take-away',9,11,'Drone',112),(144,'08:20:04','inhouse',29,5,'Pickup',998),(145,'12:35:37','take-away',17,6,'Customer',764),(146,'04:01:21','inhouse',4,3,'Drone',329),(147,'18:37:23','inhouse',49,8,'Cycle',361),(148,'14:27:52','take-away',43,11,'Car',843),(149,'01:06:38','take-away',29,10,'Car',923),(150,'13:12:54','take-away',45,1,'Pickup',754),(151,'03:19:12','inhouse',30,2,'Pickup',198),(152,'18:23:11','take-away',4,7,'Drone',778),(153,'02:40:14','inhouse',17,3,'Drone',322),(154,'20:48:40','inhouse',8,1,'Cycle',422),(155,'22:02:55','take-away',9,6,'Cycle',748),(156,'14:48:44','inhouse',14,5,'Cycle',219),(157,'06:19:19','take-away',22,2,'Pickup',905),(158,'18:28:53','inhouse',35,7,'Drone',284),(159,'13:10:31','inhouse',32,9,'Customer',307),(160,'02:16:56','inhouse',18,8,'Customer',125),(161,'00:31:53','inhouse',38,9,'Pickup',386),(162,'05:12:51','inhouse',8,8,'Customer',378),(163,'03:06:19','take-away',46,3,'Pickup',732),(164,'18:27:39','take-away',21,5,'Customer',92),(165,'17:07:00','inhouse',42,9,'Car',318),(166,'08:35:07','take-away',12,4,'Cycle',899),(167,'16:40:38','inhouse',19,10,'Drone',190),(168,'20:06:22','inhouse',40,7,'Car',618),(169,'01:50:39','inhouse',39,11,'Customer',566),(170,'17:51:07','take-away',24,8,'Drone',461),(171,'13:56:57','inhouse',30,8,'Cycle',521),(172,'23:51:21','take-away',43,10,'Pickup',543),(173,'19:13:03','inhouse',50,6,'Customer',157),(174,'03:38:07','take-away',2,10,'Pickup',249),(175,'21:01:18','take-away',46,7,'Drone',269),(176,'03:04:08','inhouse',28,8,'Cycle',937),(177,'04:33:35','take-away',40,6,'Customer',977),(178,'20:58:02','take-away',37,11,'Cycle',908),(179,'12:21:26','take-away',26,1,'Pickup',467),(180,'03:14:09','inhouse',21,8,'Pickup',822),(181,'20:02:04','take-away',6,8,'Pickup',116),(182,'03:00:27','take-away',27,8,'Drone',307),(183,'20:34:16','inhouse',34,10,'Cycle',295),(184,'23:10:43','take-away',45,10,'Pickup',579),(185,'07:09:04','take-away',21,3,'Car',202),(186,'08:51:52','inhouse',16,5,'Customer',964),(187,'22:56:12','inhouse',29,4,'Cycle',708),(188,'11:56:39','take-away',2,11,'Drone',674),(189,'07:57:12','take-away',35,4,'Car',317),(190,'20:30:56','inhouse',31,7,'Customer',86),(191,'20:07:48','inhouse',40,10,'Pickup',82),(192,'07:37:03','inhouse',26,7,'Drone',685),(193,'10:30:59','inhouse',46,10,'Customer',180),(194,'14:12:26','inhouse',32,10,'Car',981),(195,'18:27:40','take-away',4,6,'Customer',171),(196,'14:16:27','take-away',8,11,'Pickup',815),(197,'19:33:28','take-away',47,7,'Pickup',562),(198,'03:17:33','inhouse',7,10,'Drone',227),(199,'04:38:54','inhouse',49,7,'Cycle',500),(200,'00:20:21','inhouse',36,8,'Pickup',733),(201,'04:00:57','take-away',48,4,'Customer',538),(202,'13:05:15','inhouse',19,11,'Drone',427),(203,'20:17:06','take-away',32,10,'Cycle',245),(204,'07:19:29','inhouse',19,6,'Customer',639),(205,'01:15:20','take-away',49,9,'Car',927),(206,'06:04:30','inhouse',6,8,'Customer',912),(207,'18:55:57','inhouse',3,10,'Customer',144),(208,'14:48:04','inhouse',10,3,'Drone',913),(209,'07:00:46','take-away',26,8,'Pickup',753),(210,'16:18:59','take-away',33,8,'Cycle',789),(211,'21:17:36','inhouse',43,5,'Car',679),(212,'12:40:54','take-away',43,10,'Drone',72),(213,'10:12:06','inhouse',22,2,'Pickup',407),(214,'12:55:10','inhouse',5,2,'Customer',298),(215,'11:08:26','inhouse',10,8,'Car',651),(216,'05:52:55','take-away',25,1,'Customer',51),(217,'14:22:03','take-away',18,10,'Cycle',111),(218,'07:13:18','take-away',9,7,'Car',777),(219,'17:37:15','inhouse',25,2,'Drone',222),(220,'13:47:22','take-away',6,7,'Pickup',212),(221,'23:21:41','take-away',12,1,'Drone',640),(222,'22:31:47','inhouse',40,10,'Cycle',858),(223,'07:13:10','take-away',29,3,'Cycle',402),(224,'05:38:53','take-away',38,10,'Customer',302),(225,'13:23:49','inhouse',19,7,'Drone',107),(226,'01:10:02','inhouse',26,5,'Cycle',984),(227,'10:46:46','inhouse',40,6,'Pickup',393),(228,'11:09:34','inhouse',15,5,'Cycle',977),(229,'05:30:12','take-away',13,2,'Pickup',715),(230,'18:20:17','inhouse',48,7,'Pickup',498),(231,'02:53:30','take-away',41,1,'Car',66),(232,'10:04:08','inhouse',31,9,'Pickup',775),(233,'05:10:14','take-away',25,10,'Customer',743),(234,'11:15:58','inhouse',34,5,'Pickup',839),(235,'19:34:08','take-away',45,4,'Cycle',535),(236,'02:24:17','inhouse',2,1,'Cycle',345),(237,'04:48:22','take-away',30,10,'Drone',319),(238,'14:52:32','take-away',22,4,'Customer',707),(239,'06:37:33','inhouse',11,8,'Cycle',230),(240,'05:36:40','inhouse',27,9,'Customer',94),(241,'01:13:01','take-away',42,9,'Customer',509),(242,'19:07:04','inhouse',22,10,'Cycle',955),(243,'03:11:27','inhouse',28,3,'Pickup',156),(244,'06:17:22','inhouse',40,11,'Drone',602),(245,'23:26:17','take-away',13,5,'Drone',807),(246,'18:03:26','take-away',4,5,'Cycle',747),(247,'17:46:41','inhouse',27,8,'Customer',990),(248,'13:33:16','take-away',4,2,'Drone',557),(249,'15:51:39','inhouse',27,11,'Cycle',409),(250,'21:08:58','inhouse',27,3,'Cycle',156);
/*!40000 ALTER TABLE `orders` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-10-09  9:37:04
