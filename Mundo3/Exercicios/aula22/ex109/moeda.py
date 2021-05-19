'''
Exercício 109: Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais,
informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.
'''

# Resolução #

# Funções #

def moeda(p = 0, moeda = 'R$'):
    return f'{moeda}{p:>.2f}'.replace('.', ',')

def aumentar(p = 0, aum = 0, formatado = False):
    novoP = p * (1 + aum/100)

    if formatado == True:
       return moeda(novoP)
    else:
        return novoP

def diminuir(p = 0, desc = 0, formatado = False):
    novoP = p * (1 - desc/100)
    if formatado == True:
        return moeda(novoP)
    else:
        return novoP

def dobro(p = 0, formatado = False):
    novoP = p * 2
    if formatado == True:
        return moeda(novoP)
    else:
        return novoP

def metade(p = 0, formatado = False):
    novoP = p/2
    if formatado == True:
        return moeda(novoP)
    else:
        return novoP



