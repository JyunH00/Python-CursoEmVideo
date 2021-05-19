'''
Exercício 87: Aprimore o desafio 86, mostrando no final:

A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
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
        print(f'\033[1m[{matriz[i][j]:^3}]\033[m', end='')
    print()

print()
print('-='*30)

somaP = somaV3 = mV = 0
for i in range(0, 3):
    for j in range(0, 3):
        if matriz[i][j] % 2 == 0:
            somaP += matriz[i][j]
        if j == 2:
            somaV3 += matriz[i][j]
        if i == 1 and j == 0:
            maior = matriz[i][j]
        elif i == 1 and matriz[i][j] >= maior:
            maior = matriz[i][j]
print(f'A soma dos valores pares é {somaP}.')
print(f'A soma dos valores da terceira coluna é {somaV3}.')
print(f'O maior valor da segunda linha {maior}.')

'''
Solução no vídeo diferente!
'''