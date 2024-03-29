
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic
from crear_c import Registro
from login import loginUsuario
from cursos_db import cursos_db
from PyQt5.QtSql import QSqlQuery
from programas_py.db import ETEC_db
import datetime
import locale

from fechas import encontra_medio_modulo
locale.setlocale(locale.LC_TIME, "es_ES")  # Para setear el día en español


import sys

################## Nota mental para siguientes pasos
        ### Crear ventana de reservas
        ### vincular la lectura de los labels con la escritura en la db a su vez actualizar la tabla
        ### mostrar reservas pendientes en la lista izquierda
        ### Hacer que los ítems que se habían retirado tengan una bandera de anteriormente retirados (por si se retira el mismo ítem en menos de un día)
        ### lograr identificar los laboratorios en query_log
class principal(QWidget):
    def __init__(self, parent = None):
        super(principal, self).__init__(parent)
        self.estado_autoenvio = False
        self.initialize()

    def initialize(self):
        self.setGeometry(100,100,1200,800)
        self.setWindowTitle("Principal")
        icono = "imagenes/logo_etec2.png"
        self.setWindowIcon(QIcon(icono))
        self.setWindowTitle("Ventana Principal de Control de Items")
        self.setWindowFlags(Qt.WindowMinimizeButtonHint | Qt.WindowCloseButtonHint |
                            Qt.MSWindowsFixedSizeDialogHint)
        self.display_img()

    def display_img(self):
        self.layout_principal = QGridLayout(self) #Crear un layout grid

        self.et_reservas = QLabel("Registro de reservas pendientes", self)
        self.layout_principal.addWidget(self.et_reservas, 0,0,1,1)
        self.et_reservas.setMaximumSize(200,20)

        self.lst_reservas = QListWidget(self)
        self.layout_principal.addWidget(self.lst_reservas, 1,0,4,1)
        self.lst_reservas.setMaximumWidth(450)

        self.btn_reservas = QPushButton("Reservas", self)
        self.layout_principal.addWidget(self.btn_reservas, 5,0,1,1)

        self.tbl_stock = QTableWidget() #Crear la tbl_stock
        self.tbl_stock.setRowCount(4)
        self.tbl_stock.setTextElideMode(Qt.ElideRight)
        # self.tbl_stock.setColumnCount(8)
        # columnas = ['Computadoras', 'Proyectores', 'Parlantes', 'Laboratorios', 'Pinzas', 'Alicates', 'Protoboards', 'Multimetros']

        filas = ["Total:", "Disponibles:", "Entregados:", "Bajo Reserva proxima:"]
        # self.tbl_stock.setHorizontalHeaderLabels(columnas)
        self.tbl_stock.setMinimumSize(200,170)
        # self.tbl_stock.setMaximumSize(1200,170)
        # Establecer el ajuste de palabras del texto
        self.tbl_stock.setWordWrap(False)
        # Deshabilitar resaltado del texto del encabezado al seleccionar una fila
        self.tbl_stock.horizontalHeader().setHighlightSections(False)
        self.tbl_stock.setVerticalHeaderLabels(filas)
        # No Ocultar encabezado vertical
        self.tbl_stock.verticalHeader().setVisible(True)
        # Dibujar el fondo usando colores alternados
        self.tbl_stock.setAlternatingRowColors(True)
        # Deshabilitar edición
        self.tbl_stock.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # Deshabilitar el comportamiento de arrastrar y soltar
        self.tbl_stock.setDragDropOverwriteMode(False)
        # Seleccionar toda la fila
        self.tbl_stock.setSelectionBehavior(QAbstractItemView.SelectRows)
        # Seleccionar una fila a la vez
        self.tbl_stock.setSelectionMode(QAbstractItemView.SingleSelection)
        self.layout_principal.addWidget(self.tbl_stock, 0,1,2,5)

        self.et_codigo = QLabel("Introducir lectura de código QR", self)
        self.layout_principal.addWidget(self.et_codigo, 2,1,1,1)

        self.edt_codigo = QLineEdit(self)
        # self.edt_codigo.setMaximumSize(350,80)
        self.edt_codigo.setAlignment(Qt.AlignLeft)
        self.layout_principal.addWidget(self.edt_codigo, 3,1,1,1)

        self.et_curso = QLabel("Curso solicitante", self)
        self.layout_principal.addWidget(self.et_curso, 2,2,1,1)

        self.edt_curso = QLineEdit(self)
        self.edt_curso.setMaximumWidth(150)
        self.edt_curso.setAlignment(Qt.AlignLeft)
        self.layout_principal.addWidget(self.edt_curso, 3,2,1,1)

        self.et_cantidad = QLabel("Cantidad", self)
        self.layout_principal.addWidget(self.et_cantidad, 2,3,1,1)

        self.edt_cantidad = QLineEdit(self)
        self.edt_cantidad.setMaximumWidth(150)
        self.edt_cantidad.setAlignment(Qt.AlignLeft)
        self.layout_principal.addWidget(self.edt_cantidad, 3,3,1,1)

        self.rbtn_enviar = QRadioButton("Activar/Desactivar envio automático", self)
        self.layout_principal.addWidget(self.rbtn_enviar, 2,4,1,2)

        self.btn_enviar = QPushButton("Solicitar", self)
        self.layout_principal.addWidget(self.btn_enviar, 3,4,1,2)

        self.query_log = QListWidget(self)
        self.layout_principal.addWidget(self.query_log, 4,1,4,5)
        self.query_log.setMinimumSize(350,300)
        self.query_log.setMaximumHeight(900)


        # self.btn_query = QPushButton("Base de Datos", self)
        # self.layout_principal.addWidget(self.btn_query, 4,5,1,1)

        # self.btn_salir = QPushButton("Salir", self)
        # self.layout_principal.addWidget(self.btn_salir, 5,5,1,1)
        self.btn_query = QPushButton("Base de Datos", self)
        self.layout_principal.addWidget(self.btn_query, 6,0,1,1)

        self.btn_salir = QPushButton("Salir", self)
        self.layout_principal.addWidget(self.btn_salir, 7,0,1,1)

        #### Consulta a la base de datos para armado de tabla
        self.consulta_db()

    def consulta_db(self):
        self.db_etec = ETEC_db()
        # self.tbl_stock.clearContents()                  #Borra el contenido de la tabla
        # self.tbl_stock.setRowCount(0)                   #Reseteo el contador de filas para que no me agregue mas filas

        try:
            llenarColumnaSql = 'SELECT name_item FROM qr_items'
            self.db_etec.cursor.execute(llenarColumnaSql)
            columnas_sql = self.db_etec.cursor.fetchall()
            columnas = []
            for nombre_item in columnas_sql:
                s1 = str(nombre_item).replace("(", "")
                s2 = str(s1).replace(")", "")
                s3 = str(s2).replace(",", "")
                s4 = str(s3).replace("'", "")

                if s4 in columnas:
                    pass
                else:
                    columnas.append(s4)
            print(columnas)
            self.tbl_stock.setColumnCount(len(columnas))
            self.tbl_stock.setHorizontalHeaderLabels(columnas)
        except:
            print("Apareció un error en el llenado de columnas")

        try:
            for row in range(0,4):
                item = 0
                if row == 0:
                    for items in columnas:
                        # print(items)
                        sql = 'select cantidad from qr_items where name_item = "{}"'.format(items)
                        self.db_etec.cursor.execute(sql)
                        get_sql = self.db_etec.cursor.fetchall()
                        #print(get_sql)
                        cantidad = 0
                        for query in get_sql:
                            if str(query[0]) == "1":
                                cantidad = cantidad + 1
                            else:
                                cantidades = QTableWidgetItem(str(query[0]))
                        if cantidad > 2:
                            dis_item = QTableWidgetItem(str(cantidad))
                        else:
                            dis_item = cantidades
                        self.tbl_stock.setItem(row, item, dis_item)
                        item = item + 1
                else:
                    for items in columnas:
                        no_disp_item = QTableWidgetItem(str(0))
                        # reserv_item = QTableWidgetItem(str(0))
                        self.tbl_stock.setItem(row, item, no_disp_item)
                        # self.tbl_stock.setItem(row, item, reserv_item)
                        item = item + 1
        except UnboundLocalError as error:
            print("Hubo problemas al cargar tabla de stock.")
            print("Revisar exepción:", error)


        # for query in get_sql:
        #     self.tabla.insertRow(row)
        #     medio_modulo = QTableWidgetItem(str(query[0]))
        #     lunes = QTableWidgetItem(str(query[1]))
        #     martes = QTableWidgetItem(str(query[2]))
        #     miercoles = QTableWidgetItem(str(query[3]))
        #     jueves = QTableWidgetItem(str(query[4]))
        #     viernes = QTableWidgetItem(str(query[5]))
        #     horas = QTableWidgetItem(str(query[6]))
        #     reservas = QTableWidgetItem(str(query[7]))

        #     self.tabla.setItem(row, 0, medio_modulo)
        #     self.tabla.setItem(row, 1, lunes)
        #     self.tabla.setItem(row, 2, martes)
        #     self.tabla.setItem(row, 3, miercoles)
        #     self.tabla.setItem(row, 4, jueves)
        #     self.tabla.setItem(row, 5, viernes)
        #     self.tabla.setItem(row, 6, horas)
        #     self.tabla.setItem(row, 7, reservas)
        #     row = row + 1



