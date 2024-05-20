import random
from datos.rutas import obtener_segmentos

def mutar_cromosoma(cromosoma, probabilidad_mutacion):
    nuevo_cromosoma = cromosoma.copy()
    segmentos_disponibles = obtener_segmentos()

    for i in range(len(nuevo_cromosoma)):
        if random.random() < probabilidad_mutacion:
            segmento_anterior = nuevo_cromosoma[i-1][1] if i > 0 else None
            segmento_siguiente = nuevo_cromosoma[(i+1) % len(nuevo_cromosoma)][0]

            segmentos_validos = []
            for seg in segmentos_disponibles:
                if seg not in nuevo_cromosoma:
                    conecta_anterior = seg[0] == segmento_anterior
                    conecta_siguiente = seg[1] == segmento_siguiente
                    if conecta_anterior or conecta_siguiente:
                        segmentos_validos.append(seg)

            if segmentos_validos:
                nuevo_segmento = random.choice(segmentos_validos)
                nuevo_cromosoma[i] = nuevo_segmento

    return nuevo_cromosoma
