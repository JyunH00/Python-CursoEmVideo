'''
Exercício 114: Crie um código em Python que teste se o site Pudim está acessível pelo computador usado.
'''

# Resolução #

import urllib.request

# Funções #

try:
    webUrl = urllib.request.urlopen('http://pudim.com.br/')
except:
    print('\033[1;31mNão consegui acessar o site do pudim!\033[0m')
else:
    print('\033[1;32mConsegui acessar o site do pudim!\033[0m')
