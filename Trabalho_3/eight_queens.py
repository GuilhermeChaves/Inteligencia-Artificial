from copy import copy
from random import random, randrange, sample
import matplotlib.pyplot as plt

BOARD_SIZE = 8
MAX_ATTACKS = 1000

def attack(attacker, attacked, index_attacker, index_attacked):
    upper_diagonal = attacker + (index_attacked - index_attacker)
    lower_diagonal = attacker - (index_attacked - index_attacker)

    if(attacker == attacked):
        return True
    elif (not(upper_diagonal > BOARD_SIZE)):
        if(attacked == (attacker + (index_attacked - index_attacker))):
            return True
    elif (not(lower_diagonal < 0)):
        if(attacked == (attacker - (index_attacked - index_attacker))):
            return True

    return False

def evaluate(individual):
    """
    Recebe um indivíduo (lista de inteiros) e retorna o número de ataques
    entre rainhas na configuração especificada pelo indivíduo.
    Por exemplo, no individuo [2,2,4,8,1,6,3,4], o número de ataques é 9.

    :param individual:list
    :return:int numero de ataques entre rainhas no individuo recebido
    """
    attacks = 0

    for index, queen in enumerate(individual):
        i=index+1

        while(i < BOARD_SIZE):
            if(attack(queen, individual[i], index, i)):
                attacks+=1
            i+=1

    return attacks

def tournament(participants):
    """
    Recebe uma lista com vários indivíduos e retorna o melhor deles, com relação
    ao numero de conflitos
    :param participants:list - lista de individuos
    :return:list melhor individuo da lista recebida
    """
    best_score = MAX_ATTACKS
    winner_index = 0

    for index, participant in enumerate(participants):
        if(evaluate(participant) < best_score):
            winner_index = index

    return participants[winner_index]


def crossover(parent1, parent2, index):
    """
    Realiza o crossover de um ponto: recebe dois indivíduos e o ponto de
    cruzamento (indice) a partir do qual os genes serão trocados. Retorna os
    dois indivíduos com o material genético trocado.
    Por exemplo, a chamada: crossover([2,4,7,4,8,5,5,2], [3,2,7,5,2,4,1,1], 3)
    deve retornar [2,4,7,5,2,4,1,1], [3,2,7,4,8,5,5,2].
    A ordem dos dois indivíduos retornados não é importante
    (o retorno [3,2,7,4,8,5,5,2], [2,4,7,5,2,4,1,1] também está correto).
    :param parent1:list
    :param parent2:list
    :param index:int
    :return:list,list
    """
    temp_list = parent2
    parent2 = parent2[0 : index] + parent1[index : BOARD_SIZE]
    parent1 = parent1[0 : index] + temp_list[index : BOARD_SIZE]

    return parent1, parent2


def mutate(individual, m):
    """
    Recebe um indivíduo e a probabilidade de mutação (m).
    Caso random() < m, sorteia uma posição aleatória do indivíduo e
    coloca nela um número aleatório entre 1 e 8 (inclusive).
    :param individual:list
    :param m:float - probabilidade de mutacao
    :return:list - individuo apos mutacao (ou intacto, caso a prob. de mutacao nao seja satisfeita)
    """
    new_individual = copy(individual)

    if (random() < m):
        while(new_individual == individual):
            new_individual[randrange(8)] = randrange(1,9)

    return new_individual

def random_chromosome():
    """Gera um cromossomo aleatório."""
    chromosome = []
    possible_values = set((range(1, 8)))

    for _ in range(8):
        gene = sample(possible_values, 1)[0]
        chromosome.append(gene)

    return chromosome


def random_population(population_size):
    """Gera populações aleatórias de tamanho `population_size`."""
    population = []

    for _ in range(population_size):
        found = False

        while not found:
            candidate = random_chromosome()
            if not chromosome_exists(candidate, population):
                population.append(candidate)
                found = True

    return population

def chromosome_exists(chromosome, population):
    """Verifica se um dado cromossomo já existe em uma dada população."""
    for existing_chromosome in population:
        if chromosome == existing_chromosome:
            return True
    return False

all_generations = []
def run_ga(g, n, k, m, e):
    """
    Executa o algoritmo genético e retorna o indivíduo com o menor número de ataques entre rainhas
    :param g:int - numero de gerações
    :param n:int - numero de individuos
    :param k:int - numero de participantes do torneio
    :param m:float - probabilidade de mutação (entre 0 e 1, inclusive)
    :param e:bool - se vai haver elitismo
    :return:list - melhor individuo encontrado
    """
    # Inicializa a população
    current_population = random_population(n)
    # print(f"População inicial: {current_population}")

    # Roda o algoritmo genético
    for generation in range(g):
        # Aplicação de elitismo
        if e:
            new_population = [tournament(current_population)]
        else:
            new_population = []

        while len(new_population) < n:
            # Seleção de indivíduos
            sample_population_1 = sample(current_population, k)
            sample_population_2 = sample(current_population, k)

            # Torneio
            p1, p2 = tournament(sample_population_1), tournament(sample_population_2)

            p1x, p2x = crossover(p1, p2, randrange(BOARD_SIZE))
            p1m = mutate(p1x, m)
            p2m = mutate(p2x, m)

            if not chromosome_exists(p1m, new_population):
                new_population.append(p1m)
            if not chromosome_exists(p2m, new_population):
                new_population.append(p2m)

        current_population = new_population
        best = tournament(current_population)
        all_generations.append(evaluate(best))

        # print(f"Generation {generation}: {evaluate(best)}")

run_ga(400, 200, 4, 0.1, False)
# plot all generations
plt.plot(all_generations)
plt.show()

