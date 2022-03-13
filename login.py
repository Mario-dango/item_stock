from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic
from programas_py.db import ETEC_db
from cursos_db import cursos_db
import sys
from crear_c import Registro

class loginUsuario(QWidget):
    def __init__(self):
        super(loginUsuario,self).__init__()
        self.setGeometry(100,100,400,400)
        self.setWindowTitle("Ingreso de Usuario")
        self.log_estado = False
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

        self.btn_login = QPushButton("Ingresar", self)
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

        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = loginUsuario()
    window.show()
    sys.exit(app.exec_())
            