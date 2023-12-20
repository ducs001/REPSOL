from Controlador.Productos import Producto

class ArregloProductos :

    def __init__(self) :
        self.dataProductos = []
    
    def adicionaProducto (self, objProd):
        self.dataProductos.append(objProd)
    
    def devolverProducto(self, pos):
        return self.dataProductos [pos]
    
    def tamanoArregloProducto(self):
        return len(self.dataProductos)
    
    def buscarProducto(self, codigo):
        for i in range(self.tamanoArregloProducto()):
            if codigo == self.dataProductos[i].getCodigo():
                return i
        return -1
   
    def eliminarProducto(self, indice):
        del(self.dataProductos[indice])