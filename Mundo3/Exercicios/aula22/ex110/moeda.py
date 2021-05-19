'''
Exercício 110: Adicione ao módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), que mostre na
tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.
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

def resumo(p = 0, aum = 0, desc = 0):
    print('\033[1m=' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('=' * 30)
    print(f'Preço analisado: \t{moeda(p)}')
    print(f'Dobro do preço: \t{dobro(p,True)}')
    print(f'Metade do preço: \t{metade(p, True)}')
    print(f'{aum}% de aumento: \t{aumentar(p, aum, True)}')
    print(f'{desc}% de redução: \t{diminuir(p, desc, True)}')
    print('=' * 30)

