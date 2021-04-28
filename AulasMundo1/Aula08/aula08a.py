'''
Nessa aula, vamos aprender como utilizar módulos em Python utilizando os comandos import e from/import no Python.
Veja como carregar bibliotecas de funções e utilizar vários recursos adicionais nos seus programas utilizando módulos
built-in e módulos externos, oferecidos no Pypi.
'''

'''
>>> Comandos de 'import' e 'from biblioteca import funcionalidadeEspecífica, funcionalidadeEspecífica...'

>>> Exemplo da biblioteca math (import math)
    >>> ceil -> arrendodamento para cima;
    >>> floor -> arrendodamento para baixo;
    >>> trunc -> eliminação da vírgula;
    >>> pow -> potência;
    >>> sqrt -> raiz quadrada;
    >>> factorial -> fatorial;
    >>> etc.
'''

'''

https://docs.python.org/3.9/library/index.html -> documentação de python 3.9

'''


#### Prática ####

import math

# from math import sqrt, ceil, floor -> importando algumas funções de math


num = int(input('Digite um número: '))

raiz = math.sqrt(num)

### Fazendo alguns testes ###

print('A raiz de {} é igual a {}'.format(num, raiz))
print('A raiz de {} é igual a {}'.format(num, math.ceil(raiz))) # Arrendodando para cima
print('A raiz de {} é igual a {}'.format(num, math.floor(raiz))) # Arrendodando para baixo
print('A raiz de {} é igual a {:.2f}'.format(num, raiz)) # 2 casa decimais