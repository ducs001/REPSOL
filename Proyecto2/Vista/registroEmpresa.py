from PyQt5 import QtWidgets, uic


class RegistroEmpresa(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(RegistroEmpresa, self).__init__(parent)
        uic.loadUi("UI/RegistroEmpresa.ui", self)