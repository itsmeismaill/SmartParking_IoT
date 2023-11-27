-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               8.0.30 - MySQL Community Server - GPL
-- Server OS:                    Win64
-- HeidiSQL Version:             12.1.0.6537
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Dumping database structure for smart_parking
CREATE DATABASE IF NOT EXISTS `smart_parking` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `smart_parking`;

-- Dumping structure for table smart_parking.abonnements
CREATE TABLE IF NOT EXISTS `abonnements` (
  `id` int NOT NULL AUTO_INCREMENT,
  `duree` int NOT NULL DEFAULT '0',
  `montant` decimal(10,2) NOT NULL,
  `initial_duree` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table smart_parking.abonnements: ~2 rows (approximately)
DELETE FROM `abonnements`;
INSERT INTO `abonnements` (`id`, `duree`, `montant`, `initial_duree`) VALUES
	(6, 0, 100.00, 600);

-- Dumping structure for table smart_parking.time_parking
CREATE TABLE IF NOT EXISTS `time_parking` (
  `id` int NOT NULL AUTO_INCREMENT,
  `date_entree` datetime NOT NULL,
  `date_sortie` datetime DEFAULT NULL,
  `vehicule_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_vehicule_time_parking` (`vehicule_id`),
  CONSTRAINT `fk_vehicule_time_parking` FOREIGN KEY (`vehicule_id`) REFERENCES `vehicules` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table smart_parking.time_parking: ~0 rows (approximately)
DELETE FROM `time_parking`;
INSERT INTO `time_parking` (`id`, `date_entree`, `date_sortie`, `vehicule_id`) VALUES
	(35, '2023-11-25 18:48:16', '2023-11-25 18:48:47', 3);

-- Dumping structure for table smart_parking.users
CREATE TABLE IF NOT EXISTS `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `password` varchar(255) NOT NULL,
  `cin` varchar(15) NOT NULL,
  `telephone` varchar(20) NOT NULL,
  `email` varchar(100) NOT NULL,
  `role` enum('client','admin') NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table smart_parking.users: ~3 rows (approximately)
DELETE FROM `users`;
INSERT INTO `users` (`id`, `username`, `password`, `cin`, `telephone`, `email`, `role`) VALUES
	(5, 'a', 'a', 'a', 'a', 'a', 'client'),
	(7, 'admin@admin.ma', '$2b$12$DtKxPr0s2kGEXTB23D9pDe8WPDFYcFiZzzY0.XNedNhtozW9uTJ7C', 'admin', '0677364433', 'mohcine', 'admin');

-- Dumping structure for table smart_parking.vehicules
CREATE TABLE IF NOT EXISTS `vehicules` (
  `id` int NOT NULL AUTO_INCREMENT,
  `matricule` varchar(20) NOT NULL,
  `user_id` int DEFAULT NULL,
  `abonnement_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_user_vehicule` (`user_id`),
  KEY `fk_abonnement_vehicule` (`abonnement_id`),
  CONSTRAINT `fk_abonnement_vehicule` FOREIGN KEY (`abonnement_id`) REFERENCES `abonnements` (`id`),
  CONSTRAINT `fk_user_vehicule` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table smart_parking.vehicules: ~0 rows (approximately)
DELETE FROM `vehicules`;
INSERT INTO `vehicules` (`id`, `matricule`, `user_id`, `abonnement_id`) VALUES
	(3, '72364A5', 5, 6);

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
