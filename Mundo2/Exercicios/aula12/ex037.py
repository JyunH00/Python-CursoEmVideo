'''
Exercício 37: Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de
conversão:
> 1 para binário
> 2 para octal
> 3 para hexadecimal
'''

##### Resolução #####

cores = {'finaliza':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'vermelho':'\033[31m'}

print('-=-'*30)
print('====Conversor de bases====')
print('Escolha {}[1]{} para {}binário{}'.format(cores['azul'], cores['finaliza'], cores['azul'], cores['finaliza']))
print('Escolha {}[2]{} para {}octal{}'.format(cores['amarelo'], cores['finaliza'], cores['amarelo'], cores['finaliza']))
print('Escolha {}[3]{} para {}hexadecimal{}'.format(cores['vermelho'], cores['finaliza'], cores['vermelho'], cores['finaliza']))
print('-=-'*30)


### Criação das variáveis ###

numInt = int(input('\nEscreva o número inteiro: '))

tipoCon = int(input('Escreva qual a base de conversão: '))

### Condições ###

if tipoCon == 1:
    print('Você escolheu a conversão para {}binário{}'.format(cores['azul'], cores['finaliza']))
    numB = bin(numInt)[2:]
    print('O valor {} em binário é {}{}{}'.format(numInt, cores['azul'], numB, cores['finaliza'] ))
elif tipoCon == 2:
    print('Você escolheu a conversão para {}octal{}'.format(cores['amarelo'],cores['finaliza']))
    numO = oct(numInt)[2:]
    print('O valor {} em octal é {}{}{}'.format(numInt, cores['amarelo'], numO, cores['finaliza']))
elif tipoCon == 3:
    print('Você escolheu a conversão para {}hexadecimal{}'.format(cores['vermelho'], cores['finaliza']))
    numH = hex(numInt)[2:]
    print('O valor {} em hexadecimal é {}{}{}'.format(numInt, cores['vermelho'], numH, cores['finaliza']))
else:
    print('{}COLOQUE UM VALOR ENTRE VÁLIDO ENTRE 1 E 3 PARA CONVERSÃO{}'.format(cores['vermelho'], cores['finaliza']))