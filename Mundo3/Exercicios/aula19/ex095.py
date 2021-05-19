'''
Exercício 95: Aprimore o DESAFIO 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de
detalhes do aproveitamento de cada jogador.
'''

# Resolução #

# Variáveis #

jogadores = []
infoJ = {}
gols = []
total = 0

while True:
    print('\033[1m=\033[m'*40)
    infoJ['nome'] = str(input('Nome do Jogador: '))
    numP = int(input(f'Quantas partidas {infoJ["nome"]} jogou? '))
    for i in range(0, numP):
        gols.append(int(input(f'Quantos gols na partida {i}? ')))
        total += gols[i]

    infoJ['gols'] = gols[:]
    infoJ['total'] = total

    jogadores.append(infoJ.copy())
    gols.clear()
    total = 0
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp in 'N':
        break

## Não está alinhado!
print('-='*40)
print(f'cod {"nome":>3} {"gols":>15}{"total":>15}')
print('\033[1m=\033[m'*60)
for pos, j in enumerate(jogadores):
    print(f'{pos} {j["nome"]:>3}{"":<15}{j["gols"]}{j["total"]:>15}')
print('\033[1m=\033[m'*60)

while True:
    pergD = int(input('Mostrar dados de qual jogador? '))
    if pergD == 999:
        break

    print(f'-- LEVANTAMENTO DO JOGADDOR {jogadores[pergD]["nome"]}: ')
    for j in range(0, len(jogadores[pergD]['gols'])):
        print(f'   No jogo fez {j} fez {jogadores[pergD]["gols"][j]}.')
print('<< VOLTE SEMPRE >>')

'''
Para mostrar a tabela de jogadores há um jeito melhor!

print('cod ', end ='')
    print(f'{i:<15}, end ='')
print()
print('-' *40)
for k, v in enumerate(jogadores):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'str(d):<15}', end='')
    print()
print('-' *40)
'''