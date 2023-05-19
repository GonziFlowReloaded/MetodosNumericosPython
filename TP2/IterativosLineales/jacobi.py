import numpy as np

def jacobi(A, b, x_init, tol=1e-6, max_iter=100):
  """
  Solves the linear system Ax = b using the Jacobi method.

  Args:
    A: The coefficient matrix.
    b: The right-hand side vector.
    x_init: The initial guess for the solution.
    tol: The tolerance for convergence.
    max_iter: The maximum number of iterations.

  Returns:
    The solution to the linear system.
  """

  # Initialize the solution.
  x = x_init

  # Iterate until convergence or the maximum number of iterations is reached.
  for i in range(max_iter):

    # Update the solution.
    x = (b - A @ x) / A.diagonal()

    # Check for convergence.
    if np.linalg.norm(x - x_init) < tol:
      break

  return x

