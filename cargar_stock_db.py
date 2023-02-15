import pandas as pd
import xlrd
from programas_py.db import ETEC_db

todas_cuentas = []
todos_nombres = []
todos_apellidos = []
todos_nombresCompletos = []
lista_anterior =[]

curso_1 = []
curso_2 = []
curso_3 = []
curso_4 = []
curso_5 = []
curso_6 = []

all_cursos = []
    
path_curso = "Excel\\item_stock.csv"

wb = xlrd.open_workbook(path_curso)

# hoja = wb.sheet_by_index(0)
# print(hoja.nrows)
# print(hoja.ncols)
# print(hoja.cell_value(5, 3))

hoja = wb.sheet_by_name('item_stock')
# print(hoja.nrows)
# print("\n")
# print("\n")
# print("\n")
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
        
list_cantidades = []
for i in range(1,hoja.nrows):
    if hoja.cell_value(i,2) == '':
        pass
    else:
        list_cantidades.append(hoja.cell_value(i,2))



db_etec = ETEC_db()
crear_db = """
CREATE SCHEMA IF NOT EXISTS `ETEC_lab` ;
USE `ETEC_lab` ;
"""
db_etec.cursor.execute(crear_db)

cargar_items_stock = """

DROP TABLE IF EXISTS `ETEC_lab`.`qr_items` ;

CREATE TABLE IF NOT EXISTS `ETEC_lab`.`qr_items` (
  `qr_code` VARCHAR(45) NOT NULL COMMENT 'Códigos QR generados por \"terceros\" de la mano de la Universidad de Mendoza.',
  `name_item` VARCHAR(45) NULL DEFAULT 'Sin_nombre' COMMENT 'Columna referida al nombre del ítem, al cual se encuentra adherido código QR correspondiente.',
  `marca_item` VARCHAR(45) NULL DEFAULT 'Sin_marca/fabricante' COMMENT 'Columna para especificar la Marca/Modelo/Fabricante del ítem.',
  `cantidad` INT NULL DEFAULT 0 COMMENT 'Columna para especificar la Marca/Modelo/Fabricante del ítem.',
  `qr_img` BLOB NULL  COMMENT 'Columna para almacenar la imagen generada del QR del ítem.',
  `qr_url_img` VARCHAR(45) NULL DEFAULT 'Sin dirección de imagen' COMMENT 'Columna para especificar la dirección al servidor del ETEC relacionado al QR del ítem.')
ENGINE = InnoDB;

insert into etec_lab.qr_items (qr_code, name_item, marca_item, cantidad, qr_img, qr_url_img)
values
	  ("{}", "{}", "Banghoo", 1, "", ""),
	  ("notebook_002", "Computadora", "Banghoo", 1, "imagen_qr", "NADA"),
      ###########################AUTOMATIZAR
"""


query_sql = "INSERT INTO cuentas(nombre, apellido, correo, celular, usuario, contraseña, correo_etec) VALUES(%s, %s, %s, %s, %s, %s, %s)"
db_etec.cursor.execute(query_sql, (txt_nombre, txt_apellido, txt_correo, txt_celular, txt_usuario, txt_passw, txt_correo_etec))
db_etec.connection.commit()














# print(old_apellidosNombres)
# print(len(item)) ## 88 con "legajo" -> 87 con "Mariela Paz Martinez" -> 86 es decir (/2) que 43 son legajos

list_legajos = []
list_tel_y_dir = []
list_dir = []
list_dep = []
list_tel = []
list_correo_p = []
list_cuenta = []
list_correo_etec = []
list_nombre = []
list_apellido = []
list_dni = []
list_clave = []
list_nombre_completo = old_apellidosNombres

############################################## MODULO de separación de legajos
for j in range(0,len(old_legajo)):
    if j == 0:
        list_legajos.append("Legajos")
        list_dir.append("Direcciones")
        list_dep.append("Departamento")
        list_tel.append("Telefonos")
        list_correo_etec.append("Correos_ETec")
        list_cuenta.append("Cuentas")
        list_correo_p.append("Correos_Personales")
        list_tel_y_dir.append("Direccion, Telefonos y Correos")
        list_dni.append("Documentos_DNI")
    else:
        if j%2 == 0:
            ## Separo los datos vacios de Tel y () de los legajos
            # try:
            #     no_valido = old_legajo[j].find("() -   - Tel:  ")
            #     print(no_valido)
            # except TypeError as e:
            #     print(e)


            # if old_legajo[j].index("(") == 5:
            #     ## Ya reformo los que no tienen datos cargados
            #     list_tel_y_dir.append("NaN")
            #     # print("encontre un NaN")
            #     list_dir.append("N/A")
            #     list_dep.append("N/A")
            #     list_tel.append("N/A")
            # else:
            #     ## agrego a quienes tienen datos de dirección y telefono
            #     list_tel_y_dir.append(old_legajo[j])
            #     items =old_legajo[j].split("-")
            #     list_dir.append(items[0])
            #     list_dep.append(items[1])
            #     tel_email = items[2].split(" ")
            #     # print(tel_email[2])
            #     if tel_email[2] == "":
            #         list_tel.append("N/A") 
            #         try:      
            #             if len(tel_email)>2 :
            #                 if tel_email[3] == "":
            #                     list_correo_p.append("N/A")           
            #                 else:
            #                     try:
            #                         invalid = tel_email[3].find("@")
            #                     except ValueError:
            #                         list_correo_p.append(tel_email[3])
            #         except TypeError as e:
            #             print("Se produjo un error: {}".format(e))
            #     else:
            #         list_tel.append(tel_email[2])
            #         try:      
            #             if tel_email[3] == "":
            #                 list_correo_p.append("N/A")       
            #             else:
            #                 try:
            #                     invalid = tel_email[3].find("@")
            #                 except ValueError:
            #                     list_correo_p.append(tel_email[3])      
            #         except TypeError as e:
            #             print("Se produjo un error: {}".format(e))

            pass

        else:
            if isinstance(old_legajo[j], float): ## Pregunto si los pares son números
                list_legajos.append(old_legajo[j])
            else:
                ## Quito a Mariela Paz Martinez, pobrecita :(
                pass
