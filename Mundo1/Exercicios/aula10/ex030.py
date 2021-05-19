'''
Exercício 30: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
'''

##### Resolução #####

from time import sleep

print('-=-'*20)
print('Vou advinhar se o seu número é par ou ímpar!')
print('-=-'*20)

### Criação das variáveis ###

num = int(input('\nDigite um número:'))

### Procesando ###
if num > 10000:
    print('PROCESSANDO...')
    sleep(3)

### Condições ###

if (num % 2) == 0: # Se o resto da divisão de um número inteiro por 2 for 0 ele é considerado par
    print('O número {} é PAR!'.format(num))
else: # Todos os números não PAR são ÍMPARES
    print('O número {} é ÍMPAR!'.format(num))

