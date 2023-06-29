class Servicio:
    __nom_empr=""
    __nomb_cont=""
    __direcc=""
    __fecha=""
    __comision=int
    
    
    def __init__(self,nombre_empre,nombre_contra,direccion,fecha,comision):
        
        self.___nom_empr=nombre_empre
        self.__nomb_cont=nombre_contra
        self.__direcc=direccion
        self.__fecha=fecha
        self.__comision=comision
        
    def getNomEmp(self):
       return self.__nom_empr
   
    def getNomCont(self):
        return self.__nomb_cont

    def getDireccion(self):
        return self.__direcc
    
    def getFecha(self):
        return self.__fecha
    
    def getComision(self):
        return self.__comision
    
    def getServicio(self):
        pass
    
    def getCostoTotalServicio(self):  
        pass
    