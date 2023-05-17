def gauss_interpolation(x: list, y: list, x_interpolate: float) -> float:
    
    # Determinar el tamaño de los arreglos x e y
    n = len(x)

    # Calcular los coeficientes a_i
    a = y.copy()

    for j in range(1, n):
        for i in range(n-1, j-1, -1):
            a[i] = (a[i] - a[i-1]) / (x[i] - x[i-j])

    # Calcular la función interpolada en x_interpolate
    y_interpolate = a[n-1]
    for i in range(n-2, -1, -1):
        y_interpolate = a[i] + (x_interpolate - x[i]) * y_interpolate

    return y_interpolate

x = [1.5,2,2.5,3,3.5,4]
y = [2,8,14,15,8,2]
x_interpolate = 2.3
result = gauss_interpolation(x, y, x_interpolate)
print(result)
