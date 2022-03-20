from PyQt5.QtWidgets import *
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QMainWindow, QDockWidget, QApplication


class LeftDockWidget(QWidget):
    def __init__(self, parent):
        super(LeftDockWidget, self).__init__(parent=parent)
        self.setStyleSheet("QWidget{border: 1px solid #FF0000;}")  # Establecer estilo
        self.setContentsMargins(0, 0, 0, 0)
        # Crea una ventana de lista, agrega entradas
        self.leftlist = QListWidget()
        self.leftlist.insertItem(0, 'Información del contacto')
        self.leftlist.insertItem(1, 'Informacion personal')
        self.leftlist.insertItem(2, 'Nivel de Educación')
        # Diseño horizontal, agregue partes al diseño
        HBox = QHBoxLayout()
        HBox.addWidget(self.leftlist)
        self.setLayout(HBox)

    def left_list_connect(self, s):
        self.leftlist.currentRowChanged.connect(s)


class CentrolWidgetUI(QWidget):
    def __init__(self, parent):
        super(CentrolWidgetUI, self).__init__(parent=parent)
        self.setStyleSheet("QWidget{border: 1px solid #FF0000;}")  # Establecer estilo
        self.stack1 = QWidget()
        self.stack2 = QWidget()
        self.stack3 = QWidget()
        self.stack1UI()
        self.stack2UI()
        self.stack3UI()
        # Se completan tres subcontroles en el objeto QStackedWidget
        self.stack = QStackedWidget(self)
        self.set_stack(self.stack1, self.stack2, self.stack3)
        # Diseño horizontal, agregue partes al diseño
        HBox = QHBoxLayout()
        HBox.addWidget(self.stack)
        self.setLayout(HBox)


    def set_stack(self, *args):
        for stack in args:
            self.stack.addWidget(stack)


    def stack1UI(self):
        layout = QFormLayout()
        layout.addRow('Nombre', QLineEdit())
        layout.addRow('habla a', QLineEdit())
        self.stack1.setLayout(layout)

    def stack2UI(self):
        # diseño de formulario zhu, diseño subhorizontal
        layout = QFormLayout()
        sex = QHBoxLayout()
        # Agregar botones de radio en diseño horizontal
        sex.addWidget(QRadioButton('masculino'))
        sex.addWidget(QRadioButton('Hembra'))
        # Agregar controles al diseño del formulario
        layout.addRow(QLabel('género'), sex)
        layout.addRow('cumpleaños', QLineEdit())
        self.stack2.setLayout(layout)

    def stack3UI(self):
        # Disposición horizontal
        layout = QHBoxLayout()
        # Agregar controles al diseño
        layout.addWidget(QLabel('tema'))
        layout.addWidget(QCheckBox('físico'))
        layout.addWidget(QCheckBox('Número alto'))
        self.stack3.setLayout(layout)

    def display(self, index):
        # Establecer el índice de la pestaña visible actualmente
        self.stack.setCurrentIndex(index)



class StackDemo(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.docker_widget = LeftDockWidget(self) #   muelle
        self.docker_widget.setContentsMargins(0, 0, 0, 0)
        self.central_widget = CentrolWidgetUI(self) #   widget
        self.docker_widget.left_list_connect(self.central_widget.display)
        self.dock = QDockWidget('Dock', self)
        self.dock.setWidget(self.docker_widget)
        self.addDockWidget(Qt.LeftDockWidgetArea, self.dock)
        self.setCentralWidget(self.central_widget)
        self.resize(600, 400)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = StackDemo()
    demo.show()
    sys.exit(app.exec_())
