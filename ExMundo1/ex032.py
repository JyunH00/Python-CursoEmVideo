'''
Exercício 32: Faça um programa que leia um ano qualquer e mostra se ele é BISSEXTO.
'''

##### Resolução #####

from datetime import date

print('-=-'*30)
print('Olá, seja bem-vindo(a) ao calculador de ano bissexto!')
print('Irei dizer se o ano que você escreveu é bissexto ou não.')
print('-=-'*30)

print('\n')

print('-=-'*30)
print('''Chama-se ano bissexto o ano ao qual é acrescentado um dia extra, ficando com 366 dias, um dia a mais do que os 
anos normais de 365 dias, ocorrendo a cada quatro anos (exceto anos múltiplos de 100 que não são múltiplos de 400)''')
print('-=-'*30)

### Criação das variáveis ###

ano = int(input('\nDigite o ano desejado: Coloque 0 para analisar o ano atual '))

### Condições ###

if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano de {} é bissexto!'.format(ano))
else:
    print('O ano de {} não é bissexto.'.format(ano))