from PyQt5 import QtWidgets, uic


class RegistroCliente(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(RegistroCliente, self).__init__(parent)
        uic.loadUi("UI/RegistroCliente.ui", self)
        