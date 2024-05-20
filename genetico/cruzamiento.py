import random

def cruzar_padres(padre1, padre2):
    min_longitud = min(len(padre1), len(padre2))
    
    # Verificar si la longitud es suficiente para seleccionar un punto de corte
    if min_longitud < 2:
        raise ValueError("Longitud de los padres insuficiente para realizar el cruzamiento")
    
    # Seleccionar un punto de corte válido
    punto_corte = random.randint(1, min_longitud - 1)
    
    hijo1 = []
    hijo2 = []
    
    # Parte inicial del hijo obtenida del primer padre
    hijo1.extend(padre1[:punto_corte])
    hijo2.extend(padre2[:punto_corte])
    
    # Completa el hijo con las ciudades del segundo padre que no estén ya en el hijo
    for ciudad in padre2[punto_corte:]:
        if ciudad not in hijo1:
            hijo1.append(ciudad)
    for ciudad in padre1[punto_corte:]:
        if ciudad not in hijo2:
            hijo2.append(ciudad)
    
    return hijo1, hijo2
