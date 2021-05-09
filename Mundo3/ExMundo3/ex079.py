'''
Exercício 79: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista
Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados,
em ordem crescente.
'''

#### Resolução ####

#### Variáveis ####

numLista = [] # numLista = list()

#### Laço ####
while True:
    valorAd = int(input('Digite um valor: '))
    if valorAd not in numLista: # Verifica se o valor já existe na lista
        numLista.append(valorAd)
        print('Valor adicionado com sucesso...')
    else:
        print(('Valor duplicado! Não vou adicionar...'))

    resposta = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N]')).strip().upper()[0]

    if resposta in 'N':
        break

#### Prints #####
print('-=-'*20)
numLista.sort() # Deixa a lista em ordem crescente
print(f'Você digitou os valores {numLista}')

