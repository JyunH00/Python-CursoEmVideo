'''
Exercício 108: Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os
números como um valor monetário formatado.
'''

# Resolução #

# Funções #

def aumentar(p = 0, aum = 0):
    novoP = p * (1 + aum/100)
    return novoP

def diminuir(p = 0, desc = 0):
    novoP = p * (1 - desc/100)
    return novoP

def dobro(p = 0):
    novoP = p * 2
    return novoP

def metade(p = 0):
    novoP = p/2
    return novoP

def moeda(p = 0, moeda = 'R$'):
    return f'{moeda}{p:>.2f}'.replace('.', ',')

