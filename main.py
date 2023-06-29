from claseLista import Lista
from claseTransporte import Transporte
from claseEmbalaje import Embalaje

if __name__=="__main__":
    
 Lista=Lista()

 op=0
 band = True
 
 while band == True:
        print("\n -------Menu de opciones-------")
        print("1- Agregar objetos de distinto tipo de servicio a la coleccion (al final de la lista). ")
        print("2- Mostrar Listado Completo. ")
        print("3- Para todos los servicios de transporte, mostrar nombre del contratante y el costo del servicio. ")
        print("4- Generar un listado con los datos de los departamentos que la agencia tiene a la venta. ")
        print("5- Salir.")
        op = int(input("Seleccione una opcion: "))

        if op == 1:
           
            print("\n 1- Sercivio Transporte --- 2- Servicio Embalaje")
            opcion=int(input("\n Ingrese el tipo de servicio: "))
            
            if opcion==1:
               nombre=input("\n Ingrese el nombre de la empresa: ")
               nombre_contr=input(" Ingrese el nombre del contratante: ")
               direc=input(" Ingrese la direccion del contratante: ")
               fecha=input(" Ingrese fecha: ")
               com=int(input(" Ingrese comision: "))
               precio=int(input(" Ingrese precio por hora del servicio: "))
               peso=int(input(" Ingrese el peso de la carga: "))
               di=input(" Ingrese direccion de destino: ")
               unTransporte=Transporte(nombre,nombre_contr,direc,fecha,com,precio,peso,di)
               Lista.agregarElemento(unTransporte)
             
            elif opcion==2:
               nombre=input("\n Ingrese el nombre de la empresa: ")
               nombre_contr=input(" Ingrese el nombre del contratante: ")
               direc=input(" Ingrese la direccion del contratante: ")
               fecha=input(" Ingrese fecha: ")
               com=int(input(" Ingrese comision: "))
               precio=int(input(" Ingrese precio por unidad a embalar: "))
               peso=int(input(" Ingrese peso de la unidad: "))
               cant=int(input(" Ingrese cantidad de unidades a emabalar: "))
               unEmbalaje=Embalaje(nombre,nombre_contr,direc,fecha,com,precio,peso,cant)
               Lista.agregarElemento(unEmbalaje)
               
        elif op==2:  
              Lista.mostrarDatos()
              
        elif op==3:
              Lista.ServicioTransporte() 
            

        '''elif self.__op == 6:
            print("-----------Menú cerrado---------")
            band = False'''
    
