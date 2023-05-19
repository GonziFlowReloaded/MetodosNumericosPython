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

valoresX = np.array([0, 0.1, 0.3, 0.8, 1])
valoresY_A = [funA(x) for x in valoresX]
valoresY_B = [funB(x) for x in valoresX]

x = Symbol('x')
def polinomioL(xi, fi):
    polinomio = 0
    for i in range(len(xi)):
        numerador = 1
        denominador = 1
        for j in range(len(xi)):
            if (j != i):
                numerador *= x - xi[j]
                denominador *= xi[i] - xi[j]
        terminoL = numerador/denominador
        polinomio += terminoL*fi[i]
    return polinomio

def valores(xi, fi):
    pol = polinomioL(xi, fi)
    poli_simpli = pol.expand()
    px = lambdify(x, poli_simpli)
    muestras = 100
    a,b = min(xi), max(xi)
    pxi = np.linspace(a, b, muestras)
    pfi = [px(i) for i in pxi]

    return pxi, pfi, pol, poli_simpli

def grafica(xi,fi,pxi,pfi, funcion):
    plt.plot(xi, fi, 'o', label = 'Puntos')
    plt.plot(pxi, pfi, label = 'Polinomio')
    plt.legend()
    plt.grid(1)
    plt.xlabel('xi')
    plt.ylabel('fi')
    plt.title('Interpolación Lagrange: '+ funcion)
    plt.show()

puntosAEvaluar = [0.4, 0.9]

print("Funcion: raiz(x+1)")
pxi, pfi, pol, poli_simpli = valores(valoresX, valoresY_A)
grafica(valoresX, valoresY_A, pxi, pfi,'raiz(x+1)')
print("Polinomio: ", pol)
print("Polinomio simplificado: ", poli_simpli)
tabla = PrettyTable()
tabla.field_names = ["Valor a evaluar", "Valor real", "Valor interpolado", "Error"]
for valor in puntosAEvaluar:
    tabla.add_row([valor, funB(valor), poli_simpli.subs(x, valor), abs(funB(valor) - poli_simpli.subs(x, valor)) / funB(valor)])
print(tabla)




print("Funcion: tan(x)")
pxi, pfi, pol, poli_simpli = valores(valoresX, valoresY_B)
grafica(valoresX, valoresY_B, pxi, pfi, 'tan(x)')
print("Polinomio: ", pol)
print("Polinomio simplificado: ", poli_simpli)
tabla = PrettyTable()
tabla.field_names = ["Valor a evaluar", "Valor real", "Valor interpolado", "Error"]
for valor in puntosAEvaluar:
    tabla.add_row([valor, funB(valor), poli_simpli.subs(x, valor), abs(funB(valor) - poli_simpli.subs(x, valor)) / funB(valor)])
print(tabla)

