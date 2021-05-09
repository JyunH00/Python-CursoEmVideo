'''
Exercício 81: Crie um programa que vai ler vários números e colocar em uma lista.

Depois disso mostre:

A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma descrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
'''

# Resolução #

# Variáveis #

numLista = []

# Laço #

while True:
    numLista.append(int(input('Digite um valor: ')))
    resposta = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if resposta in 'N':
        break

# Prints #

print('-=-'*20)
print(f'Você digitou {len(numLista)} elementos')
numLista.sort(reverse=True)
print(f'Os valores em ordem descrescente são {numLista}')
if 5 in numLista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')