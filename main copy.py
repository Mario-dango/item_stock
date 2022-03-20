from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic
from crear_c import Registro
from login import loginUsuario
from cursos_db import cursos_db

import sys

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
        self.widgets_aplicaciones = QStackedWidget()
        # Creo los objetos correspondientes a cada ventana
        # self.ventana_ingresar = loginUsuario()                      # ventana para ingresar con cuenta
        # self.ventana_registrar = Registro()                  # ventana para registrar cuenta de acceso
        # self.ventana_db_etec = cursos_db()           # ventana para acceder a la base de datos graficamente
        # self.ventana_principal = principal()                # ventana principal para la visualización de datos
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
            QMessageBox.information(self, "Usuario 0vacio", "Por favor ingrese su nombre de usuario en el campo de Usuario.", QMessageBox.Ok, QMessageBox.Ok)
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
