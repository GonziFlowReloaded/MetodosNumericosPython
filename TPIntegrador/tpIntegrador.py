from runge_kutta import *
from euler_modificado import *
from milne import *
import matplotlib.pyplot as plt

# Se define la función diferencial:
# f(t)=-3+2 (1+ℯ^(-2 t))^(-1) funcion para el geogebra

# La ecuación diferencial correspondiente a la función diferencial dada es:
f = lambda x, y: -(y+1)*(y+3)
y0 = -2                         #es el valor inicial de y.
x0 = 0                          #es el valor inicial de x
h = 0.4                         #es el tamaño del paso o incremento utilizado en los métodos.
n = 5                           #es el número de pasos o iteraciones que se realizarán en el método numérico.
tol = 0.01                      #es la tolerancia utilizada en el método de Euler modificado.


# Asignacion de valores
runge_kuttaValores = runge_kutta(f, x0, y0, h, n)

# Se aplica el método de Runge-Kutta para calcular los valores de X e Y a través de la función runge_kutta.
# Los valores resultantes se almacenan en la variable runge_kuttaValores.

euler_modificadoValores = euler_modificado_v2(f, x0, x0 + n * h, h, y0, tol)

# Se aplica el método de Euler modificado para calcular los valores de X e Y a través de la función euler_modificado_v2.
# Los valores resultantes se almacenan en la variable euler_modificadoValores.

milne2Valores_x, milne2Valores_y = milne_2(f, y0, x0, x0 + n * h, h, tol)
# Se aplica el método de Milne para calcular los valores de X e Y a través de la función milne_2.
# Los valores resultantes se almacenan en las variables milne2Valores_x y milne2Valores_y.

runge_kuttaValores_x = [x[0] for x in runge_kuttaValores]
runge_kuttaValores_y = [x[1] for x in runge_kuttaValores]
# Se extraen los valores de X e Y de runge_kuttaValores y se almacenan en las listas runge_kuttaValores_x y runge_kuttaValores_y, respectivamente.

euler_modificadoValores_x = [x[0] for x in euler_modificadoValores]
euler_modificadoValores_y = [x[1] for x in euler_modificadoValores]
# Se extraen los valores de X e Y de euler_modificadoValores y se almacenan en las listas euler_modificadoValores_x y euler_modificadoValores_y, respectivamente.

# Graficar la función y los puntos específicos
plt.scatter(runge_kuttaValores_x, runge_kuttaValores_y, label="Runge-Kutta", color="red")
plt.scatter(euler_modificadoValores_x, euler_modificadoValores_y, label="Euler Modificado", color="green")
plt.scatter(milne2Valores_x, milne2Valores_y, label="Milne", color="blue")

#Graficar la funcion
x = np.linspace(x0, x0 + n * h, 100)
y = -3 + 2 * (1 + np.exp(-2 * x)) ** (-1)
plt.plot(x, y, label="Funcion dada")
plt.legend()
plt.show()


