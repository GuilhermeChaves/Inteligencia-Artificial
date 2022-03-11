Gabriel Lima Chimifosk - 00134078 - Turma B \
Guilherme Sonaglio Chaves - 00285686 - Turma B \
Tiago de Carvalho Magnus - 00287710 - Turma B

As bibliotecas utilizadas são comuns ao ambiente python: math e copy.

# Bibilotecas instaladas

# Descrição
O programa possui uma implementação do algoritmo Minimax com poda alfa-beta para o jogo Othello. Possui duas funções de avaliação, e é feita uma soma do resultado de ambas para conseguir uma estimativa da melhor jogada.

## Função de avaliação
A função de avaliação utiliza uma soma de pesos que leva em consideração a quantidade de jogadas possíveis naquele estado e o quão benéfica é a posição, por meio de uma matriz pré-estabelecida de pesos para cada casa do tabuleiro.

## Estratégia de parada
Além de checar se já foram esgotadas todas as possibilidades de jogadas válidas, é feita uma verificação de profundidade máxima fixa.

## Possíveis melhorias
Poderia ser implementada uma verificação do quão benéfica é a posição do tabuleiro de forma mais precisa, variando conforme o estado do jogo muda, além de utilizar outros algoritmos e técnicas mais avançadas, como mapeamento de aberturas. As jogadas estão sendo feitas de forma rápida, então, para a estratégia de parada, poderia ser utilizada alguma outra verificação de modo que a profundidade máxima pudesse ser maior, como um limite de tempo de execução, por exemplo.

## Dificuldades encontradas
As dificuldades encontradas são relacionadas principalmente à sintaxe da linguagem Python.

# Bibliografia