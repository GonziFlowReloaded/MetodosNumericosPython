import math

def falsaP(funcion, x_i, x_f, iteraciones=1000, error_r=0.001):
    # Se inicializan las variables
    solucion = None
    contador = 0
    errorCalculado = 101
    #Evaluar en el intervalo
    if funcion(x_i) * funcion(x_f) <= 0:
        
        while contador <= iteraciones and errorCalculado >= error_r:
            contador+=1
            solucion = x_f - ((funcion(x_f) * (x_f - x_i)) / (funcion(x_f) - funcion(x_i)))
            errorCalculado = abs((solucion - x_i) / solucion)
            #---
            if funcion(x_i) * funcion(solucion) >= 0:
                x_i = solucion
            else:
                x_f = solucion
        
        print("La solucion aproximada es: {:.6f}".format(solucion))
        print('Encontrada en {} iteraciones'.format(contador))
        print('Con un error relativo de: {:.6f}%'.format(errorCalculado)) 
    else:
        print("No existe solucion en el intervalo")

# Tutorial:
# El segundo parametro es nuestro principio de intervalo
# El tercer parametro es nuestro final de intervalo
# En este caso el intervalo es [3, 5]
# La funcion es: e^x - 3x^2

falsaP(lambda x: math.exp(x) - 3 * x ** 2, 3, 5)