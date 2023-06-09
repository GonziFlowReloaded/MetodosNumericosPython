from runge_kutta import *
from euler_modificado import *
from milne import *

# f(t)=-3+2 (1+ℯ^(-2 t))^(-1) funcion para el geogebra

f = lambda x, y: -(y+1)*(y+3)
y0 = -2
x0 = 0
h = 0.4
n = 5
tol = 0.01

print("Runge-Kutta")
#print(runge_kutta(f, x0, y0, h, n))

print("Euler Modificado")
#print(euler_modificado(x0, y0, h, f, tol))

print("Milne")
print(milne_2(f, y0, x0, 2, h, tol))
