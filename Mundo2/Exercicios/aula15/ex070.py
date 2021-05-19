'''
Exercício 70: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário
vai continuar. No final, mostre.

A) Qual é o total gasto na compra.
B) Quantos produtos custam mais de R$1000
C) Qual é o nome do produto mais barato
'''

#### Resolução ###

print('-' * 30)
print('         LOJA DO JYUN')
print('-' * 30)

### Variáveis ###

nomeB = ''
nomeP = ''
precoB = preco = contadorP = pTotal = contadorB = 0


### Laço ###

while True:
    nomeP = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$ '))
    contadorB += 1
    pTotal += preco

    if preco > 1000:
        contadorP += 1

    if contadorB == 1:
        precoB = preco
        nomeB = nomeP
    elif preco < precoB:
        precoB = preco
        nomeB = nomeP

    pergunta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while pergunta not in 'SN':
        pergunta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]

    if pergunta == 'N':
        break

print('-----------------------FIM DO PROGRAMA-----------------------')
print(f'O total da compra foi R${pTotal:.2f}')
print(f'Temos {contadorP} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nomeB} que custa R${precoB:.2f}')


