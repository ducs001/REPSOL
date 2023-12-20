from PyQt5 import QtWidgets, uic
 
from Vista.ventanaBoleta import VentanaBoleta
from Vista.ventanaFactura import VentanaFactura

class VentanaFacturacion(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(VentanaFacturacion, self).__init__(parent)
        uic.loadUi("UI/VentanaFacturacion.ui", self)

        self.btnBoleta.clicked.connect(self.abrirVentanaBoleta)
        self.btnFactura.clicked.connect(self.abrirVentanaFactura)

        self.show()