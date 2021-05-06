'''
Exercício 71: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual
será o valor sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.

OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1
'''

#### Resolução ###

print('-' * 35)
print('             BANCO')
print('-' * 35)

### Variáveis ###

valor = 0
nota50 = nota20 = nota10 = nota1 = 0
resto50 = resto20 = resto10 = 0
### Laço ###

while True:
    valor = float(input('Qual valor você quer sacar? R$ '))

    nota50 = valor // 50
    resto50 = valor % 50

    nota20 = resto50 // 20
    resto20 = resto50 % 20

    nota10 = resto20 // 10
    resto10 = resto20 % 10

    nota1 = (resto10)
    break
if nota50 > 0:
    print(f'Total de {nota50:.0f} cédulas de R$50')

if nota20 > 0:
    print(f'Total de {nota20:.0f} cédulas de R$20')

if nota10 > 0:
    print(f'Total de {nota10:.0f} cédulas de R$10')

if nota10 > 0:
    print(f'Total de {nota1:.0f} cédulas de R$1')

print('-' * 35)
print('VOLTE SEMPRE!')

'''
Resolução do vídeo super diferente!
'''