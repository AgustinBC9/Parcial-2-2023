from claseServicio import Servicio

class Transporte(Servicio):
    __precio_hora=int
    __peso=int
    __direccion=""
    
    def __init__(self,nombre_empre,nombre_contra,direccion,fecha,comision,precio_hora,peso,dire):
        super().__init__(nombre_empre,nombre_contra,direccion,fecha,comision)
        
        self.__precio_hora=precio_hora
        self.__peso=peso
        self.__direccion=dire
             
    def __str__(self):
        return "\n Nombre Empresa: %s, Nombre del Contrante: %s, Direccion: %s, Fecha: %s, Comision: %s, Precio: %s, Peso: %s, Direccion del destino: %s" % (super().getNomEmp(),super().getNomCont(),super().getDireccion(),super().getFecha(),super().getComision(),self.__precio_hora,self.__peso,self.__direccion)       
    
    
    def getServicio(self):
        
        if self.__peso>500:
            
            importe=self.__precio_hora+0.1
            
        else:
            
            importe=self.__precio_hora
            
        return importe
    
    
    def getCostoTotalServicio(self):
         
         costoTotal=self.getComision()+self.getServicio()
         
         return costoTotal
    
    