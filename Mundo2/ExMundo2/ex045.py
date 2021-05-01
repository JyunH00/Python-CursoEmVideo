'''
Exercício 45: Crie um programa que faça o computador jogar Jokenpô com você.
'''


##### Resolução #####

from random import randint
from time import sleep
cores = {'finaliza':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'vermelho':'\033[31m',
         'verde':'\033[32m',
         'magenta':'\033[35m'
         }

print('-=-'*30)
print('\n====JOKENPÔ COM O COMPUTADOR====')
print('\nESCOLHA PEDRA PAPEL OU TESOURA E VEJA SE GANHA DE MIM!')
print('\n REGRAS:')
print('''\n> ESCOLHAS IGUAIS: {}EMPATE{}
> PEDRA X PAPEL: {}PAPEL{}
> PEDRA X TESOURA: {}PEDRA{}
> TESOURA X PAPEL: {}TESOURA{}
'''.format(cores['azul'], cores['finaliza'], cores['verde'], cores['finaliza'], cores['magenta'], cores['finaliza'], cores['amarelo'], cores['finaliza'] ))
print('-=-'*30)

### Criação das variáveis ###

computador = ['pedra', 'papel', 'tesoura']

escolhaC = randint(0,2)

jogador = str(input('\nEscolha PEDRA, PAPEL ou TESOURA: ')).lower()


#### Condições ####

if jogador == 'pedra' or jogador == 'papel' or jogador == 'tesoura':
    print('JO')
    sleep(0.5)
    print('KEN')
    sleep(0.5)
    print('PÔ')
    sleep(0.5)
    print('-=-'*30)
    if jogador == 'pedra' and computador[escolhaC] == 'pedra':
        print('VOCÊ JOGOU {}PEDRA{} E EU JOGUEI {}PEDRA{}'.format(cores['verde'], cores['finaliza'], cores['verde'], cores['finaliza']))
        print('\n{}EMPATE{}'.format(cores['verde'], cores['finaliza']))
    elif jogador == 'papel' and computador[escolhaC] == 'papel':
        print('VOCÊ JOGOU {}PAPEL{} E EU JOGUEI {}PAPEL{}'.format(cores['azul'], cores['finaliza'], cores['azul'], cores['finaliza']))
        print('\n{}EMPATE{}'.format(cores['verde'], cores['finaliza']))
    elif jogador == 'tesoura' and computador[escolhaC] == 'tesoura':
        print('VOCÊ JOGOU {}TESOURA{} E EU JOGUEI {}TESOURA{}'.format(cores['amarelo'], cores['finaliza'], cores['amarelo'], cores['finaliza']))
        print('\n{}EMPATE{}'.format(cores['verde'], cores['finaliza']))
    elif jogador == 'pedra' and computador[escolhaC] == 'papel':
        print('VOCÊ JOGOU {}PEDRA{} E EU JOGUEI {}PAPEL{}'.format(cores['verde'], cores['finaliza'], cores['azul'], cores['finaliza']))
        print('\n{}COMPUTADOR VENCE{}'.format(cores['vermelho'], cores['finaliza']))
    elif jogador == 'pedra' and computador[escolhaC] == 'tesoura':
        print('VOCÊ JOGOU {}PEDRA{} E EU JOGUEI {}TESOURA{}'.format(cores['verde'], cores['finaliza'], cores['amarelo'], cores['finaliza']))
        print('\n{}JOGADOR VENCE{}'.format(cores['azul'], cores['finaliza']))
    elif jogador == 'papel' and computador[escolhaC] == 'pedra':
        print('VOCÊ JOGOU {}PAPEL{} E EU JOGUEI {}PEDRA{}'.format(cores['azul'], cores['finaliza'], cores['verde'], cores['finaliza']))
        print('\n{}JOGADOR VENCE{}'.format(cores['azul'], cores['finaliza']))
    elif jogador == 'papel' and computador[escolhaC] == 'tesoura':
        print('VOCÊ JOGOU {}PAPEL{} E EU JOGUEI {}TESOURA{}'.format(cores['azul'], cores['finaliza'], cores['amarelo'], cores['finaliza']))
        print('\n{}COMPUTADOR VENCE{}'.format(cores['vermelho'], cores['finaliza']))
    elif jogador == 'tesoura' and computador[escolhaC] == 'papel':
        print('VOCÊ JOGOU {}TESOURA{} E EU JOGUEI {}PAPEL{}'.format(cores['amarelo'], cores['finaliza'], cores['azul'], cores['finaliza']))
        print('\n{}JOGADOR VENCE{}'.format(cores['azul'], cores['finaliza']))
    elif jogador == 'tesoura' and computador[escolhaC] == 'pedra':
        print('VOCÊ JOGOU {}TESOURA{} E EU JOGUEI {}PEDRA{}'.format(cores['amarelo'], cores['finaliza'], cores['verde'], cores['finaliza']))
        print('\n{}COMPUTADOR VENCE{}'.format(cores['vermelho'], cores['finaliza']))
    print('-=-' * 30)
else:
    print('-=-' * 30)
    print('{}FAÇA UMA JOGADA VÁLIDA!{}'.format(cores['vermelho'], cores['finaliza']))
    print('-=-' * 30)

'''
* Ver a outra resolução no vídeo! Está bem diferente.
'''