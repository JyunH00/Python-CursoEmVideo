'''
Exercício 59: Crie um programa que leia dois valores e mostre um menu na tela:
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa
'''

#### RESOLUÇÃO ####

print('-=-'*20)
print('MiNI CALCULADORA')
print('-=-'*20)

from time import sleep

##### VARIÁVEIS ####

num1 = float(input('Digite o primeiro valor: \n'))
num2 = float(input('Digite o segundo valor: \n'))

menu = 0
while menu != 5:
    print('--------- MENU --------- ')

    print('''
    [1] SOMA
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA
    ''')
    print('----------------------- ')

    menu = int(input('Escolha o que quer fazer com os dois valores: \n'))

    if menu == 1:
        soma = num1 + num2
        print('A soma dos números é {}.'.format(soma))
    elif menu == 2:
        mult = num1 * num2
        print('A multiplicação dos números é {}.'.format(mult))
    elif menu == 3:
        if num1 > num2:
            maior = num1
            print('O maior número é {}.'.format(maior))
        elif num2 > num1:
            maior = num2
            print('O maior número é {}.'.format(maior))
        else:
            maior = num1
            print('O maior número é {}., porém os dois números são iguais'.format(maior))
    elif menu == 4:
        num1 = float(input('Digite o primeiro valor novamente: \n'))
        num2 = float(input('Digite o segundo valor novamente: \n'))
    else:
        print('ESCREVA UM VALOR VÁLIDO NO MENU')
print('SAINDO DO PROGRAMA...')
sleep(3)

'''
Solução melhor!

menu = int(input('Escolha o que quer fazer com os dois valores: \n'))

while menu != 5:

    print([1] SOMA
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA    
    )
print('----------------------- ')
    if menu == 1:
        soma = num1 + num2
        print('A soma dos números é {}.'.format(soma))
    elif menu == 2:
        mult = num1 * num2
        print('A multiplicação dos números é {}.'.format(mult))
    elif menu == 3:
        if num1 > num2:
            maior = num1
            print('O maior número é {}.'.format(maior))
        elif num2 > num1:
            maior = num2
            print('O maior número é {}.'.format(maior))
        else:
            maior = num1
            print('O maior número é {}., porém os dois números são iguais'.format(maior))
    elif menu == 4:
        num1 = float(input('Digite o primeiro valor novamente: \n'))
        num2 = float(input('Digite o segundo valor novamente: \n'))
     else:
        print('ESCREVA UM VALOR VÁLIDO NO MENU')

print('SAINDO DO PROGRAMA...')
sleep(3)


'''