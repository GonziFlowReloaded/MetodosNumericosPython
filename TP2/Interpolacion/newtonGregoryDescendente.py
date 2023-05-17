import math
def error_porcentual(valor_aproximado, valor_real):
    return abs((valor_real - valor_aproximado) / valor_real) * 100
    


def newton_descendente(x, y, x0):
    n = len(x)
    # Calculamos las diferencias divididas descendentes
    delta = [[0] * (n-i) for i in range(n)]
    delta[0] = y
    for i in range(1, n):
        for j in range(n-i):
            delta[i][j] = (delta[i-1][j+1] - delta[i-1][j]) / (x[j+i] - x[j])
    # Calculamos el polinomio interpolador
    p = delta[0][0]
    prod = 1
    for i in range(1, n):
        prod *= (x0 - x[n-i-1])
        p += delta[i][0] * prod
    return p

# Ejemplo de uso
x = []
y = []
arr = [[0, 1.0], [0.2, 0.9800665778412416], [0.4, 0.9210609940028851], [0.6000000000000001, 0.8253356149096782], [0.8, 0.6967067093471654], [1.0, 0.5403023058681398]]

f = lambda x: math.cos(x)

for i in range(len(arr)):
    x.append(arr[i][0])
    y.append(arr[i][1])


valores = [0.1,0.5,0.9]
print('Newton gregory descendente')
print("Función: cos(x)")
for valor in valores:
    p = newton_descendente(x, y, valor)
    print("El valor interpolado en x =", valor, "es:", p)
    print("El error porcentual es:", error_porcentual(p, f(valor)), "%")

