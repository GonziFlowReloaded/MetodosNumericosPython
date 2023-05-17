import numpy as np
from prettytable import PrettyTable

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



f = lambda x: np.tan(x) - np.pi
# f = lambda x 
a = 4     
b = 4.5

respuesta = punto_fijo(f,b)

tabla(respuesta)
