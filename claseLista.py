from claseNodo import Nodo
from claseTransporte import Transporte

class Lista:
     __comienzo=Nodo
     __actual=Nodo
     __indice=int
     __tope=int  
     
     def __init__(self):
         self.__comienzo=None
         self.__actual=None
         self.__indice=0
         self.___tope=0
     
     def insertar(self,elemento):
         nodo = Nodo(elemento)
         nodo.setSiguiente(self.__comienzo)
         self.__comienzo=nodo
         print("\n ---------Mostrar Datos----------\n")
         print(nodo.mostrarDatos())
     
     def agregarElemento(self,elemento):
            
         aux=self.__comienzo
            
         if aux==None:
             print("\n llegaaaa")
             self.insertar(elemento)
         else:    
              while aux.getSiguiente()!=None:     
                     print("hola1")
                     aux=aux.getSiguiente()
              nodo=Nodo(elemento)
              aux.setSiguiente(nodo)
                
     def mostrarDatos(self):
         
        print("\n ----------Mostrar Datos-----------\n ")
        aux = self.__comienzo
        while aux != None:
            print(aux.mostrarDatos())
            aux = aux.getSiguiente()
                        
                
     def ServicioTransporte(self):
         
         aux=self.__comienzo
  
         while aux != None:
             
             if isinstance(aux.getDato(),Transporte):
                 
                nomb= "\n Contratante "
                costo= " Costo Total "
                print("{:^15} {:^15}".format(nomb,costo))
                
                nombre=aux.getDato().getNomCont()
                costoT=aux.getDato().getCostoTotalServicio()
                
                print("{:^15}{:^15}".format(nombre,costoT))
                aux=aux.getSiguiente()
                
             else:
                 aux=aux.getSiguiente()
                 
                 
                 
                           
             
      



             