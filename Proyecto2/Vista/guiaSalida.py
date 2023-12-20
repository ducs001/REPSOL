from PyQt5 import QtWidgets, uic


class GuiaSalida(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(GuiaSalida, self).__init__(parent)
        uic.loadUi("UI/GuiaSalida.ui", self)