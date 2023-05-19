import numpy as np

def jacobi(A, b, x0, tol=1e-6, max_iterations=100):

    """
    Implementación del método de Jacobi para resolver un sistema de ecuaciones lineales.

    Args:
        A: Matriz de coeficientes del sistema.
        b: Vector de términos independientes.
        x0: Vector inicial de soluciones.
        tol: Tolerancia para la convergencia.
        max_iterations: Número máximo de iteraciones.

    Returns:
        x_new: Vector de soluciones aproximadas.

    """

    n = len(A)
    x = x0.copy()
    x_new = np.zeros_like(x)

    for k in range(max_iterations):
        # Iterar sobre cada fila de la matriz
        for i in range(n):
            sum_term = 0
             # Calcular la suma de los términos de la ecuación
            for j in range(n):
                if j != i:
                    sum_term += A[i][j] * x[j]
            # Calcular la nueva aproximación de x[i]
            x_new[i] = (b[i] - sum_term) / A[i][i]
            
        # Verificar la convergencia
        if np.linalg.norm(x_new - x) < tol:
            break
        
        x = x_new.copy()

    return x_new

