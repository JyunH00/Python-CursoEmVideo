'''
Exercício 84: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:

A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
'''

# Resolução #

# Variáveis #

pesPeso = list()
pessoas = list()

while True:
    nome = str(input('Nome: '))
    pesPeso.append(nome)
    peso = float(input('Peso: '))
    pesPeso.append(peso)
    pessoas.append(pesPeso[:])
    pesPeso.clear()

    resposta = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N] ')).upper().strip()[0]

    if resposta in 'N':
        break



# Print #
print('-=' * 30)
print(f'Ao todo, você cadastrou {len(pessoas)} pessoas.')

# Verfica maior e menor pesos
maior = menor = pessoas[0][1]
for p in pessoas:
    if p[1] >= maior:
        maior = p[1]
    elif p[1] <= menor:
        menor = p[1]

print(f'O maior peso foi de {maior:.1f}kg. Peso de ', end='')
for p in pessoas:
    if p[1] == maior:
        print(f'[{p[0]}]', end=' ')

print(f'\nO menor peso foi de {menor:.1f}kg. Peso de ', end='')
for p in pessoas:
    if p[1] == menor:
        print(f'[{p[0]}]', end=' ')

