from PyQt5 import QtWidgets, uic


class VentanaBoleta(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(VentanaBoleta, self).__init__(parent)
        uic.loadUi("UI/VentanaBoleta.ui", self)
