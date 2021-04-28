'''
https://pypi.org/ -> importar outras bibliotecas
'''

import random, emoji


num = random.random() # Gera um número real entre 0 e 1
num = random.randint(1, 10) # Gera um número entre 1 e 10

print(num)

print(emoji.emojize("Olá, Mundo :earth_americas:", use_aliases=True))