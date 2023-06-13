from runge_kutta import *
from euler_modificado import *
from milne import *
import matplotlib.pyplot as plt

# f(t)=-3+2 (1+ℯ^(-2 t))^(-1) funcion para el geogebra

f = lambda x, y: -(y+1)*(y+3)
y0 = -2
x0 = 0
h = 0.4
n = 5
tol = 0.01


#Asignacion de valores
runge_kuttaValores = runge_kutta(f, x0, y0, h, n)
euler_modificadoValores = modificado_euler_v3(f, x0, x0 + n * h, y0, h, tol)
milne2Valores_x, milne2Valores_y = milne_2(f, y0, x0, x0 + n * h, h, tol)

runge_kuttaValores_x = [x[0] for x in runge_kuttaValores]
runge_kuttaValores_y = [x[1] for x in runge_kuttaValores]

euler_modificadoValores_x = [x[0] for x in euler_modificadoValores]
euler_modificadoValores_y = [x[1] for x in euler_modificadoValores]


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


