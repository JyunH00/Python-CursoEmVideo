'''
Exercício 16: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
'''

'''
Ex: Digite um número: 6.127
O número 6.127 tem a parte inteira 6
'''

##### Resolução #####

import math
#from math import trunc

### Criação das variáveis ###

numReal = float(input('Digite um número: '))

parteInt = math.trunc(numReal)

### Print do resultado ###

print('O número {} tem parte inteira {}.'.format(numReal, parteInt))

'''
Outras resoluções

print('O número {} tem parte inteira {}.'.format(numReal, math.trunc(numReal)))
print('O número {} tem parte inteira {:.0f}.'.format(numReal,numReal))
print('O número {} tem parte inteira {}.'.format(numReal, int(numReal)))
'''