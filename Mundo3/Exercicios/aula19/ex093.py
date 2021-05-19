'''
Exercício 93: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do
jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso
será guardado em um dicionário. Incluindo o total de gols feitos durante o campeonato.
'''

# Resolução #

# Variáveis #

infoJ = {}

infoJ['nome'] = str(input('Nome do Jogador: '))

numP = int(input(f'Quantas partidas {infoJ["nome"]} jogou? '))
gols = []
total = 0
for i in range(0, numP):
    gols.append(int(input(f'Quantos gols na partida {i}? ')))
    total += gols[i]

infoJ['gols'] = gols
infoJ['total'] = total # sum(gols)

print('-='*40)
print(infoJ)
print('-='*40)
print(f'O jogador {infoJ["nome"]} jogou {numP} partidas.')

for i in range(0, numP):
    print(f'{"=>":>6} Na partida {i}, fez {infoJ["gols"][i]} gols.')
print(f'Foi um total de {infoJ["total"]} gols.')