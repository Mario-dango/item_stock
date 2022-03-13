-- MySQL Script generated by MySQL Workbench
-- Fri Mar  4 11:37:38 2022
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

-- --------------------------------------------------------
-- - Se creó al usuario Bawy para acceder a la base de datos correspondiente al departamento de ETEC
-- - 
-- -  create user 'bawy'@'192.168.40.8' identified by 'etec';
-- -  flush privileges;
-- ------------------------------------------------------------


SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema ETEC_lab
-- -----------------------------------------------------
-- Base de datos con el fin de poder generar una mejora en cuanto a la gestión de los ítems multimedia y gestión de reservas.
-- DROP SCHEMA IF EXISTS `ETEC_lab` ;

-- -----------------------------------------------------
-- Schema ETEC_lab
--
-- Base de datos con el fin de poder generar una mejora en cuanto a la gestión de los ítems multimedia y gestión de reservas.
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `ETEC_lab` ;
USE `ETEC_lab` ;

-- -----------------------------------------------------
-- Table `ETEC_lab`.`reservas`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `ETEC_lab`.`reservas` ;

CREATE TABLE IF NOT EXISTS `ETEC_lab`.`reservas` (
  `idreservas` INT NOT NULL,
  `qr_code` INT NULL,
  `profesor` VARCHAR(45) NULL,
  `nombre_item` VARCHAR(45) NULL,
  `hora_i` VARCHAR(45) NULL,
  `hora_f` VARCHAR(45) NULL,
  PRIMARY KEY (`idreservas`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ETEC_lab`.`qr_items`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `ETEC_lab`.`qr_items` ;

CREATE TABLE IF NOT EXISTS `ETEC_lab`.`qr_items` (
  `qr_code` INT NOT NULL COMMENT 'Códigos QR generados por \"terceros\" de la mano de la Universidad de Mendoza.',
  `name_item` VARCHAR(45) NULL DEFAULT 'Sin_nombre' COMMENT 'Columna referida al nombre del ítem, al cual se encuentra adherido código QR correspondiente.',
  `marca_item` VARCHAR(45) NULL DEFAULT 'Sin_marca/fabricante' COMMENT 'Columna para especificar la Marca/Modelo/Fabricante del ítem.',
  `qr_img` BLOB NULL  COMMENT 'Columna para almacenar la imagen generada del QR del ítem.',
  `qr_url_img` VARCHAR(45) NULL DEFAULT 'Sin dirección de imagen' COMMENT 'Columna para especificar la dirección al servidor del ETEC relacionado al QR del ítem.',
  `reservas_idreservas` INT NOT NULL,
  PRIMARY KEY (`qr_code`),
  INDEX `fk_qr_items_reservas_idx` (`reservas_idreservas` ASC) VISIBLE,
  CONSTRAINT `fk_qr_items_reservas`
    FOREIGN KEY (`reservas_idreservas`)
    REFERENCES `ETEC_lab`.`reservas` (`idreservas`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ETEC_lab`.`Labs`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `ETEC_lab`.`Labs` ;

CREATE TABLE IF NOT EXISTS `ETEC_lab`.`Labs` (
  `lab` VARCHAR(45) NOT NULL COMMENT 'Sub-clasificación de los laboratorios (Electrónica, Informática y Ciencias Naturales)',
  `hora_i` VARCHAR(45) NULL COMMENT 'Horario de la reserva generada.',
  `responsable` VARCHAR(45) NULL COMMENT 'Profesor responsable del estado del inmueble.',
  `reservas_idreservas` INT NOT NULL,
  `hora_f` VARCHAR(45) NULL,
  PRIMARY KEY (`lab`),
  INDEX `fk_Labs_reservas1_idx` (`reservas_idreservas` ASC) VISIBLE,
  CONSTRAINT `fk_Labs_reservas1`
    FOREIGN KEY (`reservas_idreservas`)
    REFERENCES `ETEC_lab`.`reservas` (`idreservas`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;







-- -----------------------------------------------------
-- Table `ETEC_lab`.`NADA`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `ETEC_lab`.`nada` ;

CREATE TABLE IF NOT EXISTS `ETEC_lab`.`nada` (
  `medio_modulo` INT NOT NULL,
  `Lunes` VARCHAR(45) NULL,
  `Martes` VARCHAR(45) NULL,
  `Miercoles` VARCHAR(45) NULL,
  `Jueves` VARCHAR(45) NULL,
  `Viernes` VARCHAR(45) NULL,
  `Hora` VARCHAR(45) NULL,
  `reservas_idreservas` INT NOT NULL,
  PRIMARY KEY (`medio_modulo`),
  INDEX `fk_nada_reservas1_idx` (`reservas_idreservas` ASC) VISIBLE,
  CONSTRAINT `fk_nada_reservas1`
    FOREIGN KEY (`reservas_idreservas`)
    REFERENCES `ETEC_lab`.`reservas` (`idreservas`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

insert into etec_lab.nada (medio_modulo, Lunes, Martes, Miercoles, Jueves, Viernes, Hora, reservas_idreservas)
values
	  ("1", "NADA", "NADA", "NADA", "NADA", "NADA", "7:45 a 8:25", "1"),
    ("2", "NADA", "NADA", "NADA", "NADA", "NADA", "8:25 a 9:05", "2"),
    ("3", "NADA", "NADA", "NADA", "NADA", "NADA", "9:15 a 9:55", "3"),
    ("4", "NADA", "NADA", "NADA", "NADA", "NADA", "9:55 a 10:35", "4"),
    ("5", "NADA", "NADA", "NADA", "NADA", "NADA", "10:50 a 11:30", "5"),
    ("6", "NADA", "NADA", "NADA", "NADA", "NADA", "11:30 a 12:10", "6"),
    ("7", "NADA", "NADA", "NADA", "NADA", "NADA", "12:20 a 13:00", "7"),
    ("8", "NADA", "NADA", "NADA", "NADA", "NADA", "14:00 a 14:40", "8"),
    ("9", "NADA", "NADA", "NADA", "NADA", "NADA", "14:40 a 15:20", "9"),
    ("10", "NADA", "NADA", "NADA", "NADA", "NADA", "15:30 a 16:10", "10"),
    ("11", "NADA", "NADA", "NADA", "NADA", "NADA", "16:10 a 16:50", "11"),
    ("12", "NADA", "NADA", "NADA", "NADA", "NADA", "17:00 a 17:40", "12"), 
    ("13", "NADA", "NADA", "NADA", "NADA", "NADA", "17:40 a 18:20", "13"); 



-- -----------------------------------------------------
-- Table `ETEC_lab`.`1A`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `ETEC_lab`.`1A` ;

CREATE TABLE IF NOT EXISTS `ETEC_lab`.`1A` (
  `medio_modulo` INT NOT NULL,
  `Lunes` VARCHAR(45) NULL,
  `Martes` VARCHAR(45) NULL,
  `Miercoles` VARCHAR(45) NULL,
  `Jueves` VARCHAR(45) NULL,
  `Viernes` VARCHAR(45) NULL,
  `Hora` VARCHAR(45) NULL,
  `reservas_idreservas` INT NOT NULL,
  PRIMARY KEY (`medio_modulo`),
  INDEX `fk_1A_reservas1_idx` (`reservas_idreservas` ASC) VISIBLE,
  CONSTRAINT `fk_1A_reservas1`
    FOREIGN KEY (`reservas_idreservas`)
    REFERENCES `ETEC_lab`.`reservas` (`idreservas`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


insert into etec_lab.1a (medio_modulo, Lunes, Martes, Miercoles, Jueves, Viernes, Hora, reservas_idreservas)
values
	  ("1", "Historia",       "Matematica", "Lengua", "Educacion Fisica", "Taller Pre-Profesional de Electronica", "7:45 a 8:25", "1"),
    ("2", "Historia",       "Matematica", "Lengua", "Educacion Fisica", "Taller Pre-Profesional de Electronica", "8:25 a 9:05", "2"),
    ("3", "Artes Visuales", "Matematica", "Geografia", "Educacion Fisica", "Taller Pre-Profesional de Electronica", "9:15 a 9:55", "3"),
    ("4", "Artes Visuales", "Geografia", "Geografia", "Ciencias Naturales", "Lengua", "9:55 a 10:35", "4"),
    ("5", "Historia",       "Geografia", "Formacion Etica y Ciudadana", "Ciencias Naturales", "Lengua", "10:50 a 11:30", "5"),
    ("6", "Lengua",         "Ciencias Naturales", "Formacion Etica y Ciudadana", "Geografia", "Musica", "11:30 a 12:10", "6"),
    ("7", "Lengua",         "Ciencias Naturales", "Formacion Etica y Ciudadana", "Geografia", "Musica", "12:20 a 13:00", "7"),
    ("8", "Ingles",         "Ingles", "Matematica", "Taller Pre-Profesional de Informatica", "NADA", "14:00 a 14:40", "8"),
    ("9", "Ingles",         "Ingles", "Matematica", "Taller Pre-Profesional de Informatica", "NADA", "14:40 a 15:20", "9"),
    ("10", "Ingles",        "Ingles", "Matematica", "Taller Pre-Profesional de Informatica", "NADA", "15:30 a 16:10", "10"),
    ("11", "NADA",          "NADA", "NADA", "NADA", "NADA", "16:10 a 16:50", "11"),
    ("12", "NADA",          "NADA", "NADA", "NADA", "NADA", "16:10 a 16:50", "12"),
    ("13", "NADA",          "NADA", "NADA", "NADA", "NADA", "17:40 a 18:20", "13"); 


-- -----------------------------------------------------
-- Table `ETEC_lab`.`1B`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `ETEC_lab`.`1B` ;

CREATE TABLE IF NOT EXISTS `ETEC_lab`.`1B` (
  `medio_modulo` INT NOT NULL,
  `Lunes` VARCHAR(45) NULL,
  `Martes` VARCHAR(45) NULL,
  `Miercoles` VARCHAR(45) NULL,
  `Jueves` VARCHAR(45) NULL,
  `Viernes` VARCHAR(45) NULL,
  `Hora` VARCHAR(45) NULL,
  `reservas_idreservas` INT NOT NULL,
  PRIMARY KEY (`medio_modulo`),
  INDEX `fk_1B_reservas1_idx` (`reservas_idreservas` ASC) VISIBLE,
  CONSTRAINT `fk_1B_reservas1`
    FOREIGN KEY (`reservas_idreservas`)
    REFERENCES `ETEC_lab`.`reservas` (`idreservas`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

insert into etec_lab.1B (medio_modulo, Lunes, Martes, Miercoles, Jueves, Viernes, Hora, reservas_idreservas)
values
	  ("1", "NADA", "NADA", "NADA", "NADA", "NADA", "7:45 a 8:25", "1"),
    ("2", "NADA", "NADA", "NADA", "NADA", "NADA", "8:25 a 9:05", "2"),
    ("3", "NADA", "NADA", "NADA", "NADA", "NADA", "9:15 a 9:55", "3"),
    ("4", "NADA", "NADA", "NADA", "NADA", "NADA", "9:55 a 10:35", "4"),
    ("5", "NADA", "NADA", "NADA", "NADA", "NADA", "10:50 a 11:30", "5"),
    ("6", "NADA", "NADA", "NADA", "NADA", "NADA", "11:30 a 12:10", "6"),
    ("7", "NADA", "NADA", "NADA", "NADA", "NADA", "12:20 a 13:00", "7"),
    ("8", "NADA", "NADA", "NADA", "NADA", "NADA", "14:00 a 14:40", "8"),
    ("9", "NADA", "NADA", "NADA", "NADA", "NADA", "14:40 a 15:20", "9"),
    ("10", "NADA", "NADA", "NADA", "NADA", "NADA", "15:30 a 16:10", "10"),
    ("11", "NADA", "NADA", "NADA", "NADA", "NADA", "16:10 a 16:50", "11"),
    ("12", "NADA", "NADA", "NADA", "NADA", "NADA", "17:00 a 17:40", "12"), 
    ("13", "NADA", "NADA", "NADA", "NADA", "NADA", "17:40 a 18:20", "13"); 

-- -----------------------------------------------------
-- Table `ETEC_lab`.`2A`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `ETEC_lab`.`2A` ;

CREATE TABLE IF NOT EXISTS `ETEC_lab`.`2A` (
  `medio_modulo` INT NOT NULL,
  `Lunes` VARCHAR(45) NULL,
  `Martes` VARCHAR(45) NULL,
  `Miercoles` VARCHAR(45) NULL,
  `Jueves` VARCHAR(45) NULL,
  `Viernes` VARCHAR(45) NULL,
  `Hora` VARCHAR(45) NULL,
  `reservas_idreservas` INT NOT NULL,
  PRIMARY KEY (`medio_modulo`),
  INDEX `fk_2A_reservas1_idx` (`reservas_idreservas` ASC) VISIBLE,
  CONSTRAINT `fk_2A_reservas1`
    FOREIGN KEY (`reservas_idreservas`)
    REFERENCES `ETEC_lab`.`reservas` (`idreservas`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

insert into etec_lab.2A (medio_modulo, Lunes, Martes, Miercoles, Jueves, Viernes, Hora, reservas_idreservas)
values
	  ("1", "NADA", "NADA", "NADA", "NADA", "NADA", "7:45 a 8:25", "1"),
    ("2", "NADA", "NADA", "NADA", "NADA", "NADA", "8:25 a 9:05", "2"),
    ("3", "NADA", "NADA", "NADA", "NADA", "NADA", "9:15 a 9:55", "3"),
    ("4", "NADA", "NADA", "NADA", "NADA", "NADA", "9:55 a 10:35", "4"),
    ("5", "NADA", "NADA", "NADA", "NADA", "NADA", "10:50 a 11:30", "5"),
    ("6", "NADA", "NADA", "NADA", "NADA", "NADA", "11:30 a 12:10", "6"),
    ("7", "NADA", "NADA", "NADA", "NADA", "NADA", "12:20 a 13:00", "7"),
    ("8", "NADA", "NADA", "NADA", "NADA", "NADA", "14:00 a 14:40", "8"),
    ("9", "NADA", "NADA", "NADA", "NADA", "NADA", "14:40 a 15:20", "9"),
    ("10", "NADA", "NADA", "NADA", "NADA", "NADA", "15:30 a 16:10", "10"),
    ("11", "NADA", "NADA", "NADA", "NADA", "NADA", "16:10 a 16:50", "11"),
    ("12", "NADA", "NADA", "NADA", "NADA", "NADA", "17:00 a 17:40", "12"), 
    ("13", "NADA", "NADA", "NADA", "NADA", "NADA", "17:40 a 18:20", "13"); 

-- -----------------------------------------------------
-- Table `ETEC_lab`.`2B`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `ETEC_lab`.`2B` ;

CREATE TABLE IF NOT EXISTS `ETEC_lab`.`2B` (
  `medio_modulo` INT NOT NULL,
  `Lunes` VARCHAR(45) NULL,
  `Martes` VARCHAR(45) NULL,
  `Miercoles` VARCHAR(45) NULL,
  `Jueves` VARCHAR(45) NULL,
  `Viernes` VARCHAR(45) NULL,
  `Hora` VARCHAR(45) NULL,
  `reservas_idreservas` INT NOT NULL,
  PRIMARY KEY (`medio_modulo`),
  INDEX `fk_2B_reservas1_idx` (`reservas_idreservas` ASC) VISIBLE,
  CONSTRAINT `fk_2B_reservas1`
    FOREIGN KEY (`reservas_idreservas`)
    REFERENCES `ETEC_lab`.`reservas` (`idreservas`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

insert into etec_lab.2B (medio_modulo, Lunes, Martes, Miercoles, Jueves, Viernes, Hora, reservas_idreservas)
values
	  ("1", "NADA", "NADA", "NADA", "NADA", "NADA", "7:45 a 8:25", "1"),
    ("2", "NADA", "NADA", "NADA", "NADA", "NADA", "8:25 a 9:05", "2"),
    ("3", "NADA", "NADA", "NADA", "NADA", "NADA", "9:15 a 9:55", "3"),
    ("4", "NADA", "NADA", "NADA", "NADA", "NADA", "9:55 a 10:35", "4"),
    ("5", "NADA", "NADA", "NADA", "NADA", "NADA", "10:50 a 11:30", "5"),
    ("6", "NADA", "NADA", "NADA", "NADA", "NADA", "11:30 a 12:10", "6"),
    ("7", "NADA", "NADA", "NADA", "NADA", "NADA", "12:20 a 13:00", "7"),
    ("8", "NADA", "NADA", "NADA", "NADA", "NADA", "14:00 a 14:40", "8"),
    ("9", "NADA", "NADA", "NADA", "NADA", "NADA", "14:40 a 15:20", "9"),
    ("10", "NADA", "NADA", "NADA", "NADA", "NADA", "15:30 a 16:10", "10"),
    ("11", "NADA", "NADA", "NADA", "NADA", "NADA", "16:10 a 16:50", "11"),
    ("12", "NADA", "NADA", "NADA", "NADA", "NADA", "17:00 a 17:40", "12"), 
    ("13", "NADA", "NADA", "NADA", "NADA", "NADA", "17:40 a 18:20", "13"); 

-- -----------------------------------------------------
-- Table `ETEC_lab`.`3e`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `ETEC_lab`.`3e` ;

CREATE TABLE IF NOT EXISTS `ETEC_lab`.`3e` (
  `medio_modulo` INT NOT NULL,
  `Lunes` VARCHAR(45) NULL,
  `Martes` VARCHAR(45) NULL,
  `Miercoles` VARCHAR(45) NULL,
  `Jueves` VARCHAR(45) NULL,
  `Viernes` VARCHAR(45) NULL,
  `Hora` VARCHAR(45) NULL,
  `reservas_idreservas` INT NOT NULL,
  PRIMARY KEY (`medio_modulo`),
  INDEX `fk_3e_reservas1_idx` (`reservas_idreservas` ASC) VISIBLE,
  CONSTRAINT `fk_3e_reservas1`
    FOREIGN KEY (`reservas_idreservas`)
    REFERENCES `ETEC_lab`.`reservas` (`idreservas`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

insert into etec_lab.3e (medio_modulo, Lunes, Martes, Miercoles, Jueves, Viernes, Hora, reservas_idreservas)
values
	  ("1", "NADA", "NADA", "NADA", "NADA", "NADA", "7:45 a 8:25", "1"),
    ("2", "NADA", "NADA", "NADA", "NADA", "NADA", "8:25 a 9:05", "2"),
    ("3", "NADA", "NADA", "NADA", "NADA", "NADA", "9:15 a 9:55", "3"),
    ("4", "NADA", "NADA", "NADA", "NADA", "NADA", "9:55 a 10:35", "4"),
    ("5", "NADA", "NADA", "NADA", "NADA", "NADA", "10:50 a 11:30", "5"),
    ("6", "NADA", "NADA", "NADA", "NADA", "NADA", "11:30 a 12:10", "6"),
    ("7", "NADA", "NADA", "NADA", "NADA", "NADA", "12:20 a 13:00", "7"),
    ("8", "NADA", "NADA", "NADA", "NADA", "NADA", "14:00 a 14:40", "8"),
    ("9", "NADA", "NADA", "NADA", "NADA", "NADA", "14:40 a 15:20", "9"),
    ("10", "NADA", "NADA", "NADA", "NADA", "NADA", "15:30 a 16:10", "10"),
    ("11", "NADA", "NADA", "NADA", "NADA", "NADA", "16:10 a 16:50", "11"),
    ("12", "NADA", "NADA", "NADA", "NADA", "NADA", "17:00 a 17:40", "12"), 
    ("13", "NADA", "NADA", "NADA", "NADA", "NADA", "17:40 a 18:20", "13"); 

-- -----------------------------------------------------
-- Table `ETEC_lab`.`3i`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `ETEC_lab`.`3i` ;

CREATE TABLE IF NOT EXISTS `ETEC_lab`.`3i` (
  `medio_modulo` INT NOT NULL,
  `Lunes` VARCHAR(45) NULL,
  `Martes` VARCHAR(45) NULL,
  `Miercoles` VARCHAR(45) NULL,
  `Jueves` VARCHAR(45) NULL,
  `Viernes` VARCHAR(45) NULL,
  `Hora` VARCHAR(45) NULL,
  `reservas_idreservas` INT NOT NULL,
  PRIMARY KEY (`medio_modulo`),
  INDEX `fk_3i_reservas1_idx` (`reservas_idreservas` ASC) VISIBLE,
  CONSTRAINT `fk_3i_reservas1`
    FOREIGN KEY (`reservas_idreservas`)
    REFERENCES `ETEC_lab`.`reservas` (`idreservas`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

insert into etec_lab.3i (medio_modulo, Lunes, Martes, Miercoles, Jueves, Viernes, Hora, reservas_idreservas)
values
	  ("1", "NADA", "NADA", "NADA", "NADA", "NADA", "7:45 a 8:25", "1"),
    ("2", "NADA", "NADA", "NADA", "NADA", "NADA", "8:25 a 9:05", "2"),
    ("3", "NADA", "NADA", "NADA", "NADA", "NADA", "9:15 a 9:55", "3"),
    ("4", "NADA", "NADA", "NADA", "NADA", "NADA", "9:55 a 10:35", "4"),
    ("5", "NADA", "NADA", "NADA", "NADA", "NADA", "10:50 a 11:30", "5"),
    ("6", "NADA", "NADA", "NADA", "NADA", "NADA", "11:30 a 12:10", "6"),
    ("7", "NADA", "NADA", "NADA", "NADA", "NADA", "12:20 a 13:00", "7"),
    ("8", "NADA", "NADA", "NADA", "NADA", "NADA", "14:00 a 14:40", "8"),
    ("9", "NADA", "NADA", "NADA", "NADA", "NADA", "14:40 a 15:20", "9"),
    ("10", "NADA", "NADA", "NADA", "NADA", "NADA", "15:30 a 16:10", "10"),
    ("11", "NADA", "NADA", "NADA", "NADA", "NADA", "16:10 a 16:50", "11"),
    ("12", "NADA", "NADA", "NADA", "NADA", "NADA", "17:00 a 17:40", "12"), 
    ("13", "NADA", "NADA", "NADA", "NADA", "NADA", "17:40 a 18:20", "13"); 

-- -----------------------------------------------------
-- Table `ETEC_lab`.`4e`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `ETEC_lab`.`4e` ;

CREATE TABLE IF NOT EXISTS `ETEC_lab`.`4e` (
  `medio_modulo` INT NOT NULL,
  `Lunes` VARCHAR(45) NULL,
  `Martes` VARCHAR(45) NULL,
  `Miercoles` VARCHAR(45) NULL,
  `Jueves` VARCHAR(45) NULL,
  `Viernes` VARCHAR(45) NULL,
  `Hora` VARCHAR(45) NULL,
  `4ecol` VARCHAR(45) NULL,
  `reservas_idreservas` INT NOT NULL,
  PRIMARY KEY (`medio_modulo`),
  INDEX `fk_4e_reservas1_idx` (`reservas_idreservas` ASC) VISIBLE,
  CONSTRAINT `fk_4e_reservas1`
    FOREIGN KEY (`reservas_idreservas`)
    REFERENCES `ETEC_lab`.`reservas` (`idreservas`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

insert into etec_lab.4e (medio_modulo, Lunes, Martes, Miercoles, Jueves, Viernes, Hora, reservas_idreservas)
values
	  ("1", "NADA", "NADA", "NADA", "NADA", "NADA", "7:45 a 8:25", "1"),
    ("2", "NADA", "NADA", "NADA", "NADA", "NADA", "8:25 a 9:05", "2"),
    ("3", "NADA", "NADA", "NADA", "NADA", "NADA", "9:15 a 9:55", "3"),
    ("4", "NADA", "NADA", "NADA", "NADA", "NADA", "9:55 a 10:35", "4"),
    ("5", "NADA", "NADA", "NADA", "NADA", "NADA", "10:50 a 11:30", "5"),
    ("6", "NADA", "NADA", "NADA", "NADA", "NADA", "11:30 a 12:10", "6"),
    ("7", "NADA", "NADA", "NADA", "NADA", "NADA", "12:20 a 13:00", "7"),
    ("8", "NADA", "NADA", "NADA", "NADA", "NADA", "14:00 a 14:40", "8"),
    ("9", "NADA", "NADA", "NADA", "NADA", "NADA", "14:40 a 15:20", "9"),
    ("10", "NADA", "NADA", "NADA", "NADA", "NADA", "15:30 a 16:10", "10"),
    ("11", "NADA", "NADA", "NADA", "NADA", "NADA", "16:10 a 16:50", "11"),
    ("12", "NADA", "NADA", "NADA", "NADA", "NADA", "17:00 a 17:40", "12"), 
    ("13", "NADA", "NADA", "NADA", "NADA", "NADA", "17:40 a 18:20", "13"); 

-- -----------------------------------------------------
-- Table `ETEC_lab`.`4i`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `ETEC_lab`.`4i` ;

CREATE TABLE IF NOT EXISTS `ETEC_lab`.`4i` (
  `medio_modulo` INT NOT NULL,
  `Lunes` VARCHAR(45) NULL,
  `Martes` VARCHAR(45) NULL,
  `Miercoles` VARCHAR(45) NULL,
  `Jueves` VARCHAR(45) NULL,
  `Viernes` VARCHAR(45) NULL,
  `Hora` VARCHAR(45) NULL,
  `reservas_idreservas` INT NOT NULL,
  PRIMARY KEY (`medio_modulo`),
  INDEX `fk_4i_reservas1_idx` (`reservas_idreservas` ASC) VISIBLE,
  CONSTRAINT `fk_4i_reservas1`
    FOREIGN KEY (`reservas_idreservas`)
    REFERENCES `ETEC_lab`.`reservas` (`idreservas`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

insert into etec_lab.4i (medio_modulo, Lunes, Martes, Miercoles, Jueves, Viernes, Hora, reservas_idreservas)
values
	("1", "Practica Profesionalizante", "Economia", "Economia", "Ingles", "Laboratorio Hardware 2", "7:45 a 8:25", "1"),
    ("2", "Practica Profesionalizante", "Economia", "Economia", "Ingles", "Laboratorio Hardware 2", "8:25 a 9:05", "2"),
    ("3", "Practica Profesionalizante", "Proteccion y Mantenimiento de Datos", "Proteccion y Mantenimiento de Datos", "Ingles", "Laboratorio Hardware 2", "9:15 a 9:55", "3"),
    ("4", "Programacion 3", "Proteccion y Mantenimiento de Datos", "Proteccion y Mantenimiento de Datos", "Mantenimiento de Software", "Programacion 3", "9:55 a 10:35", "4"),
    ("5", "Programacion 3", "Organizacion y Gestion", "NADA", "Mantenimiento de Software", "Programacion 3", "10:50 a 11:30", "5"),
    ("6", "Programacion 3", "Organizacion y Gestion", "NADA", "Mantenimiento de Software", "Programacion 3", "11:30 a 12:10", "6"),
    ("7", "Educacion Fisica", "Organizacion y Gestion", "NADA", "Laboratorio Hardware 2", "NADA", "12:20 a 13:00", "7"),
    ("8", "Educacion Fisica", "Redes de Area Local", "Laboratorio de Redes", "Orientacion y Tutoria", "NADA", "14:00 a 14:40", "8"),
    ("9", "Educacion Fisica", "Redes de Area Local", "Laboratorio de Redes", "NADA", "NADA", "14:40 a 15:20", "9"),
    ("10", "Matematicas", "NADA", "Laboratorio de Redes", "NADA", "NADA", "15:30 a 16:10", "10"),
    ("11", "Matematicas", "NADA", "NADA", "NADA", "NADA", "16:10 a 16:50", "11"),
    ("12", "Matematicas", "NADA", "NADA", "NADA", "NADA", "17:00 a 17:40", "12"); 


-- -----------------------------------------------------
-- Table `ETEC_lab`.`5i`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `ETEC_lab`.`5i` ;

CREATE TABLE IF NOT EXISTS `ETEC_lab`.`5i` (
  `medio_modulo` INT NOT NULL,
  `Lunes` VARCHAR(45) NULL,
  `Martes` VARCHAR(45) NULL,
  `Miercoles` VARCHAR(45) NULL,
  `Jueves` VARCHAR(45) NULL,
  `Viernes` VARCHAR(45) NULL,
  `Hora` VARCHAR(45) NULL,
  `reservas_idreservas` INT NOT NULL,
  PRIMARY KEY (`medio_modulo`),
  INDEX `fk_5i_reservas1_idx` (`reservas_idreservas` ASC) VISIBLE,
  CONSTRAINT `fk_5i_reservas1`
    FOREIGN KEY (`reservas_idreservas`)
    REFERENCES `ETEC_lab`.`reservas` (`idreservas`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


insert into etec_lab.5i (medio_modulo, Lunes, Martes, Miercoles, Jueves, Viernes, Hora, reservas_idreservas)
values
	("1", "Practica Profesionalizante", "Economia", "Economia", "Ingles", "Laboratorio Hardware 2", "7:45 a 8:25", "1"),
    ("2", "Practica Profesionalizante", "Economia", "Economia", "Ingles", "Laboratorio Hardware 2", "8:25 a 9:05", "2"),
    ("3", "Practica Profesionalizante", "Proteccion y Mantenimiento de Datos", "Proteccion y Mantenimiento de Datos", "Ingles", "Laboratorio Hardware 2", "9:15 a 9:55", "3"),
    ("4", "Programacion 3", "Proteccion y Mantenimiento de Datos", "Proteccion y Mantenimiento de Datos", "Mantenimiento de Software", "Programacion 3", "9:55 a 10:35", "4"),
    ("5", "Programacion 3", "Organizacion y Gestion", "NADA", "Mantenimiento de Software", "Programacion 3", "10:50 a 11:30", "5"),
    ("6", "Programacion 3", "Organizacion y Gestion", "NADA", "Mantenimiento de Software", "Programacion 3", "11:30 a 12:10", "6"),
    ("7", "Educacion Fisica", "Organizacion y Gestion", "NADA", "Laboratorio Hardware 2", "NADA", "12:20 a 13:00", "7"),
    ("8", "Educacion Fisica", "Redes de Area Local", "Laboratorio de Redes", "Orientacion y Tutoria", "NADA", "14:00 a 14:40", "8"),
    ("9", "Educacion Fisica", "Redes de Area Local", "Laboratorio de Redes", "NADA", "NADA", "14:40 a 15:20", "9"),
    ("10", "Matematicas", "NADA", "Laboratorio de Redes", "NADA", "NADA", "15:30 a 16:10", "10"),
    ("11", "Matematicas", "NADA", "NADA", "NADA", "NADA", "16:10 a 16:50", "11"),
    ("12", "Matematicas", "NADA", "NADA", "NADA", "NADA", "17:00 a 17:40", "12"); 

-- -----------------------------------------------------
-- Table `ETEC_lab`.`5e`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `ETEC_lab`.`5e` ;

CREATE TABLE IF NOT EXISTS `ETEC_lab`.`5e` (
  `medio_modulo` INT NOT NULL,
  `Lunes` VARCHAR(45) NULL,
  `Martes` VARCHAR(45) NULL,
  `Miercoles` VARCHAR(45) NULL,
  `Jueves` VARCHAR(45) NULL,
  `Viernes` VARCHAR(45) NULL,
  `Hora` VARCHAR(45) NULL,
  `reservas_idreservas` INT NOT NULL,
  PRIMARY KEY (`medio_modulo`),
  INDEX `fk_5e_reservas1_idx` (`reservas_idreservas` ASC) VISIBLE,
  CONSTRAINT `fk_5e_reservas1`
    FOREIGN KEY (`reservas_idreservas`)
    REFERENCES `ETEC_lab`.`reservas` (`idreservas`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

insert into etec_lab.5e (medio_modulo, Lunes, Martes, Miercoles, Jueves, Viernes, Hora, reservas_idreservas)
values
	  ("1", "NADA", "NADA", "NADA", "NADA", "NADA", "7:45 a 8:25", "1"),
    ("2", "NADA", "NADA", "NADA", "NADA", "NADA", "8:25 a 9:05", "2"),
    ("3", "NADA", "NADA", "NADA", "NADA", "NADA", "9:15 a 9:55", "3"),
    ("4", "NADA", "NADA", "NADA", "NADA", "NADA", "9:55 a 10:35", "4"),
    ("5", "NADA", "NADA", "NADA", "NADA", "NADA", "10:50 a 11:30", "5"),
    ("6", "NADA", "NADA", "NADA", "NADA", "NADA", "11:30 a 12:10", "6"),
    ("7", "NADA", "NADA", "NADA", "NADA", "NADA", "12:20 a 13:00", "7"),
    ("8", "NADA", "NADA", "NADA", "NADA", "NADA", "14:00 a 14:40", "8"),
    ("9", "NADA", "NADA", "NADA", "NADA", "NADA", "14:40 a 15:20", "9"),
    ("10", "NADA", "NADA", "NADA", "NADA", "NADA", "15:30 a 16:10", "10"),
    ("11", "NADA", "NADA", "NADA", "NADA", "NADA", "16:10 a 16:50", "11"),
    ("12", "NADA", "NADA", "NADA", "NADA", "NADA", "17:00 a 17:40", "12"), 
    ("13", "NADA", "NADA", "NADA", "NADA", "NADA", "17:40 a 18:20", "13"); 

-- -----------------------------------------------------
-- Table `ETEC_lab`.`6i`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `ETEC_lab`.`6i` ;

CREATE TABLE IF NOT EXISTS `ETEC_lab`.`6i` (
  `medio_modulo` INT NOT NULL,
  `Lunes` VARCHAR(45) NULL,
  `Martes` VARCHAR(45) NULL,
  `Miercoles` VARCHAR(45) NULL,
  `Jueves` VARCHAR(45) NULL,
  `Viernes` VARCHAR(45) NULL,
  `Hora` VARCHAR(45) NULL,
  `reservas_idreservas` INT NOT NULL,
  PRIMARY KEY (`medio_modulo`),
  INDEX `fk_6i_reservas1_idx` (`reservas_idreservas` ASC) VISIBLE,
  CONSTRAINT `fk_6i_reservas1`
    FOREIGN KEY (`reservas_idreservas`)
    REFERENCES `ETEC_lab`.`reservas` (`idreservas`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

insert into etec_lab.6i (medio_modulo, Lunes, Martes, Miercoles, Jueves, Viernes, Hora, reservas_idreservas)
values
	  ("1", "NADA", "NADA", "NADA", "NADA", "NADA", "7:45 a 8:25", "1"),
    ("2", "NADA", "NADA", "NADA", "NADA", "NADA", "8:25 a 9:05", "2"),
    ("3", "NADA", "NADA", "NADA", "NADA", "NADA", "9:15 a 9:55", "3"),
    ("4", "NADA", "NADA", "NADA", "NADA", "NADA", "9:55 a 10:35", "4"),
    ("5", "NADA", "NADA", "NADA", "NADA", "NADA", "10:50 a 11:30", "5"),
    ("6", "NADA", "NADA", "NADA", "NADA", "NADA", "11:30 a 12:10", "6"),
    ("7", "NADA", "NADA", "NADA", "NADA", "NADA", "12:20 a 13:00", "7"),
    ("8", "NADA", "NADA", "NADA", "NADA", "NADA", "14:00 a 14:40", "8"),
    ("9", "NADA", "NADA", "NADA", "NADA", "NADA", "14:40 a 15:20", "9"),
    ("10", "NADA", "NADA", "NADA", "NADA", "NADA", "15:30 a 16:10", "10"),
    ("11", "NADA", "NADA", "NADA", "NADA", "NADA", "16:10 a 16:50", "11"),
    ("12", "NADA", "NADA", "NADA", "NADA", "NADA", "17:00 a 17:40", "12"), 
    ("13", "NADA", "NADA", "NADA", "NADA", "NADA", "17:40 a 18:20", "13"); 

-- -----------------------------------------------------
-- Table `ETEC_lab`.`6e`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `ETEC_lab`.`6e` ;

CREATE TABLE IF NOT EXISTS `ETEC_lab`.`6e` (
  `medio_modulo` INT NOT NULL,
  `Lunes` VARCHAR(45) NULL,
  `Martes` VARCHAR(45) NULL,
  `Miercoles` VARCHAR(45) NULL,
  `Jueves` VARCHAR(45) NULL,
  `Viernes` VARCHAR(45) NULL,
  `Hora` VARCHAR(45) NULL,
  `reservas_idreservas` INT NOT NULL,
  PRIMARY KEY (`medio_modulo`),
  INDEX `fk_6e_reservas1_idx` (`reservas_idreservas` ASC) VISIBLE,
  CONSTRAINT `fk_6e_reservas1`
    FOREIGN KEY (`reservas_idreservas`)
    REFERENCES `ETEC_lab`.`reservas` (`idreservas`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

insert into etec_lab.6e (medio_modulo, Lunes, Martes, Miercoles, Jueves, Viernes, Hora, reservas_idreservas)
values
	  ("1", "NADA", "NADA", "NADA", "NADA", "NADA", "7:45 a 8:25", "1"),
    ("2", "NADA", "NADA", "NADA", "NADA", "NADA", "8:25 a 9:05", "2"),
    ("3", "NADA", "NADA", "NADA", "NADA", "NADA", "9:15 a 9:55", "3"),
    ("4", "NADA", "NADA", "NADA", "NADA", "NADA", "9:55 a 10:35", "4"),
    ("5", "NADA", "NADA", "NADA", "NADA", "NADA", "10:50 a 11:30", "5"),
    ("6", "NADA", "NADA", "NADA", "NADA", "NADA", "11:30 a 12:10", "6"),
    ("7", "NADA", "NADA", "NADA", "NADA", "NADA", "12:20 a 13:00", "7"),
    ("8", "NADA", "NADA", "NADA", "NADA", "NADA", "14:00 a 14:40", "8"),
    ("9", "NADA", "NADA", "NADA", "NADA", "NADA", "14:40 a 15:20", "9"),
    ("10", "NADA", "NADA", "NADA", "NADA", "NADA", "15:30 a 16:10", "10"),
    ("11", "NADA", "NADA", "NADA", "NADA", "NADA", "16:10 a 16:50", "11"),
    ("12", "NADA", "NADA", "NADA", "NADA", "NADA", "17:00 a 17:40", "12"), 
    ("13", "NADA", "NADA", "NADA", "NADA", "NADA", "17:40 a 18:20", "13"); 

-- -----------------------------------------------------
-- Table `ETEC_lab`.`profes`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `ETEC_lab`.`profes` ;

CREATE TABLE IF NOT EXISTS `ETEC_lab`.`profes` (
  `idprofes` INT NOT NULL,
  `nombre` VARCHAR(45) NULL,
  `apellido` VARCHAR(45) NULL,
  `correo` VARCHAR(45) NULL,
  `cel` VARCHAR(45) NULL DEFAULT 'No tiene número',
  `asignatura` VARCHAR(45) NULL,
  `reservas_idreservas` INT NOT NULL,
  PRIMARY KEY (`idprofes`),
  INDEX `fk_profes_reservas1_idx` (`reservas_idreservas` ASC) VISIBLE,
  CONSTRAINT `fk_profes_reservas1`
    FOREIGN KEY (`reservas_idreservas`)
    REFERENCES `ETEC_lab`.`reservas` (`idreservas`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `ETEC_lab`.`profes`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `ETEC_lab`.`cuentas` ;

CREATE TABLE IF NOT EXISTS `ETEC_lab`.`cuentas` (
  `idcuenta` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `nombre` VARCHAR(45) NULL,
  `apellido` VARCHAR(45) NULL,
  `correo` VARCHAR(45) NULL DEFAULT 'No quiso dar correo personal',
  `celular` VARCHAR(45) NULL DEFAULT 'No tiene celu es pobre :v',
  `usuario` varchar(45) NULL,
  `contraseña` VARCHAR(45) NULL,
  `correo_etec` VARCHAR(45) NULL DEFAULT 'No tiene correo, luis ayuda!')
ENGINE = InnoDB;

desc 1a;
select * from 1a;
SELECT usuario FROM cuentas;
SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
