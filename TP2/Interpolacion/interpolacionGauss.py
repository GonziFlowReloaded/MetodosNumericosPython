import numpy as np
def error_porcentual(valor_aproximado, valor_real):
    # Calcular el error porcentual entre un valor aproximado y un valor real
    return abs((valor_real - valor_aproximado) / valor_real) * 100

def gauss_interpolation(x: list, y: list, x_interpolate: float) -> float:
    
    # Determinar el tamaño de los arreglos x e y
    n = len(x)

    
    # Calcular los coeficientes a_i utilizando el método de interpolación de Gauss
    a = y.copy()

    for j in range(1, n):
        for i in range(n-1, j-1, -1):
            a[i] = (a[i] - a[i-1]) / (x[i] - x[i-j])

    # Calcular la función interpolada en x_interpolate utilizando los coeficientes a_i
    y_interpolate = a[n-1]
    for i in range(n-2, -1, -1):
        y_interpolate = a[i] + (x_interpolate - x[i]) * y_interpolate

    # Devolver el valor interpolado y(x_interpolate)
    return y_interpolate

