import numpy as np

def error_porcentual(valor_aproximado, valor_real):
    return abs((valor_real - valor_aproximado) / valor_real) * 100
    

def gregory_newton(x, y, target):
    n = len(x)
    tabla = [[0 for j in range(n)] for i in range(n)]

    for i in range(n):
        tabla[i][0] = y[i]

    for j in range(1, n):
        for i in range(n - j):
            tabla[i][j] = (tabla[i + 1][j - 1] - tabla[i][j - 1]) / (x[i + j] - x[i])

    resultado = tabla[0][0]
    for j in range(1, n):
        producto = 1
        for i in range(j):
            producto *= (target - x[i])
        resultado += tabla[0][j] * producto


    return resultado


