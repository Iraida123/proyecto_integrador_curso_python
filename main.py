#MENU GESTION DE PRODUCTOS\n
opcion = 0
producto = ""
lista_producto= []

while opcion != 7:
   print("Bienveido al sistema de inventario SUPERMARKET \n")
   print("1. Alta de productos nuevos")
   print("2. Mostrar lista de productos")
   print("3. Modificar la  cantidad en stock de un producto")
   print("4. Dar de baja productos")
   print("5. Listado completo de productos")
   print("6. Lista de productos con cantidad bajo minimo")
   print("7. Salir")
   opcion = int(input("Introduzca una opcion (1-7):"))
   if  opcion==1:
      print("1. Alta de productos nuevos:", ) 
      while producto != "salir":
         producto = input("ingrese nombre de producto:" ) 
         precio= float( input("ingrese precio del producto:"  ))
         stock = input("ingrese stock del producto:" )
         el_producto = {"nombre": producto,"precio": precio, "stock": stock  }
         lista_producto.append(el_producto)
         producto = input("ingrese nombre del producto o salir:" )
   elif opcion==2:             
      print("2. Mostrar lista de productos")
      



   elif opcion==3:
      print("3. Modificar la  cantidad en stock de un producto")
   elif opcion==4:
      print("4. Dar de baja productos") 
   elif opcion==5:
           print("5. Listado completo de productos")
   elif opcion==6:
      print("6. Lista de productos con cantidad bajo minimo")            
   else:
      print("Usted ha seccionado la  opcion 7. salir")

    