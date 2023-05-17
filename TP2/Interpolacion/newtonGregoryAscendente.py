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


f = lambda x: np.cos(x)
x = []
y = []
arreglo = [[0, 1.0], [0.2, 0.9800665778412416], [0.4, 0.9210609940028851], [0.6, 0.8253356149096782], [0.8, 0.6967067093471654], [1.0, 0.5403023058681398]]
for i in range(len(arreglo)):
    x.append(arreglo[i][0])
    y.append(arreglo[i][1])



print('Función: cos(x)')
print('Resultado en x = 0.1')
resultado = gregory_newton(x, y, 0.1)
print(resultado)
print(error_porcentual(resultado, f(0.1)), '%')


print('Resultado en x = 0.5')
resultado = gregory_newton(x, y, 0.5)
print(resultado)
print(error_porcentual(resultado, f( 0.5)), '%')

print('Resultado en x = 0.9')
resultado = gregory_newton(x, y, 0.9)
print(resultado)
print(error_porcentual(resultado, f( 0.9)), '%')