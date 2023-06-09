def milne(f, t0, y0, h, n):
    # f es la función que representa la ecuación diferencial
    # t0 es el valor inicial de t
    # y0 es el valor inicial de y
    # h es el tamaño del paso
    # n es el número de pasos
    
    t = t0
    y = y0
    
    for i in range(3):
        k1 = h * f(t, y)
        k2 = h * f(t + h/2, y + k1/2)
        k3 = h * f(t + h/2, y + k2/2)
        k4 = h * f(t + h, y + k3)
        
        y += (k1 + 4*k2 + k3) * h / 6
        t += h
    
    for i in range(3, n):
        y_pred = y + (h/24) * (55*f(t, y) - 59*f(t-h, y) + 37*f(t-2*h, y) - 9*f(t-3*h, y))
        y = y + (h/24) * (9*f(t+h, y_pred) + 19*f(t, y) - 5*f(t-h, y) + f(t-2*h, y))
        t += h
    
    return y