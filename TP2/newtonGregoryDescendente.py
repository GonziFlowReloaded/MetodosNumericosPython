
def newton_descendente(x, y, x0):
    n = len(x)
    # Calculamos las diferencias divididas descendentes
    delta = [[0] * (n-i) for i in range(n)]
    delta[0] = y
    for i in range(1, n):
        for j in range(n-i):
            delta[i][j] = (delta[i-1][j+1] - delta[i-1][j]) / (x[j+i] - x[j])
    # Calculamos el polinomio interpolador
    p = delta[0][0]
    prod = 1
    for i in range(1, n):
        prod *= (x0 - x[n-i-1])
        p += delta[i][0] * prod
    return p

# Ejemplo de uso
x = [1.5,2,2.5,3,3.5,4]
y = [2,8,14,15,8,2]

x0 = 4.3
p = newton_descendente(x, y, x0)
print("El valor interpolado en x =", x0, "es:", p)


