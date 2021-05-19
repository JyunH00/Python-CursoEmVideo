'''
Exercício 50: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se
o valor digitado for ímpar, desconsidere-o.
'''

### Resolução ###

### Laço ###

soma = 0 # Resultado da soma

for c in range(0, 6):
    num = int(input('Digite um número inteiro: '))
    if num % 2 == 0: # Verifica se é par
        soma += num

print('Soma dos números pares: {}'.format(soma))