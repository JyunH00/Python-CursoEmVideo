'''
Exercício 86: Crie um programa que cria uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.

[   ] [   ] [   ]
[   ] [   ] [   ]
[   ] [   ] [   ]

No final mostre a matriz na tela, com a formação correta
'''

# Resolução #

# Variáveis #

matriz = [[], [], []]


for i in range(0, 3):
    for j in range(0, 3):
        numInt = int(input(f'Digite um valor para [{i}, {j}]: '))
        matriz[i].append(numInt)

print('-='*30)
for i in range(0, 3):
    for j in range(0, 3):
        print(f'\033[1m[{matriz[i][j]:^3}]', end='')
    print()

'''
Outra solução!

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(0, 3):
    for j in range(0, 3):
        matriz[i][j] = int(input(f'Digite um valor para [{i}, {j}]: '))
        
'''