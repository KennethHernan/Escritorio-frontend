from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import * 
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
import Home, Login

class registerApp(QMainWindow):
    def __init__(self, parent=None, *args):
        super(registerApp, self).__init__(parent=parent)

        # Configuración de la Ventana
        self.setFixedSize(800, 500)  #Establece el tamaño de la ventana
        self.setWindowTitle("Title")
        label = QLabel("Registrarse", self)
        label.setAlignment(Qt.AlignHCenter)     # AlignCenter, AlignRight, AlignHeight, AlignHCenter, AlignVCenter, |
        self.setCentralWidget(label)           #Expandir el label al tamaño de la ventana

        # Entrada de Datos
        self.card_input = QLineEdit(self)
        self.card_input.setPlaceholderText("Ingrese su Card")
        self.card_input.setClearButtonEnabled(True)
        self.card_input.setGeometry(280, 150, 250, 40)
        self.card_input.setMaxLength(9)

        self.fullname_input = QLineEdit(self)
        self.fullname_input.setPlaceholderText("Ingrese sus Nombres ")
        self.fullname_input.setClearButtonEnabled(True)
        self.fullname_input.setGeometry(280, 200, 250, 40)
        self.fullname_input.setMaxLength(25)

        self.dni_input = QLineEdit(self)
        self.dni_input.setPlaceholderText("Ingrese su DNI")
        self.dni_input.setClearButtonEnabled(True)
        self.dni_input.setGeometry(280, 250, 250, 40)
        self.dni_input.setMaxLength(8)

        self.email_input = QLineEdit(self)
        self.email_input.setPlaceholderText("Ingrese su Email")
        self.email_input.setClearButtonEnabled(True)
        self.email_input.setGeometry(280, 300, 250, 40)
        self.email_input.setMaxLength(30)

        self.password_input = QLineEdit(self)
        self.password_input.setPlaceholderText("Ingrese su Contraseña")
        self.password_input.setClearButtonEnabled(True)
        self.password_input.setGeometry(280, 350, 250, 40)
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setMaxLength(6)


        # Botones
        self.btnLogin = QPushButton("Registrar", self)
        self.btnLogin.setGeometry(280, 410, 250, 40)
        
        self.btnPerfil= QPushButton("Foto",self) 
        self.btnPerfil.setWindowIcon(QIcon("../img/Perfil.png"))#No funka la fotito
        self.btnPerfil.setStyleSheet("border-radius: 50%;"
                                     "background-color: #C0A0A0;"
                                     "font-weight: bold; "
                                     "border: red;")
        self.btnPerfil.setGeometry(340, 30, 105, 105)

        # Señales
        self.btnLogin.clicked.connect(lambda: self.slotLogin("Ingresando a Login"))
        self.btnPerfil.clicked.connect(lambda x: self.slotFoto("Ingresando a la IA"))

        # Label Home
        self.label = QLabel("Has click aquí para ir al Inicio",self)
        self.label.setGeometry(310, 460, 170, 40)
        self.label.mousePressEvent = self.slotHome


    # Slot
    def slotLogin(self, mensaje):
        contCard = self.card_input.text()
        contFullname = self.fullname_input.text()
        conDni = self.dni_input.text()
        contEmail = self.email_input.text()
        contPassword = self.password_input.text()
        card =len(contCard)
        fullname = len(contFullname)
        dni = len(conDni)
        email = len(contEmail)
        password = len(contPassword)
        if (card != 0 and fullname != 0 and dni != 0 and email != 0 and password != 0 ):
            print(self.card_input.text())
            print(self.fullname_input.text())
            print(self.dni_input.text())
            print(self.email_input.text())
            print(self.password_input.text())
            self.hide()
            self.gen = Home.homeApp()
            self.gen.show()
        else:
            QMessageBox.warning(self, "Error", f"Campos vacios", QMessageBox.Ok, QMessageBox.Ok)

    def slotFoto(self, mensaje):
        print(mensaje)

    def slotHome(self, event):
        self.hide()
        self.gen = Home.homeApp()
        self.gen.show()
        print("Ingresando a Home")
