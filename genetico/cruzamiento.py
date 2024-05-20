import random

def cruzar_padres(padre1, padre2):
    min_longitud = min(len(padre1), len(padre2))
    
    # Verificar si la longitud es suficiente para seleccionar un punto de corte
    if min_longitud < 2:
        # Si uno de los padres tiene solo un segmento
        cantidad_segmentos_padre1 = len(padre1)
        cantidad_segmentos_padre2 = len(padre2)
        
        # Se elige aleatoriamente entre dos opciones: la cantidad de segmentos del padre con más de un segmento y un solo segmento
        cantidad_segmentos_hijo = random.choice([cantidad_segmentos_padre1, cantidad_segmentos_padre2])
        
        if cantidad_segmentos_hijo == 1:
            # Si el hijo tendrá un solo segmento
            if cantidad_segmentos_padre1 == 1:
                # Se elige aleatoriamente el segmento del padre2 para el hijo
                segmento_padre2 = random.choice(padre2)
                hijo1 = [segmento_padre2]
                hijo2 = padre2[:] if random.random() < 0.5 else padre1[:]
            else:
                # Se elige aleatoriamente el segmento del padre1 para el hijo
                segmento_padre1 = random.choice(padre1)
                hijo1 = padre1[:] if random.random() < 0.5 else padre2[:]
                hijo2 = [segmento_padre1]
        else:
            # Si el hijo tendrá la cantidad de segmentos del padre con más de un segmento
            if cantidad_segmentos_padre1 > 1:
                # Se elige aleatoriamente un segmento del padre1 para reemplazar en el hijo
                indice_reemplazo = random.randint(0, cantidad_segmentos_padre1 - 1)
                hijo1 = padre1[:indice_reemplazo] + [random.choice(padre2)] + padre1[indice_reemplazo + 1:]
                hijo2 = padre2[:]
            else:
                # Se elige aleatoriamente un segmento del padre2 para reemplazar en el hijo
                indice_reemplazo = random.randint(0, cantidad_segmentos_padre2 - 1)
                hijo2 = padre2[:indice_reemplazo] + [random.choice(padre1)] + padre2[indice_reemplazo + 1:]
                hijo1 = padre1[:]
        
        return hijo1, hijo2
    
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
