from SQSf import *
import time
import queue


ingredientes = {"Cilantro":500, "Cebolla":500, "Salsa": 500, "Queso":500, "Guacamole":500}
order = SqsRead()

Q1T1 = queue.Queue()
Q2T1 = queue.Queue()
Q3T1 = queue.Queue()

Q1T2 = queue.Queue()
Q2T2 = queue.Queue()
Q3T2 = queue.Queue()

Q1T3 = queue.Queue()
Q2T3 = queue.Queue()
Q3T3 = queue.Queue()

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


def Taquero1(Q1T1,Q2T1,Q3T1):
    while True:
        restaIngredientes(order)


def procesaOrden(QT):
    print("Procesando orden")


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
