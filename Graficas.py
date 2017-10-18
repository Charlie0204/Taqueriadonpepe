import matplotlib.pyplot as plt; plt.rcdefaults()
import matplotlib.pyplot as plt
import numpy as np
from time import time as t
##import json


strings = []
data = { "tipo": 1, "Cantidad":4},{ "tipo": 2, "Cantidad":10},{ "tipo": 3, "Cantidad":8},{ "tipo": 4, "Cantidad":7},{ "tipo": 5, "Cantidad":12}
Asada = 0
Adobada = 0
Suadero = 0
Cabeza = 0
Lengua = 0


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
    ##if "tipo" == 1:
    ##Asada += data["Cantidad"]

ejeX = ("Asada","Adobada", "Suadero", "Cabeza", "Lengua")
y_pos = np.arange((len(ejeX)))
ejeY = [Asada,Adobada, Suadero, Cabeza, Lengua]

ejeX2 = ("Asada","Adobada", "Suadero", "Cabeza", "Lengua")
y_pos1 = np.arange((len(ejeX2)))
ejeY2 = [TiempoAsada,TiempoAdobada,TiempoSuadero,TiempoCabeza,TiempoLengua]


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
f1.show()
f2.show()
input()

##n = 5
##X = np.arange(n)
##y1 = (1-X/float(n)) * np.random.uniform(0.5,1.0,n)

##plt.bar(X, + y1, facecolor = '#9999ff', edgecolor = 'white')


