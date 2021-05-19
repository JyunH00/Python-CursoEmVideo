'''
Exercício 94: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada um em um
dicionário e todos os dicionários em uma lista. No final, mostre:

A) Quantas pessoas foram cadastradas
B) A média de idade do grupo
C) Uma lista com todas as mulheres
D) Uma lista com todas as pessoas com idade acima da média
'''

# Resolução #

# Variáveis #

dadosP = {}
pessoas = []
somaM = 0
while True:
    dadosP['nome'] = str(input('Nome: ')).title()
    dadosP['sexo'] = str(input('Sexo: [M/F] ')).upper().strip()[0]
    while dadosP['sexo'] not in "MF":
        print('ERRO! Por favor, digite apenas M ou F.')
        dadosP['sexo'] = str(input('Sexo: [M/F] ')).upper().strip()[0]
    dadosP['idade'] = int(input('Idade: '))
    pessoas.append(dadosP.copy())
    somaM += dadosP['idade']
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    while resp not in 'SN':
        print('ERRO! Responda apenas S ou N. ')
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp in 'N':
        break

print('-='*30)
mediaI = somaM/len(pessoas)
print(f'- O grupo tem {len(pessoas)} pessoas.')
print(f'- A média de idade é de {mediaI:.2f} anos.')

print(f'- As mulheres cadastradas foram: ', end='')
for p in pessoas:
    if p['sexo'] == 'F':
        print(p['nome'], end=' ')

print()
print('- Lista das pessoas que estão acima da média: ')
print()
for p in pessoas:
    if p['idade'] >= mediaI:
        print(f'    nome = {p["nome"]}; sexo = {p["sexo"]}; idade = {p["idade"]}; ')

print('-=' * 30)
print('<< ENCERRADO >>')