class mainWindow(QMainWindow):
    def __init__(self):
        super(mainWindow, self).__init__()
        icono = "imagenes/logo_etec2.png"
        self.setWindowIcon(QIcon(icono))
        self.estado_autoenvio = False
        self.db_etec = ETEC_db()
        self.codigos = []

        #### Definición
        self.widgets_aplicaciones = QStackedWidget()
        # Creo los objetos correspondientes a cada ventana
        self.ventana_ingresar = loginUsuario()                      # ventana para ingresar con cuenta
        self.ventana_registrar = Registro()                  # ventana para registrar cuenta de acceso
        self.ventana_db_etec = cursos_db()           # ventana para acceder a la base de datos graficamente
        self.ventana_principal = principal()                # ventana principal para la visualización de datos
        # self.reservas = pedidos()                    # ventana para visualizar y gestionar pedidos de reservas

        self.widgets_aplicaciones.addWidget(loginUsuario())                  # Agrego el objeto ventana ingresar
        self.widgets_aplicaciones.addWidget(Registro())                 # Agrego el objeto ventana de registro
        self.widgets_aplicaciones.addWidget(cursos_db())           # Agrego el objeto ventana a la base de datos
        self.widgets_aplicaciones.addWidget(principal())           # Agrego el objeto ventana principal

        self.setWindowTitle("Ventana Principal de Control de Items")
        self.setCentralWidget(self.ventana_ingresar)                # Seteamos cómo central widget

        # self.widgets_aplicaciones.currentWidget(loginUsuario())
        # self.widgets_aplicaciones.setCurrentIndex(0)
        #### conexiones a los eventos

        self.ventana_ingresar.btn_login.clicked.connect(self.click_log)
        # self.ventana_registrar.boton_registro.clicked.connect(self.registro)
        # self.registrar.boton_registro.clicked.conncet(self.registro)


        ############ Eventos de la ventana principal
        self.ventana_principal.btn_enviar.clicked.connect(self.enviar)
        self.ventana_principal.rbtn_enviar.clicked.connect(self.on_off_autoenvio)
        # self.ventana_principal
        self.ventana_principal.btn_salir.clicked.connect(self.salir)
        self.ventana_principal.btn_query.clicked.connect(self.ver_mod_db)

        #### modificacion de widgets
        self.ventana_db_etec.btn_volver_consulta = QPushButton("Volver", self)
        self.ventana_db_etec.btn_volver_consulta.resize(150,40)
        self.ventana_db_etec.btn_volver_consulta.clicked.connect(self.volver)
        self.ventana_db_etec.layout.addWidget(self.ventana_db_etec.btn_volver_consulta, 8,2,1,1)

    def volver(self):
        print("Se cerrará la ventana")
        self.ventana_db_etec.close()
        print("se cerró?")

    # def des_logear(self):

    def click_log(self):
        user = self.ventana_ingresar.lned_nombre.text()
        password = self.ventana_ingresar.lend_password.text()
        if password == '':
            QMessageBox.information(self, "Contraseña vacia", "Por favor ingrese su contraseña en el campo de Contraseña.", QMessageBox.Ok, QMessageBox.Ok)
        elif user == '':
            QMessageBox.information(self, "Usuario vacio", "Por favor ingrese su nombre de usuario en el campo de Usuario.", QMessageBox.Ok, QMessageBox.Ok)
        else:
            try:
                sql = "SELECT * FROM cuentas WHERE usuario=%s AND contraseña=%s"
                self.ventana_ingresar.db_etec.cursor.execute(sql, (user, password))
                if (len(self.ventana_ingresar.db_etec.cursor.fetchall())>0):
                    QMessageBox.information(self, "Inicio de sesión exitoso", "Se inició sesión exitosamente", QMessageBox.Ok, QMessageBox.Ok)
                    self.ventana_ingresar.log_estado = True
                    self.ventana_ingresar.close()
                    # self.setCentralWidget(self.ventana_db_etec)                # Seteamos cómo central widget
                    self.volver()

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

    def on_off_autoenvio(self, selected):
        ## Realizar lógica referente al autoenvio para marcar computadoras




        item = self.ventana_principal.edt_codigo.text()

        if self.ventana_principal.rbtn_enviar.isChecked():
            self.ventana_principal.btn_enviar.setText("Finalizar")
            codigo = self.ventana_principal.edt_codigo.text()
            self.ventana_principal.edt_codigo.clear()
            self.codigos.append(codigo)
            self.ventana_principal.edt_codigo.returnPressed.connect(self.datos_autoenvio)
            # self.ventana_principal.edt_codigo.editingFinished.connect(self.datos_autoenvio)
        else:
            self.ventana_principal.btn_enviar.setText("Solicitar")
            print(self.codigos)
        try:
            index = item.find()
            print(index)
            if index == 17:
                print("se encontró indice.")
            else:
                print("Codigo incorrecto o vacío.")

        except TypeError as error:
            print("Hubo un error: {}".format(error))

    def datos_autoenvio(self):
        self.db_etec = ETEC_db()
        codigo = self.ventana_principal.edt_codigo.text()
        self.ventana_principal.edt_codigo.clear()
        self.codigos.append(codigo)
        hora_actual = datetime.datetime.now()
        # alternativa
        # hora_actual = datetime.datetime.now().time()

        hora_formateada = hora_actual.strftime('%H:%M')
        dia = hora_actual.strftime('%d')
        cantidad = self.ventana_principal.edt_cantidad.text()
        curso = self.ventana_principal.edt_curso.text().lower()
        print(curso)
        print(codigo)
        print(hora_formateada)
        if curso == "":
            self.ventana_principal.query_log.addItem("Ingresar curso!")
        else:
            self.ventana_principal.query_log.addItem("Se agregó el ítem {} a la hora {}, correspondiente al curso {}",format(codigo,hora_formateada,curso))
        self.ventana_principal.query_log.scrollToBottom()


    def enviar(self):
        item = self.ventana_principal.edt_codigo.text()
        cantidad = self.ventana_principal.edt_cantidad.text()
        curso = self.ventana_principal.edt_curso.text().lower()
        hora_actual = datetime.datetime.now()
        # alternativa
        # hora_actual = datetime.datetime.now().time()

        hora_formateada = hora_actual.strftime('%H:%M')
        hora = int(hora_actual.strftime('%H'))
        minutos = int(hora_actual.strftime('%M'))
        dia = hora_actual.strftime('%A')
        print(dia)

        try:
            print(item)
            print(cantidad)
            cursos = ["1a", "1b", "2a", "2b", "3e", "3i", "4e", "4i", "5e", "5i", "6e", "6i"]
            if curso in cursos:
                try:
                    if (item.find("'") == 2):
                        separador = "'"
                    elif  (item.find("{") == 2):
                        separador = "{"
                    else:
                        separador = "False"
                        print("Error inesperado, no se encontró separador en el código.")

                    if (separador == "'") or (separador == "{"):
                        if cantidad != "":
                            # sql_query = "SELECT  FROM stock WHERE qr_code={} ".format(item)
                            texto = "¿Qué deseas hacer con lo registrado?"
                            # texto = "Se han registrado los siguientes códigos referentes al curso: {} a la hora {} a cargo de {}\n\tLos códigos son:{}".format(curso, tiempo, profesor, codigos)
                            msg_box = QMessageBox(self)
                            msg_box.setWindowTitle("Definir Acción")
                            msg_box.setText(texto)
                            msg_box.setIcon(QMessageBox.Question)
                            msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
                            # msg_box.addButton(QPushButton("asdasd", self)
                            si_btn = msg_box.button(QMessageBox.Yes)
                            no_btn = msg_box.button(QMessageBox.No)
                            cl_btn = msg_box.button(QMessageBox.Cancel)

                            # Establecer el nuevo texto del botón
                            no_btn.setText("Devolver")
                            si_btn.setText("Entregar")
                            cl_btn.setText("Cancelar")

                            # Mostrar el QMessageBox modificado
                            # msg_box.exec_()
                            # 
                            # 
                            # )
                            # msg_box.setText(QMessageBox.Yes, "papas")
                            msg_box.setDefaultButton(QMessageBox.Cancel)
                            # msg_box.setIcon("\\imagenes")
                            # msg_box.addButton(self, "Definir", texto, QMessageBox.Cancel | QMessageBox.No | QMessageBox.Yes, QMessageBox.Cancel)
                            # 02'005'002'000061
                            
                            medio_modulo = int(encontra_medio_modulo(hora=hora, minutos=minutos))
                            print("print datos: [{}], [{}] y [{}]".format(dia, curso, medio_modulo))

                            sql = "SELECT {} FROM {} WHERE medio_modulo={}".format(dia, curso, medio_modulo)            
                            self.db_etec.cursor.execute(sql)
            
                            # sql = "SELECT %s FROM %s WHERE medio_modulo=%d"            
                            # self.db_etec.cursor.execute(sql, (dia, curso, medio_modulo))
                            consulta = self.db_etec.cursor.fetchall()
                            materia = str(consulta[0]).split("'")
                            print(materia[1])  # Me devuelve el nombre de la materia limpia
                            
                            # SELECT tbl_cliente.Nombre, tbl_usuario.correo, tbl_solicitud.estado
                            # FROM  tbl_solicitud
                            # INNER JOIN tbl_usuario
                            # ON tbl_usuario.idusuario = tbl_solicitud.idusuario
                            # INNER JOIN tbl_cliente
                            # ON tbl_cliente.idcliente = tbl_solicitud.idcliente
                            # WHERE tbl_solicitud.estado = 'abierto'


                            profesor = "pato"
                            curso_etec = "3e"
                            msg_box.setInformativeText("El responsable del registro en la hora {} es {} del curso {}.".format(hora_formateada, profesor, curso_etec))
                            msg_box.setDetailedText("""La lista de ítems es la siguiente: 
                            <QR-codigo>: [Descripción del ítem], cantidad: []
                            <02'006'005'000089>: Notebook Bangho, cantidad: 1
                            <02'006'016'000039>: Parlante grande, cantidad: 1
                            Fin de lista.-""")
                            msg_box.exec()

                            if (msg_box == QMessageBox.Yes):
                                print("fue un si")
                                self.ventana_principal.query_log.addItem("Fue un si")
                            elif (msg_box == QMessageBox.No):
                                print("Fue un nooooooooooo")
                                self.ventana_principal.query_log.addItem("Se ingresa")
                            else:
                                print("Se cancelo la operación")
                                self.ventana_principal.query_log.addItem("Se cancelo la operación")

                            # try:
                            #     sql = "SELECT * FROM cuentas WHERE usuario=%s AND contraseña=%s"
                            #     self.ventana_ingresar.db_etec.cursor.execute(sql, (user, password))
                            #     if (len(self.ventana_ingresar.db_etec.cursor.fetchall())>0):
                            #         QMessageBox.information(self, "Inicio de sesión exitoso", "Se inició sesión exitosamente", QMessageBox.Ok, QMessageBox.Ok)
                            #         self.ventana_ingresar.log_estado = True
                            #         self.ventana_ingresar.close()
                            #         # self.setCentralWidget(self.ventana_db_etec)                # Seteamos cómo central widget
                            #         self.volver()
                            #     else:
                            #         QMessageBox.information(self, "Error", "El nombre de usuario no existe o la contraseña no es correcta.", QMessageBox.Ok, QMessageBox.Ok)
                            # except:
                            #     QMessageBox.information(self, "Error", "Problemas técnicos al conectar con la base de datos", QMessageBox.Ok, QMessageBox.Ok)



                            if self.ventana_principal.rbtn_enviar.isChecked():
                                pass
                        else:
                            print("ingrese Cantidad")

                except TypeError as error:
                    print("A ocurrido un error: {}".format(error))

                print("curso ")
            else:
                print("Favor de introducir curso")
            pass
        except TypeError as error:
            print("A ocurrido un error: {}".format(error))
        ## Informar quien es el responsable y hora de devolución de los materiales
        ## Reajustar tabla de pedidos.

        # # # self.ventana_principal.query_log.addItem("Se entregó la cantidad de {} del ítem {} para el curso {}".format(cantidad, item, curso))
        # # # self.ventana_principal.query_log.addItem("Se realizó la modificación en la vase de datos, se procede a actualizar el ítem")
        self.ventana_principal.query_log.scrollToBottom()

    def reservas(self):
        pass

    def ver_mod_db(self):
        ## Metodo para la visualización de la ventana para la base de datos
        self.ventana_db_etec.show()

    def volver(self):
        self.setCentralWidget(self.ventana_principal)


    def salir(self):
        self.close()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = mainWindow()
    window.show()
    sys.exit(app.exec_())
