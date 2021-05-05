'''
Exercício 48: Faça um programa que calcule a soma entre todos os NÚMEROS ÍMPARES que são MÚLTIPLOS DE TRÊS a que se
encontram no intervalo de 1 até 500
'''

### Resolução ###

cores = {'finaliza':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'vermelho':'\033[31m',
         'verde':'\033[32m',
         'magenta':'\033[35m'
         }

### Laço ###

print('A soma entre todos os números ímpares e múltiplos de três no intervalo de 1 até 500:', end = ' ')

soma = 0 # Representa o total da soma

for c in range(1, 501):
    if c % 2 != 0 and c % 3 == 0: # Condição que verifica se é ímpar e múltiplo de 3
        soma += c # Adiciona ao  total se a condição for satisfeita
print(soma)

'''
Outra solução!

for c in range(1, 501, 2): -> Já pula os pares
    if c % 3 == 0: # Condição que verifica se é múltiplo de 3
        soma += c # Adiciona ao  total se a condição for satisfeita

'''