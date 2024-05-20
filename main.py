from genetico.algoritmo import ejecutar_algoritmo
import config

if __name__ == "__main__":
    ejecutar_algoritmo(
        config.tamano_poblacion,config.num_generaciones,config.probabilidad_cruzamiento,
        config.probabilidad_mutacion,config.origen,config.destino)