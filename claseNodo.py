class Nodo:
    __servicio=None
    __siguiente=None
    
    def __init__(self,servicio):
        self.__servicio=servicio
        self.__siguiente=None
        
    def getSiguiente(self):
        return self.__siguiente
    
    def setSiguiente(self,siguiente):
        self.__siguiente=siguiente
        
    def getDato(self):
        return self.__servicio
        
    def mostrarDatos(self):
        return self.__servicio.__str__()