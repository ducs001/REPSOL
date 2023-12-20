from PyQt5 import QtWidgets, uic
from Vista.ventanaPrincipal import VentanaPrincipal

qtCreatorFile = "UI/Login.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class Login(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(Login, self).__init__(parent)
        uic.loadUi("UI/Login.ui", self)

        self.btnIniciar.clicked.connect(self.iniciarSesion)
        self.show()

    def iniciarSesion(self):
        usuario = self.txtUsuario.text()
        password = self.txtPassword.text()
        if usuario == "Omar" and password == "123456":
            self.close()
            vPrincipal = VentanaPrincipal(self)
            vPrincipal.show()
        else:
            mensaje = QtWidgets.QMessageBox()
            mensaje.setWindowTitle("Punto de Venta")
            mensaje.setText("Usuario y/o contraseña incorrectos")
            mensaje.setIcon(QtWidgets.QMessageBox.Critical())
            mensaje.exec_()