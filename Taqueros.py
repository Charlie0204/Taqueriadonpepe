from SQSf import *
import time
import queue
from threading import Thread,Lock

listaWrite = []
ingredientes = {"Cilantro":500, "Cebolla":500, "Salsa": 500, "Queso":500, "Guacamole":500}
tortillas1 = 500
tortillas2 = 500
tortillas3 = 500
order = SqsRead()

Q1T1 = queue.Queue()
Q2T1 = queue.Queue()
Q3T1 = queue.Queue()
ListT1 = [Q1T1,Q2T1,Q3T1]

Q1T2 = queue.Queue()
Q2T2 = queue.Queue()
Q3T2 = queue.Queue()
ListT2 = [Q1T2,Q2T2,Q3T2]

Q1T3 = queue.Queue()
Q2T3 = queue.Queue()
Q3T3 = queue.Queue()
ListT3 = [Q1T3,Q2T3,Q3T3]


def Acomodar(MainQueue):
    count1 = 1
    count2 = 1
    count3 = 1
    while True:
        actual = MainQueue.pop(0)
        if(MainQueue[0] != None):
            for suborden in actual["orden"]:
                if suborden["quantity"] < 10:
                    count1 %= 3
                    if count1 == 0:
                        Q1T1.put(suborden)
                        count1 += 1
                    elif count1 == 1:
                        Q1T2.put(suborden)
                        count1 += 1
                    elif count1 == 2:
                        Q1T3.put(suborden)
                        count1 += 1
                if 5 < suborden["quantity"] < 20:
                    count2 %= 3
                    if count2 == 0:
                        Q2T1.put(suborden)
                        count2 += 1
                    elif count2 == 1:
                        Q2T2.put(suborden)
                        count2 += 1
                    elif count2 == 2:
                        Q2T3.put(suborden)
                        count2 += 1
                if suborden["quantity"] > 30:
                    count3 %= 3
                    if count3 == 0:
                        Q3T1.put(suborden)
                        count3 += 1
                    elif count3 == 1:
                        Q3T2.put(suborden)
                        count3 += 1
                    elif count3 == 2:
                        Q3T3.put(suborden)
                        count3 += 1


def startProgram():
    threads_taquero = []

def Taquero1(Q1T1,Q2T1,Q3T1):
    while True:
        for i in range(5):
            procesaOrden(Q1T1)
            tortillas1 -= 1
        for i in range(3):
            procesaOrden(Q2T1)
            tortillas1 -= 1
        procesaOrden(Q3T1)
        tortillas1 -= 1

def Taquero2(Q1T2,Q2T2,Q3T2):
    while True:
        for i in range(5):
            procesaOrden(Q1T2)
            tortillas2 -= 1
        for i in range(3):
            procesaOrden(Q2T2)
            tortillas2 -= 1
        procesaOrden(Q3T2)
        tortillas2 -= 1

def Taquero3(Q1T3,Q2T3,Q3T3):
    while True:
        for i in range(5):
            procesaOrden(Q1T3)
            tortillas2 -= 1
        for i in range(3):
            procesaOrden(Q2T3)
            tortillas2 -= 1
        procesaOrden(Q3T3)
        tortillas2 -= 1

def procesaOrden(QT):
    actual = QT.get()
    print("Procesando orden: " + actual["process_id"])
    restaIngredientes(actual)
    time.sleep(.2)



def restaIngredientes(orderI):
    for i in orderI["ingredients"]:
        ingredientes[i] -= 1



def rellenaIngredientes():
    while True:
        time.sleep(5)
        if (ingredientes["Cilantro"] <= 150):
            ingredientes["Cilantro"] += 100
        if (ingredientes["Cebolla"] <= 150):
            ingredientes["Cebolla"] += 100
        if (ingredientes["Salsa"] <= 150):
            ingredientes["Salsa"] += 100
        if (ingredientes["Queso"] <= 150):
            ingredientes["Queso"] += 100
        if (ingredientes["Guacamole"] <= 150):
            ingredientes["Guacamole"] += 100
