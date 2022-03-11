from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic
import sys

class mainWindow(QWidget):
    def __init__(self):
        super(mainWindow, self).__init__()
        self.initialize()

    def initialize(self):
        self.setGeometry(100,100,800,800)
        self.setWindowTitle("Principal")
        self.display_img()

    def display_img(self):
        titulo_etec = "imagenes/Etec-fondo-blanco2.png"
        try: 
            with open(titulo_etec):
                logo_etiqueta = QLabel(self)
                pixmap1 = QPixmap(titulo_etec)
                logo_etiqueta.setPixmap(pixmap1)
                logo_etiqueta.move(180,100)
                logo_etiqueta.resize(200,90)

        except FileNotFoundError:
            print("Error al intentar encontrar la imagen")

        