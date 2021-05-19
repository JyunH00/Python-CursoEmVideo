'''
Exercício 69: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá
perguntar se o usuário quer ou nõa continuar. No final, mostre:

A) Quantas pessoas tem mais de 18 anos.
B) quantos homems foram cadastrados.
C) Quantas mulheres tem menos de 20 anos.
'''

#### Resolução ###

### Variáveis ###

idade = contadorPM = contadorH = contadorM20 = 0
sexo = ''

### Laço while ###

while True:
    print('='*50)
    print('             CADASTRE UMA PESSOA             ' )
    print('='*50)

    idade = int(input('Idade: '))

    sexo = str(input('Sexo: [M/F]: ')).upper().strip()[0]
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]: ')).upper().strip()[0]

    print('=' * 50)
    if idade >= 18:
        contadorPM += 1
    if sexo == 'M':
        contadorH += 1
    if sexo == 'F' and idade < 20:
        contadorM20 += 1

    pergunta = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    while pergunta not in 'SN':
        pergunta = str(input('Quer continuar? [S/N] ')).upper().strip()[0]

    if pergunta == 'N':
        break
print('======= FIM DO PROGRAMA =======')
print(f'Total de pessoa com mais de 18 anos: {contadorPM}')
print(f'Ao todo temos {contadorH} homems cadastrados. ')
print(f'E temos {contadorM20} mulheres com menos de 20 anos. ')

'''
Não é necessário criar as variaveis antes do laço
podemos colocar pergunta = '' antes do while.
'''