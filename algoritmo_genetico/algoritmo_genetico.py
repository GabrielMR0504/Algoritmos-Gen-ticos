import random
import math
from func import cruzamento_ponto_unico

def funcao_bird(x, y):
    termo_1 = math.sin(x) * math.exp((1 - math.cos(y))**2)
    termo_2 = math.cos(y) * math.exp((1 - math.sin(x))**2)
    termo_3 = (x - y)**2
    return termo_1 + termo_2 + termo_3

def avaliar(individuo):
    x, y = individuo
    return funcao_bird(x, y)

def inicializar_populacao(tamanho_populacao, x_faixa, y_faixa):
    populacao = []
    for _ in range(tamanho_populacao):
        x = random.uniform(x_faixa[0], x_faixa[1])
        y = random.uniform(y_faixa[0], y_faixa[1])
        populacao.append([x, y])
    return populacao

def selecionar_pais(populacao, num_pais):
    # Use seleção de torneio simples
    pais = []
    while len(pais) < num_pais:
        torneio = random.sample(populacao, 3)  # Torneio com 3 indivíduos
        torneio.sort(key=avaliar)
        melhor = torneio[0]
        pais.append(melhor)
    return pais

def cruzamento(pais, kwargs):
    filhos = []
    for i in range(kwargs['tamanho_populacao'] - kwargs['num_pais']):
        pai1 = pais[i % kwargs['num_pais']]
        pai2 = pais[(i + 1) % kwargs['num_pais']]
        filho1, filho2 = cruzamento_ponto_unico(pai1, pai2)
        filhos.extend([filho1, filho2])
    return filhos

def mutacao(individuo, kwargs):
    x, y = individuo
    if random.random() < kwargs['taxa_mutacao']:
        x += random.uniform(-0.1, 0.1)
        x = max(min(x, kwargs['x_faixa'][1]), kwargs['x_faixa'][0])
    if random.random() < kwargs['taxa_mutacao']:
        y += random.uniform(-0.1, 0.1)
        y = max(min(y, kwargs['y_faixa'][1]), kwargs['y_faixa'][0])
    return [x, y]

def exec_algoritmo_genetico(**kwargs):
    populacao = inicializar_populacao(kwargs['tamanho_populacao'], kwargs['x_faixa'], kwargs['y_faixa'])

    for geracao in range(kwargs['num_geracoes']):

        populacao.sort(key=avaliar)
        melhor_individuo = populacao[0]
        melhor_fitness = avaliar(melhor_individuo)

        print(f"Geração {geracao}: Melhor valor = {melhor_fitness}, Melhor indivíduo = {melhor_individuo}")

        pais = selecionar_pais(populacao, kwargs['num_pais'])
        filhos = cruzamento(pais, kwargs)
        filhos = [mutacao(filho, kwargs) for filho in filhos]

        populacao = pais + filhos

    print("\nMelhor resultado encontrado:")
    print(f"Melhor valor = {melhor_fitness}, Melhor indivíduo = {melhor_individuo}")


if __name__ == "__main__":
    exec_algoritmo_genetico(
        tamanho_populacao = 100, 
        num_geracoes = 100,
        num_pais = 50,
        taxa_mutacao = 0.1,
        x_faixa = (-10, 10),
        y_faixa = (-10, 10)
    )
    



