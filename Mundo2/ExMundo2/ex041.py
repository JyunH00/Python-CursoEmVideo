'''
Exercício 41: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria,
de acordo com a idade:

> Até 9 anos: MIRIM
> Até 14 anos: INFANTIL
> Até 19 anos: JUNIOR
> Até 25 anos: SÊNIOR
> Acima: MASTER
'''

##### Resolução #####

from datetime import date

cores = {'finaliza':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'vermelho':'\033[31m',
         'verde':'\033[32m',
         'magenta':'\033[35m'
         }

print('-=-'*30)
print('====CATEGORIA DE NATAÇÃO====')
print('Coloque seu ano de nascimento para saber qual sua categoria para a Confederação Nacional de Natação!')
print('-=-'*30)

### Criação das variáveis ###

anoN = int(input('Coloque seu ano de nascimento: '))

anoAtual = date.today().year

idade = (anoAtual - anoN)

### Condições ###

if anoN > anoAtual:
    print('{}COLOQUE UM ANO VÁLIDO{}'.format(cores['vermelho'], cores['finaliza']))
else:
    if idade <= 9:
        print('Você tem {} anos e sua categoria é {}MIRIM{}.'.format(idade, cores['vermelho'], cores['finaliza']))
    elif idade <= 14:
        print('Você tem {} anos e sua categoria é {}INFANTIL{}.'.format(idade, cores['azul'], cores['finaliza'], (18 - idade) ))
    elif idade <= 19:
        print('Você tem {} anos e sua categoria é {}JUNIOR{}.'.format(idade, ['amarelo'], cores['finaliza'], idade))
    elif idade <= 25:
        print('Você tem {} anos e sua categoria é {}SÊNIOR{}.'.format(idade, cores['verde'], cores['finaliza'], idade))
    elif idade > 25:
        print('Você tem {} anos e sua categoria é {}MASTER{}.'.format(idade, cores['magenta'], cores['finaliza'], idade))
