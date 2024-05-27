from genetico.cromosoma import generar_poblacion_inicial
from genetico.evaluacion import evaluar_poblacion
from genetico.seleccion import seleccionar_padres
from genetico.cruzamiento import cruzar_padres
from genetico.mutacion import mutar_cromosoma
import random

def ejecutar_algoritmo(tamano_poblacion, num_generaciones, probabilidad_cruzamiento, probabilidad_mutacion, origen, destino):
    # Generar población inicial
    poblacion = generar_poblacion_inicial(tamano_poblacion, origen, destino)
    for generacion in range(num_generaciones):
        # Evaluar la población y obtener la población válida y sus aptitudes
        poblacion_valida, aptitudes = evaluar_poblacion(poblacion,origen,destino)
        print(f"Generacion {generacion} - Cantidad de individuos validos: {len(poblacion_valida)}")

        if len(poblacion_valida) < 3:
            print(f"No hay suficientes cromosomas válidos en la generación {generacion}. Re-generando población.")
            poblacion = generar_poblacion_inicial(tamano_poblacion, origen, destino)
            continue

        # Seleccionar padres por torneo, no se si esto esta demas, con el filtro de la evaluacion alcanza
        padres = seleccionar_padres(poblacion_valida, aptitudes)
        # Cruzamiento
        nueva_poblacion = []
        while len(nueva_poblacion) < tamano_poblacion:
            if random.random() < probabilidad_cruzamiento:
                padre1, padre2 = random.sample(padres, 2)
                hijo1, hijo2 = cruzar_padres(padre1, padre2)
                nueva_poblacion.append(hijo1)
                if len(nueva_poblacion) < tamano_poblacion:
                    nueva_poblacion.append(hijo2)
            else:
                nueva_poblacion.extend(random.sample(padres, 2))

        # Mutación
        nueva_poblacion = [mutar_cromosoma(individuo, probabilidad_mutacion) for individuo in nueva_poblacion]

        # Actualizar población
        poblacion = nueva_poblacion

    # Evaluar la población final
    poblacion_valida, aptitudes = evaluar_poblacion(poblacion,origen,destino)
    if not poblacion_valida:
        print("No se encontró una solución válida.")
        return
    
    mejor_individuo = poblacion_valida[aptitudes.index(min(aptitudes))]
    mejor_aptitud = min(aptitudes)
    tiempo_total_minutos = sum(segmento[2] for segmento in mejor_individuo)  # Asumiendo que el tiempo es el tercer elemento de cada segmento

    # Convertir tiempo total a horas y minutos
    horas = tiempo_total_minutos // 60
    minutos = tiempo_total_minutos % 60

    ruta = [origen] + [segmento[1] for segmento in mejor_individuo]
    print("Mejor ruta encontrada:", ruta)
    print("Costo total:", mejor_aptitud)
    print(f"Tiempo total del recorrido: {horas} horas y {minutos} minutos")

    