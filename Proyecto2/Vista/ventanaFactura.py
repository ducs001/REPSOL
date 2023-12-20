from PyQt5 import QtWidgets, uic


class VentanaFactura(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(VentanaFactura, self).__init__(parent)
        uic.loadUi("UI/VentanaFactura.ui", self)
