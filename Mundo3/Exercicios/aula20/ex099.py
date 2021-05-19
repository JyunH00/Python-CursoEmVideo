'''
Exercício 99: Faça um programa que tenha um função maior(), que receba vários parâmetros com valores inteiros.

Seu programa tem que analisar todos os valores e dizer qual dele é o maior.
'''

# Resolução #

from time import sleep

# Funções #

def maior(* num):
    print('-='*30)
    print('Analisando os valores passados...')

    if len(num) == 0:
        print(f'Foram analisados 0 valores ao todo.')
        print(f'O maior valor informado foi 0.')
    else:
        for i in num:
            print(i, end =' ')
            sleep(0.2)

        print(f'Foram analisados {len(num)} valores ao todo.')
        print(f'O maior valor informado foi {max(num)}.')


#Programa principal

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()