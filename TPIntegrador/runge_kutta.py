def runge_kutta(f, t0, y0, h, n):
    # f es la función que representa la ecuación diferencial
    # t0 es el valor inicial de t
    # y0 es el valor inicial de y
    # h es el tamaño del paso
    # n es el número de pasos
    
    list_values = []

    t = t0
    y = y0
    
    for i in range(n):
        k1 = h * f(t, y)
        k2 = h * f(t + h/2, y + k1/2)
        k3 = h * f(t + h/2, y + k2/2)
        k4 = h * f(t + h, y + k3)
        
        y += (k1 + 2*k2 + 2*k3 + k4) / 6
        t += h

        list_values.append((t, y))
    
    return list_values


