'''
Exercício 85: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que
mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente
'''

# Resolução #

# Variáveis #

numeros = [[], []]

# Laço #

for num in range(0,7):
    numInt = int(input(f'Digite o {num + 1}º valor: '))
    if numInt % 2 == 0:
        numeros[0].append(numInt)
    else:
        numeros[1].append(numInt)

# Prints #

print('-='*30)
numeros[0].sort()
print(f'Os valores pares digitados foram: {numeros[0]}')
numeros[1].sort()
print(f'Os valores ímpares digitados foram: {numeros[1]}')