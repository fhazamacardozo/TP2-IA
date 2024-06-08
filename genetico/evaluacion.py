
from config import datos_vehiculo
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
    precio_hora_conductor = datos_vehiculo['precio_hora_conductor']  # Costo por hora de trabajo del conductor en pesos
    precio_litro_combustible = datos_vehiculo['precio_litro_combustible']  # Precio por litro de combustible en pesos
    autonomia_vehiculo = datos_vehiculo['autonomia_vehiculo']  # Autonomía del vehículo en km/l

    tiempo_total = sum(segmento[2] for segmento in cromosoma)
    distancia_total = sum(segmento[3] for segmento in cromosoma)
    peajes_total = sum(segmento[4] for segmento in cromosoma)

    costo_combustible = (distancia_total / autonomia_vehiculo) * precio_litro_combustible  # Costo de combustible
    costo_horas_conductor = (tiempo_total / 60) * precio_hora_conductor  # Costo de las horas de trabajo del conductor

    costo_total = costo_combustible + costo_horas_conductor + peajes_total

    return costo_total, tiempo_total, distancia_total

def evaluar_poblacion(poblacion, origen, destino):
    poblacion_valida = []
    individuos_unicos = set()

    for individuo in poblacion:
        if validar_cromosoma(individuo, origen, destino):
            # Si el individuo es válido, lo agregamos a la población válida
            poblacion_valida.append(individuo)
            # Agregamos el individuo al conjunto de individuos únicos
            individuos_unicos.add(tuple(individuo))

    # Convertimos la población válida de nuevo a lista
    poblacion_valida = list(poblacion_valida)

    # Calculamos la cantidad de individuos únicos
    cantidad_individuos_unicos = len(individuos_unicos)

    # Evaluamos los cromosomas válidos y devolvemos la población válida y la cantidad de individuos únicos
    aptitudes = [evaluar_cromosoma(individuo) for individuo in poblacion_valida]
    return poblacion_valida, aptitudes, cantidad_individuos_unicos


def mostrar_top_10(poblacion):
    # Evaluar cada cromosoma de la población
    evaluaciones = [(cromosoma, *evaluar_cromosoma(cromosoma)) for cromosoma in poblacion]
    
    # Ordenar la población por costo total (aptitud)
    evaluaciones_ordenadas = sorted(evaluaciones, key=lambda x: x[1])

    print("\nTop 10 de la población:")
    
    # Utilizar un conjunto para almacenar cromosomas únicos
    cromosomas_vistos = set()
    
    for i, (cromosoma, costo_total, tiempo_total, distancia_total) in enumerate(evaluaciones_ordenadas[:10]):
        # Convertir tiempo total de minutos a horas y minutos
        horas = int(tiempo_total // 60)
        minutos = int(tiempo_total % 60)
        ruta = ' -> '.join([segmento[0] for segmento in cromosoma] + [cromosoma[-1][1]])
        
        # Si el cromosoma ya ha sido visto, continuar con el siguiente
        if tuple(cromosoma) in cromosomas_vistos:
            continue
        
        # Agregar el cromosoma al conjunto de cromosomas vistos
        cromosomas_vistos.add(tuple(cromosoma))
        
        print(f"\nIndividuo {i + 1}:")
        print(f"  Costo total: {costo_total:.2f}")
        print(f"  Ruta: {ruta}")
        print(f"  Tiempo total: {horas} horas {minutos} minutos")
        print(f"  Distancia total: {distancia_total:.2f} km")
        print( "  Cromosoma crudo: ",cromosoma)
        
        if len(cromosomas_vistos) == 10:
            break

