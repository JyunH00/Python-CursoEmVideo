'''
Exercício 38: Escreva um programa que leia dois números inteiroas e compare-os, mostrando na tela uma mensagem:

> o PRIMEIRO VALOR é maior
> o SEGUNDO VALOR é maior
> Não existe maior, os dois valores são iguais
'''

##### Resolução #####

cores = {'finaliza':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'vermelho':'\033[31m',
         'verde':'\033[32m'
         }

print('-=-'*30)
print('====COMPARADOR DE 2 NÚMEROS INTEIROS====')
print('Escreva 2 números inteiros para ver qual deles é o maior, ou se possuem o mesmo valor!')
print('-=-'*30)

### Criação das variáveis ###

num1 = int(input('\nEscreva um número inteiro: '))
num2 = int(input('Escreva outro número inteiro: '))

### Condições ###

if num1 > num2:
    print('O {}PRIMEIRO VALOR {}{} é {}MAIOR{}'.format(cores['azul'],num1, cores['finaliza'], cores['verde'], cores['finaliza']))
elif num2 > num1:
    print('O {}SEGUNDO VALOR {}{} é {}MAIOR{}'.format(cores['amarelo'], num2, cores['finaliza'], cores['verde'],cores['finaliza']))
elif num1 == num2:
    print('Os valores {}{} e {}{} são {}IGUAIS{}'.format(cores['azul'], num1, num2, cores['finaliza'], cores['amarelo'],cores['finaliza']))
