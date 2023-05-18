from interpolacionGauss import gauss_interpolation


import numpy as np
import math
from prettytable import PrettyTable
from texttable import Texttable

def coeficientes_newton_ascendente(x, y):
    n = len(x)
    coef = [y]  # Almacenar los coeficientes
    
    for j in range(1, n):
        coef.append([])  # Agregar una nueva lista vacía para almacenar los coeficientes de cada nivel
        
        for i in range(n - j):
            numerador = coef[j-1][i+1] - coef[j-1][i]
            denominador = x[i+j] - x[i]
            coef[j].append(numerador / denominador)
    
    return coef


def coeficientes_newton_descendente(x, y):
    n = len(x)
    coef = [y]  # Almacenar los coeficientes
    
    for j in range(1, n):
        coef.append([])  # Agregar una nueva lista vacía para almacenar los coeficientes de cada nivel
        
        for i in range(n - j):
            numerador = coef[j-1][i] - coef[j-1][i+1]
            denominador = x[i] - x[i+j]
            coef[j].append(numerador / denominador)
    
    return coef


def evaluar_newton(x, coef, punto):
    n = len(x)
    resultado = coef[0][0]
    producto = 1
    
    for j in range(1, n):
        producto *= (punto - x[j-1])
        resultado += coef[j][0] * producto
    
    return resultado













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
    coef_descendenteA = coeficientes_newton_descendente(valoresX, valoresYFuncionA)
    coef_ascendenteA = coeficientes_newton_ascendente(valoresX, valoresYFuncionA)
    resultado_ng_descendenteFuncionA = evaluar_newton(valoresX, coef_descendenteA, valor)
    resultado_ng_ascendenteFuncionA = evaluar_newton(valoresX, coef_ascendenteA, valor)

    coef_descendenteB = coeficientes_newton_descendente(valoresX, valoresYFuncionB)
    coef_ascendenteB = coeficientes_newton_ascendente(valoresX, valoresYFuncionB)
    resultado_ng_descendenteFuncionB = evaluar_newton(valoresX, coef_descendenteB, valor)
    resultado_ng_ascendenteFuncionB = evaluar_newton(valoresX, coef_ascendenteB, valor)


    resultadosFuncionA.append([
        valor,
        funcion_a(valor),
        gauss_interpolation(valoresX, valoresYFuncionA, valor),
        resultado_ng_descendenteFuncionA,
        resultado_ng_ascendenteFuncionA,
        str(round(error_porcentual(gauss_interpolation(valoresX, valoresYFuncionA, valor), funcion_a(valor)), 4)) + "%",
        str(round(error_porcentual(resultado_ng_descendenteFuncionA, funcion_a(valor)), 4)) + "%",
        str(round(error_porcentual(resultado_ng_ascendenteFuncionA, funcion_a(valor)), 4)) + "%",
        
    ])
    
    resultadosFuncionB.append([
        valor,
        funcion_b(valor),
        gauss_interpolation(valoresX, valoresYFuncionB, valor),
        resultado_ng_descendenteFuncionB,
        resultado_ng_ascendenteFuncionB,
        str(round(error_porcentual(gauss_interpolation(valoresX, valoresYFuncionB, valor), funcion_b(valor)), 4)) + "%",
        str(round(error_porcentual(resultado_ng_descendenteFuncionB, funcion_b(valor)), 4)) + "%",
        str(round(error_porcentual(resultado_ng_ascendenteFuncionB, funcion_b(valor)), 4)) + "%",
        
    ])


print("Función: cos(x)")
tabla = PrettyTable()
tabla.field_names = ["x", "x real", "Met. Gauss", "GNewton Descendente", "GNewton Ascendente", "E%% Gauss", "E%% Descendente", "E%% Ascendente"]
for i in range(len(resultadosFuncionA)):
    tabla.add_row(resultadosFuncionA[i])
print(tabla)

print("Función: ln(1+x)")
tabla = PrettyTable()
tabla.field_names = ["x", "x real", "Met. Gauss", "GNewton Descendente", "GNewton Ascendente", "E%% Gauss", "E%% Descendente", "E%% Ascendente"]
for i in range(len(resultadosFuncionB)):
    tabla.add_row(resultadosFuncionB[i])
print(tabla)
