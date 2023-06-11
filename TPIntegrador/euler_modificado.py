def euler_modificado(t0, y0, h, f, tolerancia):
    t = t0                      # Valor inicial de la variable independiente.
    y = y0                      # Valor inicial de la variable dependiente.
    list_values = []            # Lista para almacenar los pares (t, y)

    t_f = t0 + h                # Valor final de t
    
    while t < t_f:
        k1 = f(t, y)                        # Primer término k1
        k2 = f(t + h/2, y + h/2 * k1)       # Segundo término k2
        y_pred = y + h * k2                 # Valor estimado de Y en el siguiente paso
        error = abs(y_pred - y)             # Cálculo del error absoluto

        if error < tolerancia:              # Si el error es menor que la tolerancia
            list_values.append([t, y])      # Agrega el par (t, y) a la lista
            y = y_pred                      # Actualiza el valor de y
            t = t + h                       # Actualiza el valor de t
            
        else:                               # Si el error es mayor que la tolerancia
            h = h/2                         # Reduce el tamaño del paso a la mitad
        
    return list_values



def euler_modificado_v2(f, a, b, h, y0, tol=1e-2):
    n = int((b - a) / h)    # Numero de pasos o iteraciones
    t = a                   # Valor inicial de la variable independiente.
    y = y0                  # Valor inicial de la variable dependiente.
    list_values = []        # Lista para almacenar los pares (t, y)

    for i in range(n):
        k1 = h * f(t, y)                                # 1° término k1
        k2 = h * f(t + h / 2, y + k1 / 2)               # 2° término k1
        k3 = h * f(t + h / 2, y + k2 / 2)               # 3° término k1
        k4 = h * f(t + h, y + k3)                       # 4° término k1
        
        # Calcular los estimados
        y_pred = y + (k1 + 2 * k2 + 2 * k3 + k4) / 6    #  Valor estimado de y en el siguiente paso
        y_nuevo = y + (k1 + 4 * k2 + k4) / 6            # Valor actualizado de y para el siguiente paso
        
        # Calcula el error absoluto
        error = abs(y_nuevo - y_pred)
        
        # Actualiza la solucion y el tiempo
        y = y_nuevo
        t = a + (i + 1) * h

        list_values.append([t, y])

        
        # Verifica si el error es mayor a la tolerancia
        if error > tol:
            print(f"Error exceeds the tolerance at t = {t:.2f}.")
            break   # Sale del bucle si se supera la tolerancia
    
    return list_values