'''
Exercício 89: Crie um programa que leia o nome e duas notas de vários alunos e guarde tudo em uma lista composta. No
final, mostre um boletim contentdo a média de cada um e permita que o usuário possa mostras as notas de cada aluno
individualmente.
'''

# Resolução #


# Variáveis #

nomeA = []
notas = []
boletim = []

while True:
    nome = str(input('Nome: ')).title()
    nomeA.append(nome)
    nota1 = float(input('Nota 1: '))
    notas.append(nota1)
    nota2 = float(input('Nota 2: '))
    notas.append(nota2)
    media = (nota1 + nota2) / 2
    notas.append(media)
    nomeA.append(notas[:])
    notas.clear()
    boletim.append(nomeA[:])
    nomeA.clear()

    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp in 'N':
        break
print('-='*50)

print(f'\033[1m{"No.":<4}{"NOME":<10}{"MÈDIA":>10}') # Assim que manipulamos prints sem criar as variáveis!
print('-'*25)

for pos,n in enumerate(boletim):
    print(f'{pos:<4}{n[0]:<10}{n[1][2]:>8.1f}')
print('-'*25)

while True:
    numAluno = int(input('Mostras as notas de qual aluno? (999 interrompe): '))
    if numAluno == 999:
        break
    if numAluno <= len(boletim) - 1:
        print(f'Notas de {boletim[numAluno][0]} são {boletim[numAluno][1][0:2]}')
        print('-' * 35)
print('FINALIZANDO...')
print('<<< VOLTE SEMPRE >>>')

'''
Solução do vídeo:

boletim = []

nome = str(input('Nome: ')).title()
nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))
media = (nota1 + nota2) / 2
boletim.append([nome, [nota1, nota2], media] # Podemos montar a lista com append do jeito que quisermos.
'''