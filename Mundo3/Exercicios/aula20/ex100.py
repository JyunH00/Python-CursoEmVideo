'''
Exercício 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A
primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos
os valores PARES sorteados pela função anterior.
'''


# Resolução #

from random import randint
from time import sleep

# Variaveis #

# Funções #

def sorteia():
    print('Sorteando 5 valores da lista:', end=' ')
    for i in range(0, 5):
        numeros.append(randint(1, 10))
        print(numeros[i], end=' ')
        sleep(0.3)
    print('PRONTO!')

def somaPar():
    soma = 0
    for valorN in numeros:
        if valorN % 2 == 0:
            soma += valorN
    print(f'Somando os valores pares de {numeros}, temos {soma}. ')


#Programa principal
numeros = []
sorteia()
somaPar()