################################################ FIN de separación de legajos

################################################
for l in range(0,len(old_apellidosNombres)):
    # print((old_apellidosNombres[l]))
    aux = old_apellidosNombres[l].split(", ")
    list_apellido.append(aux[0])
    list_nombre.append(aux[1])
################################################

################################################
for i in range(0,len(old_dni)):
    try:
        if old_dni[i].index("N") == 1:
            aux = old_dni[i].split(" ")
            list_dni.append(aux[1])
        else:
            pass
    except ValueError:
        pass
################################################

### Creación de cuentas a partir de nombres y apellidos
### Creación de correos del ETec
for j in range(1,len(list_nombre)):
    letra = list(list_nombre[j])
    apellido = list_apellido[j].split(" ")
    cuenta = (letra[0] + "." + apellido[0]).lower()
    list_cuenta.append(cuenta)
    correo_etec = cuenta + "@etec.um.edu.ar"
    list_correo_etec.append(correo_etec)
todos_nombresCompletos.append(list_nombre_completo)
list_nombre_completo[0] = "NombresCompletos"

cont = 0
for i in range(0,len(list_cuenta)):
    for j in range(0,len(list_cuenta)):
        if i != len(list_cuenta) and i != j:
            if list_cuenta[i] == list_cuenta[j]:
                print("\n")
                print("Colisión de cuentas entre: {} y {}".format(list_nombre_completo[i], list_nombre_completo[j]))
                print("Se formatean las cuentas donde la segunda cuenta queda modificada.")
                letra = list(list_nombre[j])
                apellido = list_apellido[j].split(" ")
                cuenta = (letra[0] + letra[1] + "." + apellido[0]).lower()
                list_cuenta[j] = cuenta
                print("Siendo así {} y {} respectivamente".format(list_cuenta[i], list_cuenta[j]))
                print("\n")
            
# todas_cuentas = (lista_anterior + list_cuenta)
todas_cuentas.append(list_cuenta)
todos_apellidos.append(list_apellido)
todos_nombres.append(list_nombre)
            

################################################
for k in range(0,len(list_dni)):
    if k == 0:
        list_clave.append("Claves")
    else:
        aux = "ETec_" + list_dni[k]
        list_clave.append(aux)
        pass
################################################

nuevo_csv = [list_legajos, list_nombre_completo, list_apellido, list_nombre, list_cuenta ,
            list_clave, list_correo_etec, list_correo_p, list_dir, list_dep, list_tel]

# print((nuevo_csv))

curso_csv = pd.DataFrame(nuevo_csv
                        , columns= None
                        # , columns=[
                        #         "Legajos",
                        #         "Direcciones",
                        #         "Departamento",
                        #         "Telefonos",
                        #         "Apellidos",
                        #         "Nombres",
                        #         "Correos_ETec",
                        #         "Correos_Personales",
                        #         "Direccion, Telefonos y Correos",
                        #         "Documentos_DNI"
                        #         ]
                        )

# columnas = curso_csv.columns.values[1:]
curso_csv = curso_csv.transpose()
# curso_csv.drop([0], axis=0, inplace=True)
all_cursos.append(nuevo_csv)

# curso_csv.to_excel("test_01.xls", index=False, index_label=False, columns= None)
curso_csv.to_csv("test_0{}.csv".format(cursos), index=False, header=False, sep=";", encoding="utf-8")


# initializing the data and an empty list
una_sola_lista = []
for k in range(0,4):
if k == 0:
    data = todas_cuentas
    for item in data:
        una_sola_lista += item
    todas_cuentas = una_sola_lista
elif k == 1:
    data = todos_nombres
    for item in data:
        una_sola_lista += item
    todos_nombres = una_sola_lista
elif k == 2:
    for item in todos_apellidos:
        una_sola_lista += item
    todos_apellidos = una_sola_lista
elif k == 3:
    for item in todos_nombresCompletos:
        una_sola_lista += item
    todos_nombresCompletos = una_sola_lista
else:
    print("Problemas en formatear listas.")


