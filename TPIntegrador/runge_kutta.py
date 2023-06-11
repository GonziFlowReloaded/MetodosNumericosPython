def runge_kutta(f, t0, y0, h, n):
    # f es la función que representa la ecuación diferencial
    # t0 es el valor inicial de t
    # y0 es el valor inicial de y
    # h es el tamaño del paso
    # n es el número de pasos
    
    list_values = []                        # Lista para almacenar los pares (t, y)

    t = t0          # Valor inicial de t
    y = y0          # Valor inicial de y
    
    for i in range(n):
        k1 = h * f(t, y)                # 1° coeficiente k1
        k2 = h * f(t + h/2, y + k1/2)   # 2° coeficiente k2
        k3 = h * f(t + h/2, y + k2/2)   # 3° coeficiente k3
        k4 = h * f(t + h, y + k3)       # 4° coeficiente k4
        
        y += (k1 + 2*k2 + 2*k3 + k4) / 6    # Actualiza el valor de y mediante la fórmula del método de Runge-Kutta
        t += h              # Actualiza el valor de t

        list_values.append((t, y))      # Agrega el par (t, y) a la lista de valores
    
    return list_values      # Devuelve la lista de valores de la solución aproximada


