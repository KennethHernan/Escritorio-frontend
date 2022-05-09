from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import Register, Login
import sys

class homeApp(QMainWindow):
    def __init__(self, parent=None, *args):
        super(homeApp, self).__init__(parent=parent)

        # Configuración de la Ventana
        self.setFixedSize(800, 500)  #Establece el tamaño de la ventana
        self.setWindowTitle("Title")
        label = QLabel("Home", self)
        label.setAlignment(Qt.AlignHCenter)     # AlignCenter, AlignRight, AlignHeight, AlignHCenter, AlignVCenter, |
        self.setCentralWidget(label)           #Expandir el label al tamaño de la ventana


        # Botones
        self.btnLogin = QPushButton("Login", self)
        self.btnRegister= QPushButton("Registrarse", self)
        self.btnLogin.setGeometry(280, 80, 250, 40)
        self.btnRegister.setGeometry(280, 200, 250, 40)
        
        # Señales
        self.btnLogin.clicked.connect(lambda: self.slotLogin("Ingresando a Login"))
        self.btnRegister.clicked.connect(self.slotRegister)


    # Slots
    def slotLogin(self, mensaje):
        self.hide()
        self.gen = Login.loginApp()
        self.gen.show()
        print("Ingresando a Login")

    def slotRegister(self):
        self.hide()
        self.gen = Register.registerApp()
        self.gen.show()
        print("Ingresando a Register")


if __name__ == '__main__': 
    app = QApplication(sys.argv)
    window = homeApp()
    window.show()
    sys.exit(app.exec_())
