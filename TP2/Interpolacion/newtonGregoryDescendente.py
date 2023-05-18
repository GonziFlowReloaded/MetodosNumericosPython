import math
import numpy as np
def error_porcentual(valor_aproximado, valor_real):
    return abs((valor_real - valor_aproximado) / valor_real) * 100
    


def newton_gregory_descendente(x, y, punto_evaluar):
    n = len(x)
    matriz_diferencias = [[0] * n for _ in range(n)]
    
    # Calcula las diferencias divididas
    for i in range(n):
        matriz_diferencias[i][0] = y[i]
        
    for j in range(1, n):
        for i in range(n - j):
            matriz_diferencias[i][j] = (matriz_diferencias[i+1][j-1] - matriz_diferencias[i][j-1]) / (x[i+j] - x[i])
    
    # Realiza la interpolación polinómica
    resultado = matriz_diferencias[0][0]
    prod = 1
    
    for i in range(1, n):
        prod *= (punto_evaluar - x[i-1])
        resultado += prod * matriz_diferencias[0][i]
        
    return resultado


