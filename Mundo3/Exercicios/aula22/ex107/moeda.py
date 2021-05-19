'''
Exercício 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e
metade().

Faça também um programa que importe esse módulo e use algumas dessas funções
'''

# Resolução #

# Funções #

def aumentar(p, aum):
    novoP = p * (1 + aum/100)
    return novoP

def diminuir(p, desc):
    novoP = p * (1 - desc/100)
    return novoP

def dobro(p):
    novoP = p * 2
    return novoP

def metade(p):
    novoP = p/2
    return novoP