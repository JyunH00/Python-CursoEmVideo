'''
Exercício 64: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário
digitar o valor 999, que é a condição de parada. No final, mostre quandos números foram digitados e qual foi a soma entre
eles (DESCONSIDERANDO O FLAG)
'''

#### Resolução ####

# Variáveis #

numInt = int(input('Digite um valor inteiro: \n'))
numD = 0
soma = 0

# Laço while #

while numInt != 999:
    numD += 1
    soma += numInt
    numInt = int(input('Digite outro valor inteiro: \n'))
print('\nA soma dos valores digitados é: {}.'.format(soma))
print('\nO número de valores digitados é: {}.'.format(numD))
