from math import sin, pi

def bessel_interpolation(x: list, y: list, x_interpolate: float) -> float:

    # Determinar el tamaño de los arreglos x e y
    n = len(x)

    # Calcular los coeficientes a_i
    a = y.copy()

    for j in range(1, n):
        for i in range(n-1, j-1, -1):
            a[i] = (a[i] - a[i-1]) / (x[i] - x[i-j])

    # Calcular la función interpolada en x_interpolate
    y_interpolate = 0
    for i in range(n):
        y_interpolate += a[i] * sin((n-i-1/2) * pi * (x_interpolate - x[n-1]) / (x[1] - x[0]))

    return y_interpolate


x = [1.5,2,2.5,3,3.5,4]
y = [2,8,14,15,8,2]
x_interpolate = 2.3
result = bessel_interpolation(x, y, x_interpolate)
print(result)