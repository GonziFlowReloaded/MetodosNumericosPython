import sympy as sp
import matplotlib.pyplot as plt
from prettytable import PrettyTable
import numpy as np

def funA(x):
    # Función A: raiz(x+1)
    return np.sqrt(x+1)

def funB(x):
    # Función B: tan(x)
    return np.tan(x)

def interpolacion_parabolica_progresiva(puntos):
    # Interpolación parabólica progresiva
    x = sp.symbols('x')
    n = len(puntos)

    # Inicializar el polinomio de interpolación
    P = 0

    # Calcular las diferencias divididas
    divided_diff = []
    for i in range(n):
        divided_diff.append(puntos[i][1])
    
    for i in range(1, n):
        for j in range(n - 1, i - 1, -1):
            divided_diff[j] = (divided_diff[j] - divided_diff[j - 1]) / (puntos[j][0] - puntos[j - i][0])

    # Construir el polinomio de interpolación
    for i in range(n):
        term = divided_diff[i]
        for j in range(i):
            term *= (x - puntos[j][0])
        P += term

    return P

def grafica(funcion_interpolacion, puntos, fStr):
    # Graficar la función interpolada y los puntos
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
    # Crear puntos (x, y) para la función A y B
    puntosA.append((valoresX[i], valoresY_A[i]))
    puntosB.append((valoresX[i], valoresY_B[i]))
# Puntos a Evaluar
puntosAEvaluar = [0.4, 0.9]


print("Funcion: raiz(x+1)")
# Calcular la interpolación para la función A
funcion_interpolacion = interpolacion_parabolica_progresiva(puntosA)
grafica(funcion_interpolacion, puntosA, 'raiz(x+1)')
print("Polinomio: ", funcion_interpolacion)
poli_simpli = sp.simplify(funcion_interpolacion)
print("Polinomio simplificado: ", poli_simpli)
tabla = PrettyTable()
tabla.field_names = ['Valor a evaluar', 'Valor real', 'Valor interpolado', 'Error']
for valor in puntosAEvaluar:
    tabla.add_row([valor, funA(valor), funcion_interpolacion.subs('x', valor), abs(funA(valor) - funcion_interpolacion.subs('x', valor))])
print(tabla)



print("Funcion: tan(x)")
# Calcular la interpolación para la función B
funcion_interpolacion = interpolacion_parabolica_progresiva(puntosB)
grafica(funcion_interpolacion, puntosB, 'tan(x)')
print("Polinomio: ", funcion_interpolacion)
print("Polinomio simplificado: ", sp.simplify(funcion_interpolacion))
tabla = PrettyTable()
tabla.field_names = ['Valor a evaluar', 'Valor real', 'Valor interpolado', 'Error']
for valor in puntosAEvaluar:
    tabla.add_row([valor, funA(valor), funcion_interpolacion.subs('x', valor), abs(funA(valor) - funcion_interpolacion.subs('x', valor))])
print(tabla)