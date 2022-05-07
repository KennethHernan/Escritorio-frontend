import email
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import Register, Home

class loginApp(QMainWindow):
    def __init__(self, parent=None, *args):
        super(loginApp, self).__init__(parent=parent)

        # Configuración de la Ventana
        self.setFixedSize(800, 500)  #Establece el tamaño de la ventana
        self.setWindowTitle("Title") 
        label = QLabel("Iniciar Sesión", self)
        label.setAlignment(Qt.AlignHCenter)     # AlignCenter, AlignRight, AlignHeight, AlignHCenter, AlignVCenter, |
        self.setCentralWidget(label)           #Expandir el label al tamaño de la ventana

        # Entrada de textos
        self.email_input = QLineEdit(self)
        self.email_input.setPlaceholderText("Ingrese su correo")
        self.email_input.setClearButtonEnabled(True)
        self.email_input.setGeometry(280, 80, 250, 40)
        self.email_input.setMaxLength(30)

        self.password_input = QLineEdit(self)
        self.password_input.setPlaceholderText("Ingrese su contraseña")
        self.password_input.setClearButtonEnabled(True)
        self.password_input.setGeometry(280, 160, 250, 40)
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setMaxLength(6)

        # Botones
        self.btnLogin = QPushButton("Ingresar", self)
        self.btnLogin.setGeometry(280, 280, 250, 40)

        # Label Register
        self.label = QLabel("Has click aquí para Registrarte",self)
        self.label.setGeometry(280, 350, 250, 40)
        self.label.mousePressEvent = self.slotRegister

        # Señales
        self.email_input.returnPressed.connect(self.slotText)
        self.password_input.returnPressed.connect(self.slotText)
        self.btnLogin.clicked.connect(self.slotText)

    # Slots
    def slotText(self):
        contEmail = self.email_input.text()
        contPassword = self.password_input.text()
        email = len(contEmail)
        password = len(contPassword)
        if (email != 0 and password != 0 ):
            print(self.email_input.text())
            print(self.password_input.text())
        else:
            QMessageBox.warning(self, "Error", f"Campos vacios", QMessageBox.Ok, QMessageBox.Ok)
            

    def slotRegister(self, event):
        self.hide()
        self.gen = Register.registerApp()
        self.gen.show()
        print("Ingresando a Register")


