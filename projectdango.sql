-- MySQL dump 10.13  Distrib 8.0.38, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: psyc
-- ------------------------------------------------------
-- Server version	8.0.39

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `datos_usuarios`
--

DROP TABLE IF EXISTS `datos_usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `datos_usuarios` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `apellidos` varchar(45) NOT NULL,
  `descripcion` varchar(245) NOT NULL,
  `url_image` varchar(540) NOT NULL,
  `fecha_creacionl` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `fehca_uptade` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `indentificador_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_datos_usuarios_indentificador_idx` (`indentificador_id`),
  CONSTRAINT `fk_datos_usuarios_indentificador` FOREIGN KEY (`indentificador_id`) REFERENCES `indentificador` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `datos_usuarios`
--

LOCK TABLES `datos_usuarios` WRITE;
/*!40000 ALTER TABLE `datos_usuarios` DISABLE KEYS */;
INSERT INTO `datos_usuarios` VALUES (1,'benito ','juarex','hola prueba','gdsfsdfsdfsfd','2024-08-15 23:14:35','2024-08-15 23:14:35',1);
/*!40000 ALTER TABLE `datos_usuarios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `indentificador`
--

DROP TABLE IF EXISTS `indentificador`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `indentificador` (
  `id` int NOT NULL AUTO_INCREMENT,
  `email` varchar(45) NOT NULL,
  `password` varchar(45) NOT NULL,
  `fecha_creacion` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `fecha_uptade` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `type_user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_indentificador_type_user1_idx` (`type_user_id`),
  CONSTRAINT `fk_indentificador_type_user1` FOREIGN KEY (`type_user_id`) REFERENCES `type_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `indentificador`
--

LOCK TABLES `indentificador` WRITE;
/*!40000 ALTER TABLE `indentificador` DISABLE KEYS */;
INSERT INTO `indentificador` VALUES (1,'admin@gmail.com','admin','2024-08-15 23:10:38','2024-08-15 23:10:38',1),(2,'semiadmin','semiadmin','2024-08-15 23:10:38','2024-08-15 23:10:38',2),(3,'usuario','usuario','2024-08-15 23:10:38','2024-08-15 23:10:38',3);
/*!40000 ALTER TABLE `indentificador` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `permisos`
--

DROP TABLE IF EXISTS `permisos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `permisos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `permiso` varchar(45) NOT NULL,
  `fecha_creacion` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `fecha_uptade` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `permisos`
--

LOCK TABLES `permisos` WRITE;
/*!40000 ALTER TABLE `permisos` DISABLE KEYS */;
INSERT INTO `permisos` VALUES (1,'get','2024-08-15 23:12:45','2024-08-15 23:12:45'),(2,'post','2024-08-15 23:12:45','2024-08-15 23:12:45'),(3,'put','2024-08-15 23:12:45','2024-08-15 23:12:45'),(4,'delete','2024-08-15 23:12:45','2024-08-15 23:12:45');
/*!40000 ALTER TABLE `permisos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tipo_permisos_usuarios`
--

DROP TABLE IF EXISTS `tipo_permisos_usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tipo_permisos_usuarios` (
  `type_user_id` int NOT NULL,
  `permisos_id` int NOT NULL,
  PRIMARY KEY (`type_user_id`,`permisos_id`),
  KEY `fk_type_user_has_permisos_permisos1_idx` (`permisos_id`),
  KEY `fk_type_user_has_permisos_type_user1_idx` (`type_user_id`),
  CONSTRAINT `fk_type_user_has_permisos_permisos1` FOREIGN KEY (`permisos_id`) REFERENCES `permisos` (`id`),
  CONSTRAINT `fk_type_user_has_permisos_type_user1` FOREIGN KEY (`type_user_id`) REFERENCES `type_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tipo_permisos_usuarios`
--

LOCK TABLES `tipo_permisos_usuarios` WRITE;
/*!40000 ALTER TABLE `tipo_permisos_usuarios` DISABLE KEYS */;
INSERT INTO `tipo_permisos_usuarios` VALUES (1,1),(1,2),(1,3),(1,4);
/*!40000 ALTER TABLE `tipo_permisos_usuarios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `type_user`
--

DROP TABLE IF EXISTS `type_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `type_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `tipo_usuario` varchar(45) NOT NULL,
  `fecha_creacion` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `fecha_uptade` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `type_user`
--

LOCK TABLES `type_user` WRITE;
/*!40000 ALTER TABLE `type_user` DISABLE KEYS */;
INSERT INTO `type_user` VALUES (1,'admin','2024-08-15 22:16:58','2024-08-15 22:16:58'),(2,'semiadmin','2024-08-15 22:17:41','2024-08-15 22:17:41'),(3,'usuario','2024-08-15 22:17:41','2024-08-15 22:18:14');
/*!40000 ALTER TABLE `type_user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-08-15 23:44:08
