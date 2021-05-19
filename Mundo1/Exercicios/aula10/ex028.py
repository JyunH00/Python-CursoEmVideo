'''
Exercício 28: Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário
tentar descobrir qual foi o número escolhido pelo computador.

O programa deverá escrever na tela se o seu usário venceu ou perdeu.
'''

##### Resolução #####

from random import randint

from time import sleep # Resolução do víd

print('-=-'*20)
print('Estou pensando em um número entre 0 e 5...')
print('Adivinhe!')
print('-=-'*20)

### Criação das variáveis ###

numPessoa = int(input('\nDigite o número em que pensei! ')) # Número que o jogador tenta adivinhar

numComputador = randint(0, 5) # Número que o computador irá pensar

### Condições ###

print('PROCESSANDO...')
sleep(3) # Fica 3 segundos "processando"

if numPessoa == numComputador:
    print('Caramba! Você acertou! O número que eu pensei era mesmo o {}.'.format(numComputador))
else:
    print('Poxa! Tente de novo! O número que eu pensei era {}.'.format(numComputador))
