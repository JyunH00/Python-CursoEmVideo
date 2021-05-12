'''
Exercício 91: Crie um programa onde 4 jogadores joguem um dado e tenha resultados aleatórios. Guarde esses resultados em
um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número do dado.
'''


# Resolução #

from random import randint
from time import sleep

# Variáveis #

jogadores = {'jogador1': randint(1, 6),
             'jogador2': randint(1, 6),
             'jogador3': randint(1, 6),
             'jogador4': randint(1, 6)
             }

print('Valores sorteados:')
for k,v in jogadores.items():
    print(f'    O {k} tirou {v}')
    sleep(0.8)

print('Ranking do jogadores:')
lugar = 1
for k,v in sorted(jogadores.items(), key=lambda item: item[1], reverse=True):
    print(f'    {lugar}º lugar: {k} com {v}')
    lugar += 1
    sleep(0.8)

'''
Outra solução para ordenar

from operator import itemgetter

ranking = list()
ranking = sorted(jogadores.items(), key = itemgetter(1) reverse = True)

for i, v in enumerate(ranking):
    print(f '{i+1}º lugar: {v[0]} com {v[1]}. '}
'''