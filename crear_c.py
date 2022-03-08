from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic
import sys

class Registro(QWidget):
    def __init__(self):
        super(Registro, self).__init__()
        self.initialize()

    def initialize(self):
        self.setGeometry(100,100,400,400)
        self.setWindowTitle("Registro de Usuario")
        self.display_widgets()

    def display_widgets(self):
        new_user_img = "imagenes/logo_etec2.png"
        try:
            with open(new_user_img):
                etiqueta_imagen = QLabel(self)
                pixmap = QPixmap(new_user_img)
                etiqueta_imagen.setPixmap(pixmap)
                etiqueta_imagen.move(175,80)
                etiqueta_imagen.resize(90,90)

        except FileNotFoundError:
            print("Error al intentar encontrar imagen.")

        etiqueta_login = QLabel("Crear nueva cuenta", self)
        etiqueta_login.move(0,20)
        etiqueta_login.setFont(QFont("Arial",20))
        etiqueta_login.resize(400,40)
        etiqueta_login.setAlignment(Qt.AlignCenter)
        
        # Apartado para crear eriquetas de nombre de usuario y nombre completo
        self.etiqueta_nombre = QLabel("Nombre de usuario", self)
        self.etiqueta_nombre.move(30,180)

        self.entrada_nombre = QLineEdit(self)
        self.entrada_nombre.move(150,180)
        self.entrada_nombre.resize(200,20)

        self.etiqueta_completo = QLabel("Nombre completo", self)
        self.etiqueta_completo.move(30,210)

        self.entrada_completo = QLineEdit(self)
        self.entrada_completo.move(150,210)
        self.entrada_completo.resize(200,20)

        self.etiqueta_contraseña = QLabel("Contraseña", self)
        self.etiqueta_contraseña.move(30,240)

        self.entrada_contraseña = QLineEdit(self)
        self.entrada_contraseña.setEchoMode(QLineEdit.Password)
        self.entrada_contraseña.move(150,240)
        self.entrada_contraseña.resize(200,20)
        

        self.etiqueta_Confirmar = QLabel("Confirmar pssw", self)
        self.etiqueta_Confirmar.move(30,270)

        self.entrada_Confirmar = QLineEdit(self)
        self.entrada_Confirmar.setEchoMode(QLineEdit.Password)
        self.entrada_Confirmar.move(150,270)
        self.entrada_Confirmar.resize(200,20)

        #Crear boton de registro
        self.boton_registro = QPushButton("Registrar", self)
        self.boton_registro.resize(200,40)
        self.boton_registro.move(100,310)
        #crear señal de boton
        self.boton_registro.clicked.connect(self.registro)

    def registro(self):
        texto_password = self.entrada_contraseña.text()
        password_confirmar = self.entrada_Confirmar.text()

        if texto_password != password_confirmar:
            QMessageBox.warning(self, "Mensaje de error", "Las contraseñas ingresadas no coinciden, por favor vuelva a intentarlo", QMessageBox.Ok, QMessageBox.Ok)
        else:
            with open("usuario.txt", "a+") as f:
                f.write(self.entrada_nombre.text() + " ")
                f.write(texto_password + "\n")
                f.close()
            self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Registro()
    window.show()
    sys.exit(app.exec_())
