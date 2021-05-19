'''
Exercício 98: Faça um programa que tenha uma função chamada contador() que receba três parâmetros: início, fim e passo e
realize a contagem.

Seu programa tem que realizar três contagens através da função criada:

a) De 1 até 10, de 1 em 1
b) De 10 até 0, de 2 em 2
c) Uma contagem personalizada
'''

# Resolução #

from time import sleep

# Funções #

def contador(ini, fim, passo):

    if passo == 0:
        passo = 1
    if ini > fim and passo > 0:
        passo *= -1

    print('-=' * 20)
    if passo > 0:
        print(f'Contagem de {ini} até {fim} de {passo} em {passo}')
    elif passo < 0:
        print(f'Contagem de {ini} até {fim} de {-passo} em {-passo}')

    if ini <= fim:
        for i in range(ini, (fim + 1), passo):
            print(i, end=' ')
            sleep(0.3)
        print('FIM!')
        print('-=' * 20)
    elif ini >= fim:
        for i in range(ini, (fim - 1), passo):
            print(i, end=' ')
            sleep(0.3)
        print('FIM!')
        print('-=' * 20)



#Programa principal

contador(1, 10, 1)
contador(10, 0, 2)

print('Agora é sua vez de personalizar a contagem!')

ini = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

contador(ini, fim, passo)