import sympy as sp
import matplotlib.pyplot as plt

import numpy as np






def funA(x):
    return np.sqrt(x+1)

def funB(x):
    return np.tan(x)

def interpolacion_parabolica_progresiva(puntos):
    x = sp.symbols('x')
    n = len(puntos)

    # Initialize the interpolation polynomial
    P = 0

    # Calculate the divided differences
    divided_diff = []
    for i in range(n):
        divided_diff.append(puntos[i][1])
    
    for i in range(1, n):
        for j in range(n - 1, i - 1, -1):
            divided_diff[j] = (divided_diff[j] - divided_diff[j - 1]) / (puntos[j][0] - puntos[j - i][0])

    # Construct the interpolation polynomial
    for i in range(n):
        term = divided_diff[i]
        for j in range(i):
            term *= (x - puntos[j][0])
        P += term

    return P

def grafica(funcion_interpolacion, puntos, fStr):
    x_vals = np.linspace(puntos[0][0], puntos[-1][0], 100)
    y_vals = [funcion_interpolacion.subs('x', val) for val in x_vals]

    plt.plot(x_vals, y_vals, label='Funcion interpolada')
    plt.scatter([p[0] for p in puntos], [p[1] for p in puntos], color='red', label='Puntos')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.title('Interpolacion progresiva parabolica: '+ fStr)
    plt.show()
valoresX = np.array([0, 0.1, 0.3, 0.8, 1])


valoresY_A = [funA(x) for x in valoresX]
valoresY_B = [funB(x) for x in valoresX]
puntosA = []
puntosB = []
for i in range(len(valoresX)):
    puntosA.append((valoresX[i], valoresY_A[i]))
    puntosB.append((valoresX[i], valoresY_B[i]))


print("Funcion: raiz(x+1)")
funcion_interpolacion = interpolacion_parabolica_progresiva(puntosA)
grafica(funcion_interpolacion, puntosA, 'raiz(x+1)')
print("Polinomio: ", funcion_interpolacion)
print("Polinomio simplificado: ", sp.simplify(funcion_interpolacion))

print("Funcion: tan(x)")
funcion_interpolacion = interpolacion_parabolica_progresiva(puntosB)
grafica(funcion_interpolacion, puntosB, 'tan(x)')
print("Polinomio: ", funcion_interpolacion)
print("Polinomio simplificado: ", sp.simplify(funcion_interpolacion))
