USE bawydb;

CREATE TABLE ROBOTS(
 ID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
 ESTADO VARCHAR(28),
 NOMBRE VARCHAR(28)
 );
 
 DESC ROBOTS;
 
 alter table robots
 add column descripcion varchar(30);
 
 SELECT * FROM ROBOTS;

insert into ROBOTS (ESTADO, NOMBRE, descripcion)
values
	("desconectado", "Tan-k", "Robot tanque"),
    ("Revisión", "hammy", "Impresora 3D 'HomeMade'"),
    ("desconectado", "shota", "Impresora 3D copada/cheta"),
    ("desarrollo", "rower", "CNC router para fabricar PCB's");
