from gaussSiedel import gauss_seidel
import numpy as np
from jacobi import jacobi

matrizA = np.array([[3, -1, 1],
               [3, 6, 2],
               [3, 3, 7]])

b = np.array([1, 0, 4])
x_init = np.zeros(3)
tol = 1e-4
max_iter = 100

print('Matriz:')
#Mostrar matriz con formato
for i in range(len(matrizA)):
    for j in range(len(matrizA[i])):
        print(matrizA[i][j], end=' ')
    print()
print('Vector b:')
print(b)
print('Vector inicial:')
print(x_init)
print('Tolerancia:')
print(tol)
print('Máximo de iteraciones:')
print(max_iter)





print('Gauss-Seidel')
x = gauss_seidel(matrizA, b, x_init, tol, max_iter)
print(x)

print('Jacobi')
x = jacobi(matrizA, b, x_init, tol, max_iter)
print(x)


matrizB = np.array([[10, 2, -1],
                   [-3,-6,2],
                   [1,1,5]])

b = np.array([27, -61.5, -21.5])

x_init = np.zeros(3)

tol = 5e-3
print('-'*50)
print('Matriz:')
#Mostrar matriz con formato
for i in range(len(matrizB)):
    for j in range(len(matrizB[i])):
        print(matrizB[i][j], end=' ')
    print()
print('Vector b:')
print(b)
print('Vector inicial:')
print(x_init)
print('Tolerancia:')
print(tol)
print('Máximo de iteraciones:')
print(max_iter)

print('Gauss-Seidel')
x = gauss_seidel(matrizB, b, x_init, tol, max_iter)
print(x)

print('Jacobi')
x = jacobi(matrizB, b, x_init, tol, max_iter)
print(x)
