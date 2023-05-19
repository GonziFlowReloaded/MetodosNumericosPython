import numpy as np

def gauss_seidel(A, b, x0, tol, max_iter):
    n = len(A)
    x = x0.copy()
    iter_count = 0
    error = tol + 1

    while error > tol and iter_count < max_iter:
        x_new = x.copy()
        for i in range(n):
            s1 = sum(A[i][j] * x_new[j] for j in range(i))
            s2 = sum(A[i][j] * x[j] for j in range(i + 1, n))
            x_new[i] = (b[i] - s1 - s2) / A[i][i]
        
        error = max(abs(x_new[i] - x[i]) for i in range(n))
        x = x_new
        iter_count += 1

    if iter_count == max_iter and error > tol:
        print("Gauss-Seidel method did not converge within the specified tolerance.")
    
    return x

