def gregory_newton(x, y, target):

    n = len(x)
    # tabla de diferencias divididas
    tabla = [[0 for j in range(n)] for i in range(n)]

    # copiar los valores y en la primera columna de la tabla
    for i in range(n):
        tabla[i][0] = y[i]

    # calcular las diferencias divididas
    for j in range(1, n):
        for i in range(n - j):
            tabla[i][j] = (tabla[i + 1][j - 1] - tabla[i][j - 1]) / (x[i + j] - x[i])

    # evaluar el polinomio interpolante en target
    resultado = tabla[0][0]
    for j in range(1, n):
        producto = 1
        for i in range(j):
            producto *= (target - x[i])
        resultado += tabla[0][j] * producto

    return resultado


x = [1.5,2,2.5,3,3.5,4]
y = [2,8,14,15,8,2]

resultado = gregory_newton(x, y, 2.3)
print(resultado)