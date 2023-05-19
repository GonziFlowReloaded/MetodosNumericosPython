from interpolacionParabolicaProgresiva import metodo_parabolico_progresivo
import numpy as np
from interpolacionLagrange import interpolacion_lagrange
from prettytable import PrettyTable
import matplotlib.pyplot as plt
from sympy import *

def funA(x):
    return np.sqrt(x+1)

def funB(x):
    return np.tan(x)

# valoresX = np.array([0, 0.1, 0.3, 0.8, 1])
valoresX = np.array([0.1, 0.3, 0.8])
# valoresY_B = [funA(x) for x in valoresX] valA
valoresY_B = [funB(x) for x in valoresX]


def interpolacion_parabolica_progresiva(x, y):
    n = len(x)
    if n != 3:
        raise ValueError("La interpolación parabólica progresiva requiere exactamente 3 puntos.")
    
    x0, x1, x2 = x
    y0, y1, y2 = y
    
    h = x1 - x0
    delta1 = (y1 - y0) / h
    delta2 = (y2 - y1) / (x2 - x1)
    
    a = delta2 - delta1
    b = a - delta2
    c = y2 - (a * x2**2 + b * x2)
    
    # Crear símbolos para el polinomio
    x = Symbol('x')
    a_sym = Symbol('a')
    b_sym = Symbol('b')
    c_sym = Symbol('c')
    
    # Construir el polinomio
    polynomial = a_sym * x**2 + b_sym * x + c_sym
    
    # Sustituir los valores encontrados en el polinomio
    polynomial = polynomial.subs([(a_sym, a), (b_sym, b), (c_sym, c)])
    
    return simplify(polynomial)

# Ejemplo de uso


polinomio = interpolacion_parabolica_progresiva(valoresX, valoresY_B)
print("El polinomio generado es:", polinomio)


# Convertir el polinomio a una función numérica
polinomio_func = lambdify('x', polinomio, modules=['numpy'])

# Generar puntos para trazar la línea
x_vals = np.linspace(min(valoresX), max(valoresY_B), 100)
y_vals = polinomio_func(x_vals)

# Graficar los puntos de interpolación y la línea
plt.scatter(valoresX, valoresY_B, color='red', label='Puntos de interpolación')
plt.plot(x_vals, y_vals, color='blue', label='Polinomio generado')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interpolación Parabólica Progresiva')
plt.legend()
plt.grid(True)
plt.show()