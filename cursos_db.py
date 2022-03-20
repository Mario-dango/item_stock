from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic
from PyQt5.QtSql import QSqlQuery
from programas_py.db import ETEC_db
import sys
# from ETEC_cueva import Database

class cursos_db(QWidget):
    def __init__(self, login_estado=False, parent=None):
        super(cursos_db, self).__init__(parent)

        self.estado_login = login_estado
        self.parent = parent

        self.cursos = ['1a', '1b', '2a', '2b', '3i', '3e', '4i', '4e', '5i', '5e', '6i', '6e']
        self.setGeometry(100,100,1200,400)
        icono = "imagenes/logo_etec2.png"
        self.setWindowIcon(QIcon(icono))
        self.setWindowTitle("Cursos en Base de Datos")
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
        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = cursos_db()
    window.show()
    sys.exit(app.exec_())
