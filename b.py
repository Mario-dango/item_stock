import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
 
class StackedExample(QWidget):
    def __init__(self):
        super(StackedExample, self).__init__()
        #Establecer la posición inicial y el tamaño de la ventana
        self.setGeometry(300,50,10,10)
        self.setWindowTitle('Ejemplo de StackedWidget')
 
        # Crear ventana de lista, agregar entrada
        self.leftlist=QListWidget()
        self.leftlist.insertItem(0,'Información del contacto')
        self.leftlist.insertItem(1,'Informacion personal')
        self.leftlist.insertItem(2,'Nivel de Educación')
 
        # Crea tres pequeños controles
        self.stack1=QWidget()
        self.stack2=QWidget()
        self.stack3=QWidget()
 
        self.stack1UI()
        self.stack2UI()
        self.stack3UI()
 
        # Se completan tres controles secundarios en el objeto QStackedWidget
        self.stack=QStackedWidget(self)
 
        self.stack.addWidget(self.stack1)
        self.stack.addWidget(self.stack2)
        self.stack.addWidget(self.stack3)
 
        # Diseño horizontal, agregue partes al diseño
        HBox=QHBoxLayout()
        HBox.addWidget(self.leftlist)
        HBox.addWidget(self.stack)
 
        self.setLayout(HBox)
 
        self.leftlist.currentRowChanged.connect(self.display)
    def stack1UI(self):
        layout=QFormLayout()
        layout.addRow('Nombre',QLineEdit())
        layout.addRow('habla a',QLineEdit())
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
        #Establecer el índice de la pestaña visible actualmente
        self.stack.setCurrentIndex(index)
if __name__ == '__main__':
    app=QApplication(sys.argv)
    demo=StackedExample()
    demo.show()
    sys.exit(app.exec_())
