
insert into etec_lab.qr_items (qr_code, name_item, marca_item, cantidad)
values
	  ("02'005'002'000063", "Notebook", "Banghoo", 1),
	  ("02'005'002'000062", "Notebook", "Banghoo", 1);
      
select * from etec_lab.qr_items where cantidad;
select * from etec_lab.`1a`;
select * from etec_lab.`profes`;
select nombre from etec_lab.`profes` where nombre='Mario';


DROP TABLE IF EXISTS ETEC_lab.qr_items ;

CREATE TABLE IF NOT EXISTS ETEC_lab.qr_items (
  `qr_code` VARCHAR(45) NOT NULL COMMENT 'Códigos QR generados por \"terceros\" de la mano de la Universidad de Mendoza.',
  `name_item` VARCHAR(45) NULL DEFAULT 'Sin_nombre' COMMENT 'Columna referida al nombre del ítem, al cual se encuentra adherido código QR correspondiente.',
  `marca_item` VARCHAR(45) NULL DEFAULT 'Sin_marca/fabricante' COMMENT 'Columna para especificar la Marca/Modelo/Fabricante del ítem.',
  `cantidad` INT NOT NULL DEFAULT 0 COMMENT 'Columna para especificar la Marca/Modelo/Fabricante del ítem.',
  `operativa` VARCHAR(10) NULL DEFAULT 'No' COMMENT 'Columna para especificar la Marca/Modelo/Fabricante del ítem.',
  `qr_img` BLOB NULL  COMMENT 'Columna para almacenar la imagen generada del QR del ítem.',
  `qr_url_img` VARCHAR(45) NULL DEFAULT 'Sin dirección de imagen' COMMENT 'Columna para especificar la dirección al servidor del ETEC relacionado al QR del ítem.')
ENGINE = InnoDB;