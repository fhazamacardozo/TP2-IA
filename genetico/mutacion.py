import random
from datos.rutas import obtener_segmentos

def mutar_cromosoma(cromosoma, probabilidad_mutacion):
    nuevo_cromosoma = cromosoma.copy()
    segmentos_disponibles = obtener_segmentos()

    for i in range(len(nuevo_cromosoma)):
        if random.random() < probabilidad_mutacion:
            segmentos_validos = [
                seg for seg in segmentos_disponibles
                if seg not in nuevo_cromosoma and (seg[0] == nuevo_cromosoma[i-1][1] or seg[1] == nuevo_cromosoma[(i+1) % len(nuevo_cromosoma)][0])
            ]
            if segmentos_validos:
                nuevo_segmento = random.choice(segmentos_validos)
                nuevo_cromosoma[i] = nuevo_segmento
    
    return nuevo_cromosoma
