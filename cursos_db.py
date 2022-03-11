from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
import sys
# from ETEC_cueva import Database

class cursos_db(QWidget):
    def __init__(self):
        super(cursos_db, self).__init__()
        self.initialize()

    def initialize(self):
        self.setGeometry(100,100,800,400)
        self.setWindowTitle("Cursos en Base de Datos")
        self.display_widgets()

    def display_widgets(self):
        new_user_img = "imagenes/logo_etec2.png"
        try:
            with open(new_user_img):
                etiqueta_imagen = QLabel(self)
                pixmap = QPixmap(new_user_img)
                etiqueta_imagen.setPixmap(pixmap)
                etiqueta_imagen.move(150,80)
                etiqueta_imagen.resize(90,90)

        except FileNotFoundError:
            print("Error al intentar encontrar imagen.")

        etiqueta_login = QLabel("Horarios y Materias", self)
        etiqueta_login.move(0,20)
        etiqueta_login.setFont(QFont("Arial",20))
        etiqueta_login.resize(400,40)
        etiqueta_login.setAlignment(Qt.AlignCenter)
        
        # Apartado para crear eriquetas de nombre de usuario y nombre completo
        self.et_curos = QLabel("Curso", self)
        self.et_curos.move(30,180)

        self.edt_curso = QLineEdit("Ej: 5i, 1a, 2b, 6e",self)
        self.edt_curso.move(100,180)
        self.edt_curso.resize(200,20)

        self.et_mmodulo = QLabel("Medio módulo", self)
        self.et_mmodulo.move(30,210)

        self.edt_mmodulo = QLineEdit("Ej: 2 (Sería de 8:25 a 9:05)",self)
        self.edt_mmodulo.move(100,210)
        self.edt_mmodulo.resize(200,20)

        self.et_materia = QLabel("Materia", self)
        self.et_materia.move(30,240)

        self.edt_materia = QLineEdit("Ej: EIP (Electrónica Industrial y de Potencia)",self)
        self.edt_materia.move(100,240)
        self.edt_materia.resize(200,20)
        

        self.et_profesor = QLabel("Profesor", self)
        self.et_profesor.move(30,270)

        self.edt_profesor = QLineEdit("Ej: Mario Papetti",self)
        self.edt_profesor.move(100,270)
        self.edt_profesor.resize(200,20)

        #Crear boton de registro
        self.boton_registro = QPushButton("Insertar", self)
        self.boton_registro.resize(150,40)
        self.boton_registro.move(20,310)
        #crear señal de boton
        self.boton_registro.clicked.connect(self.insertar)
        #Crear boton de registro
        self.boton_registro = QPushButton("Consultar", self)
        self.boton_registro.resize(150,40)
        self.boton_registro.move(200,310)
        #crear señal de boton
        self.boton_registro.clicked.connect(self.consultar)

        ###############################################
        #Conexión a la base de datos de la cuevacha
        self.db_etec = QSqlDatabase.addDatabase('QMYSQL')
        self.db_etec.setHostName("localhost")
        self.db_etec.setDatabaseName("ETEC_lab")
        self.db_etec.setUserName("root")
        self.db_etec.setPassword("etec")

    def insertar(self):
        txt_materia = self.edt_materia.text()
        txt_mmodulo = self.edt_mmodulo.text()
        txt_profesor = self.edt_profesor.text()
        txt_curso = self.edt_curso.text()

        # if texto_password != password_confirmar:            
        #     estado = self.db_etec.open() 
        #     if estado == False:
        #         QMessageBox.warning(self, "Error", self.db_etec.lastError().text(), QMessageBox.Discard)
        #     else:
        #         nombre = self.entrada_nombre.text()
        #         passw = self.entrada_contraseña.text()
        #         sql = "INSERT INTO usuarios(nombre, contraseña) VALUES (:nombre, :contraseña)"
        #         consulta = QSqlQuery()
        #         consulta.prepare(sql)
        #         consulta.bindValue(":nombre", nombre)
        #         consulta.bindValue(":contraseña", passw)
        #         estado = consulta.exec_()
        #         if estado == True:
        #             QMessageBox.information(self, "Correcto", "Datos guardados", QMessageBox.Discard)
        #         else:
        #             QMessageBox.warning(self, "Error", self.db_etec.lastError().text(), QMessageBox.Discard)
                    
        #         self.db_etec.close()

        # else:
        #     QMessageBox.warning(self, "Mensaje de error", "Las contraseñas ingresadas no coinciden, por favor vuelva a intentarlo", QMessageBox.Ok, QMessageBox.Ok)


            # with open("usuario.txt", "a+") as f:
            #     f.write(self.entrada_nombre.text() + " ")
            #     f.write(texto_password + "\n")
            #     f.close()
            # self.close()
    def consultar(self):
        txt_materia = self.edt_materia.text()
        txt_mmodulo = self.edt_mmodulo.text()
        txt_profesor = self.edt_profesor.text()
        txt_curso = self.edt_curso.text()
        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = cursos_db()
    window.show()
    sys.exit(app.exec_())
