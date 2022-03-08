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

    def display_img