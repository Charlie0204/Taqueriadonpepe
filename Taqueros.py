from SQSf import *
import time
from time import time as t
import datetime
import queue
from threading import Thread,Lock

listaWrite = []

#INGREDIENTS STACKS
ingredientes = {"Cilantro":500, "Cebolla":500, "Salsa": 500, "Queso":500, "Guacamole":500, "Frijoles":500}

#QUEUES FOR EACH TAQUERO, Q1: SMALL ORDER QUEUE, Q2: MEDIUM ORDER QUEUE, Q3: LARGE ORDER QUEUE
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

#CALCULATES THE SIZE OF THE ORDER, AND ASIGNS TO A TAQUERO BY TURNS
def Acomodar(MainQueue):
    count1 = 1
    count2 = 1
    count3 = 1
    while True:
        if(len(MainQueue) > 0):
            actual = MainQueue.pop(0)
            for suborden in actual["orden"]:
                suborden["datetime"] = datetime.datetime.now()
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
                elif 10 < suborden["quantity"] < 20:
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
                elif suborden["quantity"] > 20:
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

#TAQUEROS: PROCESS 5 SMALL ORDERS, 3 MEDIUM ORDERS, 1 LARGE ORDER
def Taquero1(Q1T1,Q2T1,Q3T1):
    tortillas1 = 500
    while True:
        print("Taquero1")
        if Q1T1.qsize() >= 5:
            for i in range(5):
                procesaOrden(Q1T1)
                tortillas1 -= 1
        if Q2T1.qsize() >= 3:
            for i in range(3):
                procesaOrden(Q2T1)
                tortillas1 -= 1
        if Q3T1.empty() != False:
            procesaOrden(Q3T1)
            tortillas1 -= 1

def Taquero2(Q1T2,Q2T2,Q3T2):
    tortillas2 = 500
    while True:
        print("Taquero2")
        if Q1T2.qsize() >= 5:
            for i in range(5):
                procesaOrden(Q1T2)
                tortillas2 -= 1
        if Q2T2.qsize() >= 3:
            for i in range(3):
                procesaOrden(Q2T2)
                tortillas2 -= 1
        if Q3T2.empty() != False:
            procesaOrden(Q3T2)
            tortillas2 -= 1

def Taquero3(Q1T3,Q2T3,Q3T3):
    tortillas3 = 500
    while True:
        print("Taquero3")
        if Q1T3.qsize() >= 5:
            for i in range(5):
                procesaOrden(Q1T3)
                tortillas3 -= 1
        if Q2T3.qsize() >= 3:
            for i in range(3):
                procesaOrden(Q2T3)
                tortillas3 -= 1
        if Q3T3.empty() != False:
            procesaOrden(Q3T3)
            tortillas3 -= 1

#GRABS ORDER FROM QUEUE, DECREASES INGREDIENTS, WAITS FOR TACOS TO BE READY, CALCULATES PROCESS DURATION
def procesaOrden(QT):
    start = t()
    actual = QT.get()
    print("Procesando orden: " + actual["part_id"])
    restaIngredientes(actual)
    temtime = actual["quantity"] * .05
    time.sleep(temtime)
    end = t()
    tiempo = (start - end)


#BUSTRACT ONE OUT OF EACH INGREDIENT USED IN THE ORDER
def restaIngredientes(orderI):
    print("Restando ingredientes")
    for i in orderI["ingredients"]:
        ingredientes[i] -= 1

#REFILL INGREDIENTS WHEN BELOW 150
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


#START THE PROGRAM
def startProgram():
    ordenes = []
    threadTaquero1 = Thread(target=Taquero1, args=[Q1T1,Q2T1,Q3T1])
    threadTaquero1.start()
    threadTaquero2 = Thread(target=Taquero2, args=[Q1T2,Q2T2,Q3T2])
    threadTaquero2.start()
    threadTaquero3 = Thread(target=Taquero3, args=[Q1T3,Q2T3,Q3T3])
    threadTaquero3.start()
    threadAcomodar = Thread(target = Acomodar, args=[ordenes])
    threadAcomodar.start()

    while True:
        ordenes.extend(SqsRead())
        #Acomodar(ordenes)
        time.sleep(2)
        print(ingredientes)



startProgram()
