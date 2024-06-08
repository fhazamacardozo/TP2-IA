from genetico.cromosoma import generar_poblacion_inicial
from genetico.evaluacion import evaluar_poblacion
from genetico.seleccion import seleccionar_padres
from genetico.cruzamiento import cruzar_padres
from genetico.mutacion import mutar_cromosoma
from genetico.evaluacion import mostrar_top_10
import random
import matplotlib.pyplot as plt

def ejecutar_algoritmo(tamano_poblacion, num_generaciones, probabilidad_cruzamiento, probabilidad_mutacion, origen, destino):
    # Generar población inicial
    poblacion = generar_poblacion_inicial(tamano_poblacion, origen, destino)
    print("Individuos poblacion inicial: ", len(poblacion))
    
    # Inicializar listas para almacenar las aptitudes
    aptitud_promedio = []
    aptitud_mejor = []
    
    for generacion in range(num_generaciones):
        # Evaluar la población y obtener la población válida y sus aptitudes
        poblacion_valida, aptitudes, cantidad_individuos_unicos = evaluar_poblacion(poblacion,origen,destino)
        print(f"Generacion {generacion} - Cantidad de individuos validos: {len(poblacion_valida)} - Cantidad de unicos: {cantidad_individuos_unicos}")

        if len(poblacion_valida) < 3:
            print(f"No hay suficientes cromosomas válidos en la generación {generacion}. Re-generando población.")
            poblacion = generar_poblacion_inicial(tamano_poblacion, origen, destino)
            continue
        
        # Extraer solo los costos totales de las aptitudes
        solo_aptitudes = [aptitud[0] for aptitud in aptitudes]
        
        # Registrar aptitudes promedio y mejor
        promedio = sum(solo_aptitudes) / len(solo_aptitudes)
        mejor = min(solo_aptitudes)
        aptitud_promedio.append(promedio)
        aptitud_mejor.append(mejor)
        
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
    poblacion_valida, aptitudes, cantidad_individuos_unicos = evaluar_poblacion(poblacion,origen,destino)
    if not poblacion_valida:
        print("No se encontró una solución válida.")
        return

    print(f"Generacion {num_generaciones} - Cantidad de individuos validos: {len(poblacion_valida)} - Cantidad de unicos: {cantidad_individuos_unicos}")

    mostrar_top_10(poblacion_valida)
    
    # Generar el gráfico
    plt.plot(range(num_generaciones), aptitud_promedio, label='Aptitud Promedio')
    plt.plot(range(num_generaciones), aptitud_mejor, label='Aptitud Mejor')
    plt.xlabel('Generación')
    plt.ylabel('Aptitud')
    plt.title('Comportamiento General de la Función de Aptitud')
    plt.legend()
    plt.show()

    