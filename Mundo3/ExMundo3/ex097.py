'''
Exercício 97: Faça um programa que tenha uma função chamada escreva() que receba um texto qualquer como parâmetro e
mostre uma mensagem com tamanho adaptável.

Ex:
escreva('Olá, mundo!')

Saída:
-----------------
    Olá, mundo!
-----------------
'''

# Resolução #

# Funções #

def escreva(a):
    tamanho = len(a)
    print('-' * 2 * tamanho)
    print(f'{a:^{tamanho*2}}')
    print('-' * 2 * tamanho)


#Programa Principal

escreva('Gustavo Guanabara')
escreva('Curso de Python!')
escreva('CeV')