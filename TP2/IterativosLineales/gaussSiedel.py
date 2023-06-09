import numpy as np

def gauss_seidel(A, b, x0, tol, max_iter):
    n = len(A)                  # Obtener el tamaño del sistema de ecuaciones
    x = x0.copy()               # Copiar el vector inicial x0
    iter_count = 0              # Inicializar el contador de iteraciones y el error
    error = tol + 1

    # Realizar iteraciones hasta que se cumpla la condición de convergencia o se alcance el número máximo de iteraciones.
    while error > tol and iter_count < max_iter:
        x_new = x.copy()

         # Actualizar cada componente de x_new utilizando el método de Gauss-Seidel
        for i in range(n):
            s1 = sum(A[i][j] * x_new[j] for j in range(i))
            s2 = sum(A[i][j] * x[j] for j in range(i + 1, n))
            x_new[i] = (b[i] - s1 - s2) / A[i][i]
        
        # Calcular el error como la máxima diferencia entre los elementos de x_new y x
        error = max(abs(x_new[i] - x[i]) for i in range(n))
        x = x_new
        iter_count += 1

    # Si no se alcanza la convergencia dentro del número máximo de iteraciones, imprimir un mensaje de advertencia
    if iter_count == max_iter and error > tol:
        print("El método Gauss-Seidel no convergió en esa tolerancia específica.")
    
    # Devolver el vector solución x
    return x