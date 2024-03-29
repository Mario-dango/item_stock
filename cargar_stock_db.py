import pandas as pd
import xlrd
from programas_py.db import ETEC_db

# Script para cargar y conectar a la db MySQL
# Actualmente Carga todos los datos a la db desde el excel y sin repetirlos


path_curso = "Excel/item_stock.xls"
wb = xlrd.open_workbook(path_curso)
# hoja = wb.sheet_by_index(0)
# print(hoja.nrows)
# print(hoja.ncols)
# print(hoja.cell_value(5, 3))

hoja = wb.sheet_by_name('item_stock')
list_codigos = []
for i in range(1,hoja.nrows):
    if hoja.cell_value(i,0) == '':
        pass
    else:
        list_codigos.append(hoja.cell_value(i,0))

list_elementos = []
for i in range(1,hoja.nrows):
    if hoja.cell_value(i,1) == '':
        pass
    else:
        list_elementos.append(hoja.cell_value(i,1))
        
list_marca = []
for i in range(1,hoja.nrows):
    if hoja.cell_value(i,2) == '':
        pass
    else:
        list_marca.append(hoja.cell_value(i,2))

list_cantidades = []
for i in range(1,hoja.nrows):
    if hoja.cell_value(i,3) == '':
        pass
    else:
        list_cantidades.append(hoja.cell_value(i,3))

list_operativa = []
for i in range(1,hoja.nrows):
    if hoja.cell_value(i,4) == '':
        pass
    else:
        list_operativa.append(hoja.cell_value(i,4))



for elemento in range(1,len(list_elementos)):
    pass



db_etec = ETEC_db()

# crear_db = """
# CREATE SCHEMA IF NOT EXISTS `ETEC_lab` ;
# USE `ETEC_lab` ;
# """
# db_etec.cursor.execute(crear_db)

crear_tabla_qr_items = """
USE `ETEC_lab` ;
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
"""
insertar_tabla_qr_items = """
insert into etec_lab.qr_items (qr_code, name_item, marca_item, cantidad)
values
	  ("{}", "{}", "Banghoo", 1, "", ""),
	  ("notebook_002", "Computadora", "Banghoo", 1, "imagen_qr", "NADA");
      ###########################AUTOMATIZAR
"""

# db_etec.cursor.execute(crear_tabla_qr_items)
# db_etec.connection.commit()


# El formato que insertaría en etec_lab.qr_items: ("02'005'002'000063", "Notebook", "Banghoo", 1), (al final poner "";"")
for elemento in range(0,len(list_elementos)):   
    try:         
        sql = "SELECT * FROM qr_items WHERE qr_code=%s"            
        db_etec.cursor.execute(sql, (list_codigos[elemento]))
        if (len(db_etec.cursor.fetchall())>0):
            print("El elemento ya se encuentra en la base de datos.")
        else:            
            print(list_codigos[elemento], list_elementos[elemento], list_marca[elemento], list_cantidades[elemento], list_operativa[elemento])        
            query_sql = "INSERT INTO qr_items(qr_code, name_item, marca_item, cantidad, operativa) VALUES(%s, %s, %s, %s, %s);"
            db_etec.cursor.execute(query_sql, (list_codigos[elemento], list_elementos[elemento], list_marca[elemento], list_cantidades[elemento], list_operativa[elemento]))
            db_etec.connection.commit()
    except TypeError as error:
        print("Hubo un erro, el siguiente: {}".format(error))

# for elemento in range(0,len(list_elementos)):
#     print(list_codigos[elemento], list_elementos[elemento], list_marca[elemento], list_cantidades[elemento], list_operativa[elemento])        
#     query_sql = "INSERT INTO qr_items(qr_code, name_item, marca_item, cantidad, operativa) VALUES(%s, %s, %s, %s, %s);"
#     db_etec.cursor.execute(query_sql, (list_codigos[elemento], list_elementos[elemento], list_marca[elemento], list_cantidades[elemento], list_operativa[elemento]))
#     db_etec.connection.commit()

print("Se ha cargado la base de datos correctamente")

consulta_sql = "select * from etec_lab.qr_items"
db_etec.cursor.execute(consulta_sql)

# for codigo in db_etec.cursor.fetchall():
#     print("{0}".format(codigo))
tupla_sql = db_etec.cursor.fetchall()
print(tupla_sql[3], ",")


path_curso = "Excel/profe_data.xls"
profe_data = xlrd.open_workbook(path_curso)
# hoja = wb.sheet_by_index(0)
# print(hoja.nrows)
# print(hoja.ncols)
# print(hoja.cell_value(5, 3))

hoja = profe_data.sheet_by_name('Hoja1')
old_apellidosNombres = []
for i in range(1,hoja.nrows):
    if hoja.cell_value(i,0) == '':
        pass
    else:
        old_apellidosNombres.append(hoja.cell_value(i,0))

list_materias = []
for i in range(1,hoja.nrows):
    if hoja.cell_value(i,1) == '':
        pass
    else:
        list_materias.append(hoja.cell_value(i,1))

list_cursos = []
for i in range(1,hoja.nrows):
    if hoja.cell_value(i,2) == '':
        pass
    else:
        list_cursos.append(hoja.cell_value(i,2))

list_apellido = []
list_nombre = []
print(old_apellidosNombres)
for l in range(0,len(old_apellidosNombres)):
    # print((old_apellidosNombres[l]))
    aux = old_apellidosNombres[l].split(", ")
    # print(len(aux))
    list_apellido.append(aux[0])
    list_nombre.append(aux[1])
        


# El formato que insertaría en etec_lab.qr_items: ("02'005'002'000063", "Notebook", "Banghoo", 1), (al final poner "";"")
for elemento in range(0,len(old_apellidosNombres)):   
    try:         
        sql = "SELECT nombre, apellido FROM profes WHERE nombre=%s AND apellido=%s"            
        db_etec.cursor.execute(sql, (list_nombre[elemento], list_apellido[elemento]))
        if (len(db_etec.cursor.fetchall())>0):
            print("El elemento ya se encuentra en la base de datos.")
            sql = "SELECT asignaturas FROM profes WHERE asignaturas=%s"
            db_etec.cursor.execute(sql, (list_materias[elemento]))
            if (len(db_etec.cursor.fetchall())>0):
                # UPDATE columna FROM tabla SET cosa1=dato1, cosa2=dato2 WHERE campo1=lugar1
                pass
        else:            
            print(list_nombre[elemento], list_apellido[elemento], list_materias[elemento], list_cursos[elemento])        
            query_sql = "INSERT INTO profes(nombre, apellido, asignaturas, cursos) VALUES(%s, %s, %s, %s);"
            db_etec.cursor.execute(query_sql, (list_nombre[elemento], list_apellido[elemento], list_materias[elemento], list_cursos[elemento]))
            db_etec.connection.commit()
    except TypeError as error:
        print("Hubo un erro, el siguiente: {}".format(error))