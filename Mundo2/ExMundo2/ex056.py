'''
Exercício 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa
mostre:

> A média de idade do grupo
> Qual o nome do homem mais velho
> Quantas mulheres têm menos de 20 anos
'''

### Resolução ###


### Criação de Variáveis ###

mIdade = 0

homemV = ''
idadeH = 0

numMulheres = 0


# Laço

for p in range(1, 5):
    print('----- {}º PESSOA -----'.format(p))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ').upper())

    mIdade += idade # Soma as Idades

    # Verifica o homem mais velho
    if sexo == 'M':
        if idade > idadeH:
            homemV = nome
            idadeH = idade

    # Conta quantas mulheres possuem menos de 20 anos
    if sexo == 'F':
        if idade < 20:
            numMulheres += 1

mIdade = mIdade/ 4 # Calcula a média

#Prints

print('A média de idade do grupo é: {} anos.'.format(mIdade))
print('O homem mais  velho do grupo com {} anos  é: {}'.format(idadeH,homemV))
print('O número de mulheres com menos de 20 anos é: {}'.format(numMulheres))

'''
Solução do vídeo um pouco diferente!
'''