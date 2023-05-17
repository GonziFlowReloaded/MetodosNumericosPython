import math
from prettytable import PrettyTable

def falsaP(funcion, x_i, x_f, iteraciones=1000, error_r=0.001):
    # Se inicializan las variables
    solucion = None
    contador = 0
    errorCalculado = 101
    datosParaTabla = []
    #Evaluar en el intervalo
    print("-" * 20 + "Falsa Posicion" + "-" * 20)
    print('Intervalo: [{}, {}]'.format(x_i, x_f))
    if funcion(x_i) * funcion(x_f) <= 0:
        
        while contador <= iteraciones and errorCalculado >= error_r:
            contador+=1
            solucion = x_f - ((funcion(x_f) * (x_f - x_i)) / (funcion(x_f) - funcion(x_i)))
            errorCalculado = abs((solucion - x_i) / solucion)
            datosParaTabla.append([contador, x_i, funcion(x_i), solucion, errorCalculado])

            if funcion(x_i) * funcion(solucion) >= 0:
                x_i = solucion
            else:
                x_f = solucion
            
        
        print('f(x) = e^x - 3x^2')
        print("La solucion aproximada es: {}".format(solucion))
        print('Encontrada en {} iteraciones'.format(contador))
        print('Con un error relativo de: {}%'.format(errorCalculado)) 
    else:
        print("No existe solucion en el intervalo")
    
    return datosParaTabla


def hacerTabla(datosParaTabla):
    tabla = PrettyTable()
    tabla.field_names = ["Iteracion", "Xi", "f(Xi)", "Xr", "ErrorCalculado"]
    for fila in datosParaTabla:
        tabla.add_row(fila)
    print(tabla)


# Tutorial:
# El segundo parametro es nuestro principio de intervalo
# El tercer parametro es nuestro final de intervalo
# En este caso el intervalo es [0, 1]
# La funcion es: e^x - 3x^2
fx = lambda x: math.exp(x) - 3 * x ** 2
hacerTabla(falsaP(fx, 0, 1))