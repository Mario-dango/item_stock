from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic
from programas_py.db import ETEC_db
import sys

from crear_c import Registro

class loginUsuario(QWidget):
    def __init__(self):
        super(loginUsuario,self).__init__()
        self.setGeometry(100,100,400,400)
        self.setWindowTitle("Ingreso de Usuario")
        self.login_usuario()

    def login_usuario(self):
        self.lbl_login = QLabel("Login", self)
        self.lbl_login.move(180,10)
        self.lbl_login.setFont(QFont("Arial", 20))

        self.lbl_nombre = QLabel("Usuario", self)
        self.lbl_nombre.move(30,60)

        self.lned_nombre = QLineEdit(self)
        self.lned_nombre.move(110, 60)
        self.lned_nombre.resize(220, 20)

        self.lbl_password = QLabel("Contraseña", self)
        self.lbl_password.move(30,90)

        self.lend_password = QLineEdit(self)
        self.lend_password.setEchoMode(QLineEdit.Password)
        self.lend_password.move(110,90)
        self.lend_password.resize(220,20)

        self.btn_login = QPushButton("Login", self)
        self.btn_login.move(100,140)
        self.btn_login.resize(200,40)

        self.chbox_show_p = QCheckBox("Mostrar contraseña",self)
        self.chbox_show_p.move(110,115)
        self.chbox_show_p.setChecked(False)

        self.no_usuario = QLabel("No estás registrado?", self)
        self.no_usuario.move(90,195)
        self.no_usuario.setWordWrap(True)
        self.no_usuario.setFont(QFont("Arial",7))

        self.btn_registro = QPushButton("Registrar", self)
        self.btn_registro.move(160,195)

        self.btn_registro.clicked.connect(self.registro_user)
        self.chbox_show_p.stateChanged.connect(self.mostrar_passw)
        self.btn_login.clicked.connect(self.click_log)

        
        #Establecer conexión a la base de datos MySql
        
        self.db_etec = ETEC_db()

    def click_log(self):
        usuarios = {}
        usuario = self.lned_nombre.text()
        password = self.lend_password.text()
        try:            
            sql = "SELECT * FROM cuentas"            
            self.db_etec.cursor.execute(sql)
            get_sql = self.db_etec.cursor.fetchall()

        except:
            QMessageBox.information(self, "Error", "Problemas técnicos al conectar con la base de datos", QMessageBox.Ok, QMessageBox.Ok)
            

        if (usuario, password) in usuarios.items():
            QMessageBox.information(self, "Inicio de sesión exitoso", "Se inició sesión exitosamente", QMessageBox.Ok, QMessageBox.Ok)
            self.close()
        else:
            QMessageBox.information(self, "Error", "El nombre de usuario o la contraseña son invalidos", QMessageBox.Ok, QMessageBox.Ok)

    def mostrar_passw(self, state):
        if state == Qt.Checked:
            self.lend_password.setEchoMode(QLineEdit.Normal)
        else:
            self.lend_password.setEchoMode(QLineEdit.Password)

    def registro_user(self):
        self.crear_nuevo_usr = Registro()
        self.crear_nuevo_usr.show()

    def closeEvent(self, event):
        msg_cerrar = QMessageBox.question(self, "Salir de la Aplicación", "¿Seguro que desea salir?", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if msg_cerrar == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = loginUsuario()
    window.show()
    sys.exit(app.exec_())
            