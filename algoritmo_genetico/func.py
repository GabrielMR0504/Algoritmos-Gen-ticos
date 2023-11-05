import random

def cruzamento_medio(pais):
    x_media = sum([p[0] for p in pais]) / len(pais)
    y_media = sum([p[1] for p in pais]) / len(pais)
    return [x_media, y_media]

def cruzamento_ponto_unico(parent1, parent2):
    crossover_point = random.randint(0, 1)
    child1 = [parent1[0], parent2[1]] if crossover_point == 0 else [parent2[0], parent1[1]]
    child2 = [parent1[0], parent2[1]] if crossover_point == 0 else [parent2[0], parent1[1]]
    return child1, child2