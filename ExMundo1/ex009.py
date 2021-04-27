'''
Exercício 9: Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.
'''

##### Resolução #####

### Criação das variáveis ###

tNumero = int(input('Digite um número para ver sua tabuada:'))

### Print do resultado ###

print('-'*12)
print('{} *  1 = {}'.format(tNumero, tNumero*1))
print('{} *  2 = {}'.format(tNumero, tNumero*2))
print('{} *  3 = {}'.format(tNumero, tNumero*3))
print('{} *  4 = {}'.format(tNumero, tNumero*4))
print('{} *  5 = {}'.format(tNumero, tNumero*5))
print('{} *  6 = {}'.format(tNumero, tNumero*6))
print('{} *  7 = {}'.format(tNumero, tNumero*7))
print('{} *  8 = {}'.format(tNumero, tNumero*8))
print('{} *  9 = {}'.format(tNumero, tNumero*9))
print('{} * 10 = {}'.format(tNumero, tNumero*10))
print('-'*12)


### Outra resolução ###

'''
print('-'*12)
print('{} * {:2} = {}'.format(tNumero, 1, tNumero*1))
print('{} * {:2} = {}'.format(tNumero, 2, tNumero*2))
print('{} * {:2} = {}'.format(tNumero, 3, tNumero*3))
print('{} * {:2} = {}'.format(tNumero, 4, tNumero*4))
print('{} * {:2} = {}'.format(tNumero, 5, tNumero*5))
print('{} * {:2} = {}'.format(tNumero, 6, tNumero*6))
print('{} * {:2} = {}'.format(tNumero, 7, tNumero*7))
print('{} * {:2} = {}'.format(tNumero, 8, tNumero*8))
print('{} * {:2} = {}'.format(tNumero, 9, tNumero*9))
print('{} * {:2} = {}'.format(tNumero, 10, tNumero*10))
print('-'*12)
'''