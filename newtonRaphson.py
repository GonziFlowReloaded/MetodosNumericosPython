
import numpy as np
import math
from prettytable import PrettyTable

#Funcion
fx = lambda x: math.exp(x) - 3 * x ** 2
dfx = lambda x: math.exp(x) - 6 * x

intervalo1 = [0, 1]
intervalo2 = [3, 5]

def newtonRaphson(funcion, derivada, intervalo, iteraciones=1000, error_r=0.0001):
    x_i = intervalo[0]
    x_f = intervalo[1]
    # Se inicializan las variables
    solucion = None
    contador = 0
    errorCalculado = 101
    datosParaTabla = []
    #Evaluar en el intervalo
    if funcion(x_i) * funcion(x_f) <= 0:
            
            while contador <= iteraciones and errorCalculado >= error_r:
                contador+=1
                solucion = x_f - (funcion(x_f) / derivada(x_f))
                errorCalculado = (solucion - x_i) / solucion
                datosParaTabla.append([contador, x_f, funcion(x_f), derivada(x_f), solucion, errorCalculado])

                if funcion(x_i) * funcion(solucion) >= 0:
                    x_i = solucion


                else:
                    x_f = solucion

            print("-" * 20 + "Newton Raphson" + "-" * 20)
            print('f(x) = e^x - 3x^2')
            print('f\'(x) = e^x - 6x')
            print('Intervalo: {}'.format(intervalo))
    else:
        print("No existe solucion en el intervalo")

    return datosParaTabla


def imprimirTabla(datosParaTabla):
    tabla = PrettyTable()
    tabla.field_names = ["Iteracion", "Xi", "f(Xi)", "f'(Xi)", "Xr", "ErrorCalculado"]
    for fila in datosParaTabla:
        tabla.add_row(fila)
    print(tabla)


# print("Intervalo 1: {}".format(intervalo1))
# newtonRaphson(fx, dfx, intervalo1)
# print(20 * "-")
# print("Intervalo 2: {}".format(intervalo2))
# newtonRaphson(fx, dfx, intervalo2)

imprimirTabla(newtonRaphson(fx, dfx, intervalo1))

imprimirTabla(newtonRaphson(fx, dfx, intervalo2))