def validar_cromosoma(cromosoma,origen,destino):
    # Verificar que el cromosoma tenga al menos un segmento
    if len(cromosoma) < 1:
        return False
    
    # Verificar que el origen y el destino del primer y último segmento sean válidos
    if cromosoma[0][0] != origen or cromosoma[-1][1] != destino:
        return False
    
    # Verificar que no haya segmentos repetidos
    if len(set(cromosoma)) != len(cromosoma):
        return False
    
    # Verificar que el camino sea coherente
    ciudades_visitadas = [cromosoma[0][0]]
    for i in range(len(cromosoma)):
        # Verificar que la ciudad de origen del segmento actual sea igual a la ciudad de destino del segmento anterior
        if cromosoma[i][0] != ciudades_visitadas[-1]:
            return False
        # Agregar la ciudad de destino del segmento actual a la lista de ciudades visitadas
        ciudades_visitadas.append(cromosoma[i][1])
    
    return True

def evaluar_cromosoma(cromosoma):
    precio_hora_conductor = 100  # Costo por hora de trabajo del conductor en pesos
    precio_litro_combustible = 150  # Precio por litro de combustible en pesos
    autonomia_vehiculo = 10  # Autonomía del vehículo en km/l

    tiempo_total = sum(segmento[2] for segmento in cromosoma)
    distancia_total = sum(segmento[3] for segmento in cromosoma)
    peajes_total = sum(segmento[4] for segmento in cromosoma)

    costo_combustible = (distancia_total / autonomia_vehiculo) * precio_litro_combustible  # Costo de combustible
    costo_horas_conductor = (tiempo_total / 60) * precio_hora_conductor  # Costo de las horas de trabajo del conductor

    costo_total = costo_combustible + costo_horas_conductor + peajes_total

    return costo_total

def evaluar_poblacion(poblacion,origen,destino):
    # Filtrar cromosomas válidos y evaluar solo los válidos
    poblacion_valida = [individuo for individuo in poblacion if validar_cromosoma(individuo,origen,destino)]
    aptitudes = [evaluar_cromosoma(individuo) for individuo in poblacion_valida]
    return poblacion_valida, aptitudes
