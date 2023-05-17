import math
from prettytable import PrettyTable

def funcion_a(x):
    return math.cos(x)

def funcion_b(x):
    return math.log(1+x)


arrA = []
arrB = []

aux = 0
for i in range(6):
    arrA.append([aux, math.cos(aux)])
    # arrB.append([aux,funcion_b(i)])
    aux += 0.2
# print("Valores de la funcion a: ")
print(arrA)
# print("Valores de la funcion b: ")
# print(arrB)

