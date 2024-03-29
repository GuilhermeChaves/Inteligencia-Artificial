import math
import copy

# Voce pode criar funcoes auxiliares neste arquivo
# e tambem modulos auxiliares neste pacote.
#
# Nao esqueca de renomear 'your_agent' com o nome
# do seu agente.

MAX_PROFUNDIDADE = 4

class Nodo:

    MATRIZ_PESOS = [[100, -15, 15, 8, 8, 15, -15, 100],
                    [-15, -30, -2, -2, -2, -2, -30, -15],
                    [30, -2, 10, 4, 4, 10, -2, 30],
                    [8, -2, 4, 2, 2, 4, -2, 8],
                    [8, -2, 4, 2, 2, 4, -2, 8],
                    [30, -2, 10, 4, 4, 10, -2, 30],
                    [-15, -30, -2, -2, -2, -2, -30, -15],
                    [100, -15, 15, 8, 8, 15, -15, 100]]

    def __init__(self, estado, pai, profundidade, posicao, custo):
        self.estado = estado
        self.pai = pai
        self.profundidade = profundidade
        self.posicao = posicao
        self.custo = custo


def avalia(nodo, minha_cor):
    novo_custo = 0

    if(avalia_matrix(nodo) == 100):
        novo_custo = 200
    else:
        novo_custo = avalia_num_jogadas(nodo, minha_cor) + avalia_matrix(nodo)

    return novo_custo



def avalia_matrix(nodo):
    x, y = nodo.posicao
    peso = Nodo.MATRIZ_PESOS[y][x]

    return peso



def avalia_num_jogadas(nodo, minha_cor):
    peso = 0
    
    num_jogadas = len(nodo.estado.legal_moves(minha_cor))

    if(num_jogadas <= 9):
        peso = peso + num_jogadas*10  #100 - num_jogadas*10
    else:
        peso = 100

    return peso



def valor_max(nodo, color, minha_cor, alpha_, beta_):
    l_posicoes = (nodo.estado).legal_moves(color)

    if(nodo.profundidade == MAX_PROFUNDIDADE or len(l_posicoes) == 0):
        nodo.custo = avalia(nodo, minha_cor)
        return nodo

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
        nodo.custo = avalia(nodo, minha_cor)
        return nodo

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
    raiz = Nodo(the_board, None, 0, (-1, -1), 0)
    nodo = valor_max(raiz, color, color, -math.inf, math.inf)
    
    return nodo.posicao
