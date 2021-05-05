'''
Exercício 47: Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50
'''

### Resolução ###

cores = {'finaliza':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'vermelho':'\033[31m',
         'verde':'\033[32m',
         'magenta':'\033[35m'
         }

### Laço ###

print('Os números pares entre 1 e 50 estão pintados em amarelo!: ')

for c in range(1, 51):
    if c % 2 == 0:
        print('{}{}{}'.format(cores['amarelo'], c, cores['finaliza']), end = ' ')
    else:
        print(c, end = ' ')

## Sem o else, apenas aparecerão os pares.

'''
Solução mais simples:

for c in range(2, 51, 2) -> não há necessidade do if
'''