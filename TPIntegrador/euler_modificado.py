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
            list_values.append([t, y])
            y = y_pred
            t = t + h
            
        else:
            h = h/2
        
        
    return list_values



def euler_modificado_v2(f, a, b, h, y0, tol=1e-2):
    n = int((b - a) / h)  # Number of steps
    t = a
    y = y0
    list_values = []

    for i in range(n):
        k1 = h * f(t, y)
        k2 = h * f(t + h / 2, y + k1 / 2)
        k3 = h * f(t + h / 2, y + k2 / 2)
        k4 = h * f(t + h, y + k3)
        
        # Compute the modified Euler estimates
        y_pred = y + (k1 + 2 * k2 + 2 * k3 + k4) / 6
        y_new = y + (k1 + 4 * k2 + k4) / 6
        
        # Compute the error
        error = abs(y_new - y_pred)
        
        # Update the solution and time
        y = y_new
        t = a + (i + 1) * h

        list_values.append([t, y])

        
        # Check if the error is within the tolerance
        if error > tol:
            print(f"Error exceeds the tolerance at t = {t:.2f}.")
            break
    
    return list_values