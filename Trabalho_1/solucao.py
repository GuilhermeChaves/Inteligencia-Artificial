import numpy

class Nodo:

    def __init__(self, estado, pai, acao, custo):

        self.estado = estado
        self.pai = pai
        self.acao = acao
        self.custo = custo



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
            return calcula_caminho(nodos[-1])
    
        if(explorados.get(nodos[-1].estado)):
            continue

        explorados[nodos[-1].estado] = nodos[-1]

        fronteira.extend(expande(nodos[-1]))



def astar_hamming(estado):
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Hamming e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError



def astar_manhattan(estado):
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Manhattan e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError
