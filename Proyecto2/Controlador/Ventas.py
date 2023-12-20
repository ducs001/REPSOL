
from PyQt5 import QtWidgets, uic


class Formulario(QtWidgets.QMainWindow):
    def __int__(self, parent = None):
        super(Formulario, self).__init__(parent)
        uic.loadUi("Proyecto2/UI/VentanaVentas.ui", self)

        