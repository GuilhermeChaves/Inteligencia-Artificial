import numpy
import heapq

class Nodo:
    def __init__(self, estado, pai, acao, custo):
        self.estado = estado
        self.pai = pai
        self.acao = acao
        self.custo = custo
        self.custo_astar = 0



    def __lt__(self, other):
        return self.custo_astar < other.custo_astar



def sucessor(estado):
    l_sucessores = list()
    l_proximo_estado = list(estado)

    pos = estado.index('_')

    if (pos <= 5):
        l_proximo_estado[pos] = l_proximo_estado[pos+3]
        l_proximo_estado[pos+3] = '_'
        proximo_estado = ''.join(l_proximo_estado)  #transforma list em string
        l_sucessores.append(("abaixo", proximo_estado))
        l_proximo_estado = list(estado)             #retorna ao estado inicial

    if(pos >= 3):
        l_proximo_estado[pos] = l_proximo_estado[pos-3]
        l_proximo_estado[pos-3] = '_'
        proximo_estado = ''.join(l_proximo_estado)
        l_sucessores.append(("acima", proximo_estado))
        l_proximo_estado = list(estado)

    if(pos != 0 and pos != 3 and pos != 6):
        l_proximo_estado[pos] = l_proximo_estado[pos-1]
        l_proximo_estado[pos-1] = '_'
        proximo_estado = ''.join(l_proximo_estado)
        l_sucessores.append(("esquerda", proximo_estado))
        l_proximo_estado = list(estado)

    if(pos != 2 and pos != 5 and pos != 8):
        l_proximo_estado[pos] = l_proximo_estado[pos+1]
        l_proximo_estado[pos+1] = '_'
        proximo_estado = ''.join(l_proximo_estado)
        l_sucessores.append(("direita", proximo_estado))

    return l_sucessores



def expande(nodo):
    l_sucessores = sucessor(nodo.estado)

    size_array = len(l_sucessores)
    array_nodos = numpy.empty(size_array, dtype=Nodo)    # inicializa vetor de nodos

    for i in range(size_array):
        s_acao, s_estado = l_sucessores[i]
        array_nodos[i] = Nodo(s_estado , nodo, s_acao, nodo.custo + 1)

    return array_nodos



def calcula_caminho(nodo):
    caminho = list()

    while(nodo.pai != None):
        caminho.append(nodo.acao)
        nodo = nodo.pai

    caminho = list(reversed(caminho))

    return caminho



def bfs(estado):
    explorados = {}    # explorados["estado"] = Nodo
    fronteira = list()
    nodos = list()

    fronteira.append(Nodo(estado, None, None, 0))

    while(True):
        if(len(fronteira) == 0):
            return None

        nodos.append(fronteira.pop(0))

        if(nodos[-1].estado == "12345678_"):
            return calcula_caminho(nodos[-1])

        if(explorados.get(nodos[-1].estado)):
            continue

        explorados[nodos[-1].estado] = nodos[-1]

        fronteira.extend(expande(nodos[-1]))



def dfs(estado):
    explorados = {}    # explorados["estado"] = Nodo
    fronteira = list()
    nodos = list()

    fronteira.append(Nodo(estado, None, None, 0))

    while(True):
        if(len(fronteira) == 0):
            return None

        nodos.append(fronteira.pop())

        if(nodos[-1].estado == "12345678_"):
            print(nodos[-1].custo)
            print(len(explorados))
            return calcula_caminho(nodos[-1])

        if(explorados.get(nodos[-1].estado)):
            continue

        explorados[nodos[-1].estado] = nodos[-1]

        fronteira.extend(expande(nodos[-1]))



def h_hamming(estado):
    l_objetivo = list("12345678_")
    l_estado = list(estado)
    l_comparativa = zip(l_estado, l_objetivo)
    distancia = 0

    for i, j in l_comparativa:
        if i != j:
            distancia += 1

    return distancia



def astar_hamming(estado):
    explorados = {}    # explorados["estado"] = Nodo
    fronteira = []
    nodos = list()
    expansao = list()

    heapq.heappush(fronteira, Nodo(estado, None, None, 0))

    while(True):
        if(len(fronteira) == 0):
            return None

        nodos.append(heapq.heappop(fronteira))

        if(nodos[-1].estado == "12345678_"):
            return calcula_caminho(nodos[-1])

        if(explorados.get(nodos[-1].estado)):
            continue

        explorados[nodos[-1].estado] = nodos[-1]

        expansao = expande(nodos[-1])
        
        for nodo in expansao:
            setattr(nodo, "custo_astar", nodo.custo + h_hamming(nodo.estado))
            heapq.heappush(fronteira, nodo)



def get_pos_manhattan(index, str_num):
    x = index%3
    y = int(index/3)

    return (str_num,x,y)



def h_manhattan(estado):
    distancia = 0

    l_estado = list(estado)
    l_objetivo = [('1',0,0), ('2',1,0), ('3',2,0), ('4',0,1), ('5',1,1), ('6',1,2), ('7',0,2), ('8',1,2), ('_',2,2)]

    for index, estado_individual in enumerate(l_estado):
        estado_mapeado = get_pos_manhattan(index, estado_individual)

        if(estado_mapeado[0] != l_objetivo[index][0]):
            x_atual = estado_mapeado[1]
            y_atual = estado_mapeado[2]

            if(estado_mapeado[0] == '_'):
                index_objetivo = 8
            else:
                index_objetivo = int(estado_mapeado[0]) - 1
            x_objetivo = l_objetivo[index_objetivo][1]        
            y_objetivo = l_objetivo[index_objetivo][2]

            distancia_individual = abs(x_atual-x_objetivo) + abs(y_atual - y_objetivo)
            distancia += distancia_individual

    return distancia



def astar_manhattan(estado):
    explorados = {}    # explorados["estado"] = Nodo
    fronteira = []
    nodos = list()
    expansao = list()

    heapq.heappush(fronteira, Nodo(estado, None, None, 0))

    while(True):
        if(len(fronteira) == 0):
            return None

        nodos.append(heapq.heappop(fronteira))

        if(nodos[-1].estado == "12345678_"):
            return calcula_caminho(nodos[-1])

        if(explorados.get(nodos[-1].estado)):
            continue

        explorados[nodos[-1].estado] = nodos[-1]

        expansao = expande(nodos[-1])
        
        for nodo in expansao:
            setattr(nodo, "custo_astar", nodo.custo + h_manhattan(nodo.estado))
            heapq.heappush(fronteira, nodo)
   
