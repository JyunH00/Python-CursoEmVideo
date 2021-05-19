'''
Exercício 63: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os n primeiros elementos de uma
Sequência de Fibonacci.

Ex:
0 - 1 - 1 - 2 - 3 - 5 - 8
'''

#### Resolução ####

print('-=-'*20)
print('SEQUÊNCIA DE FIBONACCI')
print('-=-'*20)

### Variáveis ###

nTermos = int(input('Digite o número de elementos para a sequência de Fibonacci: \n'))

vAtual = 0 # valor atual da Sequência
sF = 0 # Valor que guarda o valor atual
sFAnt = 0 # Valor que guarda o valor anterior ao atual

# Laço While #

iterador = 1
while iterador != nTermos + 1:
    if iterador == 1:
        vAtual = 0
        sFAnt = sF
        sF = vAtual
    elif iterador == 2:
        vAtual = 1
        sFAnt = sF
        sF = vAtual
    else:
        vAtual = sF +sFAnt
        sFAnt = sF
        sF = vAtual

    print(vAtual, end = ' ')
    if iterador != nTermos:
        print('-', end = ' ')
    iterador += 1