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

    MATRIZ_PESOS = [[100, -15, 15, 8, 8, 15, -15, 100],
                    [-15, -30, -2, -2, -2, -2, -30, -15],
                    [30, -2, 10, 4, 4, 10, -2, 30],
                    [8, -2, 4, 2, 2, 4, -2, 8],
                    [8, -2, 4, 2, 2, 4, -2, 8],
                    [30, -2, 10, 4, 4, 10, -2, 30],
                    [-15, -30, -2, -2, -2, -2, -30, -15],
                    [100, -15, 15, 8, 8, 15, -15, 100]]
    
    
    '''
    MATRIZ_PESOS = [[100, 0, 50, 30, 30, 50, 0, 100],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [50, 0, 20, 10, 10, 20, 0, 50],
                    [30, 0, 10, 5, 5, 10, 0, 30],
                    [30, 0, 10, 5, 5, 10, 0, 30],
                    [50, 0, 20, 10, 10, 20, 0, 50],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [100, 0, 50, 30, 30, 50, 0, 100]]
    '''                
    

    def __init__(self, estado, pai, profundidade, posicao, custo):
        self.estado = estado
        self.pai = pai
        self.profundidade = profundidade
        self.posicao = posicao
        self.custo = custo


def avalia(nodo, minha_cor):
    nodo.custo = avalia_num_jogadas(nodo, minha_cor) + avalia_matrix(nodo);

    return nodo



def avalia_matrix(nodo):
    x, y = nodo.posicao
    peso = Nodo.MATRIZ_PESOS[y][x]

    return peso



def avalia_num_jogadas(nodo, minha_cor):
    peso = 0
    
    if(minha_cor == 'B'):
        cor_inimiga = 'W'
    elif(minha_cor == 'W'):
        cor_inimiga = 'B'

    num_jogadas = len(nodo.estado.legal_moves(minha_cor))

    if(num_jogadas <= 9):
        peso = peso + num_jogadas*10  #100 - num_jogadas*10
    else:
        peso = 100

    return peso


def avalia_num_jogadas_inimigas(nodo, minha_cor):
    peso = 0
    
    if(minha_cor == 'B'):
        cor_inimiga = 'W'
    elif(minha_cor == 'W'):
        cor_inimiga = 'B'

    num_jogadas = len(nodo.estado.legal_moves(cor_inimiga))

    if(num_jogadas <= 9):
        peso = 100 - num_jogadas*10
    else:
        peso = 0

    return peso



def valor_max(nodo, color, minha_cor, alpha_, beta_):
    l_posicoes = (nodo.estado).legal_moves(color)

    if(nodo.profundidade == 4 or len(l_posicoes) == 0):
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

    if(nodo.profundidade == 4 or len(l_posicoes) == 0):
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
