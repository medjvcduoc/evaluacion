
import random

def registrar(pedidos):
    cantidad_bidones=0
    bidones10l=0
    bidones6l=0
    bidones20l=0
    rep=True
    opco=False
    subopc=False
    vercom=False
    verdir=False
    vernocli=False
    iden=random.randint(100000,999999)
    while vernocli==False:    
        nombre=input(print("ingreese nombre de cliente"))
        vern=nombre.isalpha()
        if nombre!="" and vern==True:
            vernocli=True
        else:
            print("el nombre no puede estar vacio")
            vernocli=False    
    while verdir==False:    
        direccion=input(print("ingrese direccion"))
        if direccion!="":
            verdir=True
        else:
            print("la direccion no puede estar vacia porfavor reingrese")    
    while vercom==False:    
        sector=input(print("ingrese comuna"))
        if sector!="" and sector=="concepción" or sector=="hualpen" or sector=="chiguayante" or sector=="talcahuano" or sector=="san pedro":
            vercom=True
        else:
            print("comuna no valida, sectores validos son hualpen, concepción, talcahuano, chiguayante y san pedro")
            vercom=False    
    while rep==True:
        while opco==False:
            oc=input(print("seleccione bidon a comprar: \n1-dispensador de 6 litros \n2-despensador de 10 litros \n3-dispensador de 20 litros"))
            if oc>="1" and oc<="3":
                opco=True
            else:
                print("la opcion seleccionada es incorrecta, reingrese")
                opco=False    
            if oc=="1":
                oc2=int(input(print("cuantos dispensadores de 6 litros quiere comprar?")))
                bidones6l=bidones6l+oc2
            elif oc=="2": 
                oc3=int(input(print("cuantos dispensadores de 10 litros quiere comprar?")))
                bidones10l=bidones10l+oc3
            elif oc=="3":
                oc4=int(input(print("cuantos dispensadores de 20 litros quiere comprar?")))
                bidones20l=bidones20l+oc4
            while subopc==False: 
                decicion=input(print("desea comprar otro tipo de despensador? \n1 si \n2 no"))
                if decicion=="1" or decicion=="2":
                    subopc=True
                else:
                    print("opcion incorrecta, reingrese")
                    subopc=False    
            if decicion=="1":
                rep=True
                opco=False
                subopc=False
            elif decicion=="2":
                rep=False
    datos={"ID":iden,
           "cliente":nombre,
           "direccion":direccion,
           "comuna":sector,
           "6 litros":bidones6l,
           "10 litros":bidones10l,
           "20 litros":bidones20l
           }
    return datos