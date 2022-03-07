import random
import math
import sys
import copy

# Voce pode criar funcoes auxiliares neste arquivo
# e tambem modulos auxiliares neste pacote.
#
# Nao esqueca de renomear 'your_agent' com o nome
# do seu agente.

class Nodo:
    def __init__(self, estado, pai, profundidade, posicao, custo):
        self.estado = estado
        self.pai = pai
        self.profundidade = profundidade
        self.posicao = posicao
        self.custo = custo



def avalia(nodo, minha_cor):
    
    num_jogadas = len(nodo.estado.legal_moves(minha_cor))

    if(num_jogadas == 0):
        nodo.custo = 50
    else:
        nodo.custo = num_jogadas

    return nodo




def valor_max(nodo, color, minha_cor, alpha_, beta_):

    l_posicoes = (nodo.estado).legal_moves(color)
    
    if(nodo.profundidade == 5 or len(l_posicoes) == 0):
        return avalia(nodo, minha_cor)

    v_beta = copy.deepcopy(beta_)
    v = -math.inf

    nodos_filhos = list()

    if(color == 'B'):
        prox_cor = 'W'
    elif(color == 'W'):
        prox_cor = 'B'

    for pos in l_posicoes:
        estado = copy.deepcopy(nodo.estado)
        estado.process_move(pos, color)       
        nodos_filhos.append(Nodo(estado, nodo, nodo.profundidade+1, pos,  0))
        v = max(v, valor_min(nodos_filhos[-1], prox_cor, minha_cor, alpha_, v_beta).custo)
        alpha_ = max(alpha_, v)

        if(alpha_ > v and nodo.profundidade == 0):
            nodos_filhos[-1].posicao = pos

        if(alpha_ >= beta_):
            break 
  
    return nodos_filhos[-1]   



def valor_min(nodo, color, minha_cor, alpha_, beta_):

    l_posicoes = (nodo.estado).legal_moves(color)
    
    if(nodo.profundidade == 5 or len(l_posicoes) == 0):
        return avalia(nodo, minha_cor)

    v_alpha = copy.deepcopy(alpha_)
    v = math.inf

    nodos_filhos = list()

    if(color == 'B'):
        prox_cor = 'W'
    elif(color == 'W'):
        prox_cor = 'B'

    for pos in l_posicoes:
        estado = copy.deepcopy(nodo.estado)
        estado.process_move(pos, color)       
        nodos_filhos.append(Nodo(estado, nodo, nodo.profundidade+1, pos,  0))
        v = min(v, valor_max(nodos_filhos[-1], prox_cor, minha_cor, v_alpha, beta_).custo)
        beta_ = min(beta_, v)

        if(beta_ < v and nodo.profundidade == 0):
            nodos_filhos[-1].posicao = pos

        if(beta_ <= alpha_):
            break 
        
    return nodos_filhos[-1]



def make_move(the_board, color):
    """
    Returns an Othello move
    :param the_board: a board.Board object with the current game state
    :param color: a character indicating the color to make the move ('B' or 'W')
    :return: (int, int) tuple with x, y indexes of the move (remember: 0 is the first row/column)
    """
    # o codigo abaixo apenas retorna um movimento aleatorio valido para
    # a primeira jogada com as pretas.
    # Remova-o e coloque a sua implementacao da poda alpha-beta
    #return random.choice([(2, 3), (4, 5), (5, 4), (3, 2)])
    raiz = Nodo(the_board, None, 0, (-1, -1), 0)
    nodo = valor_max(raiz, color, color, -math.inf, math.inf)
    #l_legal_move = (raiz.estado).legal_moves(color)
    #print(l_legal_move)
    #return(-1,-1)
    return nodo.posicao

