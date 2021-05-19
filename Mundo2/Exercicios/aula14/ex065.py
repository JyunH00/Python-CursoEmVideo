'''
Exercício 65: Crie um programa que leia vários números inteiros pelo teclado. No final mostre a média entre todos os
valores e qual foi o menor e o maior valor lido. O programa deve perguntar ao usuário se ele quer ou não continuar a
digitar os valores
'''

#### Resolução ####


# Variáveis #

numInt = int(input('Digite um valor inteiro: \n'))

resposta = ''
media = numInt
contador = 1

maior = numInt
menor = numInt

# Laço while #
while resposta not in 'N':
    resposta = str(input('\nQuer continuar? [S/N]: \n')).upper()
    if resposta == 'S':
        numInt = int(input('\nDigite um valor inteiro: \n'))
        media += numInt
        contador += 1
        if numInt > maior:
            maior = numInt
        if numInt < menor:
            menor = numInt
    else:
        print('Escreva uma resposta válida!')

# Prints #
media = media/ contador
print('A média dos números colocados é: {:.2f}'.format(media))
print('O maior valor colocado é: {}'.format(maior))
print('O menor valor colocado é: {}'.format(menor))