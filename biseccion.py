import numpy as np
import math
from prettytable import PrettyTable

f = lambda x: x**3-2*x**2-11*x+12

def tabla(datos):
    tabla = PrettyTable()
    tabla.field_names = ["Iteración","a","b","c","f(a)","f(b)","f(c)","Error"]
    for i in range(len(datos)):
        tabla.add_row(datos[i])
    print(tabla)




def biseccion(f,a,b,tol):
    datos=[]
    i=0
    if f(a)*f(b)>0:
        print("No hay raíz en el intervalo")
        return
    else:
        c=(a+b)/2
        while abs(f(c))>tol:
            if f(a)*f(c)<0:
                b=c
            else:
                a=c
            c=(a+b)/2
            i+=1
            datos.append([i,a,b,c,f(a),f(b),f(c),abs(f(c))])
        tabla(datos)
        return c
    
b=-3
a=3
tol=1e-6
raiz=biseccion(f,a,b,tol)
print("La raíz es: ",raiz)
