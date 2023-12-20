from PyQt5 import QtWidgets, uic


class GuiaEntrada(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(GuiaEntrada, self).__init__(parent)
        uic.loadUi("UI/GuiaEntrada.ui", self)

