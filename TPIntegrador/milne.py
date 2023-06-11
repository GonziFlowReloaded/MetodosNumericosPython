import numpy as np
def milne(f, t0, y0, h, n):
    # f es la función que representa la ecuación diferencial
    # t0 es el valor inicial de t
    # y0 es el valor inicial de y
    # h es el tamaño del paso
    # n es el número de pasos
    
    t = t0
    y = y0
    
    # Paso de arranque utilizando el método de Runge-Kutta de orden 4
    for i in range(3):
        k1 = h * f(t, y)
        k2 = h * f(t + h/2, y + k1/2)
        k3 = h * f(t + h/2, y + k2/2)
        k4 = h * f(t + h, y + k3)
        
        y += (k1 + 4*k2 + k3) * h / 6
        t += h
    
    # Iteración principal utilizando el método de Milne
    for i in range(3, n):
        y_pred = y + (h/24) * (55*f(t, y) - 59*f(t-h, y) + 37*f(t-2*h, y) - 9*f(t-3*h, y))
        y = y + (h/24) * (9*f(t+h, y_pred) + 19*f(t, y) - 5*f(t-h, y) + f(t-2*h, y))
        t += h
    
    return [t, y]

def milne_2(f, y0, t0, tf, h, tol):
    # Función f: dy/dt = f(t, y)
    # Valor inicial y0 = y(t0)
    # Tiempo inicial t0
    # Tiempo final tf
    # Tamaño del paso h
    # Tolerancia tol

    # Calcula el número total de pasos
    n = int((tf - t0) / h)              # Número total de pasos
    t = np.linspace(t0, tf, n + 1)      # Vector de valores de t
    y = np.zeros(n + 1)                 # Vector de valores de y
    y[0] = y0

    # Paso de predicción
    for i in range(1, 4):
        k1 = h * f(t[i - 1], y[i - 1])
        k2 = h * f(t[i - 1] + h / 2, y[i - 1] + k1 / 2)
        k3 = h * f(t[i - 1] + h / 2, y[i - 1] + k2 / 2)
        k4 = h * f(t[i - 1] + h, y[i - 1] + k3)
        y[i] = y[i - 1] + (k1 + 2 * k2 + 2 * k3 + k4) / 6

    # Paso de corrección
    for i in range(3, n):
        y_pred = y[i - 3] + 4 * h / 3 * (2 * f(t[i - 2], y[i - 2]) - f(t[i - 1], y[i - 1]) + 2 * f(t[i], y[i]))
        y_corr = y[i - 1] + h / 3 * (f(t[i - 1], y[i - 1]) + 4 * f(t[i], y[i]) + f(t[i + 1], y_pred))
        delta = np.abs(y_corr - y_pred)
        
        # Ajuste del paso de integración h si se excede la tolerancia
        if delta > tol:
            h = h * (tol / delta) ** 0.25
            y_pred = y[i - 3] + 4 * h / 3 * (2 * f(t[i - 2], y[i - 2]) - f(t[i - 1], y[i - 1]) + 2 * f(t[i], y[i]))
            y_corr = y[i - 1] + h / 3 * (f(t[i - 1], y[i - 1]) + 4 * f(t[i], y[i]) + f(t[i + 1], y_pred))

        y[i + 1] = y_corr

    return t.tolist(), y.tolist()