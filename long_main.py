from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic
from crear_c import Registro
from login import loginUsuario
from cursos_db import cursos_db
from PyQt5.QtSql import QSqlQuery
from programas_py.db import ETEC_db

import sys

################################## Ventana de Login
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic
from programas_py.db import ETEC_db
from cursos_db import cursos_db
import sys
from crear_c import Registro

class loginUsuario(QDialog):
    def __init__(self):
        super(loginUsuario,self).__init__()
        self.setGeometry(400,400,400,200)
        self.setMaximumSize(400,300)
        self.setMinimumWidth(400)
        self.setWindowTitle("Ingreso de Usuario")
        self.log_estado = False
        self.login_usuario()

    def login_usuario(self):
        self.layout_grid = QGridLayout(self) #Crear un layout grid

        self.lbl_login = QLabel("Login", self)
        self.layout_grid.addWidget(self.lbl_login, 0,0,1,2)
        self.lbl_login.setFont(QFont("Arial", 20))
        self.lbl_login.setAlignment(Qt.AlignCenter)

        self.lbl_nombre = QLabel("Usuario", self)
        self.layout_grid.addWidget(self.lbl_nombre, 1,0,1,1)

        self.lned_nombre = QLineEdit(self)
        self.layout_grid.addWidget(self.lned_nombre, 1,1,1,1)
        self.lned_nombre.resize(220, 20)

        self.lbl_password = QLabel("Contraseña", self)
        self.layout_grid.addWidget(self.lbl_password, 2,0,1,1)

        self.lend_password = QLineEdit(self)
        self.lend_password.setEchoMode(QLineEdit.Password)
        self.layout_grid.addWidget(self.lend_password, 2,1,1,1)
        self.lend_password.resize(220,20)

        self.btn_login = QPushButton("Ingresar", self)
        self.layout_grid.addWidget(self.btn_login, 4,0,1,2)
        self.btn_login.resize(200,40)

        self.chbox_show_p = QCheckBox("Mostrar contraseña",self)
        self.layout_grid.addWidget(self.chbox_show_p, 3,0,1,2)
        self.chbox_show_p.setChecked(False)

        self.no_usuario = QLabel("No estás registrado?", self)
        self.layout_grid.addWidget(self.no_usuario, 5,0,1,2)
        self.no_usuario.setWordWrap(True)
        self.no_usuario.setFont(QFont("Arial",7))

        self.btn_registro = QPushButton("Registrar", self)
        self.layout_grid.addWidget(self.btn_registro, 6,0,1,2)

        self.btn_registro.clicked.connect(self.registro_user)
        self.chbox_show_p.stateChanged.connect(self.mostrar_passw)
        self.btn_login.clicked.connect(self.click_log)

        
        #Establecer conexión a la base de datos MySql        
        self.db_etec = ETEC_db()

    def click_log(self):
        user = self.lned_nombre.text()
        password = self.lend_password.text()
        if password == '':
            QMessageBox.information(self, "Contraseña vacia", "Por favor ingrese su contraseña en el campo de Contraseña.", QMessageBox.Ok, QMessageBox.Ok)
        elif user == '':
            QMessageBox.information(self, "Usuario 0vacio", "Por favor ingrese su nombre de usuario en el campo de Usuario.", QMessageBox.Ok, QMessageBox.Ok)
        else:
            try:            
                sql = "SELECT * FROM cuentas WHERE usuario=%s AND contraseña=%s"            
                self.db_etec.cursor.execute(sql, (user, password))
                if (len(self.db_etec.cursor.fetchall())>0):
                    QMessageBox.information(self, "Inicio de sesión exitoso", "Se inició sesión exitosamente", QMessageBox.Ok, QMessageBox.Ok)
                    self.log_estado = True            
                    self.close()
                    self.consulta = cursos_db()
                    self.consulta.show()
                else:
                    QMessageBox.information(self, "Error", "El nombre de usuario no existe o la contraseña no es correcta.", QMessageBox.Ok, QMessageBox.Ok)
            except:
                QMessageBox.information(self, "Error", "Problemas técnicos al conectar con la base de datos", QMessageBox.Ok, QMessageBox.Ok)

    def mostrar_passw(self, state):
        if state == Qt.Checked:
            self.lend_password.setEchoMode(QLineEdit.Normal)
        else:
            self.lend_password.setEchoMode(QLineEdit.Password)

    def registro_user(self):
        self.crear_nuevo_usr = Registro()
        self.log_estado = True
        self.close()
        self.crear_nuevo_usr.show()
        if self.crear_nuevo_usr.registro is True:
            self.show()
        else:
            self.close()

    def closeEvent(self, event):
        if self.log_estado is True:
            event.accept()
        else:
            msg_cerrar = QMessageBox.question(self, "Salir de la Aplicación", "¿Seguro que desea salir?", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            if msg_cerrar == QMessageBox.Yes:
                event.accept()
            else:
                event.ignore()

######################### Ventana de Crear Cuenta
class Registro(QWidget):
    def __init__(self):
        super(Registro, self).__init__()
        self.setGeometry(100,100,400,400)
        self.setWindowTitle("Registro de Usuario")
        self.display_widgets()
        self.registro = False

    def display_widgets(self):
        new_user_img = "imagenes/logo_etec2.png"
        self.layout = QGridLayout(self) #Crear un layout grid
        try:
            with open(new_user_img):
                etiqueta_imagen = QLabel(self)
                pixmap = QPixmap(new_user_img)
                etiqueta_imagen.setPixmap(pixmap)
                etiqueta_imagen.resize(90,90)
                etiqueta_imagen.setAlignment(Qt.AlignLeft)
                etiqueta_imagen.setMinimumWidth(340)
                etiqueta_imagen.setAlignment(Qt.AlignCenter)
                # etiqueta_imagen.setMinimumSize(343,95)
                self.layout.addWidget(etiqueta_imagen, 1,0,1,2)

        except FileNotFoundError:
            print("Error al intentar encontrar imagen.")

        etiqueta_login = QLabel("Crear nueva cuenta", self)
        etiqueta_login.move(0,20)
        etiqueta_login.setFont(QFont("Arial",20))
        etiqueta_login.resize(400,40)
        etiqueta_login.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(etiqueta_login, 0,0,1,2)
        
        # Apartado para crear eriquetas de nombre de usuario y nombre completo
        self.et_nombre = QLabel("Nombre", self)
        self.layout.addWidget(self.et_nombre, 2,0,1,1)

        self.ent_nombre = QLineEdit(self)
        self.ent_nombre.resize(200,20)
        self.layout.addWidget(self.ent_nombre, 2,1,1,1)

        self.et_apellido = QLabel("Apellidos", self)
        self.layout.addWidget(self.et_apellido, 3,0,1,1)

        self.ent_apellido = QLineEdit(self)
        self.ent_apellido.resize(200,20)
        self.layout.addWidget(self.ent_apellido, 3,1,1,1)

        self.et_usuario = QLabel("Usuario", self)
        self.layout.addWidget(self.et_usuario, 4,0,1,1)

        self.ent_usuario = QLineEdit(self)
        self.ent_usuario.resize(200,20)
        self.layout.addWidget(self.ent_usuario, 4,1,1,1)

        self.et_contrasena = QLabel("Contraseña", self)
        self.layout.addWidget(self.et_contrasena, 5,0,1,1)

        self.ent_contrasena = QLineEdit(self)
        self.ent_contrasena.setEchoMode(QLineEdit.Password)
        self.ent_contrasena.resize(200,20)
        self.layout.addWidget(self.ent_contrasena, 5,1,1,1)

        self.et_conf_contr = QLabel("Confirmar pssw", self)
        self.layout.addWidget(self.et_conf_contr, 6,0,1,1)

        self.ent_conf_contr = QLineEdit(self)
        self.ent_conf_contr.setEchoMode(QLineEdit.Password)
        self.ent_conf_contr.resize(200,20)
        self.layout.addWidget(self.ent_conf_contr, 6,1,1,1)

        self.et_correo = QLabel("Correo", self)
        self.layout.addWidget(self.et_correo, 7,0,1,1)

        self.ent_correo = QLineEdit(self)
        self.ent_correo.resize(200,20)
        self.layout.addWidget(self.ent_correo, 7,1,1,1)

        self.et_correo_etec = QLabel("Correo ETEC", self)
        self.layout.addWidget(self.et_correo_etec, 8,0,1,1)

        self.ent_correo_etec = QLineEdit(self)
        self.ent_correo_etec.resize(200,20)
        self.layout.addWidget(self.ent_correo_etec, 8,1,1,1)

        self.et_celular = QLabel("Celular", self)
        self.layout.addWidget(self.et_celular, 9,0,1,1)

        self.ent_celular = QLineEdit(self)
        self.ent_celular.resize(200,20)
        self.layout.addWidget(self.ent_celular, 9,1,1,1)

        #Crear boton de registro
        self.boton_registro = QPushButton("Registrar", self)
        self.boton_registro.resize(200,40)
        self.layout.addWidget(self.boton_registro, 10,1,1,1)
        #crear señal de boton
        self.boton_registro.clicked.connect(self.registro)

        ###############################################
        #Conexión a la base de datos de la cuevacha
        self.db_etec = ETEC_db()

    def registro(self):
        texto_password = self.ent_contrasena.text()
        password_confirmar = self.ent_conf_contr.text()

        if texto_password != password_confirmar:
            QMessageBox.warning(self, "Mensaje de error", "Las contraseñas ingresadas no coinciden, por favor vuelva a intentarlo", QMessageBox.Ok, QMessageBox.Ok)
        else:            
            txt_nombre = self.ent_nombre.text()
            txt_apellido = self.ent_apellido.text()
            txt_correo = self.ent_correo.text()
            txt_celular = self.ent_celular.text()
            txt_usuario = self.ent_usuario.text()
            txt_passw = self.ent_contrasena.text()
            txt_correo_etec = self.ent_correo_etec.text()
            query_sql = "INSERT INTO cuentas(nombre, apellido, correo, celular, usuario, contraseña, correo_etec) VALUES(%s, %s, %s, %s, %s, %s, %s)"
            self.db_etec.cursor.execute(query_sql, (txt_nombre, txt_apellido, txt_correo, txt_celular, txt_usuario, txt_passw, txt_correo_etec))
            self.db_etec.connection.commit()
            QMessageBox.information(self, "Correcto", "Datos guardados", QMessageBox.Discard)

    def closeEvent(self, event):
        msg_cerrar = QMessageBox.question(self, "Salir de la Aplicación", "¿Seguro que desea salir?", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if msg_cerrar == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

######################################### Ventana de acceso a la base de datos

class cursos_db(QWidget):
    def __init__(self):
        super(cursos_db, self).__init__()
        self.cursos = ['1a', '1b', '2a', '2b', '3i', '3e', '4i', '4e', '5i', '5e', '6i', '6e']
        self.setGeometry(100,100,1200,400)
        icono = "imagenes/logo_etec2.png"
        self.setWindowTitle("Cursos en Base de Datos")
        self.setWindowIcon(QIcon(icono))
        self.setWindowFlags(Qt.WindowMinimizeButtonHint | Qt.WindowCloseButtonHint |
                            Qt.MSWindowsFixedSizeDialogHint)
        self.display_widgets()

    def display_widgets(self):
        new_user_img = "imagenes/logo_etec.png"

        self.layout = QGridLayout(self) #Crear un layout grid

        try:
            with open(new_user_img):
                etiqueta_imagen = QLabel(self)
                pixmap = QPixmap(new_user_img)
                etiqueta_imagen.setPixmap(pixmap)
                etiqueta_imagen.setAlignment(Qt.AlignLeft)
                etiqueta_imagen.setMinimumWidth(340)
                etiqueta_imagen.setMinimumSize(343,95)
                self.layout.addWidget(etiqueta_imagen, 1,1,1,2)

        except FileNotFoundError:
            print("Error al intentar encontrar imagen.")
        
        etiqueta_login = QLabel("Horarios y Materias", self)
        etiqueta_login.setFont(QFont("Arial",20))
        etiqueta_login.setMaximumSize(400,40)
        etiqueta_login.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(etiqueta_login, 0,0,1,2)
        
        # Apartado para crear eriquetas de nombre de usuario y nombre completo
        self.et_curos = QLabel("Curso", self)
        self.layout.addWidget(self.et_curos, 2,0,1,1)

        # self.edt_curso = QLineEdit("Ej: 5i, 1a, 2b, 6e",self)
        self.edt_curso = QLineEdit(self)
        self.edt_curso.setMaxLength(2)
        self.edt_curso.setMaximumSize(350,20)
        self.edt_curso.setAlignment(Qt.AlignLeft)
        self.layout.addWidget(self.edt_curso, 2,1,1,1)

        self.et_mmodulo = QLabel("Medio módulo", self)
        self.layout.addWidget(self.et_mmodulo, 3,0,1,1)
        self.et_mmodulo.setWordWrap(True)

        # self.edt_mmodulo = QLineEdit("Ej: 2 (Sería de 8:25 a 9:05)",self)
        self.edt_mmodulo = QLineEdit(self)
        self.edt_mmodulo.setMaximumSize(350,20)
        self.edt_mmodulo.setAlignment(Qt.AlignLeft)
        self.layout.addWidget(self.edt_mmodulo, 3,1,1,1)

        self.et_dia = QLabel("Día", self)
        self.layout.addWidget(self.et_dia, 4,0,1,1)

        # self.edt_dia = QLineEdit("Ej: EIP (Electrónica Industrial y de Potencia)",self)
        self.edt_dia = QLineEdit(self)
        self.edt_dia.setMaximumSize(350,20)
        self.edt_dia.setAlignment(Qt.AlignLeft)
        self.layout.addWidget(self.edt_dia, 4,1,1,1)

        self.et_materia = QLabel("Materia", self)
        self.layout.addWidget(self.et_materia, 5,0,1,1)

        # self.edt_materia = QLineEdit("Ej: EIP (Electrónica Industrial y de Potencia)",self)
        self.edt_materia = QLineEdit(self)
        self.edt_materia.setMaximumSize(350,20)
        self.edt_materia.setAlignment(Qt.AlignLeft)
        self.layout.addWidget(self.edt_materia, 5,1,1,1)
        

        self.et_nombre_p = QLabel("Nombre de Profesor", self)
        self.layout.addWidget(self.et_nombre_p, 6,0,1,1)

        # self.edt_profesor = QLineEdit("Ej: Mario Papetti",self)
        self.edt_nombre_p = QLineEdit(self)
        self.edt_nombre_p.setMaximumSize(350,20)
        self.edt_nombre_p.setAlignment(Qt.AlignLeft)
        self.layout.addWidget(self.edt_nombre_p, 6,1,1,1)

        self.et_apellido_p = QLabel("Apellido de Profesor", self)
        self.layout.addWidget(self.et_apellido_p, 7,0,1,1)

        # self.edt_profesor = QLineEdit("Ej: Mario Papetti",self)
        self.edt_apellido_p = QLineEdit(self)
        self.edt_apellido_p.setMaximumSize(350,20)
        self.edt_apellido_p.setAlignment(Qt.AlignLeft)
        self.layout.addWidget(self.edt_apellido_p, 7,1,1,1)

        self.tabla = QTableWidget() #Crear la tabla
        self.tabla.insertRow(3)
        self.tabla.setTextElideMode(Qt.ElideRight)
        self.layout.addWidget(self.tabla, 0,2,8,1)
        self.tabla.setColumnCount(8)
        columnas = ['Medio módulo', 'Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Horas', 'reservas']
        self.tabla.setHorizontalHeaderLabels(columnas)
        self.tabla.setMinimumSize(700,500)
        # Establecer el ajuste de palabras del texto 
        self.tabla.setWordWrap(False)
        # Deshabilitar resaltado del texto del encabezado al seleccionar una fila
        self.tabla.horizontalHeader().setHighlightSections(False)
        # Ocultar encabezado vertical
        self.tabla.verticalHeader().setVisible(False)
        # Dibujar el fondo usando colores alternados
        self.tabla.setAlternatingRowColors(True)
        # Deshabilitar edición
        self.tabla.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # Deshabilitar el comportamiento de arrastrar y soltar
        self.tabla.setDragDropOverwriteMode(False)
        # Seleccionar toda la fila
        self.tabla.setSelectionBehavior(QAbstractItemView.SelectRows)
        # Seleccionar una fila a la vez
        self.tabla.setSelectionMode(QAbstractItemView.SingleSelection)
        
        menu = QMenu()
        for indice, columna in enumerate(columnas, start=0):
            accion = QAction(columna, menu)
            accion.setCheckable(True)
            accion.setChecked(True)
            accion.setData(indice)

            menu.addAction(accion)
        
        # Menú contextual
        self.tabla.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tabla.customContextMenuRequested.connect(self.menuContextual)

        #Crear boton de registro
        self.boton_insertar = QPushButton("Insertar", self)
        self.boton_insertar.resize(150,40)
        self.layout.addWidget(self.boton_insertar, 8,0,1,1)
        #crear señal de boton
        self.boton_insertar.clicked.connect(self.insertar)
        #Crear boton de registro
        self.boton_consultar = QPushButton("Consultar", self)
        self.boton_consultar.resize(150,40)
        self.layout.addWidget(self.boton_consultar, 8,1,1,1)
        #crear señal de boton
        self.boton_consultar.clicked.connect(self.consultar)

        


    def consultar(self):
        txt_materia = self.edt_materia.text()
        txt_mmodulo = self.edt_mmodulo.text()
        txt_dia = self.edt_dia.text()
        txt_apellido_p = self.edt_apellido_p.text()
        txt_nombre_p = self.edt_nombre_p.text()
        txt_curso = self.edt_curso.text()

        print(txt_curso)
        print(txt_mmodulo)
        print(txt_dia)
        print(txt_materia)
        print(txt_nombre_p)
        print(txt_apellido_p)
        ###############################################
        #Conexión a la base de datos de la cuevacha
        self.db_etec = ETEC_db()

        if ((txt_materia == '') and (txt_mmodulo == '') and (txt_nombre_p == '') and (txt_apellido_p == '') and (txt_curso in self.cursos)):  
            self.tabla.clearContents()                  #Borra el contenido de la tabla
            self.tabla.setRowCount(0)                   #Reseteo el contador de filas para que no me agregue mas filas
            row = 0
            sql = "SELECT * FROM {}".format(txt_curso)
            self.db_etec.cursor.execute(sql)
            get_sql = self.db_etec.cursor.fetchall()
            for query in get_sql:
                self.tabla.insertRow(row)
                medio_modulo = QTableWidgetItem(str(query[0]))
                lunes = QTableWidgetItem(str(query[1]))
                martes = QTableWidgetItem(str(query[2]))
                miercoles = QTableWidgetItem(str(query[3]))
                jueves = QTableWidgetItem(str(query[4]))
                viernes = QTableWidgetItem(str(query[5]))
                horas = QTableWidgetItem(str(query[6]))
                reservas = QTableWidgetItem(str(query[7]))
                
                self.tabla.setItem(row, 0, medio_modulo)
                self.tabla.setItem(row, 1, lunes)
                self.tabla.setItem(row, 2, martes)
                self.tabla.setItem(row, 3, miercoles)
                self.tabla.setItem(row, 4, jueves)
                self.tabla.setItem(row, 5, viernes)
                self.tabla.setItem(row, 6, horas)
                self.tabla.setItem(row, 7, reservas)
                row = row + 1

        elif ((txt_materia == '') and (txt_mmodulo == '') and ((txt_nombre_p != '') or (txt_apellido_p != '')) and (txt_curso == '')):            
            self.tabla.clearContents()                  #Borra el contenido de la tabla
            self.tabla.setRowCount(0)                   #Reseteo el contador de filas para que no me agregue mas filas
            row = 0
            sql = "SELECT profes FROM apellido WHERE={}".format(txt_apellido_p)
            columnas = ['ID Profe', 'Nombre', 'Apellido', 'Correo', 'Celular', 'Cursos', 'Asignaturas', 'Reservas']
            self.tabla.setHorizontalHeaderLabels(columnas)
            self.db_etec.cursor.execute(sql)
            get_sql = self.db_etec.cursor.fetchall()
            for query in get_sql:
                self.tabla.insertRow(row)
                idprofes = QTableWidgetItem(str(query[0]))
                nombre = QTableWidgetItem(str(query[1]))
                apellido = QTableWidgetItem(str(query[2]))
                correo = QTableWidgetItem(str(query[3]))
                celular = QTableWidgetItem(str(query[4]))
                curso = QTableWidgetItem(str(query[5]))
                asignaturas = QTableWidgetItem(str(query[6]))
                reservas_idreservas = QTableWidgetItem(str(query[7]))
                
                self.tabla.setItem(row, 0, idprofes)
                self.tabla.setItem(row, 1, nombre)
                self.tabla.setItem(row, 2, apellido)
                self.tabla.setItem(row, 3, correo)
                self.tabla.setItem(row, 4, celular)
                self.tabla.setItem(row, 5, curso)
                self.tabla.setItem(row, 6, asignaturas)
                self.tabla.setItem(row, 7, reservas_idreservas)
                row = row + 1
        elif ((txt_materia == '') and (txt_mmodulo != '') and (txt_nombre_p == '') and (txt_apellido_p == '') and (txt_curso != '')): 
            pass
        elif ((txt_materia == '') and (txt_mmodulo == '') and (txt_nombre_p == '') and (txt_apellido_p == '') and (txt_curso == '')): 
            pass
        elif ((txt_materia == '') and (txt_mmodulo == '') and (txt_nombre_p == '') and (txt_apellido_p == '') and (txt_curso == '')): 
            pass
        elif ((txt_materia == '') and (txt_mmodulo == '') and (txt_nombre_p == '') and (txt_apellido_p == '') and (txt_curso == '')): 
            pass
        elif ((txt_materia == '') and (txt_mmodulo == '') and (txt_nombre_p == '') and (txt_apellido_p == '') and (txt_curso == '')): 
            pass

        else:
            QMessageBox.warning(self, "Mensaje de error", "Revise los valores ingresados para realizar la consulta adecuada.", QMessageBox.Ok, QMessageBox.Ok)

        
    def insertar(self):
        txt_materia = self.edt_materia.text()
        txt_mmodulo = self.edt_mmodulo.text()
        txt_profesor = self.edt_profesor.text()
        txt_curso = self.edt_curso.text()
        self.db_etec = ETEC_db()

        if (txt_mmodulo is str(range(1, 13)) or (txt_curso in self.cursos)):  
            nombre = self.entrada_nombre.text()
            passw = self.entrada_contraseña.text()
            sql = "INSERT INTO usuarios(nombre, contraseña) VALUES (:nombre, :contraseña)"
            consulta = QSqlQuery()
            consulta.prepare(sql)
            consulta.bindValue(":nombre", nombre)
            consulta.bindValue(":contraseña", passw)
            estado = consulta.exec_()

        else:
            QMessageBox.warning(self, "Mensaje de error", "El valor de Medio módulo no es valido, recordar que es un valor entero que va desde 1 a 13", QMessageBox.Ok, QMessageBox.Ok)
    
    def menuContextual(self, posicion):
        indices = self.tabla.selectedIndexes()

        if indices:
            menu = QMenu()

            itemsGrupo = QActionGroup(self)
            itemsGrupo.setExclusive(True)
            
            menu.addAction(QAction("Copiar todo", itemsGrupo))

            columnas = [self.tabla.horizontalHeaderItem(columna).text()
                        for columna in range(self.tabla.columnCount())
                        if not self.tabla.isColumnHidden(columna)]

            copiarIndividual = menu.addMenu("Copiar individual") 
            for indice, item in enumerate(columnas, start=0):
                accion = QAction(item, itemsGrupo)
                accion.setData(indice)
                
                copiarIndividual.addAction(accion)

            itemsGrupo.triggered.connect(self.copiarTableWidgetItem)
            
            menu.exec_(self.tabla.viewport().mapToGlobal(posicion))

    def copiarTableWidgetItem(self, accion):
        filaSeleccionada = [dato.text() for dato in self.tabla.selectedItems()]
            
        if accion.text() == "Copiar todo":
            filaSeleccionada = tuple(filaSeleccionada)
        else:
            filaSeleccionada = filaSeleccionada[accion.data()]

        print(filaSeleccionada)

        return
        

class principal(QWidget):
    def __init__(self):
        super(principal, self).__init__()
        self.initialize()

    def initialize(self):
        self.setGeometry(100,100,200,200)
        self.setWindowTitle("Principal")
        self.display_img()

    def display_img(self):
        titulo_etec = "imagenes/Etec-fondo-blanco2.png"
        self.layout = QGridLayout(self) #Crear un layout grid
        try: 
            with open(titulo_etec):
                logo_etiqueta = QLabel(self)
                pixmap1 = QPixmap(titulo_etec)
                logo_etiqueta.setPixmap(pixmap1)
                logo_etiqueta.move(180,100)
                logo_etiqueta.resize(200,90)

        except FileNotFoundError:
            print("Error al intentar encontrar la imagen")


        self.et_apellido_p = QLabel("Apellido de Profesor", self)
        self.layout.addWidget(self.et_apellido_p, 7,0,1,1)

        # self.edt_profesor = QLineEdit("Ej: Mario Papetti",self)
        self.edt_apellido_p = QLineEdit(self)
        self.edt_apellido_p.setMaximumSize(350,20)
        self.edt_apellido_p.setAlignment(Qt.AlignLeft)
        self.layout.addWidget(self.edt_apellido_p, 7,1,1,1)


class mainWindow(QMainWindow):
    def __init__(self):
        super(mainWindow, self).__init__()

        #### Definición 
        self.widgets_aplicaciones = QStackedWidget(self)
        # Creo los objetos correspondientes a cada ventana
        self.ventana_ingresar = loginUsuario()                      # ventana para ingresar con cuenta
        self.ventana_registrar = Registro()                  # ventana para registrar cuenta de acceso
        self.ventana_db_etec = cursos_db()           # ventana para acceder a la base de datos graficamente
        self.ventana_principal = principal()                # ventana principal para la visualización de datos
        # self.reservas = pedidos()                    # ventana para visualizar y gestionar pedidos de reservas  

        self.widgets_aplicaciones.addWidget(self.ventana_ingresar)                  # Agrego el objeto ventana ingresar 
        self.widgets_aplicaciones.addWidget(self.ventana_registrar)                 # Agrego el objeto ventana de registro
        self.widgets_aplicaciones.addWidget(self.ventana_db_etec)           # Agrego el objeto ventana a la base de datos
        self.widgets_aplicaciones.addWidget(self.ventana_principal)           # Agrego el objeto ventana principal

        self.setCentralWidget(self.widgets_aplicaciones)                # Seteamos cómo central widget

        # self.widgets_aplicaciones.currentWidget(self.ingresar)

        #### conexiones a los eventos
        
        self.ventana_ingresar.btn_registro.clicked.connect(self.registro_user)
        self.ventana_ingresar.btn_login.clicked.connect(self.click_log)
        self.ventana_registrar.boton_registro.clicked.connect(self.registro)
        # self.registrar.boton_registro.clicked.conncet(self.registro)


    
    def registro_user(self):
        self.widgets_aplicaciones.currentWidget(self.ventana_registrar)                 # Agrego el objeto ventana de registro

    # def des_logear(self):
        
    def click_log(self):
        user = self.lned_nombre.text()
        password = self.lend_password.text()
        if password == '':
            QMessageBox.information(self, "Contraseña vacia", "Por favor ingrese su contraseña en el campo de Contraseña.", QMessageBox.Ok, QMessageBox.Ok)
        elif user == '':
            QMessageBox.information(self, "Usuario vacio", "Por favor ingrese su nombre de usuario en el campo de Usuario.", QMessageBox.Ok, QMessageBox.Ok)
        else:
            try:            
                sql = "SELECT * FROM cuentas WHERE usuario=%s AND contraseña=%s"            
                self.db_etec.cursor.execute(sql, (user, password))
                if (len(self.db_etec.cursor.fetchall())>0):
                    QMessageBox.information(self, "Inicio de sesión exitoso", "Se inició sesión exitosamente", QMessageBox.Ok, QMessageBox.Ok)
                    self.log_estado = True            
                    # self.close()
                    # self.consulta = cursos_db()
                    # self.consulta.show()
                else:
                    QMessageBox.information(self, "Error", "El nombre de usuario no existe o la contraseña no es correcta.", QMessageBox.Ok, QMessageBox.Ok)
            except:
                QMessageBox.information(self, "Error", "Problemas técnicos al conectar con la base de datos", QMessageBox.Ok, QMessageBox.Ok)


    def registro(self):
        texto_password = self.ent_contrasena.text()
        password_confirmar = self.ent_conf_contr.text()

        if texto_password != password_confirmar:
            QMessageBox.warning(self, "Mensaje de error", "Las contraseñas ingresadas no coinciden, por favor vuelva a intentarlo", QMessageBox.Ok, QMessageBox.Ok)
        else:            
            txt_nombre = self.ent_nombre.text()
            txt_apellido = self.ent_apellido.text()
            txt_correo = self.ent_correo.text()
            txt_celular = self.ent_celular.text()
            txt_usuario = self.ent_usuario.text()
            txt_passw = self.ent_contrasena.text()
            txt_correo_etec = self.ent_correo_etec.text()
            query_sql = "INSERT INTO cuentas(nombre, apellido, correo, celular, usuario, contraseña, correo_etec) VALUES(%s, %s, %s, %s, %s, %s, %s)"
            self.db_etec.cursor.execute(query_sql, (txt_nombre, txt_apellido, txt_correo, txt_celular, txt_usuario, txt_passw, txt_correo_etec))
            self.db_etec.connection.commit()
            QMessageBox.inf

    def on_off_autoenvio(self):
        pass

    def reservas(self):
        pass

    def ver_mod_db(self):
        pass

        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = mainWindow()
    window.show()
    sys.exit(app.exec_())
