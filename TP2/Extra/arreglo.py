import math
from prettytable import PrettyTable

def funcion_a(x):
    return math.cos(x)

def funcion_b(x):
    return math.log(1+x)


def newton_gregory_descendente(x, y, punto_evaluar):
    n = len(x)
    matriz_diferencias = [[0] * n for _ in range(n)]
    
    # Calcula las diferencias divididas descendentes
    for i in range(n):
        matriz_diferencias[i][0] = y[i]
        
    for j in range(1, n):
        for i in range(n - j):
            matriz_diferencias[i][j] = (matriz_diferencias[i+1][j-1] - matriz_diferencias[i][j-1]) / (x[i+j] - x[i])
    
    # Realiza la interpolación polinómica descendente
    resultado_descendente = matriz_diferencias[0][0]
    prod = 1
    
    for i in range(1, n):
        prod *= (punto_evaluar - x[i-1])
        resultado_descendente += prod * matriz_diferencias[0][i]
        
    return resultado_descendente


def gregory_newton(x, y, punto_evaluar):
    n = len(x)
    matriz_diferencias = [[0] * n for _ in range(n)]
    
    # Calcula las diferencias divididas ascendentes
    for i in range(n):
        matriz_diferencias[i][0] = y[i]
        
    for j in range(1, n):
        for i in range(n - j):
            matriz_diferencias[i][j] = (matriz_diferencias[i][j-1] - matriz_diferencias[i+1][j-1]) / (x[i] - x[i+j])
    
    # Realiza la interpolación polinómica ascendente
    resultado_ascendente = matriz_diferencias[n-1][0]
    prod = 1
    
    for i in range(1, n):
        prod *= (punto_evaluar - x[n-i])
        resultado_ascendente += prod * matriz_diferencias[n-i-1][i]
        
    return resultado_ascendente

