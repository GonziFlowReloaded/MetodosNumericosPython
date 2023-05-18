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

