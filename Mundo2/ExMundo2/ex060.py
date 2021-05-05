'''
Exercício 60: Faça um programa que leia um número qualquer e mostre seu fatorial.

Ex:
5! = 5x4x3x2x1 = 120

fazer com for e while!
'''

#### Resolução ####

print('-=-'*20)
print('CALCULADORA DE FATORIAL')
print('-=-'*20)


# Uso de while #

numeroInt = int(input('Digite um número inteiro: \n'))
iterador = (numeroInt - 1)
fatorial = numeroInt

while iterador != 0:
    fatorial *= iterador;
    iterador -= 1
    print('O fatorial de {}! = '.format(numeroInt), end=' ')


'''
# Uso de for #

numeroInt = int(input('Digite um número inteiro: \n'))
fatorial = numeroInt
iterador = (numeroInt - 1)

for i in range(iterador, 0, -1):
    fatorial *= i
print('O fatorial de {}! é {}.'.format(numeroInt, fatorial))
'''


'''

>>> Mostra todos os números

c = n
print('Calculando {}! = '.format(n), end=''
while c > 0:
    print('{}'.format(c), end = '')
    print(' x ' if c > 1 else ' = ', end ='')
    c -= 1
'''