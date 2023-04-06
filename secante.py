import math
from prettytable import PrettyTable

def secante(funcion, x_i, x_f, tol):
    print("-" * 20 + "Secante" + "-" * 20)
    print('f(x) = e^x - 3x^2')
    print('Intervalo: {}'.format([x_i, x_f]))
    error = 1e3
    contador = 0
    x_h = 0
    datosParaTabla = []
    
    while error > tol:
        x_h = x_i - ((x_f- x_i)/(funcion(x_f) - funcion(x_i))) * funcion(x_i)
        x_i = x_f
        x_f = x_h
        error = abs(funcion(x_h))
        contador += 1
        datosParaTabla.append([contador, x_i, x_f, x_h, error])

    
    

    return datosParaTabla

def imprimirTabla(datosParaTabla):
    tabla = PrettyTable()
    tabla.field_names = ["Iteracion", "Xi", "Xf", "Xh", "Error Porcentual"]
    for fila in datosParaTabla:
        tabla.add_row(fila)
    print(tabla)

fx = lambda x: math.exp(x) - 3 * x ** 2

imprimirTabla(secante(fx, 0, 1, 0.0001))
imprimirTabla(secante(fx, 3, 5, 0.0001))