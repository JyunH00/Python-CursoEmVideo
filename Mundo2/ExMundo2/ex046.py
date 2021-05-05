'''
Exercício 46: Faça um programa que mostre na tela uma CONTAGEM REGRESSIVA para o estouro de fogos de artifício, indo de 10 até 0,
com uma pausa de 1 segundo entre eles.
'''

#### Resolução ####

from time import sleep
import emoji

cores = {'finaliza':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'vermelho':'\033[31m',
         'verde':'\033[32m',
         'magenta':'\033[35m'
         }

print('CONTAGEM REGRESSIVA!!\n')

### Laço ###

for c in range(10, -1, -1):
    print('{}{}{}'.format(cores['amarelo'], c, cores['finaliza']))
    sleep(1)
print(emoji.emojize(':collision: :collision: :collision:',variant='emoji_type', use_aliases=True))