'''
Exercício 74: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
'''

#### Resolução ####

from random import randint

#### Variáveis ####

tNumA = (randint(0,9), randint(0,9), randint(0,9), randint(0,9), randint(0,9))

print(f'Os valores sorteados foram: {tNumA[0]} {tNumA[1]} {tNumA[2]} {tNumA[3]} {tNumA[4]}')

maior = menor = 0
for pos,num in enumerate(tNumA):
    if pos == 0:
        maior = num
        menor = num
    if num < menor:
        menor = num
    if num > maior:
        maior = num

print(f'O maior valor sorteado foi {maior}')
print(f'O menor valor sorteado foi {menor}')

'''
Maneira MUITO mais fácil

* Utilizar um for para imprimir os valores!

print(f'O maior valor sorteado foi {max(tnumA)}') 
print(f'O menor valor sorteado foi {min(tnumA)}')
'''