'''
Exercício 78: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.

No final, mostre qual foi o maior e o menor valor digitado e suas respectivas posições na lista.
'''

#### Resolução ####

#### Variáveis ####

numList = []

#### Laços ####
for num in range(0,5):
    numList.append(int(input(f'Digite um valor para a posição {num}: ')))
print(f'Você digitou os valores {numList}')

print(f'O maior valor digitado foi {max(numList)} nas posições: ', end='')
for pos, i in enumerate(numList):
    if i == max(numList):
        print(f'{pos}...', end=' ')

print(f'\nO menor valor digitado foi {min(numList)} nas posições: ', end='')
for pos, i in enumerate(numList):
    if i == min(numList):
        print(f'{pos}...', end=' ')
