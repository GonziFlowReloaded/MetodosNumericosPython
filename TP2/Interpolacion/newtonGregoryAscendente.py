import numpy as np

def error_porcentual(valor_aproximado, valor_real):

    """
    Calcula el error porcentual entre un valor aproximado y un valor real.

    Args:
        valor_aproximado (float): Valor aproximado.
        valor_real (float): Valor real.

    Returns:
        float: Error porcentual.
    """

    return abs((valor_real - valor_aproximado) / valor_real) * 100
    

def gregory_newton(x, y, target):

    """
    Implementa el método de interpolación de Newton-Gregory ascendente.

    Args:
        x (list): Lista de puntos x conocidos.
        y (list): Lista de puntos y conocidos.
        target (float): Punto en el que se desea interpolar.

    Returns:
        float: Valor interpolado en el punto objetivo.
    """

    n = len(x)
    tabla = [[0 for j in range(n)] for i in range(n)]

    # Inicializar primera columna de la tabla con los valores de y
    for i in range(n):
        tabla[i][0] = y[i]

    # Calcular los coeficientes interpolantes restantes en la tabla
    for j in range(1, n):
        for i in range(n - j):
            tabla[i][j] = (tabla[i + 1][j - 1] - tabla[i][j - 1]) / (x[i + j] - x[i])

    resultado = tabla[0][0]

    # Calcular el resultado interpolado
    for j in range(1, n):
        producto = 1
        for i in range(j):
            producto *= (target - x[i])
        resultado += tabla[0][j] * producto


    return resultado
