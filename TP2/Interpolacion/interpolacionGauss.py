import numpy as np
def error_porcentual(valor_aproximado, valor_real):
    return abs((valor_real - valor_aproximado) / valor_real) * 100

def gauss_interpolation(x: list, y: list, x_interpolate: float) -> float:
    
    # Determinar el tamaño de los arreglos x e y
    n = len(x)

    # Calcular los coeficientes a_i
    a = y.copy()

    for j in range(1, n):
        for i in range(n-1, j-1, -1):
            a[i] = (a[i] - a[i-1]) / (x[i] - x[i-j])

    # Calcular la función interpolada en x_interpolate
    y_interpolate = a[n-1]
    for i in range(n-2, -1, -1):
        y_interpolate = a[i] + (x_interpolate - x[i]) * y_interpolate

    return y_interpolate

f = lambda x: np.cos(x)
x = []
y = []
arreglo = [[0, 1.0], [0.2, 0.9800665778412416], [0.4, 0.9210609940028851], [0.6, 0.8253356149096782], [0.8, 0.6967067093471654], [1.0, 0.5403023058681398]]
for i in range(len(arreglo)):
    x.append(arreglo[i][0])
    y.append(arreglo[i][1])


valores = [0.1,0.5,0.9]

print('Gauss')
print("Función: cos(x)")
for valor in valores:
    p = gauss_interpolation(x, y, valor)
    print("El valor interpolado en x =", valor, "es:", p)
    print("El error porcentual es:", error_porcentual(p, f(valor)), "%")