'''
Exercício 82: Crie um programa que vai ler vários números e colocar numa lista.

Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.

Ao final, mostre o conteúdo das 3 listas geradas
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

numListaP = []
numListaI = []

for i in numLista:
    if i % 2 == 0:
        numListaP.append(i)
    else:
        numListaI.append(i)

print('-=-'*20)
print(f'A lista completa é {numLista}')
print(f'A lista de pares é {numListaP}')
print(f'A lista de ímpares é {numListaI}')