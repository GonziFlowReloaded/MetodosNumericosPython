import numpy as np

def jacobi(A, b, x0, tol=1e-6, max_iterations=100):
    n = len(A)
    x = x0.copy()
    x_new = np.zeros_like(x)

    for k in range(max_iterations):
        for i in range(n):
            sum_term = 0
            for j in range(n):
                if j != i:
                    sum_term += A[i][j] * x[j]
            x_new[i] = (b[i] - sum_term) / A[i][i]
        
        if np.linalg.norm(x_new - x) < tol:
            break
        
        x = x_new.copy()

    return x_new

