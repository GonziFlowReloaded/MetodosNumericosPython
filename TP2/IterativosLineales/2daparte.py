from gaussSiedel import gauss_seidel
import numpy as np
from jacobi import jacobi

array = np.array([[3, -1, 1],
               [3, 6, 2],
               [3, 3, 7]])

b = np.array([1, 0, 4])

x_init = np.zeros(3)

tol = 1e-4

max_iter = 100
print('Gauss-Seidel')
x = gauss_seidel(array, b, x_init, tol, max_iter)
print(x)

print('Jacobi')
x = jacobi(array, b, x_init, tol, max_iter)
print(x)

