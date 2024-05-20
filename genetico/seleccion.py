import random

def seleccionar_padres(poblacion, aptitudes):
    if len(poblacion) < 3:
        raise ValueError("No hay suficientes cromosomas válidos en la población.")

    padres = []
    for _ in range(len(poblacion) // 2):
        participantes = random.sample(list(zip(poblacion, aptitudes)), 3)
        ganador = min(participantes, key=lambda x: x[1])
        padres.append(ganador[0])
    return padres
