'''
Exercício 103: Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um
jogador e quantos gols ele marcou.

O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
'''

# Resolução #

# Funções #

def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gols no campeonato.')


#Programa principal

nome = str(input('Nome do jogador: ') or "<desconhecido>")
nGols = str(input('Número de gols: ') or "0")

#ficha(nome, nGols)

if nGols.isnumeric():
    nGols = int(nGols)
else:
    nGols = 0

if nome.strip() == '':
    ficha(gols=nGols)
else:
    ficha(nome, nGols)