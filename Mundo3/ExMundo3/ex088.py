'''
Exercício 88: Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos
serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
'''

# Resolução #

import random
from time import sleep

print('\033[1m-'*50)
mg = 'JOGA NA MEGA SENA'
print(f'{mg:^50}')
print('-'*50)

# Variáveis #

numInt = int(input('Quantos jogos você quer que eu sorteie? '))

listaJogos = []
jogos = []

print('-='*5, end =' ')
print(f'SORTEANDO {numInt} JOGOS', end=' ')
print('-='*5)

numJ = 0
while numJ < numInt:
    for i in range(0, 6):
        numAl = random.randint(1, 60)
        if numAl not in jogos:
            jogos.append(numAl)

    listaJogos.append(jogos[:])
    jogos.clear()
    listaJogos[numJ].sort()
    print(f'Jogo {numJ + 1}: {listaJogos[numJ]}')
    sleep(0.5)
    numJ += 1

print('-='*5, end=' ')
print(' < BOA SORTE! > ', end=' ')
print('-='*5)
