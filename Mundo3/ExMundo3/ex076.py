'''
Exercício 76: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços na sequência.
No final, mostre uma listagem de preços, organizandos os dados em forma tabular
'''


#### Resolução ####

#### Variáveis ####
prodPrecos = ('Lápis', 1.75,
              'Borracha', 2.00,
              'Caderno', 15.90,
              'Estojo', 25.00,
              'Transferidor', '4.20',
              'Compasso', 9.99,
              'Mochila', 120.32,
              'Canetas', 22.30,
              'Livro', 34.90,
              'Régua', 3.99,
              'Lapiseira', 5.99)

print('\033[1m-\033[m' * 60)
ListP = 'LISTAGEM DE PREÇOS'
print('\033[1;31m{:^60}\033[m'.format(ListP))
print('\033[1m-\033[m' * 60)

for pos, i in enumerate(prodPrecos):
    if pos % 2 == 0:
        print(f'\033[1m{i:.<50}', end = '')
    else:
        print(f'R$ {float(i):>6.2f}')
print('\033[1m-\033[m' * 60)