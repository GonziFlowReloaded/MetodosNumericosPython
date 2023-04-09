import numpy as np
from prettytable import PrettyTable

def puntofijo(gx,a,tolera, iteramax = 15):
    i = 1 
    datos = []
    b = gx(a)
    tramo = abs(b-a)
    while(tramo>=tolera and i<=iteramax ):
        datos.append([i,a,b,gx(a),gx(b),tramo])
        a = b
        b = gx(a)
        tramo = abs(b-a)
        i = i + 1
    respuesta = b
    
    if (i>=iteramax ):
        respuesta = np.nan
    tabla(datos)
    return(respuesta)

def tabla(datos):
    tabla = PrettyTable()
    tabla.field_names = ['Iteración','a','b','f(a)','f(b)','Error']
    for i in range(len(datos)):
        tabla.add_row(datos[i])
    print(tabla)



f = lambda x: x - np.tan(x) - np.pi

a = 4     
b = 4.5
tolera = 0.001
iteramax = 15  
muestras = 51  
tramos = 50


respuesta = puntofijo(f,a,tolera)

print(respuesta)
