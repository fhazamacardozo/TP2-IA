import random
from datos.rutas import obtener_segmentos

import random
from datos.rutas import obtener_segmentos

def generar_poblacion_inicial(tamano_poblacion, origen, destino):
    poblacion = []
    intentos = 0  # Para evitar un bucle infinito en caso de que no se puedan generar más cromosomas únicos

    while len(poblacion) < tamano_poblacion and intentos < tamano_poblacion * 10:
        cromosoma = generar_cromosoma_aleatorio(origen, destino)
        if cromosoma and cromosoma not in poblacion:
            poblacion.append(cromosoma)
        intentos += 1

    return poblacion

def generar_cromosoma_aleatorio(origen, destino):
    # Obtenemos todos los segmentos posibles
    segmentos = obtener_segmentos()
    # Lista para almacenar las ciudades visitadas en orden
    ciudades_visitadas = [origen]  # Añadimos la ciudad de origen al inicio
    # Lista para almacenar los segmentos que formarán el cromosoma
    cromosoma = []

    # Comenzamos desde la ciudad de origen
    ciudad_actual = origen

    # Avanzamos hasta llegar a la ciudad de destino
    while ciudad_actual != destino:
        # Filtramos los segmentos que parten desde la ciudad actual y van a ciudades no visitadas
        posibles_segmentos = [seg for seg in segmentos if seg[0] == ciudad_actual and seg[1] not in ciudades_visitadas]
        # Si no hay segmentos disponibles, no se puede continuar con una ruta válida
        if not posibles_segmentos:
            return None  
        # Elegimos aleatoriamente un segmento de los posibles, pero fomentamos la variación
        segmento_actual = random.choice(posibles_segmentos)
        # Agregamos el segmento al cromosoma
        cromosoma.append(segmento_actual)
        # Marcamos la ciudad de destino del segmento como visitada
        ciudades_visitadas.append(segmento_actual[1])
        # La ciudad actual ahora es la ciudad de destino del segmento
        ciudad_actual = segmento_actual[1]
    return cromosoma

#Version menos restrictiva
def generar_cromosoma_aleatorio1(origen, destino):
    segmentos = obtener_segmentos()
    ciudades_visitadas = [origen]
    cromosoma = []

    ciudad_actual = origen

    while ciudad_actual != destino:
        posibles_segmentos = [seg for seg in segmentos if seg[0] == ciudad_actual]
        if not posibles_segmentos:
            return None

        # Seleccionar un segmento aleatorio
        segmento_actual = random.choice(posibles_segmentos)
        
        # Agregar el segmento al cromosoma
        cromosoma.append(segmento_actual)
        
        # Marcar la ciudad de destino del segmento como visitada
        ciudades_visitadas.append(segmento_actual[1])
        
        # La ciudad actual ahora es la ciudad de destino del segmento
        ciudad_actual = segmento_actual[1]

    return cromosoma


