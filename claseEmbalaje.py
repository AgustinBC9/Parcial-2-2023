from claseServicio import Servicio

class Embalaje(Servicio):
     __precio_unidad=int
     __peso_unidad=int
     __cant=int
     
     
     def __init__(self,nombre_empre,nombre_contra,direccion,fecha,comision,precio_unidad,peso_unidad,cant):
         super().__init__(nombre_empre,nombre_contra,direccion,fecha,comision)
         
         self.__precio_unidad=precio_unidad
         self.__peso_unidad=peso_unidad
         self.__cant=cant
         
     def __str__(self):
         return "\n Nombre Empresa: %s, Nombre del Contrante: %s, Direccion: %s, Fecha: %s, Comision: %s, Precio por unidad: %s, Peso por unidad: %s, Cantidad a embalar: %s " % (super().getNomEmp(),super().getNomCont(),super().getDireccion(),super().getFecha(),super().getComision(),self.__precio_unidad,self.__peso_unidad,self.__cant)      
     
        
     def getServicio(self):
         
         if self.__peso_unidad>50:
             
             importe=self.__precio_unidad*self.__cant+0.1
             
         else:
             
             importe=self.__precio_unidad*self.__cant
             
         return importe
     
        
     def getCostoTotalServicio(self):
         
         costoTotal=self.getComision()+self.getServicio()
         
         return costoTotal
         
         