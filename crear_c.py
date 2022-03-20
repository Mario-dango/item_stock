from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic
from programas_py.db import ETEC_db
import sys

class Registro(QDialog):
    def __init__(self, parent=None):
        super(Registro, self).__init__()

        self.parent = parent

        self.setGeometry(100,100,400,400)
        self.setWindowTitle("Registro de Usuario")
        icono = "imagenes/logo_etec2.png"
        self.setWindowIcon(QIcon(icono))
        self.registro_estado = False
        self.display_widgets()

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
        ############################### Nota mental, revisar:
                    ## que no guarde los campos vacios
                    ## que no permita el ingreso de eltras en el telefono
                    ## que detecte el @ y los dominios en el correo
                    ## que de aviso de los campos que quedaron vacios
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
            self.registro_estado = True
            self.close()

    def closeEvent(self, event):
        if (self.registro_estado == True):                  #si se ha registrado entonces cerrar ventana
            event.accept()
            self.close()
        else:                                               #si no se ha registrado pregutnar si cerrar
            msg_cerrar = QMessageBox.question(self, "Salir de la Aplicación", "¿Seguro que desea salir?", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            if msg_cerrar == QMessageBox.Yes:
                event.accept()
            else:
                event.ignore()
                
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Registro()
    window.show()
    sys.exit(app.exec_())
