'''
Exercício 106: Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual
vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará.

OBS: use cores.
'''

# Resolução #

cores = {'finaliza':'\033[m',
         'azul':'\033[1;34m',
         'amarelo':'\033[1;33m',
         'vermelho':'\033[1;31m',
         'verde':'\033[1;32m',
         'magenta':'\033[1;35m'
         }

from time import sleep

# Funções #

def sistIH():
    """
    -> Função para Interactive Help
    """
    while True:
        print('-='*30)
        print(f'{cores["vermelho"]} SISTEMA DE AJUDA PyHELP {cores["finaliza"]}')
        print('-=' * 30)
        nomeB = str(input('Função ou Biblioteca > ')).strip().lower()
        sleep(1)
        if nomeB in 'fim':
            print('-=' * 30)
            print(f'{cores["amarelo"]} ATÉ LOGO! {cores["finaliza"]}')
            print('-=' * 30)
            break
        print('-=' * 30)
        print(f'{cores["azul"]} ACESSANDO O MANUAL DO COMANDO {nomeB} {cores["finaliza"]}')
        print('-=' * 30)
        sleep(1)
        print(f'{cores["verde"]}')
        help(nomeB)
        print(f'{cores["finaliza"]}')



#Programa Principal

sistIH()

'''
Solução bem diferente no video!
'''