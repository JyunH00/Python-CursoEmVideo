'''
Exercício 39: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:

> Se ele ainda vai se alistar ao serviço militar
> Se é a hora de se alistar
> Se já passou do tempo do alistamento.

Seu programa deverá mostrar o tempo que falta ou que passou do prazo.
'''

##### Resolução #####

from datetime import date

cores = {'finaliza':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'vermelho':'\033[31m',
         'verde':'\033[32m'
         }

print('-=-'*30)
print('====ANÁLISE PARA ALISTAMENTO MILITAR====')
print('Coloque seu ano de nascimento para saber quantos anos faltam ou se já passou do prazo para alistamento!')
print('-=-'*30)

### Criação das variáveis ###

anoN = int(input('Coloque seu ano de nascimento: '))

anoAtual = date.today().year

idade = (anoAtual - anoN)

### Condições ###

if idade == 18:
    print('Você {}PRECISA{} se alistar pois tem 18 anos!'.format(cores['vermelho'], cores['finaliza']))
elif idade < 18:
    print('Você {}NÃO PRECISA{} se alistar pois faltam {} anos.'.format(cores['azul'], cores['finaliza'], (18 - idade) ))
elif idade > 18:
    print('Você já {}PASSOU{} do tempo de alistamento pois tem {} anos.'.format(cores['amarelo'], cores['finaliza'], idade))