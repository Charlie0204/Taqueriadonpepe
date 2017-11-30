import matplotlib.pyplot as plt; plt.rcdefaults()
import matplotlib.pyplot as plt
import numpy as np
from json import *
from Taqueros import *


def graficaIngredientes ():
    Keys = []
    labels = ("Cilantro", "Cebolla", "Salsa", "Guacamole", "Frijoles")
    for i in ingredientes:
        Key = ingredientes.get(i)
        Keys.append(Key)
    sizes = Keys
    
    fig1,ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90) 
    ax1.axis('equal')
    plt.show()
    

graficaIngredientes ()

def graficas ():
    TiempoAsada = 0
    TiempoAdobada = 0
    TiempoDemas = 0
    TiempoTaco = 0
    TiempoMulita = 0
    TiempoQuesadilla = 0
    TiempoOtros = 0
    CantidadAs = 0
    CantidadAd = 0
    CanridadDe = 0
    CantidadTa = 0
    CantidadMu = 0
    CantidadQue = 0
    CantidadOt = 0
    for i in order:
##        if not suborden["meat"] == 'Asada' and if not suborden["meat"] == 'Adobada'
##            TiempoDemas += ((orden["finProcesa"] - orden["inicioProcesa"]).total_seconds())
##            CantidadDe += orden["quantity"]
        if suborden["meat"] == 'Asada':
            TiempoAsada += ((orden["finProcesa"] - orden["inicioProcesa"]).total_seconds())
            CantidadAs += orden["quantity"]
        if suborden["meat"] == 'Adobada':
            TiempoAdobada.append(orden["finProcesa"] - orden["inicioProcesa"])
##        if not suborden ["type"] == 'Taco' if not suborden ["type"] == 'Mulita' and if not suborden ["type"] == 'Quesadilla'
##            TiempoOtros += ((orden["finProcesa"] - orden["inicioProcesa"]).total_seconds())
##            CantidadOt += orden["quantity"]
##        if suborden ["type"] == 'Taco'
##            TiempoTaco += ((orden["finProcesa"] - orden["inicioProcesa"]).total_seconds())
##            CantidadTa += orden["quantity"]
##        if suborden ["type"] == 'Mulita'
##            TiempoMulita += ((orden["finProcesa"] - orden["inicioProcesa"]).total_seconds())
##            CantidadMu += orden["quantity"]
##        if suborden ["type"] == 'Quesadilla'
##            TiempoQuesadilla += ((orden["finProcesa"] - orden["inicioProcesa"]).total_seconds())
##            CantidadQue += orden["quantity"]

    PromAsada = TiempoAsada/CantidadAs
    PromAdobada = TiempoAdobada/CantidadAd
    PromDemas = TiempoDemas/CantidadDe
    PromTacos = TiempoTaco/CantidadTa
    PromMulitas = TiempoMulita/CantidadMu
    PromQuesadilla = TiempoQuesadilla/CantidadQue
    
    ejeX2 = ("Tiempo Asada")
    ejeY2 = TiempoAsada

    f2 = plt.figure(2)
    plt.bar(y_pos, ejeY2, align ='center', alpha = 0.5)
    plt.xticks(y_pos, ejeX2)
    plt.ylabel("Segundos")
    plt.title("Tiempo de tipo de carne")
    plt.show()

#graficas()
##            
##fig = plt.figure()
##fig.subplots_adjust(hspace=0.4, wspace=0.4)
##for i in range(1, 6):
##    fig.add_subplot(2, 3, i)
##plt.show()
     
