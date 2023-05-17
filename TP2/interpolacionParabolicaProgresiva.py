import numpy as np

def progressive_parabolic(x, y):
  """
  Progressive parabolic method.

  Args:
    x: A list of x-coordinates.
    y: A list of y-coordinates.

  Returns:
    A polynomial that passes through the given points.
  """

  n = len(x)
  p = np.zeros(n)

  for i in range(n):
    p[i] = (y[i] + y[i + 1]) / 2

  for j in range(1, n - 1):
    p[j] += (x[j + 1] - x[j]) * (y[j + 1] - y[j]) / (x[j + 1] - x[j - 1])

  return p

if __name__ == "__main__":
  x = [0, 1, 2]
  y = [1, 3, 2]

  p = progressive_parabolic(x, y)

  print(p)

  # x = 0.5
  y_hat = p(0.5)

  print(y_hat)
