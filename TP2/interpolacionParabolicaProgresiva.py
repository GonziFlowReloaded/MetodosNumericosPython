import numpy as np

def metodo_parabolico_progresivo(x, y):
  """
  Método parabólico progresivo.

  Args:
    x: Una lista de coordenadas x.
    y: Una lista de coordenadas y.

  Returns:
    Un polinomio que pasa por los puntos dados.
  """

  n = len(x)
  p = np.zeros(n)

  for i in range(n):
    p[i] = (y[i] + y[i + 1]) / 2  # Calcula el valor medio de y[i] y y[i + 1] para obtener los coeficientes iniciales

  for j in range(1, n - 1):
    p[j] += (x[j + 1] - x[j]) * (y[j + 1] - y[j]) / (x[j + 1] - x[j - 1])  # Ajusta los coeficientes para obtener el polinomio

  return p

if __name__ == "__main__":
  x = [0, 1, 2]
  y = [1, 3, 2]

  p = metodo_parabolico_progresivo(x, y)  # Calcula el polinomio

  print(p)

  # x = 0.5
  y_hat = p(0.5)  # Calcula el valor y_hat para x = 0.5 usando el polinomio

  print(y_hat)
