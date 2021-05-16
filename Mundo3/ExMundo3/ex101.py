'''
Exercício 101: Crie um programa que tenha uma função chamada voto() que vai recever como parâmetro o ano de nascimento
de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições
'''

# Resolução #

from datetime import date

# Funções #

def voto(ano):
    anoA = date.today().year
    idade = anoA - ano

    if idade < 0:
        return 'COLOQUE UM ANO DE NASCIMENTO VÁLIDO!'
    elif 0 <= idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    elif 16 <= idade < 18:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    elif 18 <= idade <= 65:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'
    else:
        return f'Com {idade} anos: VOTO OPCIONAL.'

#Programa Principal

anoN = int(input('Em que ano você nasceu? '))

print(voto(anoN))