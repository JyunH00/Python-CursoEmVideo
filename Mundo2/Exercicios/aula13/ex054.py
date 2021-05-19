'''
Exercício 54: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não
atingiram a maioridade e quantas já são maiores.
'''

### Resolução ###

from datetime import date

print('-=-'*30)
print('Coloque o ano de nascimento de 7 pessoas e direi quantas não atingiram a maioridade e quantas já!')
print('-=-'*30)

### Criação de Variáveis ###

anoAtual = date.today().year

maior = 0
menor = 0

for ano in range(1, 8):
    anoN = int(input('Digite o ano que a {}º pessoa nasceu: '.format(ano)))
    if (anoAtual - anoN) >= 18:
        maior += 1
    else:
        menor += 1

print('Das 7 idades mostradas tivemos {} maiores de idade e {} menores de idade!'.format(maior, menor))