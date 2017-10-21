import matplotlib.pyplot as plt; plt.rcdefaults()
import matplotlib.pyplot as plt
import numpy as np
from time import time as t
##import json


strings = []
data = { "tipo": 1, "Cantidad":4, "Ingredientes":4},{ "tipo": 2, "Cantidad":10, "Ingredientes":10},{ "tipo": 3, "Cantidad":8, "Ingredientes":3},{ "tipo": 4, "Cantidad":7, "Ingredientes":7},{ "tipo": 5, "Cantidad":12, "Ingredientes":11}
Asada = 0
Adobada = 0
Suadero = 0
Cabeza = 0
Lengua = 0
Cebolla = 100
Cilantro = 100
Salsa = 100
Guacamole = 100
#(1:C,2:CCi,3:CCiS,4:CCiSG,5:CS,6:CG,7:Ci,8:CiS,9:CiG,10:CiSG,11:S,12:SG,13:G,14:CSG,15:CCiG,16:Nada)
# C=Cebolla, Ci=Cilantro, S=Salsa, G=Guacamole

ingredientes = {"Cebolla": 0 ,"Cilantro": 0,"Salsa":0,"Guacamole":0}

for orden in data:
    if((orden["tipo"]) == 1):
        start = t()
        Asada += (orden["Cantidad"])
        end = t()
        TiempoAsada = (end - start)
        print(TiempoAsada)
    if((orden["tipo"]) == 2):
        start1 = t()
        Adobada += (orden["Cantidad"])
        end1 = t()
        TiempoAdobada = (end1 - start1)
        print(TiempoAdobada)
    if((orden["tipo"]) == 3):
        start2 = t()
        Suadero += (orden["Cantidad"])
        end2 = t()
        TiempoSuadero = (end2 - start2)
        print(TiempoSuadero)
    if((orden["tipo"]) == 4):
        start3 = t()
        Cabeza += (orden["Cantidad"])
        end3 = t()
        TiempoCabeza = (end3 - start3)
        print(TiempoCabeza)
    if((orden["tipo"]) == 5):
        start4 = t()
        Lengua += (orden["Cantidad"])
        end4 = t()
        TiempoLengua = (end4 -start4)
        print(TiempoLengua)
        
    if((orden["Ingredientes"]) == 1):
        Cebolla -= (orden["Cantidad"])
    if((orden["Ingredientes"]) == 2):
        Cebolla -= (orden["Cantidad"])
        Cilantro -= (orden["Cantidad"])
    if((orden["Ingredientes"]) == 3):
        Cebolla -= (orden["Cantidad"])
        Cilantro -= (orden["Cantidad"])
        Salsa -= (orden["Cantidad"])
    if((orden["Ingredientes"]) == 4):
        Cebolla -= (orden["Cantidad"])
        Cilantro -= (orden["Cantidad"])
        Salsa -= (orden["Cantidad"])
        Guacamole -= (orden["Cantidad"])
    if((orden["Ingredientes"]) == 5):
        Cebolla -= (orden["Cantidad"])
        Salsa -= (orden["Cantidad"])
    if((orden["Ingredientes"]) == 6):
        Cebolla -= (orden["Cantidad"])
        Guacamole -= (orden["Cantidad"])
    if((orden["Ingredientes"]) == 7):
        Cilantro -= (orden["Cantidad"])
    if((orden["Ingredientes"]) == 8):
        Cilantro -= (orden["Cantidad"])
        Salsa -= (orden["Cantidad"])
    if((orden["Ingredientes"]) == 9):
        Cilantro -= (orden["Cantidad"])
        Guacamole -= (orden["Cantidad"])
    if((orden["Ingredientes"]) == 10):
        Cilantro -= (orden["Cantidad"])
        Salsa -= (orden["Cantidad"])
        Guacamole -= (orden["Cantidad"])
    if((orden["Ingredientes"]) == 11):
        Salsa -= (orden["Cantidad"])
    if((orden["Ingredientes"]) == 12):
        Salsa -= (orden["Cantidad"])
        Guacamole -= (orden["Cantidad"])
    if((orden["Ingredientes"]) == 13):
        Guacamole -= (orden["Cantidad"])
    if((orden["Ingredientes"]) == 14):
        Cebolla -= (orden["Cantidad"])
        Salsa -= (orden["Cantidad"])
        Guacamole -= (orden["Cantidad"])
    if((orden["Ingredientes"]) == 15):
        Cebolla -= (orden["Cantidad"])
        Cilantro -= (orden["Cantidad"])
        Guacamole -= (orden["Cantidad"])
    else:
        print ("Sale uno carnivoro")
    ##if "tipo" == 1:
    ##Asada += data["Cantidad"]

ejeX = ("Asada","Adobada", "Suadero", "Cabeza", "Lengua")
y_pos = np.arange((len(ejeX)))
ejeY = [Asada,Adobada, Suadero, Cabeza, Lengua]

ejeX2 = ("Asada","Adobada", "Suadero", "Cabeza", "Lengua")
y_pos1 = np.arange((len(ejeX2)))
ejeY2 = [TiempoAsada,TiempoAdobada,TiempoSuadero,TiempoCabeza,TiempoLengua]

ejeX3 = ("Cebolla","Cilantro", "Salsa", "Guacamole")
y_pos2 = np.arange((len(ejeX3)))
ejeY3 = [Cebolla,Cilantro,Salsa,Guacamole]


f1 = plt.figure(1)
plt.bar(y_pos, ejeY, align ='center', alpha = 0.5)
plt.xticks(y_pos, ejeX)
plt.ylabel("Cantidad")
plt.title("Cantidad de Tacos")


f2 = plt.figure(2)
plt.bar(y_pos1, ejeY2, align ='center', alpha = 1)
plt.xticks(y_pos1, ejeX2)
plt.ylabel("Tiempo")
plt.title("Tiempo de Ordenes")

f3 = plt.figure(3)
plt.bar(y_pos2, ejeY3, align ='center', alpha = .5)
plt.xticks(y_pos2, ejeX3)
plt.ylabel("Ingredientes")
plt.title("Ingredientes de los tacos")
f1.show()
f2.show()
f3.show()
input()

##n = 5
##X = np.arange(n)
##y1 = (1-X/float(n)) * np.random.uniform(0.5,1.0,n)

##plt.bar(X, + y1, facecolor = '#9999ff', edgecolor = 'white')
