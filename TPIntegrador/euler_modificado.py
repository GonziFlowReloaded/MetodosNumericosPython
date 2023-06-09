def euler_modificado(t0, y0, h, f, tolerancia):
    t = t0
    y = y0
    list_values = []

    t_f = t0 + h
    
    while t < t_f:
        k1 = f(t, y)
        k2 = f(t + h/2, y + h/2 * k1)
        y_pred = y + h * k2
        error = abs(y_pred - y)
        if error < tolerancia:
            y = y_pred
            t = t + h
        else:
            h = h/2
        list_values.append((t, y))
    return list_values
