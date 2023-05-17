import numpy as np

def interpolacion_lagrange(x, y):
  """
  Interpolación de Lagrange.

  Args:
    x: Una lista de coordenadas x.
    y: Una lista de coordenadas y.

  Returns:
    Un polinomio que pasa por los puntos dados.
  """

  n = len(x)
  l = np.zeros(n)

  for i in range(n):
    l[i] = 1
    for j in range(n):
      if i != j:
        l[i] *= (x[i] - x[j])

  return np.poly1d(l)

if __name__ == "__main__":
  x = [0, 1, 2]
  y = [1, 3, 2]

  p = interpolacion_lagrange(x, y)  # Calcula el polinomio

  print(p)

  # x = 0.5
  y_hat = p(0.5)  # Calcula el valor y_hat para x = 0.5 usando el polinomio

  print(y_hat)
