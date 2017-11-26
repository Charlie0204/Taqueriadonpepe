#from SQSf import *
import time
import queue
from threading import Thread,Lock

listaWrite = []
ingredientes = {"Cilantro":500, "Cebolla":500, "Salsa": 500, "Queso":500, "Guacamole":500}
tortillas1 = 500
tortillas2 = 500
tortillas3 = 500
#order = SqsRead()

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
            tortillas3 -= 1
        for i in range(3):
            procesaOrden(Q2T3)
            tortillas3 -= 1
        procesaOrden(Q3T3)
        tortillas3 -= 1

def procesaOrden(QT):
    actual = QT.get()
    StartT = datetime.now()
    print("Procesando orden: " + actual["process_id"] + "a las: " + StartT)
    EndT = datetime.now()
    print("Orden: " + actual["process_id"] + "lista en: " + EndT)  
    restaIngredientes(actual)
    time.sleep(.2)

def restaIngredientes(orderI):
    for i in orderI["ingredients"]:
        ingredientes[i] -= 1


def rellenaIngredientes():
    while True:
        time.sleep(5)
        if (ingredientes["Cilantro"] <= 150):
            ingredientes["Cilantro"] == 500
        if (ingredientes["Cebolla"] <= 150):
            ingredientes["Cebolla"] == 500
        if (ingredientes["Salsa"] <= 150):
            ingredientes["Salsa"] == 500
        if (ingredientes["Queso"] <= 150):
            ingredientes["Queso"] == 500
        if (ingredientes["Guacamole"] <= 150):
            ingredientes["Guacamole"] == 500

def Tortillera1():
    global tortillas1
    if tortillas1 <= 150:
        time.sleep(5)
        tortillas1 += 400
        Tortillera1()
    elif tortillas1 >= 500:
        time.sleep(1)
        tortillas1 += 1
        Tortillera1()

def Tortillera2():
    global tortillas2
    if tortillas2 <= 150:
        time.sleep(5)
        tortillas2 += 400
        print(tortillas2)
        Tortillera2()
    elif tortillas2 >= 500:
        time.sleep(1)
        tortillas2 += 1
        print(tortillas2)
        Tortillera2()

def Tortillera3():
    global tortillas3
    if tortillas3 <= 150:
        time.sleep(5)
        tortillas3 += 400
        Tortillera3()
    elif tortillas3 >= 500:
        time.sleep(1)
        tortillas3 += 1
        Tortillera3()

##def ComeTortillas(): #Metodo para probar tortilleras
##        global tortillas2
##        tortillas2 -= 2
##        time.sleep(1)
##        ComeTortillas()
        
def TortillerasatWork():
    Tortilleras = []
    thread1 = Thread(target=Tortillera1)
    thread1.start()
    Tortilleras.append(thread1)
    thread2 = Thread(target=Tortillera2)
    thread2.start()
    Tortilleras.append(thread2)
    thread3 = Thread(target=Tortillera3)
    thread3.start()
    Tortilleras.append(thread3)
##    thread4 = Thread(target=ComeTortillas)
##    thread4.start()
##    Tortilleras.append(thread4)

    for  i in Tortilleras:
        i.join()
##TortillerasatWork()
