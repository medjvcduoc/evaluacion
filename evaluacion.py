import csv
import funciones
pedidos=[]
opcion_correcta=False
while True:  
    print("1.registrar pedido")
    print("2.listar los pedidos")
    print("3.imprimir hoja de ruta")
    print("4.buscar un pedido por id")
    print("5.salir del programa")
    while opcion_correcta==False:
        ou=input()
        if ou>="1" and ou<="5":
            opcion_correcta=True
        else:
            print("opcion incorrecta, re seleccione") 
            opcion_correcta=False   
    if ou=="1":
        pedidos.append(funciones.registrar(pedidos))
    elif ou=="2":
        print(pedidos)
    elif ou=="3":
        with open("ruta.csv","r+")as hojaruta:
            hojaruta.write(pedidos)
    elif ou=="4":
        idabuscar=input(print("ingrese a id a buscar"))
        with open("ruta.csv","r+")as hojaruta:
            for datos in hojaruta:
                if idabuscar==hojaruta["ID"]:
                    print(hojaruta)
    elif ou=="5":
        break                


