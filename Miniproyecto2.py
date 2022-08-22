# Mini proyecto 2 Juan Coria
from operator import mul
nom_jugadores= input("Ingrese los nombres de los jugadores: ")
lista_jugadores= nom_jugadores.upper().split(" ")

nom_jugador1= lista_jugadores[0]
nom_jugador2= lista_jugadores[1]
nom1=nom_jugador1[0:3]
nom2=nom_jugador2[0:3]

if nom1== nom2:
    nom2= nom2+"2"



#lista=[] Probando clonacion con Github agosto 2022

def puntajeDardo1():
    puntaje1=501
    puntaje2=501
    print(nom1 + " "+str(puntaje1)+"\n"+nom2+" "+str(puntaje2))
    ganador=1
    while ganador !=0:
        for i in range(3):
            
            jugada=input("Ingrese la jugada de "+nom1 +": \n")
            
            # ----------------------Entrada Primer jugador-------------------
            if i==0:
                entrada1=jugada
                if len(entrada1)>=3: #and entrada1 != "DOUBLE BULL" and entrada1 !="double bull" and entrada1 !="null" and entrada1 !="NULL" :
                    
                    
                    if entrada1 =="DOUBLE BULL" or entrada1 =="double bull":
                        entrada1=50
                    elif entrada1 =="null" or entrada1=="NULL":
                        entrada1 =0
                    elif entrada1 =="SINGLE BULL" or entrada1 =="single bull":
                        entrada1= 25
                
                    else:
                        multiplicar= jugada.split(" ")
                        for i in range(len(multiplicar)): # el largo de numero de la lista que son 3
                            multiplicar[i] = int(multiplicar[i])
                            entrada1= multiplicar[0]*multiplicar[1] 
                    print(entrada1)               
            elif i==1:
                entrada2= jugada
                if len(entrada2)>=3: #and entrada1 != "DOUBLE BULL" and entrada1 !="double bull" and entrada1 !="null" and entrada1 !="NULL" :
                
                
                    if entrada2 =="DOUBLE BULL" or entrada2 =="double bull":
                        entrada2=50
                    elif entrada2 =="null" or entrada2=="NULL":
                        entrada2 =0
                    elif entrada2 =="SINGLE BULL" or entrada2 =="single bull":
                        entrada2= 25
            
                    else:
                        multiplicar= jugada.split(" ")
                        for i in range(len(multiplicar)): # el largo de numero de la lista que son 3
                            multiplicar[i] = int(multiplicar[i])
                        entrada2= multiplicar[0]*multiplicar[1] 
                print(entrada2)
            elif i==2:
                entrada3= jugada
                if len(entrada3)>=3: #and entrada1 != "DOUBLE BULL" and entrada1 !="double bull" and entrada1 !="null" and entrada1 !="NULL" :
                    if entrada3 =="DOUBLE BULL" or entrada3 =="double bull":
                        entrada3=50
                    elif entrada3 =="null" or entrada3=="NULL":
                        entrada3 =0
                    elif entrada3 =="SINGLE BULL" or entrada3 =="single bull":
                        entrada3= 25
            
                    else:
                        multiplicar= jugada.split(" ")
                        for i in range(len(multiplicar)): # el largo de numero de la lista que son 3
                            multiplicar[i] = int(multiplicar[i])
                            entrada3= multiplicar[0]*multiplicar[1] 
                    print(entrada3)


        
        for i in range(3):
            
            jugada=input("Ingrese la jugada de "+nom2 +": \n")
            
            # ----------------------Entrada segundo jugador-------------------
            if i==0:
                entrada12=jugada
                if len(entrada12)>=3: #and entrada1 != "DOUBLE BULL" and entrada1 !="double bull" and entrada1 !="null" and entrada1 !="NULL" :
                    
                    
                    if entrada12 =="DOUBLE BULL" or entrada12 =="double bull":
                        entrada12=50
                    elif entrada12 =="null" or entrada12=="NULL":
                        entrada12 =0
                    elif entrada12 =="SINGLE BULL" or entrada12 =="single bull":
                        entrada12= 25
                
                    else:
                        multiplicar= jugada.split(" ")
                        for i in range(len(multiplicar)): # el largo de numero de la lista que son 3
                            multiplicar[i] = int(multiplicar[i])
                            entrada12= multiplicar[0]*multiplicar[1] 
                    print(entrada12)               
            elif i==1:
                entrada22= jugada
                if len(entrada22)>=3: #and entrada1 != "DOUBLE BULL" and entrada1 !="double bull" and entrada1 !="null" and entrada1 !="NULL" :
                
                
                    if entrada22 =="DOUBLE BULL" or entrada22 =="double bull":
                        entrada22=50
                    elif entrada22 =="null" or entrada22=="NULL":
                        entrada22 =0
                    elif entrada22 =="SINGLE BULL" or entrada22 =="single bull":
                        entrada22= 25
            
                    else:
                        multiplicar= jugada.split(" ")
                        for i in range(len(multiplicar)): # el largo de numero de la lista que son 3
                            multiplicar[i] = int(multiplicar[i])
                        entrada22= multiplicar[0]*multiplicar[1] 
                print(entrada22)
            elif i==2:
                entrada32= jugada
                if len(entrada32)>=3: #and entrada1 != "DOUBLE BULL" and entrada1 !="double bull" and entrada1 !="null" and entrada1 !="NULL" :
                    if entrada32 =="DOUBLE BULL" or entrada32 =="double bull":
                        entrada32=50
                    elif entrada32 =="null" or entrada32=="NULL":
                        entrada32 =0
                    elif entrada32 =="SINGLE BULL" or entrada32 =="single bull":
                        entrada32= 25
            
                    else:
                        multiplicar= jugada.split(" ")
                        for i in range(len(multiplicar)): # el largo de numero de la lista que son 3
                            multiplicar[i] = int(multiplicar[i])
                            entrada32= multiplicar[0]*multiplicar[1] 
                    print(entrada32)



            #puntaje1=puntaje1-jugada
        #global resultad_primer_jugador
        puntaje1= puntaje1-int(entrada1)-int(entrada2)-int(entrada3)
        puntaje2= puntaje2-int(entrada12)-int(entrada22)-int(entrada32)
        valor_abs1=abs(puntaje1)
        valor_abs2=abs(puntaje2)

        print(nom1+" "+str(valor_abs1)+"\n"+nom2+" "+ str(valor_abs2))

        if valor_abs1==0:
            ganador=0
            print("Gana ", nom_jugador1,"! Felicitaciones")
        elif valor_abs2==0:
            ganador=0
            print("Gana ", nom_jugador2,"! Felicitaciones")
        
            

        
        # ----------------------Fin entrada segundo jugador-------------------   


    #lista.append(jugada)

    
puntajeDardo1()



#multiplicacion=lista[2].split()
#multi1=multiplicacion[0]+multiplicacion[1]

#resultado =(lista[0]*lista[1]+lista[2])
    
#print(resultado)
#print(int(entrada1)+int(entrada2)+int(entrada3))
#print(multi1)