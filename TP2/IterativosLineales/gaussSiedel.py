import numpy as np

def gauss_seidel(A, b, x_0, tol=1e-10, max_iter=100):
  """
  Método de Gauss-Seidel.

  Args:
    A: La matriz de coeficientes.
    b: El vector del lado derecho.
    x_0: La suposición inicial.
    tol: La tolerancia.
    max_iter: El número máximo de iteraciones.

  Returns:
    La solución del sistema Ax = b.
  """

  n = len(A)
  x = x_0.copy()

  for i in range(max_iter):
    x_new = np.zeros(n)
    for j in range(n):
      x_new[j] = (b[j] - np.dot(A[j, :], x)) / A[j, j]  # Calcula el nuevo valor de x[j] utilizando el método de Gauss-Seidel

    norm = np.linalg.norm(x_new - x)
    if norm < tol:  # Comprueba si la norma de la diferencia entre el nuevo y el viejo x es menor que la tolerancia
      break

    x = x_new

  return x

if __name__ == "__main__":
  A = np.array([[1, -1, 0],
                 [-1, 2, -1],
                 [0, -1, 3]])
  b = np.array([1, 2, 3])
  x_0 = np.zeros(3)

  x = gauss_seidel(A, b, x_0)  # Calcula la solución del sistema Ax = b utilizando el método de Gauss-Seidel

  print(x)


