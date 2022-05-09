import email
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import Register, Home

class loginApp(QMainWindow):
    def __init__(self, parent=None, *args):
        super(loginApp, self).__init__(parent=parent)

        # Configuración de la Ventana
        self.setFixedSize(800, 500)  
        self.setWindowTitle("Iniciar Sesión") 
        label = QLabel("Iniciar Sesión", self)
        label.setGeometry(470, 70, 250, 40)  
        label.setStyleSheet("font-weight: bold;"
                            "font-size: 30px;")     

        # Entrada de textos
        self.dni_input = QLineEdit(self)
        self.dni_input.setPlaceholderText("Ingrese su DNI")
        self.dni_input.setClearButtonEnabled(True)
        self.dni_input.setGeometry(470, 150, 250, 40)
        self.dni_input.setMaxLength(8)

        self.password_input = QLineEdit(self)
        self.password_input.setPlaceholderText("Ingrese su contraseña")
        self.password_input.setClearButtonEnabled(True)
        self.password_input.setGeometry(470, 200, 250, 40)
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setMaxLength(6)

        # Botones
        self.btnLogin = QPushButton("Iniciar sesión", self)
        self.btnLogin.setGeometry(470, 270, 250, 40)

        # Label Register
        self.label = QLabel("Has click aquí para Registrarse",self)
        self.label.setGeometry(500, 320, 180, 40)
        self.label.mousePressEvent = self.slotRegister

        # Señales
        self.dni_input.returnPressed.connect(self.slotText)
        self.password_input.returnPressed.connect(self.slotText)
        self.btnLogin.clicked.connect(self.slotText)

        self.slotFondo()
        
    # Slot
    def slotFondo(self):     
        layout = QHBoxLayout(self)
        pixmap = QPixmap("Models/img/ucranie.jpg")
        label = QLabel(self)
        label.setPixmap(pixmap)
        label.setGeometry(0, 0, 400, 500)
        layout.addWidget(label)
        self.setLayout(layout)

    def slotText(self):
        contDni = self.dni_input.text()
        contPassword = self.password_input.text()
        email = len(contDni)
        password = len(contPassword)
        if (email != 0 and password != 0 ):
            print(self.dni_input.text())
            print(self.password_input.text())
        else:
            QMessageBox.warning(self, "Error", f"Campos vacios", QMessageBox.Ok, QMessageBox.Ok)
            
    def slotRegister(self, event):
        self.hide()
        self.gen = Register.registerApp()
        self.gen.show()
        print("Ingresando a Register")


