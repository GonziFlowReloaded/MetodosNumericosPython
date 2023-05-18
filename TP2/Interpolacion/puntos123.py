from interpolacionGauss import gauss_interpolation
from newtonGregoryAscendente import gregory_newton
from newtonGregoryDescendente import newton_gregory_descendente
import numpy as np
import math
from prettytable import PrettyTable

def error_porcentual(valor_aproximado, valor_real):
    return abs((valor_real - valor_aproximado) / valor_real) * 100

def funcion_a(x):
    return math.cos(x)

def funcion_b(x):
    return math.log(1+x)

valoresX = [0, 0.2, 0.4, 0.6, 0.8, 1.0]
valoresAEvaluar = [0.1, 0.5, 0.9]
valoresYFuncionA = []
valoresYFuncionB = []

for i in range(len(valoresX)):
    valoresYFuncionA.append(funcion_a(valoresX[i]))
    valoresYFuncionB.append(funcion_b(valoresX[i]))

resultadosFuncionA = []
resultadosFuncionB = []

for valor in valoresAEvaluar:
    resultadosFuncionA.append([valor, funcion_a(valor), gauss_interpolation(valoresX, valoresYFuncionA, valor), newton_gregory_descendente(valoresX, valoresYFuncionA, valor), gregory_newton(valoresX, valoresYFuncionA, valor), str(round(error_porcentual(gauss_interpolation(valoresX, valoresYFuncionA, valor), funcion_a(valor)), 4))+"%", str(round(error_porcentual(newton_gregory_descendente(valoresX, valoresYFuncionA, valor), funcion_a(valor)), 4))+"%", str(round(error_porcentual(gregory_newton(valoresX, valoresYFuncionA, valor), funcion_a(valor)), 4))+"%"])
    resultadosFuncionB.append([valor, funcion_b(valor), gauss_interpolation(valoresX, valoresYFuncionB, valor), newton_gregory_descendente(valoresX, valoresYFuncionB, valor), gregory_newton(valoresX, valoresYFuncionB, valor), str(round(error_porcentual(gauss_interpolation(valoresX, valoresYFuncionB, valor), funcion_b(valor)), 4))+"%", str(round(error_porcentual(newton_gregory_descendente(valoresX, valoresYFuncionB, valor), funcion_b(valor)), 4))+"%", str(round(error_porcentual(gregory_newton(valoresX, valoresYFuncionB, valor), funcion_b(valor)), 4))+"%"])
    
print("Función: cos(x)")
tabla = PrettyTable()
tabla.field_names = ["Valor a evaluar", "Valor real", "Interpolación de Gauss", "GNewton Descendente", "GNewton Ascendente", "Error porcentual Gauss", "Error porcentual Descendente", "Error porcentual Ascendente"]
for i in range(len(resultadosFuncionA)):
    tabla.add_row(resultadosFuncionA[i])
print(tabla)

print("Función: ln(1+x)")
tabla = PrettyTable()
tabla.field_names = ["Valor a evaluar", "Valor real", "Interpolación de Gauss", "Newton Descendente", "Gregory Newton", "Error porcentual Gauss", "Error porcentual Newton", "Error porcentual Gregory"]
for i in range(len(resultadosFuncionB)):
    tabla.add_row(resultadosFuncionB[i])
print(tabla)
