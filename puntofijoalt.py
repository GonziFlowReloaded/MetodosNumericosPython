import math
from prettytable import PrettyTable
def f(x):
    return x - math.tan(x) + math.pi

def g(x):
    return math.tan(x) - math.pi

def punto_fijo(f, x0, tol=1e-4, max_iter=20):
    datosTabla = []
    i = 0
    error = tol + 1
    x_ant = x0
    while error > tol:
        x_nuevo = f(x_ant)
        error = abs(x_nuevo - x_ant)
        x_ant = x_nuevo
        i += 1
        datosTabla.append([i, x_ant, f(x_ant), error])
        if i == max_iter:
            return datosTabla
    return datosTabla

def tabla(datos):
    tabla = PrettyTable()
    tabla.field_names = ['Iteración','a','f(a)','Error']
    for i in range(len(datos)):
        tabla.add_row(datos[i])
    print(tabla)

respuesta = punto_fijo(g,4.5)

tabla(respuesta)

print('f(4.5) = {}'.format(f(4.5)))
print('g(4.5) = {}'.format(g(4.5)))

print('f(4) = {}'.format(f(4)))
print('g(4) = {}'.format(g(4)))


