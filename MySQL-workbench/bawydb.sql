-- -----------------------------------------------------
-- Schema bawydb
-- -----------------------------------------------------
-- Base de datos con el fin de poder generar una mejora en cuanto a la gestión de los ítems multimedia y gestión de reservas.
DROP SCHEMA IF EXISTS `bawydb` ;

-- -----------------------------------------------------
-- Schema ETEC_lab
--
-- Base de datos con el fin de poder generar una mejora en cuanto a la gestión de los ítems multimedia y gestión de reservas.
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `bawydb` ;
USE `bawydb`;

CREATE TABLE if NOT exists ROBOTS(
 ID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
 ESTADO VARCHAR(28),
 NOMBRE VARCHAR(28)
 );
 
 DESC ROBOTS;
select * from robots;
 
 alter table robots
 add column descripcion varchar(30);
 
 SELECT * FROM ROBOTS;

insert into ROBOTS (ESTADO, NOMBRE, descripcion)
values
	("desconectado", "Tan-k", "Robot tanque"),
    ("Revisión", "hammy", "Impresora 3D 'HomeMade'"),
    ("desconectado", "shota", "Impresora 3D copada/cheta"),
    ("desarrollo", "rower", "CNC router para fabricar PCB's");
 DESC ROBOTS;
select * from robots;
select * from demo;